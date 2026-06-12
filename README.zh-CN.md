# My Agent Skills

[![Version](https://img.shields.io/badge/version-v0.2.1-blue)](./VERSION)

统一的个人 AI Agent / Codex Skill 集合，用于确定性记忆路由、文件路由、代码风格约束以及任务型推理。

## 简介

本仓库将原先分散的 Skill 项目合并为一个单一仓库。每个 Skill 都位于独立的子目录中，可以单独安装到任何兼容 Codex / Claude Code 的环境中。

## 特性

- 统一管理所有个人 Agent Skill
- 每个 Skill 提供中英双语文档（`README.md` + `README.zh-CN.md`）
- 对对话、文件和生成输出进行确定性路由
- 面向研究和训练代码的 Python 风格指南
- 独立思考、论文阅读和课程作业写作辅助

## 我的 Skill

| Skill | README | 简介 |
|-------|--------|------|
| memory-router | [README](memory-router/README.md) | 按用户、项目、类型、日期将对话记忆路由到确定性的 Markdown 文件。 |
| file-router | [README](file-router/README.md) | 将用户文件和生成输出路由到结构化的 `./files/` 工作树。 |
| python-style | [README](python-style/README.md) | 面向研究和训练代码的行为保持型 Python 风格清理。 |
| github-readme-style | [README](github-readme-style/README.md) | 规范 GitHub README，包含中英双语、版本号和目录结构。 |
| critical-thinking | [README](critical-thinking/README.md) | 用于实质性对话的独立思考与批判性思维。 |
| coursework-writing-style | [README](coursework-writing-style/README.md) | 面向课程作业的学生写作风格：清楚、朴实、规范。 |
| clarify-first | [README](clarify-first/README.md) | 在需求不明确时先澄清再行动。 |
| paper-analyst-zh | [README](paper-analyst-zh/README.md) | 将英文计算机/工程论文翻译成中文，深度分析，并准备组会汇报材料。 |
| skill-review | [README](skill-review/README.md) | 指导评审和改进本 monorepo 中的 skill。 |

## 安装

每个 Skill 的 README 中都有 **仅安装 Skill 部分** 的安装说明。从上方表格选择你需要的 Skill，按对应 README 中的命令安装即可。

安装完成后，目标 Agent 平台会自动从 `~/.codex/skills/<skill-name>/` 加载该 Skill。具体用法和示例请参考各 Skill 目录下的 `README.md`。

## 目录结构

```text
my-agent-skills/
├── README.md
├── README.zh-CN.md
├── AGENTS.md                 # 本仓库的持久化约定
├── VERSION
├── .gitignore
├── memory-router/            # 对话记忆路由
├── file-router/              # 文件和输出工作树路由
├── python-style/       # 研究代码的 Python 风格约束
├── github-readme-style/      # README 规范化约定
├── critical-thinking/        # 独立思考与提出异议的约束

├── coursework-writing-style/   # 课程作业写作风格指南
├── clarify-first/            # 先澄清需求再行动
├── paper-analyst-zh/         # 英文学术论文中文翻译与深度分析
└── skill-review/             # 评审和改进本 monorepo 中的 skill
```

## 版本

当前版本：v0.2.1

本项目遵循 [Semantic Versioning](https://semver.org/)。当前版本号见 [VERSION](VERSION)。

## 推荐的外部 Skill 与工具

我觉得好用或值得参考的 Skill 与工具。

### Skills

| Skill | 项目地址 | 简介 |
|-------|----------|------|
| ljg-skills | https://github.com/lijigang/ljg-skills | lijigang 的个人 AI Agent Skill 集合。 |
| andrej-karpathy-skills | https://github.com/duolahypercho/andrej-karpathy-skills | 面向 Codex 的 Andrej Karpathy 风格编码规范 Skill，把“先思考、保持简单、只做必要改动、用可验证目标收尾”打包成可复用的 Skill，适合提升日常编码 Agent 的稳定性与可控性。 |

### MCP Servers（工具类）

| 工具 | 项目地址 | 简介 |
|------|----------|------|
| CodeGraph | https://github.com/colbymchenry/codegraph | 把代码库变成可查询的图谱，减少 AI 探索成本 ~70%。 |

## 贡献

欢迎提交 issue 或 pull request，请在描述中清楚说明改动内容。
