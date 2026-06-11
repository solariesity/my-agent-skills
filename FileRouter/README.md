# FileRouter

[简体中文](README.zh-CN.md)

Version: `0.2.0`

FileRouter is a Codex skill for storing user-shared files, agent-created files, and explicitly saved chat notes inside a structured `./files/` workspace tree.

It helps an agent:

- route files into stable subdirectories by domain, project, course, and role
- create missing folders automatically under the current working directory
- separate incoming files from generated outputs
- append important chat notes into a reminder file instead of scattering ad hoc notes
- find previously stored files again with scoped search

## Storage Model

All storage lives under:

```text
./files/
```

Typical top-level areas:

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

Project files are routed into template subdirectories such as:

- general projects: `00_Inbox`, `01_Admin`, `02_Source`, `03_Work`, `04_Output`, `99_Archive`
- research projects: `01_Literature`, `02_Data/raw`, `02_Data/processed`, `03_Code`, `04_Experiments`, `05_Writing`, `06_Output`, `99_Archive`

## Chat Note Rule

FileRouter does not automatically store ordinary chat text.

Use `remember-text` only when the user gives a clear persistence cue such as:

- `很重要，存在文件中吧`
- `记一下，写进提醒里`
- `save this to file`
- `remember this`

Default reminder target:

```text
./files/Docs/Personal/提醒.md
```

If the file already exists, FileRouter appends a new Markdown entry instead of overwriting older content.

## Main Commands

Use the CLI entry point:

```bash
python scripts/file_router_cli.py <command> ...
```

Most common commands:

- `intake`: handle a file shared by the user
- `capture`: handle a file created by the agent
- `decide`: guess domain and role from filename and context
- `route`: resolve an explicit destination path
- `organize`: copy or move a file into its routed location
- `find`: search previously routed files
- `remember-text`: append important chat text into a note file
- `scaffold`: create workspace or project skeletons

## Typical Examples

Handle a user-shared file:

```bash
python scripts/file_router_cli.py intake --source "C:\Temp\paper.pdf" --context "paper for the sea ice project"
```

Handle an agent-created output:

```bash
python scripts/file_router_cli.py capture --source ".\figure.png" --project sea-ice-detection --project-type research --role output
```

Save an important chat message:

```bash
python scripts/file_router_cli.py remember-text --text "很重要，存在文件中吧：明天 9 点提醒我提交周报"
```

Save into a custom note file under `./files/`:

```bash
python scripts/file_router_cli.py remember-text --text "save this: weekly sync agenda" --target-file "Lab/Tasks/weekly-sync.md" --section Inbox
```

Create the local storage skeleton:

```bash
python scripts/file_router_cli.py scaffold --template workspace
```

Find a routed file again:

```bash
python scripts/file_router_cli.py find --query figure --domain research --project sea-ice-detection
```

## Repository Layout

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

## Validation

Run tests:

```bash
python -m unittest discover -s tests -v
```

Validate the skill structure:

```bash
python C:\Users\Lenovo\.codex\skills\.system\skill-creator\scripts\quick_validate.py .
```
