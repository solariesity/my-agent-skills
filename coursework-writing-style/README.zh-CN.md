# coursework-writing-style

[English](README.md)

[![Version](https://img.shields.io/badge/version-v0.2.0-blue)](./VERSION)

> 面向课程作业的学生写作风格：清楚、朴实、规范。

此 skill 用于帮助学生完成课程作业、课程论文、实验报告、读书报告、课堂反思等学生提交物。它强调语言表达清楚、朴实、规范，避免过度修辞或不必要的“包装感”。不适用于发表级学术论文、创意写作、营销文案或社交媒体内容。

## 功能特性

- 面向课程作业的中文写作：朴实、严谨，避免花哨和网络流行语。
- 面向学生提交物的英文写作：简单自然，符合学生水平。
- 动笔前先对齐作业要求（题目、字数、格式、提交形式等）。
- 根据常见作业类型调整语气（课程论文、实验报告、读书报告、反思等）。
- 避免堆砌分点和八股式结尾。
- 保持客观平实的语气。
- 以中国大学生/研究生日常写作水平为准。

## 安装

本 Skill 是 `my-agent-skills` monorepo 的一部分。安装时先将仓库克隆到临时目录，再只把真正起作用的部分复制到 Agent 的 skills 文件夹（不复制 README、测试等无关文件）。

```bash
# 1. 将整个 monorepo 克隆到临时目录
git clone git@github.com:solariesity/my-agent-skills.git /tmp/my-agent-skills

# 2. 在 Agent 的 skills 目录下创建本 Skill 的子目录
mkdir -p ~/.claude/skills/coursework-writing-style
# 如果是 Codex，使用：
# mkdir -p ~/.codex/skills/coursework-writing-style

# 3. 复制 Skill 的有效文件
cp /tmp/my-agent-skills/coursework-writing-style/SKILL.md ~/.claude/skills/coursework-writing-style/
cp -r /tmp/my-agent-skills/coursework-writing-style/agents ~/.claude/skills/coursework-writing-style/
```

```bash
# 4. 清理临时目录
rm -rf /tmp/my-agent-skills
```

重启 Agent 以使其被发现。

## 使用方式

将 `SKILL.md` 加载到 Agent 环境中。当用户请求帮助完成课程作业或学生提交物时调用此 skill。不要用于发表级学术论文、创意写作、营销文案或社交媒体内容。

## 项目结构

```text
coursework-writing-style/
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

当前版本：[v0.2.0](VERSION)。

这是 1.0 之前的 skill，规则可能会随着更多课程作业写作场景的加入而细化。

## 贡献

欢迎提交 issue 或 pull request。贡献指南请参考[父仓库 README](../README.md#contributing)。
