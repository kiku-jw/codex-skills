#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat >&2 <<'EOF'
Usage:
  lazy-audit.sh [--cwd DIR] [--out FILE] [--max-findings N] [--fail-on high|medium|low]

Runs a deterministic repo scan for overengineering candidates. This is a
candidate finder, not a verdict. Read the code before deleting or rewriting.
EOF
}

cwd="$PWD"
out=""
max_findings=40
fail_on=""

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
    --max-findings)
      [[ $# -ge 2 ]] || { usage; exit 2; }
      max_findings="$2"
      shift 2
      ;;
    --fail-on)
      [[ $# -ge 2 ]] || { usage; exit 2; }
      fail_on="$2"
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
command -v rg >/dev/null 2>&1 || { echo "rg is required" >&2; exit 2; }

case "$fail_on" in
  ""|high|medium|low) ;;
  *) echo "--fail-on must be high, medium, or low" >&2; exit 2 ;;
esac

tmp="$(mktemp "${TMPDIR:-/tmp}/lazy-audit.XXXXXX")"
trap 'rm -f "$tmp"' EXIT

count=0
high_count=0
medium_count=0
low_count=0

add_finding() {
  local severity="$1"
  local rung="$2"
  local reason="$3"
  local hit="$4"

  [[ "$count" -lt "$max_findings" ]] || return 0

  local path="${hit%%:*}"
  local rest="${hit#*:}"
  local line="${rest%%:*}"
  local snippet="${hit#*:*:}"
  local rel="$path"
  if [[ "$path" == "$cwd/"* ]]; then
    rel="${path#"$cwd/"}"
  fi
  snippet="${snippet//$'\t'/ }"
  snippet="${snippet:0:160}"

  count=$((count + 1))
  case "$severity" in
    high) high_count=$((high_count + 1)) ;;
    medium) medium_count=$((medium_count + 1)) ;;
    low) low_count=$((low_count + 1)) ;;
  esac

  {
    printf '## %s. %s\n\n' "$count" "$severity"
    printf -- '- location: `%s:%s`\n' "$rel" "$line"
    printf -- '- lower rung to check: %s\n' "$rung"
    printf -- '- reason: %s\n' "$reason"
    printf -- '- snippet: `%s`\n\n' "$snippet"
  } >>"$tmp"
}

scan() {
  local severity="$1"
  local rung="$2"
  local reason="$3"
  local pattern="$4"

  while IFS= read -r hit; do
    [[ -n "$hit" ]] || continue
    add_finding "$severity" "$rung" "$reason" "$hit"
  done < <(
    rg -n --hidden \
      --glob '!**/.git/**' \
      --glob '!**/.omx/**' \
      --glob '!**/node_modules/**' \
      --glob '!**/dist/**' \
      --glob '!**/build/**' \
      --glob '!**/.venv/**' \
      --glob '!**/venv/**' \
      --glob '!**/__pycache__/**' \
      --glob '*.{c,cc,cpp,cs,cjs,go,h,hpp,java,js,jsx,kt,mjs,php,py,rb,rs,sh,swift,ts,tsx}' \
      --glob '!**/scripts/lazy-audit.sh' \
      "$pattern" "$cwd" 2>/dev/null || true
  )
}

scan high 'platform/native UI before custom widget' 'Date picker or calendar code often collapses to native HTML/platform controls.' '(DatePicker|date picker|calendar picker)'
scan high 'stdlib or installed parser before manual parser' 'Parser-shaped code deserves a stdlib/dependency check before custom parsing grows.' '((function|def|class|const|let|var)[[:space:]]+[^[:space:]]*parse[A-Z_]|class[[:space:]]+[A-Za-z0-9_]*Parser)'
scan medium 'platform/framework primitive before custom infra' 'Cache, queue, scheduler, and limiter code is often already present in the platform or installed stack.' '(RateLimiter|TokenBucket|Scheduler|JobQueue|MessageQueue|CacheManager|LRUCache)'
scan medium 'delete or inline before abstraction' 'Factory/registry/adapter/wrapper/manager names are not bugs, but they are common agent overbuild markers.' '([A-Za-z0-9_]+Factory|[A-Za-z0-9_]+Registry|[A-Za-z0-9_]+Adapter|[A-Za-z0-9_]+Wrapper|[A-Za-z0-9_]+Manager|Base[A-Z][A-Za-z0-9_]+)'
scan low 'one expression or existing helper before utility growth' 'Generic util/helper files often hide duplicated one-liners.' '(^|/)(utils?|helpers?|common|shared)[./_-]'

status="PASS"
case "$fail_on" in
  high)
    [[ "$high_count" -eq 0 ]] || status="FAIL"
    ;;
  medium)
    [[ "$high_count" -eq 0 && "$medium_count" -eq 0 ]] || status="FAIL"
    ;;
  low)
    [[ "$count" -eq 0 ]] || status="FAIL"
    ;;
esac

report=$(cat <<EOF
# Lazy Senior Audit

- cwd: $cwd
- status: $status
- findings: $count
- high: $high_count
- medium: $medium_count
- low: $low_count
- note: Candidates only. Apply the decision ladder before changing code.

EOF
)

if [[ "$count" -gt 0 ]]; then
  report="$(printf '%s\n\n%s' "$report" "$(cat "$tmp")")"
else
  report="$(printf '%s\n\nNo overengineering candidates matched the built-in scan patterns.\n' "$report")"
fi

if [[ -n "$out" ]]; then
  mkdir -p "$(dirname "$out")"
  printf '%s' "$report" >"$out"
  printf '%s\n' "$out"
else
  printf '%s' "$report"
fi

if [[ "$status" == "FAIL" ]]; then
  exit 1
fi
