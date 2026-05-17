# Project-Lab Mode

Use project-lab mode when the user wants to learn foundations while step by step completing a concrete project. Typical triggers include:

- "complete this project through exercises"
- "project-lab mode"
- "capstone-driven learning"
- "project-driven labs"
- "build this project while learning"
- "通过练习完成项目"
- "边学边做项目"
- "以小项目为主线"
- "一步一步完成项目"
- "项目实验模式"
- "项目驱动学习"

Project-lab mode is not a quiz sheet and not a generic learning outline. The exercise document is the build path.

Before designing the build path, run source intake. If the final demo, source files, toolchain, board, simulator, build commands, or acceptance criteria are missing, put those gaps in the package and make the first tasks collect or verify them.

The build path must be written for a learner. Do not write task titles as abstract engineering labels. Say what the learner will actually do.

Bad:

- 建立板端环境基线
- 打通用户态到驱动态链路
- 完成 SPI 子系统能力闭环

Good:

- 确认板子能联网、能登录、能运行基本命令
- 从用户程序调用 `open/read/write` 开始，找到驱动里被调用的函数
- 写一个最小 SPI 读写测试，并记录读写结果

## Chapters Vs Milestones

Do not confuse chapters with project milestones.

- Chapters are the learning structure. Default to 10 chapters unless the user explicitly asks for another chapter count.
- Milestones are the project build thread. Use 4 to 8 project milestones and map them across the chapters.
- A milestone may span multiple chapters, and a chapter may contain part of a milestone.
- Do not reduce a default 10-chapter package to 4 to 8 chapters just because there are 4 to 8 milestones.
- If the user explicitly asks to organize by milestones instead of chapters, then milestone count may become the visible section count.

## Core Rule

Start from the final project acceptance target, then design the learning path backward.

Each chapter must connect three things:

1. Foundation to learn.
2. Source code or system behavior to inspect.
3. Project artifact to implement or verify.

If an exercise does not move the learner closer to the final project, rewrite it or move it to optional review.

## Required Package Shape

For project-lab mode, produce:

1. `learning-content.md`: concepts and source-reading guide, written only as much as needed for the lab.
2. `exercises.md`: milestone build guide with explicit implementation tasks.
3. `reference-answers.md`: optional for hands-on tasks. Prefer lightweight mentor checklists with expected evidence, acceptance criteria, common failures, and diagnostic order. Do not write full worked solutions unless the user asks for a teacher edition.
4. `learning-progress.json`: XP tied to project milestones and evidence.
5. `skill-tree.html`: progress page.

## Exercise Document Shape

`exercises.md` should include:

1. Final project target and acceptance checklist.
2. Required hardware/software/source assumptions and "待确认" items.
3. A 10-chapter map plus a milestone map from empty project to final demo.
4. Chapter tasks. Each task should include:
   - What to do: one plain sentence.
   - How to do it: concrete steps the learner can follow.
   - Why it matters for the final project when the reason is not obvious.
   - First read/check: concrete source files, functions, docs, logs, or commands.
   - Then implement/change: concrete file, function, module, protocol frame, test, or config to create.
   - Then run/observe: command, debug action, serial output, log, device behavior, or screenshot to collect.
   - What counts as done.
   - If it fails: shortest diagnostic path.
   - Submit evidence.
   - Learner answer space.
   - XP.
5. Stage acceptance groups.
6. Final demo script.

## Milestone Design

Use 4 to 8 project milestones, mapped across the default 10 chapters. Each milestone should produce a visible artifact, such as:

- A compiling skeleton.
- A running hello/demo task.
- A protocol parser test.
- A device or boot log.
- A working module.
- An integration demo.
- A failure-handling or rollback test.

Avoid milestones that only say "understand X".

## Exercise Granularity

Prefer many small build steps over a few broad prompts when the project is unfamiliar.

Good project-lab exercise verbs:

- create
- port
- trace
- instrument
- implement
- compile
- flash
- run
- observe
- compare
- diagnose
- submit evidence

Use these verbs in full sentences. For example, write "运行 `uname -a`，把输出复制到答题区，并用一句话说明它证明了什么" instead of "验证内核版本".

Avoid making the main exercises mostly:

- define
- summarize
- list advantages
- explain from memory

Conceptual questions are allowed only when they unlock an implementation step.

## Source Study Coupling

When source-code study is part of the project, pair it with implementation:

- "Trace this function" must lead to "use the same pattern in this project function."
- "Read this structure" must lead to "design or inspect this project structure."
- "Debug this flow" must lead to "verify this project flow."

For a "function-by-function porting" request, every copied or rewritten function should include:

- Original source location.
- Minimal dependencies.
- Inputs and outputs.
- Global state touched.
- Test harness or observation.
- What project feature it enables.

## Scoring

Award XP only for submitted evidence:

- Code file or patch.
- Build output.
- Serial/log output.
- Debug trace.
- Screenshot description.
- Test result.
- Written conclusion tied to an observed result.

Do not award XP for "I read it" unless the learner provides a trace note or source-reading artifact.

## Learner Answer Space

Every project-lab task must include a fillable record block. Use this shape unless a more specific task format is better:

```md
这一步要做什么：

怎么做：
1. 先看/先查：
2. 再修改/新建：
3. 然后运行/观察：

为什么这样做：

做到什么算完成：

如果失败，先查：

填写区：

- 我看了哪些文件/命令：
- 我改了什么：
- 我运行了什么：
- 我看到了什么现象：
- 我判断是否完成的依据：
- 我的具体卡点：写清楚卡在哪个概念/文件/现象，以及已经尝试过什么
```

For protocol, driver, boot, or RTOS tasks, prefer structured tables where useful:

| 项目 | 我的记录 |
|---|---|
| 修改的函数/文件 |  |
| 关键参数/地址/命令 |  |
| 运行现象 |  |
| 日志或截图路径 |  |
| 结论 |  |

## Reference Answers

For project-lab and hands-on lab tasks, reference answers should act like a mentor's checklist, not a full solution manual.

Default:

- Omit full worked answers for implementation tasks.
- Provide only pass criteria, minimum evidence, common failure points, and diagnostic order.
- Keep conceptual answers only for concept questions that are scored separately.
- Do not reveal final code, full protocol implementation, full driver implementation, or complete project solution unless the user asks for a teacher edition.

Use this lightweight structure:

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

When full answers are requested, they should still act like a mentor's checklist:

- Expected implementation shape.
- Expected command/log/phenomenon.
- Common failure points.
- Diagnostic order.
- Minimum acceptable evidence.

Do not reveal a full final solution unless the user asks for teacher-edition materials.
