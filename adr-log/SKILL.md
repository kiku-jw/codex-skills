---
name: adr-log
description: Record significant architecture or execution decisions so their reasoning survives the session. Trigger on requests like record this decision, write an ADR, capture the trade-off, or supersede the old decision.
---

# ADR Log

## Metadata
- Trigger when: the task is to capture one real stack, schema, workflow, boundary, or vendor decision with durable rationale.
- Do not use when: the choice is a tiny implementation detail or the decision is still too fuzzy to commit.

## Skill Purpose

Capture one expensive-to-rediscover decision so the chosen path, rejected alternatives, and revisit conditions survive beyond the current chat session.

## Instructions
1. Gate the decision first. Confirm what was chosen, what was rejected, and why this is worth preserving. If the choice is still fuzzy, route to `$product-council` or `$spec-bundle` instead. Read `/Users/nick/.codex/skills/adr-log/references/storage-rules.md` only when you need the storage surface and `/Users/nick/.codex/skills/adr-log/references/entry-template.md` only when you need the exact entry shape.
2. Record one entry in the right durable place: repo ADR file when the decision belongs to code, GitHub issue summary when issue state is canonical, or both when the project already uses `$issue-control-loop`.
3. Validate the record. Make sure it names context, options, chosen path, trade-offs, consequences, revisit conditions, and whether this entry supersedes an older decision.

## Non-Negotiable Acceptance Criteria
- One entry covers one real decision.
- Rejected alternatives and trade-offs are explicit; they are not optional filler.
- If the rationale was reconstructed after the fact, label it as reconstructed instead of pretending it was captured live.
- Superseded decisions are marked as superseded, not silently overwritten.

## Output
- The written ADR or issue summary saved to its durable destination.
- A short summary of the chosen path, the main trade-off, and the revisit trigger.
- The destination path or issue location so the decision can be reopened later.
