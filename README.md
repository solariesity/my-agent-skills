# My Agent Skills

[![Version](https://img.shields.io/badge/version-v0.1.0-blue)](./VERSION)

A unified collection of personal AI agent / Codex skills for deterministic memory routing, file routing, coding style enforcement, and task-specific reasoning.

## Description

This repository consolidates scattered skill projects into a single monorepo. Each skill is self-contained under its own directory and can be installed independently into any Codex / Claude Code compatible environment.

## Features

- Unified management of all personal agent skills in one repository
- Bilingual documentation (`README.md` + `README.zh-CN.md`) for every skill
- Deterministic routing for conversations, files, and generated outputs
- Coding style guides for research and training code
- Critical thinking, paper review, and academic writing helpers

## My Skills

| Skill | README | Introduction |
|-------|--------|--------------|
| memory-router | [README](memory-router/README.md) | Route conversational memory into deterministic markdown files by user, project, type, and date. |
| file-router | [README](file-router/README.md) | Route user files and generated outputs into a structured `./files/` workspace. |
| python-style-skill | [README](python-style-skill/README.md) | Behavior-preserving Python style cleanup for research and training code. |
| github-readme-style | [README](github-readme-style/README.md) | Standardize GitHub READMEs with bilingual docs, version info, and project structure. |
| critical-thinking | [README](critical-thinking/README.md) | Independent judgment and critical thinking for substantive conversations. |
| paper-review-prep | [README](paper-review-prep/README.md) | Systematic research paper analysis and presentation preparation. |
| academic-writing-style | [README](academic-writing-style/README.md) | Plain, rigorous academic and task-oriented writing style. |
| clarify-first | [README](clarify-first/README.md) | Require explicit clarification before acting when requirements are ambiguous. |
| paper-analyst-zh | [README](paper-analyst-zh/README.md) | Translate and deeply analyze English CS/engineering papers in Chinese. |

## Installation

Each skill has its own installation instructions in its README under the **Install only the skill** section. Pick the skill you need from the table above and follow its guide.

After installation, the target agent platform loads the skill automatically from `~/.codex/skills/<skill-name>/`. See each skill's own README for specific usage and examples.

## Project Structure

```text
my-agent-skills/
├── README.md
├── README.zh-CN.md
├── AGENTS.md                 # Durable conventions for this repo
├── VERSION
├── .gitignore
├── memory-router/            # Conversational memory routing
├── file-router/              # File and output workspace routing
├── python-style-skill/       # Python coding style for research code
├── github-readme-style/      # README standardization conventions
├── critical-thinking/        # Reasoning and disagreement guidelines
├── paper-review-prep/        # Paper reading and presentation prep
├── academic-writing-style/   # Academic writing style guide
├── clarify-first/            # Clarify requirements before acting
└── paper-analyst-zh/         # Translate and analyze papers in Chinese
```

## Versioning

Current version: v0.1.0

This project follows [Semantic Versioning](https://semver.org/). See [VERSION](VERSION) for the current version number.

## Recommended Skills & Tools

Skills and tools I find useful or worth referencing.

### Skills

| Skill | Repository | Introduction |
|-------|------------|--------------|
| ljg-skills | https://github.com/lijigang/ljg-skills | A personal collection of AI agent skills. |
| andrej-karpathy-skills | https://github.com/duolahypercho/andrej-karpathy-skills | A Codex skill that packages Andrej Karpathy-style coding practices—think first, keep it simple, only make necessary changes, and finish with verifiable goals—to improve the stability and controllability of daily coding agents. |

### MCP Servers

| Tool | Repository | Introduction |
|------|------------|--------------|
| CodeGraph | https://github.com/colbymchenry/codegraph | Turns a codebase into a queryable knowledge graph, reducing AI exploration cost by ~70%. |

## Contributing

Contributions are welcome. Please open an issue or pull request with a clear description of the change.
