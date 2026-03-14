---
name: triage-finding
description: Triage an external finding such as a post, article, GitHub repo, screenshot, video, note, or link and decide whether it matters now. Trigger on requests like triage this, look what I found, is this useful, check this out, what should we do with this, review this link, or when the user pastes an external finding and wants a verdict. Best for mapping outside information to current projects, installed skills, and reusable workflows instead of just summarizing.
---

# Triage Finding

Use this skill when the input is an external finding and the real question is whether it deserves action.

Typical prompts:

- `triage this`
- `look what I found`
- `is this useful for us`
- `check this repo/article/video`
- `what should we do with this`
- `review this ideas folder`

## Core Principle

Trust the primary source more than the post about it.

Default workflow:

`inspect source -> fact-check claims -> detect duplicates -> map to current work -> verdict -> smallest next action`

## Modes

1. `Triage a finding`
   - link, post, repo, screenshot, note, transcript, or video
2. `Review saved ideas`
   - a folder of saved findings or idea notes that needs re-triage against current work

## Inputs

This skill works with:

- article links
- GitHub repos
- screenshots
- pasted post text
- notes or transcripts
- videos when enough metadata or transcript is available
- multiple findings at once
- idea folders the user explicitly points to

Read `references/source-handling.md` before choosing the inspection path.
Read `references/verdicts.md` before finalizing the verdict.

## What to do

1. Identify the source type.
   - Read only enough to understand the actual claim.
   - Prefer the primary source over social commentary.
   - If the finding contains a link, inspect the link.

2. Fact-check the finding.
   - If a post claims a repo uses a language, has a license, supports a feature, or shows a metric, verify it against the original source.
   - If the post and the source disagree, say so explicitly.
   - Do not carry forward incorrect claims just because they were repeated confidently.

3. Detect duplicates before recommending action.
   - If the finding is a skill, check `~/.codex/skills/`.
   - If it is a tool, also check obvious local duplicates:
     - current workspace
     - nearby repos
     - installed command or package when easy to verify
   - If it already exists locally or is already in use, say that directly.
   - If the finding is an update to something already installed, evaluate the update itself, not the base tool.

4. Map it to current work.
   - Use the current conversation first.
   - Then use the current workspace, active repos, and obvious nearby work.
   - If work is tracked in GitHub, map the finding to the canonical issue or say that none is visible.
   - If several findings are provided, prioritize the ones that fit active work first.

5. Explain it in plain language.
   - `What is this`
   - `What changed after fact-checking`
   - `Where it applies`

6. Give exactly one primary verdict.
   - `Apply now`
   - `Save for later`
   - `Not relevant`

7. Propose the smallest useful next action.
   - update an existing skill
   - create a new skill
   - open or update a GitHub issue
   - save a short note
   - ignore it

## YouTube fallback

If the finding is a YouTube link, inspect it in this order:

1. title, description, chapters, and linked resources
2. transcript if one can be extracted cheaply
3. web search around the video title if the transcript path fails
4. ask the user for pasted notes only if the content still cannot be verified

If transcript extraction fails, say that the verdict is based on metadata plus supporting sources, not on the full video.

## Review ideas mode

When the user asks to review an ideas folder:

1. Read the files they pointed to.
2. Group ideas by current relevance.
3. Re-triage each item against active work.
4. End with:
   - `Apply now`
   - `Keep for later`
   - `Drop`

If no folder was provided and none is obvious from the current workspace, ask for the path instead of inventing one.

## Output format

Use this structure:

```md
## What is this

## Fact-check notes

## Duplicate check

## Where it applies

## Recommendation: Apply now | Save for later | Not relevant

## Smallest next step
```

For multiple findings, also add a short summary table at the end:

```md
| Finding | Verdict | Why |
```

## Rules

- Do not trust a repost over the original source.
- Do not stretch weak findings into fake relevance.
- If the finding is already installed or already in use, say so before recommending anything else.
- Prefer one concrete recommendation over a broad brainstorm.
- If the finding suggests a repeatable workflow, say whether it should become a skill.
- If the finding changes architecture or product direction, say whether it deserves [$product-council](~/.codex/skills/product-council/SKILL.md) or [$adr-log](~/.codex/skills/adr-log/SKILL.md).
- Do not create files or install tools unless the user asked for that step.
- If the user only wants a gist, stop after the explanation and verdict.
