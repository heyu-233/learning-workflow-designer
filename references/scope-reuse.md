# Scope-First And Reuse-First

Use this reference before editing or regenerating an existing learning package. The goal is to reduce repeated work without lowering output quality.

## Core Rule

Before generating, decide the smallest useful scope. Reuse existing package structure unless the user changed the source materials, project goal, chapter count, mode, or acceptance target.

Do not restart from raw source materials when an existing package already contains enough structure to answer the request.

## Scope Decision

Classify the request:

| Request shape | Reuse | Regenerate |
|---|---|---|
| Fix wording, make exercises more readable, add answer space | Existing chapters, source intake, progress JSON | Only touched question document sections |
| Redo exercises for the same package | Chapter map, learning content, material audit, project goal | `exercises.md`; maybe a lightweight answer/checklist file |
| Redo learning content but keep project | Source intake, project goal, progress style | `learning-content.md`; adjust exercises only if dependencies changed |
| Critique answers | Existing exercises, progress JSON | Feedback and changed XP fields only |
| Update progress | Existing package | `learning-progress.json` and `skill-tree.html` only |
| New source material, new project, new chapter count, or new mode | Nothing unless still relevant | Full package |

If unclear, infer from the user's wording. Do not ask unless a wrong scope would overwrite valuable work.

## Existing Package First

When a package directory exists:

1. Read existing package files first: `learning-content.md`, `exercises.md`, `learning-progress.json`, and only then source files if needed.
2. Reuse `material_readiness`, `source_summary`, chapter map, project target, and level title set when they still match.
3. Preserve exercise IDs and point totals when possible, so progress does not become stale.
4. Do not rerun source intake unless materials changed or the existing audit is missing.
5. Do not rewrite unrelated files.

## Reference Answer Cost Control

For project-lab and hands-on engineering tasks, a full worked answer is often unnecessary and may spoil the exercise.

Default behavior:

- Conceptual, practice, and exam questions should have reference answers or rubrics.
- Project-lab and hands-on lab tasks may omit full reference answers.
- When omitting full answers, provide a mentor checklist instead: expected evidence, pass criteria, common failure points, and diagnostic order.
- Do not generate long code solutions unless the user asks for a teacher edition or solution key.

Use this lightweight structure for lab answers:

```md
### 任务 X：标题

验收标准：
- ...

最低提交证据：
- ...

常见失败点：
- ...

建议排查顺序：
1. ...
2. ...
3. ...
```

## Render And Validate Only What Changed

- Render `skill-tree.html` only when `learning-progress.json`, XP, level titles, node states, or exercise point mappings changed.
- Run encoding validation on changed Chinese Markdown/JSON/HTML files, not necessarily the whole package.
- Run full package quality checks only after full package generation or structural changes.
- For local edits to exercises, check only answer space, plain language, answer separation, and dependency direction.

## Do Not Lower Quality

Scope reduction must not remove:

- Plain-language task wording.
- Answer space.
- Answer separation.
- Source-grounded facts.
- Chapter dependency direction.
- Explicit XP mapping when progress is updated.
