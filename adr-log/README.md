# adr-log

Codex skill for recording significant architecture and execution decisions so the reasoning survives the session.

## What it does

- decides whether a choice is ADR-worthy
- records context, alternatives, trade-offs, and revisit conditions
- routes the record to the right durable surface: repo, issue, or both
- preserves superseded decisions instead of erasing history

## Repository layout

- `SKILL.md` - main skill instructions
- `agents/openai.yaml` - UI metadata for skill surfaces
- `references/storage-rules.md` - where the decision should live
- `references/entry-template.md` - compact ADR entry shape

## Example prompts

- `record this decision`
- `write an ADR`
- `log why we chose this`
- `supersede the old decision`

## License

MIT
