# skill-review

[![Version](https://img.shields.io/badge/version-v1.0.0-blue)](./VERSION)

> Guide the review and improvement of skills inside the my-agent-skills monorepo.

`skill-review` is a Codex / Claude Code skill for reviewing other skills in this repository. When asked to evaluate a skill, it loads the skill files, checks them against monorepo conventions, compares them with similar community skills, proposes concrete improvements, and—after user approval—helps implement, version, and push the changes.

## Features

- Loads and inspects a target skill's files (`SKILL.md`, READMEs, `VERSION`, `agents/openai.yaml`, `.gitignore`).
- Checks for common convention violations and obvious issues.
- Searches for comparable community skills on GitHub.
- Presents strengths, issues, and optimization ideas with source links.
- Follows an approval workflow: evaluate → ask → implement → ask about version → push.

## Installation

This skill is part of the `my-agent-skills` monorepo. Install it by cloning the repo to a temporary directory and copying only the working files into your agent's skills folder (READMEs, tests, and other non-essential files are left out).

```bash
# 1. Clone the monorepo to a temporary directory
git clone git@github.com:solariesity/my-agent-skills.git /tmp/my-agent-skills

# 2. Create the skill directory in the agent's skills folder
mkdir -p ~/.claude/skills/skill-review
# Or, for Codex:
# mkdir -p ~/.codex/skills/skill-review

# 3. Copy the working parts of the skill
cp /tmp/my-agent-skills/skill-review/SKILL.md ~/.claude/skills/skill-review/
cp -r /tmp/my-agent-skills/skill-review/agents ~/.claude/skills/skill-review/
```

```bash
# 4. Clean up the temporary directory
rm -rf /tmp/my-agent-skills
```

Restart the agent so the skill is discovered.

## Usage

Load `SKILL.md` into your agent environment. Invoke it when the user asks to review, evaluate, or improve a skill in this monorepo:

```text
Use $skill-review to evaluate the file-router skill.
```

The agent will inspect the skill, compare it with similar community skills, present findings, and ask before making changes.

## Project Structure

```text
skill-review/
├── README.md
├── README.zh-CN.md
├── VERSION
├── SKILL.md
└── agents/
    └── openai.yaml
```

- `SKILL.md` — Review workflow and checklist.
- `agents/openai.yaml` — UI metadata for skill lists and default prompt.

## Versioning

Current version: [v1.0.0](VERSION).

This is a pre-1.0 skill. The review workflow may be refined as the monorepo grows.

## Contributing

Contributions are welcome. See the [parent repository README](../README.md#contributing) for guidelines.

## License

This project is licensed under the [MIT License](../LICENSE).
