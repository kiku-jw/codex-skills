# Audit Gates

Use primary sources and live read-back. Do not convert checklists into
unsupported ranking claims.

## GitHub repository surface

Verify:

- the name and one-sentence description identify the real artifact and audience;
- topics describe purpose, ecosystem, and interface without repetition or
  keyword stuffing;
- the homepage points to the canonical maintained surface;
- the README first screen explains value, status, primary CTA, and a proof path;
- quick start and examples match the current interface and default branch;
- limitations, security boundaries, license, support, and release/install paths
  are truthful where relevant;
- screenshots or diagrams are repository-owned, current, accessible, and useful;
- links resolve and do not point to former owners, stale products, or dead docs;
- a social preview is used only when the project has stable, representative
  visual proof.

GitHub documents README as the first explanation of what a project does, why it
is useful, how to start, and where to get help. GitHub documents topics as a
repository discovery mechanism. Neither documentation source says these fields
are direct Google ranking signals.

Primary sources:

- <https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes>
- <https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/classifying-your-repository-with-topics>
- <https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/customizing-your-repositorys-social-media-preview>

## Pages or canonical website surface

Verify:

- important URLs are public, return a successful status, and render useful
  content without requiring unsupported client behavior;
- redirects converge on the intended canonical URL;
- each important page has a descriptive title and useful snippet source;
- canonical markup matches the preferred public URL;
- robots rules do not accidentally block required crawling;
- a sitemap exists only when it materially helps discovery of multiple canonical
  URLs; its presence never counts as indexing proof;
- structured data describes visible content and uses a currently supported type;
- important images have useful alternative text and reasonable delivery size;
- navigation and internal links expose important pages;
- mobile rendering and current Core Web Vitals are checked when the site is a
  real acquisition surface;
- Search Console or analytics claims are made only from authenticated current
  data supplied for that site.

Primary sources:

- <https://developers.google.com/search/docs/essentials>
- <https://developers.google.com/search/docs/essentials/technical>
- <https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls>
- <https://developers.google.com/search/docs/crawling-indexing/sitemaps/overview>
- <https://developers.google.com/search/docs/crawling-indexing/robots/intro>
- <https://developers.google.com/search/docs/appearance/structured-data/sd-policies>
- <https://web.dev/articles/vitals>

## Agent-friendly and answer-friendly documentation

Prefer:

- a direct one-sentence definition near the top;
- explicit inputs, outputs, constraints, and supported environments;
- runnable examples with expected results;
- stable headings and descriptive link text;
- dated benchmarks and reports with methodology;
- citations to primary sources for external claims;
- clear separation between current behavior, roadmap, and non-goals.

Do not:

- add `llms.txt` as a presumed ranking or citation lever;
- repeat the same keywords in headings, topics, badges, and alt text;
- manufacture FAQ sections without real user questions;
- add schema that is not represented in visible page content;
- publish mass comparison, location, or integration pages without unique value;
- turn a demo, redirect, source mirror, or package tap into a fake product site.

## Evidence and language gate

For every proposed claim, record its source:

- code or manifest;
- test or benchmark with date and method;
- current release or deployment;
- current screenshot or recorded interaction;
- official external documentation;
- authenticated analytics supplied for the target.

If the source is missing, write `proof missing` and use `wait-for-proof`.

Write public repository descriptions, README prose, and durable technical
documentation in English. Preserve localized UI copy, content data, fixtures,
quotations, and realistic examples when translation would change the artifact
being documented.

## Recommendation contract

Each recommendation must include:

- observed fact;
- user or search-system impact;
- dependency or reason it comes first;
- smallest reversible action;
- exact verification;
- failure check or leading indicator.

Do not invent a universal numeric SEO score. Missing measurements remain
unknown rather than zero.
