---
name: skill-creator
description: 'Create or update a Codex skill with a narrow, harness-optimized contract: functional metadata, one short purpose paragraph, at most three execution steps, hard acceptance criteria, and an explicit output format. Use when the user wants a new skill, a skill rewrite, or more reliable skill behavior.'
---

# Skill Creator

## Metadata
- Trigger when: the job is to create a skill, refactor an existing skill, or improve skill reliability instead of solving the underlying domain task directly.
- Do not use when: the user only wants a one-off answer and there is no reusable skill to build.

## Skill Purpose

Turn a skill into a small, durable harness. The skill should tell the agent exactly when to trigger, what to do, what is non-negotiable, and what output shape must exist before the skill can be considered complete.

## Instructions
1. Inspect the target skill directory first. Read `SKILL.md`, only the references/scripts/assets actually needed for the rewrite, and `agents/openai.yaml` if it exists. Use `/Users/nick/.codex/skills/.system/skill-creator/references/openai_yaml.md` when UI metadata needs to be created or checked.
2. Rewrite the skill into one narrow job with this body shape: `Metadata`, `Skill Purpose`, `Instructions`, `Non-Negotiable Acceptance Criteria`, `Output`. Keep the purpose to one short paragraph. Keep `Instructions` to three top-level steps maximum. Push bulky examples, schemas, and variant-specific details into existing `references/` or `scripts/` instead of bloating `SKILL.md`.
3. Validate the result. Frontmatter must contain functional `name` and `description`; script invocations must use exact paths; output format must be explicit; and `agents/openai.yaml` must exist and match the skill. If the skill naturally hands work to another skill, make that handoff explicit inside `Output` or the final instruction: name only the valid next skills in the form `$skill-name` — one-line purpose. Keep the list short and only include real next steps, not a catalog dump. Regenerate or create `agents/openai.yaml` with `/Users/nick/.codex/skills/.system/skill-creator/scripts/generate_openai_yaml.py` and run `/Users/nick/.codex/skills/.system/skill-creator/scripts/quick_validate.py` on the finished skill when possible.

## Non-Negotiable Acceptance Criteria
- One skill owns one real job. If the workflow still needs more than three top-level steps, split the skill or route to another skill instead of expanding the harness.
- Treat “more than 3 stages” as a system-design smell, not a formatting game: prefer a stable parent router plus child skills over one fat skill.
- Metadata stays functional: clear triggers, clear anti-triggers, no vague marketing copy.
- The body stays concise and procedural. Detailed references live in `references/`; deterministic execution lives in `scripts/`.
- When a handoff is part of the real workflow, the skill must name the valid next skill options explicitly instead of leaving chaining implicit.
- The skill does not count as done until the acceptance criteria and output contract can actually be satisfied.

## Output
- Updated skill files written to disk.
- A short note listing which files changed and whether `agents/openai.yaml` was created or regenerated.
- If the rewrite exposed a skill that is too broad, an explicit split recommendation naming the proposed smaller skills or follow-up cuts.
