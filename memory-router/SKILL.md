---
name: memory-router
description: Route conversational memory into structured markdown files instead of one flat memory log. Use when an AI agent needs to remember or save a user preference, profile fact, project fact, project decision, task state, or session summary; choose the correct deterministic file path by user/project/time scope; update existing file-based memory safely; or recall prior routed context across multiple sessions. The current decision layer supports practical English and Chinese heuristics for trivial-chat filtering, preference detection, task detection, and topic inference.
---

# Memory Router

Use this skill when memory should be organized, inspectable, and easy to recall later.
This repository is currently documented as `v0.5.0`, which adds first-use legacy-memory migration rules, a cleaner `MEMORY.md` handoff model, and clearer single-source-of-truth guidance for durable memory.

Prefer it over a single append-only note when the user has:

- multiple projects
- multiple users
- long-running sessions
- stable preferences or facts worth preserving

## Use The Main Entry Point

Prefer `scripts/memrouter_cli.py`.

Inspect:

```bash
python scripts/memrouter_cli.py inspect --memory-type preferences --user-id alice
```

Decide:

```bash
python scripts/memrouter_cli.py decide --user-id alice --text "The user prefers concise Chinese answers."
```

Remember:

```bash
python scripts/memrouter_cli.py remember --vault-root <vault-root> --memory-type preferences --user-id alice --dedupe-mode topic --topic output-style --created-at 2026-06-04T14:32:10+08:00 --text "The user prefers concise Chinese answers."
```

Recall:

```bash
python scripts/memrouter_cli.py recall --vault-root <vault-root> --memory-type preferences --user-id alice --query "concise Chinese"
```

## First-Use Migration

If the workspace already has legacy memory files, migrate durable memory into memory-router before normal day-to-day use.

Typical legacy sources include:

- `MEMORY.md`
- dated memory logs
- profile or preference notes
- project fact or decision notes
- other markdown notes that already act as long-term memory

Migration rules:

- migrate durable memory, not every historical file verbatim
- extract and re-route stable facts, preferences, project facts, project decisions, and useful session summaries into memory-router
- do not blindly import todos, reminders, diaries, or raw chat transcripts; either keep them external or summarize them first
- use normal memory-router classification and dedupe rules during migration so imported memory lands in the same canonical files as future memory
- after migration, treat memory-router as the single source of truth for durable memory
- do not keep writing durable memory to both legacy memory files and memory-router

After migration, rewrite the legacy `MEMORY.md` into a routing stub instead of a content store.
That stub should say that the workspace now uses memory-router, point to the canonical memory root, list the route families, and note which operational files still live outside memory-router.

## Follow This Workflow

### 1. Decide Whether To Persist

Do not save everything.
Prefer `decide` first when classification or durability is unclear.
The current heuristic layer can recognize common English and Chinese cues, including Chinese filler phrases such as `好的` or `明白了`, plus common preference and task wording.

Prefer durable information such as:

- stable user facts
- user preferences
- project constraints
- project decisions
- ongoing tasks
- session summaries worth revisiting

Skip trivial chat, one-off wording, and low-value noise.

Do not persist passwords, secrets, API keys, access tokens, recovery codes, or other private credentials in memory-router.
If the content is sensitive, return `should_persist: false` and keep it out of markdown memory entirely.

### 2. Classify The Memory

Use one of these canonical types:

- `profile`
- `preferences`
- `project-facts`
- `project-decisions`
- `task`
- `session-summary`
- `ephemeral`

Read [references/memory-taxonomy.md](references/memory-taxonomy.md) if classification is ambiguous.

If confidence is low but the detail is still useful, use `ephemeral`.

Use this boundary rule set when types seem close:

- `profile` is for durable facts about the user as a person.
- `preferences` is only for how the user wants the agent to work or respond.
- `project-facts` is for project or workspace facts, constraints, paths, environment details, or installed integrations.
- `project-decisions` is for adopted project rules, policies, mechanisms, and deliberate choices.

Prefer these tie-breakers:

- "Who the user is" -> `profile`
- "How the user wants the agent to behave" -> `preferences`
- "What is true about the current workspace" -> `project-facts`
- "What this workspace has decided to do" -> `project-decisions`

Specific guidance:

- Personal interests such as favorite music, shows, or characters usually belong in `profile`, not `preferences`.
- Project paths, working-directory limits, repository layout, and installed workspace tooling belong in `project-facts`, not `profile`.
- Behavior rules that are specific to one project or workspace belong in `project-decisions`, even if they affect agent style or workflow.

### 3. Resolve The Route

Route by:

- `memory_type`
- `user_id`
- `project`
- `date`

Read [references/routing-policy.md](references/routing-policy.md) for the exact folder layout and naming rules.

Use stable filesystem-safe slugs for users and projects.
Preserve non-ASCII letters and digits when they are safe so names like Chinese project titles do not collapse into `general`.

Treat `user_id` as a stable machine-facing identifier, not a display name or roleplay nickname.
Use one canonical `user_id` per user across the same vault.
If a workspace already has stored memory, keep using the existing routed `user_id` slug instead of inventing a new alias.

### 4. Write Or Merge

Write compact, human-readable entries.
Indent every continuation line so one memory item always remains one markdown block.

Preferred shape:

```text
- 2026-06-04 | created_at: 2026-06-04T14:32:10+08:00 | topic: output-style | source: chat
  The user prefers concise Chinese answers.
```

Read [references/entry-format.md](references/entry-format.md) for the exact timestamp and header rules.

Default to exact-dedupe when no stable topic label is available.
Use topic-aware upsert only when you can provide an explicit stable topic such as `output-style`, `language`, `architecture`, or `next-step`.
Use append-only behavior only when the task explicitly needs chronological duplicates.
Treat exact-dedupe as “same topic, same source, same body” even if the request happens again on a later date or with a different `created_at` timestamp.

### 5. Recall From The Same Scope

Read with the same routing logic used during writes.

Inspect the direct note first.
If needed, broaden only to the same route family:

- user memory -> `memory-router/users/<user_id>/`
- project memory -> `memory-router/projects/<project_slug>/`
- project sessions -> `memory-router/projects/<project_slug>/sessions/`
- user sessions -> `memory-router/sessions/<user_id>/`
- inbox memory -> `memory-router/inbox/`

Do not let project memory fallback search spill into `sessions/` unless the memory type itself is `session-summary`.
Use broader semantic memory only after scoped file recall fails.

## Behavioral Rules

- Keep write and read rules symmetrical.
- If legacy memory exists, migrate durable memory before normal use.
- After migration, treat memory-router as the single source of truth for durable memory.
- Do not keep dual-writing durable memory to both legacy files and memory-router.
- Do not mix user preferences into project decision files.
- Do not mix personal identity facts into project fact files.
- Do not store project paths, workspace constraints, or environment details in `profile`.
- Do not store short-lived chatter as long-term memory.
- Do not store passwords, secrets, or credentials in markdown memory.
- Use `default-user` when no stable user id is available.
- Use `general` when a project-scoped route is required but no stable project name exists.
- Use the dated inbox route for low-confidence but still useful memory.

## References

- [references/entry-format.md](references/entry-format.md)
- [references/memory-taxonomy.md](references/memory-taxonomy.md)
- [references/routing-policy.md](references/routing-policy.md)
