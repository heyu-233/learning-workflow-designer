# Question Types

Use question types to expose misunderstandings, not just memorization gaps.

## Available Types

- Fill-in-the-blank: names, ports, file paths, key terms, sequence anchors.
- True/false judgment: quick concept boundaries.
- Multiple choice: exam mode or single-best-answer checks.
- Short answer: explain why a design or step is used.
- Ordering plus explanation: sort a chain, then justify the order.
- Chain judgment: inspect a data/control/media flow and decide whether it is correct.
- Chain correction: identify the wrong step, write the correct chain, and explain the debugging impact.
- System diagram judgment: inspect a textual block diagram and identify missing or wrong parts.
- Code function judgment: explain what a core code block does.
- Code correction: repair flawed pseudocode or code.
- Troubleshooting: diagnose a symptom in the shortest reliable order.
- Practical record: record command, phenomenon, log, and conclusion.
- Comprehensive retelling: explain the whole chapter or system in several sentences.
- Composite multipart question: one stem plus several related sub-questions.
- Contrast question: compare two similar options or chains.
- Engineering architecture task: describe module map, responsibilities, inputs, processing, and outputs.
- Command verification task: run a command, record the result, and explain what it proves.
- Call-chain tracing task: trace a UI action, API request, message, frame, interrupt, or function call through real modules.
- Runtime observation task: verify behavior with logs, Network, device files, ports, process status, or performance output.
- Stage acceptance task: prove the learner can explain, run, verify, or diagnose a stage.

## Reusable Templates

Replace every placeholder with project-specific material from the source.

### Ordering Plus Explanation

```md
### 题 X：排序后解释（N 分）

下面是 `{{concept_or_flow}}` 的几个步骤，目前顺序被打乱：

1. {{step_a}}
2. {{step_b}}
3. {{step_c}}
4. {{step_d}}

请完成：

1. 写出正确顺序。
2. 解释为什么 `{{key_step}}` 必须出现在这个位置。
3. 如果 `{{wrong_order}}` 发生，会出现什么现象或风险？

答：
```

### Pseudocode Multi-Question

````md
### 题 X：伪代码多问（N 分）

阅读下面的伪代码：

```text
{{pseudocode}}
```

请回答：

1. 这段逻辑解决了什么问题？
2. 哪个条件决定了 `{{state_or_branch}}`？
3. 如果 `{{edge_case}}` 发生，代码应该如何处理？
4. 给出一个最小修改，让它更符合 `{{project_constraint}}`。

答：
````

### Contrast Analysis

```md
### 题 X：对照辨析（N 分）

方案 A：{{option_a}}

方案 B：{{option_b}}

请比较：

1. 二者在 `{{dimension_1}}` 上的关键差异是什么？
2. 哪个方案更适合 `{{scenario}}`？为什么？
3. 另一个方案在什么情况下反而更合适？

答：
```

### Chain Correction

````md
### 题 X：链路纠错（N 分）

下面的链路描述有一处或多处错误：

```text
{{wrong_chain}}
```

请完成：

1. 标出错误位置。
2. 写出正确链路。
3. 说明这个错误会导致怎样的调试误判。

答：
````

## Lightweight Selection

For each chapter:

- Use at most 3 exercises.
- Prefer 2 to 3 different types.
- Include at least one reasoning-heavy type when the material supports it.
- Do not test the same knowledge point twice in the same chapter.
- Use composite multipart questions when one coherent code or flow block covers nearby ideas better than many tiny questions.
- Vary stem style across the chapter.
- For engineering projects, each chapter should have one core question, one understanding task, and one hands-on test when the source supports it.

## Detailed Selection

For each chapter:

- Use exactly 5 exercises.
- Include at least one conceptual question.
- Include at least one chain/code/diagram judgment question when applicable.
- Include at least one troubleshooting or practical record question for engineering projects.
- For engineering projects, include a chapter quick table, recommended test commands, stage acceptance criteria, and a small final task.

## Avoid

- Requiring hand-drawn diagrams when a textual system-diagram judgment would test the same skill.
- Long rote lists with no reasoning.
- Exercises whose answer is already visible in the immediately preceding sentence unless the goal is early recall.
- Splitting one coherent code or flow block into many isolated micro-questions.
- Repeating the same opening phrase across all questions in a chapter.
