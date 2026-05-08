---
name: learning-workflow-designer
description: >
  Create reusable learning workflows from projects, papers, codebases, notes,
  or course materials. Use when the user wants to learn a project/codebase,
  generate staged study content, review packs, practice drills, exam papers,
  exercises, answer keys, critique completed answers, or track learning progress
  with Markdown/DOCX/HTML outputs. Chinese triggers include: 我想学习这个项目,
  帮我学习这个代码库, 帮我出题, 生成练习题, 批改答案, 整理成学习包, 生成技能树,
  更新学习进度, 复习模式, 练习模式.
---

# Learning Workflow Designer

Use this skill to turn raw materials into a reusable learning workflow: staged lessons, exercises, answer keys, exams, review packs, and answer critique.

Trigger this skill when the user says they want to learn a project, learn a codebase, study a tutorial, make exercises, or build a reusable learning package.

Requests such as "make a learning summary", "generate exercises", "create a study pack", or "整理学习总结和习题" should be treated as file-generation tasks by default.

## Default Behavior

Unless the user specifies otherwise, use:

- Mode: learning mode.
- Density: lightweight.
- Chapters: 10.
- Outputs: learning content, exercise paper, reference answers, skill tree HTML.
- Format: Markdown first; DOCX only when requested.
- Language: follow the user's language or source material.
- Output directory: if the user does not specify a destination, create a `tutorial/` folder and put all generated files there.
- File writing: by default, write the generated package to files. Do not only print the full learning package in chat unless the user explicitly asks for inline output.

For large codebases or broad source sets, generate the chapter map and the first chapter sample first, then continue with the full package after the user confirms the direction.

Lightweight mode means each chapter has a clear main line, no logic jumps, and at most 3 exercises. In lightweight mode, a single exercise may contain multiple sub-questions if that is the best way to cover related knowledge without increasing chapter length. Detailed mode means fuller explanations and exactly 5 exercises per chapter.
The exercise set should not feel repetitive: vary stem shapes, mix prompt types, and prefer at least one multi-part or scenario-based exercise per chapter when the material supports it.

## Workflow

1. Inspect the source materials before generating content. Prefer real files, code, schemas, diagrams, and configs over assumptions.
2. Build a global map: modules, concepts, data flow, dependencies, and learning prerequisites.
3. Derive a project-specific learning tree from the materials. Do not reuse a fixed generic skill tree; extract the capabilities from the current project, paper, or course.
4. Choose the requested mode and density. If unspecified, use learning + lightweight.
5. Split content into chapters. Default to 10 chapters, but merge or split only when the source material clearly requires it.
6. For each chapter, write one main-line sentence, then the lesson content, then exercises.
   In lightweight mode, prefer compact multi-part exercises when they improve coverage: for example, one code block followed by several small questions, or one ordered sequence followed by explanation prompts.
   Avoid making every question a single-sentence "what is / why is / list" prompt.
7. Generate a separate reference-answer document. Do not mix answers into the exercise document.
8. When grading completed answers, output critique plus positive feedback: chapter gain, skill-tree update, and next-step task.
9. If no output directory was specified, create `tutorial/` before writing files. Write `learning-content.md`, `exercises.md`, `reference-answers.md`, `learning-progress.json`, and `skill-tree.html` into that folder.
10. Create or update `learning-progress.json` as the state source for the skill tree. Track exercise IDs, total points, earned points, capability node states, chapter mapping, and feedback.
11. Render the project-specific skill tree as a static HTML page when the user wants a visible progress artifact. Prefer `scripts/render_skill_tree.py tutorial/learning-progress.json tutorial/skill-tree.html` when using the default output folder; the page should feel like a game UI, with level, stars, and an experience bar.
12. The skill tree must be driven only by explicit point values in the exercise document and `learning-progress.json`. Do not infer progress from vague understanding; if a question or task has no declared points, it does not contribute to XP.
13. After every answer, critique, or learning-step response, check whether `learning-progress.json` should advance and refresh the HTML if any node or progress value changed.
14. Do not invent a README wrapper for the learning package unless the user explicitly asks for one.
15. Run the quality checks from `references/quality-checks.md` before finishing.
16. If DOCX output is requested, create Markdown first, then use `scripts/md_to_docx.py` or equivalent DOCX tooling.
17. Final chat response should be a short summary with links or paths to generated files, not the full content of every generated document.

## Mode References

Read only the references needed for the user's request:

- `references/modes.md`: learning, review, exam modes and lightweight/detailed density.
- `references/question-types.md`: available question types and when to use them.
- `references/output-formats.md`: Markdown and DOCX requirements, including red DOCX critique annotations.
- `references/feedback.md`: project-specific capability tree and positive-feedback rules.
- `references/skill-tree-html.md`: HTML skill-tree layout and styling rules.
- `references/skill-tree-skins.md`: engineering, course, and paper visual styles for skill-tree pages.
- `references/visual-inspirations.md`: GitHub references for more game-like skill tree presentation.
- `references/quality-checks.md`: anti-repetition, continuity, answer separation, and critique rules.

## Output Rules

Default output is file-based. Unless the user explicitly asks for inline-only content, create the output directory and write the artifacts to disk.

For learning mode, produce these artifacts by default:

If the user does not specify an output directory, create `tutorial/` and produce:

1. `tutorial/learning-content.md`
2. `tutorial/exercises.md`
3. `tutorial/reference-answers.md`
4. `tutorial/learning-progress.json`
5. `tutorial/skill-tree.html`

For review mode, write a review outline, weak-point checklist, and short reinforcement exercises to `tutorial/review-pack.md` unless another destination is specified.

For practice mode, write an exercise-first practice set with explicit points to `tutorial/practice.md`, and write separate answers/rubric to `tutorial/practice-answers.md` unless another destination is specified.

For exam mode, write an independent paper to `tutorial/exam.md`, scoring rubric to `tutorial/rubric.md`, and separate answers to `tutorial/exam-answers.md` unless another destination is specified.

## Critique Rules

When checking completed answers:

- Judge each answer as correct, partially correct, or incorrect.
- Distinguish "right direction but weak expression" from "conceptually wrong".
- Add actionable comments near the answer.
- Markdown comments use blockquote paragraphs beginning with `批注：`.
- DOCX comments use red text paragraphs beginning with `批注：`; do not require native Word comments.

## Positive Feedback

After critique, always emit a compact feedback block. The block should be derived from the current project, not from a fixed universal skill taxonomy.

Include:

- What the learner now clearly understands.
- Which project-specific capability nodes advanced.
- Which node remains weak or partially unlocked.
- One next-step task that is small and concrete.

When a visual progress artifact is useful, update `learning-progress.json` and render the same feedback block into `skill-tree.html` instead of wrapping it in a README.

The skill tree is stateful across the conversation or project package: if the learner answers more questions or gains new understanding, update `learning-progress.json` first, then regenerate the HTML so the level, stars, XP, and unlocked nodes reflect the latest state.
The starting state is zero progress. The tree begins at 0 XP, 0 stars, and unlocked nodes only appear after the learner earns the matching points from exercises.

## Progress State

Use `learning-progress.json` as the single source of truth for visual progress. Start from `assets/learning-progress-template.json` when creating a new learning package.

Required fields:

- `project_name`, `source_summary`, `mode`, and `density`.
- `total_xp`, `earned_xp`, `level`, and `stars`.
- `total_levels`: default to 5. Level thresholds are derived from total XP unless `level_thresholds` is explicitly provided.
- `nodes`: project-specific capability nodes or chapter task nodes with `id`, `name`, `state`, `earned_points`, `total_points`, and `chapters`. For a chapter task tree, keep one visible node per chapter.
- `exercises`: each scored exercise with `id`, `chapter`, `node_id`, `points`, and `earned_points`.
- `chapter_map`, `positive_feedback`, and `next_step`.

Allowed node states are `locked`, `active`, and `unlocked`. Progress updates must change `earned_points` only when the learner earns explicit exercise points.

Default level rule: there are 5 levels. Split the package's `total_xp` into 5 thresholds: Lv.1 at 0%, Lv.2 at 25%, Lv.3 at 50%, Lv.4 at 75%, and Lv.5 at 100%. The exercise point total must equal `total_xp`, so completing every scored exercise fills the XP bar and reaches Lv.5.

Render with:

```powershell
python scripts/render_skill_tree.py learning-progress.json skill-tree.html
```

Use the default skin unless the project type is obvious or the user asks for a style. Available skins are `engineering`, `course`, and `paper`; see `references/skill-tree-skins.md`.

```powershell
python scripts/render_skill_tree.py learning-progress.json skill-tree.html --skin engineering
```

## DOCX Conversion

Use `scripts/md_to_docx.py` for basic DOCX conversion when `python-docx` is available. The script preserves headings, tables, code blocks, answer lines, and converts Markdown critique comments into red DOCX paragraphs.

If the script cannot run, still produce clean Markdown and explain that DOCX conversion requires `python-docx`.
