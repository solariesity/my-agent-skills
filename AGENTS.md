# AGENTS.md

Durable conventions for working with the `my-agent-skills` repository.

## Adding a new skill

When creating or importing a new skill into this monorepo:

1. Place the skill in its own directory at the repository root.
2. Ensure the skill has a valid `SKILL.md` with YAML frontmatter (`name`, `description`).
3. Create or update `agents/openai.yaml` with UI metadata.
4. Create bilingual READMEs:
   - `README.md` in English
   - `README.zh-CN.md` in Simplified Chinese
5. Add a standardized `.gitignore` to the skill directory (copy from an existing skill).
6. **Update the root `README.md` and `README.zh-CN.md`:**
   - Add the skill to the **My Skills** table.
   - Add the skill to the **Project Structure** directory tree.
7. If the skill has working subdirectories (`agents/`, `references/`, `scripts/`, `assets/`), document them in the skill's README installation and project structure sections.

## Installation instructions in skill READMEs

All skill READMEs must use the same **clone-to-tmp** installation workflow. Do **not** copy the whole skill directory, because `README.md`, `README.zh-CN.md`, `tests/`, and other non-essential files should not be installed into the agent's skills folder.

Standard steps:

```bash
# 1. Clone the monorepo to a temporary directory
git clone git@github.com:solariesity/my-agent-skills.git /tmp/my-agent-skills

# 2. Create the skill directory in the agent's skills folder
mkdir -p ~/.claude/skills/<skill-name>
# Or, for Codex:
# mkdir -p ~/.codex/skills/<skill-name>

# 3. Copy only the working parts of the skill
cp /tmp/my-agent-skills/<skill-name>/SKILL.md ~/.claude/skills/<skill-name>/
cp -r /tmp/my-agent-skills/<skill-name>/agents ~/.claude/skills/<skill-name>/
# Copy references/ and/or scripts/ only if the skill has them.

# 4. Clean up the temporary directory
rm -rf /tmp/my-agent-skills
```

Restart the agent so the skill is discovered.

## README structure

Follow the `github-readme-style` skill conventions. Each skill README should include, when applicable:

1. **Title / Header**
2. **Description**
3. **Features**
4. **Installation**
5. **Usage**
6. **Project Structure**
7. **Versioning**
8. **Contributing**
9. **License**

Keep paragraphs short and use code blocks with language tags.

## Git conventions

- The root `.gitignore` excludes `.claude/`, `.codex/`, temporary directories, and common generated files.
- Each skill directory has its own `.gitignore` using the same standard template.
- Do not commit agent-local state (`.claude/`, `.codex/`) or temporary files.

## Versioning

- The repository uses a single top-level `VERSION` file.
- Individual skills do not maintain separate version files unless they have a specific reason.
- Keep badge versions in READMEs in sync with `VERSION`.

## This file will evolve

Add new conventions here as the repository grows. When updating this file, keep rules concise and actionable.
