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

BAD_SUBSTRINGS = {
    "\u93b5\u89c4\u655e": "mojibake phrase for 批注",
    "\u951b\u6b5a": "mojibake punctuation",
    "\u701b\ufe3f": "mojibake phrase for 学",
    "\u752f\ue1bd": "mojibake phrase for 帮",
    "\u9422\u71b8": "mojibake phrase for 生",
    "\u93c1\u5bf8": "mojibake phrase for 整",
    "\u59af\u2033\u7d21": "mojibake phrase for 模式",
    "\u93c8\ue047": "mojibake phrase for 未",
    "\u6769\u6d9c": "mojibake phrase for 进",
    "\u5bb8\u8336": "mojibake phrase for 已",
    "\u7ed4\u72ba": "mojibake phrase for 章",
    "\u5bf0\u546f": "mojibake phrase for 待",
    "\u9473\u82a5": "mojibake phrase for 能",
    "\ub364\ud6c5\ud6f0": "mojibake phrase for 待确认",
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
        for marker, label in BAD_SUBSTRINGS.items():
            if marker in line:
                findings.append(f"{path}:{line_no}: found {label}: {marker}")
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
