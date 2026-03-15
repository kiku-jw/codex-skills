---
name: openclaw-council
description: Stress-test OpenClaw architecture or production-config changes with an isolated council pass, contradiction check, and independent Codex review. Use when autonomy, reliability, fallbacks, or deployment risk make a one-pass answer too weak.
---

# OpenClaw Council

## Metadata
- Trigger when: an OpenClaw design or config change is serious enough to deserve multi-pass review before go-live.
- Do not use when: the change is a quick tweak with no real autonomy, reliability, or rollback risk.

## Skill Purpose

Run three independent review surfaces so risky OpenClaw plans get contradiction checks, blind-spot reduction, and an explicit go/no-go gate before production changes land.

## Instructions
1. Write a short draft plan first so every reviewer sees the same concrete proposal. Keep the plan focused on the actual architecture or config change under review.
2. Run the isolated OpenClaw council pass, the contradiction-auditor pass, and the separate `codex exec` review. Use `/Users/nick/.codex/skills/openclaw-council/references/prompt-pack.md` when you need the exact review prompts or setup details.
3. Merge and deduplicate the findings into one revised plan with clear critical issues, contradictions, go/no-go guidance, and the gates that must close before the change is safe to apply.

## Non-Negotiable Acceptance Criteria
- All three review passes complete before risky production config changes are treated as approved.
- Preview models, proxies, and multi-provider fallbacks are treated as higher-risk until proven stable.
- The revised plan includes rollback and synthetic health checks.
- The final answer distinguishes merged consensus from unresolved contradiction.

## Output
- Critical findings first.
- A contradiction section naming hidden dependencies or incompatible assumptions.
- A revised plan and a go/no-go recommendation with explicit gates before go-live.
