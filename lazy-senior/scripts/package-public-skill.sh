#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat >&2 <<'EOF'
Usage:
  package-public-skill.sh --out DIR

Creates a public-safe staging package containing README.md plus the lazy-senior
skill folder. Review license and repository metadata before publishing.
EOF
}

out=""
script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
skill_dir="$(cd -- "$script_dir/.." && pwd)"

while [[ $# -gt 0 ]]; do
  case "$1" in
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

[[ -n "$out" ]] || { usage; exit 2; }

package_skill="$out/lazy-senior"
rm -rf "$package_skill"
mkdir -p "$package_skill"
cp "$skill_dir/SKILL.md" "$package_skill/SKILL.md"
cp -R "$skill_dir/agents" "$package_skill/agents"
cp -R "$skill_dir/scripts" "$package_skill/scripts"
cp -R "$skill_dir/references" "$package_skill/references"
find "$package_skill/scripts" -type f -name '*.sh' -exec chmod +x {} +

cat >"$out/README.md" <<'EOF'
# lazy-senior

`lazy-senior` is a Codex skill for avoiding agent overengineering. It asks for
deletion, standard library, native platform APIs, installed dependencies,
one-liners, tiny local code, and GitHub prior art before writing custom code.

## Install

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R lazy-senior "${CODEX_HOME:-$HOME/.codex}/skills/lazy-senior"
"${CODEX_HOME:-$HOME/.codex}/skills/lazy-senior/scripts/skill-health.sh"
```

## Use

Ask Codex to use `$lazy-senior` when implementing or reviewing code that might
add a dependency, parser, widget, wrapper, CLI, cache, queue, scheduler, state
machine, or reusable helper.

Useful commands:

```bash
"${CODEX_HOME:-$HOME/.codex}/skills/lazy-senior/scripts/lazy-audit.sh" --cwd .
"${CODEX_HOME:-$HOME/.codex}/skills/lazy-senior/scripts/lazy-review-diff.sh" --cwd .
"${CODEX_HOME:-$HOME/.codex}/skills/lazy-senior/scripts/lazy-status.sh" --cwd .
```

## Publish Checklist

- Pick and add a license before publishing.
- Run `scripts/skill-health.sh`.
- Run benchmark fixtures with `--strict`.
- Keep benchmark claims tied to reproducible artifacts, not marketing numbers.
EOF

printf '%s\n' "$out"
