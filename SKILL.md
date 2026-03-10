---
name: spec-bundle
description: "Use when a plain PRD is no longer enough and the user needs an implementation-ready spec bundle: minimum useful contracts, schema, test plan, blueprint, gates, ADRs, boundaries, and GitHub-ready task breakdown."
---

# Spec Bundle

Use this skill when a plain PRD is no longer enough.

Typical prompts:

- `собери пакет для агента`
- `сделай implementation-ready spec`
- `PRD мало, нужен полный bundle`
- `добавь contracts / schema / test plan`
- `разложи это в bundle, который можно отдавать Codex`

## What to do

1. Decide first if a full bundle is honest.
   - For small or reversible work, a short brief is enough.
   - Use a bundle only when extra artifacts will reduce ambiguity, rework, or review pain.
2. Choose the smallest bundle shape that fits:
   - Core bundle: `prd.md`, `contracts.md`, `schema.sql`, `test-plan.md`, `epics.md`
   - Architecture pack when architecture risk is real: `blueprint.md`, `gate-matrix.md`
   - Optional `adr/` only for irreversible or high-cost decisions
3. If the bundle is warranted, scaffold it:

```bash
python3 scripts/init_bundle.py --out /absolute/path/to/spec-bundle --project-name "Project Name"
python3 scripts/init_bundle.py --out /absolute/path/to/spec-bundle --project-name "Project Name" --with-architecture-pack
python3 scripts/init_bundle.py --out /absolute/path/to/spec-bundle --project-name "Project Name" --with-architecture-pack --with-adrs
```

4. Fill only the artifacts that change implementation quality:
   - `prd.md`
   - `contracts.md`
   - `schema.sql`
   - `test-plan.md`
   - `epics.md`
   - `blueprint.md` when system shape, invariants, or local/cloud boundaries matter
   - `gate-matrix.md` when risky work needs explicit entry or exit gates
   - `adr/` when the why behind a decision will otherwise get lost
5. Make traceability explicit:
   - ADRs must point to affected blueprint, contracts, schema, or epics
   - contracts must name the consuming epic or task
   - tasks must declare inputs, outputs, dependencies, and evidence
   - gates must name the blocking condition and the evidence needed to close it
6. When architecture changes, update the affected bundle artifacts in the same pass. Do not let the bundle fork into contradictory truths.
7. Make the bundle ready for action, not for admiration.

## When to read the reference

If you need the exact bundle shape, when to include each artifact, or what good output looks like, read:

- `references/bundle-shape.md`

## Rules

- Do not turn this into paperwork religion.
- A bundle exists to remove ambiguity, not to sound senior.
- Keep one source of truth per thing: scope in `prd.md`, contracts in `contracts.md`, DB shape in `schema.sql`, validation in `test-plan.md`, breakdown in `epics.md`.
- Use `blueprint.md` for the live system map and `adr/` for the reasoning behind irreversible choices.
- Use `gate-matrix.md` only for gates that actually block or materially de-risk implementation.
- Always make the local/cloud boundary explicit when it matters.
- Keep architecture pack artifacts lean. If a decision is obvious and reversible, skip the ADR.
- If an artifact would be fake theater, leave it out or mark it as intentionally deferred.
