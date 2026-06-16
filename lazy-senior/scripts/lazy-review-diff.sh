#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat >&2 <<'EOF'
Usage:
  lazy-review-diff.sh [--cwd DIR] [--base REV] [--out FILE] [--task TEXT]

Runs one read-only Codex worker over the current git diff and asks for a
lazy-senior delete-list and smallest-path review.

Environment:
  LAZY_SENIOR_DIFF_LIMIT  Maximum diff bytes included (default: 60000)
EOF
}

cwd="$PWD"
base=""
out=""
task="Review this diff for overengineering. Prefer deletion, stdlib/platform/dependency reuse, tiny local code, or documented deferral before new code."
script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"

while [[ $# -gt 0 ]]; do
  case "$1" in
    --cwd)
      [[ $# -ge 2 ]] || { usage; exit 2; }
      cwd="$2"
      shift 2
      ;;
    --base)
      [[ $# -ge 2 ]] || { usage; exit 2; }
      base="$2"
      shift 2
      ;;
    --out)
      [[ $# -ge 2 ]] || { usage; exit 2; }
      out="$2"
      shift 2
      ;;
    --task)
      [[ $# -ge 2 ]] || { usage; exit 2; }
      task="$2"
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

if ! git -C "$cwd" rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  echo "Not a git work tree: $cwd" >&2
  exit 2
fi

mkdir -p "$cwd/.lazy-senior"
tmp_task="$(mktemp "${TMPDIR:-/tmp}/lazy-review-diff.XXXXXX")"
trap 'rm -f "$tmp_task"' EXIT

diff_limit="${LAZY_SENIOR_DIFF_LIMIT:-60000}"
if [[ -n "$base" ]]; then
  diff_cmd=(git -C "$cwd" diff --no-ext-diff --unified=80 "$base")
else
  diff_cmd=(git -C "$cwd" diff --no-ext-diff --unified=80)
fi

diff_payload="$("${diff_cmd[@]}" | head -c "$diff_limit")"
if [[ -z "$diff_payload" ]]; then
  if [[ -z "$base" ]]; then
    diff_payload="$(git -C "$cwd" diff --cached --no-ext-diff --unified=80 | head -c "$diff_limit")"
  fi
  if [[ -z "$diff_payload" ]]; then
    echo "No unstaged or staged diff found in $cwd" >&2
    exit 2
  fi
fi

cat >"$tmp_task" <<EOF
$task

Diff review contract:
- Identify code to delete or avoid.
- Prefer existing lower rungs before custom code.
- Flag dependencies, abstractions, wrappers, or large new logic.
- Return a short delete-list and one smallest acceptable path.

Diff:
$diff_payload
EOF

if [[ -z "$out" ]]; then
  out="$cwd/.lazy-senior/lazy-review-diff.txt"
fi

"$script_dir/codex-lazy-check.sh" \
  --cwd "$cwd" \
  --out "$out" \
  --task-file "$tmp_task"
