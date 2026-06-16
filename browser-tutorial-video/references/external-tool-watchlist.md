# External Tool Watchlist

This skill should stay deterministic and local by default: Playwright for
browser control, a custom overlay for cursor/click UX, and ffmpeg for rendering.
Use external tools only when they reduce real project risk.

## Try First

### pixelmatch

- Repo: https://github.com/mapbox/pixelmatch
- Use for: optional project-local pixel checks against known-good QA frames.
- Why: small, fast, and focused on image diffs.
- Limit: needs stable reference images; do not force it into every recording.

### Stagehand

- Repo: https://github.com/browserbase/stagehand
- Use for: action discovery or self-healing selector exploration on changing
  public/user-owned pages.
- Why: combines code and natural-language browser actions.
- Limit: final recording should still use deterministic Playwright selectors
  once the workflow is known.

## Borrow Patterns

### HyperFrames Video Agent Skills

- Repo: https://github.com/saranambiar/hyperframes-video-agent-skills
- Use for: proof frames, contact sheets, caption/audio sync ideas, and render QA
  discipline.
- Why: useful production patterns for agent-led video work.
- Limit: do not vendor the whole skill pack into this browser walkthrough skill.

### Remotion

- Repo: https://github.com/remotion-dev/remotion
- Use for: later polish layers such as intro/outro, chapter labels, callouts, or
  branded compositions over an already captured browser video.
- Why: strong code-based video composition framework.
- Limit: do not rewrite capture into Remotion; keep it as an optional
  composition layer.

## Watchlist

### rrweb

- Repo: https://github.com/rrweb-io/rrweb
- Use for: possible DOM/event replay logs when browser interactions need to be
  audited or replayed without video.
- Why: mature web record/replay ecosystem.
- Limit: replay is not the same as a polished MP4; it should not replace final
  video capture.

## Avoid For Now

### puppeteer-screen-recorder

- Repo: https://github.com/prasanaworld/puppeteer-screen-recorder
- Reason: confirms the CDP screencast approach, but this skill already needs
  stronger control over cursor overlays, click timing, manual PDF capture, audio
  mixing, and 60 FPS renders.

### ffmpeg.wasm

- Repo: https://github.com/ffmpegwasm/ffmpeg.wasm
- Reason: useful for browser-local products, but heavier and slower than native
  ffmpeg for this local Codex skill.

### fluent-ffmpeg

- Repo: https://github.com/fluent-ffmpeg/node-fluent-ffmpeg
- Reason: archived. Prefer direct `child_process` calls to ffmpeg/ffprobe.
