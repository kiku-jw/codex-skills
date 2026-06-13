# Forward Test Prompts

Use these prompts when checking whether the skill is usable in a fresh session.
Pass only the skill path and the test request. Do not pass expected answers.

## Planning-Only Test

```text
Use $autonomous-video-pipeline from the installed skill directory.
Create the production contract, manifest plan, narration chunking plan, storyboard
outline, and QA plan for a 45-second explainer video about a local CSV cleanup
tool. Do not call paid APIs or generate provider media.
```

## Local Artifact Test

```text
Use $autonomous-video-pipeline from the installed skill directory.
Create a fully local 20-second placeholder MP4 package from a simple generated
script, using local text/audio/video placeholders only. Produce the manifest,
ffprobe summary, QA frames, package validation report, and final response.
Do not call external APIs.
```

## Review Criteria

- The agent should create or update a manifest early.
- Narration chunks and scenes should have stable IDs.
- The final response should include evidence paths, not just prose.
- The agent should refuse or pause on cloned voice/avatar use without explicit
  authorization.
- The package validator should pass for final local artifact tests.
