# visual-explainer

Codex skill for turning complex structure into a clean self-contained HTML explainer that is easier to read in a browser than in chat.

## What it does

- chooses the right visual format for systems, workflows, tables, timelines, and comparisons
- generates one self-contained HTML artifact
- keeps the visual direction intentional instead of default dashboard sludge
- includes reusable HTML templates for architecture, Mermaid flows, and comparison tables

## Repository layout

- `SKILL.md` - main skill instructions
- `agents/openai.yaml` - UI metadata for skill surfaces
- `references/` - routing, style, and quality rules
- `assets/templates/` - starter HTML templates

## Example prompts

- `visualize this`
- `make a diagram for this system`
- `render this table as HTML`
- `show me the architecture visually`

## License

MIT
