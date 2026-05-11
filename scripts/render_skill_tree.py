#!/usr/bin/env python3
"""Render a static skill-tree HTML page from learning-progress.json."""

from __future__ import annotations

import argparse
import hashlib
import html
import json
import re
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

SKINS = {
    "default": {
        "bg": "#111827",
        "panel": "#182033",
        "panel_strong": "#202a43",
        "text": "#f8fafc",
        "muted": "#a7b0c4",
        "border": "#334155",
        "accent": "#38bdf8",
        "accent_2": "#a78bfa",
    },
    "engineering": {
        "bg": "#07111f",
        "panel": "#101b2d",
        "panel_strong": "#13233a",
        "text": "#f8fafc",
        "muted": "#a7b0c4",
        "border": "#334155",
        "accent": "#22d3ee",
        "accent_2": "#34d399",
    },
    "course": {
        "bg": "#f5f7fb",
        "panel": "#ffffff",
        "panel_strong": "#eef4ff",
        "text": "#172033",
        "muted": "#5b6475",
        "border": "#d7dfec",
        "accent": "#2563eb",
        "accent_2": "#f59e0b",
    },
    "paper": {
        "bg": "#f8f5f0",
        "panel": "#fffdf8",
        "panel_strong": "#f1ece3",
        "text": "#211f1c",
        "muted": "#6f675e",
        "border": "#ddd4c7",
        "accent": "#6d28d9",
        "accent_2": "#b45309",
    },
}

LEVEL_TITLE_SETS = {
    "classic": ["新手", "初学者", "进阶者", "熟练者", "掌握者"],
    "sao": ["起始镇新手", "单手剑练习者", "攻略组成员", "前线独行者", "黑衣剑士"],
    "eu4": ["边陲伯国", "区域强权", "王国中坚", "列强候选", "世界霸权"],
    "hoi4": ["新兵训练营", "前线参谋", "集团军指挥官", "战区统帅", "最高统帅部"],
    "civ6": ["开拓者", "建城者", "城邦盟友", "文明领袖", "时代缔造者"],
}

SURPRISE_LEVEL_TITLE_SETS = ["sao", "eu4", "hoi4", "civ6"]

BAD_ENCODING_MARKERS = {
    "\ufffd": "replacement character",
    "\u951f": "mojibake marker",
    "\u93b5": "mojibake marker",
}

QUESTION_RUN = re.compile(r"\?{4,}")


def esc(value: Any) -> str:
    return html.escape(str(value), quote=True)


def percent(earned: int | float, total: int | float) -> int:
    if not total:
        return 0
    return max(0, min(100, round((earned / total) * 100)))


def level_thresholds(total_xp: int | float, total_levels: int = 5) -> list[int]:
    if total_levels <= 1:
        return [0]
    total = max(0, int(total_xp))
    return [round(total * index / (total_levels - 1)) for index in range(total_levels)]


def level_from_xp(earned_xp: int | float, total_xp: int | float, total_levels: int = 5) -> int:
    earned = max(0, int(earned_xp))
    thresholds = level_thresholds(total_xp, total_levels)
    level = 1
    for index, threshold in enumerate(thresholds, start=1):
        if earned >= threshold:
            level = index
    return max(1, min(total_levels, level))


def stars_from_xp(earned_xp: int | float, total_xp: int | float, total_levels: int = 5) -> int:
    earned = max(0, int(earned_xp))
    if earned <= 0:
        return 0
    thresholds = level_thresholds(total_xp, total_levels)
    return sum(1 for threshold in thresholds if earned >= threshold)


def render_stars(stars: int | float, total: int = 5) -> str:
    count = max(0, min(total, int(stars)))
    return "".join("★" if index < count else "☆" for index in range(total))


def choose_level_title_set(data: dict[str, Any], total_levels: int) -> tuple[str, list[str]]:
    custom_titles = data.get("level_titles")
    if isinstance(custom_titles, list) and len(custom_titles) >= total_levels:
        return "custom", [str(title) for title in custom_titles[:total_levels]]

    requested_set = str(data.get("level_title_set", "")).strip()
    if requested_set in LEVEL_TITLE_SETS:
        return requested_set, LEVEL_TITLE_SETS[requested_set][:total_levels]

    seed = f"{data.get('project_name', '')}|{data.get('source_summary', '')}"
    digest = hashlib.sha256(seed.encode("utf-8")).hexdigest()
    if int(digest[:8], 16) % 100 < 80:
        selected = "classic"
    else:
        selected = SURPRISE_LEVEL_TITLE_SETS[int(digest[8:16], 16) % len(SURPRISE_LEVEL_TITLE_SETS)]
    return selected, LEVEL_TITLE_SETS[selected][:total_levels]


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


def render_level_table(thresholds: list[int], earned_xp: int, level_titles: list[str]) -> str:
    rows = []
    for index, threshold in enumerate(thresholds, start=1):
        state = "已达到" if earned_xp >= threshold else "未达到"
        title = level_titles[index - 1] if index - 1 < len(level_titles) else f"Lv. {index}"
        rows.append(
            "<tr>"
            f"<td>Lv. {index}</td>"
            f"<td>{esc(title)}</td>"
            f"<td>{threshold} XP</td>"
            f"<td>{state}</td>"
            "</tr>"
        )
    return (
        "<table>"
        "<thead><tr><th>等级</th><th>称号</th><th>最低 XP</th><th>状态</th></tr></thead>"
        f"<tbody>{''.join(rows)}</tbody>"
        "</table>"
    )


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


def validate_progress(data: dict[str, Any]) -> None:
    total_xp = int(data.get("total_xp", 0))
    exercises = data.get("exercises", [])
    if exercises:
        exercise_total = sum(int(exercise.get("points", 0)) for exercise in exercises)
        if exercise_total != total_xp:
            raise ValueError(
                f"Exercise points ({exercise_total}) must equal total_xp ({total_xp}) "
                "so finishing all scored work reaches Lv.5."
            )


def validate_text_encoding(text: str, label: str) -> None:
    for marker, reason in BAD_ENCODING_MARKERS.items():
        if marker in text:
            raise ValueError(f"{label} contains {reason}; regenerate from a UTF-8-safe source.")
    if QUESTION_RUN.search(text):
        raise ValueError(f"{label} contains repeated question marks; check for Chinese encoding loss.")


def render(
    progress_path: Path,
    output_path: Path,
    template_path: Path = DEFAULT_TEMPLATE,
    skin: str = "default",
) -> None:
    data = json.loads(progress_path.read_text(encoding="utf-8"))
    validate_progress(data)
    validate_text_encoding(json.dumps(data, ensure_ascii=False), str(progress_path))
    template = Template(template_path.read_text(encoding="utf-8"))
    total_xp = int(data.get("total_xp", 0))
    earned_xp = int(data.get("earned_xp", 0))
    total_levels = int(data.get("total_levels", 5))
    thresholds = data.get("level_thresholds") or level_thresholds(total_xp, total_levels)
    current_level = level_from_xp(earned_xp, total_xp, total_levels)
    current_stars = stars_from_xp(earned_xp, total_xp, total_levels)
    level_title_set, level_titles = choose_level_title_set(data, total_levels)
    current_level_title = (
        level_titles[current_level - 1] if current_level - 1 < len(level_titles) else f"Lv. {current_level}"
    )
    feedback = data.get("positive_feedback", {})
    skin_tokens = SKINS.get(skin, SKINS["default"])

    html_text = template.safe_substitute(
        skin=esc(skin if skin in SKINS else "default"),
        skin_bg=skin_tokens["bg"],
        skin_panel=skin_tokens["panel"],
        skin_panel_strong=skin_tokens["panel_strong"],
        skin_text=skin_tokens["text"],
        skin_muted=skin_tokens["muted"],
        skin_border=skin_tokens["border"],
        skin_accent=skin_tokens["accent"],
        skin_accent_2=skin_tokens["accent_2"],
        project_name=esc(data.get("project_name", "学习技能树")),
        subtitle=esc(data.get("source_summary", "")),
        mode=esc(data.get("mode", "learning")),
        density=esc(data.get("density", "lightweight")),
        level=esc(current_level),
        level_title=esc(current_level_title),
        level_title_set=esc(level_title_set),
        total_levels=esc(total_levels),
        stars=render_stars(current_stars, total_levels),
        earned_xp=earned_xp,
        total_xp=total_xp,
        xp_percent=percent(earned_xp, total_xp),
        level_rule=esc(f"共 {total_levels} 级，达到 {total_xp} XP 即满级；当前称号组：{level_title_set}。"),
        level_table_html=render_level_table([int(value) for value in thresholds], earned_xp, level_titles),
        nodes_html=render_nodes(data.get("nodes", [])),
        chapter_table_html=render_chapter_table(data.get("chapter_map", [])),
        chapter_gain=esc(feedback.get("chapter_gain", "")),
        skill_tree_progress=esc(feedback.get("skill_tree_progress", "")),
        next_step=esc(data.get("next_step") or feedback.get("next_step", "")),
        progress_json=html.escape(json.dumps(data, ensure_ascii=False, indent=2), quote=False),
    )
    validate_text_encoding(html_text, str(output_path))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(html_text, encoding="utf-8")
    validate_text_encoding(output_path.read_text(encoding="utf-8"), str(output_path))


def main() -> int:
    parser = argparse.ArgumentParser(description="Render skill-tree HTML from learning progress JSON.")
    parser.add_argument("progress", type=Path, help="Path to learning-progress.json")
    parser.add_argument("output", type=Path, help="Path to write skill-tree.html")
    parser.add_argument("--template", type=Path, default=DEFAULT_TEMPLATE)
    parser.add_argument("--skin", choices=sorted(SKINS), default="default")
    args = parser.parse_args()
    render(args.progress, args.output, args.template, args.skin)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
