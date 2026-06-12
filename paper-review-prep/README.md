# paper-review-prep

> Systematic research paper analysis and presentation preparation.

Use this skill when preparing for a group meeting or presentation by analyzing a research paper. Typical triggers include: "review this paper", "prepare a literature summary", "group meeting prep", or similar academic paper review tasks.

## Features

- Read and analyze papers systematically.
- Generate concise summaries.
- Explain papers in plain language.
- Provide formal academic phrasing.
- Build clear presentation outlines.

## Installation

This skill lives inside the [`my-agent-skills`](https://github.com/solariesity/my-agent-skills) monorepo. Clone that repository and enter the paper-review-prep directory:

```bash
git clone https://github.com/solariesity/my-agent-skills.git
cd my-agent-skills/paper-review-prep
```

### Install Only the Skill

If you only want to install paper-review-prep as a skill in an agent environment, use a temporary clone:

```bash
# 1. Clone the monorepo to a temporary directory
git clone https://github.com/solariesity/my-agent-skills.git /tmp/my-agent-skills

# 2. Copy only the skill definition to the target location
mkdir -p ~/.codex/skills/paper-review-prep
cp /tmp/my-agent-skills/paper-review-prep/SKILL.md ~/.codex/skills/paper-review-prep/

# 3. Remove the temporary directory
rm -rf /tmp/my-agent-skills
```

On Windows, use `C:\Users\<username>\.codex\skills\paper-review-prep\` as the target path.

## Usage

Load `SKILL.md` into your agent environment. The skill triggers automatically when the user asks for paper analysis, literature review, or group-meeting preparation.

## Project Structure

```text
paper-review-prep/
├── README.md
├── README.zh-CN.md
└── SKILL.md
```

- `SKILL.md` — Core workflow and output format specification.

## Versioning

Current version: `v0.1.0`.

This is a pre-1.0 skill. The workflow may evolve based on different meeting and presentation styles.

## Contributing

Suggestions and pull requests are welcome.
