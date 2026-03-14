# tool-scout

Codex skill for researching current tools, services, MCP servers, APIs, models, and libraries before you waste time building the wrong thing.

## What it does

- researches current options for a concrete task across web, GitHub, MCP catalogs, awesome-lists, and finalist package checks
- picks sources adaptively instead of running the same search pattern every time
- compares only the strongest candidates by fit, maturity, and integration cost
- aggregates signals such as GitHub stars and archived status
- deduplicates tools found across several sources
- calls out trivial tasks where custom code beats tool shopping
- ends with a recommendation instead of a giant list

## Repository layout

- `SKILL.md` - main skill instructions
- `agents/openai.yaml` - UI metadata for skill surfaces
- `references/evaluation-matrix.md` - comparison frame
- `references/search-patterns.md` - query and source rules

## Example prompts

- `find tools for this`
- `what should we use for X`
- `research options before we build`
- `is there an MCP for this`
- `find a library for PDF generation on Python`

## License

MIT
