# paper-review-prep

[English](README.md)

> 系统性文献分析与组会汇报准备。

此 skill 用于为组会或学术汇报准备文献分析。典型触发语包括："帮我梳理一篇文献"、"组会准备"、"文献分析"、"帮我读一篇论文"、"论文汇报准备"等。

## 功能特性

- 系统性地阅读和分析论文。
- 生成精炼的摘要。
- 用通俗语言解释论文。
- 提供正式的学术表述。
- 整理清晰的汇报大纲。

## 安装

这个 skill 存放在 [`my-agent-skills`](https://github.com/solariesity/my-agent-skills) 集合仓库中。克隆该仓库并进入 paper-review-prep 目录：

```bash
git clone https://github.com/solariesity/my-agent-skills.git
cd my-agent-skills/paper-review-prep
```

### 仅安装 Skill 部分

如果你只想把 paper-review-prep 当作 skill 安装到 Agent 环境，可以使用临时克隆的方式：

```bash
# 1. 克隆集合仓库到临时目录
git clone https://github.com/solariesity/my-agent-skills.git /tmp/my-agent-skills

# 2. 只复制 skill 定义到目标位置
mkdir -p ~/.codex/skills/paper-review-prep
cp /tmp/my-agent-skills/paper-review-prep/SKILL.md ~/.codex/skills/paper-review-prep/

# 3. 删除临时目录
rm -rf /tmp/my-agent-skills
```

Windows 上对应路径是 `C:\Users\<用户名>\.codex\skills\paper-review-prep\`。

## 使用方式

将 `SKILL.md` 加载到 Agent 环境中。当用户请求文献分析、文献梳理或组会汇报准备时，skill 会自动触发。

## 项目结构

```text
paper-review-prep/
├── README.md
├── README.zh-CN.md
└── SKILL.md
```

- `SKILL.md` — 核心工作流程与输出格式定义。

## 版本说明

当前版本：`v0.1.0`。

这是 1.0 之前的 skill，工作流程可能会根据不同的会议和汇报风格继续演进。

## 贡献

欢迎提出建议或提交 PR。
