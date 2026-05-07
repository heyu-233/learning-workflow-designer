# Feedback And Skill Trees

Use this layer after learning content or answer critique. Do not predefine a fixed universal capability tree. Derive the tree from the current material.

## Build The Tree

1. Read the material and the generated chapter plan.
2. Extract 5 to 8 capability nodes from repeated concepts, prerequisites, and integration points.
3. Name nodes with project language, not generic placeholders.
4. Organize them from foundation to module-level to integration/debugging.
5. Reuse the same tree throughout the document set so progress can be compared chapter by chapter.

### Example Shapes

Project-specific trees may look like:

- FreeRTOS: task scheduling, synchronization, queues, interrupts, memory, peripherals, debugging.
- Web/IoT: routing, API calls, media playback, backend services, device control, streaming, troubleshooting.
- Paper study: problem framing, method, experiments, analysis, writing, defense.

## Update Rules

For each chapter or feedback pass:

- Mark nodes as `未解锁`, `进行中`, or `已解锁`.
- If the learner shows clear understanding of a prerequisite, move that node forward.
- If the learner confuses two linked concepts, keep both visible in the tree and mark the weak node.
- Do not invent a node that is not supported by the current material.

## Positive Feedback Block

After critique, always output a compact block with:

1. `本章获得`
2. `技能树进度`
3. `下一步最小任务`

Optional extras:

- `能力条`
- `进步证据`
- `待复习点`

Keep it short. The goal is visible progress, not a second essay.

## Markdown Format

Use a compact section like:

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
- If critique is included, keep the critique in red text paragraphs.
- Do not use graphical radar charts in the first version.
