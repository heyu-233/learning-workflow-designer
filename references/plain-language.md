# Plain-Language Exercise Writing

Use this reference for every learner-facing output: learning mode, project-lab mode, review mode, practice mode, exam mode, critique, and platform adapters.

The learner is a human, not an issue tracker. Write like a teacher preparing a paper or lab sheet for a student.

## Core Rule

Every exercise must clearly answer:

1. What should I do?
2. How should I do it?
3. Why am I doing it? Include this when the reason is not obvious.
4. What counts as finished?
5. Where should I write my answer or record evidence?

If the learner cannot start the task after reading the prompt, rewrite it.

## Title Rule

Exercise titles must be concrete action sentences, not abstract labels.

Bad:

- 建立板端环境基线
- 完成驱动链路认知
- 构建 I2C 子系统能力节点
- 验证网络通信基础设施

Good:

- 确认板子能联网、能登录、能运行基本命令
- 找到应用程序调用驱动时经过的 3 个关键函数
- 写一个最小 I2C 读写测试，并记录读到的数据
- 让 3 个客户端连上服务器，并截图或记录日志证明连接成功

## Wording Rules

- Prefer everyday verbs: 看、找、运行、记录、改、写、比较、解释、排查、提交.
- Use technical terms only when the learner needs to learn that term. Explain it the first time.
- Avoid noun-heavy headings and slogans.
- Do not use vague phrases such as `完成认知`, `建立基线`, `形成闭环`, `打通链路`, `构建能力`, `沉淀经验`, `掌握机制` unless immediately translated into concrete actions.
- Replace abstract nouns with observable actions.
- Keep one sentence to one job when possible.

## Required Shape

Use this shape for normal exercises:

```md
### 题 X：用一句人话说明这题要做什么（N 分）

这一步要做什么：
...

怎么做：
1. ...
2. ...
3. ...

为什么这样做：
...

做到什么算完成：
- ...

答：
```

For engineering and project-lab tasks:

```md
### 任务 X：用一句人话说明这一步要完成什么（N 分）

这一步要做什么：
...

怎么做：
1. 先看/先查：...
2. 再修改/新建：...
3. 然后运行/观察：...

为什么这样做：
...

做到什么算完成：
- ...

如果失败，先查：
1. ...
2. ...
3. ...

填写区：
- 我看了哪些文件/命令：
- 我改了什么：
- 我运行了什么：
- 我看到了什么现象：
- 我判断是否完成的依据：
- 我的具体卡点：写清楚卡在哪个概念/文件/现象，以及已经尝试过什么
```

For exam mode, keep hints limited but still make the task understandable:

```md
### 题 X：判断这个调用顺序哪里错了（N 分）

题目：
下面这段调用顺序有一处错误。请指出错误位置，写出正确顺序，并说明如果按错误顺序运行会出现什么现象。

答：
```

## Rewrite Examples

Bad:

```md
目标：确认网络、串口、工具链、内核版本和板端用户程序链路。
```

Better:

```md
这一步要做什么：
确认你可以连上板子，能看到板子的 Linux 版本，能用交叉编译器编出一个最小程序，并能把程序放到板子上运行。

为什么这样做：
后面的 GPIO、I2C、SPI 和 TCP 实验都依赖这几件事。如果这里没通，后面的错误很可能不是代码问题，而是连接、工具链或运行环境问题。
```

Bad:

```md
实现/修改：
- 建立 linux_lab/env.md。
- 新建 linux_lab/user/hello.c。
```

Better:

```md
怎么做：
1. 新建 `linux_lab/env.md`，把板子的 IP、登录方式、Linux 版本、交叉编译器版本写进去。
2. 新建 `linux_lab/user/hello.c`，写一个只打印 `hello board` 的 C 程序。
3. 用交叉编译器编译它，把生成的程序传到板子上运行。
```

## Final Check

Before finalizing any question document, scan every title and every task block:

- Can a student tell exactly what to do?
- Is there at least one concrete action?
- Is the reason explained when the task looks mechanical?
- Is the completion standard observable?
- Is answer space present?
