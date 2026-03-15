---
name: visual-explainer
description: Create a self-contained HTML explainer for systems, workflows, diagrams, timelines, comparisons, or data-heavy summaries when plain terminal text would be painful to read. Use when the output naturally wants a visual artifact instead of chat prose.
---

# Visual Explainer

## Metadata
- Trigger when: the best output is a browser-readable HTML artifact rather than a wall of text.
- Do not use when: a short plain-text answer would already communicate the structure clearly.

## Skill Purpose

Show structure visually through a single portable HTML artifact so complex systems, tables, and flows become readable at a glance instead of buried in chat.

## Instructions
1. Choose the right visualization type first. Use `/Users/nick/.codex/skills/visual-explainer/references/routing.md` if you need help selecting between architecture, timeline, comparison, table, or other visual forms.
2. Build one self-contained HTML artifact with one clear visual direction. Reuse templates from `/Users/nick/.codex/skills/visual-explainer/assets/templates` when they help, and validate against `/Users/nick/.codex/skills/visual-explainer/references/style-rules.md` and `/Users/nick/.codex/skills/visual-explainer/references/quality-checks.md` before delivery.
3. Save the file to a sensible workspace path, open or inspect it when possible, and return the path plus a short note about what the artifact shows.

## Non-Negotiable Acceptance Criteria
- Prefer semantic HTML and a useful first screen over generic dashboard sludge.
- The output is one self-contained `.html` file unless the user explicitly asked for a multi-file artifact.
- Use Mermaid only when automatic layout helps more than it hurts.
- If the user asked for a wide table or large structured comparison, render it in HTML instead of pasting a painful terminal table.

## Output
- The HTML file path.
- A short description of what the explainer shows and how it is organized.
- Any note about template reuse, browser inspection, or unresolved visual caveats.
