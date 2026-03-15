---
name: github-mobile-ops
description: Explain a phone-first GitHub workflow using Issues as canonical task state, Projects as the operator view, GitHub Mobile as the control surface, and chat as the fast signal path. Use when the user asks how GitHub should work from a phone or lightweight operator surface.
---

# GitHub Mobile Ops

## Metadata
- Trigger when: the user wants a mobile-first control loop for GitHub Issues, Projects, and GitHub Mobile.
- Do not use when: the real task is coding, repo planning, or a generic GitHub tutorial that does not depend on phone-first operation.

## Skill Purpose

Map GitHub’s mobile surfaces into a clean operator model so the user can control work from a phone without pretending the phone is a full development environment.

## Instructions
1. Start from the split: `Issue` is canonical task truth, `Project` is the workflow board, `GitHub Mobile` is the phone control surface, and chat is the fast signal path. Build the advice around that split instead of mixing responsibilities.
2. Recommend the smallest honest phone workflow that fits the request. If the user wants field-level guidance or the fuller operator pattern, read `/Users/nick/.codex/skills/github-mobile-ops/references/mobile-control-surface.md`.
3. Return a concrete operating setup: what lives in the issue, what lives in the project, which fields matter on mobile, and what still needs a laptop.

## Non-Negotiable Acceptance Criteria
- Do not claim the phone replaces the laptop for real coding or deep review.
- Do not blur GitHub Mobile, Copilot features, Telegram/OpenClaw, and local execution into one fake surface.
- The recommendation stays concrete: fields, flows, and operator responsibilities beat platform hype.
- Language stays operator-level and plain.

## Output
- A compact recommended split between issue, project, mobile app, and chat.
- If needed, a minimal project field set such as `Status`, `Priority`, `Owner`, `Next action`, `Blocked`, and `Due date`.
- A short note about what still requires a laptop or fuller desktop workflow.
