# Storyboard And Scene Manifest

Use this reference before generating expensive media or rendering motion
graphics. The goal is to make timing, assets, and QA targets explicit.

## Minimum Scene Fields

Use JSON, YAML, Markdown tables, or a repo-local format, but preserve these
fields:

- `scene_id`: stable ID such as `scene-001`.
- `narration_chunk_id`: matching `narration-###` ID.
- `start_seconds` and `end_seconds`: planned timeline range.
- `visual_intent`: what the viewer should understand.
- `speaker_visibility`: `full`, `pip`, `side-by-side`, `hidden-ok`, or
  `not-applicable`.
- `motion_graphics`: specific chart, callout, diagram, counter, timeline, or
  none.
- `assets_required`: audio, avatar clip, screenshots, product images, generated
  graphics, fonts, or other dependencies.
- `qa_timestamps`: timestamps that should be extracted for frame inspection.
- `risk_notes`: timing, factual, layout, provider, or authorization risks.

## Example

```json
{
  "scene_id": "scene-003",
  "narration_chunk_id": "narration-002",
  "start_seconds": 42.0,
  "end_seconds": 67.5,
  "visual_intent": "Show the three-step pipeline from script to avatar clip.",
  "speaker_visibility": "side-by-side",
  "motion_graphics": "Animated pipeline with active step highlight.",
  "assets_required": ["audio/narration-002.wav", "avatar/narration-002.mp4"],
  "qa_timestamps": [43.0, 54.5, 66.0],
  "risk_notes": ["Keep pipeline labels under 4 words each."]
}
```

## Rules

- Create scenes before provider calls when the provider cost is non-trivial.
- Keep one scene responsible for one idea.
- Prefer fewer strong scenes over dense graphic churn.
- Put QA timestamps near each meaningful visual change.
- If the timeline changes after render, update the scene manifest before final
  QA.
