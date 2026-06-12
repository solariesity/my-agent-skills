# My Agent Skills

统一的个人 AI Agent / Codex Skill 集合，用于确定性记忆路由、文件路由、代码风格约束以及任务型推理。

## 简介

本仓库将原先分散的 Skill 项目合并为一个单一仓库。每个 Skill 都位于独立的子目录中，可以单独安装到任何兼容 Codex / Claude Code 的环境中。

## 特性

- 统一管理所有个人 Agent Skill
- 每个 Skill 提供中英双语文档（`README.md` + `README.zh-CN.md`）
- 对对话、文件和生成输出进行确定性路由
- 面向研究和训练代码的 Python 风格指南
- 独立思考、论文阅读和学术写作辅助

## 安装

每个 Skill 的 README 中都有 **仅安装 Skill 部分** 的安装说明。选择你需要的 Skill，按对应 README 中的命令安装即可：

| Skill | README |
|-------|--------|
| memory-router | [README](memory-router/README.md) |
| file-router | [README](file-router/README.md) |
| python-style-skill | [README](python-style-skill/README.md) |
| github-readme-style | [README](github-readme-style/README.md) |
| critical-thinking | [README](critical-thinking/README.md) |
| paper-review-prep | [README](paper-review-prep/README.md) |
| academic-writing-style | [README](academic-writing-style/README.md) |

## 使用

安装完成后，目标 Agent 平台会自动从 `~/.codex/skills/<skill-name>/` 加载该 Skill。具体用法和示例请参考各 Skill 目录下的 `README.md`。

## 目录结构

```text
my-agent-skills/
├── README.md
├── README.zh-CN.md
├── memory-router/            # 对话记忆路由
├── file-router/              # 文件和输出工作树路由
├── python-style-skill/       # 研究代码的 Python 风格约束
├── github-readme-style/      # README 规范化约定
├── critical-thinking/        # 独立思考与提出异议的约束
├── paper-review-prep/        # 论文阅读和组会汇报准备
└── academic-writing-style/   # 学术写作风格指南
```

## 贡献

欢迎提交 issue 或 pull request，请在描述中清楚说明改动内容。
