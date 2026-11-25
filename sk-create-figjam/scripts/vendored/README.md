---
title: "FigJam Vendored: Mermaid Extractor"
description: "Orientation for the Mermaid extractor vendored from the shared diagram skill into the FigJam scripts."
trigger_phrases:
  - mermaid extract vendor
  - figjam vendored
version: 1.0.0.0
---

# FigJam Vendored: Mermaid Extractor

---

## 1. OVERVIEW

`sk-create-figjam/scripts/vendored/` holds `mermaid_extract.py`, the parser `../flow_check.py` and `../compose_board.py` use for flowchart and state blocks. It reads Mermaid text into a normalized representation and never evaluates, renders, fetches or runs a label, directive or URL.

The file is a byte copy of `.skilled/skills/sk-design/sk-design-diagram/scripts/mermaid_extract.py` in the shared skill tree, recorded as package `mermaid-extract` in `vendor.json` at the repository root. Only that one file is vendored, so this README is local and a sync never touches it.

---

## 2. FILES

| File | Responsibility |
|---|---|
| `mermaid_extract.py` | Parses flowchart, sequence, state and ER Mermaid from `.mmd`, `.mermaid` or Markdown fences, and prints a digest or JSON |

---

## 3. VENDOR WORKFLOW

Never edit `mermaid_extract.py` here. Make fixes in the shared skill tree, then run from the repository root:

```bash
bash scripts/update-vendored.sh --package mermaid-extract
```

Check the recorded copy with:

```bash
python3 scripts/vendor-sync.py status --package mermaid-extract
```

Expected result: vendor status reports `mermaid-extract` in step. In a standalone clone with no Skilled checkout above it, add `--remote`, or use `--local` to check the copy against `vendor.json` alone.

---

## 4. RELATED

- [`../README.md`](../README.md) describes the scripts that import the extractor
- [`../../../scripts/README.md`](../../../scripts/README.md) describes the vendor synchronization scripts
