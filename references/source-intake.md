# Source Intake

Use source intake before generating a full learning package, especially when the user provides a broad project goal, screenshots, scattered notes, or a low-detail assignment.

## Purpose

Prevent vague or low-quality inputs from producing generic learning packages. Prefer a truthful partial package over a confident but imaginary one.

## Readiness Score

Score the input from 0 to 10 before full generation. Use this rubric:

| Dimension | Points | Check |
|---|---:|---|
| Goal clarity | 0-2 | Final learning goal or project acceptance target is explicit. |
| Source accessibility | 0-2 | Code, docs, diagrams, logs, papers, or course files are available and inspectable. |
| Environment clarity | 0-2 | Hardware, OS, toolchain, build commands, ports, devices, or runtime assumptions are known when needed. |
| Acceptance criteria | 0-2 | The output can be judged by tests, observations, deliverables, rubrics, or demos. |
| Learner constraints | 0-2 | Time, current level, language, depth, format, and chapter count are known or safely defaultable. |

Readiness bands:

- 8-10: Generate a full learning package.
- 5-7: Generate a package, but include a `待确认` section and avoid precise claims that are not source-grounded.
- 0-4: First output a missing-information checklist. Generate only a provisional package if the user still needs a starting point.

## Missing-Information Checklist

When critical material is missing, put this near the top of the response or generated package:

```md
## 材料审计

当前材料完整度：X/10

### 已确认
- ...

### 待补充
- ...

### 影响
- 如果不补充这些信息，练习题会停留在较粗粒度，无法给出准确命令、文件路径、硬件现象或验收标准。
```

Ask for at most the smallest useful set of missing items. Prefer concrete requests such as:

- source repository path or archive
- target board/model or OS/toolchain
- build/run commands
- expected final demo
- teacher rubric or screenshot text
- existing logs or failure output

## Provisional Package Rules

If generating with incomplete materials:

- Mark the package as `临时学习包` or `provisional`.
- Use `待确认` for unknown files, commands, APIs, hardware pins, addresses, or protocol fields.
- Keep chapter count defaults unless the user changes them.
- Use source-grounded tasks where possible and environment-discovery tasks where not.
- Do not invent exact module names, pins, registers, ports, commands, or acceptance logs.
- Include early exercises that collect the missing evidence.

## Project-Lab Intake

For project-lab mode, identify:

1. Final project acceptance target.
2. Demo evidence that proves completion.
3. Hardware/software/source assumptions.
4. Required submodules or drivers.
5. Safety risks or irreversible operations.
6. What can be simulated before hardware access.
7. What each milestone must produce.

If the final target is clear but the environment is unclear, make the first chapter a concrete environment check: confirm the board or project can be opened, logged into, built, run, and observed before implementation tasks.
