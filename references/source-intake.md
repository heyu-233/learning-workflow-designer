# Source Intake

Use source intake before full package generation, changed source material, or supplements that resolve missing facts. Reuse an existing audit for narrow edits.

## Initial Readiness Gate

Do not generate tutorial files on the first package-generation turn when the user only names a topic/project/technology and provides no inspectable source, environment, or acceptance target. Ask one compact missing-input question, then stop.

Ask only for blocking inputs:

- source code path, archive, repository URL, document URL, or pasted material
- target board/runtime/OS/simulator/toolchain family when hands-on work depends on it
- final demo, deliverable, rubric, or acceptance criteria
- learner constraints that cannot be safely defaulted

Classify missing facts:

| Type | What to do | Examples |
|---|---|---|
| Blocking | Ask once before generation. | source path/URL, target runtime when hands-on work depends on it, toolchain family, final demo/rubric |
| Discoverable | Inspect from source/configs/docs/commands/logs. | FreeRTOS or U-Boot version, defconfig, linker address, device tree nodes, kernel version, build targets |
| Learner-guided | Turn into tasks with commands, file paths, record tables, and acceptance checks. | SPI mode/speed, I2C address/registers, GPIO node, serial port/baud, server/client port |

Do not ask for discoverable or learner-guided details up front. Say they will be inspected or turned into exercises.

## Readiness Score

Score the input from 0 to 10 before full generation:

| Dimension | Points | Check |
|---|---:|---|
| Goal clarity | 0-2 | Final learning goal or project acceptance target is explicit. |
| Source accessibility | 0-2 | Code, docs, diagrams, logs, papers, or course files are available and inspectable. |
| Environment clarity | 0-2 | Hardware, OS, toolchain, commands, devices, or runtime assumptions are known when needed. |
| Acceptance criteria | 0-2 | Completion can be judged by tests, observations, deliverables, rubrics, or demos. |
| Learner constraints | 0-2 | Time, level, language, depth, format, and chapter count are known or safely defaultable. |

Readiness bands:

- 8-10: Generate a full learning package.
- 5-7: Generate with `待确认` items; avoid unsupported precise claims.
- 0-4: On first generation turn, ask the one intake question and stop. Later, generate only a preparation checklist or clearly marked provisional package if explicitly requested.

## Missing-Information Checklist

When critical material is missing, include a compact audit:

```md
## Material Audit
Readiness: X/10
Confirmed:
- ...
Missing:
- ...
Impact:
- ...
```

## Later Supplements

When the user later provides something that was missing:

1. Match it to old missing items.
2. Move resolved items into confirmed material.
3. Recalculate only affected readiness dimensions.
4. Patch affected chapters, exercises, acceptance criteria, and reference checklists.
5. Preserve package structure, progress state, and exercise IDs unless the project target changed.

## Provisional Package Rules

If generating with incomplete materials:

- Mark the package as provisional.
- Use `待确认` for unknown files, commands, APIs, hardware pins, addresses, or protocol fields.
- Use source-grounded tasks where possible and environment-discovery tasks where not.
- Do not invent exact module names, pins, registers, ports, commands, or acceptance logs.
- Include early exercises that collect the missing evidence.

## Project-Lab Intake

For project-lab mode, identify:

1. Final project acceptance target.
2. Demo evidence that proves completion.
3. Hardware/software/source assumptions.
4. Safety risks or irreversible operations.
5. What each milestone must produce.

If the final target is clear but the environment is unclear, make chapter 1 a concrete environment check before implementation tasks.
