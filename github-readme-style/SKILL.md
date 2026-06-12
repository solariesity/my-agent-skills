---
name: github-readme-style
description: Enforce a consistent, bilingual GitHub README structure for general projects. Use when creating, reviewing, or standardizing a project's README and repository front matter.
---

# GitHub README Style

Use this skill when the user asks you to write, review, or standardize a GitHub project's README.

## Default Deliverables

Unless the user explicitly asks otherwise, produce:

1. `README.md` — English version
2. `README.zh-CN.md` — Simplified Chinese version

Both files must cover the same content. Do not let the Chinese version become a vague summary.

## Required Sections

A standard README should include the following sections in this order. Skip a section only if it genuinely does not apply.

1. **Title / Header**
   - Project name as a level-1 heading (`# project-name`)
   - One-line description immediately below the title
   - Optional: badges (CI, version, license, PyPI, npm, etc.) on the next line

2. **Description**
   - 2-5 sentences explaining what the project does and why it exists
   - Mention the main problem it solves or the main capability it provides

3. **Features** (when applicable)
   - Bulleted list of key capabilities
   - Keep each bullet to one line

4. **Installation**
   - Step-by-step commands
   - Include prerequisites when they are not obvious
   - Use code blocks for commands

5. **Usage**
   - Minimal runnable example
   - Include code block
   - Mention the most common entry point or command

6. **Project Structure / Directory Layout** (recommended for non-trivial projects)
   - Use a tree-like code block
   - Explain non-obvious directories

7. **Versioning**
   - State the current version, e.g. `Current version: v0.1.0`
   - Mention the versioning scheme if it follows SemVer
   - Point to `VERSION` file, `package.json`, `pyproject.toml`, or Git tags when available

8. **Contributing** (for public/open projects)
   - Short guidelines or a link to `CONTRIBUTING.md`

9. **License**
   - License name and a link to the license file

## Section Rules

- Keep paragraphs short. One idea per paragraph.
- Use second-person or imperative mood for instructions (`Install`, `Run`, `Set`).
- Avoid filler phrases like "This is a project that..." or "We hope that...".
- All code blocks must specify a language tag when applicable (`bash`, `python`, `json`, `text`).
- CLI examples should be copy-pasteable on the target platform.
- File paths use forward slashes in code examples.

## Language Rules

- `README.md` is in English.
- `README.zh-CN.md` is in Simplified Chinese.
- Keep technical terms (API names, file names, environment variables, CLI flags) in English even in the Chinese version.
- Do not translate code snippets or command names.

## Version Conventions

- Use `v` prefix in prose: `Current version: v0.1.0`
- Keep version consistency between README, `VERSION` file, and package metadata.
- For pre-1.0 projects, explicitly state that the API or behavior may still change.

## Version Records (`VERSION_RECORDS.md`)

For projects that maintain a hand-written changelog or roadmap, use `VERSION_RECORDS.md` with the following structure:

1. **Current Version** — The latest released or stable version, with a short summary of what it includes and its known limits.
2. **Previous Versions** — Past milestones in descending order, each with what it introduced.
3. **Roadmap** — Planned future versions and the conditions or features that would trigger them.

### Version Records Style Rules

- Keep one version per subsection.
- Use bullet lists for changes, limits, and roadmap items.
- Keep the current version in sync with the README badge and any `VERSION` file.
- Do not let the file become a duplicate of Git commit history; focus on user-facing or maintainer-facing milestones.
- If the file is referenced from the README, make sure it is tracked by Git and not ignored.

## Directory Structure Section

When including a directory tree:

```text
project-name/
├── README.md
├── README.zh-CN.md
├── src/
│   └── module.py
├── tests/
│   └── test_module.py
└── pyproject.toml
```

- Only show meaningful levels (usually 2-3).
- Do not include generated/ignored directories (`.git`, `node_modules`, `__pycache__`, `build`, `.idea`).
- Explain any directory whose purpose is not obvious from its name.

## Installation Section Rules

- Start with prerequisites if they exist (runtime, package manager, OS constraints).
- Provide the primary install command.
- For Python: prefer `pip install -e .` for development installs.
- For Node: prefer `npm install` or `pnpm install`.
- If there are optional dependencies, mention them in a subsection.

### Skill-specific installation workflow

Use the clone-to-tmp workflow **only** when the target project is a Codex / Claude Code skill (i.e., it contains a `SKILL.md` file and is meant to be loaded from `~/.claude/skills/` or `~/.codex/skills/`).

When the skill lives inside a monorepo:

1. Clone the parent repository to a temporary directory.
2. Create a directory for the skill inside the agent's skills folder.
3. Copy **only the working files** of the skill (`SKILL.md`, `agents/`, `references/`, `scripts/`, etc.). Do **not** copy `README.md`, `README.zh-CN.md`, tests, or other non-essential files.
4. Restart the agent.

Example:

```bash
# Clone the parent monorepo to a temporary location
git clone <repo-url> /tmp/<repo-name>

# Create the skill directory in the agent's skills folder
mkdir -p ~/.claude/skills/<skill-name>
# Or, for Codex:
# mkdir -p ~/.codex/skills/<skill-name>

# Copy only the working parts of the skill
cp /tmp/<repo-name>/<skill-name>/SKILL.md ~/.claude/skills/<skill-name>/
cp -r /tmp/<repo-name>/<skill-name>/agents ~/.claude/skills/<skill-name>/
# Copy references/ and scripts/ only if the skill has them
```

If the project is **not** a skill, use the normal installation instructions for its technology (e.g., `pip install`, `npm install`) and omit this workflow entirely.

## Usage Section Rules

- Provide the simplest complete example first.
- Add more advanced examples only after the basic one.
- Use realistic but minimal input/output.
- If the project is a CLI, show the most common command and its expected output.
- If the project is a library, show a short import-and-call snippet.

## Badges

Use badges only when they provide real value. Common useful badges:

- CI status
- Latest release version
- License
- Package registry version (PyPI, npm, crates.io)

Place badges directly under the project title.

## When Reviewing an Existing README

1. Check that all required sections are present or intentionally omitted.
2. Check that `README.md` and `README.zh-CN.md` are consistent.
3. Check that installation steps actually work as written.
4. Check that the version number matches the repository metadata.
5. Remove generated directories from the directory tree.
6. Fix broken links or placeholders.

## Editing Workflow

1. Read the existing README files and project metadata (`VERSION`, `package.json`, `pyproject.toml`, etc.).
2. Decide which required sections are missing or need improvement.
3. Update `README.md` first, then mirror the changes in `README.zh-CN.md`.
4. Verify that links between the two README files work if you add language-switch links.
5. Run any examples manually if possible; if not, state the limitation.
