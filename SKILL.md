---
name: transcribe
description: Transcribe audio files to text with optional diarization and known-speaker hints using the bundled CLI. Use when the user wants text from audio or video, especially when speaker labeling or repeatable output matters.
---

# Audio Transcribe

## Metadata
- Trigger when: the user wants transcription, speaker labels, or structured transcript output from audio/video files.
- Do not use when: no audio path exists yet and the task is only about summarizing an already written transcript.

## Skill Purpose

Stay as the entrypoint for transcription work, then route into the narrowest lane: fast plain transcription or diarized speaker-aware transcription.

## Instructions
1. Collect the inputs first: file path, desired output format, language hint if any, and whether speaker labels are needed. Check that `OPENAI_API_KEY` is set; if it is missing, tell the user to set it locally and never ask them to paste the key into chat.
2. Choose the narrowest lane. Prefer `$transcribe-basic` for fast plain transcription. Prefer `$transcribe-diarize` only when speaker labels or diarization are actually required. If a child lane is unavailable in the current run, follow the same split here using `~/.codex/skills/transcribe/scripts/transcribe_diarize.py`. Use `~/.codex/skills/transcribe/references/api.md` only when you need model or format details.
3. Validate transcript quality, output location, and speaker labeling when used. Save artifacts under `output/transcribe/` when working in this repo and note any limitation such as chunking, poor audio quality, or missing speaker references.

## Non-Negotiable Acceptance Criteria
- Secrets stay in environment variables, never in chat or committed files.
- The default mode is fast text transcription, not diarization-heavy overkill.
- Output format and model choice match the user’s actual need.
- If dependencies or API access are missing, the skill says so directly.

## Output
- The transcript path or paths.
- The model and response format used.
- A short quality note covering diarization confidence or transcript caveats when relevant.
- `Next skill options` (only if needed): `$transcribe-basic` — fast text transcription without speaker labels; `$transcribe-diarize` — diarized transcription with optional known-speaker hints.
