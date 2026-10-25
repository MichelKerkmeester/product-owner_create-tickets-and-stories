---
title: "Vendored Scripts: Synchronized Code Mode Files"
description: "Orientation for the Code Mode launcher files synchronized from the shared skill tree."
trigger_phrases:
  - vendored scripts
  - code mode launcher vendor
version: 1.0.0.0
---

# Vendored Scripts: Synchronized Code Mode Files

---

## 1. OVERVIEW

`scripts/vendored/` holds the files from the `code-mode-launcher` package that `scripts/code-mode.cjs` imports. The package comes from `.skilled/bin` in the shared skill tree and includes only the launcher and Node engine resolver.

These files are vendored through `scripts/vendor-sync.py`. Never edit them here. Make fixes in the shared skill tree, then run `python3 scripts/vendor-sync.py pull --package code-mode-launcher` from the repository root.

---

## 2. DIRECTORY TREE

```text
scripts/vendored/
+-- README.md
`-- code-mode/
    +-- README.md
    +-- mcp-code-mode-launcher.cjs
    `-- lib/
        +-- README.md
        `-- node-engine-resolver.cjs
```

---

## 3. KEY FILES

| Path | Responsibility |
|---|---|
| `scripts/vendored/code-mode/mcp-code-mode-launcher.cjs` | Starts the MCP server process and forwards child process signals |
| `scripts/vendored/code-mode/lib/node-engine-resolver.cjs` | Finds a Node interpreter that satisfies the server manifest range |
| `scripts/code-mode.cjs` | Checks the server build and calls the vendored resolver and process runner |

---

## 4. VALIDATION

Run from the repository root:

```bash
python3 scripts/vendor-sync.py status --package code-mode-launcher
node --check scripts/code-mode.cjs
```

Expected result: vendor status reports the package in step and Node exits with status 0.

---

## 5. RELATED

- [`scripts/README.md`](../README.md) describes the script entrypoints
- [`scripts/vendored/code-mode/README.md`](code-mode/README.md) describes the package files
- [`scripts/vendor-sync.py`](../vendor-sync.py) reads the package entry in `vendor.json`
