# Release Guide

This guide describes how to package MemRouter `v0.5.0` for distribution.

## Release Goal

A release package should be:

- Complete enough to use immediately as a skill.
- Small enough to avoid shipping development-only artifacts.
- Consistent with the current stable feature set.

## Release Profiles

Choose one of the two profiles below based on the audience.

### Minimal Package

Best for end-users who only want to install and use the skill.

```text
MemRouter-v0.5.0/
├── SKILL.md
├── README.md
├── README.zh-CN.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── entry-format.md
│   ├── memory-taxonomy.md
│   └── routing-policy.md
└── scripts/
    ├── memrouter_cli.py
    └── memrouter_core.py
```

### Developer Package

Best when downstream users need to run tests or continue development.

Include everything from the minimal package, plus:

```text
MemRouter-v0.5.0/
└── tests/
    ├── support.py
    ├── test_cli.py
    ├── test_decide.py
    ├── test_recall.py
    ├── test_remember.py
    └── test_routes.py
```

## File Checklist

### Required

- `SKILL.md`
- `README.md`
- `README.zh-CN.md`
- `agents/openai.yaml`
- `references/entry-format.md`
- `references/memory-taxonomy.md`
- `references/routing-policy.md`
- `scripts/memrouter_cli.py`
- `scripts/memrouter_core.py`

### Optional

- `tests/*.py`

### Excluded

- `.git/`
- `.gitignore`
- `.tmp-tests/`
- `__pycache__/`
- `*.pyc`
- `VERSION_RECORDS.md`

Keep `tests/` in the repository, but exclude it from the minimal release package unless you are shipping the developer package.

## Pre-Release Checklist

Before packaging, verify:

1. `README.md` and `README.zh-CN.md` match the current CLI behavior.
2. `SKILL.md` matches the actual workflow and command examples.
3. `agents/openai.yaml` matches the current skill positioning.
4. All tests pass: `python -m unittest discover -s tests -v`
5. The release folder contains no temp files or Python cache files.
6. The archive top-level folder is named `MemRouter-v0.5.0/`.

## Release Metadata

- **Title:** `MemRouter v0.5.0`
- **Summary highlights:**
  - Deterministic markdown memory routing by type, user, project, and date
  - Safe write semantics with exact dedupe and topic-aware upsert
  - Precise `created_at` timestamps without breaking exact dedupe
  - Scoped recall with project-session boundary protection
  - Unicode-safe route names
  - Heuristic decision layer via `decide`
  - Basic English and Chinese heuristic support

## Archive Shape

If distributing a zip, create the archive from a clean copy of the package contents. The top-level folder must be:

```text
MemRouter-v0.5.0/
```

Do not zip the raw repository root, as that may include Git metadata, caches, or ignored files.

## License

If the release is meant for public reuse, add a `LICENSE` file before publishing.
