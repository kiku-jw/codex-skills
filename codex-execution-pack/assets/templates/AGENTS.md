# AGENTS.md - {{PROJECT_NAME}} Execution Rules

## Source Of Truth

1. Read `docs/PLAN.md`.
2. Read `docs/STATUS.md`.
3. Read `docs/TEST_PLAN.md`.
4. Read `docs/BACKLOG.md`.
5. If `spec/` exists, read only the files needed for the current task.

Repo files are the execution source of truth during rollout. Boards and issues may mirror state, but they do not replace repo state.

## Execution Loop

1. Select the first unfinished task whose dependencies are done.
2. Gather only the minimum context required for that task.
3. Implement the task with a scoped diff.
4. Run the validation commands defined for that task.
5. If validation fails, repair before continuing.
6. Mark progress in `docs/PLAN.md`.
7. Append the latest result to `docs/STATUS.md`.
8. Continue immediately unless a real blocker remains.

## Diff Discipline

- Keep diffs scoped to the current task.
- Do not combine architecture rewrites, UI restyling, storage changes, and packaging in one step unless the milestone explicitly says so.
- If behavior changes, add or update tests unless the test plan explicitly defers that check.
- Avoid unrelated refactors while executing milestones.

## Reasonable Assumptions

- Make reversible local assumptions when that keeps execution moving.
- Record those assumptions in `docs/STATUS.md`.
- Ask the user only when a choice is irreversible, needs a secret, requires manual external action, or changes the intended product behavior in a non-obvious way.

## Validation Policy

- No milestone is complete while its required checks are red.
- Prefer concrete repo commands over vague instructions like "run the tests".
- If a check fails, fix the failure before moving on.
- If a board or issue sync fails, log it in `docs/STATUS.md` and keep coding unless that sync is the actual task.

## Stop Conditions

Stop only when one of these is true:

1. All planned tasks are complete.
2. A real blocker remains after 3 focused repair attempts.
3. A secret, credential, payment, or manual external step is required.
4. An irreversible action needs explicit approval.

## Blocker Format

If blocked, output only:

1. `Where blocked`
2. `What already works`
3. `What failed`
4. `What you tried`
5. `Smallest unblock options`
6. `Recommended next action`
