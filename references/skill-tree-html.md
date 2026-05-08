# Skill Tree HTML

Use this file when generating a visible project progress page.

## Purpose

The HTML page should present:

- A project-specific capability tree.
- A game-like progression layer with level, stars, and an experience bar.
- Zero-based initial state that only grows from exercise points.
- A state model backed by `learning-progress.json`.
- Chapter-to-node mapping.
- Progress state.
- Compact positive feedback.

Visual inspiration should come from game skill-tree and dashboard-style UI patterns:

- RPG-like node graphs with obvious locked / active / unlocked states.
- Dark panels with controlled accent colors.
- Layered cards with strong hierarchy.
- Subtle shadow, border weight, glow, and accent contrast.
- Separate XP, stars, and node progress so the tree feels like an RPG HUD, not a plain checklist.

Do not turn the page into a long report. Keep it scannable.

## Structure

Use a single static HTML file with these sections:

1. Header with project name, learning mode, level badge, stars, and experience bar.
2. Short source summary.
3. Exercise-point schema summary.
4. Capability tree cards or rows.
5. Chapter mapping table.
6. Positive feedback block.
7. Next-step task block.

## Visual Rules

- Use a polished game UI aesthetic with visible RPG flavor.
- Use a restrained dark palette with a few strong accents.
- Use subtle contrast, borders, shadows, and opacity to indicate state.
- Use colored badges or chips for `未解锁`, `进行中`, and `已解锁`.
- Use stars, XP bars, and node meters to make progress tangible.
- Make the skill tree read like a map or progression board, not a generic dashboard.
- Keep the tree hierarchical but compact.
- Avoid decorative clutter, but allow glow, accent lines, and controlled saturated highlights.
- Make the page readable without external assets.

## Content Rules

- Derive all nodes from the current materials.
- Use 5 to 8 capability nodes.
- Order nodes from foundation to integration.
- Keep the same nodes across the generated package so progress can be compared.
- Use only explicit exercise point metadata as the source for XP and unlock progress.
- Update node states and progress values whenever the learner's latest answers or chapter results change.
- Start from 0 XP, 0 stars, and all nodes locked unless exercise points have already been awarded.
- Prefer one visible progress bar per node or chapter group, plus a global XP bar in the header.
- If the project supports multiple learning lanes, show them as branches or grouped clusters rather than a single flat list.

## Suggested Data Model

Store this model in `learning-progress.json`. Start from `assets/learning-progress-template.json` for a new package.

- `project_name`
- `source_summary`
- `mode`
- `density`
- `level`
- `stars`
- `earned_xp`
- `total_xp`
- `nodes`
- `exercises`
- `chapter_map`
- `positive_feedback`
- `next_step`

Each exercise should include an ID, chapter, node ID, total points, and earned points. Each node should include an ID, name, state, total points, earned points, and chapter list.

## Output Note

The HTML page can be generated alongside Markdown files, but it should replace the old README wrapper, not duplicate it.

Render with:

```powershell
python scripts/render_skill_tree.py learning-progress.json skill-tree.html
```

Use `--skin engineering`, `--skin course`, or `--skin paper` when the visual tone should match the source type. See `references/skill-tree-skins.md`.

## Refresh Rule

After each answer or feedback pass, re-evaluate the skill tree. If any node changes state or the learner gains XP/stars, update `learning-progress.json` first, then regenerate `skill-tree.html` so the visual state stays current.

## Source Inspirations

- `beautiful-skill-tree` on GitHub: use custom theming, borders, and explicit tree navigation ideas.
- `RPG Maker MV Skill Trees System`: use the Diablo-like tree feeling, node unlocking, and branch structure.
- `rpg-companion-sillytavern`: use stats panels, progress bars, and character/status widgets as layout inspiration.
- `Tabler`: borrow the clean dashboard hierarchy, spacing discipline, and responsive panel structure.
- `skillmap`: keep the tree relationship explicit and treat the page as a map of prerequisites rather than a flat checklist.
- For a richer version, use hue sparingly and keep the accent set small.
