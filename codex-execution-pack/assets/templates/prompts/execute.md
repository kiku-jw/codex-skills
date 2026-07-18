From this message onward, work in execution mode.

Read and follow:

- `AGENTS.md`
- `docs/PLAN.md`
- `docs/STATUS.md`
- `docs/TEST_PLAN.md`
- `docs/BACKLOG.md`
- `spec/` files only if they matter to the current task

Goal:

Finish unfinished work in dependency order using the smallest reviewable milestone.

Execution loop:

1. Select the first unfinished task whose dependencies are done.
2. Gather only the minimum context required for that task.
3. Implement that task with a scoped diff.
4. Run the validation commands defined for that task.
5. If validation fails, repair and rerun validation until green.
6. Mark the task state in `docs/PLAN.md`.
7. Append a concise log entry to `docs/STATUS.md` with task, files, commands, result, and next step.
8. Continue immediately unless a real blocker remains.

Rules:

- Do not stop after interim summaries.
- Do not ask to continue if the next dependency-safe step is clear.
- Keep diffs scoped to the current task.
- Do not do unrelated refactors.
- Do not claim completion while checks are red.
- Record assumptions in `docs/STATUS.md`.
- If sync to board or issue fails, log it and continue.

Stop only if:

1. all planned tasks are done; or
2. a real blocker remains after repair attempts; or
3. a secret, credential, or manual external action is required; or
4. an irreversible action needs explicit approval.
