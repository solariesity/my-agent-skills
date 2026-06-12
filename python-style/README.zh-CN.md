# python-style

[English](README.md)

[![Version](https://img.shields.io/badge/version-v0.1.0-blue)](./VERSION)

> 面向研究和训练代码的行为保持型 Python 风格清理 skill。

当需要审查或规范化 Python 命名、模块或文件名、中文优先的注释与 docstring，以及稳定可解析的训练或调试输出时，使用此 skill。它会尽量在不影响外部契约的前提下完成清理。

## 功能特性

- 在不改变行为的前提下清理混用的命名规范。
- 规范模块和文件命名。
- 在项目允许的情况下，让注释和 docstring 以中文为主。
- 稳定训练日志和调试输出，方便下游解析。
- 将外部消费的名称和输出字段视为契约进行保护。

## 安装

本 Skill 是 `my-agent-skills` monorepo 的一部分。安装时先将仓库克隆到临时目录，再只把真正起作用的部分复制到 Agent 的 skills 文件夹（不复制 README、测试等无关文件）。

```bash
# 1. 将整个 monorepo 克隆到临时目录
git clone git@github.com:solariesity/my-agent-skills.git /tmp/my-agent-skills

# 2. 在 Agent 的 skills 目录下创建本 Skill 的子目录
mkdir -p ~/.claude/skills/python-style
# 如果是 Codex，使用：
# mkdir -p ~/.codex/skills/python-style

# 3. 复制 Skill 的有效文件
cp /tmp/my-agent-skills/python-style/SKILL.md ~/.claude/skills/python-style/
```

```bash
# 4. 清理临时目录
rm -rf /tmp/my-agent-skills
```

重启 Agent 以使其被发现。

## 使用方式

将 `SKILL.md` 加载到 Agent 环境中。当你在研究和训练代码场景下要求 Agent 审查、清理或规范化 Python 代码时，skill 会自动触发。

常见触发说法：

- "审查这个 Python 文件的风格问题。"
- "清理这个训练脚本里的命名。"
- "在不改逻辑的前提下，让训练日志更容易解析。"

## 项目结构

```text
python-style/
├── README.md
├── README.zh-CN.md
├── VERSION
└── SKILL.md
```

- `SKILL.md` — 核心行为定义与风格规则。

## 版本说明

当前版本：[v0.1.0](VERSION)。

这是 1.0 之前的 skill，规则可能会随着更多 Python 清理模式的发现而演进。

## 贡献

欢迎提出建议或提交 PR。
