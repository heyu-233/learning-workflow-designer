# Output Formats

## Markdown

Markdown is the default because it is easy to inspect, edit, diff, and convert.

Recommended files:

- `learning-content.md`
- `exercises.md`
- `reference-answers.md`
- `skill-tree.html` as part of the default learning package

For critique:

```md
> 批注：这里理解基本正确，但建议补充……
```

Use:

- Headings for chapters.
- Tables for comparisons and port/API lists.
- Fenced code blocks for code and chains.
- Blank answer lines for learner responses.

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

If conversion fails because `python-docx` is missing, keep the Markdown outputs and tell the user to install `python-docx`.

## HTML Skill Tree

Use a static `skill-tree.html` for the project-specific capability tree when the user wants a visible progress page.

Requirements:

- Self-contained single file.
- Game-like presentation: level badge, star rating, experience bar, and unlock states.
- Starting state is always 0 XP and 0 stars until exercise points are earned.
- Clear title, source/project label, and chapter mapping.
- Visual status markers for `未解锁`, `进行中`, and `已解锁`.
- Compact positive-feedback block with `本章获得`, `技能树进度`, and `下一步最小任务`.
- No README wrapper around the same content unless the user explicitly asks for one.
- Refresh the page whenever the learner's state changes after an answer, critique, or chapter update.
- All progress values must come from explicit point values in `exercises.md`, not from guessed understanding.
