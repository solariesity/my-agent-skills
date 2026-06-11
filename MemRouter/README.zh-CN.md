# MemRouter

[English](README.md)

> 一个把对话记忆路由到确定性 Markdown 文件中的 skill 与本地工具层。

当前版本：`v0.5.0`

MemRouter 适合需要“结构化记忆”的 AI Agent。它的目标是让记忆：

- 不再堆进一个平铺的大文件
- 能按用户、项目、类型、时间隔离
- 可以被人类直接检查
- 能从可预测的路径中再次找回

## 它能做什么

MemRouter 现在提供四个实用能力：

1. `decide`：先判断一条候选信息是否值得保存，以及应该怎么保存。
2. `inspect`：查看某类记忆会被路由到哪里。
3. `remember`：把记忆写入对应的 Markdown 文件。
4. `recall`：按同一路由范围把以前的记忆找回来。

它的主流程是：

1. 判断是否值得持久化
2. 归类到某种记忆类型
3. 路由到正确路径
4. 用安全的去重策略写入
5. 之后再从同一范围回忆出来

## 版本说明

这个仓库当前按 `v0.5.0` 说明。

- `v0.5.0` 表示：路由模型、写入语义、recall 边界、启发式决策层已经稳定到可以认真使用
- `v0.5.0` 在既有 taxonomy 和敏感信息护栏基础上，新增了旧 memory 首次迁移规则、旧 `MEMORY.md` 接管方式，以及 MemRouter 作为唯一长期记忆来源的明确规范
- 它还不是 `1.0.0`，因为决策质量和 recall 质量还有明显可提升空间

维护者本地使用的版本路线记录放在 `VERSION_RECORDS.md`。

## 仓库结构

这个仓库本质上就是 skill 本体：

- [SKILL.md](SKILL.md)：触发描述与使用指令
- [agents/openai.yaml](agents/openai.yaml)：UI 元数据
- [references/entry-format.md](references/entry-format.md)：标准记忆条目头与时间戳规则
- [references/memory-taxonomy.md](references/memory-taxonomy.md)：记忆分类规则
- [references/routing-policy.md](references/routing-policy.md)：路径与检索规则
- [scripts/memrouter_core.py](scripts/memrouter_core.py)：核心路由、写入、回忆、决策逻辑
- [scripts/memrouter_cli.py](scripts/memrouter_cli.py)：命令行入口
- [RELEASE_GUIDE.md](RELEASE_GUIDE.md)：推荐的 release 打包内容与检查清单

## 记忆类型

目前支持这些标准类型：

- `profile`：用户身份、背景、长期目标等稳定事实
- `preferences`：语言、风格、工具、工作流偏好
- `project-facts`：项目约束、架构、集成、前提条件
- `project-decisions`：项目中的明确决策与转向
- `task`：待办、进度、下一步
- `session-summary`：某次会话或工作过程的总结
- `ephemeral`：低置信但暂时值得保留的短期记忆

完整边界和示例见 [references/memory-taxonomy.md](references/memory-taxonomy.md)。

## 路由模型

MemRouter 按这四个维度路由：

- `memory_type`
- `user_id`
- `project`
- `date`

默认根目录是：

```text
MemRouter/
```

典型路径包括：

- `preferences` -> `MemRouter/users/<user_id>/preferences.md`
- `profile` -> `MemRouter/users/<user_id>/profile.md`
- `project-facts` -> `MemRouter/projects/<project_slug>/facts.md`
- `project-decisions` -> `MemRouter/projects/<project_slug>/decisions.md`
- `task` -> 有项目时进项目任务文件，没有则进用户任务文件
- `session-summary` -> 按日期写到项目或用户 sessions 下
- `ephemeral` -> 按日期写到 inbox

路径名会被规范成文件系统安全的 slug，但会尽量保留安全的 Unicode 字母和数字，所以中文项目名不会再意外塌缩成同一个默认路径。

## 写入机制

每条记忆会写成这样的 Markdown 块：

```text
- 2026-06-05 | created_at: 2026-06-05T14:32:10+08:00 | topic: output-style | source: chat
  The user prefers concise Chinese answers.
```

当前写入规则：

- 多行内容会统一缩进，保证仍然是一条记忆
- 现在每条记忆除了路由日期，还会记录精确的 `created_at` 时间戳
- 默认去重模式是 `exact`
- `exact` 会把“同 topic、同 source、同正文”的内容视为同一条记忆，即使日期或时间戳不同
- 如果你提供稳定 `topic`，可以用 `topic` 模式做更新覆盖
- `none` 模式则始终追加

精确格式和兼容规则见 [references/entry-format.md](references/entry-format.md)。

## 回忆机制

回忆时会复用写入时的同一路由逻辑：

1. 先查直达文件
2. 如果没命中，再在同 scope 的子树里扩展搜索

当前的重要边界：

- 项目记忆的 recall 不会再串到项目 `sessions/`，除非要回忆的类型本身就是 `session-summary`

目前 recall 还是“文本匹配式”的，不是语义排序式的。

## 快速开始

查看一条记忆会被路由到哪里：

```bash
python scripts/memrouter_cli.py inspect --memory-type preferences --user-id alice
```

先判断一条候选记忆是否值得保存：

```bash
python scripts/memrouter_cli.py decide --user-id alice --text "The user prefers concise Chinese answers."
```

用显式 topic-aware upsert 写入记忆：

```bash
python scripts/memrouter_cli.py remember --vault-root <vault-root> --memory-type preferences --user-id alice --dedupe-mode topic --topic output-style --text "The user prefers concise Chinese answers."
```

回忆记忆：

```bash
python scripts/memrouter_cli.py recall --vault-root <vault-root> --memory-type preferences --user-id alice --query "concise Chinese"
```

## CLI 命令

`inspect`

- 不写入，不检索
- 只负责解析路由路径

`decide`

- 判断一条信息该不该存
- 返回 `should_persist`、`memory_type`、`topic`、`dedupe_mode`、`confidence`、`reason`
- 当前是启发式决策层，不是模型驱动的正式分类器
- 已支持常见的中英文线索，能处理一部分中文语气词、偏好表达、任务表达和 topic 归纳

`remember`

- 把记忆写入路由后的文件
- 支持 `none`、`exact`、`topic` 三种去重模式
- 支持可选的 `--created-at`，用于显式传入 ISO 8601 时间戳

`recall`

- 先查直达 note
- 再只在同一路由范围里扩展搜索

## 测试

运行内置测试：

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

- 决策层目前还是启发式优先，还没有接入真正的模型辅助分类
- 中文支持已经能覆盖常见场景，但本质上仍然是规则驱动，不是语义理解
- recall 目前还是按文本匹配，不带语义排序和结果摘要
- 仓库现在更偏“开发维护形态”，还不是极致精简的分发包形态

## 设计原则

- 不要什么都存
- 写入和读取的规则必须对称
- 长期记忆和临时上下文要分开
- 路径要稳定、可预测
- 兜底行为要显式，不要靠隐式魔法
