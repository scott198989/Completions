# HAVOC Training Dataset — Completions Repo

**Last Audited:** 2026-05-09 | Audited by Claude (claude-opus-4-7)

**Naming convention:** Files prefixed with `D_` are complete ("Done"). Files without a prefix are either empty stubs or in-progress.

**Dataset size:** 26,630 rows across 11 completed files — **1,298,650 tokens** (cl100k_base, prompt+completion).

---

## Overview

This repo holds `.jsonl` training data files for the HAVOC Training Syllabus — a 55-topic curriculum spanning software engineering, math, controls, business, materials, and industrial process domains. Each completed topic file contains prompt/completion pairs generated at five difficulty tiers (easy → medium → hard → extremely_hard → brutal), 15 subtopics per topic.

Schema: `{"prompt", "completion", "difficulty", "task_type", "response_style"}`

---

## Repo Inventory

- **59 `.jsonl` files** on disk: 11 done (`D_` prefix) + 48 empty stubs
- **2 Python scripts**: `build_sft.py`, `label_jsonl.py`
- **README.md** (this file)

---

## Token Counts (2026-05-09 snapshot, cl100k_base, prompt+completion)

| File | Rows | Tokens |
|---|---:|---:|
| `D_Conversations.jsonl` | 12,376 | 380,626 |
| `D_material_science.jsonl` | 1,601 | 112,235 |
| `D_physics.jsonl` | 1,600 | 111,617 |
| `D_Trigonometry.jsonl` | 1,498 | 109,344 |
| `D_calculus.jsonl` | 1,535 | 108,680 |
| `D_Algebra.jsonl` | 1,314 | 92,438 |
| `D_elect_components.jsonl` | 1,497 | 90,593 |
| `D_Advanced_Eng_Math.jsonl` | 1,474 | 77,450 |
| `D_AC_Circuits.jsonl` | 1,348 | 72,538 |
| `D_electrodynamics.jsonl` | 1,318 | 72,472 |
| `D_Thermodynamics.jsonl` | 1,069 | 70,657 |
| **TOTAL** | **26,630** | **1,298,650** |

---

## Completion Status

### Done (11 files)

| File | Entries | Notes |
|---|---:|---|
| `D_Conversations.jsonl` | 12,376 | General conversation set; 3 duplicates removed 2026-04-21; 1 row rescued from mislabeled `compilation` key; 108 near-dupes flagged 2026-05-09 (mostly intentional greeting variants — see `_near_dupe_flags.md`) |
| `D_material_science.jsonl` | 1,601 | Promoted from WIP 2026-05-09; 4 near-dupes flagged for user review (3 same-prompt/different-completion pairs + 1 hyphen variant) |
| `D_physics.jsonl` | 1,600 | All tiers; 11 near-duplicates removed 2026-04-25; 1 JSON error fixed 2026-04-21 |
| `D_calculus.jsonl` | 1,535 | All tiers; ends in brutal optimization |
| `D_Trigonometry.jsonl` | 1,498 | All tiers; 1 dupe removed 2026-04-21; 2 cross-tier near-dupes removed 2026-04-25 |
| `D_elect_components.jsonl` | 1,497 | All tiers; 190 `extremely hard` → `extremely_hard` normalized; 198 `response_style` leaks reclassified 2026-04-21 |
| `D_Advanced_Eng_Math.jsonl` | 1,474 | All tiers; 1 duplicate removed; 2 mislabeled-key rows rescued 2026-04-21; metadata not yet backfilled. (Working tree contains a row-order-only diff against HEAD — content set is byte-identical) |
| `D_AC_Circuits.jsonl` | 1,348 | All tiers; 2 duplicates removed 2026-04-21; `{prompt, completion}` only (no difficulty/task_type/response_style) |
| `D_electrodynamics.jsonl` | 1,318 | All tiers; 168 `extremely hard` normalized; `analogy` task_type reclassified to `relation` |
| `D_Algebra.jsonl` | 1,314 | All tiers; 200 rows metadata backfilled 2026-04-21; 1 cross-tier near-dupe removed 2026-04-25 |
| `D_Thermodynamics.jsonl` | 1,069 | All tiers; 46 `extremely hard` normalized; 6 invalid `response_style` reclassified; 1 cross-tier near-dupe removed 2026-04-25 |

### Stubs (48 files — exist, empty)

| File | Syllabus Topic |
|---|---|
| `AutoCAD.jsonl` | AutoCAD |
| `Bash_Shell.jsonl` | Bash/Shell |
| `business_ethics.jsonl` | Business Ethics |
| `business_law.jsonl` | Business Law |
| `business_stats.jsonl` | Business Statistics |
| `c.jsonl` | C |
| `c#.jsonl` | C# |
| `c++.jsonl` | C++ |
| `CAD.jsonl` | CAD |
| `creo.jsonl` | Creo |
| `css.jsonl` | CSS |
| `financial_accounting.jsonl` | Financial Accounting |
| `gcode_mcode.jsonl` | G-Code/M-Code (CNC) |
| `general_system_theory.jsonl` | General System Theory |
| `git_commands.jsonl` | Git Commands |
| `html.jsonl` | HTML |
| `hydraulics_pneumatics.jsonl` | Hydraulics, Pneumatics, and Electric Motors |
| `industrial_dynamics.jsonl` | Industrial Dynamics |
| `intellectual_property.jsonl` | Intellectual Property |
| `transport_phenomena.jsonl` | Introductory Transport Phenomena |
| `java.jsonl` | Java |
| `javascript.jsonl` | JavaScript |
| `json.jsonl` | JSON |
| `macroeconomics.jsonl` | Macroeconomics |
| `manufacturing_processes.jsonl` | Manufacturing Processes |
| `markdown.jsonl` | Markdown |
| `matlab_octave.jsonl` | MATLAB/Octave Syntax |
| `microeconomics.jsonl` | Microeconomics |
| `php.jsonl` | PHP |
| `plc_ladder.jsonl` | PLC Ladder Logic |
| `principles_of_management.jsonl` | Principles of Management |
| `principles_of_marketing.jsonl` | Principles of Marketing |
| `process_control.jsonl` | Process Control Technology |
| `python.jsonl` | Python |
| `quality_in_business.jsonl` | Quality in Business |
| `react_jsx.jsonl` | React (JSX) |
| `robotics.jsonl` | Robotics |
| `siemens.jsonl` | Siemens (TIA Portal) |
| `siemens_scl.jsonl` | Siemens SCL |
| `six_sigma.jsonl` | Six Sigma (All Levels) |
| `solidworks.jsonl` | Solid Modeling / SolidWorks |
| `sql.jsonl` | SQL |
| `structured_text.jsonl` | Structured Text (IEC 61131) |
| `typescript.jsonl` | TypeScript |
| `workplace_software.jsonl` | Workplace Software and Skills |
| `wh_blown_film.jsonl` | W&H Blown Film Lines |
| `ampacet_masterbatch.jsonl` | Ampacet Masterbatch (Additives & Resin Systems) |
| `yaml.jsonl` | YAML |

---

## Full Syllabus — 55 Topics

Status: [DONE] Complete | [WIP] In progress | [STUB] File exists, empty

| # | Topic | File | Status |
|---|---|---|---|
| 1 | AutoCAD | `AutoCAD.jsonl` | [STUB] |
| 2 | Bash/Shell | `Bash_Shell.jsonl` | [STUB] |
| 3 | Business Ethics | `business_ethics.jsonl` | [STUB] |
| 4 | Business Law | `business_law.jsonl` | [STUB] |
| 5 | Business Statistics | `business_stats.jsonl` | [STUB] |
| 6 | C | `c.jsonl` | [STUB] |
| 7 | C# | `c#.jsonl` | [STUB] |
| 8 | C++ | `c++.jsonl` | [STUB] |
| 9 | CAD | `CAD.jsonl` | [STUB] |
| 10 | CSS | `css.jsonl` | [STUB] |
| 11 | Calculus | `D_calculus.jsonl` | [DONE] 1,535 entries |
| 12 | Creo | `creo.jsonl` | [STUB] |
| 13 | Electrical Components | `D_elect_components.jsonl` | [DONE] 1,497 entries |
| 14 | Electrodynamics | `D_electrodynamics.jsonl` | [DONE] 1,318 entries |
| 15 | Financial Accounting | `financial_accounting.jsonl` | [STUB] |
| 16 | G-Code/M-Code (CNC) | `gcode_mcode.jsonl` | [STUB] |
| 17 | General System Theory | `general_system_theory.jsonl` | [STUB] |
| 18 | Git Commands | `git_commands.jsonl` | [STUB] |
| 19 | HTML | `html.jsonl` | [STUB] |
| 20 | Hydraulics, Pneumatics, and Electric Motors | `hydraulics_pneumatics.jsonl` | [STUB] |
| 21 | Industrial Dynamics | `industrial_dynamics.jsonl` | [STUB] |
| 22 | Intellectual Property | `intellectual_property.jsonl` | [STUB] |
| 23 | Introductory Transport Phenomena | `transport_phenomena.jsonl` | [STUB] |
| 24 | JSON | `json.jsonl` | [STUB] |
| 25 | Java | `java.jsonl` | [STUB] |
| 26 | JavaScript | `javascript.jsonl` | [STUB] |
| 27 | MATLAB/Octave Syntax | `matlab_octave.jsonl` | [STUB] |
| 28 | Macroeconomics | `macroeconomics.jsonl` | [STUB] |
| 29 | Manufacturing Processes | `manufacturing_processes.jsonl` | [STUB] |
| 30 | Markdown | `markdown.jsonl` | [STUB] |
| 31 | Material Science | `D_material_science.jsonl` | [DONE] 1,601 entries |
| 32 | Microeconomics | `microeconomics.jsonl` | [STUB] |
| 33 | PHP | `php.jsonl` | [STUB] |
| 34 | PLC Ladder Logic | `plc_ladder.jsonl` | [STUB] |
| 35 | Physics | `D_physics.jsonl` | [DONE] 1,600 entries |
| 36 | Principles of Management | `principles_of_management.jsonl` | [STUB] |
| 37 | Principles of Marketing | `principles_of_marketing.jsonl` | [STUB] |
| 38 | Process Control Technology | `process_control.jsonl` | [STUB] |
| 39 | Python | `python.jsonl` | [STUB] |
| 40 | Quality in Business | `quality_in_business.jsonl` | [STUB] |
| 41 | React (JSX) | `react_jsx.jsonl` | [STUB] |
| 42 | Robotics | `robotics.jsonl` | [STUB] |
| 43 | SQL | `sql.jsonl` | [STUB] |
| 44 | Siemens (TIA Portal) | `siemens.jsonl` | [STUB] |
| 45 | Siemens SCL | `siemens_scl.jsonl` | [STUB] |
| 46 | Six Sigma (All Levels) | `six_sigma.jsonl` | [STUB] |
| 47 | Solid Modeling / SolidWorks | `solidworks.jsonl` | [STUB] |
| 48 | Structured Text (IEC 61131) | `structured_text.jsonl` | [STUB] |
| 49 | Thermodynamics | `D_Thermodynamics.jsonl` | [DONE] 1,069 entries |
| 50 | Trigonometry | `D_Trigonometry.jsonl` | [DONE] 1,498 entries |
| 51 | TypeScript | `typescript.jsonl` | [STUB] |
| 52 | Workplace Software and Skills | `workplace_software.jsonl` | [STUB] |
| 53 | YAML | `yaml.jsonl` | [STUB] |
| 54 | W&H Blown Film Lines | `wh_blown_film.jsonl` | [STUB] |
| 55 | Ampacet Masterbatch (Additives & Resin Systems) | `ampacet_masterbatch.jsonl` | [STUB] |

**Syllabus tally:** 7 done, 0 in progress, 48 stubs.

---

## Supplemental Files (4 — outside the 55-topic syllabus)

| File | Entries | Notes |
|---|---:|---|
| `D_Conversations.jsonl` | 12,376 | General Q&A; no schema metadata |
| `D_Advanced_Eng_Math.jsonl` | 1,474 | Graduate-level engineering math; no schema metadata yet |
| `D_Algebra.jsonl` | 1,314 | Linear/abstract algebra; metadata fully backfilled |
| `D_AC_Circuits.jsonl` | 1,348 | Companion to Electrodynamics; no schema metadata |

---

## Known Concerns (Flagged 2026-04-21)

- **`D_AC_Circuits.jsonl`** and **`D_Advanced_Eng_Math.jsonl`**: prompt/completion only — no difficulty/task_type/response_style. Separate decision from Scott whether to backfill (per-Algebra approach) or leave raw.
- **`-ScottsLaptop` variants**: left untouched per Scott's guidance. Several have their own defects (e.g., `Conversations-ScottsLaptop.jsonl` has 3 JSON errors, 3 duplicates, 1 mislabeled-key row) — these are external-tool snapshots, not authoritative.
- **`Algebra-ScottsLaptop.jsonl`**: 200 rows, no metadata. Distinct from `D_Algebra.jsonl` (authoritative file).

---

## Changelog

### 2026-05-09
- Full repo audit (cl100k_base): 26,630 rows / 1,298,650 tokens across 11 done files (up from 25,029 / 1,186,415)
- `material_science.jsonl` → `D_material_science.jsonl` (renamed; promoted WIP → Done at 1,601 rows / 112,235 tokens)
- 0 exact duplicates found (verified after NFKC + smart-quote normalization across all 11 files)
- 0 JSON parse errors, 0 schema issues across all 11 files
- 112 near-duplicates flagged in `_near_dupe_flags.md`:
  - `D_Conversations.jsonl` (108): mostly intentional casing/punctuation/emoji variants of casual greetings; 10 smart-quote prompt twins with paraphrased completions; 1 substantive (with vs without "completely")
  - `D_material_science.jsonl` (4): **needs user review** — 3 same-prompt/different-completion pairs (likely generation accidents), 1 hyphen variant ("solid-solution" vs "solid solution")
  - `D_Trigonometry.jsonl` (1): false positive — `sin(x)+cos(x)` vs `sin(x)·cos(x)` (different problems)
- `D_Advanced_Eng_Math.jsonl` working-tree change vs HEAD is row-order-only (set-equal; 1,472 inserts + 1,472 deletes are pure shuffle)

### 2026-05-05
- Renamed all 10 completed populated files with `D_` prefix to mark "Done" status (e.g., `physics.jsonl` → `D_physics.jsonl`)
- Repaired `D_.jsonl` (truncated rename artifact) → `D_physics.jsonl`
- `material_science.jsonl` populated to 727 rows (status: WIP, not yet validated)
- README restructured as a changelog; pipeline/aggregate files section dropped (none of those files exist on disk yet — defer until they do)

### 2026-04-25
- physics: completed all five tiers (884 → 1,611 raw rows); 11 near-duplicate easy/definition rows removed during audit (e.g., three "Define electric field" entries collapsed to one); 1,600 final
- Trigonometry: 2 cross-tier near-dupes removed (`Solve 2cos²x + 3cosx + 1 = 0` medium/hard pair; `Solve sin(x) = tan(x)` medium/extremely_hard pair) — kept the row whose tier matched the actual problem complexity
- Algebra: 1 cross-tier near-dupe removed (`algebraic multiplicity vs geometric multiplicity` was duplicated as both medium and extremely_hard; the extremely_hard label was inappropriate)
- Thermodynamics: 1 near-dupe removed (`What's a path function?` appeared on consecutive lines as both hard and easy)
- All 10 populated files validated: zero JSON parse errors, zero exact duplicates, zero near-duplicates after dedup pass

### 2026-04-21
- Thermodynamics: 46 `extremely hard` → `extremely_hard`; 6 response_style reassignments
- electrodynamics: 168 `extremely hard` → `extremely_hard`; `analogy` task_type → `relation`
- Algebra: 200 rows backfilled with difficulty/task_type/response_style; 1 `explanatory` → `structured`
- calculus: 4 response_style defects fixed (`short` ×3 → `direct`; `contrastive` → `structured`)
- AC_Circuits: 2 duplicates removed; 1 `placement` → `completion` key rename
- elect_components: 190 difficulty normalized, 2 `analogy_based` → `analogy-based`, 198 response_style leaks reclassified
- Trigonometry / Advanced_Eng_Math: 1 duplicate each removed
- physics: 1 JSON error fixed (stray trailing period on line 884)
- Conversations: 3 duplicates removed; 1 mislabeled `compilation` key corrected; file restored from HEAD after working-tree loss during audit
