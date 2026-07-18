---
name: idea-validation
description: 'Validate a raw product idea before PRD or implementation: buyer, pain, workaround, promised outcome, smallest wedge, distribution path, proof sought, kill criteria, and the next honest lane. Use when an idea still needs market or wedge truth.'
---

# Idea Validation

## Metadata
- Trigger when: the idea is interesting enough to examine, but buyer, pain, signal, or wedge truth is still uncertain.
- Do not use when: the work already has believable validation signal and the next blocker is product shaping or implementation detail.

## Skill Purpose

Pressure-test an idea before it turns into PRD theater by forcing clarity on buyer, pain, workaround, outcome, wedge, proof, and kill criteria.

## Instructions
1. Run the contract-clean gate first whenever the idea may touch client work, sensitive exports, ambiguous rights, shared accounts, or gray-source access. Use `~/.codex/skills/idea-validation/references/contract-clean-gate.md` when you need the exact hard-reject surface.
2. Build one lean validation brief with these fields: buyer/operator, painful recurring job, current workaround, promised outcome, smallest wedge, first distribution path, proof sought, and kill criteria. Default to one function, one buyer, and one painful problem in the first pass.
3. Choose the next honest lane explicitly: stay in validation, move to `$product-shaping`, move to a short execution brief, or move to `$spec-bundle` when implementation ambiguity or architecture risk is now the real blocker. If another skill is needed, name it explicitly with a one-line reason. Use `~/.codex/skills/idea-validation/references/playbook.md` only when you need fuller heuristics.

## Non-Negotiable Acceptance Criteria
- Do not let a detailed spec pretend to be validation signal.
- If the fastest proof path is manual service or concierge work, say so directly.
- Contract-gray or rights-dirty ideas are parked, not rescued with clever framing.
- The output names a next lane; it does not end with vague “more research later” filler.

## Output
- A compact validation brief covering buyer, pain, workaround, outcome, wedge, distribution, proof, and kill criteria.
- An explicit statement of the current signal strength and the main red flag, if any.
- One next lane: stay in validation, move to product shaping, or move toward execution/spec work.
- `Next skill options` (only if needed): `$product-shaping` — structure the next product decision after basic validation; `$spec-bundle` — turn the validated direction into implementation-ready artifacts; `$work-shaping` — decide how much process or tracking the work now deserves.
