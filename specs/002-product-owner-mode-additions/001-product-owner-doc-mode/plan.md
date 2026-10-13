---
title: "Implementation Plan: Product Owner Doc Mode"
description: "Implement Doc Mode as an intent independent from energy, backed by source classification, conflict gating, adaptive document shapes, and refinement-fidelity rules. Deliver the same contract through the Product Owner source skill, interactive flow, CLI guidance, exports, and Claude Project mirrors."
trigger_phrases:
  - "product owner doc mode implementation"
  - "doc mode routing plan"
  - "documentation source authority"
  - "claude package parity"
importance_tier: "high"
contextType: "general"
_memory:
  continuity:
    packet_pointer: "002-product-owner-mode-additions/001-product-owner-doc-mode"
    last_updated_at: "2026-07-14T15:54:08Z"
    last_updated_by: "codex"
    recent_action: "Completed the engineering-document and ClickUp-layout correction plan"
    next_safe_action: "Use the verified package for local Doc work or deploy the Claude mirrors"
---
<!-- SPECKIT_TEMPLATE_SOURCE: plan-core | v2.2 -->
# Implementation Plan: Product Owner Doc Mode

<!-- SPECKIT_LEVEL: 3 -->

---

<!-- ANCHOR:summary -->
## 1. SUMMARY

### Technical Context

| Aspect | Value |
|--------|-------|
| **System** | Instruction-routed Product Owner skill with Markdown references and assets |
| **Authoritative source** | `Product Owner/skill/` plus the bootstrap and sync contract |
| **Distribution surfaces** | Codex CLI instructions, exports, Claude Custom Instructions, and Project Knowledge mirrors |
| **State or storage** | Markdown files only; no application state or data migration |
| **Verification** | Command-routing fixtures, corpus-based document fixtures, structural diffs, hashes, stale-reference searches, and strict Spec Kit validation |

### Overview

Implementation adds `DOC` beside Task, Bug, and Interactive intent while moving `QUICK` to a separate energy axis. Doc-specific rules live in one reference and one adaptive-template asset; the router owns intent selection and resource loading, while Interactive Mode gathers missing purpose, audience, authority, and status in one consolidated question. The correction permits source-grounded engineering documents and makes the established ClickUp raw-Markdown grammar the default for new documents.

The release is compatibility-sensitive. Source skill changes land first, interactive and documentation surfaces follow, and the Claude package is rebuilt from those authoritative files before routing, fidelity, export, and parity verification.

### Simplest Viable Approach

- Extend the existing Markdown router; do not introduce a second dispatcher or executable parser.
- Define token-bounded command behavior and a written regression matrix in the Skill.
- Keep source classification and refinement protections inside Doc Mode instead of copying them into Task and Bug resources.
- Add four adaptive shapes to one asset rather than four independent modes.
- Treat the four shapes as reader-purpose structures that can carry product or engineering subject matter.
- Encode ClickUp layout as shared new-document primitives instead of duplicating formatting rules inside every shape.
- Continue the manual mirror contract in `Product Owner/SYNC.md` and prove it with byte equality plus sha256-16 checks.
<!-- /ANCHOR:summary -->

---

<!-- ANCHOR:quality-gates -->
## 2. QUALITY GATES

### Definition of Ready

| Gate | Required Evidence |
|------|-------------------|
| Scope | `spec.md` identifies in-scope Product Owner surfaces and explicitly excludes source-corpus edits |
| Routing | A matrix covers exact commands, token boundaries, natural-language signals, artifact framing, command collisions, and Quick order |
| Authority | Each fixture has a declared current, approved, proposal, retired, unknown, or mixed classification |
| Versions | The source and Claude filename transition matrix is fixed before edits begin |
| Rollback | Every changed or added Product Owner file has a restore or removal action |

### Definition of Done

| Gate | Passing Condition |
|------|-------------------|
| Behavior | `$doc`, `$d`, natural-language Doc requests, and `DOC + QUICK` route as specified |
| Compatibility | Existing Task, subtask, UI-refinement, Bug, Quick Task, and Quick Bug fixtures do not change artifact intent |
| Safety | Unknown authority and unresolved contradictions stop with one consolidated question |
| Fidelity | Refinement fixtures preserve protected headings, order, links, identifiers, tables, status copy, and untouched literals |
| Engineering documentation | Requests for API, architecture, schema, data-flow, code-behavior, operational, recommendation, or decision documents select Doc; source-backed facts remain distinct from explicitly proposed analysis or selection, and neither authorizes production mutation or false approval claims |
| ClickUp layout | Four raw-Markdown golden fixtures prove exact `* * *` dividers, `*   ` bullets, heading adjacency, adaptive spacer headings, and source-native refinement |
| Delivery | New and refined artifacts use the correct export filenames without modifying fixtures |
| Parity | Eleven Claude knowledge mirrors match source bytes, old versioned filenames are absent, and every manifest digest matches |
| Specification | Placeholder and strict Spec Kit validation complete with zero warnings and zero errors |

### AI Execution Protocol

#### Pre-Task Checklist

Before each implementation task, confirm the task ID, permitted file set, required source evidence, compatibility fixtures, and rollback action. Re-read the source file immediately before changing it because the worktree may contain user changes.

#### Execution Rules

1. Make the smallest change that satisfies the named requirement.
2. Do not edit any Barter, Notification, or Feed fixture.
3. Do not normalize identifiers, links, copy, markup, or versioned filenames incidentally.
4. Run the task-specific check before beginning a dependent task.
5. Stop rather than choosing authority when sources conflict without an explicit winner.

#### Status Reporting Format

Report `Task ID — state — files — verification — residual risk`. Use `complete` only when the named evidence exists.

#### Blocked Task Protocol

Record the conflicting evidence, affected requirements, and one decision needed. Continue only with independent tasks; do not infer product authority or broaden scope to remove the blocker.
<!-- /ANCHOR:quality-gates -->

---

<!-- ANCHOR:architecture -->
## 3. ARCHITECTURE

### Pattern

The design remains an instruction router with lazily loaded mode references and assets:

1. Normalize input and extract energy.
2. Detect explicit artifact commands with token boundaries.
3. Apply explicit-command collision and natural-language tie-break rules.
4. Select `TASK`, `BUG`, `DOC`, or `INTERACTIVE`.
5. Load only the resources required by that intent.
6. For Doc, classify sources and run the conflict gate before drafting.
7. Select a shape for a new document or use the existing document as the refinement baseline.
8. For new documents, apply the ClickUp grammar and adapt heading depth to the content topology; for refinements, retain source grammar unless normalization is explicit.
9. Validate factual status, fidelity, technical-evidence boundaries, and export naming before delivery.

### Key Components

| Component | Responsibility | Must Not Own |
|-----------|----------------|--------------|
| Product Owner bootstrap | Advertise commands, identity, boundaries, and resource map | Detailed Doc workflow |
| Skill router | Parse intent and energy, apply tie-breaks, choose resources and export contract | Shape-specific document prose |
| Doc Mode reference | Create/refine lifecycle, source classes, authority order, conflict gate, fidelity protections, quality checks | Task or Bug behavior |
| Doc Templates asset | Adaptive Guide, Catalog, behavior-reference, and Proposal structures plus ClickUp-native layout primitives | Routing, source authority, unlabelled current technical claims, production authority, or fabricated evidence |
| Interactive Mode | Gather one consolidated set of missing decisions | Silently select source authority |
| CLI guide and export protocol | Explain invocation, output location, and compatibility | Claude-only packaging details |
| Claude Custom Instructions | Compact equivalent kernel and lookup/attestation behavior | Divergent rules from the source Skill |
| Knowledge mirrors and manifest | Retrievable byte-for-byte resources and integrity evidence | Independent edits |

### Routing Data Flow

`request -> energy extraction -> explicit artifact commands -> natural-language artifact framing -> intent -> scoped resources -> source classification -> conflict gate -> create/refine -> shape/baseline -> ClickUp-new or source-native-refinement grammar -> fidelity and factuality checks -> export -> brief response`

### Source Decision Flow

Authority is evaluated in this order: explicit user designation, explicit labels in the source, repository placement, then corroborating evidence. Recency and duplication are never sufficient by themselves. A clearly authoritative claim can win within its stated scope while weaker material retains its source label; otherwise the workflow asks one consolidated clarification question and waits.

### Refinement Invariant

Outside the requested edit, the source filename, heading text and hierarchy, section order, link labels and URLs, reference definitions, identifiers, tables, status notices, proposal disclaimers, list markers, divider spelling and placement, spacer headings, formatting, and literal copy remain unchanged. Structural or style normalization is allowed only when the user explicitly includes it in scope.
<!-- /ANCHOR:architecture -->

---

<!-- ANCHOR:affected-surfaces -->
## FIX ADDENDUM: AFFECTED SURFACES

| Surface | Current Role | Planned Action | Verification |
|---------|--------------|----------------|--------------|
| `Product Owner/AGENTS.md` | CLI bootstrap and mode/resource map | Add Doc commands, resource loading, boundaries, and exports | Search mode table, resource paths, and export examples |
| `Product Owner/skill/SKILL.md` | Authoritative router at `0.2.0` | Add `DOC`, separate energy, exact parsing, tie-breaks, conflict/fidelity gates; bump `0.3.0` | Routing matrix and stale-version search |
| `skill/references/doc_mode.md` | Absent in baseline | Create, then correct source boundaries | Shape, source-class, conflict, source-grounded engineering, refinement, and boundary fixture checks |
| `skill/assets/doc_templates.md` | Absent in baseline | Create, then correct new-document grammar | Render four corpus-grounded shapes against ClickUp raw-Markdown golden fixtures |
| Interactive reference and asset | Task/Bug-only intake | Add Doc intake and response; bump `0.403` and `0.101` | Ambiguous and one-question fixtures |
| `Product Owner/README.md` | Stale user guide at `0.096` | Add Doc and correct touched stale claims; bump `0.097` | Command, version, filename, and export searches |
| `Product Owner/SYNC.md` | Manual source-to-Claude contract | Add new resources and final mirror inventory | Source/mirror mapping audit |
| Claude Custom Instructions | Task/Bug-only kernel at `0.1.0` | Add equivalent Doc kernel; bump `0.2.0` | Cross-surface behavior matrix |
| Claude README | Nine-file inventory with one stale digest | Publish eleven-file inventory and rebuilt manifest | File count, names, byte checks, digest checks |
| Claude knowledge directory | Versioned source mirrors | Replace changed mirrors, add two Doc mirrors, remove superseded names | Exact inventory and `cmp` checks |
| Task and Bug resources | Existing compatible behavior | Leave content and versions unchanged | Hash before/after and regression fixtures |
| Reference corpus | Read-only test evidence | Do not modify | Source file hashes and repository status before/after |

### Producer and Consumer Inventory

- Router producers: exact command table, natural-language signals, intent/energy variables, resource lookup, and export dispatch in `SKILL.md`.
- Consumers: `AGENTS.md`, Interactive Mode, CLI README, Custom Instructions, Claude README, knowledge mirrors, and smoke-test language.
- Version consumers: all source headers, version tables, mirror filenames, knowledge lookup strings, paired-version notes, and checksum rows.
- Source-safety consumers: Doc Mode, Doc Templates, Interactive clarification copy, CLI examples, Claude kernel, and corpus fixtures.

### Required Matrix Axes

- Artifact intent: Task, Bug, Doc, Interactive.
- Energy: Quick, standard, and deep/default behavior already supported by the Product Owner.
- Signal: exact command, false-prefix token, natural language, UI refinement, mixed artifact, and conflicting explicit commands.
- Operation: create or refine.
- Shape: Guide, Catalog, Product-behavior reference, Proposal/future state.
- Subject: product behavior, mixed product/technical behavior, or engineering system documentation.
- Layout policy: ClickUp-native new document, source-native refinement, or explicitly requested normalization.
- Source class: current, approved, proposal, retired, unknown, mixed, duplicated, or contradictory.
- Surface: CLI source, Claude kernel, and Claude knowledge lookup.
<!-- /ANCHOR:affected-surfaces -->

---

<!-- ANCHOR:phases -->
## 4. IMPLEMENTATION PHASES

### Phase 1: Establish Baselines and Fixtures

- Capture hashes and version strings for every in-scope Product Owner file and read-only corpus fixture.
- Record the final eleven-file Claude mirror inventory and old filenames that must disappear.
- Convert the specification success criteria into routing, shape, source-safety, fidelity, export, and parity fixture tables.
- Confirm the existing Task, Bug, DEPTH, task-template, bug-template, and HVR versions remain unchanged.

### Phase 2: Implement Router and Doc Resources

- Update `Product Owner/skill/SKILL.md` to `0.3.0`.
- Parse standalone `$doc` and `$d`, keep false prefixes inert, and separate Quick energy from artifact intent.
- Add deterministic command-collision and natural-language tie-break rules.
- Create `doc_mode.md` `0.100` with create/refine, authority, conflict, fidelity, boundary, validation, and export contracts.
- Create `doc_templates.md` with the four adaptive shapes, then correct it to use shared ClickUp-native layout primitives for new documents.
- Permit authoritative engineering facts plus explicitly labelled technical analysis, recommendations, and selections inside those shapes while keeping production mutation, unsupported live diagnosis, fabricated current facts, and false approval claims outside Doc authority.
- Run router and resource-scope fixtures before editing downstream packaging.

### Phase 3: Extend Interactive Intake and CLI Surfaces

- Update Interactive Mode to `0.403` and its response templates to `0.101`.
- Add one consolidated clarification form covering purpose, audience, source set, authority, current-versus-proposed status, scope, and constraints.
- Update `AGENTS.md` with Doc commands, resources, boundaries, and export behavior.
- Update `README.md` to `0.097`, correcting only stale claims required for an accurate Doc release.
- Update `SYNC.md` with the new source and mirror inventory while preserving manual-copy semantics.

### Phase 4: Synchronize Claude Packaging

- Update Custom Instructions to `0.2.0` aligned with Skill `0.3.0`.
- Replace the System Skill, Interactive Mode, and Interactive Response Templates mirrors with new versioned filenames.
- Add Doc Mode and Doc Templates mirrors at `0.100`.
- Retain the six unchanged mirrors and remove all superseded filenames.
- Update the Claude README inventory, paired versions, lookup phrases, smoke tests, and manifest.
- Recompute every changed sha256-16 from bytes, including the already stale Custom Instructions entry.

### Phase 5: Exercise Product and Engineering Documentation Workflows

- Render Barter creation material as a Guide without modifying the source.
- Render Notifications as a Catalog while retaining IDs, event names, variables, CTAs, draft markers, and unresolved conflicts.
- Render Feed behavior, geo-targeting, and dead-deal material as behavior references with contradictions visible.
- Render Weighted Ranking and Feed Functions as proposals with prominent future-state disclaimers.
- Route and render engineering requests for an API, architecture reference, data flow, code behavior, operational procedure, or technical recommendation without inventing current facts; keep authored choices explicitly proposed or recommended with their evidence and approval gaps visible.
- Compare raw output with Feed - Dead Deals, Feed Functions, How it Works, and Patterns golden fixtures for divider, bullet, heading, spacer, table, quote, fence, and repeated-entry grammar.
- Refine representative documents and compare all protected structure and literals outside the requested edit.
- Verify refinement retains non-ClickUp or legacy source grammar unless the request explicitly asks to normalize it.
- Verify unknown or conflicting authority produces one consolidated question rather than a blended artifact.

### Phase 6: Complete Regression and Release Gates

- Run Task, subtask, UI-refinement, Bug, Quick Task, and Quick Bug regression fixtures.
- Verify new and refined export filenames and confirm source fixtures are unchanged.
- Verify source/mirror equality, final inventory, stale versions, and every digest.
- Search all Product Owner surfaces for obsolete routing, filenames, versions, export examples, and Quick-as-mode wording.
- Run placeholder, link, and strict packet validation; record evidence in `implementation-summary.md`.
<!-- /ANCHOR:phases -->

---

<!-- ANCHOR:testing -->
## 5. TESTING STRATEGY

| Test Layer | Scope | Evidence |
|------------|-------|----------|
| Router table | `$doc`, `$d`, false prefixes, token order, task-about-docs, bug-about-docs, document-about-bugs, UI refinements, command collisions | Request -> intent + energy + resources table |
| Create workflow | Four shapes across the named corpus | Exported fixture plus classification ledger |
| Refinement workflow | Minimal requested edit against a structure-rich source | Protected-region diff and retained basename |
| Source safety | Active, approved, proposal, retired, unknown, mixed, duplicate, and contradictory material | Classification and conflict-gate assertions |
| Boundary | Requests to document technical systems or author a technical recommendation versus requests to mutate production, diagnose a live failure, or assert unsupported current behavior | Source-backed facts and explicitly proposed analysis or selection are allowed; production action, fabrication, and authority laundering remain prohibited |
| Engineering-document routing | “Document this API/architecture/data flow” and “recommend/select a direction in a proposal” versus “implement this change” or “debug this live failure” | Request -> intent plus source-status, proposal-label, approval-gap, and no-fabrication assertions |
| ClickUp golden layout | Dead Deals, Feed Functions, How it Works, and Patterns as exact raw-Markdown fixtures | Token, line-adjacency, heading-depth, spacer, table, quote, fence, and repeated-block assertions |
| Delivery | New and refined exports in CLI and Claude response forms | Path checks and source-fixture hashes |
| Compatibility | Existing Task/Bug and Quick fixtures | Before/after intent and template comparison |
| Packaging | Source-to-mirror parity, names, versions, and manifest | `cmp`, `find`/`rg`, and `shasum -a 256` |
| Specification | Packet completeness and template compliance | Placeholder check and strict validator output |

### Corpus Fixture Matrix

| Shape | Primary Fixture | Required Assertion |
|-------|-----------------|--------------------|
| Guide | Barter creation material | Preserve ordered anatomy, brand copy, rules, links, and any unresolved Story inconsistency |
| Catalog | Active Notification documents | Preserve stable IDs and event fields; do not reconcile index/account conflicts silently |
| Product-behavior reference | Feed How it Works, Geo Targeting, and Dead Deals | Distinguish present claims from unknown authority and expose incompatible decision rules |
| Proposal/future state | Weighted Ranking and Feed Functions | Display proposal status and prevent candidate scoring/fallback logic from becoming current fact |

### ClickUp Golden Fixture Matrix

| Fixture | Primary Shape Signal | Required Raw-Markdown Assertions |
|---------|----------------------|----------------------------------|
| Feed - Dead Deals | Behavior reference | Title then blank line and `* * *`; divider after every non-empty body heading; `*   **Term** — definition`; H3 glossary groups and H4 flow steps |
| Feed - Feed Functions | Proposal and repeated technical entries | Status quote enclosed by dividers; H1 chapters, H3 functions, H4 ruleset/algorithm blocks; adjacent Current/Future/Goal labels |
| Feed - How it Works | Engineering/business guide-reference | Scope quote enclosed by dividers; purpose-fit H2/H3/H4 hierarchy; ClickUp table separators; language-tagged fences and exact identifiers |
| Feed - Patterns | Pattern reference | H3 surfaces, H4 patterns and steps; bold module-label blocks separated by `* * *`; `*   ` outcome lists |

Golden comparison operates on raw Markdown, not rendered equivalence. Compact `***`, `---`, and `- ` lists fail a new-document golden case even when another Markdown renderer would display them similarly.

### Adversarial Cases

- `$debug`, `$docs`, `$document`, filenames containing `$d`, and prose mentioning those strings.
- `$quick $doc` and `$doc $quick` with identical remaining text.
- `$task --subtask` containing “document,” and two explicit artifact commands in either order.
- Byte-identical sources with no declared winner.
- A newer proposal that conflicts with an older explicitly canonical rule.
- A file that mixes existing, verify, new, source-export, draft, and not-ready labels.
- Refinement around the literal `complated_applications_count`, exact Feed URL names, malformed copy, and unmatched markup.
- An engineering-document request with authoritative technical sources, the same request without sources, a request for a labelled technical recommendation or selection record, and a request to implement the design in production.
- A generic Markdown draft using `---`, compact `***`, `- ` bullets, fixed H2-only structure, or indiscriminate empty spacer headings.
- A refinement whose source uses another established grammar, both with and without explicit normalization authorization.
<!-- /ANCHOR:testing -->

---

<!-- ANCHOR:dependencies -->
## 6. DEPENDENCIES

| Dependency | Type | Status | Impact if Blocked |
|------------|------|--------|-------------------|
| Product Owner Skill remains authoritative | Internal contract | Confirmed | Claude packaging cannot be reconciled safely if mirrors become independently edited |
| Manual sync workflow in `SYNC.md` | Internal process | Confirmed | Requires deliberate mirror replacement and byte verification |
| Source authority evidence | Product decision | Partially unknown by design | Conflicting fixtures must stop and ask; implementation itself can proceed |
| Corpus fixture paths | Test data | Confirmed for named scope | Shape and fidelity fixtures lose coverage if files move during implementation |
| Existing Task/Bug behavior | Compatibility baseline | Must be captured before edits | Regression cannot be assessed without before-state fixtures |
| Claude Project upload | External/manual | Outside local completion | Local package can be verified, but live upload and retrieval require a separate deployment action |
| Spec Kit validator | Repository tooling | Available | Packet release evidence depends on current strict validation |
<!-- /ANCHOR:dependencies -->

---

<!-- ANCHOR:rollback -->
## 7. ROLLBACK PLAN

### Triggers

- Any existing Task or Bug fixture changes intent or output contract.
- Quick energy causes a source-safety gate to be skipped.
- Claude mirrors cannot be made byte-identical to their authoritative sources.
- Source fixtures change during implementation.
- Unresolved conflicts are merged or proposals are stated as current behavior.
- Engineering-document support fabricates current technical behavior or evidence, hides proposal status, claims approval or sign-off without authority, diagnoses unsupported live behavior, or mutates production.
- A new ClickUp-targeted document fails the exact raw-Markdown golden grammar, or a refinement normalizes source style without authorization.

### Procedure

1. Stop packaging and retain failing evidence.
2. Revert only the Product Owner files changed for Doc Mode to their captured baseline.
3. Remove the two new Doc resources and their Claude mirrors.
4. Restore old versioned mirror filenames and the previous Claude README manifest.
5. Re-run Task/Bug routing and source-fixture hash checks.
6. Re-plan the failed phase without modifying the supplied corpus.

### Scope

Rollback is file-based. There are no data migrations, persistent state changes, dependencies, or runtime deployments in this packet.
<!-- /ANCHOR:rollback -->

---

<!-- ANCHOR:phase-deps -->
## L2: PHASE DEPENDENCIES

`Phase 1 baselines -> Phase 2 router/resources -> Phase 3 interactive/CLI -> Phase 4 Claude packaging -> Phase 5 document fixtures -> Phase 6 release gates`

| Phase | Depends On | Blocks |
|-------|------------|--------|
| 1. Baselines and fixtures | None | All later phases |
| 2. Router and Doc resources | Phase 1 | Interactive, packaging, workflow tests |
| 3. Interactive and CLI surfaces | Phase 2 | Claude packaging and end-to-end tests |
| 4. Claude packaging | Phases 2 and 3 | Parity and Claude smoke tests |
| 5. Documentation workflows | Phases 2 and 3; Phase 4 for Claude checks | Release gates |
| 6. Regression and release | Phases 1 through 5 | Completion |
<!-- /ANCHOR:phase-deps -->

---

<!-- ANCHOR:effort -->
## L2: EFFORT ESTIMATION

| Phase | Relative Size | Main Driver |
|-------|---------------|-------------|
| Baselines and fixtures | Medium | Broad source and version inventory |
| Router and Doc resources | High | Compatibility-sensitive intent split and new safety contract |
| Interactive and CLI surfaces | Medium | Coordinated copy and stale-guide cleanup |
| Claude packaging | Medium | Versioned replacements and digest accuracy |
| Documentation workflows | High | Mixed-authority corpus and fidelity assertions |
| Regression and release | Medium | Cross-surface parity and stale-reference searches |

No hour estimate is asserted; the corpus conflict decisions and current test harness depth are not yet measured.
<!-- /ANCHOR:effort -->

---

<!-- ANCHOR:enhanced-rollback -->
## L2: ENHANCED ROLLBACK

### Pre-Change Evidence

- Record hashes for in-scope source files, unchanged Task/Bug resources, all Claude mirrors, and read-only fixtures.
- Record the nine-file starting Claude inventory and every starting version string.
- Preserve the existing stale Custom Instructions digest as observed evidence, not as a target value.

### Component Reversal

| Component | Reversal |
|-----------|----------|
| Router and bootstrap | Restore captured source versions and routing text |
| New Doc resources | Remove source files and corresponding mirrors |
| Interactive resources | Restore `0.402` and `0.100` content and names |
| README and SYNC | Restore pre-release documentation |
| Claude kernel | Restore `0.1.0` and prior lookup inventory |
| Knowledge package | Restore previous filenames and manifest together |

### Verification After Reversal

- Task, subtask, UI-refinement, Bug, Quick Task, and Quick Bug fixtures match baseline.
- No Doc resource or command remains advertised.
- Corpus hashes match the pre-change record.
- Source and restored mirrors are internally consistent with the rolled-back manifest.
<!-- /ANCHOR:enhanced-rollback -->

---

<!-- ANCHOR:dependency-graph -->
## L3: DEPENDENCY GRAPH

`
Source audit and baselines
  +-> Skill router 0.3.0
  |     +-> Doc Mode 0.100
  |     +-> Doc Templates 0.100
  |     +-> Interactive Mode 0.403
  |     +-> Interactive Responses 0.101
  +-> CLI bootstrap, README 0.097, SYNC
        +-> Custom Instructions 0.2.0
        +-> Eleven knowledge mirrors
              +-> Manifest and stale-file cleanup
                    +-> End-to-end, parity, and regression gates
`

### Dependency Matrix

| Component | Depends On | Produces | Blocks |
|-----------|------------|----------|--------|
| Baseline fixture set | Source audit | Expected routes, hashes, versions | Every verification result |
| Skill router | Specification and baseline routes | Intent/energy/resource contract | Interactive and packaging |
| Doc Mode and Templates | Skill resource contract and corpus research | Create/refine behavior and shapes | Workflow fixtures |
| Interactive resources | Router ambiguity states | Consolidated intake | Ambiguous end-to-end tests |
| CLI surfaces | Final source behavior | User-facing invocation/export contract | Documentation parity |
| Claude kernel and mirrors | Final source files | Equivalent packaged behavior | Manifest and Claude tests |
| Release gates | All preceding outputs | Completion evidence | Release |
<!-- /ANCHOR:dependency-graph -->

---

<!-- ANCHOR:critical-path -->
## L3: CRITICAL PATH

1. Capture compatibility, version, and fixture baselines.
2. Implement orthogonal intent/energy routing and Doc resource loading.
3. Author Doc Mode and adaptive templates.
4. Extend Interactive intake and CLI surfaces.
5. Rebuild Claude kernel, mirrors, filenames, and manifest.
6. Pass workflow, engineering-routing, ClickUp-golden, fidelity, conflict, regression, export, and parity gates.

### Parallel Opportunities

- Doc Mode prose and Doc Templates can be authored in parallel after the router contract is fixed.
- README and SYNC updates can proceed alongside Interactive updates after source versions are chosen.
- Corpus fixture expectations can be expanded while Claude mirrors are rebuilt.

### Bottlenecks

- Router semantics block every downstream surface.
- Mirror packaging must wait for authoritative source files to stop changing.
- Final release cannot pass while any source authority conflict is silently resolved.
<!-- /ANCHOR:critical-path -->

---

<!-- ANCHOR:milestones -->
## L3: MILESTONES

| Milestone | Exit Criteria |
|-----------|---------------|
| M1 — Baseline locked | Routes, versions, file inventory, hashes, and corpus classifications recorded |
| M2 — Source behavior complete | Skill, Doc Mode, templates, Interactive resources, bootstrap, README, and SYNC agree |
| M3 — Claude package complete | Kernel and eleven mirrors use correct names, versions, bytes, and digests |
| M4 — Behavior verified | Four shapes, engineering routing, ClickUp golden layout, refinement, conflict, Quick, exports, and boundaries pass |
| M5 — Compatibility verified | Task/Bug regression, stale searches, source hashes, and strict validation pass |
<!-- /ANCHOR:milestones -->

---

## L3: ARCHITECTURE DECISION RECORD

- `ADR-001`: Use a dedicated Doc intent rather than extending Task Mode, preserving the distinction between backlog artifacts and product documentation.
- `ADR-002`: Use four adaptive shapes rather than one universal template; existing structure remains authoritative during refinement.
- `ADR-003`: Keep the supplied corpus read-only and require explicit source classification plus a conflict gate before synthesis.
- `ADR-004`: Use ClickUp-native grammar for new documents while keeping refinement source-native unless normalization is explicitly requested.
- `ADR-005`: Scope Amendment 002 to spec-touched files only and exempt ClickUp scaffold tables from the repository two-column documentation preference.

The full five-check analysis and consequences are in `decision-record.md`.

---

## L3: AMENDMENT 002 PLAN (POST-RELEASE REVIEW)

An independent post-release review of the shipped packet confirmed spec fidelity and surfaced four router-pseudocode refinements plus one naming inconsistency. No finding is a release blocker.

**Step 1: Router refinements (applied, T050).** In `Product Owner/skill/SKILL.md`: suggest the detected mode in the low-confidence Interactive branch; reduce `INTENT_MODEL` keywords to unweighted vocabulary and remove the unreachable documentation fallback chain, with prose recording that `SEMANTIC_TOPICS` owns scoring; restrict natural-language Quick to request-framing positions; match semantic synonyms on word boundaries. Re-sync the Skill mirror and its checksum.

**Step 2: Title normalization (T051).** Set the frontmatter `title:` and H1 of the four spec-touched sources to their knowledge-mirror basenames. Re-sync the four mirrors byte-identically and rebuild their sha256-16 entries in `claude project/README.md`. Pinned untouched sources (Task Mode, Bug Mode, DEPTH, HVR) are out of scope.

**Step 3: Independent verification (T052).** Re-extract the router pseudocode and run the full fixture suite, confirm 11/11 mirror parity and 12/12 digests, scan for stale internal titles, and re-check exports `020`/`021` against the ClickUp grammar.

**Step 4: Closure (T053, T054).** Record ADR-005 and close the amendment in `tasks.md` and `implementation-summary.md` with evidence.

**Rollback**: Restore the pre-amendment source files and mirrors from git and revert the four checksum rows; the amendment touches no protected source, corpus fixture, or export contract.

---

## L3: AMENDMENT 003 PLAN (EXTERNAL REVIEW TRIAGE)

An external review reported eleven findings. Triage against current bytes confirmed seven and rejected four (pseudocode stand-ins, the documented `NNN` runtime adaptation, a nonexistent spelling mix in export `021`, and the designed unverified-status prose pattern in export `020`).

**Step 1: Kernel contract.** Declare Skill `0.3.0` alignment in the `Custom Instructions.md` introduction and align its Quick-energy wording with framing-scoped detection.

**Step 2: Interactive state machine.** Unify the gate `evaluate`, clarification `expectedInputs`, and parser `doc_context` field vocabularies (adding `contradictions` and `preservation_scope` where missing) and give `comprehensive_question` an explicit next state and wait flag.

**Step 3: Template and router hardening.** Canonical source-class labels in both Doc Templates Source Basis blocks; single entry-level Status in the Catalog scaffold; `bug` and `repro` added to the bug topic synonyms; both semantic matchers use word-boundary regexes with plain inflection suffixes.

**Step 4: Smoke parity.** Add `$doc/path` to the Claude README rejected-prefix line.

**Step 5: Sync and verify.** Rebuild the four affected checksums, confirm 11/11 mirror parity and 12/12 digests, and rerun the routing fixture suite extended with bare-`bug`, inflection, and `fixture` non-boost cases.

**Rollback**: Restore the four edited sources, three mirrors, and checksum rows from git; no protected source, corpus fixture, or export is involved.

---

## L3: AMENDMENT 004 PLAN (SECOND-ROUND REVIEW)

A second independent review pass (`openai/gpt-5.6-sol-fast`, variant high, via `opencode run`) reported nine findings; all nine were reproduced against current bytes and accepted. Its release-blocking verdict was rejected as overweighted: the two DEPTH conflicts live in the deliberately pinned reference and the Claude kernel already behaved correctly on one of them.

**Step 1: Router fixes.** Broaden the Task tie-break from `task to document` to `task to/for/about/covering/on` while keeping independent multi-artifact requests conflicting, and veto natural Quick when the quick/fast phrase is negated.

**Step 2: DEPTH supersede clauses.** DEPTH stays pinned; SKILL.md gains two narrow overrides: Doc refinements never inject the DEPTH artifact-metadata header into preserved source (delivery metadata stays outside the document), and legacy wording letting `$quick` select Raw is superseded by the Quick D-P-H contract.

**Step 3: Kernel parity.** Add DEPTH to the Quick route's consulted resources and expand the conflict-question example to all five source classes.

**Step 4: Template and guide polish.** Full class labels in the two Behavior Reference status hints; dash-bullet intake grammar in the source-conflict hold; the user guide names the plain Checklist contract.

**Step 5: Sync and verify.** Rebuild three checksums, confirm 11/11 mirror parity and 12/12 digests, and rerun the fixture suite extended with task-for-docs, still-conflicting multi-artifact, and negated-quick cases.

**Rollback**: Restore SKILL.md, doc_templates.md, Custom Instructions.md, README.md, two mirrors, and three checksum rows from git; no pinned source, corpus fixture, or export is involved.
