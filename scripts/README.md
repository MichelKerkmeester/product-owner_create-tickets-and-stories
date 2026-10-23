---
title: "Scripts: Repository Automation and Launchers"
description: "Python and JavaScript entrypoints for plugin builds, vendored package synchronization and Code Mode startup."
trigger_phrases:
  - repository scripts
  - plugin build script
  - vendor synchronization
version: 1.0.0.0
---

# Scripts: Repository Automation and Launchers

---

## 1. OVERVIEW

`scripts/` contains the repository's plugin build, vendor synchronization and Code Mode launch scripts. Its tests run vendor synchronization against temporary repositories.

Current state:

- `build-plugin.py` rebuilds `claude-plugin/skills/product-owner` from the hub and registered packets, then verifies the generated file hashes
- `vendor-sync.py` compares package files with `vendor.json` and supports `status`, `pull` and `push`
- `code-mode.cjs` checks the Code Mode server build, resolves a Node interpreter that meets the server manifest and starts the server through the vendored launcher

The build writes generated files to `claude-plugin/skills/`. Vendor synchronization reads and updates `vendor.json`, copies package files between the repository and the shared skill tree, and does not commit upstream changes.

---

## 2. ARCHITECTURE

```text
Repository operator
    ├── build-plugin.py ──▶ claude-plugin/skills/product-owner
    ├── vendor-sync.py ──▶ vendor.json and shared skill tree
    └── .mcp.json / opencode.json ──▶ code-mode.cjs
                                       ├── node-engine-resolver.cjs
                                       └── mcp-code-mode-launcher.cjs ──▶ mcp-code-mode server
```

`vendor-sync.py` uses `vendor.json` to locate local and upstream files. `code-mode.cjs` uses the Node range in `mcp-code-mode/mcp-server/package.json` to select an installed interpreter before it starts the built entrypoint.

---

## 3. DIRECTORY TREE

```text
scripts/
+-- build-plugin.py
+-- code-mode.cjs
+-- vendor-sync.py
+-- tests/
|   +-- README.md
|   `-- test_vendor_sync.py
`-- vendored/
    +-- README.md
    `-- code-mode/
        +-- README.md
        +-- mcp-code-mode-launcher.cjs
        `-- lib/
            +-- README.md
            `-- node-engine-resolver.cjs
```

---

## 4. KEY FILES

| Path | Responsibility |
|---|---|
| `scripts/build-plugin.py` | Builds the Claude Code plugin skills tree, checks freshness or runs its scratch-tree self-test |
| `scripts/vendor-sync.py` | Checks, pulls or pushes packages recorded in `vendor.json` |
| `scripts/code-mode.cjs` | Locates the built Code Mode server and launches it under a compatible Node interpreter |
| `scripts/tests/test_vendor_sync.py` | Exercises vendor synchronization using temporary Git repositories |
| `scripts/vendored/` | Contains the synchronized Code Mode launcher package |

---

## 5. ENTRYPOINTS

| Command | Purpose |
|---|---|
| `python3 scripts/build-plugin.py` | Rebuilds and verifies the generated plugin skills tree |
| `python3 scripts/build-plugin.py --check` | Checks the generated tree without rewriting it |
| `python3 scripts/build-plugin.py --self-test` | Runs build refusal scenarios in a temporary repository copy |
| `python3 scripts/vendor-sync.py status [--package NAME]` | Reports manifest, local and upstream state |
| `python3 scripts/vendor-sync.py pull [--package NAME]` | Copies upstream files to the local package and updates its baseline |
| `python3 scripts/vendor-sync.py push [--package NAME]` | Copies local package changes into the upstream working tree |
| `node scripts/code-mode.cjs [arguments]` | Starts the Code Mode server and passes the arguments to it |

`vendor-sync.py push` leaves the upstream changes uncommitted. The operator commits them upstream, then runs `pull` to update the local baseline.

---

## 6. VALIDATION

Run from the repository root:

```bash
python3 -m pytest -q scripts/tests
python3 scripts/build-plugin.py --check
python3 scripts/vendor-sync.py status
python3 -m py_compile scripts/build-plugin.py scripts/vendor-sync.py scripts/tests/test_vendor_sync.py
node --check scripts/code-mode.cjs
```

Expected result: pytest reports passing tests. The plugin check prints `FRESH` when the generated tree matches its sources and `STALE` when it does not. Vendor status prints each package state, returns 1 for drift and 2 for setup errors. Syntax checks exit with status 0.

---

## 7. RELATED

- [`scripts/tests/README.md`](tests/README.md) describes the vendor synchronization tests
- [`scripts/vendored/README.md`](vendored/README.md) describes the synchronized Code Mode files
- [`README.md`](../README.md) describes the repository
