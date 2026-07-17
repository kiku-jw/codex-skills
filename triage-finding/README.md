# triage-finding

Codex skill for deciding whether an external finding deserves action now, later, or not at all.

## What it does

- inspects posts, links, repos, screenshots, notes, and similar findings
- follows primary links and fact-checks claims before trusting the post
- detects duplicates, including already-installed local skills and obvious tool overlap
- explains the gist in plain language
- maps the finding to current work instead of treating novelty as value
- prioritizes multiple findings by relevance to active work
- handles YouTube findings with a fallback path instead of pretending metadata is enough
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
- `review this ideas folder`

## License

MIT
