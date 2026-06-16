#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat >&2 <<'EOF'
Usage:
  validate-worker-verdict.sh FILE

Checks the bounded lazy-senior Codex worker output contract.
EOF
}

file="${1:-}"
if [[ "$file" == "-h" || "$file" == "--help" ]]; then
  usage
  exit 0
fi
if [[ -z "$file" || ! -f "$file" ]]; then
  echo "Verdict file is required" >&2
  usage
  exit 2
fi

fail=0
bad() {
  printf 'FAIL: %s\n' "$*" >&2
  fail=1
}

require() {
  local pattern="$1"
  local label="$2"
  if ! grep -Eq -- "$pattern" "$file"; then
    bad "missing or invalid $label"
  fi
}

require '^lazy-senior worker verdict:' 'header'
require '^- lower rung: (deleted|narrowed|stdlib|platform|installed dependency|one-liner|tiny local code|GitHub prior art|custom code needed)' 'lower rung'
require '^- GitHub evidence: .+' 'GitHub evidence'
require '^- adoption: (use existing dependency|add dependency|borrow architecture|ignore|skipped)' 'adoption'
require '^- smallest implementation: .+' 'smallest implementation'
require '^- do not build: .+' 'do not build'
require '^- residual risk: .+' 'residual risk'

if grep -Eq 'GitHub prior art: used' "$file"; then
  bad 'unverifiable "GitHub prior art: used" claim'
fi

evidence_line="$(grep -E '^- GitHub evidence: ' "$file" | head -n 1 || true)"
if [[ -n "$evidence_line" ]]; then
  if [[ "$evidence_line" != *"skipped because"* && "$evidence_line" != *"->"* ]]; then
    bad 'GitHub evidence must be skipped with a reason or include query/URL -> useful result'
  fi
fi

if [[ "$fail" -eq 0 ]]; then
  printf 'OK: worker verdict contract\n' >&2
fi

exit "$fail"
