# Version Records

This file tracks monorepo versions, what each version introduced, and the near-term roadmap.

## Current Version

### v1.0.1

Current stable baseline for repo-level versioning conventions.

**Added / Changed:**

- Added a durable rule that the repository must keep both `VERSION` and `VERSION_RECORDS.md`.
- Added a durable rule that every skill must keep both `VERSION` and `VERSION_RECORDS.md`.
- Added a durable rule that version bumps must update `VERSION`, `VERSION_RECORDS.md`, and related README version text together.
- Synced the root README files with the new repo version and version-records convention.

## Previous Versions

### v1.0.0

First monorepo-wide stable release after consolidating the skills and bilingual documentation.

## Roadmap

### v1.0.2

Possible focus:

- Backfill `VERSION_RECORDS.md` for skills that still only have `VERSION`.
- Standardize a shared `VERSION_RECORDS.md` template across all skills.
- Link repo-level and skill-level version records more explicitly from READMEs where useful.
