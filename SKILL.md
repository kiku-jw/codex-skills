---
name: work-shaping
description: "Use before coding when the main question is how much process the work deserves: tiny vs substantial, chat vs GitHub, checklist vs execution brief, architecture lane vs full architecture pack, operator review vs council, private diary vs public draft."
---

# Work Shaping

Use this skill when the user is not blocked by code yet, but by the shape of the work.

Typical prompts:

- `это большая задача или мелочь`
- `нужно ли заводить issue`
- `стоит ли это тащить в блог`
- `тут нужен консилиум или можно просто делать`
- `сколько процесса вообще нужно`

## What to do

1. Classify the work on six axes:
   - `tiny` or `substantial`
   - `chat`, `local note`, or `GitHub issue`
   - `none`, `lightweight checklist`, or `execution brief`
   - `none`, `light architecture lane`, or `full architecture pack`
   - `none`, `operator review`, or `council`
   - `none`, `private diary`, or `public draft`
2. Prefer the smallest honest process.
3. If the architecture lane is not `none`, route the work into `spec-bundle` and keep architecture in durable artifacts, not in chat.
4. If the user already implied action, do not stop at classification. Move to the next step.

## Heuristics

- `substantial` if the work spans sessions, touches multiple files/systems/repos, changes user-facing behavior, or carries rollout/security risk.
- `GitHub issue` if the work needs handoff, review, or durable tracking.
- `execution brief` if ambiguity would slow coding down more than writing the brief.
- `light architecture lane` if the work crosses more than one subsystem, has a meaningful local/cloud boundary, or needs a small system map before coding.
- `full architecture pack` if the work includes schema changes, public API or event contracts, background jobs, auth/permissions changes, external integrations, or meaningful rollout/cost risk.
- `council` only if there is a real tradeoff, hidden risk, or high-impact choice.
- `public draft` only if there is a public-safe artifact or lesson. Do not build public writing on private kitchen.

## Rules

- Do not add ceremony for tiny reversible work.
- Do not let meaningful work disappear into chat.
- Make the architecture lane explicit for risky work instead of burying it in a vague PRD.
- Use hard gates only for irreversible or expensive choices. Use soft gates everywhere else.
- Be explicit about what is already real versus what is only a good next step.
