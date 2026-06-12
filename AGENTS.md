# AGENTS.md

Durable conventions for working with the `my-agent-skills` repository.

## Adding a new skill

When creating or importing a new skill into this monorepo:

1. Place the skill in its own directory at the repository root.
2. Ensure the skill has a valid `SKILL.md` with YAML frontmatter (`name`, `description`).
3. Create or update `agents/openai.yaml` with UI metadata.
4. Create `VERSION` and `VERSION_RECORDS.md` for the skill.
5. Create bilingual READMEs:
   - `README.md` in English
   - `README.zh-CN.md` in Simplified Chinese
6. Add a standardized `.gitignore` to the skill directory (copy from an existing skill).
7. **Update the root `README.md` and `README.zh-CN.md`:**
   - Add the skill to the **My Skills** table.
   - Add the skill to the **Project Structure** directory tree.
8. If the skill has working subdirectories (`agents/`, `references/`, `scripts/`, `assets/`), document them in the skill's README installation and project structure sections.

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
- Whenever a root or skill `VERSION` file is updated, create a git commit for that version update. Do not leave a version bump uncommitted.

## Versioning

- The repository has a single top-level `VERSION` file and a top-level `VERSION_RECORDS.md`.
- Each skill must also have its own `VERSION` file and `VERSION_RECORDS.md`.
- `VERSION` stores only the current version number.
- `VERSION_RECORDS.md` records:
  - what the current version changed
  - what the next planned version is
- When bumping a version, update the matching `VERSION`, `VERSION_RECORDS.md`, and any related README badges or version text together.
- A version bump must end with a git commit that includes the versioned content changes and the matching version metadata updates.
- The user is responsible for version bumps:
  - When modifying a skill, the user decides whether to update that skill's `VERSION`.
  - The user personally updates the root `VERSION` for major repository-wide changes.
- Keep badge versions in READMEs in sync with their corresponding `VERSION` file.

### When modifying the repository

Whenever you make changes to this repository (skill content, READMEs, structure, conventions, etc.):

1. Read the relevant version files:
   - The root `VERSION` and `VERSION_RECORDS.md` for repository-level changes.
   - The skill's `VERSION` and `VERSION_RECORDS.md` if you are modifying a skill.
2. Report the current version number(s) to the user.
3. Ask whether they want to bump any version.
4. Only update `VERSION`, `VERSION_RECORDS.md`, and related README badges/version text if the user explicitly confirms.
5. If a version was updated, create a git commit for that version change before finishing the task.

## This file will evolve

Add new conventions here as the repository grows. When updating this file, keep rules concise and actionable.
