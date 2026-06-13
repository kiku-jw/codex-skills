#!/usr/bin/env python3
"""Write a compact ffprobe summary for a rendered video."""

import argparse
import json
import shutil
import subprocess
import sys
from fractions import Fraction
from pathlib import Path


def run_ffprobe(video: Path) -> dict[str, object]:
    command = [
        "ffprobe",
        "-v",
        "error",
        "-print_format",
        "json",
        "-show_format",
        "-show_streams",
        str(video),
    ]
    result = subprocess.run(command, check=True, capture_output=True, text=True)
    return json.loads(result.stdout)


def number(value: object) -> float | None:
    if value in (None, "", "N/A"):
        return None
    try:
        return float(str(value))
    except ValueError:
        return None


def frame_rate(value: object) -> float | None:
    if value in (None, "", "0/0", "N/A"):
        return None
    try:
        return float(Fraction(str(value)))
    except (ValueError, ZeroDivisionError):
        return None


def first_stream(probe: dict[str, object], codec_type: str) -> dict[str, object] | None:
    streams = probe.get("streams")
    if not isinstance(streams, list):
        return None
    for stream in streams:
        if isinstance(stream, dict) and stream.get("codec_type") == codec_type:
            return stream
    return None


def summarize(video: Path, probe: dict[str, object]) -> dict[str, object]:
    format_info = probe.get("format")
    if not isinstance(format_info, dict):
        format_info = {}
    video_stream = first_stream(probe, "video") or {}
    audio_stream = first_stream(probe, "audio") or {}

    return {
        "path": str(video),
        "format": {
            "name": format_info.get("format_name"),
            "duration_seconds": number(format_info.get("duration")),
            "size_bytes": int(format_info.get("size", 0) or 0),
            "bit_rate": int(format_info.get("bit_rate", 0) or 0),
        },
        "video": {
            "codec": video_stream.get("codec_name"),
            "width": video_stream.get("width"),
            "height": video_stream.get("height"),
            "pix_fmt": video_stream.get("pix_fmt"),
            "avg_frame_rate": frame_rate(video_stream.get("avg_frame_rate")),
            "r_frame_rate": frame_rate(video_stream.get("r_frame_rate")),
            "duration_seconds": number(video_stream.get("duration")),
        },
        "audio": {
            "codec": audio_stream.get("codec_name"),
            "sample_rate": int(audio_stream.get("sample_rate", 0) or 0),
            "channels": audio_stream.get("channels"),
            "duration_seconds": number(audio_stream.get("duration")),
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("video", help="Input video file.")
    parser.add_argument("--out", help="Write JSON summary to this path.")
    args = parser.parse_args()

    if shutil.which("ffprobe") is None:
        parser.error("ffprobe is not available on PATH")
    video = Path(args.video)
    if not video.exists():
        parser.error(f"video does not exist: {video}")

    summary = summarize(video, run_ffprobe(video))
    payload = json.dumps(summary, indent=2) + "\n"
    if args.out:
        out = Path(args.out)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(payload, encoding="utf-8")
    else:
        sys.stdout.write(payload)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
