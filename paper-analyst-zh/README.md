# Paper Analyst ZH

[![Version](https://img.shields.io/badge/version-v0.3.0-blue)](./VERSION)

Translate and deeply analyze English computer science and engineering papers in Chinese. Also supports group meeting presentation preparation.

## Description

`paper-analyst-zh` is a Codex / Claude Code skill for Chinese readers who want to understand English CS or engineering papers in Chinese. It produces a faithful full-text translation, a plain-language explanation for non-specialists, a formal academic expression, a professional deep analysis of methods, experiments, results, strengths, weaknesses, and reproduction value, and a structured presentation outline for group meetings.

If the source is a PDF, the skill automatically hands off to the `pdf` skill first.

## Features

- Full Chinese translation of English papers, section by section.
- Plain-language summary for non-specialist readers.
- Formal academic expression (规范学术表述) — a polished Chinese restatement of the paper's contributions.
- Professional analysis covering motivation, methods, experiments, ablations, and limitations.
- Structured presentation outline (汇报大纲) for group meeting preparation.
- Automatic PDF ingestion via the `pdf` skill.
- Multiple reading modes: quick, detailed (default), report prep, and reproduction prep.
- Triggered by Chinese phrases such as 组会, 文献汇报, 帮我梳理这篇论文, etc.
- Produces two files by default: `paper.translation.zh.md` and `paper.analysis.zh.md`.

## Installation

This skill is part of the `my-agent-skills` monorepo. Install it by cloning the repo to a temporary directory and copying only the working files into your agent's skills folder (READMEs, tests, and other non-essential files are left out).

```bash
# 1. Clone the monorepo to a temporary directory
git clone git@github.com:solariesity/my-agent-skills.git /tmp/my-agent-skills

# 2. Create the skill directory in the agent's skills folder
mkdir -p ~/.claude/skills/paper-analyst-zh
# Or, for Codex:
# mkdir -p ~/.codex/skills/paper-analyst-zh

# 3. Copy the working parts of the skill
cp /tmp/my-agent-skills/paper-analyst-zh/SKILL.md ~/.claude/skills/paper-analyst-zh/
cp -r /tmp/my-agent-skills/paper-analyst-zh/agents ~/.claude/skills/paper-analyst-zh/
cp -r /tmp/my-agent-skills/paper-analyst-zh/references ~/.claude/skills/paper-analyst-zh/
```

```bash
# 4. Clean up the temporary directory
rm -rf /tmp/my-agent-skills
```

Restart the agent so the skill is discovered.

## Usage

Invoke the skill explicitly:

```text
/paper-analyst-zh
```

Or ask the agent to use it directly:

```text
Use $paper-analyst-zh to translate and analyze this English paper in Chinese.
```

For group meeting preparation, use natural Chinese:

```text
帮我梳理这篇论文，准备组会汇报。
```

When given a local PDF, the skill will first extract its content and then generate:

- `paper.translation.zh.md` — full Chinese translation.
- `paper.analysis.zh.md` — snapshot, plain explanation, formal academic expression, professional analysis, presentation outline (when applicable), and glossary.

## Project Structure

```text
paper-analyst-zh/
├── SKILL.md              # Skill behavior and workflow
├── README.md             # English documentation
├── README.zh-CN.md       # Chinese documentation
├── VERSION               # Current version
├── .gitignore
├── agents/
│   └── openai.yaml       # UI metadata (display name, default prompt)
└── references/
    └── analysis-checklist.md  # Analysis checklist for experiments
```

## Versioning

Current version: [v0.3.0](VERSION).

This skill is versioned together with the parent repository.

## Contributing

Contributions are welcome. See the [parent repository README](../README.md#contributing) for guidelines.
