# Video QA Checklist

Use this checklist before claiming the final video is ready.

## Technical Checks

- `ffprobe` final MP4 metadata: duration, width, height, FPS, codecs, audio
  sample rate, channel count, bitrate, and file size.
- Write the metadata with `scripts/probe_video.py` and record the output path
  in `manifest.qa.ffprobe`.
- Run `scripts/validate_video_package.py --final <manifest>` after QA evidence
  is written.
- Final duration is within requested tolerance.
- Audio exists for the full timeline and does not end early.
- Video has no blank opening, blank ending, or accidental long silence.
- Aspect ratio and resolution match the brief.
- Final file is playable locally.

## Visual Checks

Extract frames at:

- opening title or first spoken beat
- every scene boundary
- every major motion graphic entrance
- around each avatar/video clip transition
- around captions or dense text overlays
- near the end card or final beat

Inspect for clipping, blank frames, out-of-bounds elements, text readability,
speaker/avatar visibility, and timing plausibility.

## Content Checks

- Narration matches the approved script or the generated script in the manifest.
- Factual claims have sources or are marked as unverified.
- No private prompts, account details, secrets, or irrelevant local paths appear
  in the video.
- Generated voice/avatar use is authorized and recorded.
- Watermarks or provider artifacts are either absent or explicitly disclosed.

## Evidence Package

The final response should name:

- final MP4 path
- manifest path
- QA frame directory
- ffprobe metadata summary
- package validation status
- any unresolved limitations
