---
name: file-router
description: Route user-shared files, agent-created artifacts, and explicitly saved important chat notes into a structured `files/` tree inside the current working directory. Use when Codex needs to decide where a file should live, scaffold workspace or project folders, store incoming attachments or generated outputs safely, append important chat text into reminder notes, normalize names, or find previously routed files again by domain, project, course, or artifact role.
---

# File Router

Use this skill when file storage should follow stable workspace rules instead of ad hoc folders.
By default, file-router creates and uses a `files/` directory under the current working directory.

Prefer it when:

- the user shares files in chat and they need a proper long-term location
- the agent creates code, reports, images, notes, or exported outputs that should be stored consistently
- the user explicitly asks to save an important chat message into a file
- a project needs a repeatable folder skeleton
- the user asks where a file should go or asks to find a previously stored file

## 触发条件

当用户出现以下行为时，自动应用此规范：
- 在聊天中分享文件（PDF、图片、文档等），需要长期存放
- Agent 创建了代码、报告、图片、笔记等输出，需要统一管理
- 用户明确说"保存这条"、"记住这个"、"写进提醒"、"存一下"
- 需要搭建项目目录骨架或工作区结构
- 用户问"这个文件放哪里"或者"之前存的XX在哪"

**不适用场景**：
- 普通聊天内容的自动存档（不可自动，必须等用户明确保存信号）
- 非文件类任务（代码审查、论文分析、风格清理等）
- 已有独立文件管理方案的项目（尊重现有约定）

## Use The Main Entry Point

Prefer `scripts/file_router_cli.py`.

For the most common agent workflows:

- use `intake` for files the user shared in chat
- use `capture` for files the agent created itself
- use `remember-text` for chat text only when the user explicitly asks to save it
- use `find` to retrieve previously routed files from the same scope

Decide a likely route from a file plus context:

```bash
python scripts/file_router_cli.py decide --source "meeting-notes.docx" --context "lab meeting notes" --origin incoming
```

Handle a user-shared file with default incoming-file behavior:

```bash
python scripts/file_router_cli.py intake --source "C:\Temp\meeting-notes.docx" --context "lab meeting notes"
```

Handle an agent-created file with default generated-file behavior:

```bash
python scripts/file_router_cli.py capture --source ".\draft_report.docx" --project sea-ice-detection --project-type research --context "generated experiment report"
```

Resolve an explicit route:

```bash
python scripts/file_router_cli.py route --domain research --project sea-ice-detection --project-type research --role code --filename train.py
```

Organize a file safely. Default mode is `copy`:

```bash
python scripts/file_router_cli.py organize --source "C:\Temp\figure.png" --domain research --project sea-ice-detection --project-type research --role output --origin generated
```

Find routed files again within the same scope:

```bash
python scripts/file_router_cli.py find --query figure --domain research --project sea-ice-detection
```

Append an important chat message into the reminder note:

```bash
python scripts/file_router_cli.py remember-text --text "important, save this to file: remind me to submit the weekly report at 9 AM tomorrow"
```

Create workspace or project skeletons:

```bash
python scripts/file_router_cli.py scaffold --template workspace
python scripts/file_router_cli.py scaffold --template research-project --project sea-ice-detection
```

## Follow This Workflow

### Default Agent Flow

When the user shares a file in chat:

1. run `intake --dry-run` first if the scope is ambiguous
2. if the returned `needs_review` is `false`, run `intake` to store it under `./files/`
3. if the returned `needs_review` is `true`, ask the user for the missing scope such as project, course, or intended role

When the agent creates a new file itself:

1. decide whether it is a draft, source artifact, experiment record, or final output
2. run `capture --dry-run` if the target location is unclear
3. run `capture` to place it in the correct project or domain folder under `./files/`

When the user says a chat message should be saved:

1. only use `remember-text` when the user gives an explicit save cue such as `important`, `save this`, `remember this`, or an equivalent direct save request
2. default to `./files/Docs/Personal/reminder.md` conceptually; in the current implementation the note file is `./files/Docs/Personal/<Chinese reminder name>.md`
3. append a new markdown entry if the file already exists
4. create missing parent directories and the markdown file automatically
5. use `--target-file` only when the user clearly wants a different note path under `./files/`

Prefer this default:

- user-shared files: `intake`
- agent-created files: `capture`
- explicitly saved chat notes: `remember-text`
- manual route inspection: `route`
- scoped retrieval: `find`

Read [references/agent-flow.md](references/agent-flow.md) when you want the exact default handling protocol for incoming chat attachments and generated artifacts.

### 1. Decide The Storage Scope

Choose the smallest stable scope that matches the file under `./files/`:

- `courses` for class materials organized by term and course
- `lab` for lab administration, meetings, reimbursements, and shared materials
- `research` for papers, notes, shared data, thesis material, and formal research projects
- `dev` for scripts, tools, learning work, sandbox experiments, and general code projects
- `docs`, `media`, `installers`, `systems`, `archive`, or `downloads` for their dedicated long-term categories

If the file belongs to a concrete project, prefer project-scoped storage over a flat top-level bucket.
Create missing subdirectories as needed instead of dumping files into `files/` directly.

### 2. Distinguish Incoming Source From Generated Output

For project work, classify the artifact before storing it:

- incoming attachments usually belong in `source`, `raw-data`, `literature`, `writing`, or project `00_Inbox`
- agent-created drafts usually belong in `work`, `writing`, or `experiments`
- agent-created deliverables usually belong in `output`

Use the research template when the project is a paper, dataset, reproduction, experiment, or model-training effort.
Use the general project template when the project is a utility, script bundle, notes package, course deliverable, or small software project.

### 3. Route Before Writing

Prefer `route` or `decide` before `organize` when classification is unclear.

Read [references/routing-policy.md](references/routing-policy.md) for:

- deterministic path mappings
- project template directories
- role-to-folder rules
- fallback behavior

Read [references/workspace-rules.md](references/workspace-rules.md) when you need the underlying digital workspace conventions.

### 4. Organize Safely

Default to `copy` when handling user-provided files.
Use `move` only when the user explicitly wants the original relocated.

Prefer explicit metadata whenever you know it:

- `--project`
- `--project-type`
- `--course`
- `--term`
- `--role`

If the target path already exists:

- default collision behavior is `rename`
- use `skip` when duplicates should be ignored
- use `overwrite` only when replacement is intentional

### 5. Persist Chat Notes Conservatively

Do not automatically turn ordinary chat text into files.

Use `remember-text` only when at least one of these is true:

- the user explicitly says the message is important
- the user explicitly asks to save, store, or remember it in a file
- the agent is given a direct instruction to persist the chat text

Default behavior:

- store into `./files/Docs/Personal/<Chinese reminder name>.md`
- append a timestamped markdown entry instead of overwriting existing content
- keep the note inside a dedicated markdown section

Examples of valid save cues:

- `important, save this to file`
- `remember this`
- direct Chinese equivalents that clearly mean "this is important" or "save this into a file"

### 6. Find Within The Same Scope

Use `find` with the same scope that was used during storage.

Examples:

- project output should be searched inside that project first
- course files should be searched inside the specific term and course first
- screenshots should be searched in `Media/Screenshots/` unless they were explicitly routed into a project output folder

Do not broaden to unrelated top-level areas until scoped search fails.

## Behavioral Rules

- Keep storage decisions deterministic and explainable.
- Prefer stable top-level domains over one-off custom folders.
- Keep `Downloads` as a staging area, not a final destination, unless the route is genuinely unclear.
- Do not overwrite user files silently.
- Keep generated code, data, drafts, and exported outputs separated when the project template supports it.
- Normalize unsafe file names before storing.
- If route confidence is low and the file is not obviously disposable, ask the user rather than guessing aggressively.
- Do not persist ordinary chat text unless the user gives a clear save signal.
- When persisting chat text, append to the existing note instead of replacing earlier entries.

## References

- [references/workspace-rules.md](references/workspace-rules.md)
- [references/routing-policy.md](references/routing-policy.md)
- [references/agent-flow.md](references/agent-flow.md)
