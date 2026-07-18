# codex-execution-pack

Codex skill and scaffold for turning a PRD or raw product brief into a durable execution pack.

The point is simple:

- a spec explains what should be built
- an execution pack explains how Codex should carry the work without constant babysitting

This repo packages that operating layer:

- a reusable `codex-execution-pack` skill
- UI metadata for skill surfaces
- a scaffold script
- templates for plan, status, tests, backlog, and reusable execution prompts
- an optional `spec/` companion when contracts, schema, or architecture gates matter

## What is inside

- `SKILL.md` - the skill itself
- `agents/openai.yaml` - skill metadata for UI surfaces
- `scripts/init_execution_pack.py` - scaffold a new execution pack folder
- `references/pack-shape.md` - what each file is for and when to include it
- `assets/templates/` - starter files for:
  - `AGENTS.md`
  - `docs/PLAN.md`
  - `docs/STATUS.md`
  - `docs/TEST_PLAN.md`
  - `docs/BACKLOG.md`
  - `prompts/execute.md`
  - `prompts/resume.md`
  - `prompts/review-repair.md`
  - `prompts/blocker-compress.md`
  - optional `spec/` companion files

## Quick start

```bash
python3 scripts/init_execution_pack.py --out ./packs/live2reels --project-name "Live2Reels"
```

That creates:

- `AGENTS.md`
- `docs/PLAN.md`
- `docs/STATUS.md`
- `docs/TEST_PLAN.md`
- `docs/BACKLOG.md`

If you also want reusable prompts and a spec companion:

```bash
python3 scripts/init_execution_pack.py \
  --out ./packs/live2reels \
  --project-name "Live2Reels" \
  --with-prompts \
  --with-spec-companion \
  --with-architecture-pack \
  --with-adrs
```

## When this is useful

Use a full execution pack when:

- the work will span sessions
- Codex needs resumable repo state instead of chat memory
- milestones need explicit validation commands
- another agent or reviewer will touch the work
- the task needs a blocker protocol or release hardening pass

Skip the full pack when a short execution brief is enough.

## Why this exists

Many PRDs are good enough for discussion but still weak as operating systems.

The missing pieces are usually boring and operational:

- milestone order
- done criteria
- live status memory
- test gates
- continuation rules
- blocker compression

That is what this kit is trying to make easier.
