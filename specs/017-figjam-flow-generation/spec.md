---
title: "Feature Specification: Product Owner FigJam flow generation upgrade"
description: "Upgrade Product Owner to turn screenshots, Figma flows and product docs into FigJam flows, as a parent hub with an embedded figma skill and a Claude Code plugin."
trigger_phrases:
  - "figjam flow generation phase parent spec"
importance_tier: "important"
contextType: "implementation"
_memory:
  continuity:
    packet_pointer: "017-figjam-flow-generation"
    last_updated_at: "2026-10-19T21:00:00Z"
    last_updated_by: "template-author"
    recent_action: "Initialize phase-parent continuity block"
    next_safe_action: "Plan or resume a child phase folder"
    blockers: []
    key_files: []
    session_dedup:
      fingerprint: "sha256:0000000000000000000000000000000000000000000000000000000000000000"
      session_id: "template-session"
      parent_session_id: null
    completion_pct: 0
    open_questions: []
    answered_questions: []
---
<!-- SPECKIT_TEMPLATE_SOURCE: phase-parent-spec | v2.2 -->

<!-- SPECKIT_LEVEL: 2 -->
<!-- CONTENT DISCIPLINE: PHASE PARENT
  FORBIDDEN content (do NOT author at phase-parent level):
    - merge/migration/consolidation narratives (consolidate*, merged from, renamed from, collapsed, X→Y, reorganization history)
    - migrated from, ported from, originally in
    - heavy docs: plan.md, tasks.md, decision-record.md, implementation-summary.md — these belong in child phase folders only
  REQUIRED content (MUST author at phase-parent level):
    - Root purpose: what problem does this entire phased decomposition solve?
    - Sub-phase list: which child phase folders exist and what each one does
    - What needs done: the high-level outcome the phases work toward
-->

# Feature Specification: Product Owner FigJam flow generation upgrade

<!-- ANCHOR:metadata -->
## 1. METADATA

| Field | Value |
|-------|-------|
| **Level** | 2 |
| **Priority** | P1 |
| **Status** | Draft |
| **Created** | 2026-10-19 |
| **Branch** | `main` |
| **Parent Spec** | `../spec.md` |
| **Parent Packet** | product-owner/017-figjam-flow-generation |
| **Predecessor** | None |
| **Successor** | None |
| **Handoff Criteria** | Research synthesis approved, later phases added to the map, each phase validates alone |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:problem -->
## 2. PROBLEM & PURPOSE

### Problem Statement
Product Owner writes stories, epics and product docs but cannot turn screenshots, Figma flows or product docs into diagrams. The figma skill lives only in the shared `.skilled` repo, and Product Owner has neither a Claude Code plugin nor the parent-hub shape that Moneybird Accountant and Media Editor already show.

### Purpose
Deliver FigJam flow generation as the only output. Product Owner carries an embedded duplicate of the figma skill, gains a Claude Code plugin like Media Editor, becomes a parent hub like Moneybird Accountant, and can sync skill and plugin optimizations back to `.skilled` with little effort. Flow quality follows the rules in sk-design-diagram, translated to FigJam.

> **Phase-parent note:** This spec.md is the ONLY authored document at the parent level. All detailed planning, task breakdowns, checklists, and decisions live in the child phase folders listed in the Phase Documentation Map below. This keeps the parent from drifting stale as phases execute and pivot.
<!-- /ANCHOR:problem -->

---

<!-- ANCHOR:scope -->
## 3. SCOPE

### In Scope
- Research, then the build phases the research names: embedded figma skill, FigJam flow engine, Claude Code plugin, sync path to `.skilled`, hub conversion, verification.
- Inputs: screenshots, Figma flows and product docs. Output: FigJam only.

### Out of Scope
- HTML or SVG output - FigJam is the only output.
- Changes to the shared figma skill in `.skilled` during the build, except through the sync path.
- Commits and pushes without the operator's go-ahead.

### Files to Change
Detail is fixed by the research synthesis and lives in each child's plan.md.

| File Path | Change Type | Phase | Description |
|-----------|-------------|-------|-------------|
| research/ | Create | 001-research | Iterations, cross-checks and the synthesis |
<!-- /ANCHOR:scope -->

---

<!-- ANCHOR:phase-map -->
## PHASE DOCUMENTATION MAP

> This spec uses phased decomposition. Each phase is an independently executable child spec folder. All implementation details (plan, tasks, checklist, decisions, continuity) live inside the phase children.

| Phase | Folder | Focus | Status |
|-------|--------|-------|--------|
| 1 | 001-research/ | 20-iteration deep research and Opus 5.5 synthesis that names the later phases | Complete |
| 2 | 002-write-route-spike/ | Spike: scratch boards through hosted generate_diagram and through fj, tool capture, route decision note | Blocked: no Figma MCP in session |
| 3 | 003-vendored-figma-and-sync/ | Byte-identical vendored mcp-figma, vendor.json and vendor-sync.py status, pull and push | Complete |
| 4 | 004-parent-hub-conversion/ | Parent hub on the Moneybird pattern, routing readers repointed, baseline fixture counts held | Complete |
| 5 | 005-flow-mode/ | Flow Mode: inputs to a checked Mermaid model to a FigJam board, URL delivery exempt from export | Pending |
| 6 | 006-claude-code-plugin/ | Skills-only Claude Code plugin on the Media Editor build pattern | Pending |
| 7 | 007-project-mirror/ | Hand-written Claude Project mirror of Flow Mode with connector-conditional writing | Pending |
| 8 | 008-upstream-roundtrip-and-release/ | One real push to .skilled, re-baseline, release and clean-clone test | Pending |
| 9 | 009-figjam-skill-research/ | 20-iteration deep research on public FigJam diagram skills, ranked improvements for Flow Mode | Pending |
| 10 | 010-flow-mode-hardening/ | The 15 ranked changes from 009 applied to Flow Mode, its check, the Project mirror and the kernel | Complete |
| 11 | 011-figjam-packet-split/ | Flow Mode moved into its own hub packet, sk-create-figjam, routed at stage one | Complete |
| 12 | 012-vendored-clickup/ | mcp-click-up vendored into the hub as a byte copy kept in step by vendor-sync.py | Complete |
| 13 | 013-skilled-hub-alignment/ | The hub moved into product-owner/ on the skilled parent-hub contract, packet routing in each packet SKILL.md | Complete |
| 14 | 014-hub-to-root/ | The hub back at the repository root, its repository entries declared through the repo-root-hub extension | Complete |
| 15 | 015-figjam-rebuild/ | sk-create-figjam rebuilt for every FigJam diagram type, with sk-design-diagram quality rules and the research corpus translated to FigJam | Complete |
| 16 | 016-figjam-improvement-research/ | 10-iteration deep research on the public FigJam repos online and the packet's integration with sk-product-owner, ranked improvements | Complete |
| 17 | 017-board-link-in-artifact/ | A board URL whose read-back matched lands in the Flows group of the Story, Epic, Task, Bug or Doc it was made for | Complete |
| 18 | 018-artifact-plus-board-pair/ | A request for an artifact and a FigJam diagram together routes to the artifact with then FLOW, and the diagram follows from it | Complete |
| 19 | 019-hosted-route-connection/ | The packet says how the hosted Figma route is connected and that the vendored Code Mode wiring covers a different path | Complete |
| 20 | 020-accent-and-cut-test/ | The accent goes to the one node a reader would keep, a tie splits the diagram, and every node serves the userIntent sentence or is cut | Complete |
| 21 | 021-board-critic-pass/ | The runtime screenshot check covers crossings, misleading routes, accent placement and the reader question | Complete |
| 22 | 022-created-node-tags/ | A write tags the nodes it created so a revision in a later session can find and replace them | Complete |
| 23 | 023-kernel-no-connector-sentence/ | The kernel's no-connector sentence says the offered model is never the board and bans a stand-in | Complete |
| 24 | 024-flow-delivery-pointers/ | AGENTS.md and sk-product-owner/SKILL.md point at flow-mode.md Section 8 and name the Extensions line, and parent D6 matches the reply the packet ships | Complete |
| 25 | 025-plan-whoami/ | Where the server reports whoami, the packet resolves the plan before the gate and asks when there are several | Complete |
| 26 | 026-self-edit-guidance/ | A request to move, resize or restyle a generated node gets a plain answer and the user learns they can edit the board | Complete |
| 27 | 027-repeated-edge-labels/ | Four or more identical labels on non-decision edges become none or one, with decision exits and sequence messages exempt | Complete |
| 28 | 028-readback-direction/ | Read-back derives connector direction from endpoints and caps, never position, and retries a timed-out read on fewer nodes | Complete |
| 29 | 029-extension-fixes/ | Thirteen follow-up findings from phase 016 Section 9, as twelve nested child phases | Complete |
| 30 | 030-figjam-research-three/ | Three DeepSeek research runs: design output, input-to-model logic and an interactive intake | Complete |
| 31 | 031-round-three-apply/ | The 32 ranked changes of phase 030, as 32 nested child phases | Complete |
| 32 | 032-clickup-push-targets/ | ClickUp push targets set locally per artifact kind, with a private doc option | Complete |
| 33 | 033-composed-boards/ | Boards composed with use_figma for design quality, then a SWE 2 MAX rerun | Complete |
| 34 | 034-stop-and-label-fixes/ | Playback and gate kept apart, composed labels kept clear, notes contract reconciled, failed scenarios rerun | Complete |
| 35 | 035-first-glance-and-routing/ | Accent tied to the first glance, routing clear of zone borders and shared stubs, HVR line last, failed scenarios rerun | Complete |
| 36 | 036-figjam-design-system/ | Three-lineage research on board design quality and consistency and a user-editable design spec file | Complete |
| 37 | 037-figjam-design-spec/ | A user-editable design file inside sk-create-figjam, theme plumbing that falls back with a warning, the ranked fixes from 036 and the Project mirror | Complete |
| 38 | 038-figjam-model-comparison/ | The seven board-quality scenarios on DeepSeek V4.1 Flash max, SWE 2 Max and GLM 5.3 Flash max, graded on the scorecard, with the best board per type as the gallery, then the fixes for its six findings | Complete |
| 39 | 039-figjam-run-findings/ | The five skill findings and three driver findings of the stopped Opus 5.5 medium run, fixed in `sk-create-figjam` v1.0.5.0 and the run's driver | Complete |
| 40 | 040-figjam-sonnet-run-findings/ | The Sonnet 5.5 high run's findings, fixed in `sk-create-figjam` v1.0.6.0 with kernel v1.2.8, then a rerun of the 31 scenarios that did not pass and a v1.0.6.0 gallery | Complete |
| 41 | 041-figjam-rerun-findings/ | The 35 findings of the v1.0.6.0 rerun, fixed in `sk-create-figjam` v1.0.7.0, then a rerun of every scenario that did not pass | Complete |
| 42 | 042-figjam-glance-and-left-out/ | The gaps the v1.0.7.0 rerun still shows: glance plans that match the drawn board, a Left out line on every split and gate, the sticky fallback and the router spacing, then a rerun of the 14 failures | Complete |
| 43 | 043-figjam-rerun-followups/ | The gaps the v1.0.8.0 rerun still shows: a composite's inner states, the split title, a revision's second glance and title, the reply's first line, adjacent stickies and a missing-route gate, then a rerun of the 7 failures with two readers per board | Complete |
| 44 | 044-figjam-composite-and-path-order/ | The causes the v1.0.9.0 rerun still shows: the composer draws a composite across the top row, plans order a flow by fill while readers take its main row in path order and the revision exemption is too narrow, with a working node pinned for the label trace, then a rerun of the 6 failures | Complete |
| 45 | 045-figjam-findings-fixes/ | The causes the v1.0.10.0 rerun still shows, fixed with no rerun: plans that ignore the drawn state board and main row, two intake sentences that disagree, a boxed-in sticky with no place, a revision playback that reads nothing, a read-back that assumes connector labels and grading conventions the playbook never stated | Complete |
| 46 | 046-figjam-gate-and-accent-fixes/ | The v1.0.11.0 rerun findings: a gate that cannot see a noted node's sides, an accent on the goal the composer draws last, a gate without its sketch, a stop ending on a self-scan line, a missed lone word and an unwritten end-state reading, then a rerun of FJ-017, FJ-036, FJ-022 and FJ-023 | In Progress |

### Phase Transition Rules

- Each phase MUST pass `validate.sh` independently before the next phase begins
- Parent spec tracks aggregate progress via this map
- Use `/spec_kit:resume [parent-folder]/[NNN-phase]/` to resume a specific phase
- Run `validate.sh --recursive` on parent to validate all phases as integrated unit

### Phase Handoff Criteria

| From | To | Criteria | Verification |
|------|-----|----------|--------------|
| 001-research | 002 and 003 | Operator approved the later-phase list on 2026-10-20 | goal.md log |
| 002-write-route-spike | 005-flow-mode | Decision note names the route, both scratch boards read back | 002 acceptance criteria |
| 003-vendored-figma-and-sync | 004-parent-hub-conversion | vendor-sync.py status exits 0, gates green | 003 acceptance criteria |
| 004-parent-hub-conversion | 005-flow-mode | Fixture counts equal the baseline, hub check passes | 004 acceptance criteria |
| 005-flow-mode | 006 and 007 | End-to-end board reads back equal to the model | 005 acceptance criteria |
| 006 and 007 | 008-upstream-roundtrip-and-release | Plugin validates, Sync Loop gates exit 0 | 006 and 007 acceptance criteria |
| 005-flow-mode | 009-figjam-skill-research | Flow Mode sources exist to compare against | 005 acceptance criteria |
| 009-figjam-skill-research | 010-flow-mode-hardening | The operator chose which ranked changes to apply | 009 goal log |
| 010-flow-mode-hardening | 011-figjam-packet-split | Flow Mode hardened and its gates green | 010 acceptance criteria |
| 011-figjam-packet-split | 012-vendored-clickup | The hub carries a third packet and its check passes | 011 acceptance criteria |
| 012-vendored-clickup | 013-skilled-hub-alignment | The hub carries four packets and its check passes | 012 acceptance criteria |
| 013-skilled-hub-alignment | 014-hub-to-root | parent-skill-check reports 0 failures and every gate passes | 013 acceptance criteria |
| 014-hub-to-root | 015-figjam-rebuild | parent-skill-check on the repository root reports 0 failures and every gate passes | 014 acceptance criteria |
| 015-figjam-rebuild | 008-upstream-roundtrip-and-release | Every diagram type has a reference, a template and a checked example, and every gate passes | 015 acceptance criteria |
| 015-figjam-rebuild | 016-figjam-improvement-research | The rebuilt packet exists to compare against | 015 acceptance criteria |
| 016-figjam-improvement-research | 017-board-link-in-artifact | The operator adopted the ranked change | 016 goal log |
| 016-figjam-improvement-research | 018-artifact-plus-board-pair | The operator adopted the ranked change | 016 goal log |
| 016-figjam-improvement-research | 019-hosted-route-connection | The operator adopted the ranked change | 016 goal log |
| 016-figjam-improvement-research | 020-accent-and-cut-test | The operator adopted the ranked change | 016 goal log |
| 016-figjam-improvement-research | 021-board-critic-pass | The operator adopted the ranked change | 016 goal log |
| 016-figjam-improvement-research | 022-created-node-tags | The operator adopted the ranked change | 016 goal log |
| 016-figjam-improvement-research | 023-kernel-no-connector-sentence | The operator adopted the ranked change | 016 goal log |
| 016-figjam-improvement-research | 024-flow-delivery-pointers | The operator adopted the ranked change | 016 goal log |
| 016-figjam-improvement-research | 025-plan-whoami | The operator adopted the ranked change | 016 goal log |
| 016-figjam-improvement-research | 026-self-edit-guidance | The operator adopted the ranked change | 016 goal log |
| 016-figjam-improvement-research | 027-repeated-edge-labels | The operator adopted the ranked change | 016 goal log |
| 016-figjam-improvement-research | 028-readback-direction | The operator adopted the ranked change | 016 goal log |
| 016-figjam-improvement-research | 029-extension-fixes | The operator adopted all thirteen Section 9 findings | 016 goal log |
| 029-extension-fixes | 030-figjam-research-three | The operator asked for three more research runs | 030 spec |
| 030-figjam-research-three | 031-round-three-apply | The operator adopted all 32 ranked changes | 030 syntheses |
| 031-round-three-apply | 032-clickup-push-targets | The operator asked for local ClickUp push targets | 032 spec |
| 038-figjam-model-comparison | 039-figjam-run-findings | The operator chose to fix the stopped run's findings | 038 run README section 8.3 |
| 039-figjam-run-findings | 040-figjam-sonnet-run-findings | The operator chose to fix every finding group of the Sonnet 5.5 high run | 038 run README section 8.5 |
| 040-figjam-sonnet-run-findings | 041-figjam-rerun-findings | The operator chose to fix all 35 findings of the v1.0.6.0 rerun | 038 run README section 8.6 |
| 041-figjam-rerun-findings | 042-figjam-glance-and-left-out | The operator chose phase 042 to fix the remaining gaps and rerun the 14 failures | 038 run README section 8.7 |
| 042-figjam-glance-and-left-out | 043-figjam-rerun-followups | The operator chose phase 043 to fix the remaining gaps and rerun the 7 failures | 038 run README section 8.8 |
| 043-figjam-rerun-followups | 044-figjam-composite-and-path-order | The operator chose phase 044 to fix the composite placement and the path-order glance plan and rerun the 6 failures | 038 run README section 8.9 |
| 044-figjam-composite-and-path-order | 045-figjam-findings-fixes | The operator closed testing and chose phase 045 to fix the findings in the skills and sync them to the Claude Project | 038 run README section 8.10 |
| 045-figjam-findings-fixes | 046-figjam-gate-and-accent-fixes | The operator chose phase 046 under 017 to fix the v1.0.11.0 rerun findings and rerun the affected scenarios | 038 run README section 8.11 |
<!-- /ANCHOR:phase-map -->

---

<!-- ANCHOR:questions -->
## 4. OPEN QUESTIONS

- Which later phases does the synthesis name, and in what order?
- Does the plugin carry the figma skill or call the embedded copy?
<!-- /ANCHOR:questions -->

---

## RELATED DOCUMENTS

- **Phase children**: See sub-folders `[0-9][0-9][0-9]-*/` for per-phase spec.md, plan.md, tasks.md
- **Parent Spec**: See `../spec.md`
- **Graph Metadata**: See `graph-metadata.json` for `derived.last_active_child_id` pointer
