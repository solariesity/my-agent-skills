---
name: python-style
description: Behavior-preserving Python style cleanup for research and training code. Use when reviewing or standardizing Python naming, module or file names, Chinese-first comments or docstrings, and stable parseable training or debug output without breaking external contracts.
---

# Python Style

Use this skill to clean or review Python code that has mixed naming, noisy comments, or inconsistent runtime output.

Prefer this style in research and training codebases:
- keep identifiers in English for tooling and consistency
- allow comments and docstrings to be mostly Chinese when the project allows it
- keep training logs stable and easy to parse

## Default Assumptions

- Prefer behavior-preserving cleanup unless the user explicitly asks to change logic.
- Keep edits small and local.
- Do not mix naming cleanup with algorithm changes in the same patch unless required.
- Treat externally consumed names and output fields as contracts. Rename them only when every dependent reference can be updated and verified in the same patch; otherwise preserve the old name or keep compatibility.

## Naming Rules

- Use `snake_case` for functions, variables, and module-level helpers.
- Use `CapWords` for classes.
- Use `UPPER_CASE` for constants.
- Use English for code identifiers.
- Prefer semantic names over vague names like `tmp`, `ret`, `data2`, `score1`.
- Use singular names for a single tensor or sample, and plural names for batches or collections.
- Use `num_*` for counts, `*_idx` for a single index, and `*_indices` for index tensors or index lists.
- Use `*_path` and `*_dir` for filesystem paths.
- Prefer `device` and `dtype` for torch device and dtype values.

For booleans, prefer prefixes such as:
- `is_`
- `has_`
- `should_`
- `use_`
- `enable_`

For tensors and losses, prefer names that carry meaning:
- `_mask` for binary or soft masks
- `_score` for generic scores
- `_conf` for objectness or confidence-like values
- `_loss` for loss terms
- `_logits` for pre-activation class outputs

When working on detection code, keep these meanings separate:
- `obj_conf`: probability or confidence that a box contains an object
- `cls_score` or `max_cls_score`: class-related score for a category
- `combined_score`: combined detection score such as `obj_conf * max_cls_score`

Do not mix `score`, `conf`, and `prob` for the same quantity unless the code truly changes meaning.

When renaming symbols that may be referenced elsewhere:
- Search call sites, imports, config keys, CLI flags, env vars, checkpoint keys, serialized dict keys, and log parsers before renaming.
- If every dependent reference is local and can be updated together, rename consistently in the same patch.
- If some dependency is external or cannot be verified, keep the old name or add a compatibility alias.
- Public functions can be renamed when all known call sites and exports are updated atomically.

## File and Module Naming Rules

- Use English `snake_case` for Python module filenames.
- Prefer descriptive filenames over vague names like `temp.py`, `misc.py`, `util2.py`, or `new_test.py`.
- Use singular filenames for a module with one primary concept, and broader category names only when the file truly groups related utilities.
- For executable scripts, prefer action-oriented prefixes such as `train_`, `eval_`, `plot_`, `dump_`, `export_`, or `convert_` when they match the file's role.
- Keep package entry points and import paths stable unless every dependent reference can be updated together.

When renaming files or modules:
- Search imports, shell scripts, config files, docs, tests, notebook cells, and path-construction code before renaming.
- If every dependent reference is local and can be updated and verified together, rename consistently in the same patch.
- If some dependency is external or cannot be verified, keep the old filename or add a compatibility wrapper module or script.

## Comment Rules

- Prefer Chinese comments and docstrings by default.
- Keep identifiers, function names, and parameter names in English.
- If the user or project explicitly asks for English or bilingual comments, follow that request instead.
- Comments should explain one of these:
  - why this step exists
  - what a tensor or score means
  - what assumption or pitfall matters here
  - what coordinate system, shape, or unit is being used

Avoid comments that only restate the code.

Good:
- `# 这里扩张 mask 的外接框，只让候选框在目标车辆附近比较`
- `# obj_conf 表示“这个框里有物体”，不是“这个框是 car”`

Avoid:
- `# 给变量赋值`
- `# x 加 1`

For public functions, add a short docstring in Chinese when it helps future readers. Keep it compact. Prefer this structure when needed:
- one-line summary
- `参数:` for important inputs
- `返回:` for outputs with non-obvious meaning

## Output Rules

Use stable, machine-friendly text output for anything that may be parsed later.

- If the project already uses JSON logs, a logging framework, or another established structured format, preserve it and keep the schema stable instead of converting everything to `key=value`.
- Keep per-step summaries on one line.
- Separate stable summary fields with single spaces.
- Use fixed field names and fixed ordering.
- Prefer `key=value` style output when the project does not already use another established structured format.
- Keep numeric formatting stable within the same output stream.
- Avoid switching between decimal and scientific notation unless values truly require it.
- Use `na` for missing or unavailable values.
- Use lowercase `true` or `false` for booleans when printed.
- Put progress keys first when practical, such as `epoch`, `iter`, or `step`, then optimization fields like `lr`, then losses or metrics, then timing fields.
- If a field name, field order, or format changes, update every dependent parser in the same patch.

Recommended layers:
- per-step summary: concise, stable, parseable
- periodic detail block: human-readable explanation
- debug output: opt-in only, with a clear prefix

Example stable summary:
- `epoch=3 step=120 lr=0.000100 total_loss=1.234567 obj_conf=0.812300 time_ms=42`

For debug lines, use prefixes like:
- `[debug]`
- `[scene_car_feature_align]`
- `[mask]`

Do not mix temporary debug prints into stable training summaries.

## Editing Workflow

When applying this skill:

1. Identify whether the task is naming cleanup, comment cleanup, output cleanup, or a small combination.
2. Classify each touched name or output field as internal-only or externally consumed.
3. Preserve behavior unless the user asked for logic changes.
4. Rename one concept at a time, and use `rg` or equivalent to find every reference before changing it.
5. If a symbol is externally consumed, update all dependent references in the same patch or keep compatibility.
6. Do not do broad style sweeps across unrelated files.
7. After changing output strings, search for dependent parsers or plotting scripts and run a minimal verification path when available.
8. If verification cannot be run, state the gap explicitly in the final handoff.

## Quick Review Checklist

- Does each important variable name match its true meaning?
- Did any renamed symbol cross a config, CLI, checkpoint, serialization, or log-parser boundary?
- If so, were all dependent references updated together or compatibility preserved?
- Are `obj_conf`, class score, and combined score clearly separated?
- Are singular or plural names, `num_*`, `*_idx`, `*_indices`, `*_path`, and `*_dir` used consistently where applicable?
- Are comments explaining meaning instead of rephrasing syntax?
- Are public functions documented just enough to be understood later?
- Are logs stable enough for downstream scripts to parse, including key order, missing values, and numeric formatting?
- Are debug prints clearly marked and easy to disable?
