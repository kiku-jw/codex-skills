# Codex Skills

Canonical source repository for reusable Codex/OpenAI workflow skills
maintained by KikuAI Lab.

Each top-level directory is one installable skill entry point with its own
`SKILL.md`, agent metadata, and any references, scripts, assets, runtime code,
or tests it needs. Related skills may call one another, but products and
libraries with an independent audience or release lifecycle stay in their own
repositories.

## Skill catalog

### Planning, product, execution, and review

- `work-shaping`
- `idea-validation`
- `product-shaping`
- `spec-bundle`
- `codex-execution-pack`
- `continuity-ledger`
- `issue-control-loop`
- `adversarial-review`
- `adr-log`
- `github-mobile-ops`
- `justdoit`
- `lazy-senior`
- `long-context-dispatch`
- `parallel-worktrees`
- `product-council`
- `triage-finding`
- `tool-scout`

### Documentation, communication, and public artifacts

- `ai-writing-detox`
- `illustration-prompt`
- `public-artifact-lane`
- `readme-generator`
- `session-to-post`
- `visual-explainer`

### Browser, media, and external workflows

- `autonomous-video-pipeline`
- `browser-tutorial-video`
- `openclaw-council`
- `playwright`
- `screenshot`
- `video-builder`
- `video-spec-builder`
- `video-render-run`
- `transcribe`
- `transcribe-basic`
- `transcribe-diarize`

### Spreadsheet workflows

- `spreadsheet`
- `spreadsheet-xlsx-edit`
- `spreadsheet-tabular-analysis`

### System skills

- `.system/skill-creator`
- `.system/skill-installer`

## Using a skill

Copy or install the required directory as a complete unit. Do not copy only
`SKILL.md` when the directory also contains `agents/`, `references/`,
`scripts/`, `assets/`, runtime code, or tests.

The video, spreadsheet, and transcription child skills use their corresponding
parent directory for shared scripts or references. Install the whole family
when using a child entry point.

The public descriptions and use-case catalog live in
[Awesome AI Skills by Kiku](https://github.com/kiku-jw/awesome-ai-skills-by-kiku).

JW-specific workflows are intentionally excluded from this public repository
and maintained in a separate private repository.

## Repository policy

A workflow belongs here when its primary lifecycle is that of a reusable skill
for Codex or a compatible agent surface. A standalone product, reusable library,
service, operational source of truth, or experiment stays independent even if
it also exposes a skill-shaped entry point.

Imported repositories retain their source commits through non-squashed history
merges. Their former repositories remain as read-only migration redirects after
the canonical copies are verified.

## Validation

Validate all skill metadata and run the imported runtime tests:

```bash
python3 -m pip install pyyaml pytest

find . -mindepth 2 -maxdepth 2 -name SKILL.md -print \
  | sed 's#/SKILL.md##' \
  | while read -r skill; do
      python3 .system/skill-creator/scripts/quick_validate.py "$skill"
    done
python3 .system/skill-creator/scripts/quick_validate.py .system/skill-creator
python3 .system/skill-creator/scripts/quick_validate.py .system/skill-installer

PYTHONPATH=session-to-post/src python3 -m pytest -q session-to-post/tests
PYTHONPATH=issue-control-loop/src python3 -m pytest -q issue-control-loop/tests
python3 -m pytest -q codex-execution-pack/tests
```

GitHub Actions runs the same checks on pushes and pull requests.

## Contributing and security

See [CONTRIBUTING.md](CONTRIBUTING.md) for repository boundaries and test
expectations. Report vulnerabilities through GitHub's private vulnerability
reporting flow when available; see [SECURITY.md](SECURITY.md).

## Licenses

This repository is not uniformly licensed. Original KikuAI Lab material is MIT
unless a directory says otherwise. Imported AGPL-3.0 and Apache-2.0 skills keep
their own license text. See [LICENSES.md](LICENSES.md) before redistributing a
skill.
