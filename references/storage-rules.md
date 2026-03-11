# Storage Rules

Pick the smallest durable surface that preserves the reasoning.

## Repo-first cases

Use a repo-local ADR when:

- the decision changes code structure or interfaces
- future contributors will need the rationale
- the repo already has `docs/` or ADR history

Good default locations:

- `docs/architecture-decisions.md`
- `docs/adr/ADR-001-<slug>.md`

## Numbering

- Use sequential `ADR-001`, `ADR-002`, etc.
- If the repo already uses another scheme, follow it.

## Issue-first cases

Use a GitHub issue summary when:

- the work is still scoped and tracked through one canonical issue
- the decision matters before code lands
- the repo does not yet have an ADR surface

## Both

Use both when:

- the issue is the control surface
- the repo is the implementation surface
- future readers would benefit from both traceability and durable local docs
