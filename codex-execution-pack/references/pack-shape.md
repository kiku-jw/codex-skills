# Execution Pack Shape

Use this reference when the user wants Codex to behave like a managed executor rather than a chat that needs constant steering.

## Core files

Keep the operating pack lean. The default pack has five files:

1. `AGENTS.md`
2. `docs/PLAN.md`
3. `docs/STATUS.md`
4. `docs/TEST_PLAN.md`
5. `docs/BACKLOG.md`

Add prompt surfaces only when the team actually wants reusable execution prompts:

6. `prompts/execute.md`
7. `prompts/resume.md`
8. `prompts/review-repair.md`
9. `prompts/blocker-compress.md`

Add `spec/` only when contracts, schema, architecture boundaries, or hard gates matter.

## File roles

### `AGENTS.md`

Use for:

- execution policy
- stop conditions
- blocker format
- scoped diff rules
- dependency-order discipline

Bad sign:

- it repeats the product spec instead of telling the agent how to work

### `docs/PLAN.md`

Use for:

- milestone order
- task grouping
- done criteria
- validation commands
- known risks

Bad sign:

- milestones are too large to finish in one loop

### `docs/STATUS.md`

Use for:

- done / now / next
- assumptions in force
- decisions made
- commands to run
- blockers
- short audit log

Bad sign:

- the current state still has to be reconstructed from chat

### `docs/TEST_PLAN.md`

Use for:

- test levels
- fixtures
- negative tests
- release or demo gates
- smoke checklist

Bad sign:

- it only says "write tests" without naming the checks

### `docs/BACKLOG.md`

Use for:

- compact epic/task grouping
- dependency notes
- issue-ready titles
- labels, phase, and priority
- what can parallelize

Bad sign:

- tasks are either one giant blob or atomized beyond usefulness

## Relationship to `spec/`

The execution pack tells Codex how to move. A spec companion tells Codex what shape it is implementing.

Use `spec/` when at least one is true:

- schema or migration work exists
- API, IPC, or event contracts matter
- workers or queues exist
- auth or permission logic matters
- local/cloud boundary needs explicit handling
- rollout risk needs gates or ADRs

If `spec/` exists, the pack should point to it instead of duplicating it.

## Quality bar

The pack is ready when:

- a coder can execute without constant babysitting
- a reviewer can see what is done and what is blocked
- a future you can resume from repo state instead of chat archaeology

If it does not achieve those three things, shorten it or sharpen it.
