# Question Types

Use question types to expose misunderstandings, not just memorization gaps.

## Available Types

- Fill-in-the-blank: good for names, ports, file paths, key terms, and sequence anchors.
- True/false judgment: good for quick concept boundaries.
- Multiple choice: good for exam mode and single-best-answer checks.
- Short answer: good for explaining why a design is used.
- Chain judgment: provide a data/control/media flow and ask whether it is correct.
- System diagram judgment: provide a textual block diagram and ask what is wrong or missing.
- Code function judgment: provide a core code block and ask what it does.
- Code correction: provide flawed pseudocode or code and ask how to fix it.
- Troubleshooting: give a symptom and ask for a diagnostic order.
- Practical record: ask the learner to record command, phenomenon, log, and conclusion.
- Comprehensive retelling: ask the learner to explain the whole system or chapter in several sentences.
- Composite multipart question: one stem plus several sub-questions, good for covering multiple nearby knowledge points without inflating chapter count.
- Ordering plus explanation: ask the learner to sort a chain first, then explain why that order is correct.
- Pseudocode multi-question: provide one pseudocode or code block and ask several related questions about function, boundary, and failure mode.
- Contrast question: present two similar options or chains and ask the learner to explain the difference.
- Engineering architecture task: ask the learner to draw or describe the module map, responsibilities, inputs, processing, and outputs.
- Command verification task: ask the learner to run a command, record the result, and explain what the result proves.
- Call-chain tracing task: ask the learner to trace a UI action, API request, message, frame, interrupt, or function call through real modules.
- Runtime observation task: ask the learner to use logs, browser Network, device files, ports, process status, or performance output to verify behavior.
- Stage acceptance task: ask the learner to prove they can explain, run, verify, or diagnose a stage of the system.

## Reusable Templates

Use these templates as shapes. Replace every placeholder with project-specific material from the source.

### Ordering Plus Explanation

```md
### 题 X：排序后解释（N 分）

下面是 `{{concept_or_flow}}` 的若干步骤，它们现在顺序被打乱：

1. {{step_a}}
2. {{step_b}}
3. {{step_c}}
4. {{step_d}}

请完成：

1. 写出正确顺序。
2. 解释为什么 `{{key_step}}` 必须出现在这个位置。
3. 指出如果 `{{wrong_order}}` 发生，会出现什么现象或风险。

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

1. 两者在 `{{dimension_1}}` 上的关键差异是什么？
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
- Include at least one reasoning-heavy type when the material supports it: chain judgment, system diagram judgment, code judgment, or troubleshooting.
- Do not test the same knowledge point twice in the same chapter.
- It is acceptable for one exercise to contain multiple sub-questions if they are tightly related and together cover a broader concept chain.
- Try to vary the stem style across the chapter, not just the knowledge point.
- Good chapter patterns include: sort then explain, pseudo-code then diagnose, chain then correct, or compare two nearly correct options.
- For engineering projects, each chapter should have one core question, one understanding task, and one hands-on test when the source supports it.

## Detailed Selection

For each chapter:

- Use exactly 5 exercises.
- Include at least one conceptual question.
- Include at least one chain/code/diagram judgment question when applicable.
- Include at least one troubleshooting or practical record question for engineering projects.
- For engineering projects, include a chapter quick table, recommended test commands, stage acceptance criteria, and a small final task.

## Avoid

- Requiring hand-drawn diagrams when a system diagram judgment question would test the same skill.
- Long rote lists with no reasoning.
- Exercises whose answer is already visible in the immediately preceding sentence unless the goal is very early recall.
- Splitting one coherent code or flow block into many isolated micro-questions when a composite question would be clearer.
- Repeating the same opening phrase across all questions in a chapter.
