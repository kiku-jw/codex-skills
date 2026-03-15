---
name: screenshot
description: Capture desktop or system screenshots with the bundled OS helpers when the user explicitly asks for a screenshot or when tool-specific capture cannot reach the target. Supports full screen, app/window, active window, and region capture.
---

# Screenshot Capture

## Metadata
- Trigger when: the user wants an OS-level screenshot or a better-integrated tool cannot capture the target surface.
- Do not use when: a tool-specific screenshot path already solves the task more directly and faithfully.

## Skill Purpose

Use the bundled helpers to capture desktop, app, window, or region screenshots predictably across platforms without re-deriving OS-specific commands every time.

## Instructions
1. Choose the save-location rule first: user path if provided, OS default if the user just wants a screenshot, or temp storage when Codex needs the image for its own inspection. On macOS, run `/Users/nick/.codex/skills/screenshot/scripts/ensure_macos_permissions.sh` before app/window capture when possible.
2. Use the exact helper that matches the OS: `/Users/nick/.codex/skills/screenshot/scripts/take_screenshot.py` for macOS/Linux and `/Users/nick/.codex/skills/screenshot/scripts/take_screenshot.ps1` for Windows. Prefer helper flags such as `--mode temp`, `--app`, `--window-name`, `--active-window`, `--window-id`, or `--region` instead of improvising raw OS commands. Fall back to native commands only if the helper path is unavailable.
3. If the capture is for Codex inspection, view the saved temp image(s) in order and only manipulate them if needed. If permissions or prerequisites fail, report the missing piece clearly and stop instead of pretending a capture exists.

## Non-Negotiable Acceptance Criteria
- Prefer tool-specific capture first when it is clearly better for the target.
- Do not guess app names, window ids, or captured content.
- Each generated image path must be reported explicitly, especially when multiple windows or displays are captured.
- If OS permissions or dependencies block capture, say that directly.

## Output
- The saved screenshot path or paths.
- The capture mode used: full screen, app/window, active window, or region.
- If relevant, the next inspection step, such as opening/viewing the image or retrying after permission setup.
