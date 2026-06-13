# Motion Graphics Rules

Use motion graphics to explain the narration, not to decorate the video.

## Scene Design

- Create a scene list before rendering.
- Tie each scene to narration chunk IDs or transcript timestamps.
- Use `references/storyboard-scene-manifest.md` for required scene fields when
  the project does not already have a scene format.
- Use stable dimensions and safe margins for all overlays.
- Keep text short enough to read at target resolution.
- Prefer diagrams, counters, timelines, callouts, and before/after comparisons
  over generic abstract animation.
- Keep the avatar or speaker visible when requested, using side cards, lower
  thirds, crop windows, or picture-in-picture instead of full-screen takeover.

## Timing

- Define animation start/end times explicitly.
- Align graphic entrances to the words they explain.
- Avoid late overlays that appear after the concept has passed.
- Leave enough hold time for viewers to understand the graphic.

## Visual QA Failure Modes

Check for:

- blank or black scenes
- clipped text or off-canvas graphics
- hidden speaker/avatar
- overlays covering faces or important UI
- unreadable text
- unintentional layout shifts
- mismatched aspect ratio
- animation that starts too early or too late
- stale placeholder content

## Rendering

Keep scene source files, render scripts, and output paths traceable. If a scene
is generated from code, save representative frames for QA before final assembly.
