---
title: "Implementation Summary"
description: "The Project kernel is 6,407 bytes smaller with every rule kept, and the Router Code stays in the kernel on the earlier measured decision."
trigger_phrases:
  - "kernel size implementation summary"
importance_tier: "normal"
contextType: "implementation"
_memory:
  continuity:
    packet_pointer: "019-runtime-and-project-optimization/002-kernel-size"
    last_updated_at: "2026-10-21T21:00:00Z"
    last_updated_by: "claude-code"
    recent_action: "Cut table padding and duplicated rules from the kernel and resynced seven residency statements"
    next_safe_action: "Start phase 003, knowledge retrieval"
    blockers: []
    key_files:
      - "claude project/Custom Instructions.md"
      - "SYNC.md"
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
| **Spec Folder** | 002-kernel-size |
| **Status** | Complete |
| **Completed** | 2026-10-21 |
| **Level** | 2 |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:what-built -->
## What Was Built

`claude project/Custom Instructions.md` went from 75,165 to 68,758 bytes, 8.5% less on every Project turn, and the kernel stays at the unreleased v1.2.2.

- **Table padding:** 4,499 bytes, with no word changed. Section 4 lost 2,956 bytes and Section 8 lost 1,668.
- **Rules stated twice:** eight now sit in one place each. They are the HTML comment exemption, the example limit, the file-loading line, the plain `description` field, the export label lead-in, the `then: "FLOW"` offer timing, the self-scan placement and the Section 1 proposal and approval sentences.
- **Tightened with the rule kept:** the Doc gate's subject check in Section 2 and the quality line depth in Section 9. The Delivery Protocol is 1,173 bytes smaller.
- **Router Code:** unchanged. REQ-002's move or replace was not done, for the reason under Key Decisions.

### Rule count

The count splits the kernel above Section 11 into rule units, one sentence, bullet or table row each. Before the cuts there were 348 units and after them 334. Of the 26 units that changed, 3 are table separator rows. The other 23 each map to a statement that still holds their rule:

| Removed or reworded unit | Where its rule lives now |
|--------------------------|--------------------------|
| Proposal labelling in Boundary and When Not To Use, four sentences | One sentence in When Not To Use, plus Boundary's closing ban on fabricated approval |
| Gate substance explanation and comparison example | One sentence in Section 2 Executable Contract, comparison kept as the example |
| HTML comment exemption, twice | Deliverable Metadata, first paragraph |
| Example limit | Section 8 table row and Section 2 Resource Domains |
| File loading unavailable | Header line 2 and the retrieval sentence kept in Section 8 |
| Plain `description` effect, two sentences | One shorter sentence in ClickUp Connector Delivery and NEVER rule 2 |
| Quality line depth, three sentences | Two sentences in Deliverable Metadata that keep the five Doc checks |
| Export label lead-in, two sentences | Two shorter sentences in Export-Equivalent Paths |
| `then: "FLOW"` offer timing, two sentences | Flow Mode Delivery third bullet, pointed to from the offer paragraph |
| Self-scan placement, four sentences | One sentence in HVR Self-Scan, NEVER rule 5 and the Deliverable Metadata list |

### Files Changed

| File | Action | Purpose |
|------|--------|---------|
| `claude project/Custom Instructions.md` | Modified | The cuts |
| `SYNC.md` | Modified | A dated note naming v1.2.2, which the parity gate requires |
| `z — Claude Project Sync Loop/systems.py`, in the outer repository | Modified | Seven residency statements resynced to the new kernel text |
<!-- /ANCHOR:what-built -->

---

<!-- ANCHOR:how-delivered -->
## How It Was Delivered

Each statement was rewritten by `resync_statement.py` and checked in the scratch clone, since the Sync Loop gates refuse an uncommitted declaration. One statement's new text was a prefix of its old text, so the tool's guard against compounding skipped it, and it went through a one-off intermediate text in two steps. The resync touched only lines above the `prompt-improver` block. A first pass bumped the kernel to v1.2.3, and that was reverted, because v1.2.2 has not shipped and unshipped work folds into the pending version.
<!-- /ANCHOR:how-delivered -->

---

<!-- ANCHOR:decisions -->
## Key Decisions

| Decision | Why |
|----------|-----|
| Keep the Router Code in the kernel, unchanged | The 2026-09-30 run moved it into the kernel because a Project pulls Knowledge only by relevance. `ast.unparse` saves only 3 KB of its 27 KB and puts each topic table on one line of over 3,000 characters |
| Leave the ask-first lines and the Story format paragraph alone | The 2026-09-30 run found a larger kernel diluted ask-first, and Story format is what the PST scenarios check |
| Cut duplicates inside the kernel and not move rules to Knowledge | Moving a rule needs its words verbatim in a Knowledge file, which grows the set phase 003 is meant to shrink |
<!-- /ANCHOR:decisions -->

---

<!-- ANCHOR:verification -->
## Verification

| Check | Result |
|-------|--------|
| `wc -c` on the kernel | 75,165 before, 68,758 after, Section 11 26,994 both times |
| `benchmark/router/differential.py` | PASSED 219/219 differential inputs, 9 topics, 114 synonyms in parity |
| Rule count script over the old and new kernel | 348 units before, 334 after, 23 changed units each mapped above |
| `residency_check.py product-owner` in the scratch clone | PASSED, every declared statement owned and placed |
| `validate_parity.py product-owner` in the scratch clone | One finding, the open `quality-scoring.md` review that waits for the Product Owner commit, as before this phase |
| `bash benchmark/gates/run_gates.sh`, format gate | All 12 gates pass, format passed across 70 source files |
<!-- /ANCHOR:verification -->

---

<!-- ANCHOR:limitations -->
## Known Limitations

1. **No behavior run yet.** Phase 004 runs the Project playbook against this kernel.
2. **No human review of the kernel is recorded.** The SYNC.md note says one is needed.
3. **`residency_check.py --all` has a finding in Prompt Improver.** It comes from an uncommitted edit to that system's kernel in its own repository, outside this packet.
<!-- /ANCHOR:limitations -->
