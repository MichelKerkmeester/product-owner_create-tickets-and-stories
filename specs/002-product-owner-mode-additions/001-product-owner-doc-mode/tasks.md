---
title: "Tasks: Product Owner Doc Mode"
description: "Ordered implementation and verification tasks for the Product Owner Doc Mode release."
trigger_phrases:
  - "product owner doc mode tasks"
  - "doc mode implementation"
  - "doc mode verification"
importance_tier: "high"
contextType: "implementation"
_memory:
  continuity:
    packet_pointer: "002-product-owner-mode-additions/001-product-owner-doc-mode"
    last_updated_at: "2026-07-15T09:19:36Z"
    last_updated_by: "claude"
    recent_action: "Closed Amendment 004: fixed all nine second-round review findings (Task tie-break, negated-quick veto, DEPTH supersede clauses, kernel Quick/conflict parity, template and guide polish) and re-verified the full package"
    next_safe_action: "Upload the synchronized Claude package when deployment access is available"
---
<!-- SPECKIT_TEMPLATE_SOURCE: tasks-core | v2.2 -->
# Tasks: Product Owner Doc Mode

<!-- SPECKIT_LEVEL: 3 -->

---

<!-- ANCHOR:notation -->
## Task Notation

| Prefix | Meaning |
|--------|---------|
| `[ ]` | Pending |
| `[x]` | Completed with evidence |
| `[P]` | Parallelizable after its dependencies are satisfied |
| `[B]` | Blocked; do not infer a resolution |

**Task format**: `T### [P?] Description (file path)`

### AI Execution Protocol

#### Pre-Task Checklist

Before starting a task, read its linked requirements and dependencies, inspect the current file state, and confirm that any unrelated user changes can be preserved. Capture a baseline before touching a source fixture, versioned mirror, or checksum manifest.

#### Execution Rules

- Work in task-number order unless a task is marked `[P]` and all of its prerequisites are complete.
- Keep the Barter-deal, Notification, and Feed corpus read-only; use it only as verification input.
- Change only the Product Owner surfaces listed in `spec.md`. Engineering documentation is a supported Doc subject; technical analysis, recommendations, selections, and code examples may appear with explicit proposal status, but do not turn the work into production mutation, unsupported live diagnosis, fabricated current claims, or false approval.
- Keep the source skill and Claude package synchronized in the same implementation phase.
- Mark a task `[x]` only when its file, command, or test evidence is recorded.

#### Status Reporting Format

Report each transition as `T### — status — evidence — next task`. Separate authored changes from verification results, and never report the feature as implemented while a P0 task remains pending.

#### Blocked Task Protocol

Mark the task `[B]`, record the exact missing authority or conflicting evidence, and stop dependent work. Ask one consolidated question when the blocker is source purpose, audience, authority, or current-versus-proposed status.
<!-- /ANCHOR:notation -->

---

<!-- ANCHOR:phase-1 -->
## Phase 1: Setup

- [x] T001 Capture the current Product Owner source versions, Claude mirror filenames, and sha256-16 manifest as the release baseline. (`Product Owner/skill/`, `Product Owner/claude project/`) — baseline hashes and the stale Custom Instructions manifest value were captured before editing
- [x] T002 [P] Record the existing Task, subtask, UI-refinement, Bug, and Quick routing fixtures before adding Doc intent. (`Product Owner/skill/SKILL.md`, `Product Owner/skill/references/`) — twelve pre-change intent/energy fixtures were retained for regression comparison
- [x] T003 [P] Build a read-only fixture manifest for the eight Barter-deal documents, the active/concept/legacy Notification corpus, and the five named Feed documents. (`.opencode/specs/002-product-owner-mode-additions/001-product-owner-doc-mode/research.md`) — forty scoped file hashes were captured and preserved
- [x] T004 [P] Confirm the release version and mirror matrix, including superseded filenames that must be removed. (`.opencode/specs/002-product-owner-mode-additions/001-product-owner-doc-mode/spec.md`, `Product Owner/claude project/README.md`) — the pinned source and eleven-mirror matrix is published in both files
- [x] T005 Inspect the worktree and isolate this release from unrelated existing changes before editing Product Owner files. (`Product Owner/`) — pre-existing export and Feed changes were recorded and left untouched
<!-- /ANCHOR:phase-1 -->

---

<!-- ANCHOR:phase-2 -->
## Phase 2: Implementation

- [x] T010 Add Doc identity, exact commands, routed resources, clarification fields, and export behavior to the CLI bootstrap. (`Product Owner/AGENTS.md`) — bootstrap now carries the full Task/Bug/Doc/Interactive contract
- [x] T011 Bump the skill to `0.3.0` and implement token-bounded `$doc`/`$d` detection, orthogonal Quick energy, routing precedence, Doc resource loading, and Doc exports. (`Product Owner/skill/SKILL.md`) — executable pseudocode and routing fixtures pass
- [x] T012 Create Doc Mode `0.100` with separate create/refine flows, source classification, authority ordering, the conflict gate, fidelity rules, Product Owner boundaries, and one-question clarification behavior. (`Product Owner/skill/references/doc_mode.md`) — reference created and document validation passes
- [x] T013 [P] Create the `0.100` adaptive Guide, Catalog, Product-behavior reference, and Proposal or future-state structures without forcing a universal layout. (`Product Owner/skill/assets/doc_templates.md`) — four adaptive scaffolds and refinement overlay created
- [x] T014 Extend Interactive Mode to `0.403` so intake distinguishes Task, Bug, and Doc requests and gathers purpose, audience, sources, authority, and status in one prompt. (`Product Owner/skill/references/interactive_mode.md`) — state machine re-enters the Doc gate until READY
- [x] T015 [P] Extend Interactive Response Templates to `0.101` with a Doc choice and consolidated Doc clarification response. (`Product Owner/skill/assets/interactive_response_templates.md`) — conditional single-round intake added without changing Task/Bug blocks
- [x] T016 [P] Update the user guide to `0.097` with Doc Mode, corrected Task/Bug versions, current upload filenames, orthogonal Quick framing, and the two Doc export forms. (`Product Owner/README.md`) — guide and upload inventory now match the release
- [x] T017 [P] Add the Doc reference and asset to the manual synchronization contract while retaining source-skill authority. (`Product Owner/SYNC.md`) — exact eleven-file mapping and drift gates recorded
- [x] T018 Bump the Claude kernel to `0.2.0` and mirror Doc scope, routing, source safety, refinement fidelity, attestation, and artifact delivery. (`Product Owner/claude project/Custom Instructions.md`) — Project-compatible Doc contract synthesized
- [x] T019 Update Claude project setup, knowledge lookup, upload inventory, version pairing, smoke tests, and export-equivalent delivery guidance. (`Product Owner/claude project/README.md`) — setup and smoke matrix cover all routed cases
- [x] T020 Publish eleven current knowledge mirrors, add the two Doc mirrors, replace changed versioned mirrors, retain six unchanged byte-identical mirrors, and remove superseded filenames. (`Product Owner/claude project/knowledge/`) — eleven byte-identical mirrors present and three superseded names absent
- [x] T021 Recompute every affected sha256-16 entry from file bytes and correct the pre-existing Custom Instructions checksum mismatch. (`Product Owner/claude project/README.md`) — twelve final byte-derived digests pass
- [x] T022 Audit the completed edit set against the scope table and confirm Task Mode `0.301`, Bug Mode `0.201`, DEPTH `0.201`, Task Templates `0.100`, Bug Report Template `0.100`, and HVR `0.210` remain unchanged. (`Product Owner/skill/`) — all six protected source hashes match baseline
- [x] T023 Correct Doc Mode, Doc Templates, bootstrap guidance, user guidance, sync guidance, Claude instructions, mirrors, versions, and checksums so source-grounded engineering documents are supported and new documents use ClickUp-native grammar while refinements remain source-native unless normalization is explicit. (`Product Owner/`) — source and Claude contracts now allow engineering facts plus labelled analysis/recommendations, DEPTH and HVR conflicts have narrow Doc overrides, versions remain at their unreleased pins, 11/11 mirrors match, and 12/12 digests verify
<!-- /ANCHOR:phase-2 -->

---

<!-- ANCHOR:phase-3 -->
## Phase 3: Verification

- [x] T030 Verify standalone `$doc` and `$d` route to `DOC` while `$document`, `$docs`, `$debug`, embedded `$d` text, and ordinary substrings do not. (`Product Owner/skill/SKILL.md`) — token-boundary matrix passes punctuation and false-prefix cases
- [x] T031 [P] Verify explicit-command and natural-language precedence for task-about-documentation, bug-report-about-documentation, document-about-bug-behavior, UI refinement, ambiguous requests, and conflicting artifact commands. (`Product Owner/skill/SKILL.md`, `Product Owner/skill/references/interactive_mode.md`) — twenty-one final routing fixtures pass, including independent multi-artifact conflicts
- [x] T032 [P] Verify `$quick $doc` and `$doc $quick` both resolve to `DOC + QUICK` and that Quick cannot bypass authority, conflict, factuality, or status gates. (`Product Owner/skill/SKILL.md`, `Product Owner/skill/references/doc_mode.md`) — READY and six BLOCKED Doc-gate cases pass with Quick retained
- [x] T033 Exercise all four adaptive shapes: Barter creation as a Guide, Notifications as a Catalog, Feed/geo/dead-deal material as Product-behavior references, and Feed Functions/weighted ranking as Proposals. (`z — Context/Documentation/`) — nine named corpus fixtures pass the shape/status matrix
- [x] T034 [P] Verify proposal disclaimers remain prominent, retired Notification material remains historical, unknown claims are not promoted, and mixed-status sources retain claim-level classification. (`z — Context/Documentation/Notifications/`, `z — Context/Documentation/Feed/`) — proposal, retired and five-class assertions pass
- [x] T035 Verify every unresolved authority conflict produces one consolidated question and no draft, including Notification ID conflicts, duplicate Reminder files, missing canonical paths, geo ordering, Feed fallback, and dead-deal visibility. (`Product Owner/skill/references/doc_mode.md`) — conflict inventory is mapped to the non-bypassable gate and A2/A3 plus duplicate-source assertions pass
- [x] T036 Verify refinement preserves the source basename, heading hierarchy and order, links, URL labels, identifiers, tables, status notices, proposal disclaimers, formatting, and untouched literal copy byte-for-byte. (`Product Owner/skill/references/doc_mode.md`) — fidelity invariant and four literal-hazard assertions pass; corpus hashes remain unchanged
- [x] T037 [P] Verify new exports match `export/NNN - doc-[description].md`, refined exports retain the source basename, output exists before response, and no source fixture is overwritten. (`Product Owner/export/`) — both forms and export-before-response rules agree across CLI and Claude; user-requested test exports use the new-document form
- [x] T038 Run the pre-change Task, subtask, UI-refinement, Bug, and Quick Task/Bug matrix and confirm intent, resource, template, clarification, and export behavior is unchanged. (`Product Owner/skill/`) — twelve baseline fixtures preserve intent and energy; protected resources remain unchanged
- [x] T039 Compare the corpus manifest with the setup baseline and confirm the Barter-deal, Notification, and five named Feed fixtures were not changed by implementation or tests. (`z — Context/Documentation/`) — all forty sha256 values match
- [x] T040 Verify all eleven Claude knowledge mirrors are byte-identical to their source files, every sha256-16 matches, and no stale versioned mirror or stale version claim remains. (`Product Owner/claude project/`) — 11/11 mirrors, 12/12 digests and stale-name checks pass
- [x] T041 [P] Verify CLI and Claude parity for commands, routing, source classification, clarification, adaptive shapes, fidelity, exports, and completion attestation. (`Product Owner/AGENTS.md`, `Product Owner/claude project/Custom Instructions.md`) — synchronized-surface assertions and independent package audit pass
- [x] T042 Run placeholder checks and strict Spec Kit validation with zero warnings and zero errors, then record evidence without changing the feature status prematurely. (`.opencode/specs/002-product-owner-mode-additions/001-product-owner-doc-mode/`) — final placeholder and strict validation pass recorded in `implementation-summary.md`
- [x] T043 Verify engineering-document routing and safety boundaries, run exact raw-Markdown golden fixtures against Feed - Dead Deals, Feed Functions, How it Works, and Patterns, verify source-native refinement with and without explicit normalization, then rerun corpus hashes, mirror parity, checksums, placeholders, and strict Spec Kit validation. (`Product Owner/`, `z — Context/Documentation/Feed/`, `.opencode/specs/002-product-owner-mode-additions/001-product-owner-doc-mode/`) — five executable router blocks, 55 combined routing/precedence fixtures, READY/PENDING/six BLOCKED gates, four Feed goldens, four template scaffolds, 40/40 corpus hashes, 6/6 protected hashes, 11/11 mirrors, 12/12 digests, zero placeholders, and the final strict cycle pass
- [x] T044 Re-audit the pinned Claude kernel against the expanded source router, add generic modified-document, recommendation-to-document, and titled-refinement rules, extend the smoke matrix, and rebuild the kernel digest. (`Product Owner/claude project/`) — kernel `0.2.0` remains pinned to Skill `0.3.0`; 5/5 contract assertions, 13/13 smoke phrases, 11/11 mirrors, and 12/12 digests pass
- [x] T045 Create and verify two retained Doc Mode examples from the supplied Feed sources: an unverified behavior reference and an explicitly non-current engineering proposal. (`Product Owner/export/`) — exports `020` and `021` pass heading-divider adjacency, exact bullet and compact table-separator grammar, link, status, identifier, and proposal-weight checks without changing either source fixture
- [x] T046 Save final packet continuity and create a template-backed deployment handover. (`.opencode/specs/002-product-owner-mode-additions/001-product-owner-doc-mode/handover.md`) — direct Spec Kit save, canonical metadata refresh, handover placeholder scan, and strict packet validation pass
<!-- /ANCHOR:phase-3 -->

---

<!-- ANCHOR:phase-4 -->
## Phase 4: Amendment 002 - Post-Release Review Refinements

- [x] T050 Apply the four router-pseudocode refinements from the post-release review: detected-mode low-confidence suggestion, unweighted `INTENT_MODEL` vocabulary with the unreachable documentation fallback chain removed, framing-scoped natural-language Quick, and word-boundary synonym scoring; then re-sync the Skill mirror and checksum. (`Product Owner/skill/SKILL.md`, `Product Owner/claude project/`) — 23 routing fixtures pass from the extracted pseudocode, including the Doc gate PENDING/BLOCKED/READY cycle and the new low-confidence and subject-matter-"fast" behaviors; Skill sha16 rebuilt to `2d3ba686d2a20a14` with 11/11 mirrors and 12/12 digests verified
- [x] T051 Normalize the frontmatter `title:` and H1 of the four spec-touched sources to their knowledge-mirror basenames, re-sync those four mirrors byte-identically, and rebuild their sha256-16 entries. (`Product Owner/skill/references/doc_mode.md`, `Product Owner/skill/references/interactive_mode.md`, `Product Owner/skill/assets/doc_templates.md`, `Product Owner/skill/assets/interactive_response_templates.md`, `Product Owner/claude project/`) — four titles normalized to their mirror basenames, four mirrors resynced byte-identically, four sha16 rows rebuilt, and a repo-wide sweep found no stale cross-references
- [x] T052 Independently verify the amendment: rerun the routing fixture suite from freshly extracted pseudocode, confirm 11/11 mirror parity and 12/12 digests, scan for stale internal titles outside `z_legacy`/`z_archive`, and re-check exports `020` and `021` against the ClickUp grammar. (`Product Owner/`) — fixture suite green (0 failures), 11/11 mirrors and 12/12 digests verified, zero stale titles found, export `020`/`021` grammar intact, and all protected files confirmed untouched
- [x] T053 Record the amendment scope decision: spec-touched files only, pinned sources untouched, and ClickUp scaffold tables exempt from the repository two-column documentation preference. (`.opencode/specs/002-product-owner-mode-additions/001-product-owner-doc-mode/decision-record.md`) — ADR-005 recorded with five-check evaluation
- [x] T054 Close the amendment: mark T051 and T052 with evidence, append the Amendment 002 addendum to `implementation-summary.md`, and refresh packet continuity metadata. (`.opencode/specs/002-product-owner-mode-additions/001-product-owner-doc-mode/`) — T051/T052 marked complete with evidence, Amendment 002 section appended to `implementation-summary.md`, and continuity metadata refreshed in both files
<!-- /ANCHOR:phase-4 -->

---

<!-- ANCHOR:phase-5 -->
## Phase 5: Amendment 003 - External Review Triage

- [x] T060 Triage the eleven external-review findings against current bytes: confirm seven, reject four with evidence. (`.opencode/specs/002-product-owner-mode-additions/001-product-owner-doc-mode/implementation-summary.md`) — rejections recorded: pseudocode stand-ins, documented `NNN` runtime adaptation, nonexistent export `021` spelling mix, designed export `020` status pattern
- [x] T061 Apply the seven confirmed fixes as one synchronized change set: kernel `0.3.0` alignment declaration plus framing-scoped Quick wording, unified Interactive Doc-context field vocabulary plus `comprehensive_question` next state, canonical Doc Templates source-class labels plus single Catalog Status, `bug`/`repro` synonyms plus inflection-tolerant word-boundary matching in both semantic matchers, and the `$doc/path` smoke-matrix entry. (`Product Owner/claude project/Custom Instructions.md`, `Product Owner/skill/references/interactive_mode.md`, `Product Owner/skill/assets/doc_templates.md`, `Product Owner/skill/SKILL.md`, `Product Owner/claude project/README.md`) — all edits applied; three mirrors re-synced; four checksums rebuilt (`fcce89f2efedd5ad`, `7af68dc2ab7fc96b`, `4d3ca00d76b939ea`, `d1194b9165cd0e73`)
- [x] T062 Verify the amendment: rerun the routing fixture suite extended with bare-`bug` LOW-band, three-synonym MEDIUM, inflection, and `fixture` non-boost cases, then confirm mirror parity, digests, and stale-hash purge. (`Product Owner/`) — 25 fixtures pass with 0 failures; 11/11 mirrors byte-identical; 12/12 digests match; zero stale hashes outside archives
<!-- /ANCHOR:phase-5 -->

---

<!-- ANCHOR:phase-6 -->
## Phase 6: Amendment 004 - Second-Round Review

- [x] T070 Dispatch an independent second-round review through `opencode run` with `openai/gpt-5.6-sol-fast` variant high, then reproduce every reported finding against current bytes before accepting it. (`Product Owner/`) — nine of nine findings reproduced (two routing defects confirmed via the extracted-pseudocode harness); the reviewer's release-blocking verdict was rejected as overweighting conflicts inside the deliberately pinned DEPTH reference
- [x] T071 Apply the nine accepted fixes: broadened Task tie-break with preserved multi-artifact conflict, negated-quick veto, two narrow DEPTH supersede clauses in SKILL.md, kernel Quick-route DEPTH loading and five-class conflict question, full class labels in Behavior Reference status hints, dash-bullet intake grammar in the source-conflict hold, and accurate Checklist naming in the user guide. (`Product Owner/skill/SKILL.md`, `Product Owner/skill/assets/doc_templates.md`, `Product Owner/claude project/Custom Instructions.md`, `Product Owner/README.md`) — two mirrors re-synced; three checksums rebuilt (`1d72e98cc018bcfc`, `593bb88ce07d09a1`, `d6e6b0cb1ae9a3c3`)
- [x] T072 Verify the amendment: rerun the fixture suite extended with task-for-docs, task-covering-docs, still-conflicting multi-artifact, and two negated-quick cases, then confirm mirror parity, digests, and residual-pattern purge. (`Product Owner/`) — 31 fixture checks pass with 0 failures; 11/11 mirrors byte-identical; 12/12 digests match; zero stale hashes or residual abbreviated labels
- [ ] T073 Run a cross-model identity smoke test: three separate `opencode run` dispatches of `openai/gpt-5.6-luna` variant high, each bootstrapping through AGENTS.md, adopting the Product Owner identity, and creating one Doc Mode test artifact from FICTIONAL user-supplied context with the Barter corpus explicitly off limits. (`Product Owner/export/`) — first corpus-based attempt (Barter deals guide, Notifications vocabulary catalog, Geo Targeting reference) passed all ClickUp grammar checks but was withdrawn by operator direction in favor of fictional subjects; redo targets exports `028` (Ladle onboarding copy guide), `029` (Curbly webhook event catalog), `030` (Brewloop points-expiry behavior reference)
<!-- /ANCHOR:phase-6 -->

---

<!-- ANCHOR:completion -->
## Completion Criteria

- [x] Every P0 requirement in `spec.md`, including the engineering-document and ClickUp-layout correction, has test evidence.
- [x] All tasks are marked `[x]` and no `[B]` task remains.
- [x] The routing, engineering-boundary, ClickUp-golden, shape, source-safety, conflict, fidelity, export, mirror-parity, and Task/Bug regression matrices pass.
- [x] Reference-fixture hashes match the Phase 1 baseline.
- [x] Placeholder checks and strict Spec Kit validation complete with zero warnings and zero errors after the correction and generated metadata refresh.
- [x] `implementation-summary.md` is changed from “Not implemented — specification only” only after the implementation and verification evidence exists.
<!-- /ANCHOR:completion -->

---

<!-- ANCHOR:cross-refs -->
## Cross-References

- **Specification**: [spec.md](./spec.md)
- **Implementation plan**: [plan.md](./plan.md)
- **Verification checklist**: [checklist.md](./checklist.md)
- **Decisions**: [decision-record.md](./decision-record.md)
- **Research evidence**: [research.md](./research.md)
- **Implementation status**: [implementation-summary.md](./implementation-summary.md)
<!-- /ANCHOR:cross-refs -->
