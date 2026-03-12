---
name: codex-execution-pack
description: Build a Codex execution pack from raw input or PRD: AGENTS.md plus docs/PLAN.md, docs/STATUS.md, docs/TEST_PLAN.md, docs/BACKLOG.md, with optional prompt surfaces and spec companion files for durable, resumable execution.
---

# Codex Execution Pack

Use this skill when the user wants a real operating pack for Codex rather than a loose spec or one-off prompt.

Typical prompts:

- `собери execution pack для Codex`
- `сделай AGENTS.md + PLAN + STATUS + TEST_PLAN + BACKLOG`
- `нужен resumable pack для большой задачи`
- `преврати этот PRD в operating pack`
- `сделай pack для milestone-by-milestone execution`

## What to do

1. Decide first if the full pack is honest.
   - For tiny or reversible work, use a short execution brief instead.
2. If the input is still fuzzy, shape the source first.
   - If buyer, pain, or wedge are still unclear, route to `idea-validation`.
   - If the product direction is clear but implementation risk is high, pair this skill with `spec-bundle`.
3. Scaffold the pack:

```bash
python3 scripts/init_execution_pack.py --out /absolute/path/to/pack --project-name "Project Name"
python3 scripts/init_execution_pack.py --out /absolute/path/to/pack --project-name "Project Name" --with-prompts
python3 scripts/init_execution_pack.py --out /absolute/path/to/pack --project-name "Project Name" --with-prompts --with-spec-companion --with-architecture-pack --with-adrs
```

4. Fill the operating files with only the detail that changes execution quality:
   - `AGENTS.md`
   - `docs/PLAN.md`
   - `docs/STATUS.md`
   - `docs/TEST_PLAN.md`
   - `docs/BACKLOG.md`
5. Add prompt surfaces when the user wants reusable execution prompts:
   - `prompts/execute.md`
   - `prompts/resume.md`
   - `prompts/review-repair.md`
   - `prompts/blocker-compress.md`
6. Add `spec/` only when contracts, schema, architecture boundaries, or hard gates matter.
7. Keep pack state synchronized:
   - `AGENTS.md` sets execution policy
   - `docs/PLAN.md` owns dependency order and done criteria
   - `docs/STATUS.md` owns live done/now/next, assumptions, blockers, and commands
   - `docs/TEST_PLAN.md` owns validation and release gates
   - `docs/BACKLOG.md` owns the GitHub-ready task slice
   - `spec/` owns contracts and architecture details when present

## When to read the reference

If you need the exact file roles, when to include prompt surfaces, or how this pack should sit next to a spec bundle, read:

- `references/pack-shape.md`

## Rules

- Do not generate the full pack for tiny work.
- Keep one source of truth per concern.
- Prefer scoped milestones that can close in one implementation loop.
- Every milestone must have concrete validation commands.
- Use repair-before-continue as the default execution rule.
- Record local assumptions in `docs/STATUS.md`, not in chat.
- If issue or board sync fails, log it in `docs/STATUS.md` and continue.
- Use blocker compression only for real blockers after repair attempts, not for ordinary uncertainty.
- If a separate spec bundle exists, do not fork reality. Update the pack and the spec together when requirements move.
