# Claude Code Adapter

This adapter turns Learning Workflow Designer into a Claude Code skill. It keeps the same platform-neutral learning-package format while using Claude Code as the authoring environment.

## Install As A User Skill

PowerShell:

```powershell
$target = "$env:USERPROFILE\.claude\skills\learning-workflow-designer"
New-Item -ItemType Directory -Force $target | Out-Null
Copy-Item -Recurse -Force adapters\claude-code\skills\learning-workflow-designer\* $target
```

macOS/Linux:

```bash
mkdir -p ~/.claude/skills/learning-workflow-designer
cp -R adapters/claude-code/skills/learning-workflow-designer/* ~/.claude/skills/learning-workflow-designer/
```

## Install As A Project Skill

Copy the skill into the current project:

```powershell
New-Item -ItemType Directory -Force .claude\skills\learning-workflow-designer | Out-Null
Copy-Item -Recurse -Force adapters\claude-code\skills\learning-workflow-designer\* .claude\skills\learning-workflow-designer
```

## Use

In Claude Code, ask naturally:

```text
Use the learning-workflow-designer skill. Enter project-lab mode and turn this project into a 10-chapter learning package with exercises, answer space, reference answers, and progress tracking.
```

Chinese trigger:

```text
使用 learning-workflow-designer skill。进入项目实验模式，先做材料审计，再围绕这个项目生成 10 章学习包、练习题、参考答案和学习进度。
```

## Output

By default, ask Claude Code to write:

- `tutorial/learning-content.md`
- `tutorial/exercises.md`
- `tutorial/reference-answers.md`
- `tutorial/learning-progress.json`
- `tutorial/skill-tree.html` when the rendering script exists, otherwise a static placeholder or Markdown progress view

## Notes

- Claude Code can inspect and edit the local project, so this adapter is strongest for codebase learning and project-lab tasks.
- The adapter does not require Codex. It reuses the same package spec and answer-space rules.
- If the repository has `scripts/render_skill_tree.py`, ask Claude Code to render the HTML skill tree from `learning-progress.json`.
