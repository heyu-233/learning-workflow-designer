# Platform Adapters

Learning Workflow Designer is Codex-first, but its learning-package format is platform-neutral. Use this guide to run the same method in other tools.

## Adapter Map

| Platform | Best use | Adapter |
|---|---|---|
| Codex | Full local authoring, file writing, validation, skill-tree rendering | Native `SKILL.md` |
| Claude Code | Local codebase learning and project-lab package generation | `adapters/claude-code/` |
| Claude or ChatGPT web | Prompt-only learning package drafting | `docs/prompt-pack.md` |
| Obsidian | Note-based study system and progress archive | Markdown files + `learning-progress.json` |
| VS Code | Editing, previewing, and versioning learning packages | Markdown/JSON templates + scripts |
| CLI | Future automation target | Planned |

## Claude Code

Claude Code is the strongest non-Codex target because it can inspect local files and write package outputs.

Install the adapter from:

```text
adapters/claude-code/
```

Recommended prompt:

```text
Use the learning-workflow-designer skill. First audit the source materials, then create a project-lab learning package in tutorial/. Keep the default 10 chapters, include answer space after every exercise, keep answers separate, and track XP in learning-progress.json.
```

Chinese:

```text
使用 learning-workflow-designer skill。先做材料审计，再进入项目实验模式，在 tutorial/ 里生成默认 10 章学习包。练习题必须留答题空间，答案单独放，XP 写入 learning-progress.json。
```

## Claude Or ChatGPT Web

Use the prompt pack when the assistant cannot directly access your local files:

```text
docs/prompt-pack.md
```

Best practice:

- Paste a source tree summary instead of only describing the project.
- Paste assignment text, screenshots converted to text, build commands, logs, and final acceptance target.
- Ask for a material audit before the package.
- Generate one chapter first when the source is large.

## Obsidian

Use the learning package as a note vault:

```text
Learning Package/
  learning-content.md
  exercises.md
  reference-answers.md
  learning-progress.json
  skill-tree.html
```

Suggested note links:

- Link each chapter heading in `learning-content.md` to its exercises.
- Store submitted answers below the answer space in `exercises.md`.
- Keep `reference-answers.md` folded or in a separate folder to avoid spoilers.
- Use `learning-progress.json` as the durable progress state even when the visual skill tree is not open.

## VS Code

VS Code is useful for authoring and versioning packages:

- Edit Markdown and JSON directly.
- Preview `skill-tree.html` in a browser.
- Use Git to track progress changes.
- Run validation scripts when this repository is available.

Useful commands:

```powershell
python scripts/validate_text_encoding.py tutorial
python scripts/render_skill_tree.py tutorial/learning-progress.json tutorial/skill-tree.html --skin engineering
```

## Adapter Design Rules

When adding a new platform adapter:

- Keep the core output format unchanged.
- Do not remove answer-space requirements.
- Do not merge answers into learner-facing exercises.
- Preserve source intake and provisional-package behavior.
- Preserve the default 10-chapter rule unless the user explicitly changes it.
- Keep platform-specific instructions in `adapters/<platform>/` instead of bloating the core skill.
