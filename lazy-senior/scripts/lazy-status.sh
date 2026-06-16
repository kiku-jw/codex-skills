#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat >&2 <<'EOF'
Usage:
  lazy-status.sh [--cwd DIR] [--out FILE]

Writes a lightweight lazy-senior activation report for one workspace.
EOF
}

cwd="$PWD"
out=""
script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
skill_dir="$(cd -- "$script_dir/.." && pwd)"

while [[ $# -gt 0 ]]; do
  case "$1" in
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

[[ -d "$cwd" ]] || { echo "Not a directory: $cwd" >&2; exit 2; }

health_status="PASS"
health_output="$("$script_dir/skill-health.sh" "$skill_dir" 2>&1)" || health_status="FAIL"

debt_file="$cwd/.lazy-senior/debt.md"
open_debt=0
if [[ -f "$debt_file" ]]; then
  open_debt="$(grep -Ec '^- status: open$' "$debt_file" || true)"
fi

review_file="$cwd/.lazy-senior/lazy-review-diff.txt"
if [[ -f "$review_file" ]]; then
  last_review="$(date -r "$review_file" -u '+%Y-%m-%dT%H:%M:%SZ')"
else
  last_review="none"
fi

git_state="not a git work tree"
if git -C "$cwd" rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  changed="$(git -C "$cwd" status --short | wc -l | tr -d ' ')"
  git_state="$changed changed path(s)"
fi

report=$(cat <<EOF
# Lazy Senior Status

- workspace: $cwd
- skill: $skill_dir
- skill health: $health_status
- git state: $git_state
- open lazy debt: $open_debt
- last diff review: $last_review

## Health Output

\`\`\`text
$health_output
\`\`\`
EOF
)

if [[ -n "$out" ]]; then
  mkdir -p "$(dirname "$out")"
  printf '%s\n' "$report" >"$out"
  printf '%s\n' "$out"
else
  printf '%s\n' "$report"
fi
