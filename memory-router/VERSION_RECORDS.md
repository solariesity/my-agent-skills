# Version Records

This file tracks memory-router versions, what each version introduced, and the roadmap.

## Current Version

### v1.0.0

Current stable baseline.

**Added / Changed:**

- Established deterministic routing for structured conversational memory files.
- Added practical bilingual heuristics for trivial-chat filtering, preference detection, task detection, and topic inference.
- Defined write, recall, and routing boundaries for user, project, type, and time scopes.
- Packaged the skill for Codex / Claude Code installation with bilingual docs, agent metadata, scripts, and references.

**Known limits:**

- Decision behavior is still heuristic-first rather than model-assisted.
- Recall remains relatively simple compared with ranked or synthesized retrieval.
- Topic inference is practical but still rule-based.

## Previous Versions

### v0.5.0

Earlier stable pre-`v1.0.0` baseline.

**Included:**

- First-use legacy-memory migration rules for existing flat memory files.
- Cleaner legacy `MEMORY.md` handoff model.
- Clearer single-source-of-truth guidance for memory-router adoption.
- Routing model, write semantics, recall boundaries, and heuristic decision layer stable enough for real use.

### v0.3.0

First reasonably stable bilingual-and-timestamped baseline for the current architecture.

**Included:**

- Deterministic route resolution by memory type, user, project, and date.
- Markdown persistence with safe defaults for dedupe.
- Topic-aware upsert when a stable topic is available.
- Scoped recall that respects routing boundaries.
- Unicode-safe route slugs for user and project names.
- Heuristic `decide` layer for persistence and classification.
- Practical Chinese and English heuristics for trivial-chat filtering.
- Chinese preference and task detection plus topic inference.
- Less aggressive project fallback so Chinese preferences are less likely to be misrouted into `project-facts`.
- Precise `created_at` timestamps in entry headers.
- Documented canonical entry format plus backward compatibility for legacy entries without `created_at`.
- Unit tests covering route logic, write behavior, recall boundaries, CLI validation, and basic decision heuristics.

## Roadmap

### v1.0.1

Possible focus:

- Optional model-assisted decision adapter behind `decide_memory_action()`.
- Deterministic validation and routing guardrails after model output.
- Improved recall output from raw lines to grouped entries.
- Expanded tests for ambiguous classification and mixed-language cases.
