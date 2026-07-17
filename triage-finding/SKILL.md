---
name: triage-finding
description: Triage an external finding such as a post, article, repo, screenshot, video, note, or link and decide whether it matters now. Use when the user wants a verdict, not just a summary.
---

# Triage Finding

## Metadata
- Trigger when: the input is an outside finding and the real question is whether it deserves action in the current context.
- Do not use when: the user only wants a raw summary and no verdict or routing decision.

## Skill Purpose

Inspect an external finding against the primary source, local reality, and current work so the result is a usable verdict instead of yet another pile of interesting links.

## Instructions
1. Inspect the primary source first and fact-check the main claim. Use `/Users/nick/.codex/skills/triage-finding/references/source-handling.md` when you need source-type handling rules.
2. Check for local duplicates or existing use before recommending action, then map the finding to current work, repos, or issue state. If it is already installed or already in use, say that before anything else.
3. Give exactly one primary verdict and the smallest useful next action. Use `/Users/nick/.codex/skills/triage-finding/references/verdicts.md` only when you need the verdict frame.

## Non-Negotiable Acceptance Criteria
- Primary source truth beats repost or commentary.
- Weak findings do not get stretched into fake relevance.
- The answer names whether the finding is already installed, duplicated, or already in use.
- Do not install tools or create files unless the user explicitly asked for that step.

## Output
- A structured verdict with `What is this`, `Fact-check notes`, `Duplicate check`, `Where it applies`, `Recommendation`, and `Smallest next step`.
- For multiple findings, a short summary table of verdicts.
- One clear primary recommendation: apply now, save for later, or not relevant.
- `Next skill options` (only if needed): `$tool-scout` — research the broader external landscape around the finding; `$skill-creator` — turn a reusable workflow insight into a skill; `$product-council` — stress-test a finding that could change direction; `$adr-log` — record a finding that has turned into a durable decision.
