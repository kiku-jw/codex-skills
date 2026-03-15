# GitHub Mobile Control Surface

Date reference: March 7, 2026.

## Core pattern

- `Issue` holds durable task meaning.
- `Project` shows workflow and operator fields.
- `GitHub Mobile` is good for oversight, triage, comments, and nudges.
- chat is still valuable, but should not be the only source of truth.

## Why Projects matter beyond memory

- They aggregate work across repos.
- They expose operator fields like priority, owner, and next decision.
- They let a human scan the real queue quickly.
- They separate canonical task meaning from board presentation.

## What official GitHub supports

According to GitHub’s current docs:

- Copilot is available in GitHub Mobile.
- You can ask Copilot repo, file, issue, and PR questions in GitHub Mobile.
- You can assign an issue to Copilot from GitHub Mobile.
- The issue-assignment API supports `target_repo`, `base_branch`, `custom_instructions`, `custom_agent`, and `model`.

## Good recommendations

1. Keep the issue canonical.
2. Keep the project readable on a phone.
3. Keep the next human decision explicit.
4. Treat chat as signal, not memory.
5. Automate phone-triggered actions only when they are narrow and reversible.
