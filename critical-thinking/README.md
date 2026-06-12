# critical-thinking

[![Version](https://img.shields.io/badge/version-v0.2.0-blue)](./VERSION)

> Independent judgment and critical thinking for substantive conversations.

Use this skill when the assistant needs to express opinions, evaluate claims, or discuss ideas with the user. It defines an intellectual stance: have independent judgment, argue based on facts, and disagree when appropriate.

## Features

- Form independent judgments instead of agreeing blindly.
- Base arguments on facts and reliable sources.
- Explain reasoning clearly.
- Signal confidence levels when stating claims or disagreement.
- Follow a structured workflow when disagreeing with the user.
- Respect boundaries: skip pushback for preferences, values, and pure execution.
- Stay humble and correct mistakes when wrong.

## Installation

This skill is part of the `my-agent-skills` monorepo. Install it by cloning the repo to a temporary directory and copying only the working files into your agent's skills folder (READMEs, tests, and other non-essential files are left out).

```bash
# 1. Clone the monorepo to a temporary directory
git clone git@github.com:solariesity/my-agent-skills.git /tmp/my-agent-skills

# 2. Create the skill directory in the agent's skills folder
mkdir -p ~/.claude/skills/critical-thinking
# Or, for Codex:
# mkdir -p ~/.codex/skills/critical-thinking

# 3. Copy the working parts of the skill
cp /tmp/my-agent-skills/critical-thinking/SKILL.md ~/.claude/skills/critical-thinking/
cp -r /tmp/my-agent-skills/critical-thinking/agents ~/.claude/skills/critical-thinking/
```

```bash
# 4. Clean up the temporary directory
rm -rf /tmp/my-agent-skills
```

Restart the agent so the skill is discovered.

## Usage

Load `SKILL.md` into your agent environment. The skill applies automatically in discussion, analysis, and judgment tasks. Skip it only for pure execution requests such as "rename this file to X".

## Project Structure

```text
critical-thinking/
├── README.md
├── README.zh-CN.md
├── VERSION
├── SKILL.md
└── agents/
    └── openai.yaml
```

- `SKILL.md` — Core behavior specification.
- `agents/openai.yaml` — UI metadata (display name, default prompt).

## Versioning

Current version: [v0.2.0](VERSION).

This is a pre-1.0 skill. Guidelines may evolve as usage patterns become clearer.

## Contributing

Suggestions and pull requests are welcome.
