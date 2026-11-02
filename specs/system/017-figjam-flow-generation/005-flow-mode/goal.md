---
title: "Goal: Phase 5: Flow Mode"
description: "The durable directive this packet executes against and the criteria that decide when it is done."
trigger_phrases:
  - "flow mode goal"
importance_tier: "important"
contextType: "planning"
_memory:
  continuity:
    packet_pointer: "product-owner/017-figjam-flow-generation/005-flow-mode"
    last_updated_at: "2026-10-20T00:00:00Z"
    last_updated_by: "scaffold"
    recent_action: "Authored the durable directive"
    next_safe_action: "Execute against the completion criteria"
    blockers: []
    key_files: []
    session_dedup:
      fingerprint: "sha256:0000000000000000000000000000000000000000000000000000000000000000"
      session_id: "unset"
      parent_session_id: null
    completion_pct: 0
    open_questions: []
    answered_questions: []
---
<!-- SPECKIT_TEMPLATE_SOURCE: goal | v2.2 -->
# Goal: Phase 5: Flow Mode

<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->
<!-- GOAL_AUTHORING: .skilled/skills/sk-doc/sk-create-goal/SKILL.md -->

---

<!-- ANCHOR:directive -->
## 1. DURABLE DIRECTIVE

**Objective:** Add Flow Mode to sk-product-owner so a request turns screenshots, Figma flows or product docs into a checked Mermaid model and a FigJam board, delivered as the board URL with a read-back line and the HVR self-scan line.

### Decisions

Frozen choices. Changing one is an amendment.

| ID | Decision |
|----|----------|
| D1 | The hosted generate_diagram route is primary and fj is the Figma Desktop fallback (operator, 2026-10-20). |
| D2 | Flow Mode is exempt from the export file step: it delivers the board URL plus a read-back line, with no file in export/ (operator, 2026-10-20). |
| D3 | Flow Mode answers to both $flow and $figjam (operator, 2026-10-20). |
| D4 | The pre-write check vendors mermaid_extract.py from sk-design-diagram through vendor.json (operator, 2026-10-20). |

<!-- /ANCHOR:directive -->

---


<!-- ANCHOR:completion -->
## 3. COMPLETION CRITERIA

- [x] The pre-write check fails a four-exit decision, an unlabelled decision exit, an unknown shape and a 10-node diagram, and passes the Change Location model
- [x] Router fixtures pass for the Flow command and for "make a FigJam flow from these screenshots"
- [ ] One board built from the 7 Change Location screenshots lands in a scratch FigJam file, with read-back counts equal to the model and every decision exit labelled
- [ ] The Flow Mode reply carries the board URL, a read-back line and the HVR self-scan line, and find export/ shows no new file
- [x] git status shows no HTML, SVG, PNG or Mermaid file created
<!-- /ANCHOR:completion -->

---

<!-- ANCHOR:log -->
## 4. LOG

Everything below is VOLATILE. It is not part of the directive, it is not copied
into the objective, and it is expected to grow. Progress, evidence, deviations
and findings belong here.

### Progress

| Item | State | Evidence |
|------|-------|----------|
| Phase opened | Done | Built 2026-10-20 |
| Pre-write check, routing, reference and templates | Done | flow_check.py 8 of 8, router 123/123, corpus 201/201, run_gates.sh 10 of 10 |
| Live board and its reply | Blocked | The hosted Figma MCP is not connected |

### Deviations and findings

| Item | Note |
|------|------|
| Deep review 2026-10-20 | The two-line reply contradicted the self-scan every delivery carries under `AGENTS.md` step 8. The reply gained the scan as its third line. D2's export exemption is unchanged |
<!-- /ANCHOR:log -->
