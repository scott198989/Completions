# HAVOC Training Dataset — Completions Repo

**Last Audited:** 2026-04-20 | Audited by Claude (claude-sonnet-4-6)

---

## Overview

This repo holds `.jsonl` training data files for the HAVOC Training Syllabus — a 55-topic curriculum spanning software engineering, math, controls, business, materials, and industrial process domains. Each file contains prompt/completion pairs generated at five difficulty tiers (Beginner to Brutal), 15 subtopics per topic.

---

## Completion Status

### Completed

| File | Entries | Quality Check | Notes |
|---|---|---|---|
| `Conversations.jsonl` | 12,379 | — | General conversation training set |
| `calculus.jsonl` | 1,535 | — | All tiers complete — ends in brutal optimization |
| `Trigonometry.jsonl` | 1,501 | — | All tiers complete |
| `Advanced_Eng_Math.jsonl` | 1,475 | — | All tiers complete |
| `AC_Circuits.jsonl` | 1,350 | — | All tiers complete |
| `Algebra.jsonl` | 1,315 | — | All tiers complete — ends in abstract/graduate algebra |
| `Thermodynamics.jsonl` | **1,070** | 0 broken JSON, 0 dupes, 0 missing fields | All 15 subtopics covered, Beginner through Brutal |

**Thermodynamics audit detail:**
- 1,070 valid entries (1,071 non-empty lines, 0 malformed)
- 1,070 unique prompts — no duplicates
- All entries have both `prompt` and `completion` fields populated
- Completion lengths: min 6 chars, max 882 chars, avg 268 chars
- Coverage confirmed: starts at beginner basics ("Define heat in one sentence") through brutal-tier entropy theory ("Why does entropy bound cryptographic security?")
- All 15 subtopics present:
  1. Systems, properties, and state variables
  2. Energy, heat, and work
  3. First law of thermodynamics for closed systems
  4. Properties of pure substances and phase change
  5. Control-volume energy balances
  6. Entropy and the second law basics
  7. Ideal gas mixtures and psychrometric ideas
  8. Power cycles and refrigeration cycles
  9. Exergy and irreversibility intuition
  10. Real fluids, property tables, and compressibility effects
  11. Combustion and reacting systems basics
  12. Availability analysis and second-law design tradeoffs
  13. Coupling thermo with fluid flow and heat transfer
  14. Cycle optimization under realistic engineering constraints
  15. Thinking clearly about entropy when the equations get nasty

---

### Stub Files (0 entries — not yet started)

All 55 topic files now exist. Files with no entries yet:

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
| `elect_components.jsonl` | Electrical Components |
| `electrodynamics.jsonl` | Electrodynamics |
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
| `physics.jsonl` | Physics |
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

Status: [DONE] Complete | [STUB] File exists, empty | [----] Not started

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
| 13 | Electrical Components | [STUB] |
| 14 | Electrodynamics | [STUB] |
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
| 35 | Physics | [STUB] |
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
| 49 | Thermodynamics | [DONE] 1,070 entries — all 15 subtopics, all tiers |
| 50 | Trigonometry | [DONE] 1,501 entries |
| 51 | TypeScript | [STUB] |
| 52 | Workplace Software and Skills | [STUB] |
| 53 | YAML | [STUB] |
| 54 | W&H Blown Film Lines | [STUB] |
| 55 | Ampacet Masterbatch (Additives & Resin Systems) | [STUB] |

---

## Bonus / Supplemental Files

These exist outside the 55-topic syllabus:

| File | Entries | Notes |
|---|---|---|
| `Conversations.jsonl` | 12,379 | General knowledge / conversational Q&A |
| `Advanced_Eng_Math.jsonl` | 1,475 | Graduate-level engineering mathematics |
| `Algebra.jsonl` | 1,315 | Linear/abstract algebra |
| `AC_Circuits.jsonl` | 1,350 | AC circuits (maps to Electrodynamics topic) |

---

## Aggregate / Pipeline Files

| File | Entries | Purpose |
|---|---|---|
| `combined_labeled.jsonl` | 2,925 | Labeled combined dataset |
| `train.jsonl` | 2,542 | Training split |
| `val.jsonl` | 283 | Validation split |
| `build_sft.py` | — | SFT dataset build script |
| `label_jsonl.py` | — | Labeling utility |

---

## Progress Summary

- **Topics complete:** 7 (Calculus, Trigonometry, Thermodynamics, AC Circuits, Algebra, Advanced Eng Math, Conversations)
- **Stub files ready to fill:** 11
- **Topics not yet started:** 37
- **Total syllabus entries so far:** ~21,155
