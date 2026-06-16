# Lazy Senior Publication Pack

Use this when turning the local skill into a public or shared skill package.

## Public-Safe Package

Run:

```bash
scripts/package-public-skill.sh --out /tmp/lazy-senior-package
```

The package contains:

- `README.md`
- `lazy-senior/SKILL.md`
- `lazy-senior/agents/openai.yaml`
- `lazy-senior/scripts/*.sh`
- `lazy-senior/references/*.md`

## Before Publishing

- Review all files for private paths, private repo names, secrets, and local-only claims.
- Add a license deliberately.
- Run `lazy-senior/scripts/skill-health.sh`.
- Run benchmark fixtures with `--strict`.
- Keep benchmark claims reproducible and sourced from checked-in fixtures.

## Product Positioning

Describe the skill as a guardrail for smaller code and visible decisions. Do not promise universal code reduction. Show concrete examples and receipts.
