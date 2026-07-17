# Codex Skills

Canonical source repository for reusable Codex skills maintained by KikuAI Lab.

Each top-level directory is a standalone skill folder with its own `SKILL.md`,
agent metadata, and any references, scripts, or assets it needs. Small
documentation-only skills live here; projects with their own runtime, tests,
release cycle, or incompatible license remain in dedicated repositories.

## Included skills

### Planning, execution, and review

- `adversarial-review`
- `adr-log`
- `github-mobile-ops`
- `justdoit`
- `lazy-senior`
- `long-context-dispatch`
- `parallel-worktrees`
- `product-council`
- `triage-finding`
- `tool-scout`

### Public artifacts and communication

- `ai-writing-detox`
- `illustration-prompt`
- `public-artifact-lane`
- `readme-generator`

### Browser, media, and external workflows

- `autonomous-video-pipeline`
- `browser-tutorial-video`
- `openclaw-council`
- `playwright`
- `screenshot`

### System skills

- `.system/skill-creator`
- `.system/skill-installer`

## Using a skill

Copy or install the required directory as a complete unit. Do not copy only
`SKILL.md` when the directory also contains `agents/`, `references/`,
`scripts/`, or `assets/`.

The public catalog with descriptions and use cases is maintained in
[Awesome AI Skills by Kiku](https://github.com/kiku-jw/awesome-ai-skills-by-kiku).

## Repository policy

A skill belongs here when it is primarily a reusable instruction workflow.
Keep it in a dedicated repository when it has a substantial runtime, tests,
independent releases, or licensing that should remain isolated.

## License

MIT. See [LICENSE](LICENSE).
