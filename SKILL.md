---
name: idea-validation
description: "Use when a raw product idea needs to be tested before PRD or implementation: buyer, pain, workaround, promised outcome, smallest wedge, distribution path, proof sought, kill criteria, and honest routing into product shaping or architecture-aware execution."
---

# Idea Validation

Use this skill before a product idea becomes a PRD.

Typical prompts:

- `прогони идею через валидацию`
- `это вообще стоит пилить`
- `кто тут покупатель и какая боль`
- `собери validation brief`
- `сузь идею до внятного wedge`
- `как быстро проверить спрос`

## What to do

1. Run a contract-clean gate first if the idea touches old client work, moderation data, sensitive exports, ambiguous rights, or restricted tooling.
   - Hard reject ideas that rely on contract-bound data, derived work product, hidden delegation, or gray-source access.
2. Refuse fake momentum.
   - If the idea is still fuzzy, do not let it jump straight into PRD theater.
3. Build a lean validation brief with these fields:
   - buyer / operator
   - painful recurring job
   - current workaround
   - promised outcome
   - smallest wedge
   - first distribution path
   - proof sought
   - kill criteria
4. Prefer one function, one buyer, one painful problem in the first pass.
5. Prefer the fastest honest proof path:
   - manual service
   - concierge flow
   - tiny demo
   - narrow prototype
6. Once the brief is real, choose the next lane explicitly:
   - stay in validation if signal is still weak or indirect
   - move to `product-shaping` if the main uncertainty is strategy, assumptions, positioning, or wedge selection
   - move to a short execution brief or core `spec-bundle` if the build is small and reversible
   - move to `spec-bundle` with a `light architecture lane` if the work crosses subsystems, has a meaningful local/cloud boundary, or needs explicit invariants before coding
   - move to `spec-bundle` with a `full architecture pack` if the likely build includes schema changes, API/event contracts, background jobs, auth/permissions logic, external integrations, or meaningful rollout/cost risk
7. Only after at least one believable signal exists should the idea move toward PRD, spec bundle, and GitHub execution.

## Defaults

- Prefer pain over cleverness.
- Prefer self-observed problems first. A user-zero fit is the strongest fit.
- Prefer ideas that can be tested on the user's own data or public official sources before any external integration work.
- If the builder cannot realistically be the first real user, treat the idea as weaker by default.
- Prefer problems people already solve manually.
- Compare agent value against labor/time/risk replaced, not cheap SaaS anchors.
- Validate distribution early, not after the build.
- Prefer lightweight validation artifacts until the idea has earned architecture work.
- If the value cannot be understood natively from a landing page, example, or self-serve demo without a founder call, treat that as a serious weakness.
- Copying a proven wedge is allowed if it lowers market risk.
- If legal cleanliness depends on "probably nobody will mind", reject the idea.

## Strong Signals

- 5 customer conversations
- repeated pain pattern
- beta interest
- design partner interest
- paid pilot
- early revenue

## Red Flags

- no named buyer
- no clear workaround
- long explanation required
- unclear first channel
- weak personal fit
- PRD or architecture pack appears before any real signal
- contract-bound data or derived work product
- hidden delegation or prohibited tooling required for the wedge

## When to read the reference

If you need the exact one-screen template and fuller heuristics, read:

- `references/playbook.md`
- `references/contract-clean-gate.md`

## Rules

- Do not confuse a detailed spec with a validated market.
- Do not turn a nice idea into a build order before the wedge is clear.
- Do not let architecture planning get ahead of buyer, pain, and signal.
- If the fastest proof path is manual, say so.
- If the idea is boring but clear and monetizable, keep it.
- If the idea is exciting but fragile or support-heavy, cut it.
- If the idea fails the contract-clean gate, park it instead of trying to rescue it with a clever wrapper.
