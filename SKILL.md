---
name: public-artifact-lane
description: Turn real work into public-ready artifacts such as build diaries, release notes, launch posts, case studies, or demo scripts. Use when the goal is a public or shareable artifact grounded in completed work.
---

# Public Artifact Lane

## Metadata
- Trigger when: the work is real and the user wants a public or shareable artifact rather than more code.
- Do not use when: the work is not real yet, the artifact would leak private context, or the user only wants a private note.

## Skill Purpose

Convert real work and evidence into a public-facing artifact that is concrete, trustworthy, and safe to share.

## Instructions
1. Collect the real evidence first: diffs, issue notes, decisions, screenshots, metrics, or demo results. Then choose the artifact type. Read `/Users/nick/.codex/skills/public-artifact-lane/references/artifact-types.md` for artifact selection and `/Users/nick/.codex/skills/public-artifact-lane/references/storage.md` for default save locations only when needed.
2. Draft the artifact from evidence outward. Keep the first screen useful, label goals as goals, and remove private implementation chatter or backstage jargon. If the text feels synthetic afterward, route through `$ai-writing-detox`; if visuals would help, route through `$visual-explainer` or `$illustration-prompt`.
3. Validate the draft for privacy, truthfulness, and clarity before delivery. If the work is not public-safe, say so and stop instead of forcing a shareable version.

## Non-Negotiable Acceptance Criteria
- Evidence beats narrative polish.
- Do not invent results, usage, or metrics.
- Private or sensitive details are removed or the artifact is withheld.
- The artifact type matches the underlying work instead of padding a small change into a fake “launch.”

## Output
- A public-ready draft or saved artifact path.
- The chosen artifact type.
- Any follow-up lane needed before publishing, such as detox, visual support, or legal/privacy review.
- `Next skill options` (only if needed): `$ai-writing-detox` — remove generic AI tone before publishing; `$visual-explainer` — produce a supporting HTML explainer; `$illustration-prompt` — create image direction for the artifact; `$session-to-post` — turn the same work into a session-style diary draft instead of a public artifact.
