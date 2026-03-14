---
name: tool-scout
description: Find external tools, services, libraries, MCP servers, APIs, or models that can solve a concrete task faster than building from scratch. Trigger on requests like find tools for, what should we use for, what already exists for this, research options, best tool for this, compare services, is there an MCP for this, or when the user needs current options before spending build time or money.
---

# Tool Scout

Use this skill when the real question is not how to build it, but whether the ecosystem already has a better answer.

Typical prompts:

- `find tools for this`
- `what should we use for X`
- `research options before we build`
- `compare services for this task`
- `is there an MCP for this`

## Core Principle

Search adaptively, verify at the source, and stop early when the task is too small to justify a tool hunt.

Default workflow:

`clarify task -> decide if search is even warranted -> choose sources -> collect current candidates -> dedupe -> compare -> recommend`

Read `references/search-patterns.md` for source selection and query patterns.
Read `references/evaluation-matrix.md` for the comparison frame and output rules.

## What to do

1. Clarify the task briefly.
   - outcome needed
   - stack or runtime constraints
   - hosted service vs local library vs MCP preference
   - budget or tolerance for paid tools

2. Decide whether this is a real tool-scout task.
   - If the job is trivial, say so directly.
   - Examples:
     - a one-off format conversion
     - a thin wrapper over an existing SDK
     - a tiny script that is easier than integrating a product
   - In those cases, recommend custom code instead of padding the answer with tools.

3. Choose sources adaptively.
   - `Web search` for current market options, docs, pricing, and comparisons.
   - `GitHub search` for repos, libraries, MCP servers, and open-source tools.
   - `MCP catalogs` when the user asks for MCP servers or Claude/Codex-adjacent integrations.
   - `Awesome-lists` when a curated landscape is likely to exist.
   - `Package registries` only after discovery, mainly to verify the finalists.
   - If unsure, use all relevant sources instead of guessing wrong.

4. Search the current landscape.
   - Prefer primary sources:
     - official docs
     - official repo
     - official pricing or product page
   - Use comparison articles and awesome-lists for discovery, not as the final authority.
   - If `gh` is available, use it for repo discovery and quick star signals.
   - If `gh` is not available, fall back to web search with `site:github.com`.

5. Deduplicate aggressively.
   - If the same tool appears in multiple sources, keep one row.
   - Aggregate discovery signals instead of duplicating entries.
   - Mention when a tool was found repeatedly across the ecosystem, because that raises confidence.

6. Evaluate only the strongest candidates.
   - Usually 3-6 is enough.
   - Prefer fit, freshness, and integration cost over sheer popularity.
   - Mark archived or obviously stale repos as red flags.

7. End with a recommendation.
   - `Try first`
   - `Avoid for now`
   - `Build it ourselves instead` when that is honestly the better move

## Source rules

- Always browse for this skill. Tool ecosystems change fast.
- For MCP servers, check both catalogs and GitHub.
- For awesome-lists, read the list README, then verify finalists at their own primary sources.
- For package discovery, do not start from raw npm or PyPI dumps unless the user asked for package-only research.
- GitHub stars are a signal, not proof.
- Archived status is a strong warning signal.
- A small stable tool is not bad just because it is quiet.

## Output format

Return a short comparison table:

```md
| Tool | Type | Maturity | Signals | Why it fits | Main limits | Link |
```

Then end with:

- `Try first`
- `Avoid for now`
- `Build it ourselves instead` when appropriate

If the user asked about several distinct tasks, split the answer by task instead of mixing all tools into one pile.

## Rules

- Do not recommend abandoned or obviously stale tools without warning.
- Do not inflate a mediocre option just to hit a list length.
- If a tool is a strong fit only under a specific stack or budget, say so plainly.
- If the recommendation would materially affect architecture, vendor risk, or lock-in, suggest [$product-council](~/.codex/skills/product-council/SKILL.md) or [$adr-log](~/.codex/skills/adr-log/SKILL.md).
- If there is no good candidate, say that directly.
