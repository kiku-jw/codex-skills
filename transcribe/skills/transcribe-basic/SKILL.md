---
name: transcribe-basic
description: Produce a fast plain-text transcript with the bundled CLI using the light transcription model. Use when speaker diarization is not needed.
---

# Transcribe Basic

## Metadata
- Trigger when: the user needs a fast transcript without speaker labels.
- Do not use when: the user explicitly needs diarization or known-speaker matching.

## Skill Purpose

Generate the fastest honest transcript path for audio by keeping the job to plain transcription instead of overcomplicating it with diarization.

## Instructions
1. Confirm the audio path and check that `OPENAI_API_KEY` is set. If the key is missing, stop and tell the user to set it locally.
2. Run `~/.codex/skills/transcribe/scripts/transcribe_diarize.py` with `gpt-4o-mini-transcribe` and plain text output under a stable output path such as `output/transcribe/`.
3. Validate that the transcript exists, is readable, and matches the requested file/output format. Note any caveat caused by audio quality, chunking, or language uncertainty.

## Non-Negotiable Acceptance Criteria
- Secrets stay in environment variables, never in chat.
- The model choice is the fast plain-transcription path, not diarization-heavy overkill.
- Output location and format are explicit.
- Audio-quality limitations are stated when they materially affect trust in the transcript.

## Output
- The transcript path.
- The model and response format used.
- A short note on transcript quality or caveats.
- `Next skill options` (only if needed): `$transcribe-diarize` — use when the user later needs speaker labels or diarization.
