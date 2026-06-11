# Routing Policy

Use this file when you need the exact folder layout, naming rules, or retrieval scope for MemRouter.

## Default Root

Use this vault-relative root unless the project defines another one:

```text
MemRouter/
```

If the workspace already has a legacy memory system, migrate durable memory into the configured MemRouter root before writing new long-term memory.
After that handoff, MemRouter becomes the canonical durable-memory location for the workspace.

## Canonical Routes

### User scope

- `profile`
  - `MemRouter/users/<user_id>/profile.md`
  - section: `Facts`
- `preferences`
  - `MemRouter/users/<user_id>/preferences.md`
  - section: `Entries`
- `task` without project
  - `MemRouter/users/<user_id>/tasks.md`
  - section: `Entries`

### Project scope

- `project-facts`
  - `MemRouter/projects/<project_slug>/facts.md`
  - section: `Entries`
- `project-decisions`
  - `MemRouter/projects/<project_slug>/decisions.md`
  - section: `Entries`
- `task` with project
  - `MemRouter/projects/<project_slug>/tasks.md`
  - section: `Entries`

### Session scope

- `session-summary` with project
  - `MemRouter/projects/<project_slug>/sessions/<year>/<yyyy-mm-dd>.md`
  - section: `Summary`
- `session-summary` without project
  - `MemRouter/sessions/<user_id>/<year>/<yyyy-mm-dd>.md`
  - section: `Summary`

### Inbox scope

- `ephemeral`
  - `MemRouter/inbox/<year>/<yyyy-mm-dd>.md`
  - section: `Entries`

## Naming Rules

- case-fold alphabetic ids when applicable
- preserve Unicode letters and digits when they are filesystem-safe
- replace whitespace and punctuation with `-`
- collapse repeated dashes
- use `default-user` when no user id is known
- use `general` when a project route is required but no stable project name exists

## Writing Rules

- prefer compact bullet entries with timestamp and topic metadata
- use the canonical header order `date -> created_at -> topic -> source`
- indent continuation lines so multiline content stays inside the same entry
- keep entries readable to humans
- default to exact-dedupe when no stable topic label is available
- use topic-aware upsert only with an explicit stable topic label when updating durable facts or preferences
- treat exact-dedupe as the same topic, source, and body even if the reminder happens on a later date
- exact dedupe also ignores `created_at`

Read [entry-format.md](entry-format.md) for the exact field order, timestamp rules, and backward-compatibility behavior.

## Legacy Migration Rules

When a workspace already contains old memory files, migrate the durable parts first instead of starting dual writes.

Recommended migration sources:

- legacy `MEMORY.md`
- dated memory logs that already act as working-session memory
- profile or preference notes
- project rules, architecture notes, or decision notes

Recommended migration behavior:

- extract durable memory and rewrite it into the canonical MemRouter routes
- keep migration symmetric with normal routing rules so imported memory lands in the same files future memory will use
- use `session-summary` for historical logs when the source is a recap of what happened, changed, or remains unresolved
- use normal dedupe or topic-aware upsert during migration so imported memory does not create obvious duplicates

Do not blindly migrate these into MemRouter as raw files:

- todo lists
- reminder data
- diary files
- raw transcripts
- other operational files whose main value is chronological rather than durable

Keep those external, or summarize them before importing only the durable parts.

## Legacy MEMORY.md Handoff

After migration, the old `MEMORY.md` should stop being a long-term content store and become a routing stub.

Recommended responsibilities for that stub:

- say that the workspace now uses MemRouter for durable memory
- name the canonical memory root
- show the stable route families such as `profile`, `preferences`, `project-facts`, `project-decisions`, `task`, `session-summary`, and `ephemeral`
- say which files still live outside MemRouter, such as todos, reminders, or diary files
- avoid storing new durable memory content directly in the stub

Recommended minimal shape:

```text
# MEMORY.md

This workspace uses MemRouter for durable memory.
Do not append long-term memory here.

Canonical memory root: <configured-root>

Routing:
- profile -> users/<user_id>/profile.md
- preferences -> users/<user_id>/preferences.md
- project-facts -> projects/<project_slug>/facts.md
- project-decisions -> projects/<project_slug>/decisions.md
- task -> projects/<project_slug>/tasks.md or users/<user_id>/tasks.md
- session-summary -> projects/<project_slug>/sessions/<year>/<yyyy-mm-dd>.md
- ephemeral -> inbox/<year>/<yyyy-mm-dd>.md

Not stored in MemRouter:
- todos
- reminders
- diaries
- raw transcripts
```

## Retrieval Rules

- resolve the likely direct note first
- search only the relevant subtree second
- keep project memory fallback out of `projects/<project_slug>/sessions/` unless recalling `session-summary`
- use broader recall only as fallback
