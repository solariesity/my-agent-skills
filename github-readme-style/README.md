# GitHub README Style

[![Version](https://img.shields.io/badge/version-v0.1.0-blue)](./VERSION)

A Codex / Claude Code skill for standardizing GitHub READMEs.

## What it does

This skill enforces a consistent README structure across your GitHub projects. When invoked, it produces or reviews:

- `README.md` (English)
- `README.zh-CN.md` (Simplified Chinese)

Both files follow the same logical structure and cover the same content.

## Included rules

- Required sections and their order
- Bilingual output conventions
- Version formatting
- Directory tree rules
- Installation and usage examples
- Badge usage
- Review checklist

## File layout

```text
github-readme-style/
├── README.md
├── VERSION
├── SKILL.md
└── agents/
    └── openai.yaml
```

## How to use

Load this skill in your agent environment and ask it to:

- "Write a README for this project"
- "Review and standardize the README"
- "Add a Chinese README"

The skill will use `SKILL.md` as the behavior specification.

## Versioning

Current version: [v0.1.0](VERSION).
