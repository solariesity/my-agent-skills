# Memory Router

[![Version](https://img.shields.io/badge/version-v1.0.0-blue)](./VERSION)

> Route conversational memory into deterministic markdown files instead of dumping everything into one flat log.

memory-router is a skill and local tooling layer for AI agents that need structured, inspectable, and recallable memory. It classifies candidate details, routes them to predictable file paths by user, project, type, and date, and recalls them from the same scope later.

## Features

- **Decide** whether a candidate detail is worth persisting and how it should be stored.
- **Inspect** the deterministic route for a memory type and scope before writing.
- **Remember** entries into routed markdown files with safe dedupe behavior.
- **Recall** prior memory from the same scoped subtree.
- Practical heuristic support for common English and Chinese cues.
- Filesystem-safe slugging that preserves Unicode project and user names.

## Installation

This skill is part of the `my-agent-skills` monorepo. Install it by cloning the repo to a temporary directory and copying only the working files into your agent's skills folder (READMEs, tests, and other non-essential files are left out).

```bash
# 1. Clone the monorepo to a temporary directory
git clone git@github.com:solariesity/my-agent-skills.git /tmp/my-agent-skills

# 2. Create the skill directory in the agent's skills folder
mkdir -p ~/.claude/skills/memory-router
# Or, for Codex:
# mkdir -p ~/.codex/skills/memory-router

# 3. Copy the working parts of the skill
cp /tmp/my-agent-skills/memory-router/SKILL.md ~/.claude/skills/memory-router/
cp -r /tmp/my-agent-skills/memory-router/agents ~/.claude/skills/memory-router/
cp -r /tmp/my-agent-skills/memory-router/references ~/.claude/skills/memory-router/
cp -r /tmp/my-agent-skills/memory-router/scripts ~/.claude/skills/memory-router/
```

```bash
# 4. Clean up the temporary directory
rm -rf /tmp/my-agent-skills
```

Restart the agent so the skill is discovered.

## Usage

Inspect where a preference would be routed:

```bash
python scripts/memrouter_cli.py inspect \
  --memory-type preferences \
  --user-id alice
```

Decide whether a detail should be persisted:

```bash
python scripts/memrouter_cli.py decide \
  --user-id alice \
  --text "The user prefers concise Chinese answers."
```

Store a memory with topic-aware upsert:

```bash
python scripts/memrouter_cli.py remember \
  --vault-root ./memories \
  --memory-type preferences \
  --user-id alice \
  --dedupe-mode topic \
  --topic output-style \
  --text "The user prefers concise Chinese answers."
```

Recall previously stored memory:

```bash
python scripts/memrouter_cli.py recall \
  --vault-root ./memories \
  --memory-type preferences \
  --user-id alice \
  --query "concise Chinese"
```

## Project Structure

```text
memory-router/
├── README.md
├── README.zh-CN.md
├── VERSION
├── .gitignore
├── SKILL.md
├── VERSION_RECORDS.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── entry-format.md
│   ├── memory-taxonomy.md
│   └── routing-policy.md
├── scripts/
│   ├── memrouter_cli.py
│   └── memrouter_core.py
└── tests/
```

- `SKILL.md` — Trigger description and operational guidance for agent integration.
- `agents/openai.yaml` — UI-facing metadata for skill marketplaces.
- `references/` — Canonical rules for entries, memory taxonomy, and routing policy.
- `scripts/` — CLI entry point and core routing, persistence, recall, and decision logic.
- `tests/` — Unit tests covering routes, decisions, dedupe, recall, and CLI validation.

## Memory Types

memory-router supports these canonical types:

| Type | Purpose |
|------|---------|
| `profile` | Durable facts about a user or identity |
| `preferences` | Stable style, language, tooling, or workflow preferences |
| `project-facts` | Project constraints, architecture, integrations, and assumptions |
| `project-decisions` | Explicit project choices and pivots |
| `task` | Actionable next steps or work state |
| `session-summary` | Dated recaps of a conversation or working session |
| `ephemeral` | Low-confidence but useful temporary memory |

See [references/memory-taxonomy.md](references/memory-taxonomy.md) for examples and classification boundaries.

## Routing Model

memory-router routes memory by:

- `memory_type`
- `user_id`
- `project`
- `date`

Default vault-relative root is `memory-router/`. Typical paths:

- `preferences` → `memory-router/users/<user_id>/preferences.md`
- `profile` → `memory-router/users/<user_id>/profile.md`
- `project-facts` → `memory-router/projects/<project_slug>/facts.md`
- `project-decisions` → `memory-router/projects/<project_slug>/decisions.md`
- `task` → project task file or user task file, depending on scope
- `session-summary` → dated session note under project or user sessions
- `ephemeral` → dated inbox note

Routing names are normalized into filesystem-safe slugs while preserving safe Unicode letters and digits, so non-ASCII project names do not collapse into the same fallback route.

## Write Semantics

Memory entries are written as compact markdown blocks:

```text
- 2026-06-05 | created_at: 2026-06-05T14:32:10+08:00 | topic: output-style | source: chat
  The user prefers concise Chinese answers.
```

Current write rules:

- Continuation lines stay indented so multiline content remains one entry.
- Each entry stores a precise `created_at` timestamp in addition to the route date.
- Default dedupe mode is `exact`.
- `exact` treats the same topic, source, and body as the same memory even across dates.
- `topic` mode is available for stable-topic upsert behavior.
- `none` always appends.

See [references/entry-format.md](references/entry-format.md) for the exact header format and backward-compatibility rules.

## Recall Semantics

Recall follows the same route model used for writes:

1. Inspect the direct note first.
2. If needed, search the relevant scoped subtree.

Important boundary: project memory recall does not spill into project `sessions/` unless the memory type itself is `session-summary`.

Recall is currently line-match based rather than semantic ranking based.

## Versioning

Current version: [v1.0.0](VERSION).

memory-router follows semantic versioning in spirit. `v1.0.0` means the routing model, write semantics, recall boundaries, and heuristic decision layer are stable enough for real use, but decision quality and recall quality still have room to improve before a `1.0.0` release.

The local version roadmap is tracked in [VERSION_RECORDS.md](VERSION_RECORDS.md).

## Testing

Run the built-in test suite with:

```bash
python -m unittest discover -s tests -v
```

Current coverage includes:

- Route resolution for ASCII and Unicode names
- Decision-layer persistence and classification heuristics in English and Chinese
- Exact dedupe across dates
- Timestamped entry formatting and timestamp-insensitive dedupe
- Topic-aware upsert
- Multiline entry formatting
- Scoped recall boundaries
- CLI argument validation

## Current Limitations

- The decision layer is heuristic-first, not yet model-assisted.
- Chinese support is practical for common cases, but still rule-based rather than semantic.
- Recall is based on text matching, not semantic ranking or result summarization.
- The repository is currently maintained in a developer-friendly shape rather than a minimal distribution-only shape.

## Contributing

Contributions are welcome. See the [parent repository README](../README.md#contributing) for guidelines.

## Design Principles

- Do not save everything.
- Keep write and read rules symmetrical.
- Separate long-term memory from temporary context.
- Prefer stable naming and deterministic paths.
- Keep fallback behavior explicit rather than magical.

## License

This project is licensed under the [MIT License](../LICENSE).
