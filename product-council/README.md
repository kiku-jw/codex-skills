# product-council

Codex skill for stress-testing product decisions through explicit lenses instead of fake celebrity roleplay.

## What it does

- runs a multi-lens council for fuzzy, risky, or high-impact product decisions
- uses named archetypes with clear optimization targets and failure fears
- supports decision-specific councils for wedge, GTM, roadmap, pricing, and go/no-go
- surfaces disagreements, hidden assumptions, and evidence needed before commitment

## Repository layout

- `SKILL.md` - main skill instructions
- `agents/openai.yaml` - UI metadata for skill surfaces
- `references/roles.md` - role sheet for the core lenses
- `references/council-templates.md` - ready council templates by decision type

## Example prompts

- `run a product council on this`
- `help me choose the wedge`
- `do a roadmap council`
- `run a pricing council`
- `give me a go/no-go council`

## Design stance

This skill is opinionated in a few ways:

- named lenses beat pretending to be real famous people
- evidence beats style
- councils are for reducing blind spots, not decorating obvious answers
- the smallest useful council is usually the best one

## License

MIT
