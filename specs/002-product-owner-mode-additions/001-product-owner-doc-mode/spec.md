---
title: "Feature Specification: Product Owner Doc Mode"
description: "Define a dedicated Product Owner mode for creating and refining trustworthy product and engineering documentation without weakening Task or Bug behavior. The mode separates document intent from energy, classifies source authority, blocks silent conflict merging, preserves source structure, applies ClickUp-native layout to new documents, and ships consistently across CLI and Claude packaging."
trigger_phrases:
  - "product owner doc mode"
  - "document how this works"
  - "product documentation routing"
  - "source authority conflict gate"
  - "documentation refinement fidelity"
importance_tier: "high"
contextType: "general"
status: "complete"
_memory:
  continuity:
    packet_pointer: "002-product-owner-mode-additions/001-product-owner-doc-mode"
    last_updated_at: "2026-07-14T15:54:08Z"
    last_updated_by: "codex"
    recent_action: "Implemented and verified the engineering-document and ClickUp-layout correction"
    next_safe_action: "Upload the synchronized Claude package when deployment access is available"
---
<!-- SPECKIT_TEMPLATE_SOURCE: spec-core + level2-verify + level3-arch | v2.2 -->
# Feature Specification: Product Owner Doc Mode

<!-- SPECKIT_LEVEL: 3 -->

---

## EXECUTIVE SUMMARY

Before this release, Product Owner routed requests only to Task, Bug, Quick, or Interactive behavior. It could not create or safely refine product documentation, and its Quick branch would have erased a future Doc intent because energy and artifact type were coupled.

Doc Mode adds a dedicated documentation intent for new guides, catalogs, behavior references, and proposals across product and engineering subject matter. It treats Quick as an energy override, classifies every source claim by authority, stops on unresolved contradictions, uses ClickUp-native Markdown grammar for new documents, preserves existing document structure during refinement, and keeps the CLI and Claude package in parity.

**Key Decisions**: add a dedicated Doc intent rather than extending Task Mode; use four adaptive shapes rather than one rigid document template; treat supplied corpus files as read-only fixtures and classify authority below file level when needed.

**Critical Dependencies**: the existing Product Owner source-to-Claude sync contract, exact preservation of Task and Bug routing, and explicit source evidence for any claim presented as current behavior.

---
<!-- ANCHOR:metadata -->
## 1. METADATA

| Field | Value |
|-------|-------|
| **Level** | 3 |
| **Priority** | P1 |
| **Status** | Complete |
| **Created** | 2026-07-14 |
| **Packet** | `002-product-owner-mode-additions/001-product-owner-doc-mode` |
| **Implementation target** | `Product Owner/` skill, CLI bootstrap, user guide, exports, and Claude packaging |
| **Specification scope** | Product and source-grounded engineering documentation; scoped Product Owner surfaces may change and supplied corpus fixtures remain read-only |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:problem -->
## 2. PROBLEM & PURPOSE

### Problem Statement

Before this release, the Product Owner system had no documentation artifact type. Natural-language requests such as “document how this works” fell into Task or Interactive handling, `$doc` and `$d` were unknown, and `$quick` acted as a mode that could resolve only to Task or Bug. A Doc request would therefore have been routed inconsistently or lost its intent.

The reference corpus also proves that product documentation cannot be synthesized safely from path or recency alone. Active-looking files contain draft, proposed, unverified, duplicated, retired, and contradictory claims. The pre-release source-preservation rule protected task headings and references, but not document tables, links, identifiers, status notices, or untouched literal copy.

### Purpose

Enable the Product Owner to create and refine product and engineering documentation grounded in supplied evidence. Doc Mode may explain WHAT, WHY, verified behavior, architecture, interfaces, schemas, data flows, operational procedures, and implementation facts when authoritative sources establish them. When requested, it may also analyze, recommend, or select a technical direction in a clearly labelled proposal, recommendation, or decision record; it must not fabricate current facts or present an authored direction as approved or shipped without authority.
<!-- /ANCHOR:problem -->

---

<!-- ANCHOR:scope -->
## 3. SCOPE

### In Scope

- Add a `DOC` intent with exact, token-bounded `$doc` and `$d` commands plus natural-language documentation signals.
- Separate intent (`TASK`, `BUG`, `DOC`, `INTERACTIVE`) from energy (`QUICK`, `STANDARD`, `DEEP`).
- Define deterministic tie-breaks for task-about-documentation, bug-report, Doc, UI-refinement, conflicting-command, and ambiguous requests.
- Add create and refinement workflows for Guide, Catalog, Product-behavior reference, and Proposal or future-state documents.
- Support engineering documents through the same four reader-purpose shapes when their technical facts are grounded in authoritative sources.
- Classify source material as current behavior, approved direction, proposal, retired material, or unknown at the claim or section level when necessary.
- Add a conflict gate that prevents contradictory or authority-ambiguous sources from being merged silently.
- Preserve filenames, heading hierarchy and order, links, identifiers, tables, status notices, proposal disclaimers, formatting, and untouched literal copy during refinement.
- Use ClickUp-native Markdown for new documents: raw `* * *` dividers, `*   ` unordered bullets, divider-backed real headings, purpose-fit heading depth, and same-level empty spacer headings only between substantial sibling sections.
- Preserve a source document's existing list markers, divider spelling, heading/spacer scheme, and table syntax during refinement unless the user explicitly requests normalization or structural rewriting.
- Extend Interactive Mode intake to gather document purpose, audience, source authority, and current-versus-proposed status in one consolidated question.
- Extend CLI export behavior, the user guide, Claude Project instructions, Project Knowledge mirrors, versioned filenames, and the checksum manifest.
- Pin the Product Owner skill to `0.3.0`, new Doc resources to `0.100`, Interactive Mode to `0.403`, and Interactive Response Templates to `0.101`.
- Verify routing, fidelity, source safety, exports, mirror parity, stale-version cleanup, and existing Task/Bug behavior.

### Out of Scope

- Editing Product Owner files outside the implementation table or broadening the release beyond documentation behavior.
- Editing the Barter-deal, Notification, or Feed reference corpus; these are read-only fixtures.
- Treating a Doc artifact as authorization to modify or execute a production system, perform unsupported live diagnosis, fabricate current behavior, root causes, operational evidence, implementation facts, or procedures, or present an authored technical, legal, compliance, or security recommendation as externally approved or professionally signed off.
- Resolving the corpus contradictions documented in `research.md`; Doc Mode must surface them to the user.
- Changing Task Mode `0.301`, Bug Mode `0.201`, DEPTH `0.201`, Task Templates `0.100`, Bug Report Template `0.100`, or HVR `0.210`.
- Updating the separate repository-level `ARCHITECTURE.md`; its task/bug-only description is a follow-up outside this packet.
- Converting this packet into a phased parent; the implementation is one coordinated compatibility-sensitive release.

### Files to Change During Implementation

| File Path | Change Type | Description |
|-----------|-------------|-------------|
| `Product Owner/AGENTS.md` | Modify | Add Doc identity, commands, routed resources, export rules, and clarification fields |
| `Product Owner/skill/SKILL.md` | Modify | Bump to `0.3.0`; add exact command parsing, orthogonal energy, `DOC`, tie-breaks, conflict/fidelity gates, and Doc exports |
| `Product Owner/skill/references/doc_mode.md` | Create and correct | Add Doc create/refine workflow, source-authority rules, source-safe engineering support, shapes, quality gates, boundaries, and exports |
| `Product Owner/skill/assets/doc_templates.md` | Create and correct | Add adaptive Guide, Catalog, behavior-reference, and Proposal scaffolds with ClickUp-native new-document grammar |
| `Product Owner/skill/references/interactive_mode.md` | Modify | Bump `0.402` to `0.403`; add Doc states, parsing, and authority/status intake |
| `Product Owner/skill/assets/interactive_response_templates.md` | Modify | Bump `0.100` to `0.101`; add Doc choice and one consolidated Doc clarification template |
| `Product Owner/README.md` | Modify | Bump user guide `0.096` to `0.097`; document Doc Mode and correct stale versions, filenames, Quick framing, and export syntax |
| `Product Owner/SYNC.md` | Modify | Add Doc resources to manual-load and mirror guidance without changing the manual-copy contract |
| `Product Owner/claude project/Custom Instructions.md` | Modify | Bump kernel `0.1.0` to `0.2.0`; mirror Doc scope, routing, fidelity, conflict, attestation, and delivery behavior |
| `Product Owner/claude project/README.md` | Modify | Update upload inventory, paired versions, smoke tests, filenames, and sha256-16 manifest |
| `Product Owner/claude project/knowledge/` | Add/replace/remove mirrors | Publish eleven current mirrors, remove superseded versioned names, and keep unchanged mirrors byte-identical |
<!-- /ANCHOR:scope -->

---

<!-- ANCHOR:requirements -->
## 4. REQUIREMENTS

### P0 - Blockers

| ID | Requirement | Acceptance Criteria |
|----|-------------|---------------------|
| REQ-001 | Add `DOC` as a first-class Product Owner intent. | Exact standalone `$doc` and `$d` tokens and clear natural-language documentation requests select Doc Mode. |
| REQ-002 | Parse commands with token boundaries. | `$document`, `$docs`, `$debug`, identifiers containing `$d`, and ordinary text substrings do not activate Doc Mode. |
| REQ-003 | Separate intent from energy. | `$quick` and `$q` set `QUICK` energy only; `$quick $doc …` and `$doc $quick …` both resolve to `DOC + QUICK`. |
| REQ-004 | Preserve deterministic routing precedence. | `$task --subtask` is checked before `$task`; one explicit artifact command wins over natural language; conflicting artifact commands enter one-question clarification. |
| REQ-005 | Keep artifact framing stronger than subject nouns. | “Create a task to document X” is Task, “write a bug report about documentation” is Bug, “document bug behavior” is Doc, and “document X” is Doc. |
| REQ-006 | Provide separate new-document and refinement workflows. | New documents select an adaptive shape; refinements use the existing file as the structural baseline and change only requested material. |
| REQ-007 | Support four adaptive document shapes. | Guide, Catalog, Product-behavior reference, and Proposal or future-state output each use purpose-fit sections without forcing one universal layout; shape follows reader need rather than a product-versus-engineering subject split. |
| REQ-008 | Classify source authority before synthesis. | Each material claim is classified as current behavior, approved direction, proposal, retired material, or unknown; mixed files can carry multiple classifications. |
| REQ-009 | Enforce a contradiction and authority conflict gate. | Conflicting claims are never blended; unresolved authority, duplication, missing canonical sources, or current-versus-proposed ambiguity produces one consolidated question and waits. |
| REQ-010 | Preserve refinement fidelity. | Filename, heading text/hierarchy/order, links, labels, URLs, identifiers, tables, status notices, proposal disclaimers, list markers, divider spelling and placement, spacer headings, formatting, and untouched literal copy remain unchanged unless explicitly in scope; normalization requires explicit authorization. |
| REQ-011 | Keep Doc Mode source-safe across product and engineering documentation. | Output may explain source-established architecture, interfaces, schemas, data flows, operational procedures, code behavior, and implementation facts. It may author code examples, technical analysis, options, recommendations, or selections when the document calls for them, but new material remains explicitly proposed or recommended with evidence, assumptions, decision ownership, and approval gaps visible; no current fact, evidence, approval, or sign-off is fabricated. |
| REQ-012 | Apply the safety gate under Quick energy. | Quick may default length, detail, and shape, but cannot bypass factuality, contradictory-source, authority, or status checks. |
| REQ-013 | Export new and refined documents predictably. | New documents use `export/NNN - doc-[description].md`; refined copies use `export/<original-source-filename>.md` and do not overwrite supplied fixtures. |
| REQ-023 | Apply ClickUp-native Markdown grammar to new documents. | New documents use raw `* * *` dividers, `*   ` unordered bullets, a blank line between title and opening divider, an immediate divider after every non-empty body heading, and adaptive same-level spacer headings between substantial sibling sections. |
| REQ-024 | Route engineering-document requests to Doc Mode without laundering document output into implementation or approval authority. | Requests such as “document this API,” “write an architecture reference,” “recommend an architecture and document the decision,” or “explain this data flow” select Doc when a document is requested. A primary request to modify production code or debug a live failure remains implementation or Bug work, while a documented option analysis or selection remains visibly proposed until authority changes its status. |

### P1 - Required

| ID | Requirement | Acceptance Criteria |
|----|-------------|---------------------|
| REQ-014 | Extend Interactive Mode for documentation. | One prompt can gather energy, document purpose, audience, source set, source authority, desired status, scope, and constraints without a second round when the answer is complete. |
| REQ-015 | Preserve Task and Bug compatibility. | Existing task, subtask, UI-refinement, bug, and Quick Task/Bug fixtures retain their selected intent, templates, exports, and clarification behavior. |
| REQ-016 | Keep resource loading scoped. | Doc requests load HVR, DEPTH, Doc Mode, and Doc Templates; ambiguity loads Interactive resources; Task and Bug requests do not bulk-load Doc resources. |
| REQ-017 | Synchronize CLI and Claude packaging. | AGENTS, Skill, Custom Instructions, knowledge lookup, attestation, export-equivalent path, and user-facing mode tables describe the same Doc contract. |
| REQ-018 | Apply the pinned version and filename policy. | Skill is `0.3.0`; Doc reference and asset are `0.100`; Interactive Mode is `0.403`; Interactive Response Templates are `0.101`; old versioned mirrors are removed. |
| REQ-019 | Rebuild the checksum manifest from bytes. | All eleven knowledge mirrors match their sources, every changed sha256-16 is recomputed, and the existing stale Custom Instructions checksum is corrected. |
| REQ-020 | Correct stale user-guide claims touched by the feature. | README no longer advertises retired Task/Bug versions, obsolete upload filenames, the wrong export syntax, or Quick as a standalone artifact intent. |
| REQ-021 | Exercise the supplied corpus as read-only fixtures. | Tests cover a Barter creation guide, Notification catalog, Feed/geo/dead-deal behavior references, and Feed proposal material without changing any source fixture. |
| REQ-022 | Preserve source defects outside requested scope. | Broken links, legacy spellings, malformed copy, and unmatched markup are flagged but not silently repaired during unrelated refinement. |
| REQ-025 | Refine the router pseudocode per the post-release review (Amendment 002). | The low-confidence clarification suggests the detected mode instead of a hardcoded Task Mode; `INTENT_MODEL` keywords are unweighted vocabulary with scoring owned by `SEMANTIC_TOPICS`; the unreachable documentation fallback chain is removed; natural-language Quick triggers only in request-framing positions so subject-matter "fast" cannot skip intake gates; semantic synonyms match on word boundaries. |
| REQ-026 | Normalize internal titles of spec-touched sources to their mirror basenames (Amendment 002). | `doc_mode.md`, `doc_templates.md`, `interactive_mode.md`, and `interactive_response_templates.md` carry frontmatter titles and H1 headings equal to their knowledge-mirror basenames; mirrors stay byte-identical and every affected sha256-16 is rebuilt from bytes. Untouched pinned sources keep their titles until their next version bump. |
| REQ-027 | Close the confirmed external-review findings (Amendment 003). | The Claude kernel declares alignment with Skill `0.3.0` and describes framing-scoped Quick detection; the three Interactive Doc-context field lists share one vocabulary including contradictions and preservation scope, and the comprehensive question declares its next state; Doc Templates use canonical source-class labels and a single Catalog entry Status; the bug topic scores bare `bug` and `repro` with inflection-tolerant word-boundary matching; the Claude smoke matrix lists `$doc/path` as a rejected false prefix. |
| REQ-028 | Close the confirmed second-round review findings (Amendment 004). | The Task tie-break accepts `task to/for/about/covering/on` so a task about documentation routes Task while independent multi-artifact requests still conflict; negated natural quick/fast language never sets Quick energy; SKILL.md carries narrow supersede clauses for DEPTH's artifact-header contract on Doc refinements and for legacy `$quick`-selects-Raw wording; the Claude kernel loads DEPTH on the Quick route and lists all five source classes in its conflict question; Behavior Reference status hints use the full class labels; the source-conflict hold uses Interactive dash-bullet grammar; the user guide names the Checklist contract accurately. |
<!-- /ANCHOR:requirements -->

---

<!-- ANCHOR:success-criteria -->
## 5. SUCCESS CRITERIA

- **SC-001**: **Given** `$doc` or `$d` as a standalone command token, **When** the router evaluates the request, **Then** it selects `DOC` without falling through to Task or Interactive.
- **SC-002**: **Given** `$document`, `$docs`, or text containing `$d`, **When** command parsing runs, **Then** none of those substrings is treated as the Doc command.
- **SC-003**: **Given** `$quick $doc document Feed behavior` or `$doc $quick document Feed behavior`, **When** routing completes, **Then** the result is `DOC + QUICK` in both orders.
- **SC-004**: **Given** “create a task to document notification behavior,” **When** natural-language routing runs, **Then** Task Mode remains selected.
- **SC-005**: **Given** “write a bug report about broken documentation links,” **When** natural-language routing runs, **Then** Bug Mode remains selected.
- **SC-006**: **Given** “document how Deal Geo Targeting works,” **When** natural-language routing runs, **Then** Doc Mode selects the Product-behavior reference shape.
- **SC-007**: **Given** a new document request grounded only in explicit proposal sources, **When** Doc Mode drafts the artifact, **Then** proposal or future-state status is prominent and no proposal claim is stated as shipped behavior.
- **SC-008**: **Given** a retired Notification concept and an active delivery policy that disagree, **When** synthesis is requested, **Then** retired material remains historical and cannot override the active policy.
- **SC-009**: **Given** conflicting Notification IDs or ambiguous duplicate Reminder files, **When** no authority is supplied, **Then** one consolidated question lists the unresolved decisions and output pauses.
- **SC-010**: **Given** an existing document containing exact URL names, tables, links, literal copy, and a proposal disclaimer, **When** an unrelated section is refined, **Then** protected content remains byte-equivalent.
- **SC-011**: **Given** a new Doc artifact, **When** export completes, **Then** the filename matches `export/NNN - doc-[description].md` and the file exists before the response.
- **SC-012**: **Given** a refined source document, **When** export completes, **Then** the exported basename matches the source basename and the read-only source file is unchanged.
- **SC-013**: **Given** the completed Claude package, **When** mirror and manifest checks run, **Then** all eleven knowledge files are byte-identical to source and every listed sha256-16 matches.
- **SC-014**: **Given** the existing Task and Bug regression matrix, **When** it runs after Doc Mode is added, **Then** no pre-existing fixture changes intent, template, export naming, or question behavior.
- **SC-015**: **Given** “document this API from the supplied OpenAPI source” or “create an engineering reference for this verified data flow,” **When** routing and drafting run, **Then** Doc Mode is selected, exact technical facts are retained, and no missing design or behavior is invented.
- **SC-016**: **Given** each of the four named Feed golden fixtures, **When** a new document is rendered in the matching shape, **Then** the raw Markdown uses `* * *` dividers, `*   ` unordered bullets, fixture-consistent heading/divider adjacency, purpose-fit heading depth, and no unrequested normalization of refinement sources.
<!-- /ANCHOR:success-criteria -->

---

<!-- ANCHOR:risks -->
## 6. RISKS & DEPENDENCIES

| Type | Item | Impact | Mitigation |
|------|------|--------|------------|
| Dependency | `Product Owner/SYNC.md` manual-copy contract | CLI and Claude behavior can drift if mirrors or filenames are updated partially | Treat source skill files as authoritative, replace mirrors in one pass, then verify byte equality and sha256-16 values |
| Dependency | Explicit source status and authority | Some product claims cannot be documented safely from repository placement alone | Classify at claim level and ask one consolidated question when authority remains unknown |
| Risk | Doc signals steal task-about-documentation requests | Existing backlog workflows regress | Apply artifact-framing tie-breaks and retain `$task --subtask` plus UI-refinement precedence |
| Risk | Quick bypasses source safety | A fast document can promote proposals or retired material to production fact | Make the conflict, authority, and status gates non-bypassable |
| Risk | Refinement normalizes meaningful literals | Identifiers, copy, tables, or links change unintentionally | Use the existing document as baseline and verify protected spans or full-file diffs |
| Risk | Rigid templates damage source structure | Existing product docs are reformatted rather than refined | Use adaptive shapes only for new documents; existing-document structure wins |
| Risk | Generic Markdown breaks ClickUp layout conventions | New documents render differently from the established workspace grammar | Validate exact raw divider, bullet, heading, spacer, table, and block placement against four golden fixtures |
| Risk | An authored technical direction is mistaken for approved or shipped behavior | Readers implement an unapproved recommendation as if authority already exists | Permit analysis, recommendations, and selections, but require explicit proposal/recommendation status, evidence, assumptions, decision ownership, approval gaps, and no fabricated current facts |
| Risk | Whole-file authority labels hide mixed evidence | Draft copy or unverified events appear canonical | Permit section- and field-level classifications |
| Risk | Versioned Claude mirrors coexist | Project Knowledge can retrieve obsolete routing | Remove superseded filenames and smoke-test the final eleven-file inventory |
| Risk | User guide cleanup expands beyond feature scope | Unrelated historical content is rewritten | Correct only stale claims needed for Doc Mode accuracy and record other drift separately |
<!-- /ANCHOR:risks -->

---

<!-- ANCHOR:questions -->

## 7. NON-FUNCTIONAL REQUIREMENTS

### Determinism

- **NFR-D01**: The same command tokens and request wording must produce the same intent and energy regardless of `$quick` token order.
- **NFR-D02**: Explicit command collisions must never be resolved by hidden priority; they enter clarification.

### Factual Safety

- **NFR-F01**: Unknown, proposed, approved-but-unshipped, and retired material must remain visibly distinct from current behavior.
- **NFR-F02**: Recency, active-folder placement, or duplicate content alone must not establish authority.

### Fidelity

- **NFR-I01**: Refinement is minimal-diff by default and preserves protected structure and literals outside the requested change.
- **NFR-I02**: Known source defects are reported without silent correction unless correction is the stated purpose.
- **NFR-I03**: New-document layout is deterministic under the ClickUp grammar; refinement retains the source grammar unless normalization is explicitly requested.

### Compatibility

- **NFR-C01**: Task and Bug resources remain lazy-loaded and retain current versions.
- **NFR-C02**: CLI and Claude packaging must expose equivalent intent, energy, source-safety, refinement, and delivery semantics.

### Maintainability

- **NFR-M01**: The Skill remains the routing authority; Doc Mode and Doc Templates hold Doc-specific detail without duplicating Task or Bug contracts.
- **NFR-M02**: The mirror manifest must be reproducible from file bytes with `shasum -a 256`.

---

## 8. EDGE CASES

### Routing Boundaries

- `$d` inside `$debug`, `$docs`, a filename, or ordinary prose is not a command.
- `$quick` without an explicit artifact command infers Bug or Doc from the remaining request; it retains the existing Task fallback when neither is clear.
- Multiple explicit artifact commands are ambiguous even under Quick energy.
- “Document bug behavior” requests a product reference; “write a bug report about documentation” requests a bug artifact.
- “Document this API,” “write an engineering runbook,” “explain this architecture,” and “choose an architecture and record the recommendation” request Doc artifacts. A primary request to modify the API or debug a live failure remains implementation or Bug work rather than becoming Doc automatically.
- UI polish or Figma alignment with “fix” language remains Task unless Bug is explicitly requested.
- A request for both a task and a document is multi-artifact and enters Interactive Mode unless one artifact is explicitly primary.

### Source Boundaries

- A file can mix verified events, new events, draft copy, and not-ready designs; classification must be granular.
- Two byte-identical files are one evidence lineage, not independent corroboration.
- A canonical policy can win within its declared scope without becoming authoritative for unrelated copy or event identity.
- Missing linked sources, broken local assets, or stale relative links are surfaced as evidence gaps.
- Present-tense prose in `z_legacy` or explicitly retired `z_concept` material remains retired.
- A user may explicitly request historical or proposed material; the document must retain the matching status label.

### Refinement Boundaries

- Source headings, order, tables, identifiers, links, code fences, YAML keys, and literal copy remain unchanged outside the requested edit.
- Exact legacy identifiers and misspellings remain intact when they carry system meaning.
- A requested full rewrite may adopt an adaptive shape only after the user has authorized structural change.
- A request to normalize a document may change list markers, divider spelling, heading depth, spacer headings, or table syntax only when that normalization is explicitly in scope.
- For a new ClickUp-targeted document, use `* * *` rather than `---`, `*   ` rather than `- `, place a divider immediately after each non-empty body heading, and use empty same-level spacer headings only for substantial sibling sections.

---

## 9. COMPLEXITY ASSESSMENT

| Dimension | Score | Triggers |
|-----------|-------|----------|
| Scope | 22/25 | Router, two new resources, two interactive resources, bootstrap, guide, sync rules, Claude kernel, manifest, and eleven mirrors |
| Risk | 22/25 | Compatibility-sensitive routing, source authority, literal preservation, and two-package drift |
| Research | 19/20 | Current Product Owner system plus 8 Barter, 26 Notification, and 5 Feed Markdown fixtures |
| Multi-Agent | 5/15 | Analysis can parallelize; implementation remains one ordered compatibility release |
| Coordination | 12/15 | Source/mirror versioning, renames, checksums, exports, and regression verification |
| **Total** | **80/100** | **Level 3 selected; standard packet retained by explicit scope decision** |

The feature is documentation-heavy rather than infrastructure-heavy. A phased parent would split one atomic routing and packaging contract across independently drifting children, so the supplied standard Level 3 packet remains the safer control surface.

---

## 10. RISK MATRIX

| Risk ID | Description | Impact | Likelihood | Mitigation |
|---------|-------------|--------|------------|------------|
| R-001 | Natural Doc phrases override explicit Task or Bug framing | High | Medium | Command-first and artifact-framing fixtures |
| R-002 | Quick energy silently bypasses authority clarification | High | Medium | Non-bypassable conflict/status gate |
| R-003 | Proposal or retired content becomes production truth | High | High | Mandatory source classification and visible labels |
| R-004 | Refinement mutates protected literals | High | Medium | Minimal-diff contract plus before/after comparison |
| R-005 | Claude retrieves stale versioned mirrors | High | Medium | Remove old names, verify inventory and hashes |
| R-006 | README cleanup causes unrelated churn | Medium | Medium | Limit edits to feature-relevant stale claims |
| R-007 | Existing checksum drift is copied forward | Medium | High | Recompute every changed checksum from bytes |
| R-008 | Corpus fixtures are modified during testing | High | Low | Hash or Git-diff read-only guard |
| R-009 | Engineering documentation is rejected categorically or authored recommendations are presented with false authority | High | Medium | Route by requested artifact, permit technical analysis and selection records, and test status, evidence, assumption, ownership, approval-gap, and no-fabrication outcomes |
| R-010 | New documents use generic Markdown that renders inconsistently in ClickUp | High | High | Four raw-Markdown golden fixtures and exact token/adjacency assertions |

---

## 11. USER STORIES

### US-001: Create trustworthy product documentation (Priority: P0)

**As a** Product Owner, **I want** a dedicated documentation workflow, **so that** product behavior and rationale can be recorded without disguising a document as a backlog task.

**Acceptance Criteria**:

1. **Given** a clear Doc command or natural-language request, **When** routing completes, **Then** Doc Mode selects a purpose-fit shape and includes audience-appropriate WHAT, WHY, source-backed HOW, or explicitly proposed technical reasoning.
2. **Given** a product-behavior claim, **When** its source is not verified or authoritative, **Then** the output labels the uncertainty or asks for authority before stating it as current.

### US-002: Refine without damaging the source (Priority: P0)

**As a** documentation maintainer, **I want** requested edits to preserve the rest of the document, **so that** identifiers, links, tables, status warnings, and approved copy do not drift.

**Acceptance Criteria**:

1. **Given** a scoped refinement request, **When** the document is updated, **Then** untouched protected content remains unchanged and the exported basename matches the source basename.
2. **Given** a malformed source detail outside scope, **When** refinement completes, **Then** it is flagged rather than silently normalized.

### US-003: Distinguish current, approved, proposed, and retired material (Priority: P0)

**As a** product-document reader, **I want** source status to remain explicit, **so that** I can tell shipped behavior from direction, proposal, history, or uncertainty.

**Acceptance Criteria**:

1. **Given** sources with different statuses, **When** a document uses them, **Then** each status remains visible and contradictory claims are not blended.
2. **Given** unresolved source authority, **When** a definitive claim would be unsafe, **Then** one consolidated clarification question is asked and drafting waits.

### US-004: Produce a quick document safely (Priority: P1)

**As a** Product Owner under time pressure, **I want** Quick energy to shorten the workflow without changing Doc intent, **so that** I get a concise document without losing source safety.

**Acceptance Criteria**:

1. **Given** `$quick` with Doc intent, **When** purpose and authority are clear, **Then** Doc Mode produces the narrowest useful shape without ordinary follow-up.
2. **Given** contradictory sources under Quick energy, **When** no authority resolves them, **Then** the same conflict gate still asks one consolidated question.

### US-005: Keep CLI and Claude behavior aligned (Priority: P1)

**As a** packaging maintainer, **I want** both Product Owner distributions to describe the same mode, **so that** users receive equivalent routing, fidelity, and safety behavior in either runtime.

**Acceptance Criteria**:

1. **Given** the final source and Project Knowledge mirrors, **When** parity checks run, **Then** mirror bytes, filenames, versions, checksums, commands, and smoke tests align.
2. **Given** superseded versioned mirrors, **When** the package is assembled, **Then** obsolete filenames are absent.

### US-006: Document engineering systems without inventing them (Priority: P0)

**As a** technical stakeholder, **I want** Doc Mode to turn engineering evidence and requested analysis into a usable guide, catalog, behavior reference, proposal, recommendation, or decision record, **so that** technical knowledge and options can be documented without confusing an authored direction with approved or shipped implementation.

**Acceptance Criteria**:

1. **Given** authoritative API, architecture, schema, data-flow, code-behavior, or operational sources, **When** an engineering document is requested, **Then** Doc Mode may preserve and explain their verified technical facts.
2. **Given** a missing current implementation fact, root cause, procedure, approval, or operational result, **When** a definitive current-state statement would require invention, **Then** Doc Mode labels the gap or asks one consolidated question; if analysis or selection is requested, it keeps the result explicitly proposed or recommended rather than presenting it as established fact.

### US-007: Match established ClickUp document layout (Priority: P0)

**As a** ClickUp documentation maintainer, **I want** new Doc artifacts to use the workspace's raw Markdown grammar, **so that** headings, dividers, lists, and repeated blocks render like the existing Feed documentation.

**Acceptance Criteria**:

1. **Given** a new document, **When** its Markdown is generated, **Then** it follows the shared ClickUp divider, bullet, heading, spacer, table, quote, and fenced-block rules while adapting hierarchy to the selected shape.
2. **Given** an existing source with another style, **When** it is refined without a normalization request, **Then** its source grammar remains unchanged outside the requested edit.

---

## 12. OPEN QUESTIONS

No blocking product questions remain for implementation. Source-authority questions are request-specific runtime decisions handled by Doc Mode’s consolidated clarification gate.
<!-- /ANCHOR:questions -->

---

## RELATED DOCUMENTS

- **Implementation Plan**: [plan.md](plan.md)
- **Task Breakdown**: [tasks.md](tasks.md)
- **Verification Checklist**: [checklist.md](checklist.md)
- **Decision Records**: [decision-record.md](decision-record.md)
- **Corpus Research**: [research.md](research.md)
- **Specification-only Status**: [implementation-summary.md](implementation-summary.md)
