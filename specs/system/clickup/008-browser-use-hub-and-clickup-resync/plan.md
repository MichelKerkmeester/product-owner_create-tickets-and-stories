---
title: "Implementation Plan: Browser Use hub and ClickUp resync"
description: "Product Owner vendors the Skilled mcp-browser-use hub in place of the two browser packets and resyncs mcp-click-up, so the ClickUp page routines name browser packets that exist in this repository."
trigger_phrases:
  - "browser use hub and clickup resync plan"
importance_tier: "normal"
contextType: "general"
---
<!-- SPECKIT_TEMPLATE_SOURCE: plan-core | v2.4 -->
# Implementation Plan: Browser Use hub and ClickUp resync

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
One `vendor.json` entry for the `mcp-browser-use` hub replaces the two browser entries, and the two old folders are deleted. `mcp-click-up`, `mcp-figma` and `mcp-code-mode` are pulled to the latest Skilled commits. `mode-registry.json` lists the hub as a repository path, and the hub docs name it where they named the two packets.

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
Vendored owner, Product Owner pointer

### Key Components
- **`vendor.json`**: records upstream path, commit and file hashes
- **`mode-registry.json` `repo-root-hub`**: declares non-mode folders

### Data Flow
`vendor-sync.py pull` copies the hub with `graph-metadata.json` left out, and the gate run compares each copy with upstream.
<!-- /ANCHOR:architecture -->

---

<!-- ANCHOR:phases -->
## 4. IMPLEMENTATION PHASES

Follow the ordered tasks in `tasks.md`.
<!-- /ANCHOR:phases -->

---

<!-- ANCHOR:testing -->
## 5. TESTING STRATEGY

`bash benchmark/gates/run_gates.sh` and `python3 scripts/vendor-sync.py status` with `VENDOR_UPSTREAM_ROOT` set to the Skilled checkout.
<!-- /ANCHOR:testing -->

---

<!-- ANCHOR:dependencies -->
## 6. DEPENDENCIES

The Skilled checkout, read through `VENDOR_UPSTREAM_ROOT`.
<!-- /ANCHOR:dependencies -->

---

<!-- ANCHOR:rollback -->
## 7. ROLLBACK PLAN

Revert the Product Owner commit. A vendored copy returns with `vendor-sync.py pull` against an earlier upstream commit.
<!-- /ANCHOR:rollback -->

---
