# academic-writing-style

[![Version](https://img.shields.io/badge/version-v0.1.0-blue)](./VERSION)

> Plain, rigorous academic and task-oriented writing style.

Use this skill when writing academic-style or task-style content such as homework, assignments, reports, essays, or any written work that resembles a student submission. It produces clear, plain, and well-structured text without flashiness.

## Features

- Plain and rigorous Chinese academic writing.
- Simple and natural English academic writing.
- Avoids flowery language and internet slang.
- Keeps structure clear without overusing bullet points.
- Stays at a realistic student writing level.

## Installation

This skill is part of the `my-agent-skills` monorepo. Install it by cloning the repo to a temporary directory and copying only the working files into your agent's skills folder (READMEs, tests, and other non-essential files are left out).

```bash
# 1. Clone the monorepo to a temporary directory
git clone git@github.com:solariesity/my-agent-skills.git /tmp/my-agent-skills

# 2. Create the skill directory in the agent's skills folder
mkdir -p ~/.claude/skills/academic-writing-style
# Or, for Codex:
# mkdir -p ~/.codex/skills/academic-writing-style

# 3. Copy the working parts of the skill
cp /tmp/my-agent-skills/academic-writing-style/SKILL.md ~/.claude/skills/academic-writing-style/
```

```bash
# 4. Clean up the temporary directory
rm -rf /tmp/my-agent-skills
```

Restart the agent so the skill is discovered.

## Usage

Load `SKILL.md` into your agent environment. The skill triggers automatically when the user asks for academic or task-oriented writing. Do not use it for creative writing, marketing copy, or social media content.

## Project Structure

```text
academic-writing-style/
├── README.md
├── README.zh-CN.md
├── VERSION
└── SKILL.md
```

- `SKILL.md` — Core style rules and trigger conditions.

## Versioning

Current version: [v0.1.0](VERSION).

This is a pre-1.0 skill. Style rules may be refined as more writing scenarios are covered.

## Contributing

Suggestions and pull requests are welcome.
