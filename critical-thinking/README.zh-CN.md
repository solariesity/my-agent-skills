# critical-thinking

[English](README.md)

[![Version](https://img.shields.io/badge/version-v0.2.0-blue)](./VERSION)

> 主见与批判性思维，用于需要讨论、判断、分析的对话场景。

此 skill 用于 Agent 需要表达观点、评估主张或与用户讨论想法的场景。它定义了一种立场：有独立判断、基于事实论证、并在适当时提出异议。

## 功能特性

- 不盲从，形成自己的判断。
- 基于事实和可靠来源进行论证。
- 清晰说明推理过程。
- 表达观点或异议时标明置信度。
- 按结构化流程处理与用户的不一致。
- 尊重边界：对偏好、价值观和纯执行任务不强行反驳。
- 保持谦逊，错了就承认并修正。

## 安装

本 Skill 是 `my-agent-skills` monorepo 的一部分。安装时先将仓库克隆到临时目录，再只把真正起作用的部分复制到 Agent 的 skills 文件夹（不复制 README、测试等无关文件）。

```bash
# 1. 将整个 monorepo 克隆到临时目录
git clone git@github.com:solariesity/my-agent-skills.git /tmp/my-agent-skills

# 2. 在 Agent 的 skills 目录下创建本 Skill 的子目录
mkdir -p ~/.claude/skills/critical-thinking
# 如果是 Codex，使用：
# mkdir -p ~/.codex/skills/critical-thinking

# 3. 复制 Skill 的有效文件
cp /tmp/my-agent-skills/critical-thinking/SKILL.md ~/.claude/skills/critical-thinking/
cp -r /tmp/my-agent-skills/critical-thinking/agents ~/.claude/skills/critical-thinking/
```

```bash
# 4. 清理临时目录
rm -rf /tmp/my-agent-skills
```

重启 Agent 以使其被发现。

## 使用方式

将 `SKILL.md` 加载到 Agent 环境中。此 skill 会在讨论、分析、判断类任务中自动生效。仅在纯执行任务（如"把这个文件重命名为 X"）时可酌情跳过。

## 项目结构

```text
critical-thinking/
├── README.md
├── README.zh-CN.md
├── VERSION
├── SKILL.md
└── agents/
    └── openai.yaml
```

- `SKILL.md` — 核心行为定义。
- `agents/openai.yaml` — UI 元数据（显示名、默认提示词）。

## 版本说明

当前版本：[v0.2.0](VERSION)。

这是 1.0 之前的 skill，指引可能会随着使用模式的清晰而继续演进。

## 贡献

欢迎提出建议或提交 PR。
