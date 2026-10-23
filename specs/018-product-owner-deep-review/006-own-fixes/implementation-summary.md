---
title: "Implementation Summary"
description: "Every Product Owner finding from the five deep reviews fixed or recorded with its reason, the vendored ones fixed upstream."
trigger_phrases:
  - "own fixes implementation summary"
importance_tier: "normal"
contextType: "implementation"
_memory:
  continuity:
    packet_pointer: "018-product-owner-deep-review/006-own-fixes"
    last_updated_at: "2026-10-21T16:30:00Z"
    last_updated_by: "claude-code"
    recent_action: "Fixed the findings and reran every owning gate"
    next_safe_action: "The operator commits the Product Owner work"
    blockers: []
    key_files:
      - "sk-product-owner/SKILL.md"
      - "sk-product-owner/manual-testing-playbook/manual-testing-playbook.md"
      - "scripts/vendor-sync.py"
      - "scripts/build-plugin.py"
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
| **Spec Folder** | 006-own-fixes |
| **Status** | Complete |
| **Completed** | 2026-10-21 |
| **Level** | 2 |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:what-built -->
## What Was Built

The five reviews raised 68 findings. 65 are fixed, at the cited site or, for a vendored packet, in its upstream skill under Code_Environment `specs/mcp-tooling/023-vendored-copy-review-fixes`. 3 are recorded below as not fixed, each with its reason. DR-DS-004 was judged overstated in phase 001, and its wording was still tightened.

### Phase 001, sk-product-owner (15)

| ID | Outcome |
|----|---------|
| DR-DS-001 | Fixed. `references/quality-scoring.md` delivery lines now name the save and read-back, with the Deliverable Block as the Project alternative, and NEVER 9 says the same |
| DR-DS-002 | Fixed. `SKILL.md` names the shared cards where they really live |
| DR-DS-003 | Fixed. `SKILL.md` counts the 52 playbook scenarios |
| DR-DS-004 | Overstated, wording tightened. `references/router-contract.md` lines 17 and 24 now say the differential holds the copy equal, not that the file proves it |
| DR-DS-005 | Fixed. The `SKILL.md` ALWAYS row separates what the router lane loads from what is already in context |
| DR-DS-006 | Fixed. `references/routing.md` FALLBACK band states the Quick-energy Task fallback |
| DR-DS-007 | Fixed. Oracle paths are packet-relative, `../benchmark/router/` in `SKILL.md` and `../../benchmark/router/` in `references/` |
| DR-DS-008 | Fixed. The README example's reading map uses code spans for the files it does not ship, mirror included |
| DR-DS-009 | Fixed. `SKILL.md` names the three examples allowed over the word caps |
| DR-DS-010 | Fixed. `references/router-contract.md` drops its repeated Purpose |
| DR-DS-011 | Fixed. 22 "The kernel points here for X:" lead lines in `references/` now read "X:", while the Project mirrors keep theirs |
| DR-DS-012 | Fixed. `references/routing.md` carries the seven preamble fields |
| DR-DS-013 | Fixed. `SKILL.md` NEVER 17 and the kernel's NEVER 7 treat supplied source material as data |
| DR-DS-014 | Fixed. `SKILL.md` makes every `[description]` a lowercase slug of letters, digits and hyphens for every mode, the rule Doc already had |
| DR-DS-015 | Fixed. New scenarios `SDK-005` and `PDK-005` cover the Narrative overview, and the root playbook moves to 52 scenarios, sets of 26, 5 docs and 96 turns |

### Phase 002, sk-create-figjam (11)

| ID | Outcome |
|----|---------|
| R1-P1-001 | Fixed. `flowchart.py` holds a user flow to `BUDGET USER_FLOW (9, 12)`, with a 13-connector planted fixture |
| R1-P2-001 | Fixed. The way-in check no longer excuses the first declared node |
| R1-P2-002 | Fixed. The unused `ARROWS` table in `sequence.py` is gone |
| R1-P2-003 | Fixed. `state.py` and `references/types/state.md` say `TD` is another name for `TB`, mirror included |
| R2-P2-001 | Fixed. `flow-mode.md` Never invent opens with the data-not-instructions rule, `SKILL.md` gains NEVER 6, and diagnostics quote text with `!r` |
| R2-P2-002 | Fixed. The self-test fails a shipped model with no Mermaid block |
| R3-P2-001 | Fixed. `flow-mode.md` Loading Condition reads "ALWAYS on a Flow route" |
| R3-P2-002 | Fixed. `SKILL.md` names `../vendor.json` at the repository root |
| R4-P2-001 | Fixed. `README.md` section 3 points to `SKILL.md` section 3 in place of a second file map |
| R4-P2-002 | Fixed. The self-test checks `SKILL.md` DIAGRAM_TYPES against the dispatched names |
| R4-P2-003 | Not fixed. See Known Limitations |

### Phase 003, mcp-click-up and its hub handoff (16)

| ID | Outcome |
|----|---------|
| R1-P2-001 | Fixed. `vendor-sync.py status` reports a pin that differs from the upstream commit as drift |
| R1-P2-002 | Fixed. `pull` stages through `.pull-new` and `.pull-old` renames, so an interrupted pull keeps a whole copy |
| R1-P2-003 | Fixed. `build-plugin.py` hashes inside its refusal guard, and a self-test plants a symlink in a vendored packet |
| R2-P1-001 | Fixed upstream. `doctor.sh` searches upward for `.utcp_config.json` |
| R2-P2-001 | Fixed upstream. `INSTALL-GUIDE.md` warns about the token in shell history |
| R2-P2-002 | Not fixed. See Known Limitations |
| R3-P1-001 | Fixed. `AGENTS.md` offers ClickUp delivery only with the MCP, says `cupt` alone sends the plain description, and names `SKILL.md` Section 7 as owner |
| R3-P1-002 | Fixed. `SKILL.md` Section 7 makes the private doc two calls, `clickup_create_document` with `create_page: false`, then `clickup_create_document_page` with `content_format: "text/md"`, and the Project README says the same |
| R3-P2-001 | Fixed. `doc-mode.md` line 416 points to `../../mcp-click-up/SKILL.md` |
| R3-P2-002 | Fixed. `ROUTER.md` says a packet's `INSTALL-GUIDE.md` sits outside the leaf contract and loads from the packet's own `ROOT_RESOURCES` |
| R4-P1-001 | Fixed upstream. Every document now says `cupt add` creates a task through the plain `description` |
| R4-P2-001 | Fixed upstream. `INSTALL-GUIDE.md` states one version, 1.0.2.0 |
| R4-P2-002 | Fixed upstream. Run commands are packet-relative |
| R5-P2-001 | Fixed upstream. The `--json` list has one owner, `json-flag.md` |
| R5-P2-002 | Fixed. The handoff names its owner, as in R3-P1-001 |
| R5-P2-003 | Fixed upstream. The router's `RESOURCE_BASES` names only `references` |

### Phase 004, mcp-figma (17)

| ID | Outcome |
|----|---------|
| R1-P1-001 | Fixed upstream. The primitives are `create` subcommands in `tool-surface.md` and the catalog |
| R1-P1-002 | Fixed upstream. `_common.sh` probes `figma-cli --help` for the silships identity |
| R1-P1-003 | Fixed upstream. `connect-safe.sh` exits 2 on a non-TTY |
| R1-P1-004 | Fixed upstream. `doctor.sh` searches upward and checks the PID with `ps` |
| R1-P2-001 | Fixed upstream. The verbose test is `[ "$VERBOSE" = 1 ]` |
| R1-P2-002 | Fixed upstream. `INSTALL-GUIDE.md` is 1.0.1.0 with a history row |
| R1-P2-003 | Fixed. `vendor-sync.py` raises `SetupError` when the upstream commit is unreadable |
| R2-P1-001 | Fixed upstream. Extract takes a positional new path |
| R2-P2-001 | Partly fixed upstream. `install.sh` pins `REPO_REF` to a commit, and the `figma-developer-mcp` launch pin is not fixed, see Known Limitations |
| R2-P2-002 | Fixed upstream. `mcp-wiring.md` treats Figma text as untrusted data |
| R3-P1-001 | Fixed upstream. Seven depth-bound links became plain locations |
| R3-P2-001 | Fixed upstream. The playbook no longer pins a skill version |
| R3-P2-002 | Fixed upstream. Both pointers name Section 13 |
| R3-P2-003 | Fixed upstream. `INSTALL-GUIDE.md` says 11 sections |
| R4-P2-001 | Fixed upstream. The manual copies align on `@latest` |
| R4-P2-002 | Fixed upstream. A comment on the PID constant names the collision |
| R4-P2-003 | Fixed upstream. The Dev Mode sentence is scoped to Code Mode |

### Phase 005, whole repo (9)

| ID | Outcome |
|----|---------|
| R1-P2-001 | Fixed. `ROUTER.md` says no Product Owner gate runs that replay today |
| R1-P2-002 | Fixed. `ROUTER.md` gives the full `leaf-resource-contract.cjs` path |
| R2-P2-001 | Fixed. `SYNC.md` names kernel v1.2.2 and skill 1.2.1.0 |
| R2-P2-002 | Fixed. `README.md`, `benchmark/README.md` and the root playbook say 37 gold rows |
| R2-P2-003 | Fixed. `rule_parity.py` sets `min_pairs` 7 for the flow rule |
| R3-P1-001 | Fixed. `UNSHIPPED` adds `sk-create-figjam/manual-testing-playbook`, and the build drops from 376 to 323 files |
| R3-P2-001 | Fixed. The `build-plugin.py` docstring drops "and README" |
| R3-P2-002 | Fixed. `example_lint.py` adds `FIGJAM_EXAMPLES` and lints 56 files |
| R4-P2-001 | Fixed. `README.md` says 56 example files |

### Files Changed

| File | Action | Purpose |
|------|--------|---------|
| `sk-product-owner/SKILL.md`, `references/` (quality-scoring, routing, router-contract, doc-mode and the reworded lead lines), `assets/examples/doc/doc-example-readme.md` | Modified | Phase 001 and 003 findings |
| `sk-product-owner/manual-testing-playbook/` root, `skill-document-modes/narrative-status-overview.md`, `project-document-modes/narrative-status-overview.md` | Modified, Created | DR-DS-015 |
| `sk-create-figjam/` `SKILL.md`, `README.md`, `references/flow-mode.md`, `references/types/state.md`, `scripts/flow_check.py`, `scripts/figjam_checks/` | Modified | Phase 002 findings |
| `AGENTS.md`, `ROUTER.md`, `README.md`, `SYNC.md`, `benchmark/README.md`, `benchmark/grader/README.md` | Modified | Handoff owner, router contract, counts and versions |
| `scripts/vendor-sync.py`, `scripts/tests/test_vendor_sync.py`, `scripts/build-plugin.py`, `benchmark/gates/example_lint.py`, `benchmark/gates/rule_parity.py` | Modified | Tooling and gate findings |
| `claude project/Custom Instructions.md`, `claude project/README.md`, three `knowledge/` mirrors | Modified | Project mirrors of the changed sources |
| `claude-plugin/` | Rebuilt | 323 files |
<!-- /ANCHOR:what-built -->

---

<!-- ANCHOR:how-delivered -->
## How It Was Delivered

Each finding's cited line was reopened before its edit, and the exact replacements ran through an asserted edit helper that refuses a missing or repeated match. Vendored packets were never edited here. Their fixes went to the upstream skill and come back through `vendor-sync.py pull` in phase 007. The Project mirrors were compared by content because the whole of packet 017 is also uncommitted: the FigJam mirrors were regenerated and diffed, and each other changed source was set beside its mirror and changed only where a Project reader would see the difference. Nothing is committed.
<!-- /ANCHOR:how-delivered -->

---

<!-- ANCHOR:decisions -->
## Key Decisions

| Decision | Why |
|----------|-----|
| The untrusted-input rule goes to the end of the `SKILL.md` NEVER list as 17 | A first insertion numbered two items 13, and appending keeps every existing number that other documents may cite |
| The `[description]` slug rule lives once in `SKILL.md` | `SKILL.md` loads with every mode, so one rule covers task, bug, Story and Epic where three copies could drift |
| The Quality Scoring mirror keeps its Project wording | It already says the Deliverable Block is the delivery evidence, and copying the skill's save and read-back line would tell a Project something false |
| The slug, oracle-path and ALWAYS-row changes have no Project mirror | A Project saves no file, runs no oracle and has no router lane, so the lines mean nothing there |
| The narrative scenarios reuse the Loomlist sync thread | The same thread drafted for the newcomer, not the decider, tests the status discipline the Proposal scenario cannot |
<!-- /ANCHOR:decisions -->

---

<!-- ANCHOR:verification -->
## Verification

| Check | Result |
|-------|--------|
| `bash benchmark/gates/run_gates.sh` | 11 of 12 before the upstream commit, with vendor sync failing as designed. All 12 pass after the 007 pull |
| Format gate, `validate-output-format.cjs --system product-owner` | Passed across 70 source files, the same 38 advisories as the baseline |
| Playbook validator, both packages | PASS, 52 scenarios each, 0 violations. The 4 new warnings are the sandbox `context/` path class every scenario carries |
| `route_contract.py fixtures.json`, `differential.py`, `check_hub.py` | 141 of 141, 219 of 219, the hub and 37 gold rows |
| Both new prompts through `route_contract.route_request` | Turn 1 and Turn 2 route to DOC with no disambiguation |
| `flow_check.py --self-test`, `test_vendor_sync.py` | 156 of 156, 15 of 15 |
| `build-plugin.py` and `--self-test` | 323 files built, 9 self-test checks pass |
| Sync Loop in the scratch clone: `reference-parity.cjs`, `residency_check.py product-owner`, `validate_parity.py product-owner` | Identical, PASSED, and 1 finding: Quality Scoring review due, see Known Limitations |
<!-- /ANCHOR:verification -->

---

<!-- ANCHOR:limitations -->
## Known Limitations

1. **R4-P2-003 is not fixed.** `flow-mode.md` was not split. The kernel and the mirrors cite its sections, and no failure from its load cost has been measured, so a split would move citations for a cost nobody has shown.
2. **R2-P2-002 and the `figma-developer-mcp` half of R2-P2-001 are not fixed.** The launch arguments live in each repository's live `.utcp_config.json`, outside the packets, and both live files use unpinned or `@latest` arguments today.
3. **AC-004 closed through phase 007.** The vendor sync gate passed once the upstream fixes were committed and pulled.
4. **The Quality Scoring pair needs a review record after the commit.** `validate_parity.py` asks for a `reviewed_pairs` entry keyed to the source commit, and that commit does not exist yet. The mirror was read and already carries the Project form.
<!-- /ANCHOR:limitations -->
