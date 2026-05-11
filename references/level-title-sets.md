# Level Title Sets

Use this reference when rendering or designing `skill-tree.html` progress labels.

## Rule

Default learning packages use 5 levels. Give each level a short game-like title so progress feels more like a journey than a numeric score.

If the user does not specify a title style, prefer `classic`. For a small amount of surprise, the renderer may deterministically choose one of the other four built-in sets for roughly 20% of projects. The selection must be stable for the same `project_name` and `source_summary`; do not use true randomness during rendering.

If the learner or package needs a fixed style, set `level_title_set` in `learning-progress.json`.

If a project needs custom names, set `level_titles` to a 5-item list in `learning-progress.json`; this overrides `level_title_set`.

## Built-in Sets

### classic

1. 新手
2. 初学者
3. 进阶者
4. 熟练者
5. 掌握者

### sao

1. 起始镇新手
2. 单手剑练习者
3. 攻略组成员
4. 前线独行者
5. 黑衣剑士

### eu4

1. 边陲伯国
2. 区域强权
3. 王国中坚
4. 列强候选
5. 世界霸权

### hoi4

1. 新兵训练营
2. 前线参谋
3. 集团军指挥官
4. 战区统帅
5. 最高统帅部

### civ6

1. 开拓者
2. 建城者
3. 城邦盟友
4. 文明领袖
5. 时代缔造者

## Tone Guidance

- Keep titles short enough to fit in the HUD and level table.
- Use titles as flavor, not as grading language. XP and exercises remain the source of truth.
- Do not change earned XP, thresholds, or node states just because a title sounds advanced.
- Avoid adding more than one title system to the same page; the selected set should feel coherent.
