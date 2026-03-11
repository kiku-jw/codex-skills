# Prompt Template

Use this structure for the final English prompt.

## Blocks

- `SCENE`: what the viewer sees, camera angle, composition, relative placement
- `STYLE`: art style, rendering approach, detail density, stylistic anchors
- `OBJECTS`: the main subject and supporting elements, with scale and position
- `COLORS`: palette, HEX codes when known, accent and shadow behavior
- `ATMOSPHERE`: lighting, mood, depth, ambient effects
- `EDGES`: border treatment, fade, crop, floating island, bleed, vignette
- `FORMAT`: pixel size, aspect ratio, background type
- `NEGATIVE`: what must not appear

## Default guards

- Text:
  - If the user did not ask for text, add `no text, no letters, no watermark, no logo`.
- People:
  - If hands are visible, describe the pose and state natural anatomy.
- Vehicles:
  - If a vehicle appears, explicitly keep windows transparent and doors intact unless the scene says otherwise.
- Counting:
  - If exact count matters for 3 or more similar objects, state the exact number and placement.

## Writing bar

- Prefer a prompt long enough to remove ambiguity.
- Concrete nouns beat mood adjectives.
- State light direction.
- State perspective explicitly.
- Tie the prompt back to the chosen references when they exist.
