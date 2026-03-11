# triage-finding

Codex skill for deciding whether an external finding deserves action now, later, or not at all.

## What it does

- inspects posts, links, repos, screenshots, notes, and similar findings
- explains the gist in plain language
- maps the finding to current work instead of treating novelty as value
- gives one honest verdict and the smallest useful next action

## Repository layout

- `SKILL.md` - main skill instructions
- `agents/openai.yaml` - UI metadata for skill surfaces
- `references/verdicts.md` - verdict rules
- `references/source-handling.md` - guidance by source type

## Example prompts

- `triage this`
- `look what I found`
- `is this useful for us`
- `check this repo/article/video`

## License

MIT
