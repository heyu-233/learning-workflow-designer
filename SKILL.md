---
name: learning-workflow-designer
description: >
  Create project-driven learning packages from projects, papers, codebases,
  notes, or course materials. Use when the user wants to learn a project/codebase,
  audit source materials, generate staged study content, review packs, practice
  drills, exam papers, guided lab exercises, answer keys, critique completed
  answers, or track learning progress with Markdown/DOCX/HTML outputs. Use
  project-lab mode when the user wants to complete a concrete project step by
  step through guided exercises, capstone-driven learning, project-driven labs,
  or build-as-you-learn practice. Chinese triggers include: 我想学习这个项目,
  帮我学习这个代码库, 帮我出题, 生成练习题, 批改答案, 整理成学习包, 生成技能树,
  更新学习进度, 复习模式, 练习模式, 项目实验模式, 项目驱动学习, 边学边做项目,
  通过练习完成项目, 以小项目为主线, 一步一步完成项目, 材料审计, 输入材料检查.
---

# Learning Workflow Designer

Turn raw materials into reusable project-driven learning packages: staged lessons, guided exercises, answer keys, review packs, exams, feedback, and progress tracking.

This is a Codex-first skill, not a general workflow engine. Keep the core learning-package format platform-neutral so the same package can later be used in ChatGPT, Claude, Obsidian, VS Code, a CLI, or plain Markdown.

## Defaults

Unless the user specifies otherwise:

- Use learning mode + lightweight density + 10 chapters.
- Use project-lab mode instead when the user names a final project and wants exercises to guide project completion step by step.
- Write files to disk. If no destination is given, create `tutorial/`.
- Produce Markdown first: `learning-content.md`, `exercises.md`, `reference-answers.md`, `learning-progress.json`, and `skill-tree.html`.
- Run source intake before full generation unless the user only asks for a quick brainstorm or a narrow edit.
- Follow the user's language or the source language.
- For broad codebases or large source sets, generate a 10-chapter map and first-chapter sample before the full package.
- Do not print the full package in chat unless the user explicitly asks for inline output.
- Do not wrap the package in a README unless the user asks for one.
- For Chinese content, avoid PowerShell/CMD inline script strings; use `apply_patch`, existing scripts, or UTF-8 source files, then validate encoding.

## Workflow

1. Inspect source materials before generating content. Prefer real files, code, schemas, diagrams, configs, logs, and commands over assumptions.
2. Run source intake. Score material readiness, list missing inputs, and decide whether to generate a full package or a provisional package with clear `待确认` markers.
3. If critical material is missing, output a missing-information checklist first. Continue only with a provisional package when it is still useful and clearly marked as provisional.
4. Build a project-specific map: modules, concepts, data/control flow, dependencies, prerequisites, and likely failure points.
5. Choose the requested mode and density; default to learning + lightweight.
6. Split into chapters. Default to 10 chapters. Do not reduce the chapter count just because project-lab mode uses fewer project milestones.
7. For each chapter, write one main-line sentence, lesson content, and exercises.
8. Keep exercises varied. Lightweight mode uses at most 3 exercises per chapter; detailed mode uses exactly 5.
9. Keep answers separate from exercises.
10. Every exercise, practice set, exam, and project-lab task must include visible learner answer space in the question document.
11. For project-lab mode, first extract the final project acceptance target, then design exercises backward from project milestones. Milestones are a project thread, not a replacement for the default 10 chapters.
12. For engineering projects, make exercises task-based by default: record template, chapter quick table, recommended commands, stage acceptance, and one small final task.
13. Create or update `learning-progress.json` as the single source of truth for XP, stars, levels, nodes, exercises, and feedback.
14. Render `skill-tree.html` from `learning-progress.json` when producing or updating a learning package.
15. Award progress only from explicit exercise points. Do not infer XP from vague confidence.
16. When grading completed answers, output critique, positive feedback, and the next smallest task; update progress JSON and regenerate HTML when XP or node states change.
17. Run the quality checks in `references/quality-checks.md` before finishing.
18. Run `python scripts/validate_text_encoding.py <output-dir>` after generating Chinese Markdown/JSON/HTML.
19. Keep the final chat response short: summarize generated files and what changed.

## Reference Loading

Read only the references needed for the request:

- `references/modes.md`: learning, review, practice, exam modes and density rules.
- `references/source-intake.md`: material audit, readiness scoring, missing-information handling, and provisional package rules.
- `references/project-lab.md`: project-lab mode for capstone-driven, step-by-step project completion through exercises.
- `references/question-types.md`: exercise shapes and reusable templates.
- `references/engineering-practice.md`: hands-on engineering exercise packs.
- `references/output-formats.md`: Markdown, DOCX, and HTML output rules.
- `references/feedback.md`: critique, positive feedback, and progress update rules.
- `references/skill-tree-html.md`: progress JSON model and HTML skill-tree requirements.
- `references/skill-tree-skins.md`: engineering, course, and paper visual skins.
- `references/level-title-sets.md`: five-level gamified title sets.
- `references/quality-checks.md`: continuity, exercise, engineering, answer-separation, and encoding checks.
- `references/visual-inspirations.md`: optional visual inspiration only when designing richer skill trees.

## Output Modes

- Learning mode: write `learning-content.md`, `exercises.md`, `reference-answers.md`, `learning-progress.json`, and `skill-tree.html`.
- Project-lab mode: write a project-oriented package where `exercises.md` is a milestone build guide, not a quiz sheet.
- Review mode: write `review-pack.md` with outline, weak-point checklist, and reinforcement exercises.
- Practice mode: write `practice.md` plus `practice-answers.md`; keep explanations brief before the learner answers.
- Exam mode: write `exam.md`, `rubric.md`, and `exam-answers.md`; preserve assessment integrity.
- DOCX: create Markdown first, then use `scripts/md_to_docx.py` when requested.

Question documents must leave answer space directly after each prompt. Use blank lines, answer tables, or structured record blocks depending on the task type.

## Progress State

Start from `assets/learning-progress-template.json` when helpful. Required fields:

- `project_name`, `source_summary`, `mode`, `density`
- optional `material_readiness` with score, confirmed inputs, missing inputs, and provisional flag
- `total_xp`, `earned_xp`, `level`, `stars`, `total_levels`
- optional `level_thresholds`
- optional `level_title_set` or custom `level_titles`
- `nodes` with `id`, `name`, `state`, `earned_points`, `total_points`, and `chapters`
- `exercises` with `id`, `chapter`, `node_id`, `points`, and `earned_points`
- `chapter_map`, `positive_feedback`, and `next_step`

Allowed node states are `locked`, `active`, and `unlocked`. Default level rule: 5 levels at 0%, 25%, 50%, 75%, and 100% of `total_xp`; exercise point totals must equal `total_xp`.

Render with:

```powershell
python scripts/render_skill_tree.py learning-progress.json skill-tree.html
python scripts/render_skill_tree.py learning-progress.json skill-tree.html --skin engineering
```

## Critique And Feedback

When checking completed answers:

- Mark each answer as correct, partially correct, or incorrect.
- Distinguish wording weakness from concept errors.
- Keep critique actionable and close to the learner's answer.
- Markdown critique comments begin with `批注：`.
- DOCX critique comments are red paragraphs beginning with `批注：`.

After critique, include a compact positive-feedback block:

- `本章获得`
- `技能树进度`
- `下一步最小任务`

The feedback must come from the current project and explicit exercise evidence, not from a universal capability tree.

## DOCX Conversion

Use `scripts/md_to_docx.py` when `python-docx` is available. If conversion fails, keep clean Markdown and explain that DOCX conversion requires `python-docx`.
