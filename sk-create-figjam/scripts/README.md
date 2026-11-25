---
title: "FigJam Scripts: Model Check and Board Composer"
description: "Python and Node entrypoints that check a FigJam diagram model and compose its board code for use_figma."
trigger_phrases:
  - figjam scripts
  - flow check
  - compose board
version: 1.0.0.0
---

# FigJam Scripts: Model Check and Board Composer

---

## 1. OVERVIEW

`sk-create-figjam/scripts/` checks a Mermaid diagram model before any board write and turns a model that passed into the code one `use_figma` call runs. A board is slow to fix once it exists, so every rule runs on the model first and a model that breaks one is never written.

`flow_check.py` is the pre-write gate. `compose_board.py` fills `../assets/compose-board.js` from the same parse, so the board holds exactly what passed the check. `compose-trace.mjs` runs that filled code against a recording stand-in for Figma, so the self-tests can measure the board's geometry without a live write.

---

## 2. ARCHITECTURE

```text
model.md (Mermaid blocks)
    └── flow_check.py ──▶ vendored/mermaid_extract.py   (flowchart, state)
            │          └─▶ figjam_checks/                (per-kind rules, layout measures)
            ▼ pass
        compose_board.py ──▶ ../assets/compose-board.js  (MODEL and THEME filled)
            │             └─▶ ../assets/figjam-design.md (design tokens)
            ▼
        filled code ──▶ use_figma
            └── compose-trace.mjs ──▶ figjam_checks/board_geometry.py   (self-test only)
```

Dependencies point one way. The two entrypoints import `figjam_checks/` and `vendored/`, and neither package imports an entrypoint.

---

## 3. DIRECTORY TREE

```text
scripts/
+-- README.md
+-- flow_check.py
+-- compose_board.py
+-- compose-trace.mjs
+-- figjam_checks/
|   +-- README.md
|   `-- (rule, layout, design and geometry modules)
`-- vendored/
    +-- README.md
    `-- mermaid_extract.py
```

---

## 4. KEY FILES

| Path | Responsibility |
|---|---|
| `scripts/flow_check.py` | Checks every Mermaid block in a model against its kind's rules and prints the `Label:`, `Glance:`, `Row:` and `Sides:` lines the write gate reads |
| `scripts/compose_board.py` | Refuses a model that fails the check, then fills the composer's MODEL and THEME and writes the code for one `use_figma` call |
| `scripts/compose-trace.mjs` | Runs filled composer code against a recording stand-in for the Figma Plugin API and prints every box and connector end as JSON |
| `scripts/figjam_checks/` | Per-kind rule modules, layout measures, the shared palette, the design reader, the board geometry checks and the planted fixtures |
| `scripts/vendored/` | The Mermaid extractor, a byte copy kept in step through `vendor.json` at the repository root |

---

## 5. ENTRYPOINTS

| Command | Purpose |
|---|---|
| `python3 scripts/flow_check.py <model.md>` | Checks every diagram. Exit 0 every diagram passes, 1 a rule fails, 2 unreadable |
| `python3 scripts/flow_check.py <model.md> --notes <id,id>` | The same check, plus a `Sides:` line for each noted node id |
| `python3 scripts/compose_board.py <model.md> [--diagram N] [--out PATH]` | Writes the filled code. Exit 0 written, 1 the model fails the check, 2 unreadable or no such diagram |
| `python3 scripts/compose_board.py <model.md> --model` | Prints the filled MODEL as JSON instead of the code |
| `python3 scripts/compose_board.py --template [graph\|sequence,gantt]` | Prints the compact code with its MODEL and THEME placeholders |
| `python3 scripts/compose_board.py --design-check` | Prints the resolved design and its THEME. Exit 1 when the design file raises a warning |
| `node scripts/compose-trace.mjs <filled-code.js>` | Prints the trace JSON. Exit 0 the trace printed, 1 the file could not be read |

`flow_check.py` composes the board in memory when `node` is on the PATH, to report a label that would wrap one word alone onto its last line. Without `node` it prints one `Label: skipped` line instead.

---

## 6. VALIDATION

Run from the `sk-create-figjam/` folder:

```bash
python3 scripts/flow_check.py --self-test
python3 scripts/compose_board.py --self-test
python3 scripts/compose_board.py --design-check
```

Expected result: `flow_check.py` ends with `N of N self-test checks passed` and exits 0, which proves each rule fails on its planted model and the templates and examples pass. `compose_board.py --self-test` ends the same way and proves every shipped model composes, fits one `use_figma` call and keeps its geometry. The two self-tests take about 20 and 40 seconds. `--design-check` exits 0 when the design file reads with no warning.

---

## 7. RELATED

- [`../SKILL.md`](../SKILL.md) is the FigJam mode these scripts serve
- [`../assets/README.md`](../assets/README.md) describes the composer and the templates the self-tests read
- [`figjam_checks/README.md`](figjam_checks/README.md) describes the rule modules
- [`vendored/README.md`](vendored/README.md) describes the vendored extractor
- [`../references/style-guide.md`](../references/style-guide.md) records the palette the checks hold to
