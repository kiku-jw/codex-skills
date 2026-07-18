# idea-validation-skill

Codex skill for testing a raw product idea before it turns into a PRD, roadmap, or build order.

## What it does

- turns a fuzzy idea into a lean validation brief
- forces buyer, pain, workaround, outcome, wedge, distribution, and proof to become explicit
- runs a contract-clean gate before deeper shaping when rights or data provenance are risky
- routes the result into the next honest lane: stay in validation, move to product shaping, or move to a spec bundle

## Best for

- founder-led product work
- AI and automation ideas that are easy to overbuild
- deciding whether a problem is real enough to deserve architecture or code

## Repository layout

- `SKILL.md` - primary skill instructions
- `references/playbook.md` - compact validation template and routing heuristics
- `references/contract-clean-gate.md` - rights/data/operator gate
- `agents/openai.yaml` - agent metadata

## Installation

1. Clone or copy this repository into your Codex skills directory.
2. Keep the folder name stable so `SKILL.md` and `references/` stay adjacent.
3. Load the skill in the environment that resolves local skill repositories.

## Example prompts

- `run this idea through validation`
- `is this worth building`
- `who is the buyer and what hurts`
- `turn this into a validation brief`
- `cut this down to the smallest wedge`

## How it fits the suite

This repository is designed to work well with:

- `work-shaping-skill`
- `product-shaping-skill`
- `spec-bundle-skill`
- `continuity-ledger-skill`

Typical flow:

`work-shaping -> idea-validation -> product-shaping -> spec-bundle`

Use `continuity-ledger` when the work will span sessions or branches.

## License

AGPL-3.0
