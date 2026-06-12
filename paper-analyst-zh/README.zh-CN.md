# Paper Analyst ZH

[![Version](https://img.shields.io/badge/version-v1.0.0-blue)](./VERSION)

把英文计算机与工程论文翻译成中文，并进行深度分析。同时支持组会汇报材料准备。

## 简介

`paper-analyst-zh` 是一个面向中文读者的 Codex / Claude Code Skill。当你想用中文理解英文计算机科学或工程类论文时，它会提供忠实全文翻译、非专业人士也能看懂的通俗解释、规范学术表述、对方法/实验/结果/优缺点/可复现性的专业深度分析，以及适用于组会汇报的结构化大纲。

如果来源是 PDF，该 Skill 会自动先交给 `pdf` Skill 处理。

## 特性

- 按章节对英文论文进行完整中文翻译。
- 为非专业读者提供通俗解释。
- 规范学术表述 —— 用正式中文学术语言重新呈现论文贡献。
- 从动机、方法、实验、消融实验到局限性进行专业分析。
- 结构化汇报大纲，适用于组会准备场景。
- 通过 `pdf` Skill 自动摄取 PDF 内容。
- 支持多种阅读模式：快速阅读、详细阅读（默认）、汇报准备、复现准备。
- 支持中文触发词：组会、文献汇报、帮我梳理这篇论文等。
- 默认生成两个文件：`paper.translation.zh.md` 和 `paper.analysis.zh.md`。

## 安装

本 Skill 是 `my-agent-skills` monorepo 的一部分。安装时先将仓库克隆到临时目录，再只把真正起作用的部分复制到 Agent 的 skills 文件夹（不复制 README、测试等无关文件）。

```bash
# 1. 将整个 monorepo 克隆到临时目录
git clone git@github.com:solariesity/my-agent-skills.git /tmp/my-agent-skills

# 2. 在 Agent 的 skills 目录下创建本 Skill 的子目录
mkdir -p ~/.claude/skills/paper-analyst-zh
# 如果是 Codex，使用：
# mkdir -p ~/.codex/skills/paper-analyst-zh

# 3. 复制 Skill 的有效文件
cp /tmp/my-agent-skills/paper-analyst-zh/SKILL.md ~/.claude/skills/paper-analyst-zh/
cp -r /tmp/my-agent-skills/paper-analyst-zh/agents ~/.claude/skills/paper-analyst-zh/
cp -r /tmp/my-agent-skills/paper-analyst-zh/references ~/.claude/skills/paper-analyst-zh/
```

```bash
# 4. 清理临时目录
rm -rf /tmp/my-agent-skills
```

重启 Agent 以使其被发现。

## 用法

显式调用 Skill：

```text
/paper-analyst-zh
```

或直接让 Agent 使用它：

```text
用 $paper-analyst-zh 把这篇英文论文翻译成中文并分析。
```

组会准备场景：

```text
帮我梳理这篇论文，准备组会汇报。
```

### 阅读模式

支持四种阅读模式，根据你的目标自动调整分析深度：

| 模式 | 适用场景 | 翻译 | 分析侧重 |
|------|----------|:--:|------|
| **快速阅读** | 快速判断论文是否值得精读 | 完整 | 分析文件缩短，只留快照和关键结论 |
| **详细阅读**（默认） | 认真读懂一篇论文 | 完整 | 全部 9 层输出：快照、翻译、通俗解释、规范表述、专业分析、汇报大纲、个人启发、局限性、术语表 |
| **汇报准备** | 组会要讲这篇论文 | 完整 | 贡献亮点、Δ vs SOTA、听众可能问的问题、详细大纲（含口播要点和时间分配）、个人启发 |
| **复现准备** | 想复现论文结果 | 完整 | 实现细节、论文未写清的设置、实验风险、哪些地方可能复现不出来 |

给定本地 PDF 时，Skill 会先提取内容，然后生成：

- `paper.translation.zh.md` —— 完整中文翻译。
- `paper.analysis.zh.md` —— 论文概览、通俗解释、规范学术表述、专业分析、汇报大纲（如适用）、个人启发、局限性和术语表。

## 目录结构

```text
paper-analyst-zh/
├── SKILL.md              # Skill 行为与工作流
├── README.md             # 英文文档
├── README.zh-CN.md       # 中文文档
├── VERSION               # 当前版本
├── .gitignore
├── agents/
│   └── openai.yaml       # UI 元数据（显示名、默认提示词）
└── references/
    └── analysis-checklist.md  # 实验分析检查清单
```

## 版本

当前版本：[v1.0.0](VERSION)。

本 Skill 与父仓库统一版本管理。

## 贡献

欢迎提交 issue 或 pull request。贡献指南请参考[父仓库 README](../README.md#contributing)。
