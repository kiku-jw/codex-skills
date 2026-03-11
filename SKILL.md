---
name: ai-writing-detox
description: Remove obvious AI-writing tics from drafts so the text sounds credible, calm, and human. Trigger on requests like make this sound less AI, detox this draft, polish this post, clean up this README copy, edit for trust, or before publishing any public-facing writing where generic LLM style would hurt credibility.
---

# AI Writing Detox

Use this skill when a draft is directionally fine but still reads like generic model output.

Typical prompts:

- `make this sound less AI`
- `detox this draft`
- `polish this post before publishing`
- `clean up this README copy`
- `remove AI tics from this`

## Core Principle

Credibility beats flourish.

Default workflow:

`identify AI markers -> cut empty language -> smooth rhythm -> keep meaning -> return cleaner draft`

Read `references/patterns.md` for the main signatures to remove.

## What to do

1. Keep the meaning and structure unless they are part of the problem.
2. Remove empty hype, throat-clearing, and fake authority.
3. Fix choppy AI rhythm.
4. Prefer concrete nouns and verbs over puffed-up abstractions.
5. Preserve the user's actual tone instead of flattening it into generic "professional" prose.

## Rules

- Do not make the text more corporate in the name of polish.
- Do not add marketing energy the draft did not ask for.
- If the draft needs reporting or factual repair, say that detox alone is not enough.
- For journalism-like copy, suggest a stricter newsroom-style pass only if that workflow exists in the current environment.

## Output

- Return the cleaned draft.
- Add a short `Changes` list with 3-5 bullets describing what you removed or simplified.
