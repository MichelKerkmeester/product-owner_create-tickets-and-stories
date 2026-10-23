---
title: "Code Mode Vendor: Launcher and Node Resolver"
description: "Orientation for the vendored Code Mode process launcher and Node engine resolver."
trigger_phrases:
  - code mode vendor
  - node engine resolver
version: 1.0.0.0
---

# Code Mode Vendor: Launcher and Node Resolver

---

## 1. OVERVIEW

`scripts/vendored/code-mode/` contains two files imported by `scripts/code-mode.cjs`. The wrapper checks for the built Code Mode entrypoint, resolves a Node executable from `mcp-code-mode/mcp-server/package.json` and starts the child process through `runServer`.

The server manifest currently requires Node `>=24.0.0 <25.0.0`. The wrapper passes command-line arguments to the server and inherits its standard input, output and error streams.

---

## 2. ARCHITECTURE

```text
.mcp.json / opencode.json
    └── node scripts/code-mode.cjs
            ├── checks mcp-code-mode/mcp-server/dist/index.js
            ├── resolveNodeInterpreter ──▶ package.json engines.node
            └── runServer ──▶ Node child process
```

`resolveNodeInterpreter` chooses an installed Node version accepted by the manifest. `runServer` starts the server entrypoint, forwards host signals to the child and reports the child's exit status.

---

## 3. DIRECTORY TREE

```text
scripts/vendored/code-mode/
+-- README.md
+-- mcp-code-mode-launcher.cjs
`-- lib/
    +-- README.md
    `-- node-engine-resolver.cjs
```

---

## 4. KEY FILES

| File | Responsibility |
|---|---|
| `scripts/vendored/code-mode/mcp-code-mode-launcher.cjs` | Exports the runner that starts the server process and manages signals |
| `scripts/vendored/code-mode/lib/node-engine-resolver.cjs` | Resolves a matching Node interpreter from the host and version manager paths |
| `scripts/code-mode.cjs` | Repository wrapper that checks the build, resolves Node and invokes the runner |

---

## 5. VENDOR WORKFLOW

These files are vendored from `.skilled/bin` in the shared skill tree through `scripts/vendor-sync.py`, package `code-mode-launcher`. Never edit these files here. Make fixes in the shared skill tree, then run `python3 scripts/vendor-sync.py pull --package code-mode-launcher` from the repository root.

Check the recorded copy with:

```bash
python3 scripts/vendor-sync.py status --package code-mode-launcher
```

Expected result: vendor status reports `code-mode-launcher` in step.

---

## 6. RELATED

- [`scripts/README.md`](../../README.md) describes the repository scripts
- [`scripts/vendored/README.md`](../README.md) describes the vendored directory
- [`scripts/vendored/code-mode/lib/README.md`](lib/README.md) describes the resolver
- [`scripts/code-mode.cjs`](../../code-mode.cjs) is the local launch wrapper
