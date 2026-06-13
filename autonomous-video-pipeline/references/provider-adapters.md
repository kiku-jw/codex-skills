# Provider Adapters

Use providers as replaceable adapters. Record every provider decision in the
manifest so another run can reproduce or swap the step.

## TTS

Track:

- provider and model
- voice identity or style
- authorization status for cloned or real-person voices
- input chunk ID
- output audio path
- duration
- settings such as stability, speed, language, and seed when available

Prefer narration chunks under one estimated minute. Long TTS generations often
drift in pacing, pronunciation, or voice quality.

## Avatar Or Video Presenter

Track:

- provider and model/engine
- avatar identity and authorization status
- input audio chunk ID
- output video path
- resolution, FPS, duration, and watermark status
- whether the selected model was available through API or required UI control

Prefer official APIs. Use browser automation only with authorized accounts and
only when no stable API path exists. If a provider has watermarks, queues, rate
limits, or plan limits, surface that before final delivery.

## Motion Graphics

Prefer code-rendered scenes when timing matters:

- HTML/CSS/JS with a render harness
- Remotion, Motion Canvas, Three.js, canvas, SVG, or a repo-local renderer
- FFmpeg overlays for simple lower thirds, captions, and cuts

Keep scene timing keyed to narration chunk IDs or transcript timestamps.

## Assembly

FFmpeg is the default assembly layer unless the repo already has a better
pipeline. Preserve intermediate files and render commands in the manifest.

Typical final MP4 expectations:

- H.264 video
- AAC audio
- yuv420p pixel format
- `+faststart`
- requested aspect ratio and resolution
- stable frame rate

## Authorization Boundaries

Do not generate a real person's voice or avatar unless the user has clearly
authorized that use. Do not operate private provider accounts through browser
automation unless the user requested it for this task.
