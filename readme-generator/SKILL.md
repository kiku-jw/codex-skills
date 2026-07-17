---
name: readme-generator
description: Create or rewrite `README.md` for a repo. Use when the user wants a clearer landing page, setup guide, open-source intro, project overview, or README refresh rooted in the actual repo rather than generic boilerplate.
---

# README Generator

## Metadata
- Trigger when: the real task is README quality, not feature implementation.
- Do not use when: the repo facts are unknown and no source artifacts are available to ground the README.

## Skill Purpose

Produce a human-first README that quickly tells an outsider what the repo does, how to start, and what matters, without turning the page into API dump clutter.

## Instructions
1. Read the repo before drafting: existing `README.md`, package or build manifests, main entrypoints, and tests when useful. Preserve true facts and cut stale or duplicated material.
2. Choose the smallest honest README shape for the repo type. Use `/Users/nick/.codex/skills/readme-generator/references/section-matrix.md` when you need the section matrix. Add only the sections that materially reduce confusion.
3. Write for an outsider, not for an agent. Browse only when current official framework docs materially affect setup or usage, and prefer primary docs when you do.

## Non-Negotiable Acceptance Criteria
- The first screen explains value and has a truthful quick start.
- Usage examples match the real repo interface.
- The README does not become an API dump, internal note file, or architecture lecture unless the repo genuinely needs that.
- Limitations or unstable status are named when they matter.

## Output
- The updated `README.md` path.
- A short note on the chosen section set and the repo type it was optimized for.
- Any external docs used to verify setup or usage details.
