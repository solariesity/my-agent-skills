# GitHub README Style

[English](README.md) · 中文

[![Version](https://img.shields.io/badge/version-v1.0.0-blue)](./VERSION)

一个用于规范化 GitHub README 的 Codex / Claude Code Skill。

## 简介

`github-readme-style` 是一个 Codex / Claude Code Skill，用于为 GitHub 项目强制执行一致的双语 README 结构。调用时，它会生成或审阅英文版 `README.md` 和简体中文版 `README.zh-CN.md`，两者覆盖相同内容并遵循相同的逻辑结构。

适用于为新项目创建 README、为现有项目添加中文翻译，或审阅和规范化现有 README。

## 特性

- 默认输出双语 README（`README.md` + `README.zh-CN.md`）。
- 规定章节顺序与内容规则。
- 版本号格式与徽章规范。
- 目录树规则。
- 安装与用法示例模板。
- README 审阅检查清单。

## 安装

本 Skill 是 `my-agent-skills` monorepo 的一部分。安装时先将仓库克隆到临时目录，再只把真正起作用的部分复制到 Agent 的 skills 文件夹（不复制 README、测试等无关文件）。

```bash
# 1. 将整个 monorepo 克隆到临时目录
git clone git@github.com:solariesity/my-agent-skills.git /tmp/my-agent-skills

# 2. 在 Agent 的 skills 目录下创建本 Skill 的子目录
mkdir -p ~/.claude/skills/github-readme-style
# 如果是 Codex，使用：
# mkdir -p ~/.codex/skills/github-readme-style

# 3. 复制 Skill 的有效文件
cp /tmp/my-agent-skills/github-readme-style/SKILL.md ~/.claude/skills/github-readme-style/
cp -r /tmp/my-agent-skills/github-readme-style/agents ~/.claude/skills/github-readme-style/
```

```bash
# 4. 清理临时目录
rm -rf /tmp/my-agent-skills
```

重启 Agent 以使其被发现。

## 用法

显式调用 Skill：

```text
/github-readme-style
```

或在提示中要求 Agent 使用它：

```text
用 $github-readme-style 给这个项目写个 README。
```

常见请求：

- "给这个项目写个 README。"
- "审阅并规范化 README。"
- "添加中文 README。"

## 目录结构

```text
github-readme-style/
├── README.md              # 英文文档
├── README.zh-CN.md        # 简体中文文档
├── VERSION                # 当前版本
├── SKILL.md               # Skill 行为说明
└── agents/
    └── openai.yaml        # UI 元数据（显示名、默认提示词）
```

## 版本

当前版本：[v1.0.0](VERSION)。

本 Skill 遵循 [Semantic Versioning](https://semver.org/)。`VERSION` 文件是版本号的唯一来源。

## 贡献

欢迎提交 issue 或 pull request。贡献指南请参考[父仓库 README](../README.md#contributing)。

## 许可证

许可证信息请参见[父仓库](../README.md)。

## 许可证

本项目基于 [MIT License](../LICENSE) 发布。
