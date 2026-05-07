# Skill Tree HTML

Use this file when generating a visible project progress page.

## Purpose

The HTML page should present:

- A project-specific capability tree.
- A game-like progression layer with level, stars, and an experience bar.
- Zero-based initial state that only grows from exercise points.
- Chapter-to-node mapping.
- Progress state.
- Compact positive feedback.

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

- Use a polished game UI aesthetic, but keep it readable and calm.
- Use colored badges or chips for `未解锁`, `进行中`, and `已解锁`.
- Use stars or XP to make progress feel tangible.
- Keep the tree hierarchical but compact.
- Avoid decorative clutter, but allow small highlights, glows, or progress accents.
- Make the page readable without external assets.

## Content Rules

- Derive all nodes from the current materials.
- Use 5 to 8 capability nodes.
- Order nodes from foundation to integration.
- Keep the same nodes across the generated package so progress can be compared.
- Use only explicit exercise point metadata as the source for XP and unlock progress.
- Update node states and progress values whenever the learner's latest answers or chapter results change.
- Start from 0 XP, 0 stars, and all nodes locked unless exercise points have already been awarded.

## Suggested Data Model

- `project_name`
- `source_summary`
- `nodes`
- `chapter_map`
- `positive_feedback`
- `next_step`

## Output Note

The HTML page can be generated alongside Markdown files, but it should replace the old README wrapper, not duplicate it.

## Refresh Rule

After each answer or feedback pass, re-evaluate the skill tree. If any node changes state or the learner gains XP/stars, regenerate `skill-tree.html` so the visual state stays current.
