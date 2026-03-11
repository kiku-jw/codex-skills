---
name: tool-scout
description: Find external tools, services, libraries, MCP servers, APIs, or models that can solve a concrete task faster than building from scratch. Trigger on requests like find tools for, what should we use for, what already exists for this, research options, best tool for this, compare services, or when the user needs current options before spending build time or money.
---

# Tool Scout

Use this skill when the question is not how to code it, but what should exist in the market or ecosystem already.

Typical prompts:

- `find tools for this`
- `what should we use for X`
- `research options before we build`
- `compare services for this task`
- `is there an MCP for this`

## Core Principle

Freshness and fit beat popularity.

Default workflow:

`clarify task -> search current options -> compare by fit and maturity -> recommend -> define next step`

## What to do

1. Clarify the task briefly.
   - outcome needed
   - constraints
   - budget or tolerance for paid tools
   - whether build-vs-buy is actually open
2. Search the current landscape.
   - Prefer primary sources: official docs, official repos, pricing pages.
   - Freshness matters. Check recent availability and maintenance.
3. Group candidates by type.
   - MCP server
   - SaaS or hosted service
   - open-source library
   - API
   - model
4. Compare only the strongest candidates.
   - Usually 3-6 is enough.
5. End with a recommendation.
   - what to try first
   - what to avoid
   - whether the right answer is still to build it ourselves

## Output format

Return a short table and a final recommendation:

```
| Tool | Type | Maturity | Why it fits | Main limits | Link |
```

Then end with:

- `Try first`
- `Avoid for now`
- `Build ourselves`

Read `references/evaluation-matrix.md` for the comparison frame.
Read `references/search-patterns.md` for query patterns and source priorities.

## Rules

- Use web research because tool ecosystems change fast.
- Verify recent activity (release date, docs update, or repo activity).
- Do not recommend dead, abandoned, or obviously stale options.
- Do not pad the list with mediocre tools.
- Say directly when the task is simple enough that custom code is the better move.
- If the result changes architecture or vendor risk materially, suggest [$product-council](~/.codex/skills/product-council/SKILL.md) or [$adr-log](~/.codex/skills/adr-log/SKILL.md).
