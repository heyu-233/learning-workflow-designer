# Output Formats

## Markdown

Markdown is the default because it is easy to inspect, edit, diff, and convert.

Default behavior is to write files to disk. Do not emit the full package only in chat unless the user explicitly requests inline output.

Recommended learning-package files:

- `tutorial/learning-content.md`
- `tutorial/exercises.md`
- `tutorial/reference-answers.md`
- `tutorial/learning-progress.json`
- `tutorial/skill-tree.html`

These files are platform-neutral outputs. Codex is the first authoring environment, but the generated Markdown, JSON, DOCX, and static HTML should remain usable in other tools.

If the user provides another output directory, use that directory instead of `tutorial/`.

After file generation, respond with a compact file list and a short summary.

For Chinese output, avoid writing content through PowerShell/CMD inline scripts. Generate files through `apply_patch`, checked-in scripts, or UTF-8 source files, then run:

```powershell
python scripts/validate_text_encoding.py tutorial
```

## Answer Space

Every learner-facing question document must leave answer space.

Use one of these forms directly after each prompt:

- Conceptual question: `答：` followed by 3 to 6 blank lines or Markdown horizontal answer lines.
- Multi-part question: a small table with columns such as `小问`, `我的答案`, `证据/原因`.
- Engineering task: a structured record block with fields such as `命令`, `现象`, `日志`, `结论`, `证据路径`.
- Project-lab task: a build record block with fields such as `修改文件`, `实现说明`, `运行结果`, `失败排查`, `提交证据`.
- Exam paper: leave enough blank lines for the expected answer length.

Do not make `exercises.md`, `practice.md`, or `exam.md` read like an answer key or project README. The learner should be able to write directly into the file.

For critique:

```md
> 批注：这里理解基本正确，但还需要补充具体调用链或证据。
```

Use:

- Headings for chapters.
- Tables for comparisons and port/API lists.
- Fenced code blocks for code and chains.
- Blank answer lines or structured answer blocks for learner responses.

## DOCX

DOCX mode is a basic usable document mode, not a full formal exam-layout engine.

Support:

- Heading levels.
- Tables.
- Numbered or titled questions.
- Answer lines or answer space.
- Separate answer document.
- Basic page breaks.
- Red critique comments.

For critique in DOCX:

- Insert a paragraph immediately after the relevant answer or question.
- Start with `批注：`.
- Set the paragraph text color to red.
- Do not require native Word comments.

## Conversion

Use `scripts/md_to_docx.py` when possible:

```powershell
python scripts/md_to_docx.py input.md output.docx
```

For multiple files:

```powershell
python scripts/md_to_docx.py learning-content.md learning-content.docx
python scripts/md_to_docx.py exercises.md exercises.docx
python scripts/md_to_docx.py reference-answers.md reference-answers.docx
```

If conversion fails because `python-docx` is missing, keep the Markdown outputs and tell the user that DOCX conversion requires `python-docx`.

## HTML Skill Tree

Use a static `skill-tree.html` for the project-specific capability tree when producing or updating a learning package.

Requirements:

- Self-contained single file.
- Game-like presentation: level title, star rating, XP bar, and unlock states.
- Starting state is 0 XP and 0 stars until exercise points are earned.
- Generated from `learning-progress.json` whenever possible.
- Uses 5 levels by default: 0%, 25%, 50%, 75%, and 100% of `total_xp`.
- Clear project label, source summary, level table, capability nodes, and chapter mapping.
- Visual status markers for `未解锁`, `进行中`, and `已解锁`.
- Compact feedback blocks with `本章获得`, `技能树进度`, and `下一步最小任务`.
- No README wrapper around the same content unless the user explicitly asks for one.
- Refresh the page whenever the learner's state changes after an answer, critique, or chapter update.
- All progress values must come from explicit point values in `exercises.md` and `learning-progress.json`, not from guessed understanding.

Render with:

```powershell
python scripts/render_skill_tree.py learning-progress.json skill-tree.html
```

Use `--skin engineering`, `--skin course`, or `--skin paper` when the project style is clear.
