---
name: skill-review
description: >
  Guide the review and improvement of skills inside the my-agent-skills monorepo.
  When the user asks to evaluate, check, or optimize a skill, use this skill to:
  inspect the target skill's files, find convention violations, compare with similar
  community skills, propose concrete changes, and—after user approval—implement,
  version, and push. Do NOT use this skill for code reviews, paper reviews,
  or tasks outside the monorepo.
---

# Skill Review Guide

Use this skill whenever the user wants to review, evaluate, or improve a skill inside the `my-agent-skills` monorepo.

## When to use

Trigger when the user says things like:

- "看看这个 skill 写得怎么样"
- "评价一下这个 skill"
- "对比一下类似的 skill"
- "这个 skill 有没有问题"
- "优化一下这个 skill"
- "下一个 skill"

Do NOT use this skill for code reviews, paper reviews, writing tasks, or anything outside the monorepo.

## Review workflow

For the target skill (the one the user names, or the next one in alphabetical order if the user is going through all skills):

### 1. Load the skill

Read these files if they exist:

- `<skill>/SKILL.md`
- `<skill>/README.md`
- `<skill>/README.zh-CN.md`
- `<skill>/VERSION`
- `<skill>/agents/openai.yaml`
- `<skill>/.gitignore`

### 2. Check obvious issues

Inspect against monorepo conventions and common mistakes:

- [ ] Skill folder name matches `name` in `SKILL.md` frontmatter.
- [ ] Frontmatter `description` is clear and describes when to use the skill.
- [ ] `SKILL.md` has a clear scope, trigger conditions, and execution rules.
- [ ] Bilingual READMEs exist (`README.md` + `README.zh-CN.md`).
- [ ] README title matches skill name.
- [ ] README has a version badge linked to `./VERSION`.
- [ ] `VERSION` file exists and matches badge/version text in both READMEs.
- [ ] `agents/openai.yaml` exists with `display_name`, `short_description`, and `default_prompt`.
- [ ] `default_prompt` is concise (ideally 1-2 sentences) and invokes `$<skill-name>`.
- [ ] Installation instructions copy both `SKILL.md` and `agents/` (if `agents/` exists).
- [ ] Project structure in README lists all actual files, including `agents/openai.yaml` and `VERSION`.
- [ ] No outdated project names (e.g., `WorkBuddy`) or incorrect slash commands (e.g., `/<skill-name>`).
- [ ] `.gitignore` exists and excludes `.claude/`, `.codex/`, temp files, OS files, and IDE files.
- [ ] No obvious typos or inconsistent formatting.

If issues are found, list them as concrete, numbered items with file references.

### 3. Compare with similar community skills

Search for comparable skills on GitHub / the web. Use 1-3 queries such as:

- "Claude Code Codex skill <topic> github"
- "<topic> agent skill codex"

Fetch 1-3 promising READMEs or `SKILL.md` files. Identify:

- What they do better (structure, workflow, examples, stopping rules, boundaries).
- What patterns are worth borrowing.
- What pitfalls they avoid.

Summarize findings with source links.

### 4. Present the evaluation

Structure the response as:

1. Overall verdict (good / okay / needs work).
2. Strengths (3-5 bullet points).
3. Issues found in step 2 (numbered).
4. Optimization ideas from step 3 (numbered, with source links).
5. Recommended priority: which items to fix now, which are optional.
6. Ask: "要不要我现在改？"

Wait for explicit user confirmation before making edits.

### 5. Implement changes

If the user agrees:

- Apply the agreed changes.
- Update `VERSION` only after the user confirms a version bump.
- Reinstall the skill to `~/.claude/skills/<skill-name>/` (copy `SKILL.md` and `agents/`).
- Commit and push only after the user confirms.

### 6. Version and push

After changes are made:

- Report the current version from `<skill>/VERSION`.
- Recommend a new version using Semantic Versioning:
  - Patch (`0.0.x`) for small fixes or documentation updates.
  - Minor (`0.x.0`) for new rules, examples, or feature additions.
  - Major (`x.0.0`) for breaking changes or skill repositioning.
- Ask: "当前版本是 X。建议升到 Y。是否更新版本号并 push？"
- If yes, update the badge and version text in both READMEs, commit, push, and reinstall if needed.

## Tone

- Be direct but constructive.
- Prefer concrete file references.
- Do not over-engineer; respect that pre-1.0 skills can evolve incrementally.
