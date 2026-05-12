# Source Intake

Use source intake before generating a full learning package, especially when the user provides a broad project goal, screenshots, scattered notes, or a low-detail assignment.

If source intake was already done and the user later provides missing material, update the existing audit instead of treating the request as a fresh package.

## Purpose

Prevent vague or low-quality inputs from producing generic learning packages. Prefer a truthful partial package over a confident but imaginary one.

## Initial Readiness Gate

On the first turn of a new package-generation request, do not continue into tutorial files when the user only names a topic, project, or technology but provides no inspectable source, environment, or acceptance target. Pause and ask one compact missing-input question.

This gate applies when the user says things like "I want to learn FreeRTOS" but does not provide enough material to make project-specific lessons or exercises.

Critical blocking inputs depend on the domain, but usually include only what is needed to begin responsibly:

- source code path, archive, repository URL, document URL, or pasted material
- target hardware, OS, simulator, runtime, or toolchain family when hands-on work is expected
- final demo, deliverable, rubric, or acceptance criteria
- learner constraints that cannot be safely defaulted, such as level, time, language, or depth

Do not ask the user to manually fill in detailed parameters that can be discovered or taught. Classify missing facts:

| Type | What to do | Examples |
|---|---|---|
| Blocking | Ask once before generation. | source path or URL, target board/runtime when hands-on tasks depend on it, toolchain family, final demo or rubric |
| Discoverable | Inspect from source, configs, docs, commands, or logs after the user gives access. | FreeRTOS version, U-Boot version, defconfig, linker script address, device tree nodes, kernel version, build targets |
| Learner-guided | Turn into an exercise or checklist that teaches the learner how to find or configure it. | SPI chip select/mode/speed, I2C bus/address/registers, GPIO node, serial port, baud rate, server/client port |

For discoverable items, say "I will inspect this after you provide the source path or URL" instead of asking the user to type every value. For learner-guided items, write tasks such as "run this command, record the output, then decide the value" or "open this config file and fill the table".

Ask only once. The question should request the smallest useful set, not every possible detail. Example:

```md
我现在还不能负责任地生成 FreeRTOS 学习包，因为缺少可检查材料和最小运行环境。请一次性补充这几项里你已经有的内容：
- 源码位置：本机文件夹、压缩包，或 GitHub/官网源码链接
- 使用环境：芯片/开发板/模拟器，以及大致工具链，比如 Keil、GCC、IAR 或 CMake
- 验收目标：希望最后能跑出什么 demo，或要重点学哪类问题

不用现在填写 RTOS 版本、串口号、波特率、SPI mode、U-Boot 版本这类细节；能从源码或命令里查到的我会自己查，适合学习中确认的我会写成引导式练习。

如果你暂时没有这些信息，我可以先只做“材料准备清单”，不生成完整 tutorial。
```

After this one intake question:

- If the user supplies enough input, inspect it and continue normally.
- If the user explicitly asks for a provisional package, generate only a clearly marked provisional package with `待确认` markers and early evidence-collection tasks.
- If the user still supplies no inspectable source, environment, or acceptance target, do not invent a full package. Provide a material preparation checklist instead.
- Do not repeatedly ask follow-up questions just to make the package perfect; convert remaining gaps into `待确认` items.

## Missing Fact Handling

Avoid long shopping lists of technical details. Prefer this order:

1. Ask for access to the source/materials.
2. Inspect what can be inferred from files, configs, docs, and scripts.
3. Put still-unknown but non-blocking values in `待确认`.
4. Turn practical details into learner tasks with commands, file paths, record tables, and acceptance checks.

Examples:

- For FreeRTOS, ask for the project/source path and broad toolchain first. Inspect `FreeRTOSConfig.h`, portable layer, project files, linker scripts, and build docs before asking about version or port. Make serial port and baud rate an environment-check task unless a fixed value is required by the package.
- For bootloader/IAP/U-Boot, ask for source access and target MCU/board if needed. Inspect linker scripts, map files, defconfig, README, and build scripts before asking for flash layout or U-Boot version. Teach the learner to confirm erase size, app address, and jump method from docs or commands when possible.
- For Linux driver tests, ask for kernel/source path and target board/runtime first. Inspect kernel Makefile, `.config`, device tree, module Makefiles, and test scripts before asking for bus details. Make GPIO/I2C/SPI/server-client parameters guided record fields, not mandatory first-turn inputs, unless the user asks for a ready-to-run command sheet.

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
- 0-4: On the first package-generation turn, stop and ask the one intake question before writing package files. Later, generate only a material preparation checklist or a clearly marked provisional package if the user explicitly wants one.

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

Ask for at most the smallest useful set of blocking missing items. Prefer concrete requests such as:

- source repository path or archive
- target board/model or OS/toolchain family
- build/run commands when the package must be immediately runnable
- expected final demo
- teacher rubric or screenshot text
- existing logs or failure output

Do not put fine-grained configuration values in the first missing-input checklist unless they are true blockers. Values such as SPI mode/speed, I2C address, serial port, baud rate, server/client port, U-Boot version, defconfig, kernel version, or FreeRTOS port are often better handled as discoverable facts or learner-guided tasks.

## Later Supplements

When the user later provides something that was missing:

1. Match it to the old `待补充` list.
2. Move resolved items into `已确认`.
3. Recalculate only the affected readiness dimensions.
4. Update affected tasks so they use the real commands, files, board details, logs, or acceptance criteria.
5. Remove or narrow `待确认` markers that are now resolved.
6. Keep the package structure and progress state unless the supplement changes the project target.

Examples:

- New board IP and serial port should update environment-check tasks, not every chapter.
- New source code path should update reading paths and implementation tasks that point to `待确认`.
- New build log should update failure diagnosis and pass criteria.
- New teacher rubric should update acceptance criteria and scoring, but preserve exercise IDs when possible.

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
