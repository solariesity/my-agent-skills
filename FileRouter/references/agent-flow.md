# Agent Flow

Use this file when FileRouter is being applied directly inside an agent workflow.

## Default Storage Root

Unless another workspace root is explicitly supplied, FileRouter stores everything under:

```text
./files/
```

This is relative to the current working directory.

## Incoming User Files

Use `intake`.

Recommended process:

1. inspect the filename and any nearby user message
2. run `intake --dry-run` when the scope is ambiguous
3. if `needs_review` is `false`, run `intake`
4. if `needs_review` is `true`, ask the user for missing scope such as project, course, or intended storage purpose

Example:

```bash
python scripts/file_router_cli.py intake --dry-run --source "C:\Temp\paper.pdf" --context "paper for the sea ice project"
python scripts/file_router_cli.py intake --source "C:\Temp\paper.pdf" --project sea-ice-detection --project-type research
```

## Agent-Created Files

Use `capture`.

Recommended process:

1. decide whether the file is source, work, experiment, writing, or output
2. run `capture --dry-run` when the scope is not obvious
3. run `capture` with project metadata when known

Example:

```bash
python scripts/file_router_cli.py capture --source ".\figure.png" --project sea-ice-detection --project-type research --role output
```

## Explicitly Saved Chat Notes

Use `remember-text`.

Recommended process:

1. do not store ordinary chat text by default
2. only call `remember-text` when the user gives a clear save cue such as `很重要`, `记一下`, `存在文件中吧`, `save this`, or `remember this`
3. default to `./files/Docs/Personal/提醒.md`
4. append a new markdown entry when the reminder file already exists
5. use `--target-file` only when the user clearly wants another note path under `./files/`

Examples:

```bash
python scripts/file_router_cli.py remember-text --text "很重要，存在文件中吧：明天 9 点提醒我提交周报"
python scripts/file_router_cli.py remember-text --text "save this: weekly sync agenda" --target-file "Lab/Tasks/weekly-sync.md" --section Inbox
```

## Retrieval

Use `find` with the same scope used during storage.

Examples:

```bash
python scripts/file_router_cli.py find --query figure --project sea-ice-detection --domain research
python scripts/file_router_cli.py find --query assignment1 --course machine-learning --term 2026-Spring --domain courses
```

## Review Threshold

Treat these as reasons to ask the user before committing to storage:

- `needs_review` is `true`
- the route falls back to `files/Downloads/`
- the file could plausibly belong to more than one project
- the user has given a project name but not enough scope to distinguish source, work, and output
- the user did not explicitly ask to persist the chat text but the agent is considering `remember-text`
