# Learning Workflow Designer

![License](https://img.shields.io/badge/license-MIT-2563eb)
![Codex Skill](https://img.shields.io/badge/Codex-skill-111827)
![Outputs](https://img.shields.io/badge/outputs-Markdown%20%7C%20HTML%20%7C%20DOCX-16a34a)
![Mode](https://img.shields.io/badge/mode-project--lab-f59e0b)

把项目、代码库、论文或课程资料，整理成一套可以学习、可以练习、可以批改、可以追踪进度的学习包。

它不只是帮你写学习总结。它会生成章节化学习内容、带答题空间的练习题、参考答案、学习进度 JSON，以及带 XP、等级称号和能力节点的技能树页面。

![Skill tree preview](docs/images/skill-tree.png)

## 适合什么场景

- 你想系统学习一个陌生代码库，但不知道从哪里开始。
- 你想把老师布置的任务拆成可执行的学习路线。
- 你想边学基础知识，边一步一步完成一个小项目。
- 你想自动生成练习题、参考答案和批改反馈。
- 你想用技能树记录自己学到了哪里，而不是只靠感觉。

## 生成什么

默认学习模式会生成一个 `tutorial/` 文件夹：

| 文件 | 用途 |
|---|---|
| `learning-content.md` | 章节化学习内容，包含主线、知识点和源码/材料阅读路径 |
| `exercises.md` | 带答题空间的练习题或项目实验任务 |
| `reference-answers.md` | 参考答案、验收标准、常见错误和排查方向 |
| `learning-progress.json` | XP、等级、星级、题目分值和能力节点状态 |
| `skill-tree.html` | 可视化技能树页面，展示等级、称号、章节映射和下一步任务 |

练习题不会只是一串问题。它会保留可填写的答题区，例如空行、记录表、命令输出区、日志路径区和结论区。

![Exercise chain preview](docs/images/exercise-chain.png)

## 核心模式

| 模式 | 适合场景 | 输出重点 |
|---|---|---|
| Learning Mode | 从零学习项目、论文、课程或代码库 | 先讲解，再练习，默认 10 章 |
| Project-Lab Mode | 边学边完成一个具体项目 | 从最终项目验收目标倒推里程碑和练习 |
| Review Mode | 已学过，想快速复习巩固 | 弱点清单、对照表、短练习 |
| Practice Mode | 主要想刷题并获得反馈 | 练习题、答案、批改和进度更新 |
| Exam Mode | 想做正式自测或模拟考试 | 独立试卷、评分标准、单独答案 |

## Project-Lab Mode

Project-Lab Mode 是这个 skill 的重点模式之一。它适合“我想学这个项目，同时通过练习一步一步把项目做出来”的场景。

它的工作方式是：

1. 先提取最终项目目标和验收标准。
2. 拆出 4 到 8 个项目里程碑。
3. 保留默认 10 个学习章节。
4. 把项目里程碑映射到 10 个章节里。
5. 每章练习都连接基础知识、源码阅读、实现任务、运行观察和失败排查。

> [!NOTE]
> 章节和里程碑不是一回事。默认仍然生成 10 个学习章节；项目里程碑只是贯穿这些章节的实现主线。

Project-Lab 任务通常会包含：

```md
目标：
为什么它服务于最终项目：
阅读/跟踪：
实现/修改：
运行/观察：
通过标准：
失败排查：
填写区：
- 修改文件：
- 实现说明：
- 运行命令：
- 观察现象：
- 提交证据：
```

![Annotated exercise preview](docs/images/exercise-annotated.png)

## 技能树和等级

技能树由 `learning-progress.json` 驱动。XP 只来自显式带分值的练习，不会凭“感觉懂了”自动加分。

默认 5 级：

| 等级 | 默认称号 | XP 阈值 |
|---|---|---|
| Lv.1 | 新手 | 0% |
| Lv.2 | 初学者 | 25% |
| Lv.3 | 进阶者 | 50% |
| Lv.4 | 熟练者 | 75% |
| Lv.5 | 掌握者 | 100% |

默认大多数项目使用 classic 称号组；少数项目会稳定抽到 `sao`、`eu4`、`hoi4` 或 `civ6` 风格称号，增加一点新鲜感。你也可以在 `learning-progress.json` 里指定 `level_title_set` 或自定义 `level_titles`。

## 快速开始

### 安装到 Codex

```powershell
git clone https://github.com/heyu-233/learning-workflow-designer.git $env:USERPROFILE\.codex\skills\learning-workflow-designer
```

也可以让 Codex 安装：

```text
请帮我安装这个 skill：https://github.com/heyu-233/learning-workflow-designer
```

### 常用触发方式

```text
我想学习这个项目，请整理成学习包。
```

```text
进入 project-lab mode，围绕这个小项目生成 10 章学习路线和练习题。
```

```text
通过练习一步一步完成这个项目，练习题里要有答题空间、运行记录和验收标准。
```

```text
批改我的答案，并更新 learning-progress.json 和 skill-tree.html。
```

## 示例

仓库内置了一个 FreeRTOS 轻量示例：

- `examples/freertos-lightweight/exercises.md`
- `examples/freertos-lightweight/reference-answers.md`
- `examples/freertos-lightweight/learning-progress.json`
- `examples/freertos-lightweight/skill-tree.html`

重新渲染示例技能树：

```powershell
python scripts/render_skill_tree.py examples/freertos-lightweight/learning-progress.json examples/freertos-lightweight/skill-tree.html --skin engineering
```

## 质量约束

这个 skill 会尽量遵守以下规则：

- 默认学习包为 10 章，除非用户明确要求改变章节数。
- 后面的章节可以复用前面的知识点，前面的章节不能依赖后面才讲的内容。
- 练习题、试卷和项目实验任务必须留下答题空间。
- 工程类任务必须包含可观察证据，例如命令输出、日志、截图路径或运行现象。
- Project-Lab Mode 中，每个主要练习都应该推动最终项目向前完成一小步。
- 中文输出生成后应运行编码检查，避免 PowerShell/CMD 写入导致乱码。

```powershell
python scripts/validate_text_encoding.py tutorial
```

## 目录结构

| 路径 | 说明 |
|---|---|
| `SKILL.md` | skill 主规则和触发说明 |
| `references/` | 模式、题型、输出格式、质量检查、技能树规则 |
| `assets/` | Markdown、JSON 和 HTML 模板 |
| `examples/` | 示例学习包 |
| `docs/images/` | README 和文档示例图片 |
| `scripts/` | DOCX 转换、技能树渲染、编码检查等工具 |

## DOCX 支持

Markdown 和 HTML 输出可直接使用。若需要 DOCX 转换，请确认 Python 环境中安装了 `python-docx`。

```powershell
python scripts/md_to_docx.py learning-content.md learning-content.docx
```

## License

MIT License. See [LICENSE](LICENSE).
