---
title: "Scripts: Repository Automation and Launchers"
description: "Python, shell and JavaScript entrypoints for vendored package synchronization and Code Mode startup."
trigger_phrases:
  - repository scripts
  - vendor synchronization
version: 1.0.1.0
---

# Scripts: Repository Automation and Launchers

---

## 1. OVERVIEW

`scripts/` contains the repository's vendor synchronization and Code Mode launch scripts. Its tests run vendor synchronization against temporary repositories.

Current state:

- `vendor-sync.py` compares package files with `vendor.json` and supports `status`, `sync`, `diff`, `pull`, `push` and `add`, reading upstream from a local checkout or from a cached clone of the public repository
- `update-vendored.sh` runs the sync and the gates as one command, and the Claude Code `/vendor-update` command runs it
- `code-mode.cjs` checks the Code Mode server build, resolves a Node interpreter that meets the server manifest and starts the server through the vendored launcher

Vendor synchronization reads and updates `vendor.json`, copies package files between the repository and the shared skill tree, and does not commit upstream changes.

---

## 2. ARCHITECTURE

```text
Repository operator
    ├── update-vendored.sh ──▶ vendor-sync.py ──▶ vendor.json
    │                                          ├── shared skill tree
    │                                          └── cached clone of the public repository
    └── .mcp.json / opencode.json ──▶ code-mode.cjs
                                       ├── node-engine-resolver.cjs
                                       └── mcp-code-mode-launcher.cjs ──▶ mcp-code-mode server
```

`vendor-sync.py` uses `vendor.json` to locate local and upstream files, and reads upstream from whichever of the two sources the run selects. `code-mode.cjs` uses the Node range in `mcp-code-mode/mcp-server/package.json` to select an installed interpreter before it starts the built entrypoint.

---

## 3. DIRECTORY TREE

```text
scripts/
+-- README.md
+-- code-mode.cjs
+-- update-vendored.sh
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
| `scripts/vendor-sync.py` | Checks, syncs, diffs, pulls, pushes or adds packages recorded in `vendor.json` |
| `scripts/update-vendored.sh` | Syncs every entry from a local Skilled checkout or the public repository, prints the rebuild lines again and runs the gates |
| `scripts/code-mode.cjs` | Locates the built Code Mode server and launches it under a compatible Node interpreter |
| `scripts/tests/test_vendor_sync.py` | Exercises vendor synchronization using a temporary Git upstream, a temporary bare repository and a temporary local repository |
| `scripts/vendored/` | Contains the synchronized Code Mode launcher package |

`vendor.json` records six packages: `mcp-figma`, `mcp-click-up`, `mcp-browser-use`, `mcp-code-mode`, `code-mode-launcher` and `mermaid-extract`. The last one's copy sits in `sk-create-figjam/scripts/vendored`, outside this folder.

---

## 5. ENTRYPOINTS

| Command | Purpose |
|---|---|
| `bash scripts/update-vendored.sh [--package NAME] [--ref REF] [--remote \| --local-upstream]` | Syncs every entry from a local Skilled checkout or the public repository, prints the rebuild lines again and runs the gates |
| `/vendor-update` | Runs `update-vendored.sh` from Claude Code, defined in `.claude/commands/vendor-update.md` |
| `python3 scripts/vendor-sync.py status [--package NAME]` | Reports manifest, local and upstream state and ends by naming the entries out of step |
| `python3 scripts/vendor-sync.py status --local` | Compares each local copy with the hashes in `vendor.json` and reads no upstream, so it works in a standalone clone |
| `python3 scripts/vendor-sync.py sync [--package NAME]` | Pulls every entry that is behind upstream, leaves the rest alone and prints one line per entry |
| `python3 scripts/vendor-sync.py diff [--package NAME]` | Prints what differs between each local copy and upstream and writes nothing |
| `python3 scripts/vendor-sync.py pull [--package NAME]` | Copies upstream files to the local package and updates its baseline |
| `python3 scripts/vendor-sync.py push [--package NAME]` | Copies local package changes into the upstream working tree |
| `python3 scripts/vendor-sync.py add --package NAME --upstream PATH` | Writes a new `vendor.json` entry for an upstream path and pulls it |
| `node scripts/code-mode.cjs [arguments]` | Starts the Code Mode server and passes the arguments to it |

`vendor-sync.py` finds upstream by walking up from this repository to the folder that holds `.skilled`. Set `VENDOR_UPSTREAM_ROOT` to that folder when none sits above the repository. The override must hold `.skilled` too, and a path one level off is a setup error.

`--remote` reads upstream from a cached partial clone of the public Skilled repository instead, so a standalone clone syncs with no checkout above it. The clone keeps every commit and fetches a blob only when a checkout needs one, because the commit lookups read history. It lives in `VENDOR_UPSTREAM_CACHE`, else under `XDG_CACHE_HOME` or `~/.cache/product-owner-vendor/skilled`, and a later run fetches into it rather than cloning again. `VENDOR_UPSTREAM_URL` points the fetch at a mirror and `--ref` picks the branch, tag or commit, `main` by default. `--remote` outranks `VENDOR_UPSTREAM_ROOT`, which outranks the walk-up, and it is refused with `status --local`.

`add` writes the entry through the same manifest helpers and then pulls it. `--local-path` defaults to the last part of the upstream path, and `--exclude` defaults to `graph-metadata.json`, because this hub keeps one advisor identity. An explicit `--exclude` list replaces that default. It refuses a name `vendor.json` already holds, a local path that escapes the repository and a folder that already holds files, and it takes the entry back out when the pull fails.

`sync` prints one line per entry:

- `in step at <commit>` means nothing was rewritten, so `vendor.json` does not churn
- `pulled, N file(s) changed, now at <commit>` is followed by up to five upstream commit subjects for that path, which are the material for a changelog
- `rebuild: cd <folder> && ...` follows a pulled entry that keeps `node_modules` or `dist` out of the copy when a `package.json`, `package-lock.json` or `.nvmrc` changed, or when a `.ts`, `.tsx`, `.js`, `.mjs` or `.cjs` file changed outside `node_modules` and `dist`. The folder is the nearest ancestor of the changed file that holds a `package.json`, printed once
- `refused, <reason>` names local edits that upstream does not carry, uncommitted changes upstream or a never-pulled entry whose folder already holds other files, which only an explicit `pull` vendors over

`status` and `sync` end with a line shaped `N of M entries out of step: <names>` when any entry is out of step. `status --local` is the only form that needs no upstream, and `--local` is valid only with `status`. `diff` prints a unified diff from the local copy to upstream for each changed text file and one line for a binary file or a file that exists on one side only.

| Exit | Meaning |
|---|---|
| 0 | every selected entry is in step or matches its record, `add` wrote and pulled its entry, or `diff` has nothing to show |
| 1 | an entry drifted, a sync was refused or `diff` has something to show |
| 2 | setup error such as a missing, truncated or unreadable manifest, an entry with no name, an escaping path, a symlink, a bad `VENDOR_UPSTREAM_ROOT`, no upstream, a name `add` cannot use, a missing git or a failed clone, fetch or checkout |

`vendor-sync.py push` leaves the upstream changes uncommitted. The operator commits them upstream, then runs `sync` to update the local baseline.

---

## 6. DAY TO DAY

Upstream moved:

```bash
bash scripts/update-vendored.sh
```

That is the whole routine. It syncs every entry, prints any `rebuild:` line again under a heading, then runs the gates. Run each rebuild line it names, because a stale build is the one failure the gates cannot see. It exits 0 when the sync and every gate pass, 1 when the sync or any gate fails, and 2 on a bad argument. The gates still run after a refused sync, so both results show.

`update-vendored.sh` reads a local Skilled checkout when one sits above the repository, because that is faster and carries edits that have not been pushed yet. `--remote` and `--local-upstream` force either source. `--package NAME` limits the run to one entry and `--ref REF` reads another branch, tag or commit from the remote.

Then commit the pulled files with `vendor.json`. Write the changelog from the commit subjects `sync` printed.

A new skill, mode or hub:

```bash
python3 scripts/vendor-sync.py add --package NAME --upstream .skilled/skills/<area>/<skill>
bash scripts/update-vendored.sh
```

The first command writes the entry and pulls it. The second proves the whole tree is still in step and the gates still pass.

A fix made here, edit the vendored file first, then:

```bash
python3 scripts/vendor-sync.py push --package mcp-click-up
# commit the change in the Skilled repository, then
python3 scripts/vendor-sync.py sync --package mcp-click-up
```

Then run the gates and commit the re-baselined `vendor.json`. Run `diff` first to see what would move. A `+` line is upstream's and a `-` line is the local copy's.

---

## 7. WHAT THE CODE MODE ENTRY LEAVES OUT

The `mcp-code-mode` entry excludes four names. `node_modules` and `dist` are build output, so a pull never copies them and carries a local build across the swap. `mcp-server/README.md` is a symlink to `../README.md` upstream and this script refuses symlinks, so the entry skips that one path and the copy keeps the real `README.md`. `graph-metadata.json` stays out because upstream's copy names the skill `mcp-code-mode` and the hub `SKILL.md` allows only the hub's own `graph-metadata.json`, so the advisor finds one identity.

---

## 8. SKILLED'S OVERLAY ENGINE

Skilled ships an overlay engine, `/doctor:overlay`. It carries a project's own edits across a whole-tree re-copy of `.skilled`. This repository does not use it. The engine keeps one tree with one pin, while each entry here has its own pin. It has no include list, so it cannot vendor a single file. It never pushes a fix back upstream. These copies also carry no local edits by rule, so there is nothing to carry. A package-scoped repin upstream or local edits kept here would change that.

---

## 9. VALIDATION

Run from the repository root:

```bash
python3 -m pytest -q scripts/tests
python3 scripts/vendor-sync.py status
python3 scripts/vendor-sync.py status --local
python3 scripts/vendor-sync.py status --remote
python3 -m py_compile scripts/vendor-sync.py scripts/tests/test_vendor_sync.py
bash -n scripts/update-vendored.sh
shellcheck scripts/update-vendored.sh
node --check scripts/code-mode.cjs
```

Expected result: pytest reports 41 passed tests. Vendor status prints each package state, returns 1 for drift and 2 for setup errors. `status --local` needs no upstream and returns 1 when a local copy differs from `vendor.json`. `status --remote` needs network and git 2.25 or later. Syntax checks and shellcheck exit with status 0.

---

## 10. RELATED

- [`scripts/tests/README.md`](tests/README.md) describes the vendor synchronization tests
- [`scripts/vendored/README.md`](vendored/README.md) describes the synchronized Code Mode files
- [`.claude/commands/vendor-update.md`](../.claude/commands/vendor-update.md) runs the update from Claude Code
- [`README.md`](../README.md) describes the repository
