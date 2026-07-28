#!/usr/bin/env python3
"""Reject accidental personal data from the public repository."""

from __future__ import annotations

import re
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EMAIL_PATTERN = re.compile(
    r"\b[A-Za-z0-9._%+-]+@([A-Za-z0-9.-]+\.[A-Za-z]{2,})\b"
)
ALLOWED_CONTENT_EMAIL_DOMAINS = {
    "example.com",
    "github.com",
    "kikuai.dev",
    "users.noreply.github.com",
}
ALLOWED_COMMIT_EMAIL_DOMAINS = {
    "github.com",
    "users.noreply.github.com",
}
PRIVATE_NAME = "Ni" + "ck"
DISALLOWED_TEXT = {
    "absolute home path": re.compile(
        r"/(?:Users|home)/[A-Za-z0-9._-]+|[A-Za-z]:\\Users\\[A-Za-z0-9._-]+"
    ),
    "personal name": re.compile(rf"\b{PRIVATE_NAME}\b", re.IGNORECASE),
    "location hint": re.compile(
        "|".join((re.escape("Europe/" + "Kyiv"), re.escape("Ukra" + "ine")))
    ),
    "private workflow hint": re.compile(
        re.escape("J" + "W-specific"), re.IGNORECASE
    ),
}


def text_files() -> list[Path]:
    return [
        path
        for path in ROOT.rglob("*")
        if path.is_file() and ".git" not in path.parts
    ]


def scan_content() -> list[tuple[str, str]]:
    findings: list[tuple[str, str]] = []
    for path in text_files():
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        relative = path.relative_to(ROOT).as_posix()
        for label, pattern in DISALLOWED_TEXT.items():
            if pattern.search(text):
                findings.append((label, relative))
        for domain in EMAIL_PATTERN.findall(text):
            if domain.lower() not in ALLOWED_CONTENT_EMAIL_DOMAINS:
                findings.append(("unapproved email domain", relative))
    return findings


def scan_history() -> list[tuple[str, str]]:
    findings: list[tuple[str, str]] = []
    output = subprocess.check_output(
        ["git", "log", "--all", "--format=%an%x09%ae%x09%cn%x09%ce"],
        cwd=ROOT,
        text=True,
    )
    for line in output.splitlines():
        author_name, author_email, committer_name, committer_email = line.split("\t")
        if DISALLOWED_TEXT["personal name"].search(
            author_name
        ) or DISALLOWED_TEXT["personal name"].search(committer_name):
            findings.append(("personal name in commit metadata", "Git history"))
        for email in (author_email, committer_email):
            if email.rpartition("@")[2].lower() not in ALLOWED_COMMIT_EMAIL_DOMAINS:
                findings.append(("unapproved commit email domain", "Git history"))

    patch_history = subprocess.check_output(
        [
            "git",
            "log",
            "--all",
            "--root",
            "--format=",
            "--patch",
            "--no-ext-diff",
        ],
        cwd=ROOT,
        text=True,
    )
    for label, pattern in DISALLOWED_TEXT.items():
        if pattern.search(patch_history):
            findings.append((f"{label} in commit content", "Git history"))
    for domain in EMAIL_PATTERN.findall(patch_history):
        if domain.lower() not in ALLOWED_CONTENT_EMAIL_DOMAINS:
            findings.append(("unapproved email domain in commit content", "Git history"))
    return findings


def main() -> int:
    findings = sorted(set(scan_content() + scan_history()))
    if not findings:
        print("Public privacy check passed.")
        return 0
    print("Public privacy check failed; inspect these categories and paths:")
    for label, path in findings:
        print(f"- {label}: {path}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
