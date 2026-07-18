---
name: spreadsheet-xlsx-edit
description: Create or edit `.xlsx` workbooks while preserving formulas, references, formatting, and layout. Use when workbook integrity matters more than raw data analysis.
---

# Spreadsheet XLSX Edit

## Metadata
- Trigger when: the task is to create or edit `.xlsx` files without breaking formulas, styles, sheet structure, or references.
- Do not use when: the job is mainly aggregation, joins, filtering, or analysis over CSV/TSV/tabular data.

## Skill Purpose

Make targeted `.xlsx` changes with `openpyxl` while preserving workbook integrity instead of flattening the file into disposable data.

## Instructions
1. Inspect the workbook first: target sheets, named ranges, formulas, styles, and the exact cells or structures that need to change. Use `openpyxl` and consult `/Users/nick/.codex/skills/spreadsheet/references/examples/openpyxl` only when you need a concrete pattern.
2. Apply the minimal workbook change that satisfies the task while preserving formulas, references, merged cells, widths, formatting, and sheet structure. Save the result under a stable descriptive path such as `output/spreadsheet/`.
3. Validate formulas, references, number/date formats, and visible layout. If layout matters and `soffice` plus `pdftoppm` are available, render for visual review; otherwise state that local eyeballing is still needed.

## Non-Negotiable Acceptance Criteria
- Existing formatting is preserved unless the user explicitly asked for redesign.
- Derived cells remain formulas when formulas are the correct source of truth.
- Structural workbook changes are intentional and explicit; no silent sheet damage or broken refs.
- If formula evaluation or visual rendering cannot be fully verified in this environment, that caveat is stated clearly.

## Output
- The final workbook path.
- Any render artifact path used for visual validation.
- A short note on formulas, style preservation, and remaining validation caveats.
- `Next skill options` (only if needed): `$spreadsheet-tabular-analysis` — use when the task turns into aggregation, joins, or reshaping rather than workbook-preserving edits.
