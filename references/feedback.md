# Feedback And Skill Trees

Use this layer after learning content or answer critique. Do not predefine a fixed universal capability tree. Derive the tree from the current material.

## Build The Tree

1. Read the material and the generated chapter plan.
2. Choose the visible node model:
   - Capability tree: extract 5 to 8 capability nodes from repeated concepts, prerequisites, and integration points.
   - Chapter task tree: create one visible node per chapter so the node count matches the chapter count.
3. Name nodes with project language, not generic placeholders.
4. Organize them from foundation to module-level to integration/debugging, or from chapter 1 to the final chapter for a chapter task tree.
5. Reuse the same tree throughout the document set so progress can be compared chapter by chapter.

## Example Shapes

- FreeRTOS: task scheduling, synchronization, queues, interrupts, memory, peripherals, debugging.
- Web/IoT: routing, API calls, media playback, backend services, device control, streaming, troubleshooting.
- Paper study: problem framing, method, experiments, analysis, writing, defense.

## Update Rules

- Mark nodes as `未解锁`, `进行中`, or `已解锁` in user-facing text; keep JSON states as `locked`, `active`, or `unlocked`.
- If the learner shows clear understanding of a prerequisite, move that node forward.
- If the learner confuses two linked concepts, keep both visible in the tree and mark the weak node.
- Do not invent a node that is not supported by the current material.
- Award XP only for explicit exercise points and submitted evidence.
- After grading a chapter, compare earned chapter points with that chapter's total points.
- If earned points are less than one third of the chapter total, do not advance to the next chapter. Tell the learner that continuing now is not suitable, name the weakest 1-2 concepts or missing evidence types, and add two remedial exercises targeted at those gaps.
- Remedial exercises should keep their own small point values or be marked as repair tasks, and should not unlock the next chapter until the learner submits concrete evidence.

## Positive Feedback Block

After critique, output a compact block with:

1. `本章获得`
2. `技能树进度`
3. `下一步最小任务`

Optional extras:

- `能力树`
- `进步证据`
- `待复习点`

Keep it short. The goal is visible progress, not a second essay.

## Markdown Format

```md
## 本章正反馈

本章获得：
- ...

技能树进度：
- ...

下一步最小任务：
- ...
```

## DOCX Format

- Use the same sections as Markdown.
- Keep the tree textual or table-based.
- If critique is included, keep critique in red text paragraphs.
- Do not use graphical radar charts in the first version.
