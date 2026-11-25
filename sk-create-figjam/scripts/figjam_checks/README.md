---
title: "FigJam Checks: Per-Kind Rules and Board Geometry"
description: "The rule, layout, design and geometry modules flow_check.py and compose_board.py hold a FigJam model to."
trigger_phrases:
  - figjam checks
  - figjam rule modules
  - board geometry checks
version: 1.0.0.0
---

# FigJam Checks: Per-Kind Rules and Board Geometry

---

## 1. OVERVIEW

`sk-create-figjam/scripts/figjam_checks/` is the package of rules a FigJam model is held to before any board write. Each diagram kind has its own module, because neither the composer nor Figma's generated fallback draws everything Mermaid can say, and a model must never promise a reader what the board leaves out.

The package also measures shape on the same parse, reads the board design and checks the geometry of a composed board from a `compose-trace.mjs` run. `../flow_check.py` and `../compose_board.py` are its only callers.

---

## 2. PACKAGE TOPOLOGY

```text
flow_check.py, compose_board.py
    ├── flowchart.py, sequence.py, state.py, er.py, gantt.py   (one rule module per kind)
    │       └── common.py                                      (shared rules and the palette)
    ├── layout.py                                              (shape measures)
    ├── design.py                                              (design file and floors)
    ├── board_geometry.py                                      (composed-board checks)
    └── fixtures.py, board_fixtures.py                         (self-test models)
```

`common.py` is the shared base. The kind modules import it, and no kind module imports another kind's module.

---

## 3. KEY FILES

| File | Responsibility |
|---|---|
| `__init__.py` | Marks the package and names its purpose |
| `common.py` | Rules every kind holds to, such as no emoji, no HTML, no literal `\n` and no reserved or underscored id, plus the FigJam palette and contrast helpers |
| `flowchart.py` | User flow, process and architecture rules: shape, exits, connectors, colour, lanes and edges, through `check_flow` and `check_architecture` |
| `sequence.py` | The narrow sequence subset the board draws, refusing notes, activations, fragments, boxes, numbering and aliases, through `check_sequence` |
| `state.py` | State diagram rules, refusing notes and style lines that would grow phantom states, through `check_state` |
| `er.py` | Its own entity-relationship parse, because the extractor drops the fields of an aliased entity, through `check_er` |
| `gantt.py` | Its own gantt parse, because the extractor refuses gantt, refusing colour and axis settings the board ignores, through `check_gantt` |
| `layout.py` | Ranks, chain length and an estimated crossing count, through `measure` |
| `design.py` | Reads `../../assets/figjam-design.md` over the composer's built-in design and holds it to the contrast, accent and type-size floors, through `resolve` and `theme` |
| `board_geometry.py` | Reads a trace and reports lines through boxes, shared magnets, crossing edges, labels on titles and other drawn defects |
| `fixtures.py` | Good models that must pass and planted models that each break one rule and name the message its failure prints |
| `board_fixtures.py` | Composer models that once drew a geometry defect, kept whole so a layout change that brings one back fails |

---

## 4. BOUNDARIES

- The modules parse text only and never render or run anything in a label
- A new rule needs a planted model in `fixtures.py` with its expected message, or the self-test cannot prove the rule fires
- A geometry defect found on a live board is kept as a model in `board_fixtures.py`

---

## 5. VALIDATION

Run from the `sk-create-figjam/` folder:

```bash
python3 scripts/flow_check.py --self-test
python3 scripts/compose_board.py --self-test
```

Expected result: each run ends with `N of N self-test checks passed` and exits 0. The first proves every rule module against its fixtures, and the second proves the design reader and the geometry checks against the composed boards.

---

## 6. RELATED

- [`../README.md`](../README.md) describes the entrypoints that call this package
- [`../../references/types/`](../../references/types/) explains the rules for each diagram kind
- [`../../references/style-guide.md`](../../references/style-guide.md) records the palette `common.py` holds
