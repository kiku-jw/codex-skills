# Section Matrix

Use this matrix to choose sections by repo type. Do not include everything by default.

## Core Sections

These are usually worth keeping for any public repo:

- `# Project Name`
- one-line value proposition
- short description
- `Quick Start`
- `Usage`
- `License`

## CLI Tool

Prefer:

- `Installation`
- `Quick Start`
- `Usage`
- `Common Commands` or `Options`
- `Examples`

Optional:

- `Requirements`
- `Configuration`
- `Known Limitations`

Avoid:

- large architecture sections unless the CLI is a platform

## Library / SDK

Prefer:

- `Installation`
- `Quick Start`
- `Usage`
- `API Overview`
- `Examples`

Optional:

- `Supported Environments`
- `Error Handling`
- `Integration Notes`

Avoid:

- full method-by-method API dumps in README

## Web App

Prefer:

- `Features`
- `Quick Start`
- `Requirements`
- `Tech Stack`

Optional:

- `Architecture`
- `Environment Variables`
- `Deployment`

## Full-Stack App

Prefer:

- `Features`
- `Quick Start`
- `Requirements`
- `Tech Stack`
- `Architecture`

Optional:

- `Project Structure`
- `Deployment`
- `Environment Variables`
- `Testing`

## Skill / Workflow Repo

Prefer:

- `What it does`
- `When to use it`
- `Repository layout` or `What's inside`
- `Example prompts` or `Quick Start`

Optional:

- `How it fits the suite`
- `Related Skills`

## Template / Starter Repo

Prefer:

- `What this template gives you`
- `Quick Start`
- `Included pieces`
- `Customization points`

Optional:

- `Opinionated defaults`
- `When not to use this template`

## Taxonomy Hint

If a repo spans multiple categories, make the split explicit near the top:

- tool
- skill
- library
- app
- docs site
- MCP integration

That small taxonomy cue reduces confusion fast.
