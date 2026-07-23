---
name: github-seo
description: Audit and improve a public GitHub repository's discoverability and any linked canonical site without confusing repository presentation with website SEO. Use for repository SEO, GitHub discoverability, topics/homepage/README optimization, GitHub Pages SEO, AEO, or agent-friendly public documentation.
license: MIT
metadata:
  author: KikuAI Lab
  version: "1.0.0"
  upstream: "AgriciDaniel/claude-seo@09d37c7b66ed3ca9c6efbdb765a805a6c76a8f01"
---

# GitHub SEO

## Metadata

- Trigger when: the user wants better discoverability for a public repository,
  its GitHub Pages deployment, or its canonical product site.
- Do not use when: the repository is private, the task is ordinary product
  development, or the user only wants generic marketing copy.

## Skill Purpose

Choose the correct discoverability surface before changing anything, then make
the smallest evidence-backed improvement that helps people or search systems
understand a real maintained project.

## Instructions

1. Ground the audit in live state. Read the repository metadata, README,
   manifests, releases, current screenshots, and linked homepage. Classify the
   target with `references/surface-model.md` before recommending changes.
2. Audit only the applicable surface. Use `references/audit-gates.md` for
   GitHub metadata and README checks, Pages or canonical-site checks, language,
   evidence, and anti-spam rules. Separate observed facts from hypotheses and
   give every recommendation a verification or failure check.
3. If implementation is authorized, apply only the highest-value reversible
   slice, preserve URLs/Pages/releases/CI, and read back the changed metadata,
   rendered README, deployed page, and relevant checks. Otherwise return the
   ranked plan without mutating anything.

## Non-Negotiable Acceptance Criteria

- The output names exactly one surface:
  `repo-only`, `pages-product`, `canonical-site`, or `support-surface`.
- GitHub metadata and README quality are not represented as confirmed Google
  ranking factors.
- Claims, metrics, screenshots, examples, schema, and product status are
  supported by current repository or live-product evidence.
- English is canonical for public descriptions, README prose, and durable
  technical documentation. Localized product content, fixtures, quotations,
  and user-facing examples may remain in their real language.
- No keyword stuffing, fake comparisons, bulk AI content, doorway pages,
  invented social proof, speculative schema, or decorative asset churn.
- No new credentials, paid APIs, MCP servers, hooks, background services, or
  dependencies are installed without a separate explicit decision.
- Redirects, organization metadata repositories, compatibility layers,
  unproven prototypes, and parked surfaces default to `skip` or
  `wait-for-proof`.

## Output

Return:

- `Surface`: one surface classification with evidence.
- `Verdict`: `keep`, `metadata-only`, `asset-only`, `readme-rewrite`,
  `site-baseline`, `wait-for-proof`, or `skip`.
- `Findings`: observed facts separated from hypotheses.
- `Action`: the smallest useful change, its dependency, and why it is first.
- `Verification`: exact read-back, test, crawl, or deployment check.
- `Failure check`: what would show that the recommendation did not help.

Optional handoffs after the audit:

- `$readme-generator` — build a truthful README when structure is the problem.
- `$beautify-github-readme` — redesign only when repo-native visual proof exists.
- `$ai-writing-detox` — remove generic AI copy after the facts are settled.
