# paper-review-prep

[![Version](https://img.shields.io/badge/version-v0.1.0-blue)](./VERSION)

> Systematic research paper analysis and presentation preparation.

Use this skill when preparing for a group meeting or presentation by analyzing a research paper. Typical triggers include: "review this paper", "prepare a literature summary", "group meeting prep", or similar academic paper review tasks.

## Features

- Read and analyze papers systematically.
- Generate concise summaries.
- Explain papers in plain language.
- Provide formal academic phrasing.
- Build clear presentation outlines.

## Installation

This skill is part of the `my-agent-skills` monorepo. Install it by cloning the repo to a temporary directory and copying only the working files into your agent's skills folder (READMEs, tests, and other non-essential files are left out).

```bash
# 1. Clone the monorepo to a temporary directory
git clone git@github.com:solariesity/my-agent-skills.git /tmp/my-agent-skills

# 2. Create the skill directory in the agent's skills folder
mkdir -p ~/.claude/skills/paper-review-prep
# Or, for Codex:
# mkdir -p ~/.codex/skills/paper-review-prep

# 3. Copy the working parts of the skill
cp /tmp/my-agent-skills/paper-review-prep/SKILL.md ~/.claude/skills/paper-review-prep/
```

```bash
# 4. Clean up the temporary directory
rm -rf /tmp/my-agent-skills
```

Restart the agent so the skill is discovered.

## Usage

Load `SKILL.md` into your agent environment. The skill triggers automatically when the user asks for paper analysis, literature review, or group-meeting preparation.

## Project Structure

```text
paper-review-prep/
├── README.md
├── README.zh-CN.md
├── VERSION
└── SKILL.md
```

- `SKILL.md` — Core workflow and output format specification.

## Versioning

Current version: [v0.1.0](VERSION).

This is a pre-1.0 skill. The workflow may evolve based on different meeting and presentation styles.

## Contributing

Suggestions and pull requests are welcome.
