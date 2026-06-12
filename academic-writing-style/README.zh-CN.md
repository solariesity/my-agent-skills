# academic-writing-style

[English](README.md)

[![Version](https://img.shields.io/badge/version-v0.1.1-blue)](./VERSION)

> 朴实、严谨的学术与任务型写作风格。

此 skill 用于学术写作和任务型文本生成，例如作业、报告、课程论文等。它强调语言表达清楚、朴实、规范，避免过度修辞或不必要的“包装感”。

## 功能特性

- 中文学术写作：朴实、严谨，避免花哨和网络流行语。
- 英文学术写作：简单自然，优先使用 CET-4/CET-6 常用词。
- 避免堆砌分点和八股式结尾。
- 保持客观平实的语气。
- 以中国大学生/研究生日常写作水平为准。

## 安装

本 Skill 是 `my-agent-skills` monorepo 的一部分。安装时先将仓库克隆到临时目录，再只把真正起作用的部分复制到 Agent 的 skills 文件夹（不复制 README、测试等无关文件）。

```bash
# 1. 将整个 monorepo 克隆到临时目录
git clone git@github.com:solariesity/my-agent-skills.git /tmp/my-agent-skills

# 2. 在 Agent 的 skills 目录下创建本 Skill 的子目录
mkdir -p ~/.claude/skills/academic-writing-style
# 如果是 Codex，使用：
# mkdir -p ~/.codex/skills/academic-writing-style

# 3. 复制 Skill 的有效文件
cp /tmp/my-agent-skills/academic-writing-style/SKILL.md ~/.claude/skills/academic-writing-style/
cp -r /tmp/my-agent-skills/academic-writing-style/agents ~/.claude/skills/academic-writing-style/
```

```bash
# 4. 清理临时目录
rm -rf /tmp/my-agent-skills
```

重启 Agent 以使其被发现。

## 使用方式

将 `SKILL.md` 加载到 Agent 环境中。当用户请求学术写作或任务型文本时，skill 会自动触发。不要用于创意写作、营销文案或社交媒体内容。

## 项目结构

```text
academic-writing-style/
├── README.md
├── README.zh-CN.md
├── VERSION
├── SKILL.md
└── agents/
    └── openai.yaml
```

- `SKILL.md` — 核心风格规则与触发条件。
- `agents/openai.yaml` — Skill 列表与默认提示词的 UI 元数据。

## 版本说明

当前版本：[v0.1.1](VERSION)。

这是 1.0 之前的 skill，风格规则可能会随着更多写作场景的加入而细化。

## 贡献

欢迎提交 issue 或 pull request。贡献指南请参考[父仓库 README](../README.md#contributing)。
