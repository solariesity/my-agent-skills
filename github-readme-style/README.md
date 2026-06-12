# GitHub README Style

🌐 English · [中文](README.zh-CN.md)

[![Version](https://img.shields.io/badge/version-v1.0.0-blue)](./VERSION)

A Codex / Claude Code skill for standardizing GitHub READMEs.

## Description

`github-readme-style` is a Codex / Claude Code skill that enforces a consistent, bilingual README structure for GitHub projects. When invoked, it produces or reviews both an English `README.md` and a Simplified Chinese `README.zh-CN.md` that cover the same content with the same logical structure.

Use it to bootstrap a new README, add a Chinese translation, or review and standardize an existing README.

## Features

- Bilingual output (`README.md` + `README.zh-CN.md`) by default.
- Required section ordering and content rules.
- Version formatting and badge conventions.
- Directory tree rules.
- Installation and usage example templates.
- README review checklist.

## Installation

This skill is part of the `my-agent-skills` monorepo. Install it by cloning the repo to a temporary directory and copying only the working files into your agent's skills folder (READMEs, tests, and other non-essential files are left out).

```bash
# 1. Clone the monorepo to a temporary directory
git clone git@github.com:solariesity/my-agent-skills.git /tmp/my-agent-skills

# 2. Create the skill directory in the agent's skills folder
mkdir -p ~/.claude/skills/github-readme-style
# Or, for Codex:
# mkdir -p ~/.codex/skills/github-readme-style

# 3. Copy the working parts of the skill
cp /tmp/my-agent-skills/github-readme-style/SKILL.md ~/.claude/skills/github-readme-style/
cp -r /tmp/my-agent-skills/github-readme-style/agents ~/.claude/skills/github-readme-style/
```

```bash
# 4. Clean up the temporary directory
rm -rf /tmp/my-agent-skills
```

Restart the agent so the skill is discovered.

## Usage

Invoke the skill explicitly:

```text
/github-readme-style
```

Or ask the agent to use it in a prompt:

```text
Use $github-readme-style to write a README for this project.
```

Typical requests:

- "Write a README for this project."
- "Review and standardize the README."
- "Add a Chinese README."

## Project Structure

```text
github-readme-style/
├── README.md              # English documentation
├── README.zh-CN.md        # Simplified Chinese documentation
├── VERSION                # Current version
├── SKILL.md               # Skill behavior specification
└── agents/
    └── openai.yaml        # UI metadata (display name, default prompt)
```

## Versioning

Current version: [v1.0.0](VERSION).

This skill follows [Semantic Versioning](https://semver.org/). The `VERSION` file is the source of truth.

## Contributing

Contributions are welcome. See the [parent repository README](../README.md#contributing) for guidelines.

## License

See the [parent repository](../README.md) for license information.
