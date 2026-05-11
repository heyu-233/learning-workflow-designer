---
description: >
  Build project-driven learning packages from codebases, notes, assignments,
  papers, or course materials. Use when the user wants to audit source materials,
  learn a project, generate staged lessons, project-lab exercises, answer keys,
  practice packs, exams, critique completed answers, or track learning progress
  in Markdown/JSON/HTML. Chinese triggers include: 学习包, 材料审计, 项目实验模式,
  边学边做项目, 通过练习完成项目, 生成练习题, 批改答案, 更新学习进度.
---

# Learning Workflow Designer For Claude Code

Turn raw materials into platform-neutral project-driven learning packages. This is a Claude Code adapter for the Learning Workflow Designer format.

## Defaults

Unless the user specifies otherwise:

- Use learning mode + lightweight density + 10 chapters.
- Use project-lab mode when the user names a final project and wants exercises to guide project completion.
- Write files to `tutorial/` unless the user gives another directory.
- Produce Markdown first: `learning-content.md`, `exercises.md`, `reference-answers.md`, and `learning-progress.json`.
- Generate `skill-tree.html` when the repository has a rendering script or when a static HTML progress view can be produced safely.
- Run source intake before full generation.
- Keep answers separate from learner-facing exercises.
- Every learner-facing exercise must include visible answer space directly after the prompt.
- Mark unknown files, commands, APIs, hardware behavior, logs, ports, pins, addresses, and protocol fields as `待确认`.

## Workflow

1. Inspect available files and materials before generating content.
2. Run source intake and score readiness from 0 to 10.
3. If readiness is below 5/10, output a missing-information checklist before generating a full package.
4. If still generating with incomplete information, mark the package as provisional.
5. Build a project-specific concept and artifact map.
6. Split into 10 chapters unless the user explicitly changes the count.
7. For project-lab mode, extract the final acceptance target first, then map 4 to 8 project milestones across the 10 chapters.
8. Write exercises that include read/trace, implement/change, run/observe, pass criteria, failure diagnosis, submitted evidence, XP, and answer space.
9. Create or update `learning-progress.json`; XP must come only from explicit exercise points and submitted evidence.
10. Run quality checks before finishing.

## Source Intake

Score each dimension 0 to 2:

| Dimension | Check |
|---|---|
| Goal clarity | Final learning goal or project acceptance target is explicit. |
| Source accessibility | Code, docs, diagrams, logs, papers, or course files are inspectable. |
| Environment clarity | Hardware, OS, toolchain, commands, ports, devices, or runtime assumptions are known. |
| Acceptance criteria | Completion can be judged by tests, observations, deliverables, rubrics, or demos. |
| Learner constraints | Time, level, language, depth, format, and chapter count are known or safely defaultable. |

Readiness bands:

- 8-10: Generate a full learning package.
- 5-7: Generate with a `待确认` section and avoid unsupported precision.
- 0-4: Output a missing-information checklist first; generate only a clearly marked provisional package if useful.

## Output Shape

Default package:

```text
tutorial/
  learning-content.md
  exercises.md
  reference-answers.md
  learning-progress.json
  skill-tree.html
```

`learning-content.md`:

- Material audit when useful.
- Project main line.
- 10 chapters.
- Each chapter has one main-line sentence, learning content, read/trace path, and summary.

`exercises.md`:

- Learner-facing only.
- No hidden answers.
- Answer space after every prompt.
- Engineering tasks should include command/operation, observation, log or screenshot path, conclusion, and questions.
- Project-lab tasks should include modified files, implementation notes, trace record, run command, observation, diagnosis, submitted evidence, and learner questions.

`reference-answers.md`:

- Expected answer or implementation shape.
- Expected commands, logs, observations, or evidence.
- Common mistakes and diagnostic order.
- Minimum acceptable evidence.

`learning-progress.json`:

- Include project name, source summary, mode, density, material readiness, XP, level, nodes, exercises, chapter map, positive feedback, and next step.
- Use 5 levels by default: 0%, 25%, 50%, 75%, 100%.
- Node states are `locked`, `active`, and `unlocked`.

## Project-Lab Rules

Project-lab mode is a build guide, not a quiz sheet.

Each main task must include:

```md
目标：
为什么它服务于最终项目：
阅读/跟踪：
实现/修改：
运行/观察：
通过标准：
失败排查：
提交证据：
XP：
填写区：
- 修改文件：
- 实现说明：
- 阅读/跟踪记录：
- 运行命令：
- 观察现象：
- 失败排查：
- 提交证据：
- 我的问题：
```

## Continuity Rules

- Later chapters may reuse earlier concepts, tools, code, logs, and artifacts.
- Earlier chapters must not require concepts, APIs, files, protocol fields, debugging methods, or artifacts introduced only later.
- Future previews are allowed, but they cannot be required to answer current tasks.

## Feedback Rules

When critiquing learner answers:

- Mark each answer as correct, partially correct, or incorrect.
- Separate wording weakness from concept errors.
- Award XP only from explicit evidence.
- Include `本章获得`, `技能树进度`, and `下一步最小任务`.
