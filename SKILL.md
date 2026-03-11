---
name: readme-generator
description: Create or rewrite README.md for a repo. Trigger when the user asks to write, improve, refresh, or restructure a README, landing repo page, open-source intro, setup guide, or project overview. Produce a human-first README with truthful quick start, project-type-specific sections, and no API-dump bloat.
---

# README Generator

Use this skill when the real task is README quality, not code changes.

Typical prompts:

- `write a README for this repo`
- `rewrite this README`
- `make the project page clearer`
- `refresh the open-source intro`
- `fix the setup docs in README`
- `turn this repo into a human-readable landing page`

## Core Principle

README is for humans scanning quickly, not for agents showing off context volume.

Default workflow:

`analyze repo -> identify project type -> choose minimum honest sections -> write concise README`

## What to do

1. Read the repo before drafting.
   - Prefer existing `README.md`, `package.json`, `pyproject.toml`, `Cargo.toml`, `go.mod`, `CLAUDE.md`, main entrypoints, and tests.
   - If the repo already has docs, preserve true facts and cut stale or duplicated material.
2. Identify the project type.
   - CLI tool
   - library / SDK
   - web app
   - full-stack app
   - skill / framework / template
3. Choose the smallest useful README shape.
   - Every README needs: title, one-line value proposition, short description, quick start, usage, and license.
   - Add extra sections only when they reduce confusion.
4. Write for an outsider.
   - Start with what the project does and why it matters.
   - Keep examples runnable.
   - Prefer bullets, tables, and short paragraphs over walls of text.
5. Keep it honest.
   - Name limitations if they matter.
   - Do not imply features, stability, or polish that the repo does not actually have.

## When to Use Web Research

- Prefer repo artifacts first.
- Browse only when framework-specific setup or current external docs materially affect the README.
- When browsing, prefer official docs and primary sources.

## Section Rules

- Always include a minimal `Quick Start`.
- Add `Requirements` when runtime, OS, hardware, or credentials matter.
- Add `Tech Stack` only if the stack is non-trivial or multi-layer.
- Add `Architecture` only when a diagram or system split would reduce confusion.
- Add `Project Structure` only for repos where contributors need orientation.
- Do not dump full API reference into README. Link out or summarize.

Read `references/section-matrix.md` for the section matrix by project type.

## Writing Rules

- Lead with value, not implementation details.
- Keep the first screen useful.
- Use active voice and concrete nouns.
- Avoid generic hype words like `powerful`, `robust`, `next-generation`.
- Prefer one honest example over five vague claims.
- If the repo contains skills, MCP servers, or multiple tools, make the taxonomy explicit.

## Common Failure Modes

- README starts with architecture before value.
- Quick start is too long or missing.
- Usage examples do not match the real CLI or API.
- The README reads like internal notes instead of a public front page.
- Every section is present whether or not it helps.
