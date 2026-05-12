# Engineering Practice Packs

Use this reference for software, embedded, IoT, backend/frontend, robotics, hardware-in-the-loop, streaming, driver, operating-system, and infrastructure projects.

The goal is not to create a normal quiz sheet. The goal is to make the learner able to reproduce, explain, test, and debug the system.

If the user wants exercises to drive completion of a named final project, use project-lab mode from `references/project-lab.md`. Engineering practice packs can be task-based, but project-lab mode is stricter: each exercise must advance the final project artifact.

Engineering tasks are still written for people. Do not make the learner decode phrases like "establish a board-side baseline" or "complete the driver chain". Say the real action: "确认板子能联网、能登录、能运行 `uname -a`", or "从用户程序的 `open()` 调用开始，找到驱动里对应的函数".

## Default Shape

For engineering projects, the exercise document should include these sections:

1. Learning record template.
2. Chapter exercise quick table.
3. Recommended test commands.
4. Stage acceptance criteria.
5. Small final task.

Keep reference answers separate.

## Chapter Quick Table

Each chapter row should include:

- Chapter number.
- Core question.
- Required understanding task.
- Required hands-on test.

The core question should be concrete, for example:

- Which modules form this system?
- How does the project start and stop?
- How does the frontend reach backend data?
- How does a controller reach a database mapper?
- How does the device expose hardware state?
- How does the media/control/data path flow end to end?

## Exercise Style

Prefer task verbs over school-exam verbs.

Each hands-on task should include:

- What to do.
- How to do it.
- Why it matters when the task is only preparation.
- What evidence proves it is done.

Good verbs:

- draw the architecture or flow.
- trace a request, command, frame, message, interrupt, or function call.
- list the real command/API/register/ioctl order.
- modify a small piece of test data and observe the result.
- run a command and record command, phenomenon, and conclusion.
- compare logs under two settings.
- explain where an error would first appear.
- design the smallest diagnostic path.

Avoid making engineering chapters mostly:

- define this term.
- list generic advantages.
- explain from memory without touching the system.
- answer multiple choice questions unless the user asks for exam mode.
- establish a baseline, build a chain, form a closed loop, or construct capability without immediately saying the concrete command, file, code, log, or observation.

## Required Tests

For each engineering chapter, include at least one verification action when the source material supports it.

Examples:

- Build or status command.
- Start, stop, and port check.
- Browser Network observation.
- API call and returned data check.
- Database test data change.
- Device file or sysfs inspection.
- Media pipeline run.
- MQTT or message-bus publish/subscribe.
- Log comparison under different parameters.

If a real command is unavailable or unsafe, ask for a practical record instead: command to run, expected phenomenon, possible failure point, and what the learner should record.

## Stage Acceptance

Group chapters into 2 to 4 stages. Each stage should answer "what can the learner now do?"

Typical engineering stages:

1. Can explain the system and module responsibilities.
2. Can explain the main runtime/data/media/control path.
3. Can run and verify the system.
4. Can diagnose common failures.

Acceptance criteria should be observable, not vague.

Good criteria:

- Can trace one frontend page to its backend API.
- Can explain the exact buffer or message loop.
- Can start the environment, verify a stream, and stop it cleanly.
- Can diagnose no image, no heartbeat, no alarm, or failed API response.

## Final Task

End with one small task that takes no more than half a day.

The final task should force synthesis but not become a new project. Examples:

- Create `learning-notes.md` with architecture, main flow, and the most forgettable debugging points.
- Add a one-page runbook for start/stop/check/debug.
- Add a small diagnostic checklist for the most likely failure chain.

## Scoring And Progress

Hands-on tests can have points only when the learner can submit evidence: command output, screenshot description, log snippet, observed behavior, or written conclusion.

Do not award XP for vague confidence. Award XP for explicit answers, runnable checks, or recorded observations.
