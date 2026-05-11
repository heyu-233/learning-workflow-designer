# Quality Checks

Run these checks before finalizing generated learning materials or critique.

## Continuity

- Every chapter has a one-sentence main line.
- Concepts appear after their prerequisites.
- No chapter jumps from global architecture to low-level details without a bridge.
- Later exercises may refer to earlier chapters, but not to unexplained future concepts.

## Exercise Quality

- Lightweight mode: no more than 3 exercises per chapter.
- Detailed mode: exactly 5 exercises per chapter.
- Do not repeat the same knowledge point across multiple questions in the same chapter.
- Do not overuse one question type in a chapter.
- Include reasoning-heavy questions where possible.
- Prefer system diagram judgment or chain correction over asking the learner to hand-draw diagrams.
- In lightweight mode, favor compact composite exercises when they cover a broader concept chain without inflating chapter count.
- If a chapter uses three exercises, they should feel structurally different.
- If a chapter uses one composite exercise, its sub-questions should progress from recognition to explanation to boundary checking.

## Engineering Practice Quality

- Engineering learning packs should include a learning record template.
- Engineering chapter tables should include chapter, core question, required understanding task, and required hands-on test.
- Prefer "run, observe, trace, draw, compare, diagnose, record" tasks over pure definition questions.
- Include recommended commands when the source material contains runnable commands, ports, device paths, APIs, logs, or build steps.
- Include 2 to 4 observable stage acceptance groups.
- Include one small final task that forces synthesis without becoming a new project.

## Answer Separation

- Keep learning content, exercises, and reference answers separate unless the user asks for a combined teacher edition.
- Exercise documents should not reveal answers.
- Reference answers should identify the question clearly.
- When the source material supports it, include at least one exercise that asks the learner to order, then explain.

## Critique

- Mark each answer as correct, partially correct, or incorrect.
- Separate wording issues from concept errors.
- For partially correct answers, say what is already right and what must be added.
- For incorrect answers, explain the mistaken boundary or chain.
- Keep comments actionable and close to the relevant answer.

## Anti-Hallucination

- Prefer source-grounded facts.
- If files or facts are missing, write "待确认" instead of inventing.
- For codebases, inspect actual files before naming modules, ports, APIs, or classes.
- Do not reuse a fixed capability tree across unrelated projects; derive feedback nodes from the current materials and chapter plan.

## Encoding Integrity

- Do not embed Chinese content inside PowerShell/CMD inline Python or one-liner script strings.
- Prefer `apply_patch`, checked-in templates, or UTF-8 files read by scripts.
- After generating Chinese Markdown, JSON, or HTML, run:

```powershell
python scripts/validate_text_encoding.py tutorial
```

- If the user chose another output directory, scan that directory instead.
- Treat repeated question marks, Unicode replacement characters, or common mojibake markers as real corruption until proven otherwise.
