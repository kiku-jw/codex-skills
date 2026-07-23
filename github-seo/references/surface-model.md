# Surface Model

Classify the real public surface before auditing it. Repository visibility and
website search optimization overlap, but they are not the same job.

| Surface | Evidence | Audit scope | Typical verdict |
| --- | --- | --- | --- |
| `repo-only` | Library, CLI, SDK, skill, research project, or source package without a maintained user-facing site | Repository name, description, topics, homepage link, README first screen, examples, docs, release/install path, social preview | `keep`, `metadata-only`, `asset-only`, `readme-rewrite` |
| `pages-product` | GitHub Pages hosts the actual app, game, documentation, or interactive demo | Repository presentation plus deployed HTML, status, canonical, title/description, crawlability, sitemap when warranted, structured data only when supported, mobile rendering | `site-baseline`, `asset-only`, `wait-for-proof` |
| `canonical-site` | A maintained product or organization website is the primary acquisition and conversion surface | Canonical site first; repository as trust, source, install, release, or documentation layer | `site-baseline`, `metadata-only`, `wait-for-proof` |
| `support-surface` | Redirect, organization metadata repo, package tap, compatibility layer, duplicate prototype, internal infrastructure, or parked experiment | Truth and link integrity only | `keep`, `wait-for-proof`, `skip` |

## Classification order

1. Follow the configured homepage and determine whether it is live, canonical,
   maintained, and user-facing.
2. Check whether GitHub Pages is the product itself, documentation, a demo, or
   only a redirect.
3. Read releases, workflows, screenshots, and current product status before
   treating a repository as maintained.
4. If evidence conflicts, choose the narrower surface and return
   `wait-for-proof`.

## Priority order

1. Indexing or availability blockers on a real maintained site.
2. Canonical and redirect errors that split or lose the real surface.
3. A false, stale, or missing explanation of what the project does.
4. A missing proof path: runnable example, result state, release, or live CTA.
5. Metadata, topics, social preview, and visual improvements.

The priority list is a dependency order, not a score. A polished preview does
not compensate for a broken canonical, missing product proof, or misleading
README.
