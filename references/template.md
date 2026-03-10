# Continuity Template

Use the smallest durable shape that keeps the task coherent.

## Minimal template

```md
# CONTINUITY

## Sources of Truth
- issue:
- bundle:
- test plan:

## Goal
- ...

## Constraints
- ...

## Decisions
- 2026-03-08: ...

## Evidence
- file: ...
- command: ...
- test: ...

## State
- Done:
  - ...
- Now:
  - ...
- Next:
  - ...

## Open Questions
- ...
```

## Update rules

- update after any meaningful decision
- update after important tool output that changes the plan
- update source bundle artifacts before or with the ledger when architecture/contracts/gates changed
- remove stale items instead of letting them pile up
- keep unresolved claims marked `UNCONFIRMED`
- if the issue or execution brief already carries the same state, update that instead
