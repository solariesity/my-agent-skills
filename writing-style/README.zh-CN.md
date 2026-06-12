# writing-style

[English](README.md)

> 朴实、严谨的学术与任务型写作风格。

此 skill 用于学术写作和任务型文本生成，例如作业、报告、课程论文等。它强调语言表达清楚、朴实、规范，避免过度修辞或不必要的“包装感”。

## 功能特性

- 中文学术写作：朴实、严谨，避免花哨和网络流行语。
- 英文学术写作：简单自然，优先使用 CET-4/CET-6 常用词。
- 避免堆砌分点和八股式结尾。
- 保持客观平实的语气。
- 以中国大学生/研究生日常写作水平为准。

## 安装

这个 skill 存放在 [`my-agent-skills`](https://github.com/solariesity/my-agent-skills) 集合仓库中。克隆该仓库并进入 writing-style 目录：

```bash
git clone https://github.com/solariesity/my-agent-skills.git
cd my-agent-skills/writing-style
```

### 仅安装 Skill 部分

如果你只想把 writing-style 当作 skill 安装到 Agent 环境，可以使用临时克隆的方式：

```bash
# 1. 克隆集合仓库到临时目录
git clone https://github.com/solariesity/my-agent-skills.git /tmp/my-agent-skills

# 2. 只复制 skill 定义到目标位置
mkdir -p ~/.codex/skills/writing-style
cp /tmp/my-agent-skills/writing-style/SKILL.md ~/.codex/skills/writing-style/

# 3. 删除临时目录
rm -rf /tmp/my-agent-skills
```

Windows 上对应路径是 `C:\Users\<用户名>\.codex\skills\writing-style\`。

## 使用方式

将 `SKILL.md` 加载到 Agent 环境中。当用户请求学术写作或任务型文本时，skill 会自动触发。不要用于创意写作、营销文案或社交媒体内容。

## 项目结构

```text
writing-style/
├── README.md
├── README.zh-CN.md
└── SKILL.md
```

- `SKILL.md` — 核心风格规则与触发条件。

## 版本说明

当前版本：`v0.1.0`。

这是 1.0 之前的 skill，风格规则可能会随着更多写作场景的加入而细化。

## 贡献

欢迎提出建议或提交 PR。
