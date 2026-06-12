# My Agent Skills

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A unified collection of personal AI agent / Codex skills for deterministic memory routing, file routing, coding style enforcement, and task-specific reasoning.

## Description

This repository consolidates scattered skill projects into a single monorepo. Each skill is self-contained under its own directory and can be installed independently into any Codex / Claude Code compatible environment.

## Features

- Unified management of all personal agent skills in one repository
- Bilingual documentation (`README.md` + `README.zh-CN.md`) for every skill
- Deterministic routing for conversations, files, and generated outputs
- Coding style guides for research and training code
- Critical thinking, paper review, and academic writing helpers

## Installation

Each skill is a self-contained directory. Pick the skill you need from the table below and install it to `~/.codex/skills/`:

```bash
# 1. Clone to a temporary location
git clone https://github.com/<your-username>/my-agent-skills.git /tmp/my-agent-skills

# 2. Copy the skill you want
cp -r /tmp/my-agent-skills/<skill-name> ~/.codex/skills/<skill-name>

# 3. Remove the temporary clone
rm -rf /tmp/my-agent-skills
```

| Skill | Directory | Install path |
|-------|-----------|--------------|
| memory-router | [memory-router/](memory-router/) | `~/.codex/skills/memory-router` |
| file-router | [file-router/](file-router/) | `~/.codex/skills/file-router` |
| python-style-skill | [python-style-skill/](python-style-skill/) | `~/.codex/skills/python-style-skill` |
| github-readme-style | [github-readme-style/](github-readme-style/) | `~/.codex/skills/github-readme-style` |
| critical-thinking | [critical-thinking/](critical-thinking/) | `~/.codex/skills/critical-thinking` |
| paper-review-prep | [paper-review-prep/](paper-review-prep/) | `~/.codex/skills/paper-review-prep` |
| academic-writing-style | [academic-writing-style/](academic-writing-style/) | `~/.codex/skills/academic-writing-style` |

## Usage

After installation, the target agent platform loads the skill automatically from `~/.codex/skills/<skill-name>/`. See each skill's own `README.md` for specific usage and examples.

## Project Structure

```text
my-agent-skills/
├── README.md
├── README.zh-CN.md
├── VERSION
├── LICENSE
├── memory-router/            # Conversational memory routing
├── file-router/              # File and output workspace routing
├── python-style-skill/       # Python coding style for research code
├── github-readme-style/      # README standardization conventions
├── critical-thinking/        # Reasoning and disagreement guidelines
├── paper-review-prep/        # Paper reading and presentation prep
└── academic-writing-style/   # Academic writing style guide
```

## Versioning

Current version: v0.1.0

This project follows [Semantic Versioning](https://semver.org/). See [VERSION](VERSION) for the current version number.

## Contributing

Contributions are welcome. Please open an issue or pull request with a clear description of the change.

## License

This project is released under the MIT License. See [LICENSE](LICENSE) for details.
