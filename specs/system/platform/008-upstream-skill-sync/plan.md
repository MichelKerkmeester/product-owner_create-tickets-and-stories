---
title: "Implementation Plan: Upstream skill sync"
description: "vendor-sync.py fetches vendored skills from the public Skilled repository, adds a new skill, mode or hub by its upstream path, flags rebuilds on source changes and runs as one update command."
trigger_phrases:
  - "upstream skill sync plan"
importance_tier: "normal"
contextType: "general"
---
<!-- SPECKIT_TEMPLATE_SOURCE: plan-core | v2.4 -->
# Implementation Plan: Upstream skill sync

<!-- SPECKIT_LEVEL: 1 -->

---

<!-- ANCHOR:summary -->
## 1. SUMMARY

### Technical Context

| Aspect | Value |
|--------|-------|
| **Language/Stack** | Markdown skill docs, vendored skill packages |
| **Framework** | Product Owner hub |
| **Storage** | None |
| **Testing** | `run_gates.sh`, `vendor-sync.py status`, live ClickUp pages |

### Overview
`vendor-sync.py` gains a `--remote` source, an `add` command and a source-file rebuild trigger. `scripts/update-vendored.sh` runs the sync and the gates as one command, and `.claude/commands/vendor-update.md` runs that script for an agent.

<!-- /ANCHOR:summary -->

---

<!-- ANCHOR:quality-gates -->
## 2. QUALITY GATES

### Definition of Ready
- [x] Problem statement clear and scope documented
- [x] Success criteria measurable
- [x] Dependencies identified

### Definition of Done
- [x] All acceptance criteria met
- [x] `run_gates.sh` fails no gate that passed in the baseline
- [x] Docs updated (spec/plan/tasks)
<!-- /ANCHOR:quality-gates -->

---

<!-- ANCHOR:architecture -->
## 3. ARCHITECTURE

### Pattern
One script, three upstream sources

### Key Components
- **`remote_upstream_root()`**: a cached partial clone of the public Skilled repository, sparse to the vendored paths
- **`add_package()`**: writes a `vendor.json` entry and pulls it
- **`scripts/update-vendored.sh`**: sync, rebuild lines, then the gates

### Data Flow
`--remote` resolves the clone and sets it as the upstream root, so every command reads it the same way as a local checkout.
<!-- /ANCHOR:architecture -->

---

<!-- ANCHOR:phases -->
## 4. IMPLEMENTATION PHASES

Follow the ordered tasks in `tasks.md`.
<!-- /ANCHOR:phases -->

---

<!-- ANCHOR:testing -->
## 5. TESTING STRATEGY

`python3 scripts/tests/test_vendor_sync.py`, a real `status --remote` fetch and `bash scripts/update-vendored.sh --remote`.
<!-- /ANCHOR:testing -->

---

<!-- ANCHOR:dependencies -->
## 6. DEPENDENCIES

git 2.25 or later and network access to GitHub for `--remote`.
<!-- /ANCHOR:dependencies -->

---

<!-- ANCHOR:rollback -->
## 7. ROLLBACK PLAN

Revert the commit. `vendor.json` and the vendored folders are untouched by this change.
<!-- /ANCHOR:rollback -->

---
