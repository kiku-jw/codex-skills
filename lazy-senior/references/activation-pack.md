# Lazy Senior Activation Pack

Use this when the skill is installed but not yet shaping daily work.

## AGENTS Snippet

Add one lightweight routing line to the relevant `AGENTS.md`:

```markdown
- Use `lazy-senior` before adding new dependencies, parsers, widgets, wrappers, CLIs, state machines, caches, schedulers, or more than roughly 30-50 LOC of reusable code; include its compact receipt when files change.
```

Avoid broad blocking hooks until a repeated failure justifies them.

## Operating Loop

1. For suspicious new surface area, ask Codex to use `$lazy-senior`.
2. For an existing repo, run `scripts/lazy-audit.sh --cwd .`.
3. For an active change, run `scripts/lazy-review-diff.sh --cwd .`.
4. If you accept temporary complexity, record it with `scripts/lazy-debt.sh add`.
5. Use `scripts/lazy-status.sh --cwd .` to check whether the skill is active or silent.

## Success Evidence

- A final response includes a compact lazy-senior receipt.
- A diff review prevents or deletes at least one dependency, abstraction, or custom helper.
- Debt entries are deliberate and revisit-ready, not forgotten TODOs.
