# skill-review

[English](README.md)

[![Version](https://img.shields.io/badge/version-v1.0.0-blue)](./VERSION)

> 指导评审和改进 my-agent-skills monorepo 中的 skill。

`skill-review` 是一个 Codex / Claude Code Skill，用于评审本仓库中的其它 skill。当用户要求评价某个 skill 时，它会加载目标 skill 的文件，检查是否符合仓库约定，对比类似的社区 skill，提出具体改进建议，并在获得用户确认后协助实现、更新版本号并 push。

## 功能特性

- 加载并检查目标 skill 的文件（`SKILL.md`、README、`VERSION`、`agents/openai.yaml`、`.gitignore`）。
- 检查常见的约定违规和明显问题。
- 在 GitHub 上搜索可比的社区 skill。
- 以「优点 / 问题 / 优化建议 / 来源链接」的形式呈现评审结果。
- 遵循审批工作流：评审 → 询问 → 实现 → 询问版本号 → push。

## 安装

本 Skill 是 `my-agent-skills` monorepo 的一部分。安装时先将仓库克隆到临时目录，再只把真正起作用的部分复制到 Agent 的 skills 文件夹（不复制 README、测试等无关文件）。

```bash
# 1. 将整个 monorepo 克隆到临时目录
git clone git@github.com:solariesity/my-agent-skills.git /tmp/my-agent-skills

# 2. 在 Agent 的 skills 目录下创建本 Skill 的子目录
mkdir -p ~/.claude/skills/skill-review
# 如果是 Codex，使用：
# mkdir -p ~/.codex/skills/skill-review

# 3. 复制 Skill 的有效文件
cp /tmp/my-agent-skills/skill-review/SKILL.md ~/.claude/skills/skill-review/
cp -r /tmp/my-agent-skills/skill-review/agents ~/.claude/skills/skill-review/
```

```bash
# 4. 清理临时目录
rm -rf /tmp/my-agent-skills
```

重启 Agent 以使其被发现。

## 使用方式

将 `SKILL.md` 加载到 Agent 环境中。当用户要求评审、评价或改进本 monorepo 中的某个 skill 时调用：

```text
Use $skill-review to evaluate the file-router skill.
```

Agent 会检查该 skill、对比社区类似 skill、给出评审结果，并在修改前询问用户。

## 目录结构

```text
skill-review/
├── README.md
├── README.zh-CN.md
├── VERSION
├── .gitignore
├── SKILL.md
└── agents/
    └── openai.yaml
```

- `SKILL.md` — 评审工作流与检查清单。
- `agents/openai.yaml` — UI 元数据（显示名、默认提示词）。

## 版本说明

当前版本：[v1.0.0](VERSION)。

这是 1.0 之前的 skill，评审工作流可能会随着 monorepo 的增长而继续细化。

## 贡献

欢迎提交 issue 或 pull request。贡献指南请参考[父仓库 README](../README.md#contributing)。

## 许可证

本项目基于 [MIT License](../LICENSE) 发布。
