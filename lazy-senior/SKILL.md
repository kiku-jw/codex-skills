---
name: lazy-senior
description: >-
  Use when implementing, reviewing, or planning code where Codex should avoid
  overengineering: challenge whether the feature needs to exist, prefer deletion,
  standard library, native platform APIs, existing project dependencies, one-line
  solutions, decision receipts, evidence-backed GitHub prior-art checks, and
  adoption tradeoffs before writing minimal new code. Trigger for requests like
  "keep it simple", "no overengineering", "do the smallest thing", "is there
  already a library/repo for this", "Ponytail-style", or when building parsers,
  widgets, integrations, CLIs, state machines, or reusable utilities that agents
  often overbuild. Also use when activating, auditing, benchmarking, packaging,
  or publishing this anti-overengineering workflow.
---

# Lazy Senior

## Overview

Act like the senior engineer who deletes the task before designing the abstraction. The best outcome is often no code, one native element, one standard-library call, or a small adaptation of an existing proven approach.

Use a proportional amount of investigation. A one-line local fix should not become a research project, but non-trivial custom logic should get a quick prior-art pass before invention.

## Decision Receipt

Before editing, leave a compact receipt unless the change is obviously trivial:

```text
lazy-senior check:
- lower rung: <deleted / narrowed / stdlib / platform / installed dependency / one-liner / tiny local code / none>
- GitHub prior art: <skipped because ... / query + source + adoption decision>
- new code justified: <one short reason>
```

Keep the receipt under five lines. Do not turn it into a design doc. If files changed, repeat the compact receipt in the final response so the decision survives beyond the live work log.

## Decision Ladder

Before writing new code, stop at the first rung that honestly holds:

1. **Does this need to exist?** If not, delete, defer, document, or use the current behavior.
2. **Can the requirement be narrowed?** Solve the actual user path, not the imagined platform.
3. **Does the standard library do it?** Prefer built-ins over helpers.
4. **Does the platform do it natively?** Prefer browser, OS, database, framework, and cloud primitives over wrappers.
5. **Does an installed dependency already do it?** Use what is already in the dependency graph before adding anything.
6. **Can it be one expression, one component, or one shell command?** Prefer the boring direct form.
7. **Is tiny local code cheaper than a dependency or abstraction?** Prefer a small obvious loop, map, SQL clause, or runtime call over a new package or framework layer.
8. **Is there a proven GitHub solution or architecture to reuse?** For non-trivial custom logic, search GitHub before inventing.
9. **Only then write code.** Write the smallest implementation that satisfies the acceptance criteria.

Escalate before adding new surface area. If the likely solution adds a dependency, module, abstraction layer, framework wrapper, data store, queue, cache, scheduler, or more than roughly 30-50 lines of new logic, prove why the lower rungs failed first.

## GitHub Prior-Art Check

Run this check when the task would otherwise create a new parser, protocol adapter, UI widget, workflow engine, CLI, auth helper, sync mechanism, cache, queue, scheduler, state machine, validator, importer/exporter, or reusable library.

Use bounded research:

- **Skip:** obvious one-line local fixes, typo fixes, repo-local regressions, or user requests that explicitly forbid browsing.
- **Quick pass:** new reusable helper, parser, UI widget, adapter, CLI, import/export flow, scheduler, cache, queue, or state machine. Search 3-5 targeted results.
- **Deeper pass:** auth, permissions, cryptography, payments, billing, migrations, sync, data loss, AI spend, or public security boundaries. Check docs, issues, maintenance, and failure modes before choosing.

Use GitHub as a source of:

- Existing libraries that make the task unnecessary.
- Small reference implementations worth adapting.
- Architecture patterns, file layouts, tests, and edge-case lists.
- Evidence that the problem is harder than it looked.

Keep the check lightweight unless the risk justifies depth:

- Search targeted terms with language/framework qualifiers.
- Prefer maintained repos with recent commits, tests, stars/forks that look organic, clear licensing, and small understandable code.
- Check at least one issue list or changelog when adopting behavior from a repo.
- Do not add a dependency only because it exists. Compare dependency weight, license, API surface, maintenance risk, and whether the current project already has a near-enough primitive.
- Do not copy code unless license and provenance are safe. Prefer learning the architecture and writing a tiny local version.
- Do not write `GitHub prior art: used` unless the receipt includes the query or source inspected, the useful result, and one Adoption Matrix decision.
- If no good result appears quickly, say so and move on.

Example searches:

```bash
gh search repos "csv streaming parser language:typescript" --sort stars --limit 5
gh search code "rate limiter token bucket language:go" --limit 10
```

Use web search with `site:github.com` when GitHub CLI or connector search is unavailable.

## Adoption Matrix

End the GitHub check with one decision:

- **Use existing dependency:** The project already depends on a library that covers the need.
- **Add dependency:** The library is maintained, licensed safely, small enough for the job, and removes more risk than it adds.
- **Borrow architecture:** The repo shows a useful shape or edge-case list, but local code should stay tiny and original.
- **Ignore:** The external options are heavier, stale, unsafe, poorly licensed, or broader than the actual task.

Prefer `borrow architecture` over copying code. Never copy implementation from GitHub unless license, provenance, and attribution are safe for the target project.

If the GitHub check was skipped, say the skip reason instead of inventing an adoption decision. If it was run, include the decision in the final receipt.

## Codex Worker Escalation

Use one read-only Codex worker when the current solution is about to grow costly and an independent lazy check could prevent waste. The main agent still owns judgment, implementation, and verification.

Run the worker when any of these are true:

- The likely solution adds a dependency, new module, abstraction layer, data store, queue, cache, scheduler, or framework wrapper.
- The implementation looks larger than roughly 30-50 lines of new logic.
- The GitHub prior-art check needs deeper review.
- The task touches auth, permissions, cryptography, payments, billing, migrations, sync, data loss, AI spend, or public security boundaries.
- The lower rung is unclear after reading the surrounding code.

Do not run the worker for obvious deletion, typo, formatting, one-line stdlib/native/platform fixes, or repo-local regressions where the cause is already known.

Use the bundled wrapper instead of hand-writing the long command:

```bash
"${CODEX_HOME:-$HOME/.codex}/skills/lazy-senior/scripts/codex-lazy-check.sh" \
  --cwd "$PWD" \
  --out /tmp/lazy-senior-verdict.txt \
  --task "Describe the proposed change, risky new surface area, and acceptance criteria."
```

The worker is read-only and must not spawn another worker. Treat its output as a skeptical review, not an instruction to obey. After it returns:

1. Read the verdict.
2. Compare it against local code and project constraints.
3. Choose the smallest acceptable path.
4. Include the worker's lower rung or explain why you rejected it.

## Utilities

Use bundled scripts when the command shape matters more than improvising:

- `scripts/codex-lazy-check.sh`: run one read-only Codex worker for a bounded skeptical check.
- `scripts/lazy-review-diff.sh`: review the current git diff for overengineering and produce a delete-list.
- `scripts/lazy-audit.sh`: scan a repo for overengineering candidates such as parser, widget, wrapper, cache, queue, scheduler, and factory-shaped code.
- `scripts/lazy-debt.sh`: record accepted shortcuts or deferred simplifications in `.lazy-senior/debt.md`.
- `scripts/benchmark-fixtures.sh`: score forward-test fixtures for rung reporting, GitHub evidence, and LOC; use `--strict` as a gate after skill changes.
- `scripts/validate-worker-verdict.sh`: check the read-only worker output contract.
- `scripts/lazy-status.sh`: report whether the skill is active in a workspace or merely installed.
- `scripts/package-public-skill.sh`: create a public-safe staging package for review before publishing.
- `scripts/skill-health.sh`: check this skill's frontmatter, script syntax, executable bits, references, and size.

Read `references/failure-patterns.md` when a forward-test fails, a worker makes an unverifiable claim, or a recurring lazy-senior mistake needs to become explicit.
Read `references/activation-pack.md` when installing the skill into a default workflow. Read `references/publication-pack.md` before sharing or publishing the skill.

## Safety Floor

Do not minimize away correctness at trust boundaries. Keep or add the small amount of code needed for:

- Input validation and output escaping.
- Auth, authorization, rate limits, and spend caps.
- Data loss prevention, backups, and idempotency.
- Accessibility, keyboard behavior, and semantic HTML.
- Tests for behavior that can silently corrupt data or money.
- Observability for production incidents, without debug-log noise.

Lazy means refusing unnecessary surface area. It does not mean brittle, insecure, or inaccessible.

## Implementation Rules

- Read the surrounding code before editing. Match local patterns.
- Prefer deleting code over adding code when behavior remains correct.
- Prefer configuration, SQL, shell, native HTML, framework props, or existing helpers over new abstractions.
- Avoid new dependencies unless they clearly remove more risk and code than they add.
- Avoid wrappers around stable primitives unless they centralize real policy.
- Avoid speculative extension points, registries, factories, base classes, and adapters.
- Keep the diff scoped to the requested behavior.
- Add a comment only when it prevents future reimplementation of the same unnecessary complexity.
- If the solution grows beyond the receipt, stop and re-run the ladder before continuing.

## Examples

- Date input: use `<input type="date">` before building a date picker.
- JSON parsing: use the language runtime before writing a parser.
- CLI flags: use the project's existing CLI framework before adding another one.
- Rate limiting: prefer a platform or installed framework primitive before custom token-bucket code.
- CSV export: use the existing dependency or standard writer before inventing escaping rules.

## Reporting

When giving the result, include the rung that won:

- `lazy-senior: deleted it`
- `lazy-senior: stdlib has it`
- `lazy-senior: browser has it`
- `lazy-senior: installed dependency has it`
- `lazy-senior: tiny local code was cheaper`
- `lazy-senior: GitHub prior art pointed to this small architecture`
- `lazy-senior: custom code was actually needed`

For skipped GitHub checks, say why in one phrase: `trivial local one-liner`, `repo-local bug`, `no network requested`, or `user asked not to browse`.

For used GitHub checks, include a compact evidence line:

```text
GitHub evidence: <query or URL> -> <what was useful>; adoption=<use existing dependency / add dependency / borrow architecture / ignore>
```
