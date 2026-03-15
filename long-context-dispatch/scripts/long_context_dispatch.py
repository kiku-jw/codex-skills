#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import secrets
import signal
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


DEFAULT_JOB_ROOT = Path.home() / ".codex" / "tmp" / "long-context-jobs"
DEFAULT_LAUNCHER = Path("/Users/nick/.local/bin/codex-long")
DEFAULT_TIMEOUT_SECONDS = 45 * 60
DEFAULT_PROGRESS_INTERVAL_SECONDS = 15
TERMINAL_STATES = {"succeeded", "failed", "timed_out"}
RESULT_SECTIONS = [
    "Executive Summary",
    "Key Findings",
    "Cross-Document / Cross-File Connections",
    "Recommended Next Actions",
    "Open Questions",
]


def utc_now() -> str:
    return (
        datetime.now(timezone.utc)
        .replace(microsecond=0)
        .isoformat()
        .replace("+00:00", "Z")
    )


def make_job_id() -> str:
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    return f"lc-{timestamp}-{secrets.token_hex(4)}"


def ensure_dir(path: Path) -> Path:
    path.mkdir(parents=True, exist_ok=True)
    return path


def read_text_argument(
    *,
    text: str | None,
    file_path: str | None,
    name: str,
    required: bool,
    default: str | None = None,
) -> str:
    if text:
        return text.strip()
    if file_path:
        if file_path == "-":
            value = sys.stdin.read().strip()
        else:
            value = Path(file_path).expanduser().read_text(encoding="utf-8").strip()
        if value:
            return value
    if default is not None:
        return default
    if required:
        raise ValueError(f"Missing required {name}.")
    return ""


def write_text(path: Path, content: str) -> None:
    path.write_text(content, encoding="utf-8")


def write_json(path: Path, payload: dict[str, Any]) -> None:
    tmp_path = path.with_suffix(path.suffix + ".tmp")
    tmp_path.write_text(
        json.dumps(payload, ensure_ascii=True, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    tmp_path.replace(path)


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def emit_json(payload: dict[str, Any]) -> None:
    sys.stdout.write(json.dumps(payload, ensure_ascii=True) + "\n")
    sys.stdout.flush()


def append_log(log_path: Path, message: str) -> None:
    with log_path.open("a", encoding="utf-8") as handle:
        handle.write(f"[{utc_now()}] {message}\n")


def truncate(text: str, limit: int = 160) -> str:
    single_line = " ".join(text.split())
    if len(single_line) <= limit:
        return single_line
    return single_line[: limit - 3] + "..."


def is_pid_running(pid: int | None) -> bool:
    if not pid:
        return False
    try:
        os.kill(pid, 0)
    except ProcessLookupError:
        return False
    except PermissionError:
        return True
    return True


def kill_process_group(pid: int | None, log_path: Path | None = None) -> None:
    if not pid:
        return
    try:
        os.killpg(pid, signal.SIGTERM)
        deadline = time.time() + 3
        while time.time() < deadline:
            if not is_pid_running(pid):
                return
            time.sleep(0.1)
        os.killpg(pid, signal.SIGKILL)
    except ProcessLookupError:
        return
    except Exception as exc:  # pragma: no cover - best effort cleanup
        if log_path:
            append_log(log_path, f"Failed to terminate process group {pid}: {exc}")


def stderr_tail(stderr_path: Path, line_count: int = 20) -> str:
    if not stderr_path.exists():
        return ""
    lines = stderr_path.read_text(encoding="utf-8", errors="replace").splitlines()
    if not lines:
        return ""
    return "\n".join(lines[-line_count:])


def job_paths(job_dir: Path) -> dict[str, Path]:
    return {
        "job_dir": job_dir,
        "request": job_dir / "request.md",
        "prompt": job_dir / "prompt.md",
        "status": job_dir / "status.json",
        "events": job_dir / "events.jsonl",
        "result": job_dir / "result.md",
        "stderr": job_dir / "stderr.log",
        "dispatcher_log": job_dir / "dispatcher.log",
    }


def build_prompt(*, request_text: str, reason: str, scope: str, cwd: Path) -> str:
    sections = "\n".join(f"- {section}" for section in RESULT_SECTIONS)
    return f"""# Long-Context Child Worker

You are the already-launched child worker for a long-context dispatch.
The routing decision has already been made by the parent agent.
Do not re-evaluate whether long context is needed.
Do not invoke `long-context-dispatch` again.
Do not ask for confirmation.
Do not suggest switching to another session or app.

## Task Objective

{request_text}

## Why Long Context Was Chosen

{reason}

## Workspace / Corpus Scope

- Working directory: `{cwd}`
- Scope notes: {scope}

## Required Output Shape

Produce Markdown with exactly these top-level sections:
{sections}

## Constraints

- Operate in read-only mode.
- Do not edit files, write patches, or change the workspace.
- Use shell commands only for inspection and evidence gathering.
- If the task is code-focused, return findings and an implementation brief only.
- Make cross-document and cross-file relationships explicit.
- Cite concrete file paths, document names, or corpus segments when they materially support a finding.
"""


def parse_events(events_path: Path) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    events: list[dict[str, Any]] = []
    malformed: list[dict[str, Any]] = []
    if not events_path.exists():
        return events, malformed
    for line_number, raw_line in enumerate(
        events_path.read_text(encoding="utf-8", errors="replace").splitlines(),
        start=1,
    ):
        line = raw_line.strip()
        if not line:
            continue
        try:
            payload = json.loads(line)
        except json.JSONDecodeError:
            malformed.append(
                {
                    "line": line_number,
                    "preview": truncate(line, 200),
                }
            )
            continue
        if isinstance(payload, dict):
            events.append(payload)
    return events, malformed


def extract_thread_id(events: list[dict[str, Any]]) -> str | None:
    for event in events:
        if event.get("type") == "thread.started":
            thread_id = event.get("thread_id")
            if isinstance(thread_id, str) and thread_id:
                return thread_id
    return None


def summarize_progress(
    events: list[dict[str, Any]], malformed: list[dict[str, Any]]
) -> dict[str, Any]:
    summary = "Child worker queued."
    event_type = "queued"
    for event in reversed(events):
        event_type = str(event.get("type", "unknown"))
        if event_type == "item.started":
            item = event.get("item") or {}
            if item.get("type") == "command_execution":
                summary = f"Running command: {truncate(str(item.get('command', '')))}"
                break
        if event_type == "item.completed":
            item = event.get("item") or {}
            item_type = item.get("type")
            if item_type == "command_execution":
                exit_code = item.get("exit_code")
                summary = (
                    f"Completed command (exit {exit_code}): "
                    f"{truncate(str(item.get('command', '')))}"
                )
                break
            if item_type == "agent_message":
                summary = "Child worker produced an analysis message."
                break
        if event_type == "turn.started":
            summary = "Child worker turn started."
            break
        if event_type == "turn.completed":
            summary = "Child worker turn completed."
            break
        if event_type == "thread.started":
            summary = "Child worker thread created."
            break

    if malformed:
        summary = f"{summary} ({len(malformed)} malformed event line(s) recorded.)"

    return {
        "last_event_type": event_type,
        "last_progress": summary,
        "malformed_event_lines": len(malformed),
    }


def extract_event_error(events: list[dict[str, Any]]) -> str | None:
    for event in reversed(events):
        if event.get("type") == "turn.failed":
            error = event.get("error") or {}
            message = error.get("message")
            if isinstance(message, str) and message.strip():
                return message.strip()
        if event.get("type") == "error":
            message = event.get("message")
            if isinstance(message, str) and message.strip():
                return message.strip()
    return None


def find_rollout_path(thread_id: str | None) -> Path | None:
    if not thread_id:
        return None
    sessions_root = Path.home() / ".codex" / "sessions"
    matches = sorted(sessions_root.rglob(f"*{thread_id}*.jsonl"))
    return matches[0] if matches else None


def extract_model_context_window(rollout_path: Path | None) -> int | None:
    if not rollout_path or not rollout_path.exists():
        return None
    with rollout_path.open("r", encoding="utf-8", errors="replace") as handle:
        for raw_line in handle:
            try:
                event = json.loads(raw_line)
            except json.JSONDecodeError:
                continue
            payload = event.get("payload") or {}
            payload_type = payload.get("type")
            if payload_type == "task_started":
                value = payload.get("model_context_window")
                if isinstance(value, int):
                    return value
            if payload_type == "token_count":
                info = payload.get("info") or {}
                value = info.get("model_context_window")
                if isinstance(value, int):
                    return value
    return None


def load_status(job_dir: Path) -> dict[str, Any]:
    return read_json(job_paths(job_dir)["status"])


def save_status(job_dir: Path, status: dict[str, Any]) -> None:
    write_json(job_paths(job_dir)["status"], status)


def resolve_job_dir(args: argparse.Namespace) -> Path:
    if getattr(args, "job_dir", None):
        return Path(args.job_dir).expanduser().resolve()
    job_id = getattr(args, "job_id", None)
    if not job_id:
        raise ValueError("Either --job-id or --job-dir is required.")
    return Path(args.job_root).expanduser().resolve() / job_id


def build_summary(job_dir: Path) -> dict[str, Any]:
    paths = job_paths(job_dir)
    status = load_status(job_dir)
    events, malformed = parse_events(paths["events"])
    progress = summarize_progress(events, malformed)
    thread_id = extract_thread_id(events)
    rollout_path = find_rollout_path(thread_id)
    model_context_window = extract_model_context_window(rollout_path)
    result_preview = ""
    if paths["result"].exists():
        result_preview = truncate(paths["result"].read_text(encoding="utf-8", errors="replace"), 400)
    summary = dict(status)
    summary.update(progress)
    summary["thread_id"] = thread_id
    summary["session_rollout_path"] = str(rollout_path) if rollout_path else None
    summary["model_context_window"] = model_context_window
    summary["event_error"] = extract_event_error(events)
    summary["stderr_tail"] = stderr_tail(paths["stderr"])
    summary["result_preview"] = result_preview
    summary["job_dir"] = str(job_dir)
    return summary


def finalize_job(
    *,
    job_dir: Path,
    state: str,
    exit_code: int | None,
    error_summary: str | None,
) -> dict[str, Any]:
    paths = job_paths(job_dir)
    status = load_status(job_dir)
    summary = build_summary(job_dir)
    result_text = ""
    if paths["result"].exists():
        result_text = paths["result"].read_text(encoding="utf-8", errors="replace").strip()
    if state == "succeeded" and not result_text:
        state = "failed"
        error_summary = "Child finished without writing a non-empty result.md."
    if state == "failed" and not error_summary:
        event_error = summary.get("event_error")
        if event_error:
            error_summary = event_error
        elif exit_code is not None:
            error_summary = f"Child exited with code {exit_code}."
        else:
            error_summary = "Child failed without a captured exit code."
    status.update(
        {
            "state": state,
            "finished_at": utc_now(),
            "exit_code": exit_code,
            "error_summary": error_summary,
        }
    )
    save_status(job_dir, status)
    summary = build_summary(job_dir)
    warning_summary = None
    if summary.get("malformed_event_lines"):
        warning_summary = (
            f"Event log contains {summary['malformed_event_lines']} malformed line(s)."
        )
    status = load_status(job_dir)
    status["last_event_type"] = summary["last_event_type"]
    status["last_progress"] = summary["last_progress"]
    status["thread_id"] = summary.get("thread_id")
    status["session_rollout_path"] = summary.get("session_rollout_path")
    status["model_context_window"] = summary.get("model_context_window")
    status["malformed_event_lines"] = summary.get("malformed_event_lines")
    if warning_summary:
        status["warning_summary"] = warning_summary
        summary["warning_summary"] = warning_summary
    save_status(job_dir, status)
    return summary


def create_initial_status(
    *,
    job_id: str,
    cwd: Path,
    paths: dict[str, Path],
    launcher: Path,
    timeout_seconds: int,
) -> dict[str, Any]:
    return {
        "job_id": job_id,
        "state": "queued",
        "pid": None,
        "monitor_pid": None,
        "cwd": str(cwd),
        "started_at": None,
        "finished_at": None,
        "exit_code": None,
        "result_path": str(paths["result"]),
        "events_path": str(paths["events"]),
        "error_summary": None,
        "prompt_path": str(paths["prompt"]),
        "request_path": str(paths["request"]),
        "stderr_path": str(paths["stderr"]),
        "dispatcher_log_path": str(paths["dispatcher_log"]),
        "launcher_path": str(launcher),
        "timeout_seconds": timeout_seconds,
        "last_event_type": "queued",
        "last_progress": "Child worker queued.",
    }


def create_job(
    *,
    job_root: Path,
    job_id: str | None,
    cwd: Path,
    request_text: str,
    reason: str,
    scope: str,
    launcher: Path,
    timeout_seconds: int,
) -> tuple[Path, dict[str, Any]]:
    ensure_dir(job_root)
    final_job_id = job_id or make_job_id()
    job_dir = ensure_dir(job_root / final_job_id)
    paths = job_paths(job_dir)
    write_text(paths["request"], request_text + "\n")
    write_text(
        paths["prompt"],
        build_prompt(
            request_text=request_text,
            reason=reason,
            scope=scope,
            cwd=cwd,
        ),
    )
    status = create_initial_status(
        job_id=final_job_id,
        cwd=cwd,
        paths=paths,
        launcher=launcher,
        timeout_seconds=timeout_seconds,
    )
    save_status(job_dir, status)
    return job_dir, status


def start_monitor(
    *,
    job_dir: Path,
    timeout_seconds: int,
    progress_interval_seconds: int,
) -> int:
    paths = job_paths(job_dir)
    command = [
        sys.executable,
        str(Path(__file__).resolve()),
        "monitor",
        "--job-dir",
        str(job_dir),
        "--timeout-seconds",
        str(timeout_seconds),
        "--progress-interval-seconds",
        str(progress_interval_seconds),
    ]
    with paths["dispatcher_log"].open("a", encoding="utf-8") as log_handle:
        proc = subprocess.Popen(
            command,
            stdout=log_handle,
            stderr=log_handle,
            stdin=subprocess.DEVNULL,
            start_new_session=True,
        )
    status = load_status(job_dir)
    status["monitor_pid"] = proc.pid
    save_status(job_dir, status)
    return proc.pid


def command_start(args: argparse.Namespace) -> int:
    cwd = Path(args.cwd).expanduser().resolve()
    if not cwd.exists():
        raise FileNotFoundError(f"Working directory does not exist: {cwd}")
    request_text = read_text_argument(
        text=args.request,
        file_path=args.request_file,
        name="request",
        required=True,
    )
    reason = read_text_argument(
        text=args.reason,
        file_path=args.reason_file,
        name="reason",
        required=True,
    )
    scope = read_text_argument(
        text=args.scope,
        file_path=args.scope_file,
        name="scope",
        required=False,
        default=f"Inspect material reachable under `{cwd}`.",
    )
    launcher = Path(args.launcher).expanduser().resolve()
    job_root = Path(args.job_root).expanduser().resolve()
    job_dir, status = create_job(
        job_root=job_root,
        job_id=args.job_id,
        cwd=cwd,
        request_text=request_text,
        reason=reason,
        scope=scope,
        launcher=launcher,
        timeout_seconds=args.timeout_seconds,
    )
    args.job_id = status["job_id"]
    if not launcher.exists():
        failed = finalize_job(
            job_dir=job_dir,
            state="failed",
            exit_code=None,
            error_summary=f"Launcher not found: {launcher}",
        )
        emit_json({"event": "terminal", **failed})
        return 1

    monitor_pid = start_monitor(
        job_dir=job_dir,
        timeout_seconds=args.timeout_seconds,
        progress_interval_seconds=args.progress_interval_seconds,
    )
    append_log(job_paths(job_dir)["dispatcher_log"], f"Monitor started with pid {monitor_pid}.")

    deadline = time.time() + 2
    while time.time() < deadline:
        current_status = load_status(job_dir)
        if current_status.get("state") in {"running", "failed", "timed_out", "succeeded"}:
            break
        time.sleep(0.1)

    summary = build_summary(job_dir)
    emit_json({"event": "started", **summary})
    return 0


def command_monitor(args: argparse.Namespace) -> int:
    job_dir = Path(args.job_dir).expanduser().resolve()
    paths = job_paths(job_dir)
    status = load_status(job_dir)
    launcher = Path(status["launcher_path"]).expanduser().resolve()
    cwd = Path(status["cwd"]).expanduser().resolve()
    timeout_seconds = int(status.get("timeout_seconds") or args.timeout_seconds)
    log_path = paths["dispatcher_log"]
    child_proc: subprocess.Popen[str] | None = None
    interrupted = False

    def handle_interrupt(signum: int, _frame: Any) -> None:
        nonlocal interrupted
        interrupted = True
        append_log(log_path, f"Received signal {signum}; stopping child.")
        if child_proc is not None:
            kill_process_group(child_proc.pid, log_path)

    signal.signal(signal.SIGTERM, handle_interrupt)
    signal.signal(signal.SIGINT, handle_interrupt)

    if not launcher.exists():
        append_log(log_path, f"Launcher missing: {launcher}")
        finalize_job(
            job_dir=job_dir,
            state="failed",
            exit_code=None,
            error_summary=f"Launcher not found: {launcher}",
        )
        return 1

    prompt_text = paths["prompt"].read_text(encoding="utf-8")
    child_command = [
        str(launcher),
        "-a",
        "never",
        "exec",
        "--sandbox",
        "read-only",
        "--json",
        "-C",
        str(cwd),
        "--skip-git-repo-check",
        "-o",
        str(paths["result"]),
        prompt_text,
    ]
    append_log(log_path, f"Launching child command in {cwd}: {truncate(' '.join(child_command), 320)}")

    try:
        with paths["events"].open("w", encoding="utf-8") as events_handle, paths["stderr"].open(
            "w", encoding="utf-8"
        ) as stderr_handle:
            child_proc = subprocess.Popen(
                child_command,
                cwd=str(cwd),
                stdout=events_handle,
                stderr=stderr_handle,
                stdin=subprocess.DEVNULL,
                text=True,
                start_new_session=True,
            )
    except OSError as exc:
        append_log(log_path, f"Spawn failure: {exc}")
        finalize_job(
            job_dir=job_dir,
            state="failed",
            exit_code=None,
            error_summary=f"Failed to start child process: {exc}",
        )
        return 1

    status.update(
        {
            "state": "running",
            "pid": child_proc.pid,
            "started_at": utc_now(),
            "finished_at": None,
            "exit_code": None,
            "error_summary": None,
        }
    )
    save_status(job_dir, status)
    append_log(log_path, f"Child started with pid {child_proc.pid}.")

    deadline = time.time() + timeout_seconds
    next_status_refresh = 0.0

    while True:
        if interrupted:
            summary = finalize_job(
                job_dir=job_dir,
                state="failed",
                exit_code=None,
                error_summary="interrupted_by_parent",
            )
            append_log(log_path, "Job interrupted by parent.")
            return 1 if summary["state"] != "succeeded" else 0

        exit_code = child_proc.poll()
        now = time.time()

        if exit_code is not None:
            state = "succeeded" if exit_code == 0 else "failed"
            error_summary = None
            if state == "failed":
                error_summary = stderr_tail(paths["stderr"]) or f"Child exited with code {exit_code}."
            summary = finalize_job(
                job_dir=job_dir,
                state=state,
                exit_code=exit_code,
                error_summary=error_summary,
            )
            append_log(log_path, f"Child exited with code {exit_code}. Final state: {summary['state']}.")
            return 0 if summary["state"] == "succeeded" else 1

        if now >= deadline:
            append_log(log_path, f"Job timed out after {timeout_seconds} seconds.")
            kill_process_group(child_proc.pid, log_path)
            finalize_job(
                job_dir=job_dir,
                state="timed_out",
                exit_code=None,
                error_summary=f"Timed out after {timeout_seconds} seconds.",
            )
            return 1

        if now >= next_status_refresh:
            summary = build_summary(job_dir)
            status = load_status(job_dir)
            status["last_event_type"] = summary["last_event_type"]
            status["last_progress"] = summary["last_progress"]
            status["thread_id"] = summary.get("thread_id")
            status["session_rollout_path"] = summary.get("session_rollout_path")
            status["model_context_window"] = summary.get("model_context_window")
            status["warning_summary"] = summary.get("warning_summary")
            status["malformed_event_lines"] = summary.get("malformed_event_lines")
            save_status(job_dir, status)
            next_status_refresh = now + args.progress_interval_seconds

        time.sleep(1)


def command_status(args: argparse.Namespace) -> int:
    job_dir = resolve_job_dir(args)
    summary = build_summary(job_dir)
    emit_json({"event": "status", **summary})
    return 0


def command_cancel(args: argparse.Namespace) -> int:
    job_dir = resolve_job_dir(args)
    status = load_status(job_dir)
    if status.get("state") in TERMINAL_STATES:
        summary = build_summary(job_dir)
        emit_json({"event": "terminal", **summary})
        return 0 if summary["state"] == "succeeded" else 1
    log_path = job_paths(job_dir)["dispatcher_log"]
    kill_process_group(status.get("pid"), log_path)
    monitor_pid = status.get("monitor_pid")
    if monitor_pid and is_pid_running(monitor_pid):
        kill_process_group(monitor_pid, log_path)
    summary = finalize_job(
        job_dir=job_dir,
        state="failed",
        exit_code=None,
        error_summary="interrupted_by_parent",
    )
    append_log(log_path, "Job cancelled by parent.")
    emit_json({"event": "terminal", **summary})
    return 1


def command_wait(args: argparse.Namespace) -> int:
    job_dir = resolve_job_dir(args)
    seen_progress: str | None = None
    try:
        while True:
            summary = build_summary(job_dir)
            progress = summary.get("last_progress")
            if progress != seen_progress:
                emit_json(
                    {
                        "event": "progress",
                        "job_id": summary["job_id"],
                        "state": summary["state"],
                        "summary": progress,
                        "thread_id": summary.get("thread_id"),
                    }
                )
                seen_progress = progress
            if summary["state"] in TERMINAL_STATES:
                emit_json({"event": "terminal", **summary})
                return 0 if summary["state"] == "succeeded" else 1
            time.sleep(args.progress_interval_seconds)
    except KeyboardInterrupt:
        return command_cancel(args)


def command_run(args: argparse.Namespace) -> int:
    start_code = command_start(args)
    if start_code != 0:
        return start_code
    wait_args = argparse.Namespace(
        job_id=args.job_id,
        job_dir=None,
        job_root=args.job_root,
        progress_interval_seconds=args.progress_interval_seconds,
    )
    return command_wait(wait_args)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Dispatch a long-context Codex worker and manage its job artifacts."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    def add_job_locator_arguments(target: argparse.ArgumentParser) -> None:
        target.add_argument("--job-id", help="Existing job id under the job root.")
        target.add_argument("--job-dir", help="Absolute path to an existing job directory.")
        target.add_argument(
            "--job-root",
            default=str(DEFAULT_JOB_ROOT),
            help=f"Job root directory. Defaults to {DEFAULT_JOB_ROOT}.",
        )

    def add_common_start_arguments(target: argparse.ArgumentParser) -> None:
        target.add_argument("--cwd", required=True, help="Workspace or corpus root to inspect.")
        target.add_argument("--request", help="Direct request text.")
        target.add_argument("--request-file", help="Path to request Markdown or text.")
        target.add_argument("--reason", help="Why long context is warranted.")
        target.add_argument("--reason-file", help="Path to reason text.")
        target.add_argument("--scope", help="Scope notes for the child worker.")
        target.add_argument("--scope-file", help="Path to scope text.")
        target.add_argument(
            "--launcher",
            default=str(DEFAULT_LAUNCHER),
            help=f"Path to the verified long-context launcher. Defaults to {DEFAULT_LAUNCHER}.",
        )
        target.add_argument(
            "--timeout-seconds",
            type=int,
            default=DEFAULT_TIMEOUT_SECONDS,
            help=f"Job timeout. Defaults to {DEFAULT_TIMEOUT_SECONDS}.",
        )
        target.add_argument(
            "--progress-interval-seconds",
            type=int,
            default=DEFAULT_PROGRESS_INTERVAL_SECONDS,
            help=f"Polling interval for progress refresh. Defaults to {DEFAULT_PROGRESS_INTERVAL_SECONDS}.",
        )
        target.add_argument(
            "--job-root",
            default=str(DEFAULT_JOB_ROOT),
            help=f"Job root directory. Defaults to {DEFAULT_JOB_ROOT}.",
        )
        target.add_argument("--job-id", help="Optional explicit job id.")

    start_parser = subparsers.add_parser("start", help="Create a job and launch a detached monitor.")
    add_common_start_arguments(start_parser)
    start_parser.set_defaults(func=command_start)

    monitor_parser = subparsers.add_parser("monitor", help=argparse.SUPPRESS)
    monitor_parser.add_argument("--job-dir", required=True, help="Absolute path to the job directory.")
    monitor_parser.add_argument(
        "--timeout-seconds",
        type=int,
        default=DEFAULT_TIMEOUT_SECONDS,
        help=argparse.SUPPRESS,
    )
    monitor_parser.add_argument(
        "--progress-interval-seconds",
        type=int,
        default=DEFAULT_PROGRESS_INTERVAL_SECONDS,
        help=argparse.SUPPRESS,
    )
    monitor_parser.set_defaults(func=command_monitor)

    wait_parser = subparsers.add_parser("wait", help="Wait for a job to finish and emit JSON progress.")
    add_job_locator_arguments(wait_parser)
    wait_parser.add_argument(
        "--progress-interval-seconds",
        type=int,
        default=DEFAULT_PROGRESS_INTERVAL_SECONDS,
        help=f"Polling interval for user-facing progress. Defaults to {DEFAULT_PROGRESS_INTERVAL_SECONDS}.",
    )
    wait_parser.set_defaults(func=command_wait)

    status_parser = subparsers.add_parser("status", help="Read the current job status.")
    add_job_locator_arguments(status_parser)
    status_parser.set_defaults(func=command_status)

    cancel_parser = subparsers.add_parser("cancel", help="Cancel a running job.")
    add_job_locator_arguments(cancel_parser)
    cancel_parser.set_defaults(func=command_cancel)

    run_parser = subparsers.add_parser("run", help="Start a job, then wait with JSON progress.")
    add_common_start_arguments(run_parser)
    run_parser.set_defaults(func=command_run)

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    try:
        return args.func(args)
    except Exception as exc:
        emit_json({"event": "error", "error": str(exc)})
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
