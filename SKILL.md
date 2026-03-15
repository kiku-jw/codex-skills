---
name: continuity-ledger
description: Keep substantial work coherent across long sessions or compaction with one short factual `CONTINUITY.md` covering sources of truth, goal, constraints, decisions, evidence, and done/now/next state. Use when session drift would otherwise become a real risk.
---

# Continuity Ledger

## Metadata
- Trigger when: the task is long enough, branchy enough, or interruption-prone enough that chat memory is no longer a safe source of truth.
- Do not use when: an existing issue, brief, or spec bundle already serves as current durable state and no extra memory layer is needed.

## Skill Purpose

Keep one compact, factual continuity file that lets the next session resume work without reconstructing the project state from chat history.

## Instructions
1. Gate the need for a ledger first. If a better durable artifact already exists and is current, reuse it instead of creating a second memory layer. When you do need a ledger, read `/Users/nick/.codex/skills/continuity-ledger/references/template.md` for the minimal section set.
2. Read the current `CONTINUITY.md` before substantial work and update it only when goals, constraints, decisions, evidence, or done/now/next state actually changed. Keep it short, factual, and bullet-based.
3. Validate the ledger. Mark uncertain items as `UNCONFIRMED`, update higher-authority source artifacts first when architecture or test state changed, and make sure the ledger points back to those sources instead of duplicating them.

## Non-Negotiable Acceptance Criteria
- At most one repo-local continuity ledger exists for the task.
- The ledger contains stable facts and actionable status, not chat transcript or vibes.
- `Done`, `Now`, and `Next` are explicit and current.
- The ledger is a bridge to the real source artifacts, not a shadow PRD.

## Output
- An updated `CONTINUITY.md` path.
- A short summary of changed sections, especially decisions and `Done`/`Now`/`Next`.
- Any unresolved question that still blocks confident continuation.
