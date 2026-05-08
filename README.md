# learning-workflow-designer

一个把项目、代码库、论文或课程材料整理成“可学习、可练习、可批改、可追踪进度”的 Codex skill。

## 它能做什么

- 把一个项目拆成章节，生成学习内容。
- 生成练习题、参考答案、批注版答案。
- 支持学习模式、复习模式、练习模式、考试模式。
- 支持轻量模式和详细模式。
- 自动生成 `learning-progress.json` 和 `skill-tree.html`，用题目分值驱动 XP、等级、星级和能力节点状态。

## 默认产物

学习模式下默认生成：

如果没有指定输出目录，会自动创建 `tutorial/` 文件夹，并生成：

1. `tutorial/learning-content.md`
2. `tutorial/exercises.md`
3. `tutorial/reference-answers.md`
4. `tutorial/learning-progress.json`
5. `tutorial/skill-tree.html`

其中：

- `learning-content.md`：讲解章节主线知识。
- `exercises.md`：出题并保留答题空间。
- `reference-answers.md`：给出参考答案。
- `learning-progress.json`：记录 XP、等级、星级、题目分值和能力节点状态。
- `skill-tree.html`：展示项目技能树、等级规则、章节映射和下一步任务。

默认行为是写入文件，而不是只在聊天窗口里展开全文。生成完成后，AI 应只返回文件路径和简短说明。

## 等级规则

技能树默认总共 5 级。

- Lv.1：0% XP
- Lv.2：25% XP
- Lv.3：50% XP
- Lv.4：75% XP
- Lv.5：100% XP

`total_xp` 必须等于全部带分值练习的分值总和。学完并完成所有课程练习时，`earned_xp` 应等于 `total_xp`，技能树达到 Lv.5。

## 模式区别

- 学习模式：先讲再练，适合从零学习项目、代码库、论文或课程。
- 复习模式：压缩和巩固已经学过的内容，输出弱点清单、对照表、回忆提示和短练习。
- 练习模式：少讲解，多出题，学习者作答后再批改并更新技能树。
- 考试模式：更正式的自测或试卷，隐藏提示，保留评分标准和独立答案。

## 安装

这个 skill 不需要前端构建流程。Markdown、JSON 和 HTML 生成功能可直接使用；DOCX 转换才需要 Python 环境里的 `python-docx`。

### Codex

把仓库放到 Codex skills 目录即可：

```powershell
git clone https://github.com/heyu-233/learning-workflow-designer.git $env:USERPROFILE\.codex\skills\learning-workflow-designer
```

也可以直接让 Codex 执行：

```text
请帮我安装这个 skill：https://github.com/heyu-233/learning-workflow-designer
```

### Claude Code

Claude Code 也可以交给 AI 安装。把仓库克隆到本机可被 Claude Code 读取的 skills 目录，或让 Claude Code 按当前环境的 skill 目录约定安装：

```text
请把 https://github.com/heyu-233/learning-workflow-designer 安装成一个可用的 skill，并确认 SKILL.md 能被加载。
```

### 交给 AI 安装时的确认点

让 AI 安装后确认这几项：

1. 仓库目录中存在 `SKILL.md`。
2. `SKILL.md` 的 frontmatter 含有 `name` 和 `description`。
3. `references/`、`assets/`、`scripts/` 和 `examples/` 已完整保留。
4. 能运行 `python scripts/render_skill_tree.py assets/learning-progress-template.json skill-tree.html`。
5. 如果需要 DOCX，确认 `python-docx` 可导入；否则只使用 Markdown/HTML 输出。

安装后可以用这些话触发：

- “我想学习这个项目”
- “帮我把这个代码库整理成学习包”
- “进入练习模式，按章节给我出题”
- “批改我的答案，并更新技能树”

## 示例

仓库内置一个 FreeRTOS 轻量示例：

- `examples/freertos-lightweight/exercises.md`
- `examples/freertos-lightweight/reference-answers.md`
- `examples/freertos-lightweight/learning-progress.json`
- `examples/freertos-lightweight/skill-tree.html`

重新渲染示例技能树：

```powershell
python scripts/render_skill_tree.py examples/freertos-lightweight/learning-progress.json examples/freertos-lightweight/skill-tree.html --skin engineering
```

## 目录说明

- `SKILL.md`：主规则和触发方式。
- `references/`：模式、题型、输出格式、质量检查、技能树皮肤和视觉参考。
- `assets/`：Markdown、JSON 和 HTML 模板。
- `examples/`：轻量示例项目。
- `scripts/`：Markdown 转 DOCX、技能树渲染等工具。

## 许可证

MIT License，见 `LICENSE` 文件。
