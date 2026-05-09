#!/usr/bin/env python3
"""Detect common Chinese text corruption markers in generated text files."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


TEXT_SUFFIXES = {
    ".css",
    ".csv",
    ".html",
    ".htm",
    ".json",
    ".md",
    ".py",
    ".txt",
    ".yaml",
    ".yml",
}

SKIP_DIRS = {
    ".git",
    ".hg",
    ".svn",
    "__pycache__",
    "node_modules",
}

BAD_MARKERS = {
    "\ufffd": "replacement character",
    "\u951f": "mojibake marker",
    "\u93b5": "mojibake marker",
}

QUESTION_RUN = re.compile(r"\?{4,}")


def iter_text_files(paths: list[Path]) -> list[Path]:
    files: list[Path] = []
    for path in paths:
        if path.is_file():
            if path.suffix.lower() in TEXT_SUFFIXES:
                files.append(path)
            continue
        if not path.exists():
            continue
        for item in path.rglob("*"):
            if any(part in SKIP_DIRS for part in item.parts):
                continue
            if item.is_file() and item.suffix.lower() in TEXT_SUFFIXES:
                files.append(item)
    return files


def scan_file(path: Path) -> list[str]:
    findings: list[str] = []
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError as exc:
        return [f"{path}: cannot decode as UTF-8: {exc}"]

    for line_no, line in enumerate(text.splitlines(), start=1):
        for marker, label in BAD_MARKERS.items():
            if marker in line:
                findings.append(f"{path}:{line_no}: found {label}")
        if QUESTION_RUN.search(line):
            findings.append(f"{path}:{line_no}: found repeated question marks")
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate generated text files for encoding damage.")
    parser.add_argument("paths", nargs="+", type=Path, help="Files or directories to scan")
    args = parser.parse_args()

    findings: list[str] = []
    for path in iter_text_files(args.paths):
        findings.extend(scan_file(path))

    if findings:
        print("Encoding validation failed:")
        for finding in findings:
            print(f"- {finding}")
        return 1

    print("Encoding validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
