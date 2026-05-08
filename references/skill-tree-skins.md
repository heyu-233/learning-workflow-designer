# Skill Tree Skins

Use a skin when the source material clearly belongs to a project style, or when the user asks for a visual tone.

## Available Skins

- `engineering`: embedded systems, infrastructure, backend services, robotics, hardware/software integration.
- `course`: course notes, textbooks, tutorials, classroom-style learning.
- `paper`: research papers, theses, experiment reports, literature reading.

## Selection Rules

- Use `engineering` for codebases with modules, drivers, APIs, tasks, queues, protocols, or debugging flows.
- Use `course` for chaptered educational material where the learner mainly needs concept progression and review.
- Use `paper` for academic materials where the learner needs problem framing, method, experiments, limitations, and writing/defense.
- If unsure, keep the default skin.

## Render Command

```powershell
python scripts/render_skill_tree.py learning-progress.json skill-tree.html --skin engineering
```

## Skin Traits

### Engineering

- Dark console-like surface.
- Cyan and green accents.
- Strong status badges and module-like node cards.
- Good for FreeRTOS, Linux drivers, networking, IoT, compilers, and service architecture.

### Course

- Light, readable surface.
- Blue and amber accents.
- Chapter progress should be easy to scan.
- Good for tutorials, textbooks, and structured class notes.

### Paper

- Quiet editorial surface.
- Ink, violet, and warm highlight accents.
- Nodes should read like research capabilities: framing, method, experiments, analysis, critique, and presentation.

## Content Reminder

The skin changes presentation only. It must not change point rules, exercise scoring, or node state.
