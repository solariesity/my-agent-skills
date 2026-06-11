# FileRouter

[English](README.md)

版本：`0.2.0`

FileRouter 是一个给 Codex / agent 使用的文件路由 skill，用来把用户发来的文件、agent 自己生成的文件，以及用户明确要求保存的聊天内容，统一存进当前工作目录下的 `./files/` 结构里。

它主要解决这些问题：

- 文件应该存到哪里
- 是否需要自动创建子目录
- 用户上传的文件和 agent 生成的文件如何分开管理
- 聊天里明确说“很重要，存文件里”的内容怎么稳定追加保存
- 之前存过的文件后面怎么快速找回来

## 存储模型

FileRouter 默认把所有内容都存到：

```text
./files/
```

常见顶层目录包括：

```text
files/
  Archive/
  Courses/
  Dev/
  Docs/
  Downloads/
  Installers/
  Lab/
  Media/
  Research/
  Systems/
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
./files/Docs/Personal/提醒.md
```

如果这个文件已经存在，FileRouter 会把新内容追加进去，而不是覆盖原来的内容。

## 主要命令

统一入口：

```bash
python scripts/file_router_cli.py <command> ...
```

最常用的命令有：

- `intake`：处理用户在聊天里发来的文件
- `capture`：处理 agent 自己生成的文件
- `decide`：根据文件名和上下文猜测分类
- `route`：解析明确的目标路径
- `organize`：把文件复制或移动到目标位置
- `find`：查找之前已经存过的文件
- `remember-text`：把明确要求保存的聊天内容追加到 Markdown 笔记文件
- `scaffold`：创建工作区或项目骨架

## 常见用法

处理用户发来的文件：

```bash
python scripts/file_router_cli.py intake --source "C:\Temp\paper.pdf" --context "sea ice 项目的论文"
```

处理 agent 生成的结果文件：

```bash
python scripts/file_router_cli.py capture --source ".\figure.png" --project sea-ice-detection --project-type research --role output
```

保存一条重要聊天内容：

```bash
python scripts/file_router_cli.py remember-text --text "很重要，存在文件中吧：明天 9 点提醒我提交周报"
```

保存到自定义提醒文件：

```bash
python scripts/file_router_cli.py remember-text --text "save this: weekly sync agenda" --target-file "Lab/Tasks/weekly-sync.md" --section Inbox
```

创建本地 `files/` 骨架：

```bash
python scripts/file_router_cli.py scaffold --template workspace
```

查找已经存过的文件：

```bash
python scripts/file_router_cli.py find --query figure --domain research --project sea-ice-detection
```

## 仓库结构

```text
FileRouter/
  README.md
  README.zh-CN.md
  VERSION
  SKILL.md
  agents/
  references/
  scripts/
  tests/
```

## 校验

运行测试：

```bash
python -m unittest discover -s tests -v
```

校验 skill 结构：

```bash
python C:\Users\Lenovo\.codex\skills\.system\skill-creator\scripts\quick_validate.py .
```
