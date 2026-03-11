---
name: adr-log
description: Record significant architecture or execution decisions so their reasoning survives the session. Trigger on requests like record this decision, ADR, architecture decision, why did we choose this, log the trade-off, supersede the old decision, or when a meaningful stack, schema, workflow, or vendor choice is made. Best when a choice affects future implementation, review, or reversibility.
---

# ADR Log

Use this skill when a decision is expensive enough to deserve durable reasoning.

Typical prompts:

- `record this decision`
- `write an ADR`
- `log why we chose this`
- `supersede the old decision`
- `capture the trade-off`

## Core Principle

The rejected alternatives are part of the asset.

Default workflow:

`identify real decision -> decide whether it deserves ADR -> store in the right place -> record options and trade-off -> sync the durable summary`

## What counts as ADR-worthy

- stack or vendor choice
- schema or storage pattern
- API or contract shape
- workflow architecture
- deployment or boundary decision
- any decision that will be expensive to rediscover

Do not use this for tiny implementation details.

Read `references/storage-rules.md` for where to store the record.
Read `references/entry-template.md` for the entry shape.

## What to do

1. Confirm the decision is real.
   - what was chosen
   - what was rejected
   - why now
2. Decide the storage surface.
   - repo ADR file when the decision belongs to code
   - GitHub issue summary when the task is issue-driven
   - both when the project already uses [$issue-control-loop](~/.codex/skills/issue-control-loop/SKILL.md)
3. Record the decision.
   - context
   - options
   - chosen path
   - consequences
   - revisit conditions
4. If this replaces an older decision, mark it as superseded instead of silently overwriting history.

## Rules

- Prefer one entry per real decision.
- Be explicit about trade-offs and reversibility.
- If the rationale is uncertain, label it as reconstructed rather than pretending.
- If the decision is still fuzzy, route first to [$product-council](~/.codex/skills/product-council/SKILL.md) or [$spec-bundle](~/.codex/skills/spec-bundle/SKILL.md).
