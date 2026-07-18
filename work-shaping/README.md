# work-shaping-skill

Codex skill for deciding how much process a task deserves before coding starts.

## What it does

- classifies work as tiny or substantial
- decides whether chat, a local note, or a GitHub issue should hold the durable record
- picks the smallest honest planning layer: none, checklist, or execution brief
- decides whether the task needs architecture work, review overhead, or public writing

## The six axes

- size: `tiny` or `substantial`
- durable surface: `chat`, `local note`, or `GitHub issue`
- planning layer: `none`, `lightweight checklist`, or `execution brief`
- architecture lane: `none`, `light architecture lane`, or `full architecture pack`
- review lane: `none`, `operator review`, or `council`
- writing lane: `none`, `private diary`, or `public draft`

## Repository layout

- `SKILL.md` - core classification logic
- `agents/openai.yaml` - agent metadata

## Installation

1. Clone or copy this repository into your Codex skills directory.
2. Load the skill in the environment that resolves local skills.

## Example prompts

- `is this a big task or a small one`
- `do I need an issue for this`
- `should this go into a blog post`
- `do we need council or can we just build`
- `how much process does this deserve`

## How it fits the suite

Use this at the front of the workflow:

`work-shaping -> idea-validation -> product-shaping -> spec-bundle`

It is the entry router for the rest of the suite.

## License

AGPL-3.0
