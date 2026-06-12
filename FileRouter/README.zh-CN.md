# FileRouter

[English](README.md)

[![Version](https://img.shields.io/badge/version-v0.2.0-blue)](./VERSION)

> 将用户分享的文件、Agent 生成的文件，以及用户明确要求保存的聊天内容，统一存放到当前工作目录下的结构化 `files/` 树中。

FileRouter 是一个面向 Codex / Agent 的 skill 与本地 CLI 工具，帮助 Agent 决定文件该放哪里、自动创建工作区骨架、区分用户上传文件与 Agent 生成文件，并支持按作用域找回已存储的文件。

## 功能特性

- 按域、项目、课程、角色将文件路由到稳定的子目录。
- 在当前工作目录下自动创建缺失的文件夹。
- 区分用户上传附件与 Agent 生成结果。
- 将重要的聊天内容追加到提醒文件，而不是零散保存。
- 按作用域搜索之前路由过的文件。

## 安装

FileRouter 需要 Python 3.10 或更高版本。

这个 skill 存放在 [`my-agent-skills`](https://github.com/solariesity/my-agent-skills) 集合仓库中。克隆该仓库并进入 FileRouter 目录：

```bash
git clone https://github.com/solariesity/my-agent-skills.git
cd my-agent-skills/FileRouter
```

使用 CLI 不需要安装 Python 包。直接从 `scripts/` 目录运行命令：

```bash
python scripts/file_router_cli.py --help
```

### 仅安装 Skill 部分

如果你只想把 FileRouter 当作 skill 安装到 Agent 环境（不需要 `README`、`tests`、`VERSION` 等项目维护文件），可以使用临时克隆的方式：

```bash
# 1. 克隆集合仓库到临时目录
git clone https://github.com/solariesity/my-agent-skills.git /tmp/my-agent-skills

# 2. 只复制 skill 运行所需的核心文件到目标位置
mkdir -p ~/.codex/skills/FileRouter
cp -r /tmp/my-agent-skills/FileRouter/SKILL.md ~/.codex/skills/FileRouter/
cp -r /tmp/my-agent-skills/FileRouter/agents ~/.codex/skills/FileRouter/
cp -r /tmp/my-agent-skills/FileRouter/references ~/.codex/skills/FileRouter/
cp -r /tmp/my-agent-skills/FileRouter/scripts ~/.codex/skills/FileRouter/

# 3. 删除临时目录
rm -rf /tmp/my-agent-skills
```

Windows 上对应路径是 `C:\Users\<用户名>\.codex\skills\FileRouter\`。

## 使用方式

处理用户分享的文件：

```bash
python scripts/file_router_cli.py intake \
  --source "C:/Temp/paper.pdf" \
  --context "sea ice 项目的论文"
```

处理 Agent 生成的结果文件：

```bash
python scripts/file_router_cli.py capture \
  --source "./figure.png" \
  --project sea-ice-detection \
  --project-type research \
  --role output
```

保存一条重要聊天内容：

```bash
python scripts/file_router_cli.py remember-text \
  --text "很重要，存在文件中吧：明天 9 点提醒我提交周报"
```

保存到自定义提醒文件：

```bash
python scripts/file_router_cli.py remember-text \
  --text "save this: weekly sync agenda" \
  --target-file "Lab/Tasks/weekly-sync.md" \
  --section Inbox
```

创建本地 `files/` 骨架：

```bash
python scripts/file_router_cli.py scaffold --template workspace
```

查找已经存过的文件：

```bash
python scripts/file_router_cli.py find \
  --query figure \
  --domain research \
  --project sea-ice-detection
```

## 存储模型

FileRouter 默认把所有内容都存到：

```text
./files/
```

常见顶层目录包括：

```text
files/
├── Archive/
├── Courses/
├── Dev/
├── Docs/
├── Downloads/
├── Installers/
├── Lab/
├── Media/
├── Research/
└── Systems/
```

如果文件属于具体项目，还会继续路由到项目模板子目录，例如：

- 通用项目：`00_Inbox`、`01_Admin`、`02_Source`、`03_Work`、`04_Output`、`99_Archive`
- 科研项目：`01_Literature`、`02_Data/raw`、`02_Data/processed`、`03_Code`、`04_Experiments`、`05_Writing`、`06_Output`、`99_Archive`

## 聊天文本保存规则

FileRouter 不会默认把普通聊天内容自动写入文件。

只有当用户出现明确保存信号时，才建议调用 `remember-text`，例如：

- `很重要，存在文件中吧`
- `记一下，写进提醒里`
- `save this to file`
- `remember this`

默认保存位置是：

```text
./files/Docs/Personal/reminder.md
```

如果这个文件已经存在，FileRouter 会把新内容追加进去，而不是覆盖原来的内容。

## 项目结构

```text
FileRouter/
├── README.md
├── README.zh-CN.md
├── SKILL.md
├── VERSION
├── agents/
│   └── openai.yaml
├── references/
│   ├── agent-flow.md
│   ├── routing-policy.md
│   └── workspace-rules.md
├── scripts/
│   ├── file_router_cli.py
│   └── file_router_core.py
└── tests/
    └── test_file_router.py
```

- `SKILL.md` — 触发描述与 agent 集成时的使用指引。
- `agents/openai.yaml` — skill 市场所需的 UI 元数据。
- `references/` — agent 流程、路由策略、工作区规范的权威规则。
- `scripts/` — CLI 入口与核心路由逻辑。
- `tests/` — 文件路由行为的单元测试。

## 版本说明

当前版本：`v0.2.0`。

FileRouter 在精神上遵循语义化版本。`v0.2.0` 是 1.0 之前的版本，CLI 接口和路由策略可能会随着使用模式的清晰而继续演进。

## 测试

运行内置测试套件：

```bash
python -m unittest discover -s tests -v
```

## 贡献

欢迎提出建议或提交 PR。

## 主要命令

- `intake`：处理用户在聊天里发来的文件
- `capture`：处理 Agent 自己生成的文件
- `decide`：根据文件名和上下文猜测分类
- `route`：解析明确的目标路径
- `organize`：把文件复制或移动到目标位置
- `find`：查找之前已经存过的文件
- `remember-text`：把明确要求保存的聊天内容追加到 Markdown 笔记文件
- `scaffold`：创建工作区或项目骨架

详细的工作流程指引见 `SKILL.md` 和 `references/`。
