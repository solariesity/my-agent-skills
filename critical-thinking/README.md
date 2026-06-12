# critical-thinking

> Independent judgment and critical thinking for substantive conversations.

Use this skill when the assistant needs to express opinions, evaluate claims, or discuss ideas with the user. It defines an intellectual stance: have independent judgment, argue based on facts, and disagree when appropriate.

## Features

- Form independent judgments instead of agreeing blindly.
- Base arguments on facts and reliable sources.
- Explain reasoning clearly.
- Push back on unreasonable or misleading requests.
- Stay humble and correct mistakes when wrong.

## Installation

This skill lives inside the [`my-agent-skills`](https://github.com/solariesity/my-agent-skills) monorepo. Clone that repository and enter the critical-thinking directory:

```bash
git clone https://github.com/solariesity/my-agent-skills.git
cd my-agent-skills/critical-thinking
```

### Install Only the Skill

If you only want to install critical-thinking as a skill in an agent environment, use a temporary clone:

```bash
# 1. Clone the monorepo to a temporary directory
git clone https://github.com/solariesity/my-agent-skills.git /tmp/my-agent-skills

# 2. Copy only the skill definition to the target location
mkdir -p ~/.codex/skills/critical-thinking
cp /tmp/my-agent-skills/critical-thinking/SKILL.md ~/.codex/skills/critical-thinking/

# 3. Remove the temporary directory
rm -rf /tmp/my-agent-skills
```

On Windows, use `C:\Users\<username>\.codex\skills\critical-thinking\` as the target path.

## Usage

Load `SKILL.md` into your agent environment. The skill applies automatically in discussion, analysis, and judgment tasks. Skip it only for pure execution requests such as "rename this file to X".

## Project Structure

```text
critical-thinking/
├── README.md
├── README.zh-CN.md
└── SKILL.md
```

- `SKILL.md` — Core behavior specification.

## Versioning

Current version: `v0.1.0`.

This is a pre-1.0 skill. Guidelines may evolve as usage patterns become clearer.

## Contributing

Suggestions and pull requests are welcome.
