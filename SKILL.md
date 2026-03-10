---
name: continuity-ledger
description: "Keep substantial work coherent across long sessions or context compaction with a short factual CONTINUITY.md: sources of truth, goal, constraints, decisions, evidence, done/now/next, and open questions."
---

# Continuity Ledger

Use this skill when a task is likely to span sessions, long tool loops, or multiple branches.

Typical prompts:

- `keep continuity on this task`
- `update the ledger`
- `this task is too long for chat memory`
- `stabilize the session state`
- `don't lose the thread`

## What to do

1. Use one repo-local `CONTINUITY.md` only when it clearly reduces drift.
2. Read the ledger before continuing substantial work.
3. Keep it short and factual. Update only when goals, constraints, decisions, status, or evidence change.
4. Prefer these sections:
   - `Sources of Truth` when a bundle, issue, or brief already owns the real details
   - `Goal`
   - `Constraints`
   - `Decisions`
   - `Evidence`
   - `State` with `Done`, `Now`, `Next`
   - `Open Questions`
5. Mark uncertain items as `UNCONFIRMED`.
6. If a better durable artifact already exists and is current, do not create a second memory layer.
   - Prefer the existing GitHub issue, execution brief, or spec bundle.
7. When architecture, contracts, tests, or gates change, update those source artifacts first or in the same pass, then note the result in the ledger.
8. If context looks compacted or fragmented, rebuild the ledger from visible facts first, then ask only the minimum missing questions.

## Defaults

- Use bullets, not prose.
- Keep only stable facts and actionable status.
- Reference files, commands, and decisions when they matter.
- Reference current bundle artifacts when they exist instead of restating them.
- Do not paste chat transcript into the ledger.

## Anti-Frankenstein rules

- No extra database, vector store, or sidecar memory service.
- No duplicate "memory" file if an issue or brief already serves that role.
- The ledger is a bridge, not a second PRD.

## When to read the reference

For a minimal template and update rules, read `references/template.md`.
