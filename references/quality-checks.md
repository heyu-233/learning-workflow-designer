# Quality Checks

Run only checks relevant to changed files unless producing a full package.

## Scope And Intake

- Reuse source intake, chapter map, progress JSON, and skill tree for existing packages unless the request changes them.
- Treat later code, logs, commands, screenshots, board info, or rubrics as supplements; patch affected chapters/tasks instead of regenerating everything.
- Run source intake before full package generation. If first-turn readiness is below 5/10, ask one compact question for blocking inputs only, then stop.
- Do not ask for details that can be inspected from source/configs/docs/logs or taught through exercises.
- Mark unknown facts as `待确认`; do not invent files, commands, pins, APIs, logs, tests, or hardware behavior.

## Continuity And Exercises

- Every chapter has a one-sentence main line; prerequisites appear before dependent concepts.
- Earlier chapters must not require future APIs, files, protocol fields, debugging methods, or artifacts.
- Lightweight mode uses <= 3 exercises per chapter; detailed mode uses exactly 5.
- Exercise titles must be concrete actions, not abstract labels such as `建立环境基线` or `打通链路`.
- Every learner-facing item includes immediate answer space.
- Keep learning content, exercises, and reference answers separate.
- Include varied, reasoning-heavy questions where useful; avoid repeating the same point in one chapter.

## Engineering And Project-Lab

- Prefer run/observe/trace/compare/diagnose/record tasks over definitions.
- Include commands, observable evidence, pass criteria, failure diagnosis, submitted evidence, and XP when the source supports them.
- Project-lab keeps the default 10 chapters unless explicitly changed; milestones map across chapters.
- Each milestone creates or verifies a concrete artifact.
- Hands-on reference answers may be mentor checklists instead of full solutions unless teacher edition is requested.

## Critique And Progress

- Mark answers correct, partially correct, or incorrect.
- Separate wording weakness from concept errors.
- Award XP only from explicit submitted evidence.
- Keep feedback close to the answer and include the next smallest task.

## Encoding

- Avoid Chinese inside PowerShell/CMD inline script strings.
- Prefer `apply_patch`, checked-in templates, or UTF-8 files read by scripts.
- After generating Chinese Markdown/JSON/HTML, run `python scripts/validate_text_encoding.py <output-path>`.
