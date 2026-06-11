# MemRouter

[简体中文](README.zh-CN.md)

> A skill and local tooling layer for routing conversational memory into deterministic markdown files.

Current version: `v0.5.0`

MemRouter is designed for AI agents that need memory to be:

- structured instead of dumped into one flat note
- separated by user, project, type, and time
- inspectable by humans
- recallable from predictable file paths

## What It Does

MemRouter provides four practical capabilities:

1. `decide`: estimate whether a candidate detail should be persisted and how.
2. `inspect`: show the deterministic route for a memory type and scope.
3. `remember`: write a memory entry into the routed markdown file.
4. `recall`: search the same routed scope to find prior memory again.

The core workflow is:

1. decide whether a detail is worth keeping
2. classify it into a memory type
3. route it to the right path
4. write it with safe dedupe behavior
5. recall it from the same scope later

## Versioning

This repository is currently documented as `v0.5.0`.

- `v0.5.0` means the routing model, write semantics, recall boundaries, and heuristic decision layer are stable enough for real use
- `v0.5.0` adds first-use legacy-memory migration rules, a cleaner legacy `MEMORY.md` handoff model, and clearer single-source-of-truth guidance for MemRouter adoption
- it is not yet a "finished" `1.0.0` because decision quality and recall quality still have obvious room to improve

The maintainer-facing local version roadmap is tracked in `VERSION_RECORDS.md`.

## Repository Layout

This repository is primarily the skill itself:

- [SKILL.md](SKILL.md): trigger description and operational guidance
- [agents/openai.yaml](agents/openai.yaml): UI-facing metadata
- [references/entry-format.md](references/entry-format.md): canonical markdown entry header and timestamp rules
- [references/memory-taxonomy.md](references/memory-taxonomy.md): memory type guidance
- [references/routing-policy.md](references/routing-policy.md): folder and retrieval rules
- [scripts/memrouter_core.py](scripts/memrouter_core.py): core routing, persistence, recall, and decision logic
- [scripts/memrouter_cli.py](scripts/memrouter_cli.py): command-line entrypoint
- [RELEASE_GUIDE.md](RELEASE_GUIDE.md): recommended release packaging contents and checklist

## Memory Types

MemRouter currently supports these canonical types:

- `profile`: durable facts about a user or identity
- `preferences`: stable style, language, tooling, or workflow preferences
- `project-facts`: project constraints, architecture, integrations, and assumptions
- `project-decisions`: explicit project choices and pivots
- `task`: actionable next steps or work state
- `session-summary`: dated recaps of a conversation or working session
- `ephemeral`: low-confidence but still useful temporary memory

See [references/memory-taxonomy.md](references/memory-taxonomy.md) for examples and classification boundaries.

## Routing Model

MemRouter routes by:

- `memory_type`
- `user_id`
- `project`
- `date`

Default vault-relative root:

```text
MemRouter/
```

Typical paths:

- `preferences` -> `MemRouter/users/<user_id>/preferences.md`
- `profile` -> `MemRouter/users/<user_id>/profile.md`
- `project-facts` -> `MemRouter/projects/<project_slug>/facts.md`
- `project-decisions` -> `MemRouter/projects/<project_slug>/decisions.md`
- `task` -> project or user task file, depending on whether project scope exists
- `session-summary` -> dated session note under project or user sessions
- `ephemeral` -> dated inbox note

Routing names are normalized into filesystem-safe slugs while preserving safe Unicode letters and digits, so non-ASCII project names do not collapse into the same fallback route.

## Write Semantics

Memory entries are written as compact markdown blocks such as:

```text
- 2026-06-05 | created_at: 2026-06-05T14:32:10+08:00 | topic: output-style | source: chat
  The user prefers concise Chinese answers.
```

Current write rules:

- continuation lines stay indented so multiline content remains one entry
- entries now store a precise `created_at` timestamp in addition to the route date
- default dedupe mode is `exact`
- `exact` treats the same topic, source, and body as the same memory even across dates or different timestamps
- `topic` mode is available when you provide a stable topic and want upsert behavior
- `none` always appends

See [references/entry-format.md](references/entry-format.md) for the exact header format and backward-compatibility rules.

## Recall Semantics

Recall follows the same route model used for writes:

1. inspect the direct note first
2. if needed, search the relevant scoped subtree

Important boundary:

- project memory recall does not spill into project `sessions/` unless the memory type itself is `session-summary`

Recall is currently line-match based rather than semantic ranking based.

## Quick Start

Inspect where a memory would go:

```bash
python scripts/memrouter_cli.py inspect --memory-type preferences --user-id alice
```

Decide whether a candidate memory should be stored:

```bash
python scripts/memrouter_cli.py decide --user-id alice --text "The user prefers concise Chinese answers."
```

Store memory with explicit topic-aware upsert:

```bash
python scripts/memrouter_cli.py remember --vault-root <vault-root> --memory-type preferences --user-id alice --dedupe-mode topic --topic output-style --text "The user prefers concise Chinese answers."
```

Recall memory:

```bash
python scripts/memrouter_cli.py recall --vault-root <vault-root> --memory-type preferences --user-id alice --query "concise Chinese"
```

## CLI Commands

`inspect`

- does not write or search
- only resolves the route

`decide`

- classifies whether a detail should be persisted
- returns `should_persist`, `memory_type`, `topic`, `dedupe_mode`, `confidence`, and `reason`
- currently uses heuristic decision logic rather than a model-backed classifier
- handles common English and Chinese cues for trivial chat, preferences, tasks, and topic inference

`remember`

- writes memory to the routed file
- supports `none`, `exact`, and `topic` dedupe modes
- accepts optional `--created-at` for an explicit ISO 8601 entry timestamp

`recall`

- searches the routed note first
- then broadens only within the same routed scope

## Testing

Run the built-in test suite with:

```bash
python -m unittest discover -s tests -v
```

Current coverage includes:

- route resolution for ASCII and Unicode names
- decision-layer persistence and classification heuristics in English and Chinese
- exact dedupe across dates
- timestamped entry formatting and timestamp-insensitive dedupe
- topic-aware upsert
- multiline entry formatting
- scoped recall boundaries
- CLI argument validation

## Current Limitations

- the decision layer is heuristic-first, not yet model-assisted
- Chinese support is now practical for common cases, but still rule-based rather than semantic
- recall is based on text matching, not semantic ranking or result summarization
- the repo is still maintained in a developer-friendly shape rather than a minimal distribution-only shape

## Design Principles

- do not save everything
- keep write and read rules symmetrical
- separate long-term memory from temporary context
- prefer stable naming and deterministic paths
- keep fallback behavior explicit rather than magical
