---
name: long-context-dispatch
description: Delegate a large read-only cross-document or cross-file analysis to the verified long-context worker while the ordinary Codex thread stays in control. Use for big audits, due diligence, large literature synthesis, policy mapping, or other tasks that genuinely need much larger context.
---

# Long Context Dispatch

## Metadata
- Trigger when: the current thread should stay in control but the analysis genuinely needs a much larger read-only context window.
- Do not use when: the task is ordinary coding, a short review, or anything that comfortably fits in the current thread.

## Skill Purpose

Use the long-context worker as a read-only analysis surface, then synthesize the result back into the parent Codex thread without handing off final judgment.

## Instructions
1. Gate the need honestly. If the task is not a strong long-context candidate, do nothing special and continue normally. If it is, get one short confirmation from the user before launch.
2. Launch the dispatcher with the exact script `/Users/nick/.codex/skills/long-context-dispatch/scripts/long_context_dispatch.py`. Put the request in a temporary Markdown file, pass an explicit `--cwd`, `--reason`, and `--scope`, and keep the child job read-only.
3. While the job runs, relay brief human updates instead of raw JSON. On success, read `result.md` and synthesize its findings back into the current thread. On failure, report the exit code, a short error summary, and the artifact paths with a concrete retry suggestion.

## Non-Negotiable Acceptance Criteria
- The child worker stays read-only.
- One child job per parent request is the default; do not fragment the analysis without a reason.
- The parent Codex thread owns synthesis, editing decisions, and next steps.
- If the user wants an interactive long-context session rather than delegated analysis, route them to the dedicated launcher/app instead of forcing this skill.

## Output
- A short launch note with job id and scope when dispatch starts.
- A synthesized result covering summary, key findings, cross-file connections, next actions, and open questions when the job succeeds.
- If the job fails: exit code, short error summary, and artifact paths.
- `Next skill options` (only if needed): `$spec-bundle` — turn large-scope analysis into implementation-ready artifacts; `$adversarial-review` — stress-test findings against actual changed behavior; `$tool-scout` — research the external landscape if the analysis exposed a buy-vs-build question.
