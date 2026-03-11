---
name: visual-explainer
description: Create self-contained HTML explainers for systems, workflows, diagrams, architecture, comparisons, timelines, or data-heavy summaries when plain terminal text would be painful to read. Trigger on requests like diagram this, visualize this, show me the architecture, make a table I can read, render this as HTML, explain this system visually, or when the output naturally wants a structured visual artifact instead of chat prose.
---

# Visual Explainer

Use this skill when the best output is a browser-readable artifact, not a wall of text.

Typical prompts:

- `visualize this`
- `make a diagram for this system`
- `render this table as HTML`
- `show me the architecture visually`
- `turn this into a readable explainer`

## Core Principle

If the structure matters, show the structure.

Default workflow:

`pick visualization type -> choose one clear aesthetic -> generate self-contained HTML -> validate readability -> share file path`

## When to use

- architecture overviews
- flowcharts and pipelines
- side-by-side comparisons
- timelines
- dashboards or metric summaries
- data tables too large for comfortable chat output
- diff or system explainers where spatial grouping matters

## What to do

1. Pick the right format.
   - Read `references/routing.md`.
2. Choose one visual direction.
   - Make it intentional, not generic.
   - Read `references/style-rules.md`.
3. Build a self-contained HTML artifact.
   - Use one of the templates in `assets/templates/` when helpful.
4. Save the file in a sensible workspace location.
   - Prefer a descriptive filename.
5. If browser tooling is available, open or inspect the result.
6. Return the file path and a short note about what it shows.

## Output rules

- Prefer semantic HTML over div soup when tables or lists are involved.
- Use Mermaid only when automatic layout helps more than it hurts.
- Keep the first screen informative.
- Avoid generic dark-dashboard slop.
- If the user asked for a table with many rows or columns, render HTML instead of pasting a wide ASCII table.

## File rules

- Output should be one self-contained `.html` file unless the user asks otherwise.
- Inline CSS and small JS are preferred for portability.
- Use CDN assets only when they materially help, such as Mermaid or Chart.js.

## References

- Read `references/routing.md` to choose the visualization type.
- Read `references/style-rules.md` for typography, color, spacing, and accessibility guardrails.
- Read `references/quality-checks.md` before delivery.
