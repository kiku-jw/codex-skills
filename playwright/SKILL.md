---
name: playwright
description: Drive a real browser from the terminal with the bundled Playwright CLI wrapper. Use when the task requires navigation, form filling, snapshots, screenshots, data extraction, or UI-flow debugging without turning the job into a Playwright test suite.
---

# Playwright CLI Skill

## Metadata
- Trigger when: the user needs browser automation or browser-state inspection from the terminal.
- Do not use when: the task is to author Playwright test files or when a different built-in browser tool already solves the job better.

## Skill Purpose

Provide a deterministic CLI-first browser workflow that always starts from a fresh snapshot and uses stable element refs instead of ad hoc DOM poking.

## Instructions
1. Check prerequisites first: `command -v npx >/dev/null 2>&1`. If `npx` is missing, stop and ask the user to install Node/npm. Otherwise use the exact wrapper script at `/Users/nick/.codex/skills/playwright/scripts/playwright_cli.sh`.
2. Run the core loop through the wrapper: open the page, snapshot, interact using refs from the latest snapshot, and snapshot again after navigation or major DOM change. Use `/Users/nick/.codex/skills/playwright/references/cli.md` for command reference and `/Users/nick/.codex/skills/playwright/references/workflows.md` for troubleshooting only when needed.
3. Capture artifacts such as screenshots, PDFs, or traces when they help. Keep the workflow explicit and CLI-based; do not pivot into Playwright test code unless the user explicitly asked for test files.

## Non-Negotiable Acceptance Criteria
- Always snapshot before using element refs like `e12`.
- Re-snapshot after navigation, modal changes, tab switches, or any UI change that could stale refs.
- Prefer explicit CLI commands over `eval`/custom code when the wrapper can already do the job.
- Use `--headed` when a visual check materially helps.

## Output
- A concise command sequence or workflow summary.
- Latest relevant element refs or artifact paths when the task depends on them.
- A short note on whether the flow succeeded, stalled on stale refs, or needs a new snapshot.
