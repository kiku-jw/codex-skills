---
name: codex-execution-pack
description: 'Build a Codex execution pack from a raw task or PRD: `AGENTS.md` plus `docs/PLAN.md`, `docs/STATUS.md`, `docs/TEST_PLAN.md`, and `docs/BACKLOG.md`, with optional prompt surfaces and a spec companion when the work is large enough to justify them.'
---

# Codex Execution Pack

## Metadata
- Trigger when: the user wants a durable operating pack for Codex instead of a loose spec or one-off prompt.
- Do not use when: the work is tiny, highly reversible, or better served by a short execution brief.

## Skill Purpose

Create a durable execution harness that survives long runs and resumptions by separating execution policy, plan, live status, validation, and backlog into explicit files.

## Instructions
1. Decide whether a full pack is honest. If the source is still fuzzy, route through `$idea-validation` or `$spec-bundle` first. If the pack is justified, scaffold it with `/Users/nick/.codex/skills/codex-execution-pack/scripts/init_execution_pack.py`. Use `/Users/nick/.codex/skills/codex-execution-pack/references/pack-shape.md` only when you need the exact file roles.
2. Fill only the artifacts that materially improve execution quality: `AGENTS.md`, `docs/PLAN.md`, `docs/STATUS.md`, `docs/TEST_PLAN.md`, and `docs/BACKLOG.md`, plus optional prompt surfaces or `spec/` files when they reduce ambiguity. Keep one source of truth per concern.
3. Validate the pack. Every milestone must have concrete validation commands, `docs/STATUS.md` must own live done/now/next state, and the pack must stay synchronized with any separate spec bundle instead of forking reality.

## Non-Negotiable Acceptance Criteria
- Do not generate a full pack for tiny work.
- Every meaningful milestone has explicit validation, repair-before-continue expectations, and a durable status surface.
- Prompt surfaces and spec companion files exist only when they reduce ambiguity or recovery cost.
- If issue or board sync fails, that fact is written into the pack instead of disappearing into chat.

## Output
- The created or updated pack files on disk.
- A short summary of what starts first, which validation gates matter most, and what would stop execution.
- Any missing input or blocker that prevents the pack from being truly executable.
- `Next skill options` (only if needed): `$spec-bundle` — add deeper contracts or architecture artifacts; `$justdoit` — drive execution from the generated pack; `$continuity-ledger` — preserve durable state across long execution runs.
