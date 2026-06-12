# Entry Format

Use this file when you need the exact on-disk markdown entry format for memory-router memories.

## Canonical Entry Shape

Preferred entry shape:

```text
- 2026-06-05 | created_at: 2026-06-05T14:32:10+08:00 | topic: output-style | source: chat
  The user prefers concise Chinese answers.
```

## Header Fields

The first line of each memory block uses this field order:

```text
- <date> | created_at: <iso-8601-datetime> | topic: <topic> | source: <source>
```

Field meanings:

- `date`: the logical memory date used for routing and day-level organization
- `created_at`: the exact entry timestamp with timezone information
- `topic`: a short stable label used for grouping and topic-aware upsert
- `source`: where the memory came from, such as `chat`, `import`, or `system`

## Body Rules

- continuation lines must be indented by two spaces
- multiline text stays inside one memory block
- nested bullets are allowed only as indented body lines

Example:

```text
- 2026-06-05 | created_at: 2026-06-05T14:32:10+08:00 | topic: notes | source: chat
  First line
  - nested detail
```

## Timestamp Rules

- `created_at` should be stored as an ISO 8601 timestamp
- include timezone information whenever possible
- if memory-router generates the value automatically, it uses the current local time with second precision
- if `created_at` is provided without an explicit route `date`, memory-router uses the timestamp date for routing
- if you explicitly pass both `date` and `created_at`, `date` controls routing while `created_at` preserves the exact entry timestamp

## Dedupe Rules

- exact dedupe compares `topic + source + body`
- exact dedupe ignores both `date` and `created_at`
- topic-aware upsert matches `topic + source`
- changing only the timestamp does not create a new exact-duplicate memory

## Metadata Normalization

- `topic` and `source` must not contain raw `|`
- repeated whitespace is collapsed
- empty metadata falls back to safe defaults such as `general` or `chat`

## Backward Compatibility

Older entries without `created_at` are still valid.

Legacy shape still accepted:

```text
- 2026-06-05 | topic: output-style | source: chat
  The user prefers concise Chinese answers.
```

memory-router can still parse these older entries for recall, exact dedupe, and topic-aware upsert.
