---
name: spreadsheet-tabular-analysis
description: Analyze and reshape spreadsheet, CSV, or TSV data with `pandas` and stable output files. Use when the job is aggregation, filtering, joins, metrics, or tabular transformations rather than workbook-style editing.
---

# Spreadsheet Tabular Analysis

## Metadata
- Trigger when: the task is to analyze, aggregate, filter, join, reshape, or summarize spreadsheet-like data.
- Do not use when: the job is primarily about preserving workbook formatting, formulas, or sheet structure.

## Skill Purpose

Treat the task as tabular analysis first: produce correct metrics and stable outputs with `pandas` before worrying about polished workbook-level formatting.

## Instructions
1. Inspect the input tables first: file type, schema, key columns, joins, date/number handling, and the exact output shape the user needs. Use `pandas` as the default analysis surface.
2. Run the analysis and write stable outputs under a path such as `output/spreadsheet/`, choosing `.csv` or `.xlsx` based on what the user needs. Keep transformations explicit so row counts, joins, and metrics can be checked.
3. Validate totals, row counts, joins, deduping, date/number formatting, and any source or citation columns the task requires. If the result now needs workbook-style formatting or preservation, hand off to `$spreadsheet-xlsx-edit`.

## Non-Negotiable Acceptance Criteria
- The output tables are reproducible from explicit transformations, not ad hoc spreadsheet clicking.
- Row counts, joins, and aggregates are checked before delivery.
- The skill does not pretend to preserve rich workbook formatting it never managed.
- Source or citation columns are included when the task depends on externally sourced data.

## Output
- The result file path or paths.
- A short summary of the transformation or analysis performed.
- Any validation caveat involving joins, missing values, or formatting limits.
- `Next skill options` (only if needed): `$spreadsheet-xlsx-edit` — use when the analyzed output now needs workbook-preserving formatting or formula-aware editing.
