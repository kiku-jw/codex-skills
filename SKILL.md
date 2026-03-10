---
name: product-shaping
description: "Shape product work with the minimum useful framework after an idea clears basic validation: assumptions, experiments, opportunity-solution tree, strategy, value proposition, or pre-mortem, then route it into the right execution lane without drifting into PM theater."
---

# Product Shaping

Use this skill when the work is worth considering, but the next product decision is still fuzzy.

Typical prompts:

- `shape the product side`
- `which framework fits here`
- `map the risky assumptions`
- `help me narrow the strategy`
- `run a pre-mortem`

## Before you start

- If the real question is `build or not`, use `idea-validation` first.
- If the user already has a clear spec and just needs execution, move to `spec-bundle` or coding work instead.
- If architecture choices already dominate the risk, skip framework tourism and move to `spec-bundle` with the smallest honest architecture lane.

## Choose the smallest framework that fits

- `identify-assumptions` when the main risk is hidden assumptions.
- `prioritize-assumptions` when there are too many assumptions to test at once.
- `brainstorm-experiments` when the risky assumption is known and the next move is the fastest proof path.
- `opportunity-solution-tree` when the outcome is clear but the solution space is messy.
- `product-strategy` when positioning, defensibility, or strategic fit is fuzzy.
- `value-proposition` when the user, pain, or promised outcome is still soft.
- `pre-mortem` when execution is moving and the failure modes need to surface early.

## Route the result

- Stay in `product-shaping` only if another product question clearly blocks progress.
- Move back to `idea-validation` if the work still lacks believable signal or buyer clarity.
- Move to a short execution brief or core `spec-bundle` if the next move is straightforward, local, and reversible.
- Move to `spec-bundle` with a `light architecture lane` if the shaped solution crosses subsystems, needs a system map, or depends on explicit invariants or local/cloud boundaries.
- Move to `spec-bundle` with a `full architecture pack` if the chosen direction now implies schema work, public API/event contracts, background jobs, auth/permissions logic, external integrations, or meaningful rollout/cost risk.

## Output rules

1. Use one framework by default. Chain only when one output clearly feeds the next.
2. Keep outputs compact, decision-ready, and tied to the current task.
3. Prefer bullets over essays.
4. Name tradeoffs, risky assumptions, and the next concrete move.
5. End with an explicit next lane: `validation`, `product-shaping`, `execution brief`, `core spec-bundle`, `light architecture lane`, or `full architecture pack`.
6. Do not auto-expand into PRD, roadmap, sprint, or release planning unless asked.

## Anti-Frankenstein rules

- No marketplace logic.
- No slash-command assumptions.
- No generic PM ceremony.
- No duplication of the operator's existing build flow.
- No handoff vagueness. Say which lane the work should enter next.

## When to read the reference

For framework selection, exact output shapes, and compact templates, read `references/patterns.md`.
