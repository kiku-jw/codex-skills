Resume execution mode.

Re-read and follow:

- `AGENTS.md`
- `docs/PLAN.md`
- `docs/STATUS.md`
- `docs/TEST_PLAN.md`
- `docs/BACKLOG.md`
- relevant `spec/` files if present

Do not restart from the beginning.
Do not repeat finished work.

Use `docs/PLAN.md` and `docs/STATUS.md` to identify the exact next unfinished task and continue from there.

Rules:

- If the previous stop was caused by failed validation, fix that first.
- If the current task has partial changes, finish and validate them before switching tasks.
- Keep diffs scoped.
- Continue task by task until all remaining work is done or a real blocker is hit.
- If blocked, use the blocker format from `AGENTS.md`.
