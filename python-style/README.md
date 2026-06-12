# python-style

[中文](README.zh-CN.md)

[![Version](https://img.shields.io/badge/version-v1.0.0-blue)](./VERSION)

> Behavior-preserving Python style cleanup for research and training code.

Use this skill when reviewing or standardizing Python naming, module or file names, Chinese-first comments or docstrings, and stable parseable training or debug output without breaking external contracts.

## Features

- Clean up mixed naming conventions without changing behavior.
- Standardize module and file names.
- Keep comments and docstrings mostly Chinese when the project allows it.
- Stabilize training logs and debug output for downstream parsers.
- Preserve externally consumed names and output fields as contracts.

## Installation

This skill is part of the `my-agent-skills` monorepo. Install it by cloning the repo to a temporary directory and copying only the working files into your agent's skills folder (READMEs, tests, and other non-essential files are left out).

```bash
# 1. Clone the monorepo to a temporary directory
git clone git@github.com:solariesity/my-agent-skills.git /tmp/my-agent-skills

# 2. Create the skill directory in the agent's skills folder
mkdir -p ~/.claude/skills/python-style
# Or, for Codex:
# mkdir -p ~/.codex/skills/python-style

# 3. Copy the working parts of the skill
cp /tmp/my-agent-skills/python-style/SKILL.md ~/.claude/skills/python-style/
cp -r /tmp/my-agent-skills/python-style/agents ~/.claude/skills/python-style/
```

```bash
# 4. Clean up the temporary directory
rm -rf /tmp/my-agent-skills
```

Restart the agent so the skill is discovered.

## Usage

Load `SKILL.md` into your agent environment. The skill triggers automatically when you ask the agent to review, clean, or standardize Python code in a research or training codebase.

Typical prompts:

- "Review this Python file for style issues."
- "Clean up the naming in this training script."
- "Make the training logs easier to parse without changing the logic."

## Project Structure

```text
python-style/
├── README.md
├── README.zh-CN.md
├── VERSION
├── .gitignore
├── SKILL.md
└── agents/
    └── openai.yaml
```

- `SKILL.md` — Core behavior specification and style rules.

## Versioning

Current version: [v1.0.0](VERSION).

This is a pre-1.0 skill. Rules may evolve as more Python cleanup patterns are identified.

## Contributing

Suggestions and pull requests are welcome.

## License

This project is licensed under the [MIT License](../LICENSE).
