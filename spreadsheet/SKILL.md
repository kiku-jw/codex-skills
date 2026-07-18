---
name: spreadsheet
description: Create, edit, analyze, or format spreadsheets (`.xlsx`, `.csv`, `.tsv`) with `openpyxl` and `pandas`, especially when formulas, references, and formatting must survive the change. Use when spreadsheet integrity matters more than ad hoc CSV hacking.
---

# Spreadsheet Skill

## Metadata
- Trigger when: the task involves real spreadsheet creation, editing, analysis, formatting, or visual validation.
- Do not use when: a trivial one-line CSV inspection is enough and workbook integrity does not matter.

## Skill Purpose

Stay as the stable entrypoint for spreadsheet work, then route into the narrowest correct lane: workbook-preserving `.xlsx` editing or tabular data analysis.

## Instructions
1. Classify the spreadsheet job first. If the task is `.xlsx` creation/editing with formulas or formatting preservation, prefer `$spreadsheet-xlsx-edit`. If the task is CSV/TSV or spreadsheet-backed analysis, aggregation, or reshaping, prefer `$spreadsheet-tabular-analysis`. Read the runnable examples under `/Users/nick/.codex/skills/spreadsheet/references/examples/openpyxl` only when you need a concrete pattern.
2. If a child lane is unavailable in the current run, continue here with the same split: use `openpyxl` for `.xlsx` structure-preserving work and `pandas` for tabular analysis workflows. Keep filenames stable and outputs under a sensible path such as `output/spreadsheet/`.
3. Validate the result. Check formulas, references, number/date formats, source citations when relevant, and render for visual review when layout matters and `soffice` plus `pdftoppm` are available.

## Non-Negotiable Acceptance Criteria
- Existing workbook formatting is preserved unless the user asked for redesign.
- Derived values stay as formulas when formulas are the right source of truth.
- Formatting and citation rules are explicit when the spreadsheet is financial or source-sensitive.
- If rendering dependencies are missing, the skill says so instead of pretending the layout was verified.

## Output
- The final spreadsheet path or paths.
- Any render artifact path used for visual validation.
- A short note on formula handling, dependency installs, or validation caveats.
- `Next skill options` (only if needed): `$spreadsheet-xlsx-edit` — create or edit `.xlsx` files while preserving formulas and formatting; `$spreadsheet-tabular-analysis` — analyze and reshape spreadsheet/CSV/TSV data with stable outputs.
