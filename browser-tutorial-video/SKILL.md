---
name: browser-tutorial-video
description: Use when recording a browser walkthrough, app tutorial, screencast, PDF scroll, highlighted clicks, localized demo video, or polished browser automation MP4 with Playwright and ffmpeg.
---

# Browser Tutorial Video

## Metadata
- Trigger when: the requested artifact is a real browser tutorial video, not just instructions or a script.
- Do not use when: the task is only browser inspection, a generic narrated video, or a Playwright test suite.

## Skill Purpose

Produce polished browser tutorial MP4 artifacts from a described workflow by
combining Playwright browser control, custom cursor/highlight overlays, click
audio, ffmpeg rendering, and visual verification.

For implementation details and snippets, read
[references/playwright-ffmpeg-pattern.md](references/playwright-ffmpeg-pattern.md)
when building or modifying a recorder.

For final-render QA, read [references/qa-pattern.md](references/qa-pattern.md)
and use `scripts/tutorial_video_qa.js` when the video has a click timeline or
long-scroll/PDF checkpoints.

For optional external helpers, read
[references/external-tool-watchlist.md](references/external-tool-watchlist.md)
only when deciding whether to add Remotion, Stagehand, pixelmatch, rrweb, or a
recording wrapper to a specific project.

## Workflow

1. Pin the requested flow.
   - Capture the URL, exact navigation steps, language variants, allowed
     overlays, click sound, zoom, resolution, FPS, and output file names.
   - Confirm the workflow is public, user-owned, demo-account based, or
     otherwise explicitly authorized.
   - If the user provides enough detail, act directly. Ask only when missing
     information changes the artifact.

2. Inspect the live target with the same browser style used for recording.
   - Use Playwright with persistent Chrome when the site is sensitive to
     automation, plus the final viewport, locale, and user agent.
   - For changing websites, discover current selectors and localized text from
     the DOM before editing the recorder.
   - Prefer functional selectors, roles, and hrefs over fragile visible text.
   - For localized pages, put labels and URLs in a config map.

3. Build or adapt a repo-local recorder.
   - Use a high-resolution viewport such as `2560x1440` and render at `60 fps`
     when the user asks for quality.
   - Hide or pre-accept cookie banners before recording unless requested.
   - Apply page zoom intentionally while excluding the overlay.
   - Inject an overlay with a large custom cursor, target highlight, and click
     ripple. Hide the native cursor.
   - Keep a global cursor position and reinstall the overlay after navigation
     using that position so the cursor does not teleport.
   - For each click target: show the highlight first, pause briefly, animate the
     cursor to the highlighted target, click, then show the ripple.
   - Log click timestamps and coordinates for later audio mixing.

4. Capture and render.
   - Use Chrome DevTools screencast frames at high JPEG quality for normal
     browser motion.
   - If browser-native PDF scrolling records at low FPS, stop screencast and
     capture manual screenshots at the target FPS while scrolling.
   - For PDFs, download the file and open it in a local HTML viewer with browser
     PDF parameters such as `#toolbar=1&navpanes=0&zoom=150`.
   - Decode the click MP3 with ffmpeg to mono 48 kHz float samples, mix it at
     logged click times, write a WAV click track, and encode final audio as AAC.
   - Render the final MP4 with H.264, `yuv420p`, BT.709 color metadata,
     `+faststart`, and a low CRF such as `10`.

5. Verify before claiming completion.
   - Run syntax checks on the recorder.
   - Inspect the MP4 with `ffprobe`: width, height, video FPS, audio codec,
     sample rate, duration, and size.
   - If a click timeline exists, run `scripts/tutorial_video_qa.js` to extract
     pre-click, post-click, interval, and long-scroll checkpoint frames plus a
     contact sheet.
   - Check the click timeline JSON includes the expected click sound and click
     count.
   - Extract control frames around each click: one before the click to confirm
     the highlight appears before the cursor arrives, one at or after click for
     the ripple, and one near any PDF or long-scroll ending.
   - View representative frames before the final response.

## Quality Rules

- Do not add instructional text overlays when the user asked for a clean
  recording; keep only cursor, highlight, and click effects.
- Prefer recording at the final high resolution over upscaling a low-resolution
  capture.
- Preserve smoothness by capturing enough source frames; do not rely on nominal
  output FPS alone.
- When a site blocks default headless automation, switch to persistent Chrome
  with a realistic user agent and the same setup used for final capture.
- Avoid waiting on localized modal titles when a stable functional element
  exists.
- Keep outputs separate by locale or variant so rerenders do not overwrite
  completed videos.
- Keep Remotion, Stagehand, rrweb, and other helpers optional. The final
  recording path should stay deterministic Playwright plus ffmpeg unless a
  project-specific need justifies extra moving parts.

## Output

- MP4 video artifact paths.
- Verification summary: syntax check, `ffprobe` metadata, click count, and QA
  frame checks.
- Contact sheet and QA summary paths when `scripts/tutorial_video_qa.js` was
  used.
- Any residual limitation, such as target-site layout drift, PDF viewer
  behavior, or authorization boundaries.
