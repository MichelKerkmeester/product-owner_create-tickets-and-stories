---
title: "Product Owner - Templates - Doc Mode - v0.109"
description: "Source-safe workflow, ClickUp formatting rules, and delivery standards for creating and refining product or engineering documentation."
version: "0.109"
contextType: reference
importance_tier: high
trigger_phrases:
  - "doc mode"
  - "$doc product documentation"
  - "$doc engineering documentation"
  - "write an API reference"
  - "create a runbook"
  - "document how this works"
  - "refine product documentation"
  - "refine technical documentation"
  - "source authority conflict"
---

# Product Owner - Templates - Doc Mode - v0.109

Doc-mode guidance for trustworthy product and engineering documentation. The mode creates or refines guides, catalogs, behavior references, and proposal or future-state documents without turning unverified material into current or approved fact.

**Loading Condition:** ON-DEMAND
**Purpose:** Provides the workflow, source-authority rules, refinement safeguards, adaptive structures, and delivery standards for `$doc`, `$d`, and clear natural-language documentation requests
**Scope:** Product, engineering, operational, security, compliance, and mixed-domain documentation covering verified facts, source-backed HOW, approved direction, and explicitly labelled proposals or recommendations
**Output Path:** `export/[###] - doc-[description].md` for a new document or `export/[original-source-filename].md` for a refinement
**Loads With:** `assets/doc-templates.md` as the paired scaffold, beside the always-loaded `references/hvr-core.md` and `references/conciseness.md`
**Routed By:** `$doc`, `$d`, doc framing, and the documentation semantic topic on its 0.85 override. Every Doc route runs the source-authority and conflict gate before drafting, including under Quick energy
**Hands Off To:** `references/interactive-mode.md` when that gate returns BLOCKED on a missing field, an unresolved source conflict or a claim whose subject no supplied source covers, which returns here once the answer clears the gate

---

## 1. OVERVIEW

### Purpose

Doc Mode turns supplied context into a usable product or engineering document while preserving the difference between fact, direction, proposal, history, and uncertainty. The artifact may explain technical HOW, analyze alternatives, or propose a design when the request and evidence support it. It must not disguise unverified analysis as current implementation or approval.

### When to Use

Use Doc Mode for:

- A new product or engineering guide, implementation guide, runbook, troubleshooting guide, or content standard
- A catalog of messages, states, APIs, endpoints, events, schemas, data fields, configuration, controls, or other stable entries
- A product- or system-behavior reference that explains states, architecture, components, flows, rules, boundaries, and outcomes
- A proposal, RFC, decision record, or future-state document that keeps candidate design distinct from current and approved behavior
- A narrative overview: a folder README, project status, investigation log, handover or post-mortem where the reader needs orientation and story in prose
- A targeted refinement of an existing product or engineering document
- A natural-language request such as "document how this works"

Use another mode when the requested artifact is different:

- "Create a task to document X" is Task Mode because the requested artifact is a task
- "Write a bug report about documentation" is Bug Mode because the requested artifact is a bug report
- "Document bug behavior" is Doc Mode because the subject is a bug but the requested artifact is documentation
- "Write an API reference from this schema" and "create an architecture document" are Doc Mode
- "Create a task to write engineering documentation" remains Task Mode because the requested artifact is a task
- UI feedback or design refinement remains Task Mode unless the user explicitly asks for a document

### Commands

- **Primary command:** `$doc`
- **Short alias:** `$d`
- **Energy override:** `$quick` or `$q` may accompany either Doc command
- **Output:** One markdown product or engineering documentation artifact
- **Thinking:** Rigor scales with the selected energy
- **Interactive behavior:** Ask one consolidated question only when purpose, audience, source authority, scope, or source classification cannot be established safely
- Stopping to ask still produces a file. Export the question in this mode's lane as `export/[###] - {artifact}-[description]-clarification.md`, holding the question and nothing else, so the request is not lost between sessions

Command recognition belongs to the Product Owner router. `$doc` and `$d` are exact, standalone tokens. Strings such as `$document`, `$docs`, `$debug`, or text that merely contains `$d` are not Doc commands.

### Core Rules

- Determine whether the work is creation or refinement before choosing a structure
- Classify material claims before composing them
- Keep current behavior, approved direction, proposal, retired material, and unknown material distinct
- Stop at unresolved contradictions instead of merging plausible claims
- Use the existing document as the structural baseline for refinement
- Preserve supplied technical identifiers, implementation facts, code, architecture, APIs, schemas, data models, debugging procedures, controls, and operational evidence accurately
- Use source-backed HOW when the audience needs it. Label new analysis, recommendations, or designs as proposal until authority establishes a stronger status
- Use the ClickUp Markdown contract for new documents and the source's established style for refinements
- Apply every factuality and conflict gate under Quick energy
- Export and verify the artifact before responding

### ClickUp Output Contract

For every new Doc artifact:

- Use the exact horizontal divider `* * *`. Never substitute `---` inside the deliverable
- Put one blank line between the document title and its first divider. Put the divider on the line immediately after every non-title, non-empty content heading
- Balance heading depth: H1 is the title only. H2 anchors major sections such as the Overview and the primary body section but stays a minority of the document's headings, roughly three or four when a document has ten, because ClickUp renders H2 very large. H3 carries the remaining sections and the subsections under an H2 anchor, H4 carries deeper subsections, and bold paragraph leads replace anything deeper
- Wrap an optional document-wide status or scope blockquote between title-level dividers
- Use `*   ` for unordered bullets and `*   **{Term}** — {Definition}` for compact definitions
- Use `*   [ ]` for document checklists. Keep ordered procedures numbered
- Write every heading in sentence case: capitalize the first word plus proper nouns, acronyms and literal identifiers, and nothing else. `### Boundaries and exceptions`, never `### Boundaries and Exceptions`. The scaffold names in doc-templates.md are already written this way, and a heading a writer invents follows the same rule. This is the Human Voice card's title-case ban, and Doc Mode holds no exemption from it. A refinement keeps the supplied document's own heading case
- Do not end a newly authored or rewritten bullet item with a full stop
- Treat same-level empty spacer headings such as `##   `, `###   ` or `####   ` as a ClickUp rendering affordance: use them only in ClickUp-bound content, never in a file export, where plain blank lines carry the spacing
- A divider needs no blank line after it. Content may open on the line directly below, which is what every ClickUp layout fixture in `assets/examples/doc/` does under its section headings, and a blank line there is equally fine. What the layout does fix is the line above: the divider sits immediately under its heading with nothing between them
- Meet the Readability Floor in doc-templates.md: one idea per paragraph with the takeaway first, links at the end of the sentence or bullet they support, checklist items as short bold imperatives with rationale in the surrounding prose, lists one level deep
- Preserve semantic table, code-fence, blockquote, link, and identifier formatting

This Doc-specific ClickUp contract overrides the generic dash-bullet guidance in SKILL.md's Rules section. Task, Bug, and Interactive artifacts retain their own formatting rules. Refinements retain the supplied document's style unless the user explicitly requests ClickUp normalization.

The exact `*   **Term** — definition` form, the `Status: {class} — {qualifier}` label from the Status language table and preserved source text narrowly override Human Voice Rules' general em-dash ban. The status label earns it because its qualifier routinely carries commas of its own, which a comma delimiter would then hide. Do not extend the exception to newly authored prose outside those two structural shapes.

---

## 2. DOCUMENTATION BOUNDARY

### In Scope

Doc Mode may:

- Explain product, engineering, operational, security, compliance, or mixed-domain purpose, audience, value, behavior, and mechanism
- Organize supplied rules, states, examples, copy, code, identifiers, components, interfaces, schemas, evidence, and cross-references
- Describe approved direction when its not-yet-current status remains explicit
- Preserve or explain source-backed implementation facts, architecture, frameworks, APIs, schemas, data models, configuration, code, root causes, debugging procedures, operational evidence, event names, variables, URL names, and table values
- Surface contradictions, gaps, missing dependencies, and unresolved decisions
- Analyze options, trade-offs, and recommendations for a product or technical proposal while keeping assumptions, evidence, decision ownership, and approval status explicit
- Record legal, compliance, security, architecture, and technical decisions or requirements with their supplied authority and status

### Constraints, Not Topic Exclusions

Engineering and regulated subject matter is not categorically out of scope. Apply these constraints instead:

- A documentation artifact may contain source-backed or illustrative code, configuration, commands, APIs, schemas, data models, architecture, debugging procedures, and operational evidence. A request whose primary deliverable is production code remains implementation work, not Doc Mode
- Technical analysis, selection, or design may be written as a proposal or recommendation. Do not present it as approved or shipped without authority
- Never fabricate system behavior, code behavior, implementation facts, root causes, operational evidence, approvals, or professional sign-off
- Update approved direction to current behavior only when authoritative evidence establishes that the relevant scope shipped
- Correct source defects when the requested refinement includes cleanup. Otherwise preserve them, flag them when relevant, and avoid silent scope expansion
- Legal, compliance, security, and technical questions may be analyzed and documented. Identify the decision owner and evidence. Do not claim external approval or professional authority that was not supplied

When a source contains technical material, preserve and explain it to the depth the audience needs. Attribute current facts, approved decisions, and proposals accurately. New reasoning is allowed in an explicitly labelled proposal or recommendation, with assumptions and verification gaps visible.

This Doc-specific boundary overrides the generic backlog-only instructions that say WHAT not HOW, leave implementation detail to developers, remove implementation detail, or prevent final deliverables from becoming implementation guidance. Those constraints remain active for Task and Bug backlog artifacts. They do not strip source-backed or explicitly proposed technical HOW from an engineering document.

---

## 3. SOURCE CLASSIFICATION

Classify every material claim before synthesis. A file may contain more than one class, so apply classification at section, field, table row, or individual claim level when necessary.

| Class | Meaning | Treatment in the document |
| --- | --- | --- |
| **Current behavior** | Verified active behavior within the authority and scope of the source | May be stated as current only within that verified scope |
| **Approved direction** | Accepted product direction that is not established as shipped behavior | Label as approved or intended and keep it separate from current behavior |
| **Proposal** | Candidate, exploratory, or future-state material not yet approved as fact | Use proposal framing, a prominent status notice, and unresolved decisions |
| **Retired material** | Superseded, historical, legacy, or explicitly retired content | Keep historical context visible, but never let it override active material |
| **Unknown** | Authority or lifecycle status cannot be established safely | Label the uncertainty or ask for authority before making a definitive claim |

### Classification Rules

- Explicit status markers travel with the claims they qualify
- Labels such as `draft`, `new`, `exists, verify`, `not ready`, `proposal`, `legacy`, and `retired` must not be normalized into current behavior
- A present-tense sentence is not proof of current behavior
- A filename containing "canonical" is not enough when the file contradicts itself
- Active-directory placement does not establish every claim in a mixed-status file as current
- A newer timestamp is not a source-authority rule
- Duplicate wording is not independent corroboration
- Missing canonical sources remain missing. Do not reconstruct them from references

---

## 4. SOURCE AUTHORITY AND CONFLICT GATE

### Authority Order

Resolve authority in this order:

1. **Explicit user designation**: the user identifies the source or claim that governs the requested document
2. **Explicit source declaration**: a source states its lifecycle, approval, canonical scope, or relationship to another source
3. **Repository placement**: a clearly named legacy, retired, concept, proposal, or active area provides supporting lifecycle evidence
4. **Corroborating evidence**: independent, compatible sources support the same claim within the same scope

Each authority signal is limited to the scope it actually covers. A source that declares itself authoritative for delivery policy does not automatically govern message identifiers, code behavior, schema ownership, security controls, copy readiness, or unrelated rules.

### Conflict Gate

Before drafting or refining:

1. Compare source claims that cover the same behavior, identifier, state, rule, or status
2. Check whether the authority order establishes a clear winner within that claim's scope
3. If one source clearly wins, use it within scope and retain the weaker source's proposal, retired, or unknown status where relevant
4. If no source clearly wins, stop composition
5. Ask one consolidated question containing every decision needed to continue
6. Wait for the user's answer. Do not choose a winner or answer the question internally

Never settle a conflict through recency alone, filename confidence, directory proximity, majority wording, or duplicate content.

### Consolidated Clarification

Use one prompt, adapted to the known context:

> Before I draft, please confirm the document's purpose and audience, which source should govern each listed conflict, whether the result describes current behavior, approved direction, proposal, retired material, or unknown, and any scope that should be excluded?

List the conflicting claims beneath that single question when specificity helps. Do not ask separate follow-up questions when the user's answer supplies all required decisions.

A promised source does not defer the question. When the request says the notes or sources are still to come, the consolidated question asks for them together with every other unresolved field rather than asking for the source alone and holding the rest for after it arrives. At minimum it covers source set, authority, status, shape and scope, each unless the user has already stated it. Shape stays among those fields until the user states it or the notes arrive, so the turn-1 question asks about it even when the request's wording suggests one, because Step 4 has nothing to route on before then. Asking for the source alone spends the one intake round without settling what the draft still needs.

### When Clarification Is Blocking

Clarification is mandatory when:

- Purpose or audience materially changes what belongs in the document
- The selected source set contains incompatible claims and no scoped authority resolves them
- The request asks the document to make a claim about a subject no supplied source covers. Purpose, audience, source set, authority, conflict review and scope can all be settled while the sources say nothing about the thing being claimed, and a comparison request is where that hides best: it names two subjects, the sources commonly cover one, and the uncovered half would have to be invented. Name the uncovered subject in the same consolidated question and ask for a source or for the subject to be dropped from scope
- An existing duplicate has no declared authoritative version
- Current behavior cannot be distinguished from approved or proposed behavior
- A requested definitive statement depends on unknown material
- The user requests a structural rewrite but has not authorized changing the existing structure

---

## 5. CREATE WORKFLOW

Use this workflow for a new product, engineering, operational, security, compliance, or mixed-domain document.

### Step 1: Establish the Contract

Identify:

- Document purpose
- Primary audience
- Document domain and the depth of product versus technical detail the audience needs
- Requested scope and exclusions
- Supplied source set
- Authority signals for the material claims
- Intended source classification(s): current behavior, approved direction, proposal, retired material, or unknown
- Requested depth or Quick energy

If any missing field makes a definitive document unsafe, use the consolidated clarification and wait.

### Step 2: Classify the Sources

- Classify claims using the five source classes
- Preserve local status markers from mixed files
- Record contradictions, duplicates, missing references, and unsupported claims
- Confirm that any current-behavior statement has authority within scope

### Step 3: Apply the Conflict Gate

- Resolve only conflicts with a clear authority winner
- Keep lower-authority lifecycle status visible where it matters
- Stop and clarify all unresolved conflicts together

### Step 4: Select the Adaptive Shape

Route by the reader's job, first match wins:

```text
Does the reader follow an order or apply a standard?      -> Guide
Does the reader locate and compare repeated entries?      -> Catalog
Does the reader predict states, rules and outcomes?       -> Behavior reference
Does the material describe what might or should change?   -> Proposal
Does the reader need orientation and story?               -> Narrative overview
```

A request that could fit two shapes takes the first match on the reader's PRIMARY job. "Document how our notification states work" reads as prediction, so Behavior reference beats Catalog unless the user asks for a lookup surface.

The routing needs material to route on. When the request promises a source it has not yet supplied, shape counts as unresolved until the user states it or the notes arrive, so the turn-1 consolidated question asks about it, even when the request's wording suggests a shape. The question may name the shape the wording suggests, and that suggestion never replaces the question. Once the notes are present and make the reader's use clear, the routing above picks the shape without a preference question.

Shape detail:

- **Guide** for an ordered process, content standard, implementation guide, runbook, troubleshooting path, or practical instruction
- **Catalog** for stable entries, identifiers, shared fields, APIs, events, schemas, configuration, controls, and cross-references
- **Behavior reference** for product or system states, architecture, components, flows, rules, combinations, boundaries, and outcomes
- **Proposal or future-state document** for candidate product behavior or technical design, principles, alternatives, trade-offs, recommendations, and open decisions
- **Narrative overview** for orientation and story: READMEs, statuses, investigation logs and handovers, written prose-first with sparse structured blocks

Do not force empty sections. Prose is a first-class citizen in every shape: label-bullet blocks serve genuinely enumerable content, never replace explanation. Combine compatible sections or omit optional sections when that improves the document without obscuring status.

### Step 5: Draft Within the Boundary

- Explain WHAT and WHY, plus source-backed HOW when the document and audience require it
- Preserve supplied identifiers, implementation facts, code, configuration, diagrams-as-text, and literal content accurately
- State approval, proposal, retirement, and uncertainty explicitly
- Attribute examples to their source context when their authority is limited
- Put new technical analysis, recommendations, or designs in an explicitly labelled proposal. Never use them to fill current-state gaps silently
- Apply the ClickUp output contract before content validation

### Step 6: Validate and Export

- Run the Doc quality checklist
- Apply Human Voice Rules
- Validate `* * *` divider placement, `*   ` bullets, heading adjacency, absence of generic hyphen bullets and bullet terminal punctuation in the new artifact
- Confirm status labels and conflict decisions survived editing
- Save using the new-document export contract
- Verify the exported file exists before responding

---

## 6. REFINEMENT WORKFLOW

Use this workflow when the user supplies an existing document and asks to update, correct, extend, or improve it.

### Structural Baseline

The existing document, not an adaptive template, is the baseline. Adaptive shapes may guide a new document. They do not authorize reformatting an existing one.

### Fidelity Invariant

Unless the user explicitly places an element in scope, preserve:

- Source filename
- Heading text, hierarchy, and order
- Link labels, destination URLs, and reference definitions
- Identifiers, casing, punctuation, event names, variables, CTA names, YAML keys, and exact URL names
- Tables, column order, row order, and row relationships
- Status notices, verification qualifiers, retirement labels, and proposal disclaimers
- Code fences, quoted copy, whitespace-sensitive formatting, and untouched literal copy
- Divider syntax, unordered-list markers and indentation, same-level spacer headings, and heading-to-divider adjacency
- Existing references to missing files or assets

The requested change should produce the smallest coherent diff. Correct typos, malformed quotes, unmatched tags, missing assets, or legacy identifiers when the requested scope includes cleanup. Otherwise preserve them and flag them when relevant.

### Refinement Steps

1. Read the entire source document and identify the exact requested change
2. Capture the protected structure and literals before editing
3. Classify the existing document and every supplemental source
4. Apply the conflict gate to changed claims
5. Make only the requested change in the source structure
6. Compare the result against the baseline for protected-content drift
7. Export a copy with the original source filename
8. Verify that the supplied source remains unchanged

### Structural Change

Adopt an adaptive shape during refinement only when the user explicitly authorizes a structural rewrite. Even then, preserve protected identifiers, links, literal copy, tables, and status signals unless the requested rewrite specifically changes them.

---

## 7. ADAPTIVE DOCUMENT SHAPES

Templates live in [doc-templates.md](../assets/doc-templates.md). Choose by use, not by source filename.

Every shape honors the Opening Contract and the two-register rule in doc-templates.md Section 2: the first screen tells a no-context reader what the document is, who it serves and whether they need it, and each section holds one register, narrative for understanding or reference for lookup.

### Guide

Use a Guide when the reader needs to follow an order or apply a standard. Typical elements are purpose, audience or prerequisites, ordered steps, component-level rules, examples, checks, and related guidance.

### Catalog

Use a Catalog when the reader needs to locate and compare repeated entries. Typical elements are scope, shared vocabulary, an index, stable identifiers, repeated entry fields, local status, and cross-links.

### Behavior Reference

Use a Behavior reference when the reader needs to understand product or system rules and outcomes. Typical elements are overview, terminology, architecture or context, states, components, flows, implementation mechanisms, combinations, decision rules, boundaries, examples, and unresolved behavior.

### Proposal or Future-State Document

Use a Proposal or future-state document when material describes what might or should change. Typical elements are a prominent status notice, current-state context, desired outcome, candidate behavior or technical design, alternatives, recommendation, trade-offs, dependencies, risks, decision ownership, and open decisions.

The proposal shape must not read like shipped documentation. Product acceptance does not imply implementation, and implementation must not be claimed without evidence.

### Narrative Overview

Use a Narrative overview when the reader needs orientation and story rather than lookup or procedure: a folder README, a project status, an investigation log, a handover, a post-mortem. It is prose-first: a self-sufficient opening that states situation, stakes and current state, then sections ordered by how the reader builds understanding. Structured blocks are sparse and earned. Open items may carry checklists. Status discipline and exact identifiers apply exactly as in every other shape.

---

## 8. QUICK ENERGY

Quick is an energy override, not a document type.

- `$quick $doc …` and `$doc $quick …` both mean Doc intent with Quick energy
- Quick may choose the narrowest useful shape, reduce detail, omit optional sections, and use safe formatting defaults
- Quick does not change current behavior into proposal, or proposal into current behavior
- Quick does not bypass source classification, factuality, status, conflict, or refinement-fidelity gates
- Quick may skip ordinary preference questions only when purpose, audience, source authority, and intended status can be inferred safely
- Quick must still ask the one consolidated question when a blocking conflict or authority gap exists
- A Quick refinement still uses the existing source as its baseline and preserves the original filename

---

## 9. DELIVERY STANDARDS

### Artifact Rules

- Deliver one complete ClickUp-compatible markdown document for new artifacts
- Do not add a generated table of contents unless the user requests one or the source already contains one
- Do not include template instructions, conditional comments, or placeholder text in the final document
- Keep source-status language close to the claims it qualifies
- Preserve links to related product or engineering documentation when supplied
- Use `* * *` dividers, `*   ` unordered bullets, and source-faithful technical fences in new artifacts

### Export Contract

For a new document:

```text
export/[###] - doc-[description].md
```

For a refined document:

```text
export/[original-source-filename].md
```

- Allocate the next available three-digit number for a new document
- Use a short lowercase hyphenated description
- Retain the exact source basename for a refinement
- Never overwrite a supplied reference fixture or source document
- Verify the exported artifact before claiming completion

### Response Contract

In a filesystem-capable runtime, respond with the saved path, a compact quality summary, and a brief 2-3 sentence summary. Do not paste the full exported document into chat.

The compact quality summary is a dimensioned verdict: one line each for Source safety, Shape fit, ClickUp layout, Readability, and Voice, each marked pass or attention. An attention line names the specific item, such as "Layout: attention — two headings missing the trailing divider". The dimensions map onto the Section 10 checklist groups, so the summary reports gate outcomes rather than adding a new gate. Source-safety, conflict, and export failures block delivery regardless of the verdict wording.

In a Claude Project runtime, deliver one markdown artifact and identify the same export-equivalent path in the response. The artifact name and the reported path must follow the same new-versus-refined filename contract.

In either runtime, when ClickUp tooling is available, offer ClickUp delivery as an optional next step and wait for explicit approval. Never push a document or task to ClickUp unsolicited. An approved push follows the `mcp-tooling` ClickUp transport contract: markdown-aware parameters only, never the plain description field.

---

## 10. QUALITY CHECKLIST

### Intake

- [ ] Creation or refinement identified correctly?
- [ ] Purpose, audience, scope, and intended status established?
- [ ] Supplied sources and exclusions recorded?
- [ ] Quick treated as energy rather than artifact intent?

### Source Safety

- [ ] Material claims classified using the five source classes?
- [ ] Mixed-status content classified below file level where needed?
- [ ] Authority applied only within each source's declared scope?
- [ ] Recency and duplication rejected as standalone authority?
- [ ] Conflicts resolved by evidence or held for one consolidated question?
- [ ] Proposal, retired, and unknown material prevented from becoming current fact?

### Content

- [ ] Adaptive shape fits the reader's use?
- [ ] Document explains WHAT and WHY, plus the product or technical HOW its audience needs?
- [ ] Current technical facts are source-backed and new analysis or design remains explicitly proposed?
- [ ] Supplied identifiers, implementation details, code, architecture, APIs, schemas, data models, debugging procedures, and evidence are represented accurately?
- [ ] Status notices remain close to qualified claims?
- [ ] Unsupported gaps remain explicit rather than filled by invention?
- [ ] Legal, compliance, security, and technical recommendations identify their status, evidence, decision owner, and approval gap?
- [ ] The opening screen answers what this is, who it is for, and whether the reader needs it?
- [ ] The chosen shape passes its reader simulation: a Guide audience can complete the process without opening another document, a Catalog reader moves from index to entry and back in one hop, a Behavior reference reader can predict the outcome of a given state and event, no Proposal candidate could be mistaken for shipped behavior on a skim, and a Narrative overview orients a no-context reader by the end of its opening?
- [ ] Procedural steps with source-supplied outcomes carry expected results, and steps without them are marked unverified?
- [ ] Every included optional section satisfies its shape's Include when condition in doc-templates.md?

### ClickUp Layout

- [ ] New artifact uses exact `* * *` dividers rather than `---`? (the output-format gate blocks on this)
- [ ] Every non-title, non-empty content heading is immediately followed by a divider? (the output-format gate blocks on this)
- [ ] Unordered bullets use exact `*   ` syntax and no generic hyphen bullet remains?
- [ ] Definition bullets use `*   **{Term}** — {Definition}` where appropriate?
- [ ] Empty spacer headings appear only in ClickUp-bound content, never in a file export, and never trail a section?
- [ ] Every heading is sentence case, with only proper nouns, acronyms and literal identifiers capitalized mid-heading?
- [ ] The Readability Floor holds: one idea per paragraph with the takeaway first, links at the end of what they support, checklist items short with rationale in prose?
- [ ] Refinement preserves the source layout unless normalization was explicitly authorized?
- [ ] No template scaffold text, `{...}` placeholders, or instruction comments survive in the export?
- [ ] Heading depth is balanced: H2 anchors only the major sections and stays a minority of headings, H3 and H4 carry the rest, bold leads below H4? (the gate blocks on anything deeper than H4, the balance is yours)

### Refinement Fidelity

- [ ] Original filename retained for export?
- [ ] Heading hierarchy and order preserved?
- [ ] Links, identifiers, tables, and untouched literal copy preserved?
- [ ] Proposal disclaimers and lifecycle labels preserved?
- [ ] Unrelated source defects left unchanged and surfaced when relevant?
- [ ] Supplied source verified unchanged after export?

### Delivery

- [ ] Human Voice Rules passed?
- [ ] Source-backed or explicitly proposed HOW is included only to the depth the audience needs?
- [ ] Correct new or refined export path used?
- [ ] Export exists and was verified before response?

---

## 11. CORPUS-GROUNDED EXAMPLES

These examples are routing and safety fixtures. Their repository presence does not establish production truth.

### Barter Creation Material as a Guide Fixture

The Barter creation, copywriting, image, and tone-of-voice documents exhibit a Guide shape: ordered anatomy, per-component rules, examples, and related guidance. Treat their behavior authority as unknown until the user or an explicit source declaration establishes it. If a source references a missing image, preserve the reference and flag the dependency rather than inventing or deleting it.

### Notifications as a Catalog Fixture

The Notification material exhibits a Catalog shape through indexes, stable message IDs, shared vocabulary, template variables, repeated fields, and cross-links. Status can differ by field: markers such as existing, verify, new, draft, and not ready must remain local. If an index and an account file assign different IDs, or duplicate reminder files have no declared winner, apply the conflict gate.

### Feed and Geo Material as Behavior Fixtures

Feed, geo-targeting, and dead-deal material exhibit a Behavior reference shape through product and technical states, architecture, rules, fallbacks, boundaries, and outcomes. Present-tense wording alone does not make these sources current. Contradictory visibility or targeting rules require a scoped authority decision before they can be documented as settled behavior.

### Feed Future Material as Proposal Fixtures

Feed Functions and Weighted Ranking material exhibit a Proposal shape because they describe candidate or future behavior and state that implementation may differ. Keep a prominent proposal notice, separate current context from candidate rules, and preserve open decisions. Their technical ideas may support an engineering proposal or recommendation, but not an approved or shipped architecture without authority.

### Feed ClickUp Layout Fixtures

Dead Deals, Feed Functions, How it Works, and Patterns establish the default new-document layout: exact `* * *` dividers, `*   ` unordered bullets, a blank line between the document title and opening divider, dividers immediately after non-title content headings, same-level empty spacer headings between substantial siblings (a ClickUp-paste affordance that file exports drop), divided status blockquotes, definition bullets with bold terms and em dashes, tables for real matrices, and language-tagged technical fences. Treat those files as read-only formatting fixtures, not as proof that every behavior claim is current. They sit outside the output-format gate's enforced set, so their own em dashes and semicolons are reported as advice rather than failing the run, which is why a source-mode run lists them and still exits 0. That is a reporting level for past corpus text and never a licence to write either mark into a new artifact.

### Retired Notification Material

Conceptual or legacy Notification material can provide historical context when relevant, but its retired status must remain visible. It cannot override a more authoritative active policy or become production fact because its wording is detailed.

### Literal Preservation Fixture

An identifier such as `complated_applications_count` remains exact during unrelated refinement, even if it appears misspelled. Notification IDs, event names, variables, CTA labels, YAML keys, and exact URL names receive the same protection.

---

## 12. ERROR RECOVERY

### Unclear Document Type

Ask one consolidated question that establishes whether the user wants a Guide, Catalog, Behavior reference, Proposal, Narrative overview, or refinement. If the notes are present and make the intended use clear, choose the adaptive shape without adding a preference question. While the source is promised but not yet supplied, shape stays unresolved and the question asks about it.

### Unknown Authority

Do not guess. Label non-definitive content as unknown when a labelled draft is useful, or ask the consolidated question when the user expects a definitive current-state document.

### Contradictory Sources

List the conflicting claims plainly under the consolidated question, ask which source governs each conflict, and wait. Do not produce a blended draft as a workaround.

### Mixed Current and Future Material

Separate it into clearly labelled current, approved, and proposed sections. If status itself is disputed, clarification is blocking.

### Refinement Drift

Restore protected content from the source baseline and reapply only the requested change. If the user wants broader normalization, obtain explicit structural scope first.

### Missing Source or Asset

Preserve the reference, mark the dependency as missing or not supplied, and avoid reconstructing it as current fact. Missing evidence cannot support a product or technical claim. A clearly labelled proposal may state what still needs design or verification.

---

## 13. FINAL REMINDERS

- Classify before composing
- Authority is scoped, not global
- Conflicts stop the draft when no winner is established
- Ask once and wait
- New documents adapt. Refinements preserve
- Quick changes effort, never truth standards
- Keep source-backed HOW distinct from proposals, recommendations, and unknowns
- Use ClickUp dividers and bullets for new documents. Preserve source style for refinements
- Export first and verify the file
---

The kernel points here for the refinement fidelity rule:

6. Preserve source shape when refining an existing task. Preserve the full Doc fidelity invariant (basename, heading text/hierarchy/order, dividers, spacer headings, bullet markers, indentation, links, identifiers, tables, code fences, literal copy and status labels) outside the explicitly requested change.

The kernel points here for the source classification rule:

7. Classify material Doc claims as current behavior, approved direction, proposal, retired material or unknown, at section, row or claim level when a source mixes statuses.

The kernel points here for the source of truth rule:

8. Use the user-provided context as the main source of truth, then the scoped Project Knowledge. Never turn general Knowledge into unrelated product or engineering facts.

The kernel points here for the ClickUp and house format rule:

11. Use ClickUp Markdown for a new Doc (exact `* * *` dividers, `*   ` bullets, `*   **Term** — definition`), the Barter house format for a new PRD (`*   ` bullets, Requirements limited to hard constraints with no checklist and omitted when there are none, a few numbered `1.` outcome-led acceptance criteria each closed with a `- [ ]` Mark-as-done line that no divider separates from the next criterion, a `* * *` section close directly above each `##   ` spacer heading, `- [ ]` used only for the Mark-as-done line and optional readiness or done gates, and a `## Delivery` close only where the requester asked for it or an open question or an undated external constraint forced it), and `-`/`- [ ]` for Task, Bug and Interactive. Never end a newly authored or rewritten bullet item with a full stop. Preserve untouched source punctuation and markers in refinements unless normalization is requested.

The kernel points here for these documentation prohibitions:

1. Never turn a Doc request into unrequested live implementation or claim a documentation artifact is production code.
2. Never present unsupported implementation guidance, code behavior, architecture, APIs, schemas, root causes, debugging evidence or operational evidence as established fact.
3. Never present a technical selection, design, recommendation, or legal, compliance or security analysis as approved, shipped, or externally sanctioned without supplied authority.
4. Never expand scope beyond the request, or invent requirements, evidence, root causes or platform details.

The kernel points here for these source and refinement prohibitions:

10. Never merge contradictory sources silently, never promote approved direction, proposals, retired material or unknown claims into current product behavior, and never treat recency or duplicate bytes as source authority.
11. Never rewrite an existing document's structure, identifiers, links, tables, literal copy or status labels outside requested scope. Never fill a current-state gap with invented technical detail or hide proposal status.

The kernel points here for this new Doc format prohibition:

12. Never emit generic hyphen bullets or `---` dividers in a new Doc artifact.
