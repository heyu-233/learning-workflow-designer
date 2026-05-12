# Modes And Density

## Main Modes

### Learning Mode

Use when the user wants to learn a project, paper, codebase, or course from the ground up.

Default outputs:

- Learning content.
- Exercise paper.
- Reference answers.

Default structure:

- 10 chapters unless the source material strongly suggests another count.
- Each chapter has a main-line sentence, lesson body, and exercises.
- Chapters must progress from global map to module details to integration and debugging.

Learning mode teaches first, then tests. It should create a coherent path from prerequisites to application, and it may introduce new concepts the learner has not seen.

For engineering projects, learning mode should also produce a task-based exercise pack. Write each task in teacher language: first say what the learner should do, then how to do it, why it matters when useful, and what counts as finished. Do not name tasks with abstract labels such as "environment baseline" or "capability chain"; translate them into concrete actions.

### Project-Lab Mode

Use when the user wants to learn foundations while completing a concrete project step by step. English triggers include `project-lab mode`, `capstone-driven learning`, `project-driven labs`, `build this project while learning`, and `complete the project through exercises`. Chinese triggers include `项目实验模式`, `项目驱动学习`, `边学边做项目`, `通过练习完成项目`, `以小项目为主线`, and `一步一步完成项目`.

Outputs:

- Learning content focused on only the concepts needed for the project.
- Exercise document as a milestone build guide.
- Reference answers with acceptance criteria, expected observations, hints, and diagnostic paths.
- Progress JSON and skill-tree HTML.

Project-lab mode starts from the final project acceptance target and designs exercises backward from project milestones. Milestones are not chapters. Keep the default 10-chapter learning structure unless the user explicitly asks for a different chapter count; map the project milestones across those chapters. Each chapter should connect a foundation topic, a source-reading or observation task, and a concrete project artifact to implement or verify.

Every project-lab task must be understandable without decoding engineering shorthand. Use titles like "确认板子能联网、能登录、能运行基本命令" instead of "建立板端环境基线".

Project-lab mode may use more guided sub-steps than normal lightweight mode when the project is unfamiliar. The main exercises should move the project forward; pure review questions should be optional.

### Review Mode

Use when the user already studied the material and wants fast consolidation.

Outputs:

- Review outline.
- Weak-point checklist.
- Mistake categories.
- Short reinforcement exercises.

Keep review mode concise, but still write like a teacher. A review prompt must say what to recall, what to compare, or what symptom to diagnose. Do not write vague items like "巩固核心链路"; write "用 5 句话说清楚客户端发消息到服务器回复之间经过了哪些步骤".

Review mode does not re-teach the whole course. It compresses existing material into weak-point maps, memory hooks, contrast tables, and targeted checks. Use it when the learner says they have learned once but want to consolidate, summarize, or prepare for a second pass.

### Practice Mode

Use when the user mainly wants to answer questions and receive feedback.

Outputs:

- Practice set without embedded answers.
- Separate reference answers or rubric.
- Optional answer sheet for learner responses.
- Critique and skill-tree update after the learner submits answers.

Practice mode is exercise-first. Keep explanations short before the learner answers, then give detailed feedback after grading. Use varied question types and explicit point values so progress can update reliably. Even short prompts must be concrete: what to answer, how much to answer, and what evidence or reason to include.

### Exam Mode

Use when the user wants a formal test or self-test.

Outputs:

- Paper without answers.
- Scoring rubric when useful.
- Separate reference-answer document.

Exam mode should combine factual recall, concept judgment, chain analysis, code judgment, and troubleshooting.

Exam mode is stricter than practice mode: fewer hints, clearer timing/scoring expectations, and a paper-like structure. Practice mode may coach after each answer; exam mode should preserve assessment integrity until answers are submitted. Do not remove clarity for the sake of difficulty: exam questions still need plain wording and an observable scoring target.

## Density

### Lightweight Mode

Default. Use when the user does not specify density.

Rules:

- Keep each chapter concise and coherent.
- Avoid deep side topics.
- Do not exceed 3 exercises per chapter.
- Use 2 to 3 different question types per chapter when possible.
- Avoid repeated knowledge points in exercises.

### Detailed Mode

Use when the user asks for deeper, fuller, or more rigorous learning material.

Rules:

- Explain important concepts more fully.
- Emphasize relationships, failure modes, and implementation details.
- Use exactly 5 exercises per chapter.
- Still preserve chapter continuity and avoid repeated testing of the same point.

## Defaults

If the user only says "make a learning workflow" or similar, choose:

```text
learning mode + lightweight mode + 10 chapters + Markdown outputs
```

If the user names a final project and asks to complete it through exercises, choose:

```text
project-lab mode + 10-chapter learning path + milestone build guide + explicit evidence-based XP
```
