---
name: product-council
description: Run a multi-lens council when a product decision is fuzzy, risky, or high-impact and one answer is not enough. Use for wedge selection, pricing, launch readiness, roadmap trade-offs, go/no-go calls, or other decisions where blind spots matter more than speed.
---

# Product Council

## Metadata
- Trigger when: the decision is important enough that multiple explicit lenses would reduce blind spots or hidden risk.
- Do not use when: the task is a trivial copy tweak, obvious bug fix, or any decision where one clear answer is already enough.

## Skill Purpose

Force meaningful disagreement across named lenses that optimize for different evidence and failure modes, then synthesize that disagreement into one recommendation.

## Instructions
1. Start with one short decision brief covering problem, target user, current workaround, proposed move, key risks, and the actual decision to be made.
2. Choose 3-5 lenses and run them on the same evidence base. Use `/Users/nick/.codex/skills/product-council/references/roles.md` for role definitions and `/Users/nick/.codex/skills/product-council/references/council-templates.md` when a named template fits the decision better than the default council.
3. Synthesize the council into consensus points, disagreements, hidden assumptions, evidence that would change a mind, and one final recommendation: go, no-go, or proceed only after specific validation.

## Non-Negotiable Acceptance Criteria
- Use named lenses, not celebrity cosplay or fake authority.
- All lenses reason from the same facts.
- The council produces one recommendation rather than a pile of unranked commentary.
- Evidence outranks performance; the exercise exists to reduce blind spots, not to sound grand.

## Output
- The decision brief.
- Lens-by-lens findings plus explicit disagreements.
- A final recommendation with the key gate or proof needed to move forward.
- `Next skill options` (only if needed): `$idea-validation` — get real buyer/pain/proof signal before committing; `$product-shaping` — structure the chosen product question into one framework; `$spec-bundle` — turn the chosen direction into implementation-ready artifacts; `$adr-log` — record the decision if it is now durable enough.
