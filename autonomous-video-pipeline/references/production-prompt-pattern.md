# Production Prompt Pattern

Use this reference when turning a loose "make a video" request into an
execution-ready production contract.

## Required Fields

- Goal: the exact video artifact to produce.
- Duration: target range and hard max.
- Audience: who the video must work for.
- Packaging: title, framing, style, and final use.
- Source material: what claims, files, URLs, or transcripts may be used.
- Voice: narrator style, language, and any voice-playbook constraints.
- Visual grammar: avatar visibility, scene types, overlays, captions, and motion
  graphics expectations.
- Storyboard: whether Codex should create a scene manifest before paid media
  generation.
- Providers: allowed TTS, avatar, image/video, browser, render, and editing
  tools.
- Budget ceiling: API spend, time ceiling, and whether paid provider calls are
  allowed.
- Verification: required checks before completion.
- Stop condition: what must be true before the agent may say the video is done.

## High-Stakes Stop Condition

For reputation-sensitive or public-channel work, include a concrete stop rule:

```text
Only stop when the final deliverable is ready for upload or when a specific
external blocker prevents completion. Verify the full video visually and
technically. Motion graphics must appear on time, nothing may be out of bounds,
no scene may be blank, narration must match the script, and the final package
must include evidence sufficient for fast human review.
```

Avoid claims like "the user does not need to review." Instead, produce evidence
that makes review fast: manifest, render metadata, QA frames, timing notes, and
known limitations.

## Anti-Patterns

- Hardcoding one model, provider, or UI as mandatory.
- Treating a transcript or rough prompt as fact-checked source material.
- Creating drafts without a render and QA loop.
- Letting generated motion graphics hide the speaker when the brief asks for an
  avatar-led video.
- Using cloned voices, avatars, private accounts, or paid APIs without explicit
  authorization.
