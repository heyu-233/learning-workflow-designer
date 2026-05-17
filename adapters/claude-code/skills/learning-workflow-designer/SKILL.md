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
- Use scope-first and reuse-first behavior for existing packages. Do not full-regenerate unless source materials, project goal, mode, chapter count, or acceptance target changed.
- Treat later environment details, source code, logs, screenshots, run commands, board info, or rubric as supplemental material to merge into the existing package, not as a reason to restart.
- Run source intake before full generation.
- On the first package-generation turn, if critical blocking inputs are missing, pause and ask one compact missing-input question before writing tutorial files. Do not ask for low-level parameters that can be discovered from source code, commands, device tree, config files, logs, or learner-guided exercises.
- Write learner-facing content in plain teacher language. Every task must say what to do, how to do it, why it matters when useful, what counts as done, and where to write the answer.
- Keep answers separate from learner-facing exercises.
- Every learner-facing exercise must include visible answer space directly after the prompt.
- Mark unknown files, commands, APIs, hardware behavior, logs, ports, pins, addresses, and protocol fields as `待确认`.

## Workflow

1. Decide scope first. If a package exists, inspect existing package files before raw source materials.
2. Reuse source intake, chapter map, exercise IDs, point totals, progress JSON, and level title set unless the source materials, project goal, mode, chapter count, or acceptance target changed.
3. If the user provides later supplemental material, match it to existing `待确认` items, update the material audit, and patch only affected chapters, exercises, acceptance criteria, and reference checklists.
4. Inspect raw source materials only for new packages, changed materials, supplemental material, or missing facts.
5. Run source intake for full generation, changed source materials, or supplements that resolve missing facts; skip it for wording fixes, answer-space fixes, exercise rewrites within the same chapter map, critique, or progress-only updates.
6. If readiness is below 5/10 on the first package-generation turn, stop before generating package files and ask once for the smallest blocking input set, usually source path or URL plus the target environment/toolchain when hands-on work is expected.
7. Separate missing inputs into `blocking`, `discoverable`, and `learner-guided`. Ask the user only for blocking inputs. Inspect discoverable facts from source/configs/docs/logs. Turn learner-guided facts into exercises that teach the user how to check or configure them.
8. Do not ask repeated follow-up questions for completeness. After the one intake question, continue only when the user provides enough material or explicitly asks for a provisional package.
9. If still generating with incomplete information, mark the package as provisional and use `待确认` for unknown facts.
10. Build or reuse a project-specific concept and artifact map.
11. Split into 10 chapters unless the user explicitly changes the count.
12. For project-lab mode, extract or reuse the final acceptance target, then map 4 to 8 project milestones across the 10 chapters.
13. Write exercises that sound like a teacher wrote them for a student. Avoid abstract task names like "建立环境基线"; write concrete actions like "确认板子能联网、能登录、能运行基本命令".
14. Include what to do, how to do it, why it matters when useful, completion criteria, failure diagnosis, submitted evidence, XP, and answer space.
15. For project-lab or hands-on lab tasks, do not generate full worked answers by default. Use lightweight mentor checklists unless the user asks for a teacher edition.
16. Create or update `learning-progress.json`; XP must come only from explicit exercise points and submitted evidence.
17. Regenerate `skill-tree.html` only when progress JSON, XP, node states, level titles, or point mappings changed.
18. Run only quality checks relevant to changed files unless producing a full package.

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
- 0-4: On the first package-generation turn, stop and ask one missing-input question before writing package files; later generate only a material preparation checklist or a clearly marked provisional package if the user asks for one.

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
- Plain wording: the learner should know what to do, how to do it, why it matters when useful, and what counts as done.
- Engineering tasks should include command/operation, observation, log or screenshot path, conclusion, and questions.
- Project-lab tasks should include modified files, implementation notes, trace record, run command, observation, diagnosis, submitted evidence, and learner questions.

`reference-answers.md`:

- Expected answer or implementation shape.
- Expected commands, logs, observations, or evidence.
- Common mistakes and diagnostic order.
- Minimum acceptable evidence.
- For project-lab and hands-on lab tasks, use lightweight checklists by default and avoid full worked solutions unless requested.

`learning-progress.json`:

- Include project name, source summary, mode, density, material readiness, XP, level, nodes, exercises, chapter map, positive feedback, and next step.
- Use 5 levels by default: 0%, 25%, 50%, 75%, 100%.
- Node states are `locked`, `active`, and `unlocked`.

## Project-Lab Rules

Project-lab mode is a build guide, not a quiz sheet.

Each main task must include:

```md
这一步要做什么：
怎么做：
1. 先看/先查：
2. 再修改/新建：
3. 然后运行/观察：
为什么这样做：
做到什么算完成：
如果失败，先查：
XP：
填写区：
- 我看了哪些文件/命令：
- 我改了什么：
- 我运行了什么：
- 我看到了什么现象：
- 我判断是否完成的依据：
- 我的具体卡点：写清楚卡在哪个概念/文件/现象，以及已经尝试过什么
```

Bad title: `建立板端环境基线`.

Good title: `确认板子能联网、能登录、能运行基本命令`.

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
