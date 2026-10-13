---
title: "Decision Record: Product Owner Doc Mode"
description: "Record the product and packaging decisions that define Doc Mode routing, adaptive document shapes, source-safe engineering documentation, ClickUp-native layout, and read-only source handling."
trigger_phrases:
  - "product owner doc mode decisions"
  - "dedicated doc intent"
  - "adaptive document shapes"
  - "source authority conflict gate"
importance_tier: "high"
contextType: "decision"
_memory:
  continuity:
    packet_pointer: "002-product-owner-mode-additions/001-product-owner-doc-mode"
    last_updated_at: "2026-07-14T15:54:08Z"
    last_updated_by: "codex"
    recent_action: "Implemented ADR-004 and verified the corrected source and Claude package"
    next_safe_action: "No decision action remains; preserve the recorded contracts during future changes"
---
<!-- SPECKIT_TEMPLATE_SOURCE: decision-record | v2.2 -->
# Decision Record: Product Owner Doc Mode

<!-- SPECKIT_LEVEL: 3 -->
<!-- HVR_REFERENCE: .opencode/skills/sk-doc/references/hvr_rules.md -->

---

<!-- ANCHOR:adr-001 -->
## ADR-001: Use a Dedicated Doc Intent

### Metadata

| Field | Value |
|-------|-------|
| **Status** | Accepted |
| **Date** | 2026-07-14 |
| **Deciders** | Product Owner maintainers |

---

<!-- ANCHOR:adr-001-context -->
### Context

Before this release, the Product Owner created task and bug artifacts only. Product documentation has different intake, source-safety, refinement, and export requirements. Extending Task Mode would make task fields stand in for audience, source authority, and current-versus-proposed status, while leaving refinement fidelity and conflict handling implicit.

The router must also preserve existing behavior. “Create a task to document X” remains a task, while “document X” selects the new document artifact. Quick controls effort and length; it does not identify the artifact.

### Constraints

- Existing Task, Subtask, UI-refinement, and Bug fixtures must keep their current intent and artifact behavior.
- Exact `$doc` and `$d` command tokens must not match longer strings such as `$docs` or `$debug`.
- Doc output may cover verified product or engineering behavior, supplied technical facts, and explicitly proposed analysis, recommendations, selections, or code examples; it must not mutate production, fabricate current behavior or evidence, or claim unsupported approval or sign-off.
- CLI and Claude packaging must expose the same routing contract.
<!-- /ANCHOR:adr-001-context -->

---

<!-- ANCHOR:adr-001-decision -->
### Decision

**We chose**: Add `DOC` as a first-class artifact intent and model `QUICK` as an independent energy override.

**How it works**: The router extracts energy separately, then resolves one artifact intent from explicit commands and natural-language framing. A single explicit artifact command wins over prose; conflicting artifact commands or unsafe ambiguity enter Interactive Mode and produce one consolidated clarification question. Task-about-documentation and bug-report framing retain Task and Bug precedence respectively.
<!-- /ANCHOR:adr-001-decision -->

---

<!-- ANCHOR:adr-001-alternatives -->
### Alternatives Considered

| Option | Pros | Cons | Score |
|--------|------|------|-------|
| **Dedicated `DOC` intent** | Gives documentation its own safety, refinement, resource, and export contract; keeps intent separate from energy | Adds one router branch and new regression surface | 9/10 |
| Extend Task Mode | Reuses an existing mode and task templates | Conflates backlog work with product documentation; cannot express source authority or structural fidelity cleanly | 4/10 |
| Handle documents only through Interactive Mode | Avoids a new direct command | Makes clear requests unnecessarily conversational and leaves no stable document artifact contract | 3/10 |

**Why this one**: Doc Mode needs controls that do not belong in Task Mode. A dedicated intent isolates those controls while explicit tie-breaks protect compatibility.
<!-- /ANCHOR:adr-001-alternatives -->

---

<!-- ANCHOR:adr-001-consequences -->
### Consequences

**What improves**:

- Documentation requests receive purpose-built intake, source classification, refinement, and export behavior.
- `$quick $doc ...` and `$doc $quick ...` resolve consistently to the same intent and energy.
- Task and Bug semantics remain independently testable.

**What it costs**:

- The router, Interactive Mode, bootstrap guidance, user guide, and Claude package must change together. Mitigation: treat the source-to-Claude sync and regression matrix as release gates.
- Natural-language boundaries need more fixtures. Mitigation: test artifact framing separately from subject nouns.

**Risks**:

| Risk | Impact | Mitigation |
|------|--------|------------|
| Doc signals steal task-about-documentation requests | High | Make artifact framing stronger than the word “document” and retain explicit-command priority |
| `$d` matches longer text | High | Require a standalone, token-bounded command |
| Quick bypasses a Doc safety gate | High | Apply authority, status, and conflict gates after energy extraction |
<!-- /ANCHOR:adr-001-consequences -->

---

<!-- ANCHOR:adr-001-five-checks -->
### Five Checks Evaluation

| # | Check | Result | Evidence |
|---|-------|--------|----------|
| 1 | **Necessary?** | PASS | The pre-release router had no documentation artifact or safe refinement path |
| 2 | **Beyond Local Maxima?** | PASS | Task extension and Interactive-only handling were compared |
| 3 | **Sufficient?** | PASS | One new intent plus orthogonal energy covers direct, quick, and ambiguous requests |
| 4 | **Fits Goal?** | PASS | Dedicated routing is required before Doc resources can be loaded predictably |
| 5 | **Open Horizons?** | PASS | Independent intent and energy allow future effort levels without multiplying artifact modes |

**Checks Summary**: 5/5 PASS
<!-- /ANCHOR:adr-001-five-checks -->

---

<!-- ANCHOR:adr-001-impl -->
### Implementation

**What changes**:

- Update `Product Owner/skill/SKILL.md` to parse exact Doc commands, separate energy, add tie-breaks, and load Doc resources.
- Update Interactive Mode, CLI guidance, exports, and Claude packaging to describe the same artifact and energy model.
- Add routing fixtures for exact commands, token boundaries, artifact framing, ambiguity, and Task/Bug regressions.

**How to roll back**: Restore the previous router and packaging files as one versioned set, remove the Doc-only reference and template mirrors, and rerun the existing Task/Bug regression and checksum checks. The reference corpus remains untouched.
<!-- /ANCHOR:adr-001-impl -->
<!-- /ANCHOR:adr-001 -->

---

## ADR-002: Use Four Adaptive Document Shapes

### Metadata

| Field | Value |
|-------|-------|
| **Status** | Accepted |
| **Date** | 2026-07-14 |
| **Deciders** | Product Owner maintainers |

---

### Context

The supplied corpus does not follow one useful universal structure. Barter creation material behaves like an ordered guide, Notification material needs stable catalog entries and identifiers, Feed behavior needs rules and state boundaries, How it Works combines business and engineering detail, and ranking documents describe future options rather than current facts.

A single mandatory template would either flatten those distinctions or accumulate many optional sections. Refinement raises a second constraint: an existing document’s structure carries meaning and must remain the baseline unless the user explicitly requests a structural rewrite.

### Constraints

- New documents must be recognizable as Guide, Catalog, Product-behavior reference, or Proposal or future-state documents regardless of whether their subject is product, engineering, or mixed.
- Shape selection must follow purpose, audience, evidence, and status rather than keywords alone.
- Existing heading hierarchy, order, links, identifiers, tables, literal copy, and status notices remain protected during scoped refinement.
- Quick energy may shorten a shape but may not remove required status or evidence boundaries.

---

### Decision

**We chose**: Provide four adaptive shapes for new documents and make the existing document the structural authority for refinements.

**How it works**: Guide emphasizes purpose, ordered steps, component rules, and next links. Catalog emphasizes an index, stable identifiers, vocabulary, repeated entries, and cross-links. Product-behavior reference emphasizes states, rules, combinations, examples, boundaries, and outcomes. Proposal or future-state documentation leads with status, separates current from proposed behavior, and records trade-offs and open decisions. An API guide, schema catalog, architecture behavior reference, or engineering proposal uses the same shape logic; engineering is subject matter, not a fifth shape.

---

### Alternatives Considered

| Option | Pros | Cons | Score |
|--------|------|------|-------|
| **Four adaptive shapes** | Matches observed product-document patterns; makes status and audience visible; remains compact | Requires a shape-selection rule and four quality checks | 9/10 |
| One universal template | One scaffold and one validation path | Produces empty or misleading sections; encourages proposal and behavior content to look alike | 5/10 |
| Free-form generation | Maximum flexibility | Weak repeatability, hard-to-test quality, and no reliable status placement | 3/10 |

**Why this one**: Four shapes cover the real corpus patterns without making subject matter determine structure, inventing a fifth engineering-only shape, or forcing existing documents into a new layout. Technical analysis or architecture selection can live in the Proposal shape when requested and accurately labelled.

---

### Consequences

**What improves**:

- New documents expose the sections readers need for their purpose.
- Proposal disclaimers and current-versus-future distinctions become structural requirements.
- Refinement avoids format churn because the source document wins over the new-document templates.

**What it costs**:

- Shape selection adds one decision to document intake. Mitigation: infer it only when purpose, audience, and status make the choice safe.
- Quality checks vary by shape. Mitigation: keep common factuality and fidelity gates outside the shape-specific template.

**Risks**:

| Risk | Impact | Mitigation |
|------|--------|------------|
| The wrong shape is inferred from a topic noun | Medium | Select from purpose and intended use, not subject vocabulary |
| A Proposal looks like shipped behavior | High | Require a prominent status warning and explicit current/future split |
| Refinement reformats a source document | High | Treat source structure as the baseline unless structural change is authorized |

---

### Five Checks Evaluation

| # | Check | Result | Evidence |
|---|-------|--------|----------|
| 1 | **Necessary?** | PASS | The corpus contains four materially different reader and status needs |
| 2 | **Beyond Local Maxima?** | PASS | Universal and free-form structures were compared |
| 3 | **Sufficient?** | PASS | The four shapes cover the named product and engineering-oriented fixtures without adding a subject-specific type |
| 4 | **Fits Goal?** | PASS | Adaptive structure directly supports trustworthy product and engineering documentation |
| 5 | **Open Horizons?** | PASS | Shape rules can evolve independently while refinements remain source-led |

**Checks Summary**: 5/5 PASS

---

### Implementation

**What changes**:

- Add `Product Owner/skill/assets/doc_templates.md` with the four new-document shapes and shared status requirements.
- Add shape selection and refinement-baseline rules to `Product Owner/skill/references/doc_mode.md`.
- Test Barter, Notification, Feed behavior, engineering-oriented How it Works, and Feed proposal fixtures against their expected shapes.

**How to roll back**: Remove the Doc template asset and shape-selection references, restore the previous package inventory and checksums, and leave any exported documents and source fixtures unchanged for manual review.

---

## ADR-003: Treat the Source Corpus as Read-Only Evidence

### Metadata

| Field | Value |
|-------|-------|
| **Status** | Accepted |
| **Date** | 2026-07-14 |
| **Deciders** | Product Owner maintainers |

---

### Context

The reference corpus contains active-looking, proposed, retired, duplicated, internally inconsistent, and authority-unknown material. Some files mix verified events, new events, draft copy, and not-ready design status. Directory placement, present tense, recency, and duplicate copies do not establish enough authority to merge claims safely.

The Product Owner must use these sources to document product or engineering behavior without editing them, resolving contradictions by assumption, or silently correcting meaningful defects. It may retain and explain supplied technical facts and may develop an explicitly proposed technical recommendation from stated evidence and assumptions, but cannot turn incomplete evidence into fabricated current facts or false approval.

### Constraints

- Barter-deal, Notification, and the five named Feed documents are read-only fixtures.
- Claims can require classification below file level.
- Current behavior, approved direction, proposal, retired material, and unknown must remain distinct.
- Unresolved authority or contradictory claims must stop synthesis after one consolidated clarification question.
- Refinements export a copy and never overwrite the supplied source.

---

### Decision

**We chose**: Classify source claims before synthesis, keep the supplied corpus read-only, and block unresolved conflicts instead of merging them.

**How it works**: Authority follows explicit user designation, explicit source labels, repository placement, then corroborating evidence. Recency alone does not decide authority, and duplicate files count as one evidence lineage. A clearly authoritative source may win within its declared scope; otherwise Doc Mode asks one consolidated question and waits.

---

### Alternatives Considered

| Option | Pros | Cons | Score |
|--------|------|------|-------|
| **Read-only classified evidence with a conflict gate** | Preserves provenance; prevents proposals and retired material from becoming production facts | Some requests pause for clarification | 10/10 |
| Prefer the newest or active-path file | Fast and deterministic | Repository placement and recency are unreliable in the supplied corpus | 2/10 |
| Merge all sources and note disagreements afterward | Produces a draft in one pass | Creates internally contradictory documents and hides which claim controls | 1/10 |

**Why this one**: A slower, explicit clarification is cheaper than publishing a confident but false product contract. The corpus demonstrates that silent source blending is unsafe.

---

### Consequences

**What improves**:

- Current, approved, proposed, retired, and unknown claims remain distinguishable.
- Conflicts, missing canonical sources, duplicate lineages, and source defects stay visible.
- Source fixtures, exact identifiers, links, tables, and literal copy remain available for audit.

**What it costs**:

- Some document requests cannot complete without user authority. Mitigation: ask one consolidated question containing every blocking authority and status choice.
- Claim-level classification adds review work. Mitigation: classify only material claims and inherit an explicit status when its scope is unambiguous.

**Risks**:

| Risk | Impact | Mitigation |
|------|--------|------------|
| A retired concept overrides active policy | High | Retired material cannot establish current behavior |
| Two duplicate files appear to corroborate a claim | High | De-duplicate evidence lineage before authority assessment |
| A source defect is silently normalized | Medium | Flag out-of-scope defects and preserve source literals |
| Supplied identifiers imply unsupported current architecture | High | Preserve established facts; leave current-state gaps explicit, and put any authored design choice in a labelled proposal with evidence, assumptions, decision owner, and approval gap |

---

### Five Checks Evaluation

| # | Check | Result | Evidence |
|---|-------|--------|----------|
| 1 | **Necessary?** | PASS | The corpus audit found explicit status conflicts, duplicate files, missing sources, and internal contradictions |
| 2 | **Beyond Local Maxima?** | PASS | Newest-file and merge-all policies were rejected against observed evidence |
| 3 | **Sufficient?** | PASS | Five source classes plus a conflict gate cover the identified authority states |
| 4 | **Fits Goal?** | PASS | Trustworthy documentation depends on preventing unsupported production claims |
| 5 | **Open Horizons?** | PASS | The authority order accepts future explicit sources without hardcoding corpus-specific winners |

**Checks Summary**: 5/5 PASS

---

### Implementation

**What changes**:

- Add source classification, authority ordering, conflict handling, and one-question clarification rules to Doc Mode and Interactive Mode.
- Add preservation checks for filenames, headings, links, identifiers, tables, status notices, and untouched literal copy.
- Exercise the corpus through read-only tests and compare source hashes or repository diffs before and after.

**How to roll back**: Remove the Doc-only classification and conflict resources with the rest of the mode, restore prior packaging, and verify that the read-only corpus has no diff. Do not “resolve” corpus conflicts as part of rollback.

---

<!-- ANCHOR:adr-004 -->
## ADR-004: Use ClickUp-Native Grammar for New Documents and Source-Native Grammar for Refinements

### Metadata

| Field | Value |
|-------|-------|
| **Status** | Accepted and implemented |
| **Date** | 2026-07-14 |
| **Deciders** | Product Owner maintainers |

---

### Context

The initial adaptive templates captured document purpose but used generic Markdown scaffolds. The four named Feed fixtures establish a separate workspace grammar: raw `* * *` dividers, `*   ` unordered bullets, divider-backed headings, same-level empty spacer headings between substantial siblings, compact definition blocks, and purpose-fit H2/H3/H4 depth. Their repeated entries use label blocks unless the content is a real comparison matrix.

The distinction between creation and refinement matters. A new ClickUp-targeted document should look native to the workspace. An existing document may use another deliberate grammar, and silently normalizing it would violate the minimal-diff fidelity invariant.

### Constraints

- The raw source, not rendered equivalence, defines the golden grammar.
- Compact `***`, `---`, and `- ` lists are not accepted substitutes in new ClickUp-targeted documents.
- Heading depth follows document topology rather than a rigid H2-only outline.
- Empty same-level spacer headings separate substantial siblings but are not inserted mechanically into compact entry sequences.
- Refinement preserves the source's list markers, divider form and placement, heading/spacer scheme, tables, fences, quotes, and repeated-entry style unless normalization is explicitly requested.

---

### Decision

**We chose**: Make ClickUp-native grammar the shared default for new Doc artifacts and keep refinement source-native unless the user explicitly requests structural or style normalization.

**How it works**: New templates share an opening envelope, divider-backed real headings, exact unordered-list syntax, and adaptive section primitives. Guide, Catalog, behavior-reference, and Proposal shapes then select their semantic hierarchy and repeated-entry patterns. Refinement bypasses normalization and applies the smallest coherent edit in the source's established grammar.

---

### Alternatives Considered

| Option | Pros | Cons | Score |
|--------|------|------|-------|
| **ClickUp-native new documents plus source-native refinement** | Matches workspace output while preserving existing documents | Requires exact raw-Markdown fixtures and two layout policies | 10/10 |
| Generic CommonMark everywhere | Familiar and easy to author | Produces visibly inconsistent ClickUp documents and ignores supplied examples | 3/10 |
| Normalize every refinement to ClickUp | Creates one future style | Causes broad format churn and violates refinement fidelity | 2/10 |
| Copy one Feed file as a universal template | Matches one fixture closely | Conflates content topology with formatting and fails other document shapes | 4/10 |

**Why this one**: Creation and refinement optimize for different risks. Native defaults improve new-document consistency; source-led refinement prevents collateral rewrites.

---

### Consequences

**What improves**:

- New documents render consistently with established ClickUp documentation.
- Bullet, divider, heading, table, quote, fence, and repeated-entry behavior becomes testable from raw Markdown.
- Engineering and product documents share layout primitives without sharing one rigid outline.
- Existing documents retain their own grammar unless the user asks to normalize it.

**What it costs**:

- Template resources and mirrors require a correction release. Mitigation: change source first, rebuild mirrors, and recompute checksums.
- Raw-Markdown tests are stricter than renderer snapshots. Mitigation: use four golden fixtures that cover different topologies rather than one universal string fixture.

**Risks**:

| Risk | Impact | Mitigation |
|------|--------|------------|
| Empty spacer headings are inserted everywhere | Medium | Limit them to substantial same-level siblings and test compact glossary sequences separately |
| Export artifacts are mistaken for authoring rules | Medium | Do not generate bare trailing headings; preserve them only during unrelated refinement |
| A valid but non-native Markdown equivalent passes | High | Assert exact raw tokens and line adjacency |
| Refinement is normalized incidentally | High | Require explicit normalization scope and compare protected formatting regions |

---

### Five Checks Evaluation

| # | Check | Result | Evidence |
|---|-------|--------|----------|
| 1 | **Necessary?** | PASS | All four Feed fixtures use the same divider and bullet tokens while the current scaffolds use neither |
| 2 | **Beyond Local Maxima?** | PASS | Generic Markdown, universal normalization, and single-fixture copying were compared |
| 3 | **Sufficient?** | PASS | Shared primitives plus adaptive hierarchy cover behavior, proposal, engineering-reference, and pattern fixtures |
| 4 | **Fits Goal?** | PASS | Native layout and source-safe refinement directly address the reported document-quality gap |
| 5 | **Open Horizons?** | PASS | Layout primitives can evolve independently from source classification and shape semantics |

**Checks Summary**: 5/5 PASS

---

### Implementation

**What changes**:

- Correct Doc Mode and Doc Templates so new documents use the shared ClickUp grammar and refinements remain source-native.
- Update bootstrap, user guidance, synchronization guidance, Claude instructions, mirrors, versions, and checksums as one package.
- Add engineering-document routing, labelled recommendation/selection, no-fabrication, and no-false-authority cases.
- Add exact raw-Markdown golden fixtures for Feed - Dead Deals, Feed Functions, How it Works, and Patterns.

**How to roll back**: Restore the last verified Doc reference, template asset, synchronized guidance, mirrors, and checksum manifest as one set. Keep the expanded packet research as evidence of the rejected generic-layout behavior, and do not alter the reference fixtures.
<!-- /ANCHOR:adr-004 -->

---

<!-- ANCHOR:adr-005 -->
## ADR-005: Scope Amendment 002 to Spec-Touched Files and Exempt ClickUp Scaffold Tables from the Two-Column Preference

### Metadata

| Field | Value |
|-------|-------|
| **Status** | Accepted |
| **Date** | 2026-07-14 |
| **Deciders** | Product Owner maintainers |

---

### Context

An independent post-release review confirmed the shipped packet matches the specification and surfaced five minor findings: four router-pseudocode refinements and one internal-title naming inconsistency. It also flagged that the doc-template scaffolds contain five-column tables while the repository documentation preference caps tables at two columns.

Three title conventions coexist in the skill sources. Mirror filenames already normalize to one convention. Pinned sources such as Task Mode, Bug Mode, DEPTH, and the shared Human Voice Rules were declared protected by this release, and changing their bytes for a cosmetic title would break that freeze without a version bump.

### Constraints

- Protected sources must keep their release bytes until their own version bump.
- Every source edit must re-sync its mirror and rebuild its checksum in the same change.
- New-document scaffolds were validated against the four Feed golden fixtures, which use real matrix tables for dense indexes and trade-off comparisons.
- The two-column preference governs repository documentation prose, and the scaffolds live inside code fences as deliverable grammar.

---

### Decision

**We chose**: Normalize internal titles only in the four sources this release created or modified, keep every pinned source untouched, and exempt ClickUp scaffold tables inside code fences from the repository two-column documentation preference.

**How it works**: The four spec-touched sources adopt their knowledge-mirror basename as frontmatter title and H1. Pinned sources adopt the convention at their next real version bump. Scaffold tables remain fixture-shaped because they are deliverable output grammar, not repository documentation prose; the template files' own prose tables already comply with the two-column preference.

---

### Alternatives Considered

| Option | Pros | Cons | Score |
|--------|------|------|-------|
| **Normalize spec-touched files only; exempt scaffold tables** | Ends the drift for new work without breaking the protected-source freeze or fixture parity | Title drift persists in pinned files until their next bump | 9/10 |
| Normalize every source title now | One convention immediately | Mutates protected release bytes for cosmetics and forces checksum churn across frozen files | 3/10 |
| Narrow scaffold tables to two columns | Satisfies the repository preference literally | Deviates from the validated Feed golden fixtures and degrades dense catalog indexes | 2/10 |
| Do nothing | Zero churn | Leaves three coexisting conventions and an unresolved preference conflict | 4/10 |

**Why this one**: It fixes what this release owns, respects what this release froze, and resolves the table question by distinguishing deliverable grammar from repository prose.

---

### Consequences

**What improves**:

- The four amendment sources match their mirror basenames, so title and filename can be compared mechanically.
- The two-column preference has a recorded boundary instead of an ambiguous conflict with the golden fixtures.
- Future version bumps have a stated convention to adopt.

**What it costs**:

- Pinned sources keep their legacy titles for now. Mitigation: the convention is recorded here and applies at each next bump.
- Four mirrors and checksums must be rebuilt. Mitigation: the existing sync contract already covers this.

**Risks**:

| Risk | Impact | Mitigation |
|------|--------|------------|
| A title edit drifts from its mirror | Medium | Re-sync and re-hash in the same change, then verify 11/11 parity and 12/12 digests |
| A stale title reference survives elsewhere | Low | Scan the package for the old title strings outside archived folders |

---

### Five Checks Evaluation

| # | Check | Result | Evidence |
|---|-------|--------|----------|
| 1 | **Necessary?** | PASS | Three coexisting title conventions and an unresolved table-preference conflict were found by independent review |
| 2 | **Beyond Local Maxima?** | PASS | Full normalization, table narrowing, and doing nothing were compared |
| 3 | **Sufficient?** | PASS | Spec-touched scope ends the drift for this release and records the convention for future bumps |
| 4 | **Fits Goal?** | PASS | Protected-source freeze and golden-fixture parity are both preserved |
| 5 | **Open Horizons?** | PASS | Pinned files can adopt the convention independently at their next version bump |

**Checks Summary**: 5/5 PASS

---

### Implementation

**What changes**:

- Set frontmatter title and H1 to the mirror basename in `doc_mode.md`, `doc_templates.md`, `interactive_mode.md`, and `interactive_response_templates.md`.
- Re-sync the four affected mirrors and rebuild their sha256-16 entries.
- Leave every pinned source, corpus fixture, and scaffold table unchanged.

**How to roll back**: Restore the four sources and mirrors from git and revert the four checksum rows. No protected file or fixture is involved.
<!-- /ANCHOR:adr-005 -->

---

<!--
Level 3 Decision Record (Addendum): One ADR per major decision.
Write in human voice: active, direct, specific. No em dashes, no hedging.
HVR rules: .opencode/skills/sk-doc/references/hvr_rules.md
-->
