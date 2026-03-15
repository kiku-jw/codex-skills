---
name: justdoit
description: Default execution-planning skill for almost any non-trivial repo task. Turn a raw task, feature request, PRD, or project brief into durable plan, status, and test-plan files, then hand back a concise ready-to-execute proposal.
---

# justdoit

## Metadata
- Trigger when: the work is non-trivial enough to benefit from durable execution docs before or during implementation.
- Do not use when: the request is a trivial one-shot edit, pure discussion, or a factual answer with no execution surface.

## Skill Purpose

Turn messy task input into a durable execution pack that another Codex run can resume from without reconstructing scope, sequencing, or validation from chat.

## Instructions
1. Determine the target files first. Prefer existing repo conventions; otherwise default to `docs/plans.md`, `docs/status.md`, and `docs/test-plan.md`. Normalize scope, constraints, risks, validation commands, and assumptions before drafting.
2. Build or update the plan, status, and test-plan files using the repo truth plus `/Users/nick/.codex/skills/justdoit/references/plan-template.md`, `/Users/nick/.codex/skills/justdoit/references/status-template.md`, and `/Users/nick/.codex/skills/justdoit/references/test-plan-template.md` when you need the baseline structure. Keep milestones dependency-ordered and validation-first.
3. Finish with a short execution proposal that points to the written files, names what starts first, how validation will run, and what would stop the run. If the user only asked for planning, stop and wait for confirmation unless they already explicitly asked to execute immediately. If another skill is needed after planning, name it explicitly with a one-line reason.

## Non-Negotiable Acceptance Criteria
- The plan is the source of truth; status and test-plan must line up with it.
- Every meaningful milestone has copy-pasteable validation commands and explicit done criteria.
- Assumptions are explicit instead of buried in prose.
- The skill does not paste huge file contents into chat unless the user explicitly asks for inspection.

## Output
- A short product-level summary.
- The plan, status, and test-plan file paths.
- A compact `Ready to execute` handoff plus either a confirmation question or a clear note that execution is already starting.
- `Next skill options` (only if needed): `$agx-orchestrator` — dispatch bounded execution through AGX; `$parallel-worktrees` — split substantial work into isolated lanes; `$continuity-ledger` — preserve cross-session state when the run will be long; `$adversarial-review` — run a skeptical second pass after implementation.
