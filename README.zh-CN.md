# My Agent Skills

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

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

每个 Skill 都是独立的目录。从下表选择你需要的 Skill，安装到 `~/.codex/skills/`：

```bash
# 1. 克隆到临时目录
git clone https://github.com/<your-username>/my-agent-skills.git /tmp/my-agent-skills

# 2. 复制你想要的 Skill
cp -r /tmp/my-agent-skills/<skill-name> ~/.codex/skills/<skill-name>

# 3. 删除临时克隆
rm -rf /tmp/my-agent-skills
```

| Skill | 目录 | 安装路径 |
|-------|------|----------|
| memory-router | [memory-router/](memory-router/) | `~/.codex/skills/memory-router` |
| file-router | [file-router/](file-router/) | `~/.codex/skills/file-router` |
| python-style-skill | [python-style-skill/](python-style-skill/) | `~/.codex/skills/python-style-skill` |
| github-readme-style | [github-readme-style/](github-readme-style/) | `~/.codex/skills/github-readme-style` |
| critical-thinking | [critical-thinking/](critical-thinking/) | `~/.codex/skills/critical-thinking` |
| paper-review-prep | [paper-review-prep/](paper-review-prep/) | `~/.codex/skills/paper-review-prep` |
| academic-writing-style | [academic-writing-style/](academic-writing-style/) | `~/.codex/skills/academic-writing-style` |

## 使用

安装完成后，目标 Agent 平台会自动从 `~/.codex/skills/<skill-name>/` 加载该 Skill。具体用法和示例请参考各 Skill 目录下的 `README.md`。

## 目录结构

```text
my-agent-skills/
├── README.md
├── README.zh-CN.md
├── VERSION
├── LICENSE
├── memory-router/            # 对话记忆路由
├── file-router/              # 文件和输出工作树路由
├── python-style-skill/       # 研究代码的 Python 风格约束
├── github-readme-style/      # README 规范化约定
├── critical-thinking/        # 独立思考与提出异议的约束
├── paper-review-prep/        # 论文阅读和组会汇报准备
└── academic-writing-style/   # 学术写作风格指南
```

## 版本

当前版本：v0.1.0

本项目遵循 [Semantic Versioning](https://semver.org/)。当前版本号见 [VERSION](VERSION)。

## 贡献

欢迎提交 issue 或 pull request，请在描述中清楚说明改动内容。

## 许可证

本项目采用 MIT License。详见 [LICENSE](LICENSE)。
