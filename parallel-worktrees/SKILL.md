---
name: parallel-worktrees
description: Split substantial work into isolated git worktrees so coding, tests, docs, review, or experiments can proceed in separate lanes without contaminating the main checkout.
---

# Parallel Worktrees

## Metadata
- Trigger when: the work is substantial and has truly separable lanes that can benefit from isolation.
- Do not use when: there is only one lane, one owner concern, or the split would be process theater.

## Skill Purpose

Use git worktrees as clean execution lanes for substantial multi-track work without inventing extra repos or runtime layers.

## Instructions
1. Confirm that the work really splits into separate owner concerns such as implementation, tests, docs, review, or experiment. Prefer two or three lanes maximum.
2. Create dedicated worktrees on dedicated `codex/` branches, never directly on the main branch. The command pattern is `git worktree add /absolute/path/to/lane -b codex/<lane-name> <base-ref>`. Record each lane’s purpose and shared source of truth before work starts.
3. Merge or clean up only after each lane has a clear result and no ownership confusion remains. Use `git worktree remove /absolute/path/to/lane` only when the lane is intentionally merged, parked, or discarded.

## Non-Negotiable Acceptance Criteria
- Worktrees are for isolation, not orchestration theater.
- Shared decisions live in one durable place such as an issue, brief, or `CONTINUITY.md`.
- No lane starts on the main branch or in an unsafe directory.
- Cleanup does not happen until the lane outcome is explicit.

## Output
- A lane list with branch name, worktree path, owner concern, and purpose.
- The shared source-of-truth artifact for cross-lane decisions.
- Cleanup status for each lane: active, merged, parked, or removed.
