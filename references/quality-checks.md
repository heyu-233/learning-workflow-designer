# Quality Checks

Run these checks before finalizing generated learning materials or critique.

## Continuity

- Every chapter has a one-sentence main line.
- Concepts appear after their prerequisites.
- No chapter jumps from global architecture to low-level details without a bridge.
- Later exercises may refer to earlier chapters, but not to unexplained future concepts.

## Exercise Quality

- Lightweight mode: no more than 3 exercises per chapter.
- Detailed mode: exactly 5 exercises per chapter.
- Do not repeat the same knowledge point across multiple questions in the same chapter.
- Do not overuse one question type in a chapter.
- Include reasoning-heavy questions where possible.
- Avoid hand-drawing requirements; prefer system diagram judgment or chain correction.
- In lightweight mode, favor a small number of composite exercises with multiple sub-questions over several isolated tiny questions when that yields broader concept coverage.
- A composite exercise may span ordering, explanation, boundary checking, and bug spotting, as long as the sub-questions remain tightly related and the answer space is still manageable.
- Do not let an entire chapter become one-note. Mix stem styles such as sort-and-explain, code-and-diagnose, chain-and-correct, compare-and-contrast, or scenario-based multi-part prompts.
- If a chapter uses three exercises, they should feel structurally different from each other.
- If a chapter uses one composite exercise, its sub-questions should progress from recognition to explanation to boundary checking.

## Answer Separation

- Keep learning content, exercises, and reference answers separate unless the user asks for a combined teacher edition.
- Exercise documents should not reveal answers.
- Reference answers should identify the question clearly.
- When the source material supports it, create at least one exercise that asks the learner to order, then explain, rather than only asking them to describe.

## Critique

When checking completed answers:

- Mark whether the answer is correct, partially correct, or incorrect.
- Separate wording issues from concept errors.
- For partially correct answers, say what is already right and what must be added.
- For incorrect answers, explain the mistaken boundary or chain.
- Keep comments actionable and close to the relevant answer.

## Anti-Hallucination

- Prefer source-grounded facts.
- If files or facts are missing, write "待确认" instead of inventing.
- For codebases, inspect actual files before naming modules, ports, APIs, or classes.
- Do not reuse a fixed capability tree across unrelated projects; derive feedback nodes from the current materials and chapter plan.
