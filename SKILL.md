---
name: triage-finding
description: Triage an external finding such as a post, article, GitHub repo, screenshot, video, note, or link and decide whether it matters now. Trigger on requests like triage this, look what I found, is this useful, check this out, what should we do with this, review this link, or when the user pastes an external finding and wants a verdict. Best for mapping outside information to current projects, GitHub tasks, and reusable skills instead of just summarizing.
---

# Triage Finding

Use this skill when the input is an external finding and the real question is whether it deserves action.

Typical prompts:

- `triage this`
- `look what I found`
- `is this useful for us`
- `check this repo/article/video`
- `what should we do with this`

## Core Principle

Usefulness beats novelty.

Default workflow:

`understand source -> explain plainly -> map to current work -> decide now/later/no -> suggest next action`

## Inputs

This skill works with:

- article links
- GitHub repos
- screenshots
- pasted post text
- notes or transcripts
- videos when enough metadata or transcript is available

## What to do

1. Identify the source type.
   - Read only enough to understand the gist and the claim.
   - Prefer the primary source over commentary about it.
2. Explain it in plain language.
   - What it is.
   - Why it exists.
   - Why someone might care.
3. Map it to current work.
   - Check active repos, current issues, recent work, or known priorities from the conversation.
   - If work is tracked in GitHub, map to the canonical issue or suggest creating one.
   - If nothing real matches, say so plainly.
4. Give one verdict.
   - `Apply now`
   - `Save for later`
   - `Not relevant`
5. Propose the smallest next action.
   - create a skill
   - open or update a GitHub issue
   - save a short note
   - ignore it

Read `references/verdicts.md` for verdict rules.
Read `references/source-handling.md` when the source format affects how to inspect it.

## Rules

- Do not stretch weak findings into fake relevance.
- Prefer a specific recommendation over a broad brainstorm.
- If the finding suggests a repeatable workflow, say whether it should become a skill.
- If the finding changes architecture or product direction, say whether it deserves [$product-council](~/.codex/skills/product-council/SKILL.md) or [$adr-log](~/.codex/skills/adr-log/SKILL.md).
- If the user only wants a gist, stop after the explanation and verdict.
