# License map

License terms apply at directory scope when a skill contains its own license
file. Do not remove those files when copying or packaging a skill.

| Scope | License | Canonical text |
| --- | --- | --- |
| Repository content without a more specific directory license | MIT | [`LICENSE`](LICENSE) |
| `work-shaping`, `idea-validation`, `product-shaping`, `spec-bundle`, `continuity-ledger` | AGPL-3.0 | each directory's `LICENSE` |
| `spreadsheet`, `spreadsheet-xlsx-edit`, `spreadsheet-tabular-analysis` | Apache-2.0 | [`spreadsheet/LICENSE.txt`](spreadsheet/LICENSE.txt) |
| `transcribe`, `transcribe-basic`, `transcribe-diarize` | Apache-2.0 | [`transcribe/LICENSE.txt`](transcribe/LICENSE.txt) |
| `.system/skill-creator`, `.system/skill-installer` | Apache-2.0 | license file in each directory |
| `playwright`, `screenshot` | Apache-2.0 | license file in each directory |

The root MIT license does not override a more specific directory license.
Source histories are retained in Git so provenance can be audited beyond this
summary.
