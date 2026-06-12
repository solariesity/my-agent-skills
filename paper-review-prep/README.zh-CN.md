# paper-review-prep

[English](README.md)

[![Version](https://img.shields.io/badge/version-v0.1.0-blue)](./VERSION)

> 系统性文献分析与组会汇报准备。

此 skill 用于为组会或学术汇报准备文献分析。典型触发语包括："帮我梳理一篇文献"、"组会准备"、"文献分析"、"帮我读一篇论文"、"论文汇报准备"等。

## 功能特性

- 系统性地阅读和分析论文。
- 生成精炼的摘要。
- 用通俗语言解释论文。
- 提供正式的学术表述。
- 整理清晰的汇报大纲。

## 安装

本 Skill 是 `my-agent-skills` monorepo 的一部分。安装时先将仓库克隆到临时目录，再只把真正起作用的部分复制到 Agent 的 skills 文件夹（不复制 README、测试等无关文件）。

```bash
# 1. 将整个 monorepo 克隆到临时目录
git clone git@github.com:solariesity/my-agent-skills.git /tmp/my-agent-skills

# 2. 在 Agent 的 skills 目录下创建本 Skill 的子目录
mkdir -p ~/.claude/skills/paper-review-prep
# 如果是 Codex，使用：
# mkdir -p ~/.codex/skills/paper-review-prep

# 3. 复制 Skill 的有效文件
cp /tmp/my-agent-skills/paper-review-prep/SKILL.md ~/.claude/skills/paper-review-prep/
```

```bash
# 4. 清理临时目录
rm -rf /tmp/my-agent-skills
```

重启 Agent 以使其被发现。

## 使用方式

将 `SKILL.md` 加载到 Agent 环境中。当用户请求文献分析、文献梳理或组会汇报准备时，skill 会自动触发。

## 项目结构

```text
paper-review-prep/
├── README.md
├── README.zh-CN.md
├── VERSION
└── SKILL.md
```

- `SKILL.md` — 核心工作流程与输出格式定义。

## 版本说明

当前版本：[v0.1.0](VERSION)。

这是 1.0 之前的 skill，工作流程可能会根据不同的会议和汇报风格继续演进。

## 贡献

欢迎提出建议或提交 PR。
