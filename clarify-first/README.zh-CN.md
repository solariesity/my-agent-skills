# Clarify First

在需求不明确时，先问清楚再行动。

## 简介

`clarify-first` 是一个 Codex / Claude Code Skill。当用户请求含糊、不完整或留下重要决策未明确时，它会在开始实质性工作前暂停，把模糊的指令变成带字母选项的明确选择，并等待用户确认后再继续。

适用于任务可能有多种理解、范围不清、缺少关键输入，或措辞犹豫/矛盾的场景。

## 特性

- 自动识别含糊、不完整或开放性的请求。
- 用字母选项（`A`、`B`、`C` …… 以及 `Other`）呈现具体选择。
- 存在明显默认值时标记推荐选项。
- 用一句话说明每个选项的取舍。
- 持续澄清，直到所有阻塞性决策都明确为止。

## 安装

本 Skill 是 `my-agent-skills` monorepo 的一部分。安装时先将仓库克隆到临时目录，再只把真正起作用的部分复制到 Agent 的 skills 文件夹（不复制 README、测试等无关文件）。

```bash
# 1. 将整个 monorepo 克隆到临时目录
git clone git@github.com:solariesity/my-agent-skills.git /tmp/my-agent-skills

# 2. 在 Agent 的 skills 目录下创建本 Skill 的子目录
mkdir -p ~/.claude/skills/clarify-first
# 如果是 Codex，使用：
# mkdir -p ~/.codex/skills/clarify-first

# 3. 复制 Skill 的有效文件
cp /tmp/my-agent-skills/clarify-first/SKILL.md ~/.claude/skills/clarify-first/
cp -r /tmp/my-agent-skills/clarify-first/agents ~/.claude/skills/clarify-first/
```

```bash
# 4. 清理临时目录
rm -rf /tmp/my-agent-skills
```

重启 Agent 以使其被发现。

## 用法

显式调用 Skill：

```text
/clarify-first
```

或在提示中要求 Agent 使用它：

```text
开始前先用 $clarify-first。我想重构 auth 模块，但不确定是原地修改还是加 feature flag。
```

Agent 会在编辑文件或执行命令前停下来，先向你澄清问题。

## 目录结构

```text
clarify-first/
├── SKILL.md          # Skill 行为与澄清规则
├── README.md         # 英文文档
├── README.zh-CN.md   # 中文文档
└── agents/
    └── openai.yaml   # UI 元数据（显示名、默认提示词）
```

## 版本

本 Skill 与父仓库统一版本管理。当前版本见顶层 [`VERSION`](../VERSION) 文件。

## 贡献

欢迎提交 issue 或 pull request。贡献指南请参考[父仓库 README](../README.md#contributing)。
