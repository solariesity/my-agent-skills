# My Agent Skills

这个仓库汇总我自己编写和整理的 AI Agent / Codex Skill，方便统一管理和使用。

## 我的 Skills

| Skill | 目录 | 简介 |
|-------|------|------|
| **MemRouter** | [`MemRouter/`](MemRouter/) | 将对话记忆按类型、用户、项目、时间路由到确定性的 markdown 文件，支持决定、写入、回顾等能力。 |
| **FileRouter** | [`FileRouter/`](FileRouter/) | 将用户分享、Agent 生成或聊天中明确的备忘文本，按域/项目/角色存储到结构化的 `./files/` 工作树。 |
| **py-style-skill** | [`py-style-skill/`](py-style-skill/) | 针对研究和训练代码的 Python 风格清理约束：命名、注释、文件命名、稳定可解析的输出等。 |
| **github-readme-style** | [`github-readme-style/`](github-readme-style/) | 规范 GitHub 项目 README，默认输出中英双语，包含版本号、目录结构、安装使用等章节。 |
| **critical-thinking** | [`critical-thinking/`](critical-thinking/) | 讨论、分析、判断类任务中的独立思考约束，强调基于事实判断并在必要时提出异议。 |
| **paper-review** | [`paper-review/`](paper-review/) | 论文阅读、文献梳理和组会汇报准备，覆盖背景、方法、实验到汇报提纲整理。 |
| **writing-style** | [`writing-style/`](writing-style/) | 学术写作和任务型文本生成，强调清楚、朴实、规范，避免过度修辞。 |

## 推荐的外部 Skills / MCP Servers

下面是一些我觉得好用或值得参考的外部 Skill 与工具：

### Skills

#### andrej-karpathy-skills

- 项目地址：https://github.com/duolahypercho/andrej-karpathy-skills
- 简介：一个面向 Codex 的 Andrej Karpathy 风格编码规范 Skill，把“先思考、保持简单、只做必要改动、用可验证目标收尾”这类实践打包成可复用的 Skill 和插件，适合提升日常编码代理的稳定性与可控性。

### MCP Servers（工具类）

#### CodeGraph

- 类型：MCP Server（附带使用指引）
- 用途：给 AI Agent 提供代码知识图谱查询能力
- GitHub：https://github.com/colbymchenry/codegraph
- 一句话：把代码库变成可查询的图谱，减少 AI 探索成本 ~70%

## 目录结构

```text
my-agent-skills/
├── README.md
├── MemRouter/
├── FileRouter/
├── py-style-skill/
├── github-readme-style/
├── critical-thinking/
├── paper-review/
└── writing-style/
```

每个 Skill 目录内部通常包含 `SKILL.md` 作为核心定义文件；涉及代码实现的 Skill（MemRouter、FileRouter）还包括 `scripts/`、`tests/`、`references/` 等。

## 使用方式

根据你使用的 Agent 平台，将对应 Skill 目录（或其中的 `SKILL.md`）加载到系统中即可。具体安装/加载方式取决于你使用的 Codex / Claude Code / 其他 Agent 环境。
