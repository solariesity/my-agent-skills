# Clarify First

[![Version](https://img.shields.io/badge/version-v0.2.0-blue)](./VERSION)

Ask before acting when requirements are ambiguous.

## Description

`clarify-first` is a Codex / Claude Code skill that pauses before starting meaningful work whenever a request is ambiguous, underspecified, or leaves important decisions open. It turns vague instructions into explicit, lettered choices and waits for the user to confirm the path forward.

Use it when a task could be interpreted in multiple ways, the scope is unclear, important inputs are missing, or the wording is tentative or contradictory.

## Features

- Detects ambiguous, incomplete, or open-ended requests automatically.
- Checks for false premises before entering clarification.
- Presents concrete options using lettered choices (`A`, `B`, `C`, … plus `Other`).
- Groups up to 5 tightly coupled blockers in one message.
- Marks a recommended option when a clear default exists.
- Explains the trade-off of each option in one sentence.
- Keeps clarifying up to 5 rounds, then states any remaining assumptions and proceeds.
- Outputs a short clarification snapshot after the user confirms the path.

## Installation

This skill is part of the `my-agent-skills` monorepo. Install it by cloning the repo to a temporary directory and copying only the working files into your agent's skills folder (READMEs, tests, and other non-essential files are left out).

```bash
# 1. Clone the monorepo to a temporary directory
git clone git@github.com:solariesity/my-agent-skills.git /tmp/my-agent-skills

# 2. Create the skill directory in the agent's skills folder
mkdir -p ~/.claude/skills/clarify-first
# Or, for Codex:
# mkdir -p ~/.codex/skills/clarify-first

# 3. Copy the working parts of the skill
cp /tmp/my-agent-skills/clarify-first/SKILL.md ~/.claude/skills/clarify-first/
cp -r /tmp/my-agent-skills/clarify-first/agents ~/.claude/skills/clarify-first/
```

```bash
# 4. Clean up the temporary directory
rm -rf /tmp/my-agent-skills
```

Restart the agent so the skill is discovered.

## Usage

Load `SKILL.md` into your agent environment. The skill applies automatically when a request is ambiguous or underspecified.

You can also invoke it explicitly in a prompt:

```text
Use $clarify-first before you start. I want to refactor the auth module, but I'm not sure whether to do it in-place or behind a feature flag.
```

The agent will stop and ask clarifying questions before editing files or running commands.

## Project Structure

```text
clarify-first/
├── SKILL.md          # Skill behavior and clarification rules
├── README.md         # English documentation
├── README.zh-CN.md   # Chinese documentation
├── VERSION           # Skill version
└── agents/
    └── openai.yaml   # UI metadata (display name, default prompt)
```

## Versioning

Current version: [v0.2.0](VERSION).

This is a pre-1.0 skill. Rules may be refined as more clarification scenarios are covered.

## Contributing

Contributions are welcome. See the [parent repository README](../README.md#contributing) for guidelines.
