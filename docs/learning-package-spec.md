# Learning Package Spec

This document defines the platform-neutral output shape of Learning Workflow Designer. Codex is the first implementation, but the package format should remain usable in ChatGPT, Claude, Obsidian, VS Code, a CLI, or any Markdown-based workflow.

## Core Idea

A learning package is a small learning product with four jobs:

1. Explain what to learn.
2. Give guided exercises with answer space.
3. Keep answers and grading criteria separate.
4. Track progress with explicit evidence and XP.

## Default Files

| File | Required | Purpose |
|---|---|---|
| `learning-content.md` | Yes | Chaptered learning path, source-reading guide, concepts, and summaries. |
| `exercises.md` | Yes | Learner-facing exercises, labs, or project tasks with answer space. |
| `reference-answers.md` | Yes | Mentor checklist, expected observations, answers, hints, and acceptance criteria. |
| `learning-progress.json` | Yes | Machine-readable state for XP, levels, nodes, exercises, and next step. |
| `skill-tree.html` | Optional but recommended | Static visual progress page rendered from `learning-progress.json`. |
| `review-pack.md` | Mode-specific | Review-mode output for weak points and short reinforcement tasks. |
| `practice.md` | Mode-specific | Practice-mode question sheet. |
| `exam.md` | Mode-specific | Exam-mode paper. |
| `rubric.md` | Mode-specific | Exam scoring rules. |

## Source Intake Block

Every substantial package should begin from a material audit. Put this block in the package or final response when input quality is uncertain:

```md
## 材料审计

当前材料完整度：X/10

### 已确认
- ...

### 待补充
- ...

### 影响
- ...
```

If the score is below 5/10, generate a missing-information checklist before generating a full package. A provisional package is acceptable only when clearly marked and useful.

## Chapter Rules

- Default to 10 chapters unless the user explicitly asks for another number.
- Each chapter has one main-line sentence.
- Later chapters may reuse earlier concepts, tools, artifacts, and code.
- Earlier chapters must not require concepts, APIs, files, protocol fields, debugging methods, or artifacts introduced only later.
- Future previews are allowed, but they cannot be required for current tasks.

## Exercise Rules

Every learner-facing exercise must include answer space directly after the prompt.

Recommended answer-space forms:

| Task type | Answer space |
|---|---|
| Concept question | `答：` plus blank lines |
| Multi-part question | table with `小问`, `我的答案`, `证据/原因` |
| Engineering task | record block with command, observation, log, conclusion, evidence path |
| Project-lab task | build record with modified files, implementation notes, run result, diagnosis, evidence |
| Exam question | enough blank lines for the expected answer length |

## Project-Lab Package

Project-lab mode is used when the learner wants to complete a concrete project while learning. The exercise document is a build guide, not a quiz sheet.

Required shape:

1. Final project target.
2. Acceptance checklist.
3. Required hardware/software/source assumptions and `待确认` items.
4. 10-chapter map.
5. 4 to 8 project milestones mapped across those chapters.
6. Chapter tasks with read/trace, implement/change, run/observe, pass criteria, failure diagnosis, submitted evidence, answer space, and XP.
7. Stage acceptance groups.
8. Final demo script.

## Progress JSON

`learning-progress.json` is the single source of truth for progress. Required fields:

```json
{
  "project_name": "项目名称",
  "source_summary": "材料来源摘要",
  "mode": "learning",
  "density": "lightweight",
  "total_levels": 5,
  "level": 1,
  "level_title_set": "classic",
  "stars": 0,
  "earned_xp": 0,
  "total_xp": 100,
  "nodes": [],
  "exercises": [],
  "chapter_map": [],
  "positive_feedback": {
    "chapter_gain": "",
    "skill_tree_progress": "",
    "next_step": ""
  },
  "next_step": ""
}
```

Rules:

- XP comes only from explicit exercise points.
- Exercise point totals must equal `total_xp`.
- Node states are `locked`, `active`, or `unlocked`.
- Default levels are 0%, 25%, 50%, 75%, and 100%.

## Compatibility Targets

| Target | How to use |
|---|---|
| Codex | Install as a skill and generate files directly. |
| ChatGPT or Claude | Use `docs/prompt-pack.md` and paste source materials. |
| Obsidian | Store Markdown files as notes; link chapters, exercises, and progress. |
| VS Code | Edit Markdown/JSON directly and preview `skill-tree.html`. |
| CLI | Future target: run intake, scaffold package files, validate package quality, render skill tree. |
