---
name: ai-writing-detox
description: Remove obvious AI-writing tics from drafts so the text sounds credible, calm, and human. Trigger on requests like make this sound less AI, detox this draft, or clean up public-facing copy before publishing.
---

# AI Writing Detox

## Metadata
- Trigger when: the draft is directionally fine, but its tone, rhythm, or phrasing still reads like generic model output.
- Do not use when: the draft primarily needs factual reporting, structural rewriting, or a new argument rather than style cleanup.

## Skill Purpose

Remove empty hype, fake authority, and synthetic rhythm while preserving the author’s actual meaning and tone.

## Instructions
1. Inspect the draft and preserve its real intent, structure, and voice. Read `~/.codex/skills/ai-writing-detox/references/patterns.md` only when you need the pattern sheet for common AI markers.
2. Edit for credibility: cut throat-clearing, inflated abstractions, repetitive cadence, and bland transitions; replace them with concrete nouns, verbs, and cleaner rhythm.
3. Return the cleaned draft plus a short note on what changed. If detox alone is not enough because the copy is factually weak or structurally broken, say that explicitly instead of over-polishing it.

## Non-Negotiable Acceptance Criteria
- Meaning stays intact unless the meaning itself was the problem.
- The edit does not become more corporate, more salesy, or more generic than the source draft.
- If factual repair is required, the skill says so instead of hiding behind smoother prose.
- The finished draft sounds human because it is more specific and calm, not because it adds flair.

## Output
- The cleaned draft.
- A short `Changes` list with 3-5 bullets describing what was removed, tightened, or made more concrete.
- An explicit note if the draft still needs reporting, restructuring, or fact-checking beyond detox.
