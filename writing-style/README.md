# writing-style

> Plain, rigorous academic and task-oriented writing style.

Use this skill when writing academic-style or task-style content such as homework, assignments, reports, essays, or any written work that resembles a student submission. It produces clear, plain, and well-structured text without flashiness.

## Features

- Plain and rigorous Chinese academic writing.
- Simple and natural English academic writing.
- Avoids flowery language and internet slang.
- Keeps structure clear without overusing bullet points.
- Stays at a realistic student writing level.

## Installation

This skill lives inside the [`my-agent-skills`](https://github.com/solariesity/my-agent-skills) monorepo. Clone that repository and enter the writing-style directory:

```bash
git clone https://github.com/solariesity/my-agent-skills.git
cd my-agent-skills/writing-style
```

### Install Only the Skill

If you only want to install writing-style as a skill in an agent environment, use a temporary clone:

```bash
# 1. Clone the monorepo to a temporary directory
git clone https://github.com/solariesity/my-agent-skills.git /tmp/my-agent-skills

# 2. Copy only the skill definition to the target location
mkdir -p ~/.codex/skills/writing-style
cp /tmp/my-agent-skills/writing-style/SKILL.md ~/.codex/skills/writing-style/

# 3. Remove the temporary directory
rm -rf /tmp/my-agent-skills
```

On Windows, use `C:\Users\<username>\.codex\skills\writing-style\` as the target path.

## Usage

Load `SKILL.md` into your agent environment. The skill triggers automatically when the user asks for academic or task-oriented writing. Do not use it for creative writing, marketing copy, or social media content.

## Project Structure

```text
writing-style/
├── README.md
├── README.zh-CN.md
└── SKILL.md
```

- `SKILL.md` — Core style rules and trigger conditions.

## Versioning

Current version: `v0.1.0`.

This is a pre-1.0 skill. Style rules may be refined as more writing scenarios are covered.

## Contributing

Suggestions and pull requests are welcome.
