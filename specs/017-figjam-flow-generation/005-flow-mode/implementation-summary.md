---
title: "Implementation Summary"
description: "Flow Mode is built: $flow and $figjam route to it, a pre-write check holds every model to the flowchart rules, and the reply is the board URL, a read-back line and the self-scan. The live board criteria wait on the hosted Figma MCP."
trigger_phrases:
  - "flow mode implementation summary"
importance_tier: "normal"
contextType: "general"
_memory:
  continuity:
    packet_pointer: "017-figjam-flow-generation/005-flow-mode"
    last_updated_at: "2026-10-20T09:30:00Z"
    last_updated_by: "claude-code"
    recent_action: "Built Flow Mode, fixed the deep-review findings and recorded the evidence"
    next_safe_action: "Connect the hosted Figma MCP and write the Change Location board"
    blockers:
      - "The hosted Figma MCP is not connected, so no board can be written or read back"
    key_files:
      - "sk-product-owner/references/flow-mode.md"
      - "sk-product-owner/assets/flow-templates.md"
      - "sk-product-owner/scripts/flow_check.py"
    session_dedup:
      fingerprint: "sha256:0000000000000000000000000000000000000000000000000000000000000000"
      session_id: "1004bf13-7863-4447-a63e-6ad2f5fcfd86"
      parent_session_id: null
    completion_pct: 70
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
| **Spec Folder** | 005-flow-mode |
| **Status** | In Progress |
| **Completed** | Not yet. The board criteria wait on the hosted Figma MCP |
| **Level** | 2 |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:what-built -->
## What Was Built

Product Owner can now draw a user flow. `$flow`, `$figjam` or FigJam wording such as "make a FigJam flow from these screenshots" routes to Flow Mode, which reads screenshots, a Figma flow or a product doc, writes a Mermaid model with a provenance table, checks it, and writes it to a FigJam board after a yes.

### Phase 5: flow-mode

You get a board that cannot drift into a shape the generator mangles, because `sk-product-owner/scripts/flow_check.py` refuses a model before the write: an unknown shape, a decision with more than 3 exits or an unlabelled exit, more than 9 nodes, a direction other than top to bottom, a label with a line break or markup, or more than one accent colour. It parses with `sk-product-owner/scripts/vendored/mermaid_extract.py`, a byte copy of the shared diagram skill's extractor kept in step through `vendor.json`. The reply is the board URL, a `Read-back:` line with counts measured on the board, and the `HVR self-scan:` line, and Flow Mode writes nothing to `export/`.

### Files Changed

| File | Action | Purpose |
|------|--------|---------|
| sk-product-owner/references/flow-mode.md | Created | Workflow, intake per input type, flowchart rules, the hosted and `fj` routes, delivery, recovery |
| sk-product-owner/assets/flow-templates.md | Created | Five patterns that pass the check, the provenance table and the three-line reply |
| sk-product-owner/scripts/flow_check.py | Created | The pre-write check and its 8-row self-test |
| sk-product-owner/scripts/vendored/mermaid_extract.py, vendor.json | Created, Modified | The vendored extractor and its `include` package entry |
| scripts/vendor-sync.py, scripts/tests/test_vendor_sync.py | Modified | Single-file `include` packages, and path containment for every manifest path |
| benchmark/router/route_contract.py, references/router-contract.md, claude project/Custom Instructions.md | Modified | The FLOW intent, kept equal across the three copies |
| benchmark/router/fixtures.json, differential_corpus.json | Modified | 6 Flow fixtures and a flow-mode corpus group |
| sk-product-owner/ROUTER.md, AGENTS.md | Modified | Commands, routing, the export exemption, the self-scan in the Flow reply |
| SKILL.md, hub-router.json, benchmark/gates/check_hub.py | Modified | Clarification words route to Product Owner, and the gate compares the hub prose with the router |
| Change Location model in the private Product Context repo | Created | The pass case: 8 nodes, 8 connectors, 2 labelled exits |
<!-- /ANCHOR:what-built -->

---

<!-- ANCHOR:how-delivered -->
## How It Was Delivered

The check and its self-test came first, then the routing in all three router copies with fixtures, then the reference and templates. A five-iteration deep review with GPT-6 Luna at max reasoning found 4 P1 and 6 P2 findings, all fixed and recorded in `../review/review-report.md` and the goal log. Every gate was rerun from the final state.
<!-- /ANCHOR:how-delivered -->

---

<!-- ANCHOR:decisions -->
## Key Decisions

| Decision | Why |
|----------|-----|
| The Flow reply carries the HVR self-scan as its third line | `AGENTS.md` step 8 requires the scan in every delivery. Flow is exempt from the export steps, not from the scan |
| The hosted route writes only into a new or confirmed-empty page | Its rollback clears the page, so a page holding other work could lose it. Superseded in phase 010: a FigJam file has one page, so the write now targets a file |
| `$figjam` has no single-letter alias | `$f` would read as an energy control |
| The one-accent rule reads the raw block | The extractor drops `style`, `classDef` and `linkStyle` lines before the check sees the model |
<!-- /ANCHOR:decisions -->

---

<!-- ANCHOR:verification -->
## Verification

| Check | Result |
|-------|--------|
| flow_check.py --self-test | PASS, 8 of 8: the good model passes and each of 7 planted models fails on its own rule |
| Change Location model and the 6 template diagrams | PASS, each through flow_check.py |
| Router fixtures | PASS, 123/123, among them `$flow the location change from these screenshots` and `make a FigJam flow from these screenshots`, both FLOW |
| Differential corpus | PASS, 201/201 |
| run_gates.sh | PASS, all 10 gates |
| Format gate | PASS, 44 source files, and the outer validator exits 0 on all four systems |
| Rendered files | 0 HTML, SVG, PNG or Mermaid files in git status outside the spec tree |
| Default Task read set, o200k | 28,109 tokens against 27,685 after phase 004. No criterion governs this phase. The rise is the Flow routing and export lines in AGENTS.md, ROUTER.md and the hub SKILL.md |
<!-- /ANCHOR:verification -->

---

<!-- ANCHOR:limitations -->
## Known Limitations

1. **No board has been written yet.** AC-003 and AC-004 need the hosted Figma MCP and a scratch FigJam file the operator names. Until then the reply contract is written and checked, but never observed on a real board.
2. **The `fj` route is unproven here.** It needs Figma Desktop and figma-ds-cli 1.2.0 or later with a healthy daemon.
<!-- /ANCHOR:limitations -->
