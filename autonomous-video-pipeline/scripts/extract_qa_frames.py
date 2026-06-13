#!/usr/bin/env python3
"""Extract deterministic QA frames from a video with ffmpeg."""

import argparse
import shutil
import subprocess
from pathlib import Path


def parse_timestamps(raw_values: list[str]) -> list[str]:
    timestamps: list[str] = []
    for raw in raw_values:
        for part in raw.split(","):
            value = part.strip()
            if value:
                timestamps.append(value)
    return timestamps


def run(command: list[str]) -> None:
    subprocess.run(command, check=True)


def extract_specific(video: Path, out_dir: Path, timestamps: list[str]) -> None:
    for index, timestamp in enumerate(timestamps, start=1):
        safe = timestamp.replace(":", "-").replace(".", "_")
        output = out_dir / f"qa-{index:03d}-{safe}.jpg"
        run([
            "ffmpeg",
            "-hide_banner",
            "-loglevel",
            "error",
            "-ss",
            timestamp,
            "-i",
            str(video),
            "-frames:v",
            "1",
            "-q:v",
            "2",
            str(output),
        ])


def extract_interval(video: Path, out_dir: Path, every_seconds: float) -> None:
    output_pattern = out_dir / "qa-every-%04d.jpg"
    run([
        "ffmpeg",
        "-hide_banner",
        "-loglevel",
        "error",
        "-i",
        str(video),
        "-vf",
        f"fps=1/{every_seconds}",
        "-q:v",
        "2",
        str(output_pattern),
    ])


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("video", help="Input MP4 or video file.")
    parser.add_argument("--out", required=True, help="Output directory for QA frames.")
    parser.add_argument("--timestamps", nargs="*", default=[], help="Timestamps like 0, 00:00:05.5 or comma-separated lists.")
    parser.add_argument("--every", type=float, help="Extract one frame every N seconds.")
    args = parser.parse_args()

    if shutil.which("ffmpeg") is None:
        parser.error("ffmpeg is not available on PATH")
    video = Path(args.video)
    if not video.exists():
        parser.error(f"video does not exist: {video}")
    if args.every is not None and args.every <= 0:
        parser.error("--every must be positive")

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    timestamps = parse_timestamps(args.timestamps)
    if timestamps:
        extract_specific(video, out_dir, timestamps)
    if args.every is not None:
        extract_interval(video, out_dir, args.every)
    if not timestamps and args.every is None:
        parser.error("provide --timestamps, --every, or both")

    print(out_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
