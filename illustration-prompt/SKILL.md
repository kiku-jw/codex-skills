---
name: illustration-prompt
description: Turn a vague image request into a generator-ready illustration prompt for Midjourney, DALL-E, Flux, Stable Diffusion, or similar tools. Use when the user needs visual direction, prompt structure, or reference-aware image prompting rather than image generation code.
---

# Illustration Prompt

## Metadata
- Trigger when: the real work is turning a visual idea plus references into a high-quality prompt.
- Do not use when: the user already has a finished prompt or wants direct generation without prompt design.

## Skill Purpose

Translate vague visual intent into a concrete, reference-aware prompt that a generator can follow without leaning on hand-wavy adjective soup.

## Instructions
1. Lock the brief in this order: placement/context, style family, detail density, references, scene, palette/mood, and format. Collapse questions that the conversation already answered; do not re-interview for sport.
2. If references are present, summarize what should be borrowed and what should not. Read `/Users/nick/.codex/skills/illustration-prompt/references/reference-analysis.md` when you need the reference-reading checklist and `/Users/nick/.codex/skills/illustration-prompt/references/prompt-template.md` for the 8-block prompt structure.
3. Return one structured prompt in English plus a short filename and only the minimal model-specific tweak when it materially changes the result. If the user wants actual generation afterward, hand off to whatever image-generation tool is available in the current environment.

## Non-Negotiable Acceptance Criteria
- References and explicit scene constraints outrank decorative adjectives.
- Conflicting references are called out instead of blended into fake coherence.
- Perspective, composition, palette, material cues, and count-sensitive objects are concrete when they matter.
- Default to `no text` in the image unless the user explicitly asks for text.

## Output
- A short kebab-case filename.
- One structured English prompt using the 8-block format.
- An optional short generator note only when a model-specific tweak genuinely matters.
