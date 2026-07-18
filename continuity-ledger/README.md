# continuity-ledger-skill

Codex skill for keeping substantial work coherent across long sessions, compaction, parallel branches, and multi-step tool loops.

## What it does

- maintains one short repo-local `CONTINUITY.md`
- records stable facts instead of chat transcript noise
- keeps goal, constraints, decisions, evidence, and state readable at a glance
- helps restart work after interruption without rebuilding context from scratch

## Repository layout

- `SKILL.md` - main guidance for when and how to keep a ledger
- `references/template.md` - minimal template and update rules
- `agents/openai.yaml` - agent metadata

## Installation

1. Clone or copy this repository into your Codex skills directory.
2. Keep `SKILL.md` and `references/` together.
3. Load the skill in the environment that resolves local skills.

## Example prompts

- `keep continuity on this task`
- `update the ledger`
- `this task is too long for chat memory`
- `stabilize the session state`

## Minimal ledger shape

```md
# CONTINUITY

## Sources of Truth
- issue:
- bundle:
- test plan:

## Goal
- ...

## State
- Done:
- Now:
- Next:
```

## How it fits the suite

This skill is cross-cutting. Use it alongside `work-shaping`, `spec-bundle`, or implementation work whenever the task is likely to span sessions or contributors.

## License

AGPL-3.0
