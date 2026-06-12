# Memory Router

[English](README.md)

[![Version](https://img.shields.io/badge/version-v0.5.1-blue)](./VERSION)

> 将对话记忆路由到确定性的 Markdown 文件，而不是全部丢进一个平铺的日志里。

memory-router 是一个面向 AI Agent 的 skill 与本地工具层，用于管理结构化、可检查、可回忆的记忆。它对候选信息进行分类，按用户、项目、类型、日期路由到可预测的文件路径，并在之后从同一路由范围回忆出来。

## 功能特性

- **decide**：判断一条候选信息是否值得持久化，以及应该如何保存。
- **inspect**：在写入前查看某类记忆会被路由到哪里。
- **remember**：将记忆条目写入路由后的 Markdown 文件，并支持安全去重。
- **recall**：从同一路由范围的子树中找回先前的记忆。
- 对常见中英文线索提供实用的启发式支持。
- 文件系统安全的 slug 规范化，同时保留 Unicode 项目名和用户名。

## 安装

本 Skill 是 `my-agent-skills` monorepo 的一部分。安装时先将仓库克隆到临时目录，再只把真正起作用的部分复制到 Agent 的 skills 文件夹（不复制 README、测试等无关文件）。

```bash
# 1. 将整个 monorepo 克隆到临时目录
git clone git@github.com:solariesity/my-agent-skills.git /tmp/my-agent-skills

# 2. 在 Agent 的 skills 目录下创建本 Skill 的子目录
mkdir -p ~/.claude/skills/memory-router
# 如果是 Codex，使用：
# mkdir -p ~/.codex/skills/memory-router

# 3. 复制 Skill 的有效文件
cp /tmp/my-agent-skills/memory-router/SKILL.md ~/.claude/skills/memory-router/
cp -r /tmp/my-agent-skills/memory-router/agents ~/.claude/skills/memory-router/
cp -r /tmp/my-agent-skills/memory-router/references ~/.claude/skills/memory-router/
cp -r /tmp/my-agent-skills/memory-router/scripts ~/.claude/skills/memory-router/
```

```bash
# 4. 清理临时目录
rm -rf /tmp/my-agent-skills
```

重启 Agent 以使其被发现。

## 使用方式

查看一条偏好记忆会被路由到哪里：

```bash
python scripts/memrouter_cli.py inspect \
  --memory-type preferences \
  --user-id alice
```

判断一条候选记忆是否值得保存：

```bash
python scripts/memrouter_cli.py decide \
  --user-id alice \
  --text "The user prefers concise Chinese answers."
```

使用 topic-aware upsert 存储记忆：

```bash
python scripts/memrouter_cli.py remember \
  --vault-root ./memories \
  --memory-type preferences \
  --user-id alice \
  --dedupe-mode topic \
  --topic output-style \
  --text "The user prefers concise Chinese answers."
```

回忆先前存储的记忆：

```bash
python scripts/memrouter_cli.py recall \
  --vault-root ./memories \
  --memory-type preferences \
  --user-id alice \
  --query "concise Chinese"
```

## 项目结构

```text
memory-router/
├── README.md
├── README.zh-CN.md
├── VERSION
├── .gitignore
├── SKILL.md
├── VERSION_RECORDS.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── entry-format.md
│   ├── memory-taxonomy.md
│   └── routing-policy.md
├── scripts/
│   ├── memrouter_cli.py
│   └── memrouter_core.py
└── tests/
```

- `SKILL.md` — 触发描述与 agent 集成时的使用指引。
- `agents/openai.yaml` — skill 市场所需的 UI 元数据。
- `references/` — entry 格式、记忆分类、路由策略的权威规则。
- `scripts/` — CLI 入口，以及路由、持久化、回忆、决策的核心逻辑。
- `tests/` — 覆盖路由、决策、去重、回忆、CLI 参数校验的单元测试。

## 记忆类型

memory-router 支持以下标准类型：

| 类型 | 用途 |
|------|------|
| `profile` | 用户身份、背景、长期目标等稳定事实 |
| `preferences` | 语言、风格、工具、工作流偏好 |
| `project-facts` | 项目约束、架构、集成、前提条件 |
| `project-decisions` | 项目中的明确决策与转向 |
| `task` | 待办、进度、下一步 |
| `session-summary` | 某次会话或工作过程的总结 |
| `ephemeral` | 低置信但暂时值得保留的短期记忆 |

完整边界和示例见 [references/memory-taxonomy.md](references/memory-taxonomy.md)。

## 路由模型

memory-router 按以下四个维度路由记忆：

- `memory_type`
- `user_id`
- `project`
- `date`

默认的 vault 相对根目录是 `memory-router/`。典型路径包括：

- `preferences` → `memory-router/users/<user_id>/preferences.md`
- `profile` → `memory-router/users/<user_id>/profile.md`
- `project-facts` → `memory-router/projects/<project_slug>/facts.md`
- `project-decisions` → `memory-router/projects/<project_slug>/decisions.md`
- `task` → 根据是否有项目作用域，进入项目任务文件或用户任务文件
- `session-summary` → 按日期写入项目或用户 sessions 下
- `ephemeral` → 按日期写入 inbox

路径名会被规范成文件系统安全的 slug，但会尽量保留安全的 Unicode 字母和数字，因此中文项目名不会再意外塌缩成同一个默认路径。

## 写入机制

每条记忆会写成如下紧凑的 Markdown 块：

```text
- 2026-06-05 | created_at: 2026-06-05T14:32:10+08:00 | topic: output-style | source: chat
  The user prefers concise Chinese answers.
```

当前写入规则：

- 多行内容会统一缩进，保证仍然是一条记忆。
- 每条记忆除了路由日期，还会记录精确的 `created_at` 时间戳。
- 默认去重模式是 `exact`。
- `exact` 会把“同 topic、同 source、同正文”的内容视为同一条记忆，即使日期不同。
- 如果你提供稳定的 `topic`，可以用 `topic` 模式做更新覆盖。
- `none` 模式始终追加。

精确格式和兼容规则见 [references/entry-format.md](references/entry-format.md)。

## 回忆机制

回忆时会复用写入时的同一路由逻辑：

1. 先查直达文件。
2. 如果没命中，再在同 scope 的子树里扩展搜索。

重要边界：项目记忆的 recall 不会再串到项目 `sessions/`，除非要回忆的类型本身就是 `session-summary`。

目前 recall 还是“文本匹配式”的，不是语义排序式的。

## 版本说明

当前版本：[v0.5.1](VERSION)。

memory-router 在精神上遵循语义化版本。`v0.5.1` 表示路由模型、写入语义、recall 边界和启发式决策层已经稳定到可以认真使用，但决策质量和 recall 质量在达到 `1.0.0` 之前仍有提升空间。

本地版本路线记录见 [VERSION_RECORDS.md](VERSION_RECORDS.md)。

## 测试

运行内置测试套件：

```bash
python -m unittest discover -s tests -v
```

当前测试覆盖：

- ASCII 与 Unicode 名称的路由解析
- 决策层的持久化判断与中英双语分类启发式
- 跨日期的 exact 去重
- 带时间戳的条目格式与“忽略时间戳”的 dedupe 行为
- topic-aware upsert
- 多行条目的格式稳定性
- recall 的作用域边界
- CLI 参数校验

## 当前限制

- 决策层目前还是启发式优先，还没有接入真正的模型辅助分类。
- 中文支持已经能覆盖常见场景，但本质上仍然是规则驱动，不是语义理解。
- recall 目前还是按文本匹配，不带语义排序和结果摘要。
- 仓库现在更偏“开发维护形态”，还不是极致精简的分发包形态。

## 贡献

欢迎提交 issue 或 pull request。贡献指南请参考[父仓库 README](../README.md#contributing)。

## 设计原则

- 不要什么都存。
- 写入和读取的规则必须对称。
- 长期记忆和临时上下文要分开。
- 路径要稳定、可预测。
- 兜底行为要显式，不要靠隐式魔法。
