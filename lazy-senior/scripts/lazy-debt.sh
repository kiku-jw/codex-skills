#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat >&2 <<'EOF'
Usage:
  lazy-debt.sh add --reason TEXT [--file PATH] [--rung TEXT] [--ledger FILE]
  lazy-debt.sh list [--ledger FILE]

Tracks accepted shortcuts or deferred simplifications in a tiny markdown ledger.
EOF
}

cmd="${1:-}"
if [[ "$cmd" == "-h" || "$cmd" == "--help" ]]; then
  usage
  exit 0
fi
if [[ -z "$cmd" ]]; then
  usage
  exit 2
fi
shift

ledger=".lazy-senior/debt.md"
reason=""
file=""
rung=""

while [[ $# -gt 0 ]]; do
  case "$1" in
    --ledger)
      [[ $# -ge 2 ]] || { usage; exit 2; }
      ledger="$2"
      shift 2
      ;;
    --reason)
      [[ $# -ge 2 ]] || { usage; exit 2; }
      reason="$2"
      shift 2
      ;;
    --file)
      [[ $# -ge 2 ]] || { usage; exit 2; }
      file="$2"
      shift 2
      ;;
    --rung)
      [[ $# -ge 2 ]] || { usage; exit 2; }
      rung="$2"
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

init_ledger() {
  mkdir -p "$(dirname "$ledger")"
  if [[ ! -f "$ledger" ]]; then
    cat >"$ledger" <<'EOF'
# Lazy Senior Debt

Track accepted shortcuts, deferred simplifications, and intentional local code that should be revisited.

EOF
  fi
}

case "$cmd" in
  add)
    if [[ -z "$reason" ]]; then
      echo "--reason is required for add" >&2
      usage
      exit 2
    fi
    init_ledger
    day="$(date -u +%Y-%m-%d)"
    {
      printf '\n## %s\n\n' "$day"
      printf -- '- status: open\n'
      [[ -n "$file" ]] && printf -- '- file: `%s`\n' "$file"
      [[ -n "$rung" ]] && printf -- '- rung: %s\n' "$rung"
      printf -- '- reason: %s\n' "$reason"
    } >>"$ledger"
    printf '%s\n' "$ledger"
    ;;
  list)
    init_ledger
    cat "$ledger"
    ;;
  *)
    usage
    exit 2
    ;;
esac
