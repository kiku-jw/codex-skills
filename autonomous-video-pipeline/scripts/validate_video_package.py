#!/usr/bin/env python3
"""Validate a video package manifest and final-delivery evidence."""

import argparse
import json
import sys
from pathlib import Path


IMAGE_SUFFIXES = {".jpg", ".jpeg", ".png", ".webp"}


def load_manifest(path: Path) -> dict[str, object]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        raise ValueError(f"manifest is not valid JSON: {error}") from error
    if not isinstance(data, dict):
        raise ValueError("manifest root must be an object")
    return data


def nested(data: dict[str, object], keys: list[str]) -> object:
    current: object = data
    for key in keys:
        if not isinstance(current, dict) or key not in current:
            return None
        current = current[key]
    return current


def resolve(project_dir: Path, value: object) -> Path | None:
    if not isinstance(value, str) or not value:
        return None
    path = Path(value)
    if path.is_absolute():
        return path
    return project_dir / path


def check_path(project_dir: Path, value: object, label: str, final: bool, failures: list[str], warnings: list[str]) -> Path | None:
    path = resolve(project_dir, value)
    if path is None:
        (failures if final else warnings).append(f"{label} is not set")
        return None
    if not path.exists():
        (failures if final else warnings).append(f"{label} does not exist: {path}")
        return path
    if path.is_file() and path.stat().st_size == 0:
        (failures if final else warnings).append(f"{label} is empty: {path}")
    return path


def validate(manifest_path: Path, final: bool) -> dict[str, object]:
    manifest = load_manifest(manifest_path)
    project_dir = manifest_path.parent
    failures: list[str] = []
    warnings: list[str] = []

    for key in ("title", "target", "production_contract", "script", "render", "qa"):
        if key not in manifest:
            failures.append(f"missing top-level key: {key}")

    acceptance = nested(manifest, ["production_contract", "acceptance_criteria"])
    if not isinstance(acceptance, list) or not acceptance:
        warnings.append("production_contract.acceptance_criteria is empty")

    sources = manifest.get("sources")
    if not isinstance(sources, list):
        failures.append("sources must be a list")
    elif final and not sources:
        warnings.append("sources is empty; factual claims may be untraceable")

    script_path = check_path(project_dir, nested(manifest, ["script", "path"]), "script.path", final, failures, warnings)
    chunks_path = check_path(project_dir, nested(manifest, ["script", "chunks_manifest"]), "script.chunks_manifest", final, failures, warnings)
    scene_manifest = check_path(project_dir, nested(manifest, ["storyboard", "scene_manifest"]), "storyboard.scene_manifest", False, failures, warnings)
    final_mp4 = check_path(project_dir, nested(manifest, ["render", "final_mp4"]), "render.final_mp4", final, failures, warnings)
    ffprobe = check_path(project_dir, nested(manifest, ["qa", "ffprobe"]), "qa.ffprobe", final, failures, warnings)
    frames_dir = resolve(project_dir, nested(manifest, ["qa", "frames_dir"]))

    frame_count = 0
    if frames_dir is None:
        (failures if final else warnings).append("qa.frames_dir is not set")
    elif not frames_dir.exists():
        (failures if final else warnings).append(f"qa.frames_dir does not exist: {frames_dir}")
    elif not frames_dir.is_dir():
        failures.append(f"qa.frames_dir is not a directory: {frames_dir}")
    else:
        frame_count = sum(1 for path in frames_dir.iterdir() if path.suffix.lower() in IMAGE_SUFFIXES)
        if final and frame_count == 0:
            failures.append(f"qa.frames_dir has no QA images: {frames_dir}")

    limitations = nested(manifest, ["qa", "limitations"])
    if limitations is not None and not isinstance(limitations, list):
        failures.append("qa.limitations must be a list when present")

    checks = nested(manifest, ["qa", "checks"])
    if final and (not isinstance(checks, list) or not checks):
        warnings.append("qa.checks is empty; record manual visual review notes")

    return {
        "manifest": str(manifest_path),
        "final_mode": final,
        "ok": not failures,
        "failures": failures,
        "warnings": warnings,
        "paths": {
            "script": str(script_path) if script_path else None,
            "chunks": str(chunks_path) if chunks_path else None,
            "scene_manifest": str(scene_manifest) if scene_manifest else None,
            "final_mp4": str(final_mp4) if final_mp4 else None,
            "ffprobe": str(ffprobe) if ffprobe else None,
            "frames_dir": str(frames_dir) if frames_dir else None,
        },
        "qa_frame_count": frame_count,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", help="Path to video-manifest.json.")
    parser.add_argument("--final", action="store_true", help="Require final MP4 and QA evidence.")
    parser.add_argument("--out", help="Write validation JSON to this path.")
    args = parser.parse_args()

    manifest_path = Path(args.manifest)
    if not manifest_path.exists():
        parser.error(f"manifest does not exist: {manifest_path}")

    try:
        report = validate(manifest_path, args.final)
    except ValueError as error:
        parser.error(str(error))

    payload = json.dumps(report, indent=2) + "\n"
    if args.out:
        out = Path(args.out)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(payload, encoding="utf-8")
    else:
        sys.stdout.write(payload)
    return 0 if report["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
