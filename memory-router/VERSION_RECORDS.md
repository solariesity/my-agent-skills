# Version Records

This file tracks memory-router versions, what each version introduced, and the roadmap.

## Current Version

### v0.5.0

Current stable baseline.

**Added / Changed:**

- First-use legacy-memory migration rules for existing flat memory files.
- Cleaner legacy `MEMORY.md` handoff model.
- Clearer single-source-of-truth guidance for memory-router adoption.
- Routing model, write semantics, recall boundaries, and heuristic decision layer are stable enough for real use.

**Known limits:**

- Decision layer is heuristic-first, not model-assisted.
- Recall is line-match based, without ranking or summarization.
- Topic inference is useful but narrow.
- Bilingual support is practical for common cases but still rule-based.

## Previous Versions

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

### v0.6.0

Possible focus:

- Optional model-assisted decision adapter behind `decide_memory_action()`.
- Deterministic validation and routing guardrails after model output.
- Improved recall output from raw lines to grouped entries.
- Expanded tests for ambiguous classification and mixed-language cases.

### v1.0.0

Only consider when:

- Decision behavior is stable across realistic usage.
- Recall output is meaningfully more helpful than plain text matching.
- Packaging and docs are polished enough for wider reuse.
- Major routing and memory semantics are unlikely to change.
