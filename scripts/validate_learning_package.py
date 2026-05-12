#!/usr/bin/env python3
"""Validate learning-workflow-designer skill metadata and package outputs."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


REQUIRED_PACKAGE_FILES = [
    "learning-content.md",
    "exercises.md",
    "reference-answers.md",
    "learning-progress.json",
]

REQUIRED_PROGRESS_FIELDS = [
    "project_name",
    "source_summary",
    "mode",
    "density",
    "total_levels",
    "level",
    "stars",
    "earned_xp",
    "total_xp",
    "nodes",
    "exercises",
    "chapter_map",
    "positive_feedback",
    "next_step",
]

VALID_NODE_STATES = {"locked", "active", "unlocked"}
ANSWER_SPACE_PATTERNS = [
    re.compile(r"_{6,}"),
    re.compile(r"\|\s*[^|\n]+\s*\|\s*\|"),
    re.compile(r"(?i)\b(answer|response|notes|record|evidence)\b\s*:"),
    re.compile(r"(答|填写|记录|证据|结论|输出|观察)\s*(区|：|:)"),
]

ENGINEERING_MARKERS = {
    "core question": ["核心问题", "core question"],
    "understanding task": ["理解任务", "required understanding", "read/trace"],
    "hands-on test": ["实操测试", "hands-on test", "run/observe"],
    "stage acceptance": ["阶段验收", "验收标准", "acceptance"],
}


@dataclass
class Finding:
    path: Path
    message: str


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def load_json(path: Path) -> dict[str, Any]:
    try:
        data = json.loads(read_text(path))
    except json.JSONDecodeError as exc:
        raise ValueError(f"invalid JSON: {exc}") from exc
    if not isinstance(data, dict):
        raise ValueError("top-level JSON value must be an object")
    return data


def add(failures: list[Finding], path: Path, message: str) -> None:
    failures.append(Finding(path=path, message=message))


def as_int(value: Any, default: int = 0) -> int:
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


def validate_frontmatter(skill_root: Path, failures: list[Finding]) -> None:
    skill_file = skill_root / "SKILL.md"
    if not skill_file.exists():
        add(failures, skill_file, "missing SKILL.md")
        return

    text = read_text(skill_file)
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        add(failures, skill_file, "missing opening YAML frontmatter marker")
        return

    try:
        end_index = next(index for index, line in enumerate(lines[1:], start=1) if line.strip() == "---")
    except StopIteration:
        add(failures, skill_file, "missing closing YAML frontmatter marker")
        return

    frontmatter = lines[1:end_index]
    keys: set[str] = set()
    for number, line in enumerate(frontmatter, start=2):
        if not line.strip() or line.startswith((" ", "\t", "-")):
            continue
        if ":" not in line:
            add(failures, skill_file, f"frontmatter line {number} is not a key/value pair")
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        keys.add(key)
        if value and not value.startswith((">", "|", "'", '"')) and ": " in value:
            add(
                failures,
                skill_file,
                f"frontmatter line {number} has an unquoted scalar containing ': '; use quotes or a block scalar",
            )

    for required in ("name", "description"):
        if required not in keys:
            add(failures, skill_file, f"frontmatter missing required key: {required}")


def validate_answer_space(package_dir: Path, failures: list[Finding]) -> None:
    exercises_path = package_dir / "exercises.md"
    if not exercises_path.exists():
        return
    text = read_text(exercises_path)
    if not any(pattern.search(text) for pattern in ANSWER_SPACE_PATTERNS):
        add(failures, exercises_path, "exercise document does not appear to contain learner answer space")


def validate_reference_separation(package_dir: Path, failures: list[Finding]) -> None:
    exercises_path = package_dir / "exercises.md"
    answers_path = package_dir / "reference-answers.md"
    if not exercises_path.exists() or not answers_path.exists():
        return
    exercises = read_text(exercises_path).strip()
    answers = read_text(answers_path).strip()
    if exercises and answers and exercises == answers:
        add(failures, answers_path, "reference answers must be separate from the learner exercise document")


def validate_progress(package_dir: Path, failures: list[Finding]) -> None:
    progress_path = package_dir / "learning-progress.json"
    if not progress_path.exists():
        return

    try:
        data = load_json(progress_path)
    except ValueError as exc:
        add(failures, progress_path, str(exc))
        return

    for field in REQUIRED_PROGRESS_FIELDS:
        if field not in data:
            add(failures, progress_path, f"missing required progress field: {field}")

    nodes = data.get("nodes", [])
    exercises = data.get("exercises", [])
    chapter_map = data.get("chapter_map", [])
    if not isinstance(nodes, list):
        add(failures, progress_path, "nodes must be a list")
        nodes = []
    if not isinstance(exercises, list):
        add(failures, progress_path, "exercises must be a list")
        exercises = []
    if not isinstance(chapter_map, list):
        add(failures, progress_path, "chapter_map must be a list")
        chapter_map = []

    total_xp = as_int(data.get("total_xp"))
    exercise_total = sum(as_int(exercise.get("points")) for exercise in exercises if isinstance(exercise, dict))
    if exercise_total != total_xp:
        add(failures, progress_path, f"exercise points total {exercise_total} does not equal total_xp {total_xp}")

    node_ids = {str(node.get("id")) for node in nodes if isinstance(node, dict) and node.get("id")}
    chapter_map_chapters = {
        as_int(chapter.get("chapter"))
        for chapter in chapter_map
        if isinstance(chapter, dict) and "chapter" in chapter
    }
    exercise_chapters = {
        as_int(exercise.get("chapter"))
        for exercise in exercises
        if isinstance(exercise, dict) and "chapter" in exercise
    }
    missing_chapters = sorted(chapter for chapter in exercise_chapters if chapter not in chapter_map_chapters)
    if missing_chapters:
        add(failures, progress_path, f"chapter_map does not cover exercise chapters: {missing_chapters}")

    for index, node in enumerate(nodes, start=1):
        if not isinstance(node, dict):
            add(failures, progress_path, f"nodes[{index}] must be an object")
            continue
        for field in ("id", "name", "state", "earned_points", "total_points", "chapters"):
            if field not in node:
                add(failures, progress_path, f"node {node.get('id', index)} missing field: {field}")
        state = node.get("state")
        if state is not None and state not in VALID_NODE_STATES:
            add(failures, progress_path, f"node {node.get('id', index)} has invalid state: {state}")

    points_by_node: dict[str, int] = {}
    for index, exercise in enumerate(exercises, start=1):
        if not isinstance(exercise, dict):
            add(failures, progress_path, f"exercises[{index}] must be an object")
            continue
        for field in ("id", "chapter", "node_id", "points", "earned_points"):
            if field not in exercise:
                add(failures, progress_path, f"exercise {exercise.get('id', index)} missing field: {field}")
        node_id = str(exercise.get("node_id", ""))
        if node_id and node_id not in node_ids:
            add(failures, progress_path, f"exercise {exercise.get('id', index)} references unknown node_id: {node_id}")
        points_by_node[node_id] = points_by_node.get(node_id, 0) + as_int(exercise.get("points"))

    for node in nodes:
        if not isinstance(node, dict):
            continue
        node_id = str(node.get("id", ""))
        expected = points_by_node.get(node_id, 0)
        actual = as_int(node.get("total_points"))
        if node_id in points_by_node and actual != expected:
            add(failures, progress_path, f"node {node_id} total_points {actual} does not equal exercise points {expected}")

    for index, chapter in enumerate(chapter_map, start=1):
        if not isinstance(chapter, dict):
            add(failures, progress_path, f"chapter_map[{index}] must be an object")
            continue
        for field in ("chapter", "title", "nodes"):
            if field not in chapter:
                add(failures, progress_path, f"chapter_map entry {index} missing field: {field}")
        for node_id in chapter.get("nodes", []) if isinstance(chapter.get("nodes"), list) else []:
            if str(node_id) not in node_ids:
                add(failures, progress_path, f"chapter_map entry {index} references unknown node_id: {node_id}")


def validate_engineering_markers(package_dir: Path, failures: list[Finding]) -> None:
    combined = ""
    for name in ("learning-content.md", "exercises.md", "reference-answers.md"):
        path = package_dir / name
        if path.exists():
            combined += "\n" + read_text(path)

    for label, markers in ENGINEERING_MARKERS.items():
        if not any(marker.lower() in combined.lower() for marker in markers):
            add(failures, package_dir, f"engineering package missing {label}")


def validate_package(package_dir: Path, failures: list[Finding], engineering: bool) -> None:
    if not package_dir.exists():
        add(failures, package_dir, "package directory does not exist")
        return
    if not package_dir.is_dir():
        add(failures, package_dir, "package path is not a directory")
        return

    for name in REQUIRED_PACKAGE_FILES:
        path = package_dir / name
        if not path.exists():
            add(failures, path, "missing required package file")

    validate_answer_space(package_dir, failures)
    validate_reference_separation(package_dir, failures)
    validate_progress(package_dir, failures)
    if engineering:
        validate_engineering_markers(package_dir, failures)


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate learning package structure and progress data.")
    parser.add_argument("packages", nargs="*", type=Path, help="Package directories to validate")
    parser.add_argument("--skill-root", type=Path, help="Validate SKILL.md frontmatter in this repository root")
    parser.add_argument(
        "--engineering",
        action="store_true",
        help="Also require engineering/project-lab markers such as core questions and stage acceptance",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    failures: list[Finding] = []

    if args.skill_root:
        validate_frontmatter(args.skill_root, failures)

    for package_dir in args.packages:
        validate_package(package_dir, failures, args.engineering)

    if failures:
        for failure in failures:
            print(f"{failure.path}: {failure.message}", file=sys.stderr)
        return 1

    checked = len(args.packages)
    if args.skill_root:
        checked += 1
    print(f"Validated {checked} target(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
