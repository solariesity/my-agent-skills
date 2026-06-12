# coursework-writing-style

[![Version](https://img.shields.io/badge/version-v1.0.0-blue)](./VERSION)

> Plain, clear coursework writing for student assignments and course papers.

Use this skill when helping with coursework writing tasks such as homework, assignments, course papers, lab reports, reading reports, and reflection pieces. It produces clear, plain, and appropriately structured text that matches a realistic student writing level. Do not use it for published academic papers, creative writing, marketing copy, or social media content.

## Features

- Plain and clear Chinese writing for coursework.
- Simple and natural English writing for student submissions.
- Aligns with assignment requirements before drafting.
- Adapts tone to common coursework types (course paper, lab report, reading report, reflection).
- Avoids flowery language and internet slang.
- Keeps structure clear without overusing bullet points.
- Stays at a realistic student writing level.

## Installation

This skill is part of the `my-agent-skills` monorepo. Install it by cloning the repo to a temporary directory and copying only the working files into your agent's skills folder (READMEs, tests, and other non-essential files are left out).

```bash
# 1. Clone the monorepo to a temporary directory
git clone git@github.com:solariesity/my-agent-skills.git /tmp/my-agent-skills

# 2. Create the skill directory in the agent's skills folder
mkdir -p ~/.claude/skills/coursework-writing-style
# Or, for Codex:
# mkdir -p ~/.codex/skills/coursework-writing-style

# 3. Copy the working parts of the skill
cp /tmp/my-agent-skills/coursework-writing-style/SKILL.md ~/.claude/skills/coursework-writing-style/
cp -r /tmp/my-agent-skills/coursework-writing-style/agents ~/.claude/skills/coursework-writing-style/
```

```bash
# 4. Clean up the temporary directory
rm -rf /tmp/my-agent-skills
```

Restart the agent so the skill is discovered.

## Usage

Load `SKILL.md` into your agent environment. Invoke the skill when the user asks for help with coursework or student assignments.

Example prompt:

> "Use $coursework-writing-style to help me write a 1500-word course paper on the impact of AI on education. The assignment asks for an introduction, three main sections, and a conclusion, with APA citations."

Do not use it for published papers, creative writing, marketing copy, or social media content.

## Project Structure

```text
coursework-writing-style/
├── README.md
├── README.zh-CN.md
├── VERSION
├── SKILL.md
└── agents/
    └── openai.yaml
```

- `SKILL.md` — Core style rules and trigger conditions.
- `agents/openai.yaml` — UI metadata for skill lists and default prompt.

## Versioning

Current version: [v1.0.0](VERSION).

This is a pre-1.0 skill. Rules may be refined as more coursework writing scenarios are covered.

## Contributing

Contributions are welcome. See the [parent repository README](../README.md#contributing) for guidelines.
