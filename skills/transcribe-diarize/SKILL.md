---
name: transcribe-diarize
description: Produce a speaker-aware transcript with diarization and optional known-speaker hints using the bundled CLI. Use when the user explicitly needs speaker labels.
---

# Transcribe Diarize

## Metadata
- Trigger when: the user explicitly wants speaker labels, diarization, or structured speaker-aware transcript output.
- Do not use when: a plain fast transcript is enough.

## Skill Purpose

Produce a diarized transcript with the narrow settings required for speaker-aware output instead of treating every transcription job as a plain text task.

## Instructions
1. Gather the audio path, desired output location, and any known-speaker reference files. Check that `OPENAI_API_KEY` is set before doing anything else.
2. Run `~/.codex/skills/transcribe/scripts/transcribe_diarize.py` with `gpt-4o-transcribe-diarize`, `diarized_json`, and any provided `--known-speaker` hints under a stable output path such as `output/transcribe/`.
3. Validate the transcript, speaker labels, and segment boundaries. State clearly when speaker confidence is weak because references were missing or the audio is noisy.

## Non-Negotiable Acceptance Criteria
- The task explicitly needs diarization or speaker labels.
- Output format is diarization-capable and the chosen model matches that need.
- Known-speaker hints are used only when they actually exist; they are never invented.
- Confidence or segmentation caveats are called out when labels are weak.

## Output
- The diarized transcript path.
- The model, response format, and any known-speaker hints used.
- A short note on label confidence, segmentation quality, or caveats.
- `Next skill options` (only if needed): `$transcribe-basic` — use when the user decides speaker labeling is unnecessary after all.
