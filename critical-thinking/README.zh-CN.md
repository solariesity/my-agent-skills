# critical-thinking

[English](README.md)

[![Version](https://img.shields.io/badge/version-v0.1.0-blue)](./VERSION)

> 主见与批判性思维，用于需要讨论、判断、分析的对话场景。

此 skill 用于 Agent 需要表达观点、评估主张或与用户讨论想法的场景。它定义了一种立场：有独立判断、基于事实论证、并在适当时提出异议。

## 功能特性

- 不盲从，形成自己的判断。
- 基于事实和可靠来源进行论证。
- 清晰说明推理过程。
- 对不合理或可能产生误导的要求提出异议。
- 保持谦逊，错了就承认并修正。

## 安装

这个 skill 存放在 [`my-agent-skills`](https://github.com/solariesity/my-agent-skills) 集合仓库中。克隆该仓库并进入 critical-thinking 目录：

```bash
git clone https://github.com/solariesity/my-agent-skills.git
cd my-agent-skills/critical-thinking
```

### 仅安装 Skill 部分

如果你只想把 critical-thinking 当作 skill 安装到 Agent 环境，可以使用临时克隆的方式：

```bash
# 1. 克隆集合仓库到临时目录
git clone https://github.com/solariesity/my-agent-skills.git /tmp/my-agent-skills

# 2. 只复制 skill 定义到目标位置
mkdir -p ~/.codex/skills/critical-thinking
cp /tmp/my-agent-skills/critical-thinking/SKILL.md ~/.codex/skills/critical-thinking/

# 3. 删除临时目录
rm -rf /tmp/my-agent-skills
```

Windows 上对应路径是 `C:\Users\<用户名>\.codex\skills\critical-thinking\`。

## 使用方式

将 `SKILL.md` 加载到 Agent 环境中。此 skill 会在讨论、分析、判断类任务中自动生效。仅在纯执行任务（如"把这个文件重命名为 X"）时可酌情跳过。

## 项目结构

```text
critical-thinking/
├── README.md
├── README.zh-CN.md
├── VERSION
└── SKILL.md
```

- `SKILL.md` — 核心行为定义。

## 版本说明

当前版本：[v0.1.0](VERSION)。

这是 1.0 之前的 skill，指引可能会随着使用模式的清晰而继续演进。

## 贡献

欢迎提出建议或提交 PR。
