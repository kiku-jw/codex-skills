---
name: tool-scout
description: Find current external tools, services, libraries, MCP servers, APIs, or models that could solve a concrete task faster than building from scratch. Use when the user needs ecosystem research before spending build time or money.
---

# Tool Scout

## Metadata
- Trigger when: the real question is “what already exists for this?” rather than “how do we implement it ourselves?”.
- Do not use when: the job is obviously smaller than the cost of a tool hunt.

## Skill Purpose

Research the current tool landscape, verify finalists at primary sources, and recommend the smallest honest option set without padding weak candidates into the answer.

## Instructions
1. Clarify the concrete task, constraints, and whether a tool hunt is even justified. If the job is truly trivial, say that and recommend custom code instead of performing fake research theater.
2. Browse the current landscape using primary sources first, with GitHub, official docs, pricing pages, and other relevant discovery sources. Use `/Users/nick/.codex/skills/tool-scout/references/search-patterns.md` for search patterns and `/Users/nick/.codex/skills/tool-scout/references/evaluation-matrix.md` for the comparison frame only when needed.
3. Compare only the strongest 3-6 candidates, dedupe repeated discoveries, and end with a recommendation: `Try first`, `Avoid for now`, or `Build it ourselves instead` when that is honestly the best call.

## Non-Negotiable Acceptance Criteria
- Always browse for this skill; tool ecosystems are time-sensitive.
- Finalists are verified at their own primary sources, not just blog posts or reposts.
- Archived or obviously stale tools are clearly flagged.
- The answer does not inflate weak tools just to hit a list length.

## Output
- A short comparison table covering tool, type, maturity/signals, why it fits, limits, and link.
- A clear recommendation section: `Try first`, `Avoid for now`, or `Build it ourselves instead`.
- If architecture or vendor lock-in risk is material, a note that the choice deserves `$product-council` or `$adr-log`.
- `Next skill options` (only if needed): `$product-council` — debate a high-impact or ambiguous tool choice; `$adr-log` — record the chosen tool and rejected alternatives durably; `$spec-bundle` — turn the chosen tool into contracts, boundaries, and implementation tasks.
