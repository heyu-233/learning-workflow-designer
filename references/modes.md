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

### Review Mode

Use when the user already studied the material and wants fast consolidation.

Outputs:

- Review outline.
- Weak-point checklist.
- Mistake categories.
- Short reinforcement exercises.

Keep review mode concise. Prefer recall prompts, comparison tables, and troubleshooting checklists.

### Exam Mode

Use when the user wants a formal test or self-test.

Outputs:

- Paper without answers.
- Scoring rubric when useful.
- Separate reference-answer document.

Exam mode should combine factual recall, concept judgment, chain analysis, code judgment, and troubleshooting.

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
