# readme-generator-skill

Codex skill for creating or rewriting human-first README files without turning them into bloated internal docs.

## What it does

- reads the repo before drafting
- identifies the project type before picking sections
- prefers a small truthful README over a giant doc dump
- keeps quick start, usage, and value proposition on the first screen
- avoids fake polish and stale architecture theater

## Repository layout

- `SKILL.md` - main skill instructions
- `agents/openai.yaml` - skill metadata for UI surfaces
- `references/section-matrix.md` - section recommendations by project type

## Example prompts

- `write a README for this repo`
- `rewrite this README`
- `make the open-source intro clearer`
- `refresh the quick start and usage sections`

## Design stance

This skill is opinionated in a few ways:

- README is for humans, not for agents
- repo facts beat generic template text
- quick start must be real
- full API reference does not belong in README by default

## License

AGPL-3.0
