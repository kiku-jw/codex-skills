---
name: illustration-prompt
description: Turn vague image requests into generator-ready illustration prompts for Midjourney, DALL-E, Flux, Stable Diffusion, or similar tools. Trigger on requests like illustration prompt, prompt for image, visual direction, art prompt, moodboard prompt, hero image prompt, Midjourney prompt, DALL-E prompt, Flux prompt, or when the user wants help describing an image precisely. Especially useful when the user has reference images and wants the prompt to inherit the right style cues without copying them blindly.
---

# Illustration Prompt

Use this skill when the main task is visual direction and prompt quality, not coding.

Typical prompts:

- `write an illustration prompt`
- `turn this vague idea into a Midjourney prompt`
- `help me make an image prompt from these refs`
- `I need a hero image prompt for this page`
- `make this visual brief more precise`

## Core Principle

References and context beat adjectives.

Default workflow:

`context -> style -> references -> scene -> palette -> format -> structured prompt -> targeted iteration`

## Interview Flow

Walk step by step, but collapse or confirm steps that are already known from the conversation.

1. `Context`
   - Where will the image live: hero, card, social post, slide, cover, app icon, background, illustration inside a feature page.
   - If the project context is already known, reuse it instead of asking generic questions.
2. `Style`
   - Confirm or propose style families: isometric, flat, voxel, watercolor, photoreal, 3D render, collage, line art, pixel art, editorial illustration, and so on.
   - Ask about detail density: minimal, medium, rich.
3. `References`
   - Strongly prefer 2-5 references when available.
   - If refs are provided, read `references/reference-analysis.md`.
   - Ask what exactly should be borrowed and what should not be borrowed from each ref.
   - Ask which reference is primary when they conflict.
   - Ask which generator or model they plan to use (optional).
4. `Scene`
   - Offer 2-3 scene directions when the brief is vague.
   - Then lock the main subject, supporting elements, camera angle, and what story the image should tell.
5. `Palette and Mood`
   - Ask for theme, brand colors, mood, and lighting.
   - Reuse project colors, CSS variables, or known design tokens when they exist.
6. `Format`
   - Confirm aspect ratio, size, and background behavior.
   - If the user does not know the size, recommend one based on context.

## Reference-First Rules

- If the user provides references, summarize the shared patterns before drafting.
- Name the traits you will carry forward:
  - composition
  - perspective
  - shape language
  - texture or material feel
  - palette
  - lighting
  - detail density
  - negative space
- If the refs conflict, call out the tension instead of faking coherence.
- If there are no refs, compensate by asking more concrete scene and palette questions.

## Output

After the interview, output:

1. A short kebab-case file name.
2. One structured prompt in English using the 8-block format from `references/prompt-template.md`.
3. Optional short generator note only when a model-specific tweak matters.

## Prompt Quality Rules

- Be concrete about perspective, light direction, scale, and material cues.
- Use HEX colors when known.
- Default to `no text` unless the user explicitly wants text inside the image.
- If people are visible, describe poses and keep anatomy constraints explicit.
- If 3 or more identical objects matter, state the exact count and placement.
- Revise by editing specific blocks, not by rewriting everything from scratch.

## Handoff

- If the user wants only the prompt, stop after the structured output.
- If the user also wants the image generated here, hand off to [$imagegen](~/.codex/skills/imagegen/SKILL.md) after the prompt is approved.
