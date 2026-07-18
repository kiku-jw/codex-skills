# Contributing

Keep changes scoped to one skill or one repository-wide policy.

## Repository boundary

- Add a directory here only when the primary artifact is a reusable Codex or
  compatible agent workflow.
- Keep standalone products, libraries, services, operational runbooks, and
  experiments in independent repositories.
- Keep JW-specific workflows private and outside this repository.
- Preserve a directory's existing license and provenance.

## Skill shape

Every top-level skill entry point must contain:

- `SKILL.md` with valid YAML frontmatter;
- `agents/openai.yaml` when the skill is exposed through agent UI surfaces;
- only the references, scripts, assets, runtime code, and tests it actually
  needs.

Family child skills may call a documented parent skill for shared runtime code.
Do not duplicate a renderer, parser, or large reference tree merely to make a
child folder look self-contained.

## Checks

Run the validation commands from the root README. If a changed skill owns tests,
run those tests from its directory or with the documented `PYTHONPATH`.

Pull requests should explain the user-visible workflow change, verification,
and any license or migration impact.
