#!/usr/bin/env python3
"""Sync the runtime Codex skill folder with only files needed at runtime."""

from __future__ import annotations

import argparse
import os
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_TARGET = Path.home() / ".codex" / "skills" / "learning-workflow-designer"
ALLOW = ["SKILL.md", "agents", "references", "scripts", "assets", "templates", "LICENSE"]


def safe_target(path: Path) -> Path:
    resolved = path.resolve()
    if resolved.name != "learning-workflow-designer":
        raise SystemExit(f"Refusing to sync to unexpected folder: {resolved}")
    return resolved


def remove_contents(path: Path) -> None:
    if not path.exists():
        return
    for item in path.iterdir():
        if item.is_dir():
            shutil.rmtree(item)
        else:
            item.unlink()


def copy_item(source: Path, target: Path) -> None:
    if source.is_dir():
        ignore = shutil.ignore_patterns("__pycache__", "*.pyc", ".pytest_cache")
        shutil.copytree(source, target, ignore=ignore)
    elif source.exists():
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)


def sync(target: Path) -> None:
    target = safe_target(target)
    target.mkdir(parents=True, exist_ok=True)
    remove_contents(target)
    for name in ALLOW:
        copy_item(ROOT / name, target / name)


def main() -> int:
    parser = argparse.ArgumentParser(description="Sync a pruned runtime Codex skill install.")
    parser.add_argument("--target", type=Path, default=Path(os.getenv("CODEX_SKILL_TARGET", DEFAULT_TARGET)))
    args = parser.parse_args()
    sync(args.target)
    print(f"Synced runtime skill to {args.target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
