---
name: public-artifact-lane
description: Turn real work into public-ready artifacts like build diaries, release notes, launch posts, case studies, or demo scripts. Trigger on requests like public artifact, write a launch post, make release notes, turn this work into a post, write a build diary, or prepare a public-facing summary of work.
---

# Public Artifact Lane

Use this skill when the work is real and the goal is a public or shareable artifact, not more code.

Typical prompts:

- `write a build diary from this work`
- `make release notes`
- `turn this into a public post`
- `prepare a launch writeup`
- `make a case study draft`

## Core Principle

Evidence before narrative.

Default workflow:

`collect artifacts -> pick artifact type -> outline -> draft -> detox -> finalize`

## What to do

1. Collect inputs.
   - diffs, issue notes, decisions, metrics, screenshots, or demo results
2. Choose the artifact type.
   - Read `references/artifact-types.md`.
   - Read `references/storage.md` for default save locations.
3. Draft the outline first.
   - keep it short and concrete
4. Write the draft in plain English.
5. Run a detox pass if the text feels generic.
   - use [$ai-writing-detox](~/.codex/skills/ai-writing-detox/SKILL.md)
6. If visuals help, suggest:
   - [$visual-explainer](~/.codex/skills/visual-explainer/SKILL.md)
   - [$illustration-prompt](~/.codex/skills/illustration-prompt/SKILL.md)

## Output rules

- Keep the first screen useful.
- Do not invent results or metrics.
- If something is a goal, label it as a goal.
- Remove private or sensitive details.

## When not to use

- the work is not real yet
- the artifact would leak internal context or private data
- the user only wants a private note
