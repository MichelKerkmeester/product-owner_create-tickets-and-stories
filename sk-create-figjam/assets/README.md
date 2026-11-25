---
title: "FigJam Assets: Composer, Design and Model Templates"
description: "The board composer, the editable board design and the Mermaid templates, examples and screenshots FigJam mode builds from."
trigger_phrases:
  - figjam assets
  - figjam board composer
  - figjam templates
version: 1.0.0.0
---

# FigJam Assets: Composer, Design and Model Templates

---

## 1. OVERVIEW

`sk-create-figjam/assets/` holds what a FigJam board is built from. `compose-board.js` is the composer code one `use_figma` call runs, `figjam-design.md` is the design a team edits, and the template and example folders hold Mermaid models that pass the pre-write check.

`../scripts/compose_board.py` fills the composer's `__MODEL__` and `__THEME__` placeholders, so never paste `compose-board.js` by hand. The self-tests in `../scripts/` read the templates and examples, so a model added here must pass `flow_check.py`.

---

## 2. DIRECTORY TREE

```text
assets/
+-- README.md
+-- compose-board.js
+-- figjam-design.md
+-- flow-templates.md
+-- templates/       (architecture, er, gantt, process, sequence and state patterns)
+-- examples/        (worked models, one or more per diagram kind)
`-- screenshots/
    `-- README.md    (renders of composed boards, one per kind)
```

---

## 3. KEY FILES

| Path | Responsibility |
|---|---|
| `compose-board.js` | Draws one checked diagram as a framed board: title block, tinted zones, shapes sized to their text, routed connectors, a key and a source line on an 8 px grid |
| `figjam-design.md` | The board design as prose and one fenced json block: colour meanings, the first-glance accent, type sizes, lines, zone tints and key words |
| `flow-templates.md` | User-flow Mermaid patterns, the provenance table and the reply shape for Flow Mode |
| `templates/` | Patterns per diagram kind that pass the pre-write check |
| `examples/` | Worked models on fictional products, each with its intake, playback, gate message and reply |
| `screenshots/` | Renders of real composed boards, with the scenario and scorecard result each came from |

A bad edit to `figjam-design.md` never stops a board. A token that is unknown, of the wrong type or under a floor falls back to its built-in value with a warning that names it.

---

## 4. VALIDATION

Run from the `sk-create-figjam/` folder:

```bash
python3 scripts/compose_board.py --design-check
python3 scripts/flow_check.py --self-test
python3 scripts/compose_board.py --self-test
```

Expected result: `--design-check` exits 0 when the design reads with no warning. Each self-test ends with `N of N self-test checks passed`. The first includes every template and example. The second fills `compose-board.js` for every shipped model and checks the filled code. Never run `node --check` on the raw file: it uses top-level `await`, which is valid only once `use_figma` runs it as an async body.

---

## 5. RELATED

- [`../scripts/README.md`](../scripts/README.md) describes the check and the composer that fill this code
- [`screenshots/README.md`](screenshots/README.md) describes the board renders
- [`../SKILL.md`](../SKILL.md) is the FigJam mode these assets serve
