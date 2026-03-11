---
name: product-council
description: Use when a product decision is fuzzy, risky, or high-impact and you want a multi-lens council. Trigger on requests like council, product review, go-to-market debate, wedge selection, pricing debate, roadmap prioritization, launch readiness, pre-mortem, or go/no-go review. Use explicit archetypes with evidence and anti-goals, not cosplay of real people.
---

# Product Council

Use this skill when one smart answer is not enough and the risk is in blind spots.

Typical prompts:

- `run a product council on this`
- `stress test this product idea`
- `I need multiple perspectives before we commit`
- `do a go/no-go review`
- `what would a skeptical council say`
- `run a pricing council`
- `do a roadmap council`
- `help me choose the wedge`

## Core Principle

Use named lenses, not celebrity cosplay.

Good council roles are explicit about:

- what they optimize for
- what evidence they trust
- what failure they fear
- what anti-patterns they reject

Bad councils imitate famous personalities and import fake authority.

## Default Council

Use 3-5 lenses depending on the decision:

1. `Product Strategist`
   - asks whether the wedge, buyer, and outcome are sharp enough
2. `Operator Skeptic`
   - asks what breaks in execution, support, onboarding, and workflow reality
3. `Distribution / GTM`
   - asks how this reaches users and why they would care now
4. `User Value`
   - asks whether this removes a painful recurring job or only looks clever
5. `Risk / Economics`
   - asks about cost, reversibility, and downside if we are wrong

Read `references/roles.md` for the role sheet.
Read `references/council-templates.md` when the user wants a council shaped for a specific decision type.

## What to do

1. Start with a short decision brief.
   - problem
   - target user
   - current workaround
   - proposed move
   - key risks
   - what decision is actually being made
2. Run each lens on the same evidence base.
   - Do not feed different facts to different roles.
3. Force disagreement into the open.
   - consensus
   - disagreements
   - hidden assumptions
   - what evidence would change a mind
4. End with one recommendation.
   - go
   - no-go
   - proceed only after specific validation

## Template Selection

- Use the default council when the decision is broad and you mainly need blind-spot reduction.
- Use a named template when the user is deciding one concrete thing such as wedge, pricing, roadmap, or launch.
- Prefer the smallest council that still captures the real disagreement.

Default named templates live in `references/council-templates.md`.

## When to Use Subagents

- Use subagents only when the decision is substantial and the lenses can reason independently.
- For small decisions, keep the council in one thread.

## Rules

- Do not use this for trivial copy tweaks or obvious bug fixes.
- Do not roleplay real people unless the user explicitly asks for it.
- If the user does ask for real people, translate them into principles and disclaim that this is an approximation, not a simulation.
- Evidence beats style.
- The council exists to reduce blind spots, not to make the answer sound grander.
