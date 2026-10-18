---
title: "Implementation Summary"
description: "Product Owner replies now follow one Delivery Reply Shape with numbered Open items, the draft comes after one question round, the Doc examples pass the format gate under an example lint, and Catalog entry headings may carry one em dash."
trigger_phrases:
  - "deal templates upgrades implementation summary"
importance_tier: "normal"
contextType: "general"
_memory:
  continuity:
    packet_pointer: "016-deal-templates-upgrades"
    last_updated_at: "2026-10-18T18:00:00Z"
    last_updated_by: "claude-code"
    recent_action: "Closed the packet: every gate passes"
    next_safe_action: "Resync the handed-over systems.py pairs, then commit when the operator asks"
    blockers: []
    key_files:
      - "sk-product-owner/assets/interactive-response-templates.md"
      - "claude project/Custom Instructions.md"
      - "benchmark/gates/example_lint.py"
    session_dedup:
      fingerprint: "sha256:0000000000000000000000000000000000000000000000000000000000000000"
      session_id: "61ef885c-592f-4cc5-8163-827a30b0a258"
      parent_session_id: null
    completion_pct: 100
    open_questions: []
    answered_questions:
      - "Catalog em dash: widen the exception"
      - "Explicit commands: keep asking first"
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
| **Spec Folder** | 016-deal-templates-upgrades |
| **Completed** | 2026-10-18 |
| **Level** | 2 |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:what-built -->
## What Was Built

Every reply you get now opens on its path line and ends on one closing line, with one quality line and numbered Open items in between.

### One reply shape, one question round

Interactive Response Templates Section 3 holds the shape, a wrong first line beside the right one, and three worked replies. The other surfaces point there. After you answer one question round, the next reply drafts, and anything assumed lands under Open items as a bold topic with Situation and Open bullets.

### Examples that pass their own gate

The six failing Doc examples are fixed on both packagings. `example_lint.py` keeps them honest, and `run_gates.sh` runs every gate in one command. Catalog entry headings and their links may carry one em dash, inside a Catalog with an Index heading.

### Files Changed

| File | Action | Purpose |
|------|--------|---------|
| `sk-product-owner/assets/interactive-response-templates.md` and mirror | Modified | Delivery Reply Shape |
| `AGENTS.md`, `SKILL.md`, four references, `doc-templates.md`, mirrors | Modified | Pointers, one round, Catalog grant |
| Seven Doc examples and mirrors | Modified | Gate-clean examples |
| `claude project/Custom Instructions.md` | Modified | Kernel v1.2.1 |
| Both `validate-output-format.cjs` twins | Modified | Catalog grant |
| `benchmark/format/run_fixtures.sh`, three fixtures | Modified, Created | Catalog cases |
| `benchmark/gates/example_lint.py`, `run_gates.sh` | Created | Example lint, gate runner |
| READMEs, `SYNC.md`, playbook, `changelog/v1.2.1.0.md` | Modified, Created | Records |
<!-- /ANCHOR:what-built -->

---

<!-- ANCHOR:how-delivered -->
## How It Was Delivered

Skill source first, then the mirrors, a dated `SYNC.md` note and the changelog. Each edit stayed on its own line so no cited line moved. Static checks only, nothing committed.
<!-- /ANCHOR:how-delivered -->

---

<!-- ANCHOR:decisions -->
## Key Decisions

| Decision | Why |
|----------|-----|
| Worked replies live in the always-loaded Section 3, not in example preambles | The validator would flag self-scan lines inside an artifact example |
| Explicit commands still ask first | Operator decision, as v0.12.0.0 set it |
| Catalog grant needs an Index heading and a stable ID | Keeps the exception narrow, so prose em dashes still fail |
| Patch steps only | Operator choice, though `SYNC.md` says minor |
<!-- /ANCHOR:decisions -->

---

<!-- ANCHOR:verification -->
## Verification

| Check | Result |
|-------|--------|
| Gate runner | PASS, all 5 gates |
| Format fixtures | PASS, 59 cases |
| Router fixtures and differential | PASS, 117/117 and 189/189 |
| Example lint and self-test | PASS, 42 files; 3 self-test cases |
| Reference parity | PASS, identical |
| Other systems' format fixtures | PASS, Deal Templates, Copywriter, Sales Direct |
| Playbook validator | PASS, 46 scenarios, 0 violations |
| Residency | 6 findings, every one covered by a handed-over resync pair |
<!-- /ANCHOR:verification -->

---

<!-- ANCHOR:limitations -->
## Known Limitations

1. **Residency waits on a resync.** `systems.py` was not edited, so residency stays red until the handed-over pairs land.
2. **Shared card not updated.** The Human Voice card still lists only the definition and status grants.
3. **Kernel not reviewed or deployed.** The `SYNC.md` entry is a change record only.
<!-- /ANCHOR:limitations -->

---
