# My Agent Skills

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

Each skill has its own installation instructions in its README under the **Install only the skill** section. Pick the skill you need and follow its guide:

| Skill | README |
|-------|--------|
| memory-router | [README](memory-router/README.md) |
| file-router | [README](file-router/README.md) |
| python-style-skill | [README](python-style-skill/README.md) |
| github-readme-style | [README](github-readme-style/README.md) |
| critical-thinking | [README](critical-thinking/README.md) |
| paper-review-prep | [README](paper-review-prep/README.md) |
| academic-writing-style | [README](academic-writing-style/README.md) |

## Usage

After installation, the target agent platform loads the skill automatically from `~/.codex/skills/<skill-name>/`. See each skill's own README for specific usage and examples.

## Project Structure

```text
my-agent-skills/
├── README.md
├── README.zh-CN.md
├── VERSION
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

## Recommended Skills & Tools

Skills and tools I find useful or worth referencing.

### Skills

| Skill | Repository | Introduction |
|-------|------------|--------------|
| andrej-karpathy-skills | https://github.com/duolahypercho/andrej-karpathy-skills | A Codex skill that packages Andrej Karpathy-style coding practices—think first, keep it simple, only make necessary changes, and finish with verifiable goals—to improve the stability and controllability of daily coding agents. |

### MCP Servers

| Tool | Repository | Introduction |
|------|------------|--------------|
| CodeGraph | https://github.com/colbymchenry/codegraph | Turns a codebase into a queryable knowledge graph, reducing AI exploration cost by ~70%. |

## Contributing

Contributions are welcome. Please open an issue or pull request with a clear description of the change.
