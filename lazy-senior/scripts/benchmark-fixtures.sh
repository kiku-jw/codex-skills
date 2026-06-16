#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat >&2 <<'EOF'
Usage:
  benchmark-fixtures.sh --fixtures DIR [--out FILE] [--strict] [--min-results N]

Scores lazy-senior forward-test fixture results without calling a model.
Expected layout: DIR/results/*.txt plus edited fixture files.

With --strict, exits non-zero when any result lacks a lazy-senior rung, any
result lacks a GitHub evidence/skip line, or any result contains the
unverifiable phrase "GitHub prior art: used".
EOF
}

fixtures=""
out=""
strict=0
min_results=1

while [[ $# -gt 0 ]]; do
  case "$1" in
    --fixtures)
      [[ $# -ge 2 ]] || { usage; exit 2; }
      fixtures="$2"
      shift 2
      ;;
    --out)
      [[ $# -ge 2 ]] || { usage; exit 2; }
      out="$2"
      shift 2
      ;;
    --strict)
      strict=1
      shift
      ;;
    --min-results)
      [[ $# -ge 2 ]] || { usage; exit 2; }
      min_results="$2"
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

if [[ -z "$fixtures" || ! -d "$fixtures" ]]; then
  echo "--fixtures DIR is required" >&2
  usage
  exit 2
fi

results_dir="$fixtures/results"
if [[ ! -d "$results_dir" ]]; then
  echo "Missing results directory: $results_dir" >&2
  exit 2
fi

result_count="$(find "$results_dir" -type f -name '*.txt' | wc -l | tr -d ' ')"
rung_count="$( (rg -l 'lazy-senior:' "$results_dir" 2>/dev/null || true) | wc -l | tr -d ' ')"
github_count="$( (rg -l 'GitHub prior art:|GitHub evidence:' "$results_dir" 2>/dev/null || true) | wc -l | tr -d ' ')"
bad_github_count="$( (rg -l 'GitHub prior art: used' "$results_dir" 2>/dev/null || true) | wc -l | tr -d ' ')"
line_count=0
while IFS= read -r -d '' file; do
  lines="$(wc -l <"$file" | tr -d ' ')"
  line_count=$((line_count + lines))
done < <(find "$fixtures" -type f ! -path '*/results/*' ! -path '*/__pycache__/*' ! -path '*/.omx/*' -print0)

strict_status="not run"
strict_fail=0
if [[ "$strict" -eq 1 ]]; then
  strict_status="PASS"
  if [[ "$result_count" -lt "$min_results" ]]; then
    strict_status="FAIL"
    strict_fail=1
  fi
  if [[ "$rung_count" -lt "$result_count" ]]; then
    strict_status="FAIL"
    strict_fail=1
  fi
  if [[ "$github_count" -lt "$result_count" ]]; then
    strict_status="FAIL"
    strict_fail=1
  fi
  if [[ "$bad_github_count" -gt 0 ]]; then
    strict_status="FAIL"
    strict_fail=1
  fi
fi

report=$(cat <<EOF
# Lazy Senior Fixture Score

- fixtures: $fixtures
- strict: $([[ "$strict" -eq 1 ]] && echo enabled || echo disabled)
- strict status: $strict_status
- minimum result files: $min_results
- result files: $result_count
- result files with lazy-senior rung: $rung_count
- result files with GitHub evidence/skip line: $github_count
- result files with unverifiable "GitHub prior art: used": $bad_github_count
- edited fixture LOC: $line_count

EOF
)

if [[ -n "$out" ]]; then
  mkdir -p "$(dirname "$out")"
  printf '%s' "$report" >"$out"
  printf '%s\n' "$out"
else
  printf '%s' "$report"
fi

exit "$strict_fail"
