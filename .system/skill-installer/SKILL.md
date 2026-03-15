---
name: skill-installer
description: Install Codex skills into `$CODEX_HOME/skills` from the curated OpenAI list or from an explicit GitHub repo/path. Use when the user wants to list installable skills, install one or more curated skills, or install a skill from another repo.
---

# Skill Installer

## Metadata
- Trigger when: the user asks what skills are available or asks to install a skill from OpenAI or GitHub.
- Do not use when: the skill already exists locally and the real task is to edit or debug it.

## Skill Purpose

Install skills reproducibly through the bundled helper scripts instead of ad hoc copying. The harness should make it obvious whether we are listing options, installing from the curated catalog, or installing from a specific GitHub path.

## Instructions
1. Choose the mode first: list curated skills, install a curated skill, or install from a GitHub repo/path. Use `/Users/nick/.codex/skills/.system/skill-installer/scripts/list-skills.py` for listings and `/Users/nick/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py` for installs.
2. Run the helper with explicit inputs only. For curated installs, use the requested skill name. For GitHub installs, require an explicit repo/path or URL. If the runtime requires approval for network access, request it instead of pretending the install already happened.
3. Validate the destination. Confirm the skill now exists under `$CODEX_HOME/skills/<skill-name>`, that `SKILL.md` is present, and that we did not silently overwrite an existing directory. Then tell the user they should restart Codex to pick up newly installed skills.

## Non-Negotiable Acceptance Criteria
- Never invent a skill name, repo path, or availability signal that the helper did not return.
- Do not overwrite an existing skill directory unless the user explicitly asked for that outcome.
- Use the bundled installer scripts instead of hand-copying files.
- If installation fails, report the exact failure mode and stop instead of implying success.

## Output
- For listings: a concise numbered list of candidate skills, clearly labeled by source.
- For installs: the installed skill path(s) and whether each install succeeded or failed.
- A final restart note: `Restart Codex to pick up new skills.`
