---
title: "Feature Specification: Phase 50: FigJam lessons from a hand-built spec board"
description: "A hand-built FigJam board of a two-party lifecycle showed five gaps in sk-create-figjam: a read-back screenshot that can show the board before the write, a subtitle that says little, no lane for a record's status, no card that carries a prompt's details and no worked example of that board shape. This phase closes each as v1.0.16.0 with the Claude Project in step."
trigger_phrases:
  - "figjam spec board learnings"
  - "phase 50 figjam"
  - "figjam status lane"
  - "figjam detail cards"
importance_tier: "normal"
contextType: "implementation"
---
<!-- SPECKIT_TEMPLATE_SOURCE: spec-core | v2.3 -->
# Feature Specification: Phase 50: FigJam lessons from a hand-built spec board

<!-- SPECKIT_LEVEL: 2 -->
---

<!-- ANCHOR:metadata -->
## 1. METADATA

| Field | Value |
|-------|-------|
| **Level** | 2 |
| **Priority** | P2 |
| **Status** | Complete |
| **Created** | 2026-10-29 |
| **Branch** | `main` |
| **Parent Spec** | ../spec.md |
| **Phase** | 50 of 50 |
| **Predecessor** | 049-figjam-reading-order-and-reply-lead |
| **Successor** | 051-figjam-gallery-rerun |
| **Handoff Criteria** | Every row in acceptance-criteria.md is Met |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:phase-context -->
## Phase Context

This is **Phase 50** of the Product Owner FigJam flow generation upgrade specification.

**Scope Boundary**: `sk-create-figjam` (its references, assets, composer, checker and playbook) and the hand-written Claude Project mirror. No other Product Owner packet changes.

**Dependencies**:
- `sk-create-figjam` v1.0.15.0 as phase 049 left it.
- The operator's review of a hand-built board on 2026-10-29, recorded as the decisions below.

**Deliverables**:
- The five changes D1 to D5, released as hub v1.0.17.0 and `sk-create-figjam` v1.0.16.0.
- The hand-written Project mirror in the same commit, with a dated SYNC note.
- One composed board of the new worked example, read back with a fresh screenshot.

**Changelog**:
- When this phase closes, refresh the matching file in ../changelog/ using the parent packet number plus this phase folder name.
<!-- /ANCHOR:phase-context -->

---

<!-- ANCHOR:problem -->
## 2. PROBLEM & PURPOSE

### Problem Statement
On 2026-10-29 the operator had a FigJam board drawn by hand, outside Flow Mode, from a set of product prompt docs and their screens: two parties moving one shared record through a series of statuses. The board took several sections, each with one swimlane for the status and one for each party, and cards that carry a prompt's button label, its numbered form steps and its options. Over eight rounds of review the operator asked for things `sk-create-figjam` cannot draw or does not check:

- A screenshot taken with `get_screenshot` right after a `use_figma` write showed the board before the write. The cards read white when the write had tinted them, and only `node.screenshot()` inside a `use_figma` call showed the change. Flow-mode step 10 reads a node's view with `get_screenshot`, so a read-back can pass or fail on a stale render.
- The operator called a section description that restated the board's scope low value and asked what starts the flow and what ends it. `assets/flow-templates.md` Section 1 asks the subtitle for who reads the board and why.
- The record's own status ran as a lane above the two actor lanes, each prompt that moved it joined to it by a dotted line. `references/types/process.md` has actor lanes only, so a status that changes hands has no place on a process board.
- Each card needed its prompt's details to be useful as a spec: the button label, the numbered steps and the options a person picks from. The user flow and process grammars hold a node to one line of 40 characters and 9 or 12 nodes, and notes go on through pins. The operator rejected neither limit for ordinary flows, but a spec board needs both.
- The operator asked for that board shape as a reusable asset, with nothing of the source product in it.

### Purpose
Make a read-back trust only a screenshot taken after the write, make the subtitle say where a flow starts and ends, give a laned process an optional status lane, give the highest detail level a card that carries a step's details, and ship one anonymized worked example of that board, in the skill and the Project alike.

### Decisions
Taken from the operator's answers of 2026-10-29.

- **D1**: Fresh read-back. A view of a node or a section taken after a write is evidence only when it was rendered after that write. Flow-mode step 10, Section 7 and the rubric read a node's view through `node.screenshot()` inside a `use_figma` call, or through `get_screenshot` only when that render shows the write's change. A view that matches the board before the write is reported as stale and taken again, never counted.
- **D2**: Subtitle names the start and the end. `%% subtitle:` stays one sentence, and it names where the flow starts and where it ends, with the reader where the brief names one. The flow templates, every shipped example's subtitle line and the mirrors follow.
- **D3**: Status lane. A laned process may declare one status lane, drawn first, holding the states of the record the process moves, in order and joined by the status line. A step whose move changes the status joins the state it reaches by a dotted connector the key names `Moves the status`. The status lane never counts as an actor lane, its states count toward the node budget and the checker holds the rules in Section 4.
- **D4**: Detail cards. At the highest detail level a step may carry a body under its label: a button label, numbered form steps and the options a person picks, as short lines. The label stays on one line and sizes the card's width, a spacer sits between the label and the body and the body takes its own type token. The budget at that level is set in plan.md and printed by the checker. Below that level nothing changes.
- **D5**: Anonymized worked example. The hand-built board becomes one new worked example and one new process template pattern: a two-party lifecycle with a status lane and detail cards, written for one of the shipped fictional brands. No name, prompt code, phase key, screen copy or deal from the source product appears in any committed file.
- **D6**: Release. Every change lands in the skill and its hand-written Project mirror in the same commit as hub v1.0.17.0 and `sk-create-figjam` v1.0.16.0, a patch step each. The kernel moves to v1.2.17 only when a kernel sentence changes.
<!-- /ANCHOR:problem -->

---

<!-- ANCHOR:scope -->
## 3. SCOPE

### In Scope
- Write the fresh read-back rule per D1 in flow-mode, the rubric and the hybrid workflow's read of an added note.
- Rewrite the subtitle rule and every shipped subtitle line per D2.
- Add the status lane to the process grammar, the composer, the checker, the design key and the process template per D3, with self-tests.
- Add the detail card body, its type token, its spacing and its budget at the highest detail level per D4, with self-tests and a design-check floor.
- Write the anonymized worked example and template pattern per D5, compose its board once and read it back under D1.
- Write the Project mirror and release per D6.

### Out of Scope
- Escalation timers, reminders, deadlines or any time-based rule. The source board carried none, and the operator ruled them out.
- Custom colours. The hand-built board ended on tints outside FigJam's pairs, and `assets/figjam-design.md` keeps every colour on FigJam's palette, so a softer look stays a hand edit.
- The user flow grammar, which keeps its four shapes, its 9-node budget and its 40-character labels.
- A rerun of the manual testing playbook beyond the scenarios this phase adds.

### Files to Change

| File Path | Change Type | Description |
|-----------|-------------|-------------|
| sk-create-figjam/references/flow-mode.md, references/quality-rubric.md, references/hybrid-workflow.md | Modify | The fresh read-back rule, the detail level and the new checks |
| sk-create-figjam/assets/flow-templates.md, assets/examples/*.md | Modify | The subtitle rule and every shipped subtitle line |
| sk-create-figjam/references/types/process.md, assets/templates/process.md | Modify | The status lane grammar, rules, read-back and template pattern |
| sk-create-figjam/assets/figjam-design.md, assets/compose-board.js, scripts/compose_board.py | Modify | The status line, the dotted status connector, the key entry, the detail body token and the card layout |
| sk-create-figjam/scripts/flow_check.py, scripts/figjam_checks/ | Modify | The status lane and detail card checks with their self-tests |
| sk-create-figjam/assets/examples/process-fernhouse-commission.md | Create | The anonymized worked example |
| sk-create-figjam/scripts/compose-trace.mjs, leaf-manifest.json | Modify | The trace stand-in's `setRangeLineHeight` and the hub's leaf list, which the new example joins |
| sk-create-figjam/manual-testing-playbook/ | Create, Modify | One scenario each for the status lane, the detail cards and the fresh read-back |
| claude project/knowledge/, claude project/Custom Instructions.md, SYNC.md, README.md | Modify | The mirror, the SYNC note and the release notes |
| claude project/README.md, ../z — Claude Project Sync Loop/systems.py and systems.cjs | Modify | The Project's file count and composer figures, and the new mirror pair, declared in the outer repository |
| changelog/, sk-create-figjam/changelog/, version files | Create, Modify | v1.0.17.0 and v1.0.16.0 |
<!-- /ANCHOR:scope -->

---

<!-- ANCHOR:requirements -->
## 4. REQUIREMENTS

### P0 - Blockers (MUST complete)

| ID | Requirement |
|----|-------------|
| REQ-001 | The composer self-test, the design check, the flow check self-test, pytest, the repository gates and the output format gate all exit 0 on the committed tree. |
| REQ-002 | The Sync Loop parity, residency and divergence checks print PASSED after the last commit. |
| REQ-003 | No committed file names the source product, its parties, its prompt codes, its phase keys, its screen copy or its deals, as the anonymity scan in plan.md shows. |

### P1 - Required (complete OR user-approved deferral)

| ID | Requirement |
|----|-------------|
| REQ-004 | Flow-mode step 10 and Section 7, the rubric and the hybrid workflow read a view only when it was rendered after the write, and report a stale one per D1. |
| REQ-005 | The subtitle rule names the start and the end, and every shipped example's subtitle line follows it per D2. |
| REQ-006 | A laned process may declare one status lane that the composer draws first with the status line, dotted `Moves the status` connectors and a key entry, and the checker holds its rules with self-tests per D3. |
| REQ-007 | At the highest detail level a step carries a body under a one-line label, with a spacer, a body type token held to a floor and the budget the checker prints per D4. |
| REQ-008 | One anonymized worked example and one template pattern show a two-party lifecycle with a status lane and detail cards, and its board is composed and read back per D5. |
| REQ-009 | The playbook holds one scenario each for the status lane, the detail cards and the fresh read-back. |
| REQ-010 | `sk-create-figjam` reads 1.0.16.0 and the hub 1.0.17.0 with changelogs, and the mirror and the SYNC note carry every change per D6. |

> Acceptance criteria for these requirements live in `acceptance-criteria.md`,
> which is the document that decides whether this packet may close.
<!-- /ANCHOR:requirements -->

---

<!-- ANCHOR:success-criteria -->
## 5. SUCCESS CRITERIA

- **SC-001**: A Flow Mode run can draw the hand-built board's shape, a status lane over two actor lanes with detail cards, from a model rather than by hand.
- **SC-002**: The skill and the Project state each changed rule in the same words, as the Sync Loop parity and divergence checks show.
- **SC-003**: A read-back never counts a view rendered before its write.
<!-- /ANCHOR:success-criteria -->

---

<!-- ANCHOR:risks -->
## 6. RISKS & DEPENDENCIES

| Type | Item | Impact | Mitigation |
|------|------|--------|------------|
| Risk | Detail cards turn every board into a wall of text | High | The body exists only at the highest detail level, the default level is unchanged and the checker prints the budget |
| Risk | The status lane adds crossings between the status states and the steps that move them | Med | The status lane is drawn first and the dotted connectors route as the lightest line, with a self-test on the example's shape |
| Risk | The worked example carries a trace of the source product | High | The anonymity scan in plan.md runs on every changed file before each commit |
| Dependency | The stale screenshot was seen once, on one board | Med | The rule asks for a render after the write, which holds whether or not the staleness repeats |
<!-- /ANCHOR:risks -->

---

<!-- ANCHOR:nfr -->
## L2: NON-FUNCTIONAL REQUIREMENTS

### Security
- **NFR-S01**: No board URL, Figma file key, plan name or email in any committed file. Product Owner is a public repository.
- **NFR-S02**: No name, prompt code, phase key, screen copy or deal from the source product in any committed file.
<!-- /ANCHOR:nfr -->

---

<!-- ANCHOR:edge-cases -->
## L2: EDGE CASES

### Data Boundaries
- A laned process with a status lane and one actor lane: the status lane does not count toward the 2 to 6 actor lanes, so a single actor lane fails as it does today.
- A step that changes the status twice on two paths: each path's move gets its own dotted connector.
- A detail card whose label alone is wider than the column: the label sizes the card and the column widens to fit.

### Error Scenarios
- A status lane declared at a detail level below the highest: it is drawn, because the status lane does not depend on detail cards.
- A body line over the body length the checker prints: the check names the line and fails.
- A view rendered before the write: the read-back reports it as stale, takes a fresh one and counts only that.
<!-- /ANCHOR:edge-cases -->

---

<!-- ANCHOR:complexity -->
## L2: COMPLEXITY ASSESSMENT

| Dimension | Score | Notes |
|-----------|-------|-------|
| Scope | 17/25 | About 35 files across the composer, the checker, references, templates, examples, the playbook and the mirror |
| Risk | 11/25 | Two new layout features in the composer and a new body token, each self-tested |
| Research | 4/20 | The needs come from one reviewed board, and the composer's layout has to be read before D3 and D4 are built |
| **Total** | **32/70** | **Level 2** |
<!-- /ANCHOR:complexity -->

---

<!-- ANCHOR:questions -->
## 10. OPEN QUESTIONS

- The detail level's node and body budget, proposed in plan.md, is the operator's to confirm before the checker enforces it.
- Which shipped fictional brand carries the worked example, proposed in plan.md.
<!-- /ANCHOR:questions -->
