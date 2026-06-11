# Release Guide

This document describes the recommended release package for MemRouter `v0.5.0`.

## Recommended Release Goal

Package MemRouter as a reusable skill folder that is:

- complete enough to be usable immediately
- small enough to avoid shipping unnecessary development artifacts
- consistent with the current stable feature set

## Recommended Release Profiles

Use one of these two release shapes depending on the audience.

### 1. Minimal End-User Package

Recommended when the release is mainly for skill installation and direct use.

Include:

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

### 2. Developer Package

Recommended when you want downstream users to validate behavior, run tests, or continue development.

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

## Exact Recommended Files

If you want a file-by-file checklist, these are the current recommended release files:

- `SKILL.md`
- `README.md`
- `README.zh-CN.md`
- `agents/openai.yaml`
- `references/entry-format.md`
- `references/memory-taxonomy.md`
- `references/routing-policy.md`
- `scripts/memrouter_cli.py`
- `scripts/memrouter_core.py`

Optional:

- `tests/support.py`
- `tests/test_cli.py`
- `tests/test_decide.py`
- `tests/test_recall.py`
- `tests/test_remember.py`
- `tests/test_routes.py`

## Recommended Files To Exclude

Do not include these in the release artifact:

- `.git/`
- `.gitignore`
- `.tmp-tests/`
- `__pycache__/`
- `*.pyc`
- `VERSION_RECORDS.md`

Exclude `tests/` when you want the smallest end-user package.

## Why Tests Are Optional In Release

Keep `tests/` in the development repository, but exclude it from a minimal end-user release unless you explicitly want a developer-facing distribution.

Recommended default:

- repository: include `tests/`
- release zip: exclude `tests/`

## Pre-Release Checklist

Before packaging a release, verify:

1. `README.md` and `README.zh-CN.md` match the current CLI behavior.
2. `SKILL.md` still matches the actual workflow and command examples.
3. `agents/openai.yaml` still matches the current skill positioning.
4. `python -m unittest discover -s tests -v` passes in the development repo.
5. The release folder contains no temp files or Python cache files.
6. The archive top-level folder is named `MemRouter-v0.5.0/`.

## Suggested Release Title

Recommended title:

```text
MemRouter v0.5.0
```

## Suggested Release Summary

Suggested short summary:

- deterministic markdown memory routing by type, user, project, and date
- safe write semantics with exact dedupe and topic-aware upsert
- precise `created_at` timestamps in memory entries without breaking exact dedupe
- scoped recall with project-session boundary protection
- Unicode-safe route names
- heuristic decision layer via `decide`
- basic English and Chinese heuristic support for trivial chat, preferences, tasks, and topic inference

## Recommended Archive Shape

If you are distributing a zip, the top-level folder should be:

```text
MemRouter-v0.5.0/
```

Inside that folder, keep the same structure shown above.

## Practical Packaging Tip

Create the release from a clean copy of the repository contents rather than zipping the whole repo root blindly. That avoids accidentally shipping Git metadata, caches, local notes, or ignored files.

## One Extra Recommendation

If this release is meant for public reuse outside your own environment, decide whether you want to add a `LICENSE` file before publishing. That is not a code issue, but it affects whether other people can safely reuse the project.
