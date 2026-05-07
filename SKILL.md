---
name: learning-workflow-designer
description: Create reusable learning workflows from projects, papers, codebases, notes, or course materials. Use when the user wants to learn a project, generate staged study content, review packs, exam papers, exercises, answer keys, or critique completed answers with Markdown/DOCX annotations.
---

# Learning Workflow Designer

Use this skill to turn raw materials into a reusable learning workflow: staged lessons, exercises, answer keys, exams, review packs, and answer critique.

Trigger this skill when the user says they want to learn a project, learn a codebase, study a tutorial, make exercises, or build a reusable learning package.

## Default Behavior

Unless the user specifies otherwise, use:

- Mode: learning mode.
- Density: lightweight.
- Chapters: 10.
- Outputs: learning content, exercise paper, reference answers, skill tree HTML.
- Format: Markdown first; DOCX only when requested.
- Language: follow the user's language or source material.

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
9. Render the project-specific skill tree as a static HTML page when the user wants a visible progress artifact. The page should feel like a game UI, with level, stars, and an experience bar.
10. The skill tree must be driven only by explicit point values in the exercise document. Do not infer progress from vague understanding; if a question or task has no declared points, it does not contribute to XP.
11. After every answer, critique, or learning-step response, check whether the skill tree state should advance and refresh the HTML if any node or progress value changed.
12. Do not invent a README wrapper for the learning package unless the user explicitly asks for one.
13. Run the quality checks from `references/quality-checks.md` before finishing.
14. If DOCX output is requested, create Markdown first, then use `scripts/md_to_docx.py` or equivalent DOCX tooling.

## Mode References

Read only the references needed for the user's request:

- `references/modes.md`: learning, review, exam modes and lightweight/detailed density.
- `references/question-types.md`: available question types and when to use them.
- `references/output-formats.md`: Markdown and DOCX requirements, including red DOCX critique annotations.
- `references/feedback.md`: project-specific capability tree and positive-feedback rules.
- `references/skill-tree-html.md`: HTML skill-tree layout and styling rules.
- `references/visual-inspirations.md`: GitHub references for more game-like skill tree presentation.
- `references/quality-checks.md`: anti-repetition, continuity, answer separation, and critique rules.

## Output Rules

For learning mode, produce these artifacts by default:

1. Learning content document.
2. Exercise document with answer space.
3. Reference-answer document.
4. Project skill tree page as part of the default learning package.

For review mode, produce a review outline, weak-point checklist, and short reinforcement exercises.

For exam mode, produce an independent paper, scoring rubric, and separate answers.

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

When a visual progress artifact is useful, render the same feedback block into `skill-tree.html` instead of wrapping it in a README.

The skill tree is stateful across the conversation or project package: if the learner answers more questions or gains new understanding, update the HTML so the level, stars, XP, and unlocked nodes reflect the latest state.
The starting state is zero progress. The tree begins at 0 XP, 0 stars, and unlocked nodes only appear after the learner earns the matching points from exercises.

## DOCX Conversion

Use `scripts/md_to_docx.py` for basic DOCX conversion when `python-docx` is available. The script preserves headings, tables, code blocks, answer lines, and converts Markdown critique comments into red DOCX paragraphs.

If the script cannot run, still produce clean Markdown and explain that DOCX conversion requires `python-docx`.
