# Tutorial Job Spec

Use a job spec when a browser tutorial should be repeatable, localized, or
reviewable without reconstructing steps from chat.

Start from `templates/tutorial-job.json`:

```bash
node /path/to/browser-tutorial-video/scripts/scaffold_tutorial_job.js \
  --out tutorial-job.json \
  --url https://example.com \
  --title "Example walkthrough"
```

For simple public or local pages, run the job:

```bash
node /path/to/browser-tutorial-video/scripts/run_tutorial_job.js \
  --job tutorial-job.json
```

The runner is intentionally narrow. It supports deterministic `goto`, `wait`,
`click`, and `scroll` actions with custom cursor/highlight overlay, frame
capture, MP4 render, click timeline, and QA contact sheet generation.

For complex sites, PDFs, downloads, multi-page localization, or login/session
workflows, treat the job spec as the contract and build a repo-local recorder
around it.

## Core Fields

- `title`: human-readable name for logs and output.
- `startUrl`: HTTP(S), `file://`, or a relative local HTML path.
- `outputDir`: output directory relative to the job file unless absolute.
- `viewport`: `{ "width": 1280, "height": 720 }` or larger.
- `fps`: capture/render FPS. Use low values for smoke tests and `60` for final
  high-quality renders when the runner can keep up.
- `zoom`: CSS zoom applied to page content while excluding the overlay.
- `browserChannel`: optional Playwright browser channel such as `"chrome"` when
  a local system browser should be used instead of Playwright's bundled browser.
- `actions`: ordered browser actions.
- `qa`: optional QA extraction settings.

## Actions

```json
{ "type": "wait", "ms": 500 }
```

```json
{ "type": "click", "selector": "#export", "label": "Export MP4" }
```

```json
{ "type": "click", "text": "Export MP4", "exact": true }
```

```json
{ "type": "scroll", "y": 720, "durationMs": 900 }
```

```json
{ "type": "goto", "url": "./next-page.html" }
```

Prefer selectors for repeatability. Use text only when selector ownership is
not available.

## Output

The generic runner writes:

- `frames/frame-*.jpg`
- `final.mp4`
- `clicks.json`
- `qa/contact-sheet.jpg`
- `qa/qa-summary.json`
- `run-summary.json`

## Acceptance

A job is not complete until:

- `final.mp4` exists;
- `clicks.json` contains expected click count;
- `qa/contact-sheet.jpg` exists;
- `qa/qa-summary.json` exists;
- representative frames were inspected manually.
