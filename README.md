# HAVOC Training Dataset — Completions Repo

**Last Audited:** 2026-04-25 | Audited by Claude (claude-opus-4-7)

**Dataset size:** 25,029 rows across 10 main files — **1,186,415 tokens** (cl100k_base, prompt+completion)

**Status:** `physics.jsonl` completed 2026-04-25 (1,600 rows, all five tiers). No populated files remain in progress.

---

## Overview

This repo holds `.jsonl` training data files for the HAVOC Training Syllabus — a 55-topic curriculum spanning software engineering, math, controls, business, materials, and industrial process domains. Each file contains prompt/completion pairs generated at five difficulty tiers (easy → medium → hard → extremely_hard → brutal), 15 subtopics per topic.

Schema: `{"prompt", "completion", "difficulty", "task_type", "response_style"}`

---

## Token Counts (2026-04-25, cl100k_base, prompt+completion)

| File | Rows | Tokens |
|---|---:|---:|
| Conversations.jsonl | 12,376 | 380,626 |
| physics.jsonl | 1,600 | 111,617 |
| Trigonometry.jsonl | 1,498 | 109,344 |
| calculus.jsonl | 1,535 | 108,680 |
| Algebra.jsonl | 1,314 | 92,438 |
| elect_components.jsonl | 1,497 | 90,593 |
| Advanced_Eng_Math.jsonl | 1,474 | 77,450 |
| AC_Circuits.jsonl | 1,348 | 72,538 |
| electrodynamics.jsonl | 1,318 | 72,472 |
| Thermodynamics.jsonl | 1,069 | 70,657 |
| **TOTAL** | **25,029** | **1,186,415** |

---

## Completion Status

### Completed

| File | Entries | Notes |
|---|---:|---|
| `Conversations.jsonl` | 12,376 | General conversation set; 3 duplicates removed 2026-04-21; 1 row rescued from mislabeled `compilation` key |
| `physics.jsonl` | 1,600 | All tiers; 11 near-duplicates removed 2026-04-25; 1 JSON error fixed 2026-04-21 |
| `calculus.jsonl` | 1,535 | All tiers; ends in brutal optimization |
| `Trigonometry.jsonl` | 1,498 | All tiers; 1 dupe removed 2026-04-21; 2 cross-tier near-dupes removed 2026-04-25 |
| `elect_components.jsonl` | 1,497 | All tiers; 190 `extremely hard` → `extremely_hard` normalized; 198 `response_style` leaks reclassified 2026-04-21 |
| `Advanced_Eng_Math.jsonl` | 1,474 | All tiers; 1 duplicate removed; 2 mislabeled-key rows rescued 2026-04-21; metadata not yet backfilled |
| `AC_Circuits.jsonl` | 1,348 | All tiers; 2 duplicates removed 2026-04-21; `{prompt, completion}` only (no difficulty/task_type/response_style) |
| `electrodynamics.jsonl` | 1,318 | All tiers; 168 `extremely hard` normalized; `analogy` task_type reclassified to `relation` |
| `Algebra.jsonl` | 1,314 | All tiers; 200 rows metadata backfilled 2026-04-21; 1 cross-tier near-dupe removed 2026-04-25 |
| `Thermodynamics.jsonl` | 1,069 | All tiers; 46 `extremely hard` normalized; 6 invalid `response_style` reclassified; 1 cross-tier near-dupe removed 2026-04-25 |

---

### Stub Files (0 entries — not yet started)

All 55 topic files exist. The following are still empty stubs:

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
| `material_science.jsonl` | Material Science |
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

| # | Topic | Status |
|---|---|---|
| 1 | AutoCAD | [STUB] |
| 2 | Bash/Shell | [STUB] |
| 3 | Business Ethics | [STUB] |
| 4 | Business Law | [STUB] |
| 5 | Business Statistics | [STUB] |
| 6 | C | [STUB] |
| 7 | C# | [STUB] |
| 8 | C++ | [STUB] |
| 9 | CAD | [STUB] |
| 10 | CSS | [STUB] |
| 11 | Calculus | [DONE] 1,535 entries |
| 12 | Creo | [STUB] |
| 13 | Electrical Components | [DONE] 1,497 entries |
| 14 | Electrodynamics | [DONE] 1,318 entries |
| 15 | Financial Accounting | [STUB] |
| 16 | G-Code/M-Code (CNC) | [STUB] |
| 17 | General System Theory | [STUB] |
| 18 | Git Commands | [STUB] |
| 19 | HTML | [STUB] |
| 20 | Hydraulics, Pneumatics, and Electric Motors | [STUB] |
| 21 | Industrial Dynamics | [STUB] |
| 22 | Intellectual Property | [STUB] |
| 23 | Introductory Transport Phenomena | [STUB] |
| 24 | JSON | [STUB] |
| 25 | Java | [STUB] |
| 26 | JavaScript | [STUB] |
| 27 | MATLAB/Octave Syntax | [STUB] |
| 28 | Macroeconomics | [STUB] |
| 29 | Manufacturing Processes | [STUB] |
| 30 | Markdown | [STUB] |
| 31 | Material Science | [STUB] |
| 32 | Microeconomics | [STUB] |
| 33 | PHP | [STUB] |
| 34 | PLC Ladder Logic | [STUB] |
| 35 | Physics | [DONE] 1,600 entries |
| 36 | Principles of Management | [STUB] |
| 37 | Principles of Marketing | [STUB] |
| 38 | Process Control Technology | [STUB] |
| 39 | Python | [STUB] |
| 40 | Quality in Business | [STUB] |
| 41 | React (JSX) | [STUB] |
| 42 | Robotics | [STUB] |
| 43 | SQL | [STUB] |
| 44 | Siemens (TIA Portal) | [STUB] |
| 45 | Siemens SCL | [STUB] |
| 46 | Six Sigma (All Levels) | [STUB] |
| 47 | Solid Modeling / SolidWorks | [STUB] |
| 48 | Structured Text (IEC 61131) | [STUB] |
| 49 | Thermodynamics | [DONE] 1,070 entries |
| 50 | Trigonometry | [DONE] 1,500 entries |
| 51 | TypeScript | [STUB] |
| 52 | Workplace Software and Skills | [STUB] |
| 53 | YAML | [STUB] |
| 54 | W&H Blown Film Lines | [STUB] |
| 55 | Ampacet Masterbatch (Additives & Resin Systems) | [STUB] |

---

## Bonus / Supplemental Files

| File | Entries | Notes |
|---|---:|---|
| `Conversations.jsonl` | 12,376 | General Q&A; no schema metadata |
| `Advanced_Eng_Math.jsonl` | 1,474 | Graduate-level engineering math; no schema metadata yet |
| `Algebra.jsonl` | 1,314 | Linear/abstract algebra; metadata fully backfilled |
| `AC_Circuits.jsonl` | 1,348 | Companion to Electrodynamics; no schema metadata |

---

## Pipeline / Aggregate Files

| File | Entries | Purpose |
|---|---:|---|
| `combined_labeled.jsonl` | 2,925 | Labeled combined dataset |
| `train.jsonl` | 2,542 | Training split |
| `val.jsonl` | 283 | Validation split |
| `Conversations_filtered.jsonl` | 5,506 | Candidate filtered conversations — ≥80 chars, non-restatement, non-filler (for review) |
| `Advanced_Eng_Math_KEEP.jsonl` | 1,281 | Rows passing regeneration filter (for review) |
| `Advanced_Eng_Math_REGEN.jsonl` | 193 | Rows flagged for regeneration (for review) |

---

## Known Concerns (Flagged 2026-04-21)

- **`AC_Circuits.jsonl`** and **`Advanced_Eng_Math.jsonl`**: prompt/completion only — no difficulty/task_type/response_style. Separate decision from Scott whether to backfill (per-Algebra approach) or leave raw.
- **`-ScottsLaptop` variants**: left untouched per Scott's guidance. Several have their own defects (e.g., `Conversations-ScottsLaptop.jsonl` has 3 JSON errors, 3 duplicates, 1 mislabeled-key row) — these are external-tool snapshots, not authoritative.
- **`Algebra-ScottsLaptop.jsonl`**: 200 rows, no metadata. Distinct from `Algebra.jsonl` (authoritative file).

## Recent Fixes (2026-04-25)

- physics: completed all five tiers (884 → 1,611 raw rows); 11 near-duplicate easy/definition rows removed during audit (e.g. three "Define electric field" entries collapsed to one); 1,600 final
- Trigonometry: 2 cross-tier near-dupes removed (`Solve 2cos²x + 3cosx + 1 = 0` medium/hard pair; `Solve sin(x) = tan(x)` medium/extremely_hard pair) — kept the row whose tier matched the actual problem complexity
- Algebra: 1 cross-tier near-dupe removed (`algebraic multiplicity vs geometric multiplicity` was duplicated as both medium and extremely_hard; the extremely_hard label was inappropriate)
- Thermodynamics: 1 near-dupe removed (`What's a path function?` appeared on consecutive lines as both hard and easy)
- All 10 populated files validated: zero JSON parse errors, zero exact duplicates, zero near-duplicates after dedup pass

## Recent Fixes (2026-04-21)

- Thermodynamics: 46 `extremely hard` → `extremely_hard`; 6 response_style reassignments
- electrodynamics: 168 `extremely hard` → `extremely_hard`; `analogy` task_type → `relation`
- Algebra: 200 rows backfilled with difficulty/task_type/response_style; 1 `explanatory` → `structured`
- calculus: 4 response_style defects fixed (`short` ×3 → `direct`; `contrastive` → `structured`)
- AC_Circuits: 2 duplicates removed; 1 `placement` → `completion` key rename
- elect_components: 190 difficulty normalized, 2 `analogy_based` → `analogy-based`, 198 response_style leaks reclassified
- Trigonometry / Advanced_Eng_Math: 1 duplicate each removed
- physics: 1 JSON error fixed (stray trailing period on line 884)
- Conversations: 3 duplicates removed; 1 mislabeled `compilation` key corrected; file restored from HEAD after working-tree loss during audit
