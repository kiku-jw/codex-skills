#!/usr/bin/env bash
set -euo pipefail

script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
default_skill_dir="$(cd -- "$script_dir/.." && pwd)"
skill_dir="${1:-$default_skill_dir}"

fail=0
say() { printf '%s\n' "$*"; }
bad() { say "FAIL: $*"; fail=1; }
ok() { say "OK: $*"; }

[[ -d "$skill_dir" ]] || { echo "Missing skill dir: $skill_dir" >&2; exit 2; }
[[ -f "$skill_dir/SKILL.md" ]] || bad "missing SKILL.md"
[[ -f "$skill_dir/agents/openai.yaml" ]] || bad "missing agents/openai.yaml"

if [[ -f "$skill_dir/SKILL.md" ]]; then
  rg -q '^name: lazy-senior$' "$skill_dir/SKILL.md" && ok "frontmatter name" || bad "frontmatter name"
  rg -q '^description:' "$skill_dir/SKILL.md" && ok "frontmatter description" || bad "frontmatter description"
  if rg -n 'TODO|FIXME|\[TODO' "$skill_dir/SKILL.md"; then
    bad "TODO markers remain in SKILL.md"
  else
    ok "no TODO markers"
  fi
  lines="$(wc -l <"$skill_dir/SKILL.md" | tr -d ' ')"
  if [[ "$lines" -le 500 ]]; then
    ok "SKILL.md size ${lines} lines"
  else
    bad "SKILL.md is too large: ${lines} lines"
  fi
fi

if [[ -d "$skill_dir/scripts" ]]; then
  while IFS= read -r script; do
    [[ -x "$script" ]] || bad "script is not executable: $script"
    bash -n "$script" && ok "bash syntax: $(basename "$script")" || bad "bash syntax: $script"
  done < <(find "$skill_dir/scripts" -type f -name '*.sh' | sort)
fi

if [[ -d "$skill_dir/references" ]]; then
  while IFS= read -r ref; do
    [[ -s "$ref" ]] && ok "reference present: $(basename "$ref")" || bad "empty reference: $ref"
  done < <(find "$skill_dir/references" -type f -name '*.md' | sort)
fi

exit "$fail"
