---
title: "Code Mode Resolver Library: Node Engine Selection"
description: "Documents the vendored resolver that selects a Node interpreter for the Code Mode server."
trigger_phrases:
  - node resolver library
  - node engine selection
version: 1.0.0.0
---

# Code Mode Resolver Library: Node Engine Selection

---

## 1. OVERVIEW

`scripts/vendored/code-mode/lib/` contains the Node engine resolver imported by `scripts/code-mode.cjs`. It reads the server manifest's `engines.node` range, enumerates visible Node interpreters and returns the highest candidate that satisfies that range.

The resolver checks the running interpreter, `PATH` entries and the configured nvm, fnm and Volta directory layouts. For a `PATH` candidate without a version in its path, it can inspect the real path and make a bounded version probe.

---

## 2. FILES

| File | Responsibility |
|---|---|
| `scripts/vendored/code-mode/lib/node-engine-resolver.cjs` | Parses Node versions and ranges, enumerates candidates and resolves a compatible interpreter |

---

## 3. EXPORTED FUNCTIONS

| Function | Purpose |
|---|---|
| `enumerateNodeCandidates` | Lists visible interpreter candidates ordered by version |
| `isNodeVersionInRange` | Checks a parsed version against a parsed range |
| `parseNodeEngineRange` | Parses supported major shorthand and comparator range forms |
| `parseNodeVersion` | Parses a Node version string into numeric components |
| `resolveNodeInterpreter` | Reads a package manifest and selects the highest matching candidate |

---

## 4. VENDOR WORKFLOW

This file is vendored from `.skilled/bin` in the shared skill tree through `scripts/vendor-sync.py`, package `code-mode-launcher`. Never edit it here. Make fixes in the shared skill tree, then run `python3 scripts/vendor-sync.py pull --package code-mode-launcher` from the repository root.

Check the recorded copy with:

```bash
python3 scripts/vendor-sync.py status --package code-mode-launcher
```

Expected result: vendor status reports `code-mode-launcher` in step.

---

## 5. RELATED

- [`scripts/README.md`](../../../README.md) describes the repository scripts
- [`scripts/vendored/code-mode/README.md`](../README.md) describes the launcher package
- [`scripts/vendor-sync.py`](../../../vendor-sync.py) synchronizes the package
- [`scripts/code-mode.cjs`](../../../code-mode.cjs) calls the resolver
