#!/usr/bin/env python3
"""Split narration text into stable, sub-minute chunks for TTS/avatar steps."""

import argparse
import json
import re
import sys
from pathlib import Path


SENTENCE_RE = re.compile(r"(?<=[.!?])\s+")


def read_text(path: str | None) -> str:
    if path:
        return Path(path).read_text(encoding="utf-8")
    return sys.stdin.read()


def split_sentences(text: str) -> list[str]:
    paragraphs = [part.strip() for part in re.split(r"\n\s*\n", text) if part.strip()]
    sentences: list[str] = []
    for paragraph in paragraphs:
        sentences.extend(part.strip() for part in SENTENCE_RE.split(paragraph) if part.strip())
    return sentences


def word_count(text: str) -> int:
    return len(re.findall(r"\b[\w'-]+\b", text))


def build_chunks(text: str, max_seconds: float, wpm: float) -> list[dict[str, object]]:
    max_words = max(1, int(max_seconds * wpm / 60.0))
    chunks: list[dict[str, object]] = []
    current: list[str] = []
    current_words = 0

    for sentence in split_sentences(text):
        sentence_words = word_count(sentence)
        if current and current_words + sentence_words > max_words:
            chunks.append(make_chunk(len(chunks) + 1, current, wpm))
            current = []
            current_words = 0
        current.append(sentence)
        current_words += sentence_words

    if current:
        chunks.append(make_chunk(len(chunks) + 1, current, wpm))

    return chunks


def make_chunk(index: int, sentences: list[str], wpm: float) -> dict[str, object]:
    text = " ".join(sentences).strip()
    words = word_count(text)
    return {
        "id": f"narration-{index:03d}",
        "word_count": words,
        "estimated_seconds": round(words / wpm * 60.0, 2),
        "text": text,
    }


def write_chunk_files(chunks: list[dict[str, object]], output_dir: Path) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    for chunk in chunks:
        chunk_id = str(chunk["id"])
        text = str(chunk["text"])
        (output_dir / f"{chunk_id}.txt").write_text(text + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", nargs="?", help="Narration text file. Reads stdin when omitted.")
    parser.add_argument("--max-seconds", type=float, default=55.0)
    parser.add_argument("--wpm", type=float, default=150.0)
    parser.add_argument("--out", help="Write chunk manifest JSON to this path.")
    parser.add_argument("--chunk-dir", help="Optional directory for one text file per chunk.")
    args = parser.parse_args()

    text = read_text(args.input).strip()
    if not text:
        parser.error("input text is empty")
    if args.max_seconds <= 0:
        parser.error("--max-seconds must be positive")
    if args.wpm <= 0:
        parser.error("--wpm must be positive")

    chunks = build_chunks(text, args.max_seconds, args.wpm)
    manifest = {
        "max_seconds": args.max_seconds,
        "wpm": args.wpm,
        "chunk_count": len(chunks),
        "chunks": chunks,
    }

    if args.chunk_dir:
        write_chunk_files(chunks, Path(args.chunk_dir))

    payload = json.dumps(manifest, indent=2, ensure_ascii=False) + "\n"
    if args.out:
        Path(args.out).write_text(payload, encoding="utf-8")
    else:
        sys.stdout.write(payload)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
