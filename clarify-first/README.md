# Clarify First

Ask before acting when requirements are ambiguous.

## Description

`clarify-first` is a Codex / Claude Code skill that pauses before starting meaningful work whenever a request is ambiguous, underspecified, or leaves important decisions open. It turns vague instructions into explicit, lettered choices and waits for the user to confirm the path forward.

Use it when a task could be interpreted in multiple ways, the scope is unclear, important inputs are missing, or the wording is tentative or contradictory.

## Features

- Detects ambiguous, incomplete, or open-ended requests automatically.
- Presents concrete options using lettered choices (`A`, `B`, `C`, … plus `Other`).
- Marks a recommended option when a clear default exists.
- Explains the trade-off of each option in one sentence.
- Keeps clarifying until all blocking decisions are explicit.

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

Invoke the skill explicitly:

```text
/clarify-first
```

Or ask the agent to use it in a prompt:

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
└── agents/
    └── openai.yaml   # UI metadata (display name, default prompt)
```

## Versioning

This skill is versioned together with the parent repository. See the top-level [`VERSION`](../VERSION) file for the current version.

## Contributing

Contributions are welcome. See the [parent repository README](../README.md#contributing) for guidelines.
