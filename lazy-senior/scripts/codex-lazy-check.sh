#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat >&2 <<'EOF'
Usage:
  codex-lazy-check.sh --task TASK [--cwd DIR] [--out FILE]
  codex-lazy-check.sh --task-file FILE [--cwd DIR] [--out FILE]

Runs one read-only Codex worker to challenge an overbuilt solution.

Environment:
  LAZY_SENIOR_MODEL        Codex model to use (default: gpt-5.4-mini)
  LAZY_SENIOR_SERVICE_TIER Codex service_tier override (default: fast)
  LAZY_SENIOR_CODEX        Codex binary (default: codex)
EOF
}

task=""
task_file=""
cwd="$PWD"
out=""
script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
skill_path="$(cd -- "$script_dir/.." && pwd)"

while [[ $# -gt 0 ]]; do
  case "$1" in
    --task)
      [[ $# -ge 2 ]] || { usage; exit 2; }
      task="$2"
      shift 2
      ;;
    --task-file)
      [[ $# -ge 2 ]] || { usage; exit 2; }
      task_file="$2"
      shift 2
      ;;
    --cwd)
      [[ $# -ge 2 ]] || { usage; exit 2; }
      cwd="$2"
      shift 2
      ;;
    --out)
      [[ $# -ge 2 ]] || { usage; exit 2; }
      out="$2"
      shift 2
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "Unknown argument: $1" >&2
      usage
      exit 2
      ;;
  esac
done

if [[ -n "$task" && -n "$task_file" ]]; then
  echo "Use either --task or --task-file, not both" >&2
  usage
  exit 2
fi

if [[ -n "$task_file" ]]; then
  if [[ ! -f "$task_file" ]]; then
    echo "Task file not found: $task_file" >&2
    exit 2
  fi
  task="$(cat "$task_file")"
fi

if [[ -z "$task" ]]; then
  echo "--task or --task-file is required" >&2
  usage
  exit 2
fi

if [[ -z "$out" ]]; then
  mkdir -p "$cwd/.lazy-senior"
  out="$cwd/.lazy-senior/codex-worker-verdict.txt"
fi

model="${LAZY_SENIOR_MODEL:-gpt-5.4-mini}"
service_tier="${LAZY_SENIOR_SERVICE_TIER:-fast}"
codex_bin="${LAZY_SENIOR_CODEX:-codex}"
prompt=$(cat <<EOF
Use \$lazy-senior at $skill_path.

Read-only worker. Do not edit files. Do not run write commands. Do not spawn another Codex worker.

Task:
$task

Return exactly this structure:
lazy-senior worker verdict:
- lower rung: <deleted / narrowed / stdlib / platform / installed dependency / one-liner / tiny local code / GitHub prior art / custom code needed>
- GitHub evidence: <skipped because ... / query or URL -> useful result; adoption=...>
- adoption: <use existing dependency / add dependency / borrow architecture / ignore / skipped>
- smallest implementation: <one short concrete sketch>
- do not build: <surface area to avoid>
- residual risk: <one short risk or none>
EOF
)

"$codex_bin" exec \
  -c "service_tier='$service_tier'" \
  --ephemeral \
  --skip-git-repo-check \
  --sandbox read-only \
  -m "$model" \
  -C "$cwd" \
  -o "$out" \
  "$prompt"

validator="$script_dir/validate-worker-verdict.sh"
if [[ -x "$validator" ]]; then
  "$validator" "$out" >&2
fi

printf '%s\n' "$out"
