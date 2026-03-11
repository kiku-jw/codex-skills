# illustration-prompt

Codex skill for turning vague image ideas and reference sets into precise generator-ready prompts.

## What it does

- runs a structured 6-step interview: context, style, references, scene, palette, format
- works especially well when the user has references and wants the prompt to inherit the right cues
- outputs a structured English prompt with clear scene, style, color, format, and negative constraints
- can hand off to `imagegen` after the prompt is approved

## Repository layout

- `SKILL.md` - main skill instructions
- `agents/openai.yaml` - UI metadata for skill surfaces
- `references/reference-analysis.md` - how to extract useful traits from refs
- `references/prompt-template.md` - the final 8-block prompt format

## Example prompts

- `write an illustration prompt`
- `help me make an image prompt from these refs`
- `turn this vague idea into a Midjourney prompt`
- `I need a hero image prompt for this page`

## Design stance

This skill is opinionated in a few ways:

- references and context beat generic adjectives
- prompt quality matters more than generator brand
- vague briefs should be clarified, not decorated
- iteration should happen by editing blocks, not rewriting from zero

## License

MIT
