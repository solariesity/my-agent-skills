# FileRouter

[![Version](https://img.shields.io/badge/version-v0.2.0-blue)](./VERSION)

> Route user-shared files, agent-created artifacts, and explicitly saved chat notes into a structured `files/` tree inside the current working directory.

FileRouter is a Codex skill and local CLI tool that helps an agent decide where files should live, create workspace skeletons, separate incoming files from generated outputs, and find previously stored files again.

## Features

- Route files into stable subdirectories by domain, project, course, and role.
- Create missing folders automatically under the current working directory.
- Separate incoming attachments from agent-generated outputs.
- Append important chat notes into a reminder file instead of scattering ad hoc notes.
- Find previously routed files with scoped search.

## Installation

FileRouter requires Python 3.10 or newer.

This skill lives inside the [`my-agent-skills`](https://github.com/solariesity/my-agent-skills) monorepo. Clone that repository and enter the FileRouter directory:

```bash
git clone https://github.com/solariesity/my-agent-skills.git
cd my-agent-skills/FileRouter
```

No package installation is required for CLI usage. Run commands directly from the `scripts/` directory:

```bash
python scripts/file_router_cli.py --help
```

### Install Only the Skill

If you only want to install FileRouter as a skill in an agent environment (without project-maintenance files like `README`, `tests`, or `VERSION`), use a temporary clone:

```bash
# 1. Clone the monorepo to a temporary directory
git clone https://github.com/solariesity/my-agent-skills.git /tmp/my-agent-skills

# 2. Copy only the core skill files to the target location
mkdir -p ~/.codex/skills/FileRouter
cp -r /tmp/my-agent-skills/FileRouter/SKILL.md ~/.codex/skills/FileRouter/
cp -r /tmp/my-agent-skills/FileRouter/agents ~/.codex/skills/FileRouter/
cp -r /tmp/my-agent-skills/FileRouter/references ~/.codex/skills/FileRouter/
cp -r /tmp/my-agent-skills/FileRouter/scripts ~/.codex/skills/FileRouter/

# 3. Remove the temporary directory
rm -rf /tmp/my-agent-skills
```

On Windows, use `C:\Users\<username>\.codex\skills\FileRouter\` as the target path.

## Usage

Handle a user-shared file:

```bash
python scripts/file_router_cli.py intake \
  --source "C:/Temp/paper.pdf" \
  --context "paper for the sea ice project"
```

Handle an agent-created output:

```bash
python scripts/file_router_cli.py capture \
  --source "./figure.png" \
  --project sea-ice-detection \
  --project-type research \
  --role output
```

Save an important chat message:

```bash
python scripts/file_router_cli.py remember-text \
  --text "important, save this: remind me to submit the weekly report at 9 AM tomorrow"
```

Save into a custom note file under `./files/`:

```bash
python scripts/file_router_cli.py remember-text \
  --text "save this: weekly sync agenda" \
  --target-file "Lab/Tasks/weekly-sync.md" \
  --section Inbox
```

Create the local storage skeleton:

```bash
python scripts/file_router_cli.py scaffold --template workspace
```

Find a routed file again:

```bash
python scripts/file_router_cli.py find \
  --query figure \
  --domain research \
  --project sea-ice-detection
```

## Storage Model

All storage lives under:

```text
./files/
```

Typical top-level areas:

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

Project files are routed into template subdirectories such as:

- General projects: `00_Inbox`, `01_Admin`, `02_Source`, `03_Work`, `04_Output`, `99_Archive`
- Research projects: `01_Literature`, `02_Data/raw`, `02_Data/processed`, `03_Code`, `04_Experiments`, `05_Writing`, `06_Output`, `99_Archive`

## Chat Note Rule

FileRouter does not automatically store ordinary chat text.

Use `remember-text` only when the user gives a clear persistence cue such as:

- `important, save this to file`
- `remember this`
- `记一下，写进提醒里`
- `很重要，存在文件中吧`

Default reminder target:

```text
./files/Docs/Personal/reminder.md
```

If the file already exists, FileRouter appends a new Markdown entry instead of overwriting older content.

## Project Structure

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

- `SKILL.md` — Trigger description and operational guidance for agent integration.
- `agents/openai.yaml` — UI-facing metadata for skill marketplaces.
- `references/` — Canonical rules for agent flow, routing policy, and workspace conventions.
- `scripts/` — CLI entry point and core routing logic.
- `tests/` — Unit tests for file routing behavior.

## Versioning

Current version: `v0.2.0`.

FileRouter follows semantic versioning in spirit. `v0.2.0` is a pre-1.0 release; the CLI surface and routing policies may still evolve as usage patterns become clearer.

## Testing

Run the built-in test suite with:

```bash
python -m unittest discover -s tests -v
```

## Contributing

Suggestions and pull requests are welcome.

## Main Commands

- `intake`: handle a file shared by the user
- `capture`: handle a file created by the agent
- `decide`: guess domain and role from filename and context
- `route`: resolve an explicit destination path
- `organize`: copy or move a file into its routed location
- `find`: search previously routed files
- `remember-text`: append important chat text into a note file
- `scaffold`: create workspace or project skeletons

See `SKILL.md` and `references/` for detailed workflow guidance.
