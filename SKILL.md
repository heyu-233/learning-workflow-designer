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

Turn projects, codebases, papers, notes, or courses into learning packages with lessons, exercises, answer keys, progress JSON, and optional skill-tree HTML.

## Defaults

Unless the user specifies otherwise:

- Use learning mode + lightweight density + 10 chapters.
- Use project-lab mode when the user wants to complete a concrete project step by step.
- Write files to `tutorial/`.
- Produce Markdown first: `learning-content.md`, `exercises.md`, `reference-answers.md`, `learning-progress.json`, and `skill-tree.html`.
- Reuse existing package structure, exercise IDs, point totals, progress JSON, and chapter map unless source, goal, mode, chapter count, or acceptance target changed.
- Treat later logs, code, commands, screenshots, board info, or rubrics as supplements to merge into the existing package.
- Run source intake before full generation. If first-turn blocking inputs are missing, ask one compact question and stop before writing package files.
- Ask only for blocking inputs. Discover source/config/log facts yourself; turn practical unknowns into learner-guided tasks.
- Use the user's language. Write tasks in plain teacher language: what to do, how, why when useful, what counts as done, and where to answer.
- For broad codebases or large source sets, generate a 10-chapter map and first-chapter sample before the full package.
- For Chinese content, avoid PowerShell/CMD inline script strings; use `apply_patch`, UTF-8 files, or existing scripts, then validate encoding.

## Workflow

1. Decide scope first. If a package already exists, inspect existing package files before raw source materials.
2. Run source intake for new/full packages, changed source material, or supplements that resolve missing facts.
3. If readiness is too low on the first generation turn, ask once for minimum blocking inputs such as source path/URL and target environment; do not request low-level values that can be discovered or taught.
4. Build or reuse a project-specific map: modules, concepts, data/control flow, dependencies, prerequisites, and likely failure points.
5. For large codebases, audit tokens/source shape first, scan README/build/config/entry files, then create chapter map + chapter 1 sample before bulk generation.
6. Keep 10 chapters by default. For project-lab mode, map project milestones across chapters; milestones do not replace chapters.
7. Write changed chapters only. Keep exercises varied: lightweight <= 3 per chapter; detailed = 5.
8. Keep learning content, learner exercises, and answers separate. Every learner-facing item must have answer space.
9. For engineering and project-lab tasks, prefer run/observe/trace/diagnose/record work with submitted evidence and stage acceptance.
10. Use `learning-progress.json` as the source of truth for XP, level, stars, nodes, exercises, feedback, and next step.
11. Render `skill-tree.html` only when progress JSON, XP, node states, level titles, exercise IDs, or point mappings changed.
12. Award progress only from explicit exercise points. When grading, update progress only from submitted evidence.
13. Validate changed Chinese Markdown/JSON/HTML with `python scripts/validate_text_encoding.py <path>`.
14. Keep the final chat response short: generated files, important changes, and next action.

## Reference Loading

Read only what the task needs:

- `source-intake.md`: readiness gates, missing inputs, provisional packages.
- `scope-reuse.md`: update existing packages with minimal rewrites.
- `modes.md`: learning/review/practice/exam/project-lab behavior.
- `project-lab.md`: capstone/project-driven package rules.
- `plain-language.md`, `question-types.md`, `engineering-practice.md`: exercise writing.
- `output-formats.md`, `skill-tree-html.md`, `skill-tree-skins.md`, `level-title-sets.md`: outputs and progress UI.
- `feedback.md`: grading, positive feedback, progress updates.
- `quality-checks.md`: final checks for broad/full-package edits.
- `visual-inspirations.md`: only for richer skill-tree design.

## Output Modes

- Learning: `learning-content.md`, `exercises.md`, `reference-answers.md`, `learning-progress.json`, `skill-tree.html`.
- Project-lab: milestone build guide in `exercises.md`; use mentor checklists for hands-on answers unless teacher edition is requested.
- Review: `review-pack.md`.
- Practice: `practice.md` and `practice-answers.md`.
- Exam: `exam.md`, `rubric.md`, `exam-answers.md`.
- DOCX: create Markdown first; convert with `scripts/md_to_docx.py` when requested.

Question documents must leave answer space directly after each prompt using blank lines, tables, or record blocks. Avoid abstract task names; write concrete learner actions.

## Progress State

Start from `assets/learning-progress-template.json` when useful. Required state includes project/source/mode/density, readiness when applicable, XP/level/stars, nodes, exercises, chapter map, feedback, and next step.

Allowed node states: `locked`, `active`, `unlocked`. Default levels: 5 levels at 0%, 25%, 50%, 75%, 100% of `total_xp`. Exercise point totals must equal `total_xp`.

Render with:

```powershell
python scripts/render_skill_tree.py learning-progress.json skill-tree.html
python scripts/render_skill_tree.py learning-progress.json skill-tree.html --skin engineering
```

## Critique And Feedback

When checking completed answers:

- Mark each answer as correct, partially correct, or incorrect.
- Separate wording weakness from concept errors.
- Keep critique actionable and close to the answer.
- Include positive feedback and the next smallest task.
- Base XP and progress on explicit evidence, not confidence.

## DOCX Conversion

Use `scripts/md_to_docx.py` when `python-docx` is available. If conversion fails, keep clean Markdown and explain that DOCX conversion requires `python-docx`.
