---
name: autonomous-video-pipeline
description: Use when Codex needs to produce or supervise a complete short-form explainer, avatar, tutorial, or YouTube-ready video package from source material, including scripted narration, optional TTS/avatar generation, code-based motion graphics, FFmpeg assembly, QA frames, timing checks, and a verified final MP4 deliverable.
---

# Autonomous Video Pipeline

## Purpose

Produce a finished short-form video package from source material with explicit
quality gates. Treat this as a production workflow, not a prompt trick: plan the
artifact, build deterministic manifests, create media in replaceable provider
steps, render the final MP4, then verify before claiming completion.

If the requested artifact is only a browser walkthrough or screencast, prefer
`browser-tutorial-video`. Use this skill when narration, generated scenes,
motion graphics, avatar/TTS clips, or multi-stage video assembly are involved.

## Workflow

1. Pin the production contract.
   - Capture topic, audience, target duration, aspect ratio, language, output
     directory, allowed source material, provider constraints, budget ceiling,
     and whether voice/avatar likeness is explicitly authorized.
   - If paid APIs, cloned voices, avatars, private accounts, or live provider
     UIs are required and authorization is unclear, ask before proceeding.
   - For current or factual claims, verify from primary/current sources and
     keep a source ledger in the project manifest.

2. Create a project manifest.
   - Use `scripts/build_video_manifest.py` to create the starting manifest and
     project folders when useful.
   - Track deliverables, sources, narration chunks, media assets, scene files,
     render commands, QA evidence, and residual limitations.
   - Keep the manifest current as work proceeds. It is the control surface for
     review, rerendering, and handoff.

3. Write the script as a production script.
   - Use the user's voice playbook if provided; otherwise write clearly and
     avoid impersonating a real person.
   - Separate narration from visual direction.
   - Keep factual claims traceable to the source ledger.
   - Read `references/production-prompt-pattern.md` when shaping a high-stakes
     goal prompt or stop condition.

4. Chunk narration before media generation.
   - Use `scripts/chunk_script.py` to split narration into provider-friendly
     chunks, defaulting to sub-minute estimated speech duration.
   - Keep chunk IDs stable because downstream audio, avatar clips, subtitles,
     and QA notes should refer to the same IDs.

5. Create a storyboard and scene manifest.
   - Read `references/storyboard-scene-manifest.md`.
   - Map each narration chunk to scenes, visual intent, motion graphic needs,
     asset dependencies, and QA timestamps before generating expensive media.
   - Use a simple JSON or Markdown scene manifest; do not rely on memory or
     chat-only timing notes.

6. Generate or collect media through adapters.
   - Read `references/provider-adapters.md` before using TTS, avatar, stock
     media, browser automation, or code-rendered motion graphics.
   - Prefer APIs and local tools. Use browser automation only when the user is
     authorized and no stable API path exists.
   - Never hardcode one provider as required. Record the chosen provider,
     model/settings, input chunk ID, output path, and failure notes.

7. Build motion graphics and edit.
   - Read `references/motion-graphics-rules.md` before creating scene code.
   - Keep the speaker/avatar visible when the brief asks for an avatar-led
     explainer.
   - Use scene manifests and explicit timings instead of visual guesswork.
   - Assemble with FFmpeg or an existing repo-local render pipeline.

8. Verify before completion.
   - Read `references/video-qa-checklist.md`.
   - Use `ffprobe` metadata, QA frame extraction, representative visual review,
     audio/subtitle timing checks, and scene-boundary checks.
   - Use `scripts/extract_qa_frames.py` for deterministic frame extraction.
   - Use `scripts/probe_video.py` to write a compact `ffprobe` summary.
   - Use `scripts/validate_video_package.py --final` before claiming upload
     readiness.
   - Rerender or patch until the acceptance criteria are met, or report the
     exact limitation that prevents completion.

## Stop Condition

Do not claim that the video is finished until these are true:

- A final MP4 exists at the declared output path.
- The manifest lists all source material, generated chunks, media assets,
  render steps, and verification evidence.
- `ffprobe` metadata matches the requested format closely enough.
- `validate_video_package.py --final` passes for the project manifest, or each
  failure is explicitly waived with a reason.
- Representative QA frames were inspected for timing, layout, clipping, blank
  scenes, out-of-bounds elements, and visible avatar/speaker constraints.
- Any unverified factual claims, provider failures, watermarks, account limits,
  or human-review dependencies are stated plainly.

## Output

Return the final MP4 path, manifest path, QA evidence path, key render metadata,
and any residual limitations. If the work cannot safely complete, return the
best partial package with a concrete next action instead of pretending it is
ready to publish.
