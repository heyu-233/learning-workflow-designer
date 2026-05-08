#!/usr/bin/env python3
"""Render a static skill-tree HTML page from learning-progress.json."""

from __future__ import annotations

import argparse
import html
import json
from pathlib import Path
from string import Template
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_TEMPLATE = ROOT / "assets" / "html-templates" / "skill-tree.html"

STATE_LABELS = {
    "locked": "未解锁",
    "active": "进行中",
    "unlocked": "已解锁",
}

STATE_CLASSES = {
    "locked": "todo",
    "active": "doing",
    "unlocked": "done",
}


def esc(value: Any) -> str:
    return html.escape(str(value), quote=True)


def percent(earned: int | float, total: int | float) -> int:
    if not total:
        return 0
    return max(0, min(100, round((earned / total) * 100)))


def render_stars(stars: int | float) -> str:
    count = max(0, min(5, int(stars)))
    return "".join("★" if index < count else "☆" for index in range(5))


def render_nodes(nodes: list[dict[str, Any]]) -> str:
    rows: list[str] = []
    for node in nodes:
        state = str(node.get("state", "locked"))
        earned = int(node.get("earned_points", 0))
        total = int(node.get("total_points", 0))
        progress = percent(earned, total)
        chapters = ", ".join(str(chapter) for chapter in node.get("chapters", []))
        label = STATE_LABELS.get(state, state)
        css_class = STATE_CLASSES.get(state, "todo")
        rows.append(
            f"""
            <article class="node-card {css_class}">
              <div class="node-top">
                <div>
                  <h3>{esc(node.get("name", node.get("id", "未命名节点")))}</h3>
                  <p>{esc(node.get("description", ""))}</p>
                </div>
                <span class="badge {css_class}">{esc(label)}</span>
              </div>
              <div class="meter"><span style="width:{progress}%"></span></div>
              <div class="node-meta">
                <span>{earned}/{total} XP</span>
                <span>章节 {esc(chapters or "-")}</span>
              </div>
            </article>
            """.strip()
        )
    return "\n".join(rows)


def render_chapter_table(chapter_map: list[dict[str, Any]]) -> str:
    rows = []
    for chapter in chapter_map:
        nodes = ", ".join(str(node) for node in chapter.get("nodes", []))
        rows.append(
            "<tr>"
            f"<td>{esc(chapter.get('chapter', '-'))}</td>"
            f"<td>{esc(chapter.get('title', ''))}</td>"
            f"<td>{esc(nodes)}</td>"
            "</tr>"
        )
    body = "\n".join(rows) or '<tr><td colspan="3">暂无章节映射</td></tr>'
    return (
        "<table>"
        "<thead><tr><th>章</th><th>主题</th><th>能力节点</th></tr></thead>"
        f"<tbody>{body}</tbody>"
        "</table>"
    )


def render(progress_path: Path, output_path: Path, template_path: Path = DEFAULT_TEMPLATE) -> None:
    data = json.loads(progress_path.read_text(encoding="utf-8"))
    template = Template(template_path.read_text(encoding="utf-8"))
    total_xp = int(data.get("total_xp", 0))
    earned_xp = int(data.get("earned_xp", 0))
    feedback = data.get("positive_feedback", {})

    html_text = template.safe_substitute(
        project_name=esc(data.get("project_name", "学习技能树")),
        subtitle=esc(data.get("source_summary", "")),
        mode=esc(data.get("mode", "learning")),
        density=esc(data.get("density", "lightweight")),
        level=esc(data.get("level", 1)),
        stars=render_stars(data.get("stars", 0)),
        earned_xp=earned_xp,
        total_xp=total_xp,
        xp_percent=percent(earned_xp, total_xp),
        nodes_html=render_nodes(data.get("nodes", [])),
        chapter_table_html=render_chapter_table(data.get("chapter_map", [])),
        chapter_gain=esc(feedback.get("chapter_gain", "")),
        skill_tree_progress=esc(feedback.get("skill_tree_progress", "")),
        next_step=esc(data.get("next_step") or feedback.get("next_step", "")),
        progress_json=html.escape(json.dumps(data, ensure_ascii=False, indent=2), quote=False),
    )
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(html_text, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description="Render skill-tree HTML from learning progress JSON.")
    parser.add_argument("progress", type=Path, help="Path to learning-progress.json")
    parser.add_argument("output", type=Path, help="Path to write skill-tree.html")
    parser.add_argument("--template", type=Path, default=DEFAULT_TEMPLATE)
    args = parser.parse_args()
    render(args.progress, args.output, args.template)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
