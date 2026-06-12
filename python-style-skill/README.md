# python-style-skill

> Behavior-preserving Python style cleanup for research and training code.

Use this skill when reviewing or standardizing Python naming, module or file names, Chinese-first comments or docstrings, and stable parseable training or debug output without breaking external contracts.

## Features

- Clean up mixed naming conventions without changing behavior.
- Standardize module and file names.
- Keep comments and docstrings mostly Chinese when the project allows it.
- Stabilize training logs and debug output for downstream parsers.
- Preserve externally consumed names and output fields as contracts.

## Installation

This skill lives inside the [`my-agent-skills`](https://github.com/solariesity/my-agent-skills) monorepo. Clone that repository and enter the python-style-skill directory:

```bash
git clone https://github.com/solariesity/my-agent-skills.git
cd my-agent-skills/python-style-skill
```

### Install Only the Skill

If you only want to install python-style-skill as a skill in an agent environment, use a temporary clone:

```bash
# 1. Clone the monorepo to a temporary directory
git clone https://github.com/solariesity/my-agent-skills.git /tmp/my-agent-skills

# 2. Copy only the skill definition to the target location
mkdir -p ~/.codex/skills/python-style-skill
cp /tmp/my-agent-skills/python-style-skill/SKILL.md ~/.codex/skills/python-style-skill/

# 3. Remove the temporary directory
rm -rf /tmp/my-agent-skills
```

On Windows, use `C:\Users\<username>\.codex\skills\python-style-skill\` as the target path.

## Usage

Load `SKILL.md` into your agent environment. The skill triggers automatically when you ask the agent to review, clean, or standardize Python code in a research or training codebase.

Typical prompts:

- "Review this Python file for style issues."
- "Clean up the naming in this training script."
- "Make the training logs easier to parse without changing the logic."

## Project Structure

```text
python-style-skill/
├── README.md
├── README.zh-CN.md
└── SKILL.md
```

- `SKILL.md` — Core behavior specification and style rules.

## Versioning

Current version: `v0.1.0`.

This is a pre-1.0 skill. Rules may evolve as more Python cleanup patterns are identified.

## Contributing

Suggestions and pull requests are welcome.
