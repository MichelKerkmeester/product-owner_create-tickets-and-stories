---
title: "Implementation Summary"
description: "A Claude Desktop user guide for the ClickUp and Figma connectors, and every finding of the 005 review fixed or recorded."
trigger_phrases:
  - "claude project fixes implementation summary"
importance_tier: "normal"
contextType: "implementation"
_memory:
  continuity:
    packet_pointer: "019-runtime-and-project-optimization/006-claude-project-fixes"
    last_updated_at: "2026-10-21T17:30:00Z"
    last_updated_by: "claude-code"
    recent_action: "Wrote USER-GUIDE.md and fixed the review findings"
    next_safe_action: "The operator reviews the kernel and approves the commit"
    blockers: []
    key_files:
      - "USER-GUIDE.md"
      - "claude project/Custom Instructions.md"
    session_dedup:
      fingerprint: "sha256:0000000000000000000000000000000000000000000000000000000000000000"
      session_id: "1004bf13-7863-4447-a63e-6ad2f5fcfd86"
      parent_session_id: null
    completion_pct: 100
    open_questions: []
    answered_questions: []
---
<!-- SPECKIT_TEMPLATE_SOURCE: impl-summary-core | v2.2 -->
# Implementation Summary

<!-- SPECKIT_LEVEL: 2 -->
<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->

---

<!-- ANCHOR:metadata -->
## Metadata

| Field | Value |
|-------|-------|
| **Spec Folder** | 006-claude-project-fixes |
| **Status** | Complete |
| **Completed** | 2026-10-21 |
| **Level** | 2 |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:what-built -->
## What Was Built

### Findings

| ID | Outcome |
|----|---------|
| R2-P1-001, R2-P1-002, R2-P2-001, R2-P2-002 | Fixed. A root `USER-GUIDE.md` in Media Editor's shape: overview, what you need, adding both connectors under **Settings > Connectors** with the URLs ClickUp and Figma publish, opening the Project and switching them on under **+ > Connectors**, a check per connector with the reply to expect, and eight troubleshooting rows. `README.md` and `claude project/README.md` link it |
| R3-P1-001 | Fixed. Kernel Section 9 makes the private doc two calls with `name`, `parent` and `create_page: false`, matching `sk-product-owner/SKILL.md` Section 7, and asks for a space or folder when none is named |
| R1-P1-002 | Fixed. "just do it" selects Quick in `references/router-contract.md`, `benchmark/router/route_contract.py`, kernel Section 11 and the kernel Quick row, with a new corpus input |
| R1-P1-001 | Fixed. ALWAYS 1 and ALWAYS 6 name the Flow exception |
| R1-P2-001 | Fixed. The Flow Quality Rubric mirror names the Flow Type document instead of a skill path |
| R1-P2-002 | Fixed. `README.md` routes Flow in its router line, counts the 7 FigJam examples and states 220 differential inputs |
| R1-P2-003 | Fixed. ESCALATE IF says `$flow` and `$figjam` follow their Brief |
| R3-P2-002 | Fixed. Templates - Flow Mode tags a write only when the connector reports a tool that runs Plugin API code, and says what happens without one |
| R3-P1-002 | Recorded, overstated. Figma's own docs list `generate_diagram` and `get_figjam` |
| R3-P2-001 | Recorded. It sits in the vendored `mcp-click-up/SKILL.md`, which is never edited here. `USER-GUIDE.md` says the Project reads tool names from the connector at run time |

### Files Changed

| File | Action | Purpose |
|------|--------|---------|
| `USER-GUIDE.md` | Created | The Claude Desktop connector guide |
| `README.md`, `claude project/README.md` | Modified | Links, the router line and the counts |
| `claude project/Custom Instructions.md` | Modified | Six kernel fixes, 68,814 to 69,339 bytes |
| `claude project/knowledge/` Flow Quality Rubric and Templates - Flow Mode | Modified | Project wording |
| `sk-product-owner/references/router-contract.md`, `benchmark/router/route_contract.py`, `benchmark/router/differential_corpus.json` | Modified | The Quick phrase and its corpus input |
| `SYNC.md` | Modified | A dated note |
| `z — Claude Project Sync Loop/systems.py`, in the outer repository | Modified | Three residency statements resynced |
<!-- /ANCHOR:what-built -->

---

<!-- ANCHOR:how-delivered -->
## How It Was Delivered

Each cited line was reopened before its edit. The guide names only menus that ClickUp's setup page or Media Editor's guide confirms, and says that labels can differ by Claude version. The connector URLs are the ones ClickUp and Figma publish.
<!-- /ANCHOR:how-delivered -->

---

<!-- ANCHOR:decisions -->
## Key Decisions

| Decision | Why |
|----------|-----|
| One guide for both connectors at the repository root | A Project user looks for setup beside the README, as Media Editor's users do |
| Leave the vendored ClickUp finding to upstream | Vendored packets are never edited locally |
<!-- /ANCHOR:decisions -->

---

<!-- ANCHOR:verification -->
## Verification

| Check | Result |
|-------|--------|
| `route_contract.py --request` with and without "just do it" | QUICK and STANDARD |
| `differential.py` | PASSED 220/220 differential inputs |
| `run_gates.sh`, format gate, format gate on `USER-GUIDE.md` | All 12 gates, 70 source files, the guide passes |
| `residency_check.py product-owner` in the scratch clone | PASSED after three statements resynced |
| `validate_parity.py product-owner` in the scratch clone | Only the `quality-scoring.md` review open since 018 |
<!-- /ANCHOR:verification -->

---

<!-- ANCHOR:limitations -->
## Known Limitations

1. **The guide's checks were not run against live connectors.** The first ClickUp and Figma sign-in is the operator's.
2. **Menu labels come from ClickUp's docs and Media Editor's guide.** Claude's own help pages were not read.
<!-- /ANCHOR:limitations -->
