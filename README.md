# spec-bundle-skill

Codex skill for turning a fuzzy PRD into an implementation-ready bundle with contracts, schema, tests, and task breakdown.

## What it does

- chooses the smallest honest bundle shape
- scaffolds a reusable spec bundle on disk
- keeps scope, contracts, schema, tests, and epics in separate source-of-truth files
- adds an architecture pack only when it materially reduces ambiguity

## Repository layout

- `SKILL.md` - bundle rules and routing
- `references/bundle-shape.md` - when to use each artifact
- `scripts/init_bundle.py` - stdlib-only scaffolder
- `assets/templates/` - core and architecture-pack templates
- `agents/openai.yaml` - agent metadata

## Quick start

```bash
python3 scripts/init_bundle.py \
  --out /absolute/path/to/spec-bundle \
  --project-name "Project Name"
```

With architecture pack:

```bash
python3 scripts/init_bundle.py \
  --out /absolute/path/to/spec-bundle \
  --project-name "Project Name" \
  --with-architecture-pack
```

With ADR scaffolding:

```bash
python3 scripts/init_bundle.py \
  --out /absolute/path/to/spec-bundle \
  --project-name "Project Name" \
  --with-architecture-pack \
  --with-adrs
```

## Generated files

Core bundle:

- `prd.md`
- `contracts.md`
- `schema.sql`
- `test-plan.md`
- `epics.md`

Architecture pack:

- `blueprint.md`
- `gate-matrix.md`
- `adr/0001-decision.md`

## Example prompts

- `assemble an implementation-ready spec`
- `PRD is not enough, build a full bundle`
- `add contracts, schema, and a test plan`
- `turn this into a Codex-ready bundle`

## How it fits the suite

Typical flow:

`work-shaping -> idea-validation -> product-shaping -> spec-bundle`

Use this when the next bottleneck is ambiguity in execution, not lack of market signal.

## License

AGPL-3.0
