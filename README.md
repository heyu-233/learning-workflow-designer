# learning-workflow-designer

一个把项目、代码库、论文或课程材料整理成“可学习、可做题、可批改、可追踪进度”的 Codex skill。

## 它能做什么

- 把一个项目拆成章节，生成学习内容。
- 生成练习题、参考答案、批注版答案。
- 支持学习模式、复习模式、考试模式。
- 支持轻量模式和详细模式。
- 自动生成项目技能树 `skill-tree.html`，并用题目分值驱动进度。

## 适合什么场景

- 你想学习一个新项目。
- 你想把一个代码库快速梳理成笔记。
- 你想把章节内容做成题目再反复练习。
- 你想在答题后得到批注和正反馈。

## 默认产物

学习模式下，默认会生成：

1. `learning-content.md`
2. `exercises.md`
3. `reference-answers.md`
4. `learning-progress.json`
5. `skill-tree.html`

其中：
- `learning-content.md` 负责讲解主线知识。
- `exercises.md` 负责出题和留答题空间。
- `reference-answers.md` 负责参考答案。
- `learning-progress.json` 负责记录 XP、星级、题目分值和能力节点状态。
- `skill-tree.html` 负责展示项目技能树、XP、星级和节点状态。

## 设计特点

- 默认从源码和实际材料出发，不靠空想。
- 题目支持多小问、排序题、代码判断题、链路判断题、故障排查题。
- 技能树的成长只认 `exercises.md` 里的明确分值。
- 每次答题后都可以继续刷新技能树状态。

## 示例截图

### 技能树页面

![技能树示例](docs/images/skill-tree.png)

### 带批注的练习内容

![练习批注示例](docs/images/exercise-annotated.png)

### 链路判断题示例

![链路判断示例](docs/images/exercise-chain.png)

## 使用方式

你可以直接对 Codex 说：

- “我想学习这个项目”
- “帮我把这个代码库整理成学习包”
- “按章节给我出题”
- “把我做的题批改一下”

也可以明确指定：

- `学习模式`
- `复习模式`
- `考试模式`
- `轻量模式`
- `详细模式`

## 目录说明

- `SKILL.md`：主规则和触发方式
- `references/`：模式、题型、输出格式、质量检查、视觉参考
- `assets/`：模板和 HTML 骨架
- `examples/`：轻量示例项目
- `scripts/`：Markdown 转 DOCX 的工具

## 许可证

MIT License，见 `LICENSE` 文件。
