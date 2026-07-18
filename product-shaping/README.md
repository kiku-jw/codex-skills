# product-shaping-skill

Codex skill for shaping product decisions after an idea clears basic validation but before execution becomes obvious.

## What it does

- picks the smallest useful product framework for the question at hand
- helps surface assumptions, experiments, strategy choices, value proposition, or failure modes
- keeps outputs compact and decision-ready
- routes the result into the next honest lane instead of drifting into PM theater

## Frameworks included

- `identify-assumptions`
- `prioritize-assumptions`
- `brainstorm-experiments`
- `opportunity-solution-tree`
- `product-strategy`
- `value-proposition`
- `pre-mortem`

## Repository layout

- `SKILL.md` - main routing and usage rules
- `references/patterns.md` - framework chooser and output templates
- `agents/openai.yaml` - agent metadata

## Installation

1. Clone or copy this repository into your Codex skills directory.
2. Keep `SKILL.md` and `references/` together.
3. Load the skill in the environment that resolves local skills.

## Example prompts

- `shape the product side`
- `which framework fits this`
- `map the risky assumptions`
- `help me narrow the strategy`
- `run a pre-mortem`

## How it fits the suite

Use this after `idea-validation` when the core question is no longer "is the pain real?" but "what is the smartest next product move?".

Typical flow:

`idea-validation -> product-shaping -> spec-bundle`

## License

AGPL-3.0
