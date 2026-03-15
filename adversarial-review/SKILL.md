---
name: adversarial-review
description: 'Run a second-pass review on meaningful changes with a deliberately skeptical lens: bugs, regressions, security, prompt or tool abuse, data loss, and missing tests. Use after non-trivial diffs or risky agent output.'
---

# Adversarial Review

## Metadata
- Trigger when: a meaningful diff, refactor, workflow change, or agent-generated patch deserves a skeptical second pass.
- Do not use when: the task is a trivial copy edit or there is no changed behavior to review.

## Skill Purpose

Stress-test a change for correctness, regressions, security, destructive side effects, and missing test coverage before anyone treats it as safe.

## Instructions
1. Inspect the changed behavior first, not just the diff text. If another model or isolated review path is available, use it; otherwise deliberately switch into a failure-hunting stance.
2. Review for the highest-signal risks: correctness bugs, behavior regressions, permission mistakes, prompt or tool abuse surfaces, data loss, destructive side effects, and missing or weak tests.
3. Report findings first and tie each one to concrete behavior plus file references. If there are no findings, say that explicitly and mention any residual risk or testing gap that still remains.

## Non-Negotiable Acceptance Criteria
- Findings are ordered by severity and grounded in observable behavior.
- Style nits do not outrank bugs, regressions, security flaws, or missing tests.
- Every non-trivial silent-failure risk calls out the missing test surface.
- If there are no findings, the response still states the residual risk honestly.

## Output
- A findings-first review with concrete file references and why each issue matters.
- If clean: an explicit `no findings` statement plus residual risk or testing gaps.
- No implementation detours, no rewrite plan, and no style-only padding.
