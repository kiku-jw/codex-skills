# Lazy Senior Failure Patterns

Use this when forward-tests or real tasks show the skill missing its own standard.

## Pattern: Unverifiable GitHub Prior Art

- Symptom: The agent writes `GitHub prior art: used` without a query, URL, inspected repo, or adoption decision.
- Root cause: The skill asked for a GitHub check but did not force evidence.
- Correct approach: Include `GitHub evidence: <query or URL> -> <useful result>; adoption=<decision>`.
- Avoid: Treating a plausible memory or generic claim as current GitHub evidence.

## Pattern: Tiny Local Code Mislabelled As Stdlib

- Symptom: The agent writes a small custom loop or map but reports `stdlib has it`.
- Root cause: Reporting labels did not distinguish real stdlib reuse from tiny local code.
- Correct approach: Use `lazy-senior: tiny local code was cheaper`.
- Avoid: Inflating tiny local code into a dependency, or pretending it was a built-in.

## Pattern: Receipt Lost In The Work Log

- Symptom: The agent emits a useful decision receipt while working, but the final answer only says what changed.
- Root cause: The skill did not require final receipt repetition.
- Correct approach: Repeat the compact receipt in the final response whenever files changed.
- Avoid: Making the user infer the lower rung from the diff.

## Pattern: Worker As Authority

- Symptom: The main agent follows the read-only Codex worker verdict without checking local constraints.
- Root cause: Delegation replaced judgment.
- Correct approach: Treat worker output as skeptical review. Main agent owns implementation and verification.
- Avoid: Nested workers, write-capable workers, or unverified worker claims.

## Pattern: Hard Gates Too Early

- Symptom: A hook or wrapper blocks normal small edits and creates process drag.
- Root cause: Guardrails were added before repeated failures justified them.
- Correct approach: Add hard gates only after a concrete recurring failure.
- Avoid: Broad shell hooks for a narrow procedural skill.
