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
3. `reference-answers.md`: expected observations, acceptance criteria, and hints, not just conceptual answers.
4. `learning-progress.json`: XP tied to project milestones and evidence.
5. `skill-tree.html`: progress page.

## Exercise Document Shape

`exercises.md` should include:

1. Final project target and acceptance checklist.
2. Required hardware/software/source assumptions and "待确认" items.
3. Milestone map from empty project to final demo.
4. Chapter tasks. Each task should include:
   - Goal.
   - Why this matters for the final project.
   - Read/trace first: concrete source files, functions, docs, logs, or commands.
   - Implement/change: concrete file, function, module, protocol frame, test, or config to create.
   - Run/observe: command, debug action, serial output, log, device behavior, or screenshot to collect.
   - Pass criteria.
   - If it fails: shortest diagnostic path.
   - Submit evidence.
   - XP.
5. Stage acceptance groups.
6. Final demo script.

## Milestone Design

Use 4 to 8 project milestones. Each milestone should produce a visible artifact, such as:

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

## Reference Answers

Reference answers should act like a mentor's checklist:

- Expected implementation shape.
- Expected command/log/phenomenon.
- Common failure points.
- Diagnostic order.
- Minimum acceptable evidence.

Do not reveal a full final solution unless the user asks for teacher-edition materials.
