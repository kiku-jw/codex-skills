#!/usr/bin/env python3
"""Create a starter manifest and folder layout for a video production run."""

import argparse
import json
from datetime import datetime, timezone
from pathlib import Path


DEFAULT_DIRS = [
    "sources",
    "script",
    "audio",
    "avatar",
    "scenes",
    "renders",
    "qa/frames",
    "qa/reports",
]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project_dir", help="Directory where the video package should live.")
    parser.add_argument("--title", required=True)
    parser.add_argument("--duration", default="2-4 minutes")
    parser.add_argument("--aspect-ratio", default="16:9")
    parser.add_argument("--language", default="en")
    parser.add_argument("--manifest-name", default="video-manifest.json")
    args = parser.parse_args()

    project_dir = Path(args.project_dir)
    project_dir.mkdir(parents=True, exist_ok=True)
    for name in DEFAULT_DIRS:
        (project_dir / name).mkdir(parents=True, exist_ok=True)

    manifest = {
        "title": args.title,
        "created_at": datetime.now(timezone.utc).isoformat(),
        "target": {
            "duration": args.duration,
            "aspect_ratio": args.aspect_ratio,
            "language": args.language,
        },
        "production_contract": {
            "audience": "",
            "style": "",
            "budget_ceiling": "",
            "authorized_voice_or_avatar": "",
            "acceptance_criteria": [],
        },
        "sources": [],
        "script": {
            "path": "script/script.md",
            "chunks_manifest": "script/narration-chunks.json",
        },
        "storyboard": {
            "path": "scenes/storyboard.md",
            "scene_manifest": "scenes/scene-manifest.json",
        },
        "assets": {
            "audio": [],
            "avatar_clips": [],
            "motion_graphics": [],
            "other": [],
        },
        "render": {
            "commands": [],
            "final_mp4": "renders/final.mp4",
        },
        "qa": {
            "ffprobe": "qa/reports/ffprobe-summary.json",
            "frames_dir": "qa/frames",
            "package_validation": "qa/reports/package-validation.json",
            "checks": [],
            "limitations": [],
        },
    }

    manifest_path = project_dir / args.manifest_name
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(manifest_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
