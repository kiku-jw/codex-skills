# GitHub SEO

Codex skill for improving public repository discoverability without confusing
GitHub presentation with website SEO.

## What it does

- classifies a project as repo-only, GitHub Pages product, canonical website, or
  support surface;
- audits only the surface that can create real value;
- separates observed facts from SEO hypotheses;
- requires proof, verification, and a failure check for every recommendation;
- defaults redirects, unproven prototypes, and infrastructure surfaces to
  `skip` or `wait-for-proof`;
- keeps public README, description, and durable documentation in English while
  preserving legitimate localized product content.

## What it does not do

- install crawlers, hooks, paid APIs, MCP servers, or credentials;
- generate keyword-stuffed README files or mass content;
- claim that GitHub topics or descriptions are direct Google ranking signals;
- add schema, sitemaps, `llms.txt`, or social previews without a surface-specific
  reason and read-back.

## Example prompts

- `Audit this repository for GitHub discoverability.`
- `Improve the SEO of this GitHub Pages project.`
- `Which repositories deserve website SEO and which only need README work?`
- `Make these public docs more agent-friendly without inventing claims.`

## Provenance

This is a narrow Codex and KikuAI adaptation inspired by the evidence,
dependency, and falsifiability approach in
[`AgriciDaniel/claude-seo`](https://github.com/AgriciDaniel/claude-seo) at
commit `09d37c7b66ed3ca9c6efbdb765a805a6c76a8f01`.

The adaptation intentionally does not vendor the upstream runtime, subagents,
hooks, extensions, or credentials. It also does not copy from
`AgriciDaniel/codex-seo`; that repository's checked-in license did not permit
redistribution or derivative work at the time of evaluation.

## License

MIT. See [`LICENSE`](LICENSE).
