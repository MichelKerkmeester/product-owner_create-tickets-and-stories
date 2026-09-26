# Product Owner - Assets - Doc Templates - v0.108

The five adaptive ClickUp-native scaffolds a new Doc artifact is copied from, the Guide, Catalog, Behavior reference, Proposal and Narrative overview shapes, plus the layout contract they share and the overlay a refinement uses instead. Refinements preserve the supplied document's existing structure instead of imposing these shapes.

---

## 1. OVERVIEW

### Purpose

Provides five adaptive starting points for product, engineering, or mixed-domain documentation:

- Guide
- Catalog
- Behavior reference, including product or system behavior
- Proposal or future-state document
- Narrative overview, the README-style prose shape for orientation, status and story

### Usage

Use these scaffolds with the Doc Mode document, which holds the wider Doc rules, the authority order, the conflict gate and the quality checklist this file points at. Select the shape by how the audience will use the document, not by whether its subject is product or engineering. Remove optional sections that add no value and retain all source-status qualifications.

Before applying a template:

1. Establish purpose, audience, scope, source authority, and intended status
2. Classify material claims as current behavior, approved direction, proposal, retired material, or unknown
3. Resolve conflicts through the authority order in Templates - Doc Mode
4. Ask one consolidated question and wait if a definitive document would otherwise be unsafe

These templates organize material. They do not establish truth.

---

## 2. SHARED APPLICATION RULES

### ClickUp Markdown Contract

New documents use the same layout grammar as the canonical Feed documentation:

- Use the exact divider line `* * *`; do not substitute `---`
- Put one blank line between the document title and its first divider. Put a divider on the line immediately after every non-title content heading that opens a section or subsection
- Heading depth: H1 is the document title only. Balance the rest of the ladder instead of flattening it. H2 anchors the major sections, Overview included, and stays a minority because ClickUp renders it very large: in a document with around ten headings, three or four H2s is the healthy ceiling. H3 carries the remaining sections and the subsections under an H2 anchor, H4 carries deeper subsections and repeated entries, and a bold paragraph lead replaces anything deeper than H4
- Put a divider between completed content blocks. A divider needs no blank line after it, and a blank line there is equally fine. What is fixed is the line above: the divider sits immediately under its heading with nothing between them
- Empty spacer headings (`##   `, `###   ` or `####   `, matching the level of the section they close) are a ClickUp rendering affordance, not document structure. Use them only when the artifact is being prepared for a ClickUp paste or push. A file export uses plain blank lines instead; in a plain markdown reader a spacer line reads as a broken empty heading
- Wrap a document-wide status notice between the title divider and a second divider
- Use `*   ` for unordered list items. Do not emit hyphen bullets in a document artifact
- Do not end a newly authored or rewritten bullet item with a full stop
- Use `*   **{Term}** — {Definition}` for glossary, shorthand, state, or compact definition lists
- Every heading in a Doc artifact is sentence case, including the scaffold names below. Capitalize the first word and whatever is a proper noun, an acronym or a literal identifier, and nothing else. `### Boundaries and exceptions`, never `### Boundaries and Exceptions`. This is the title-case ban in Rules - Human Voice Core, and Doc Mode holds no exemption from it: the card's only Doc exemptions are the definition delimiter above and the `Status: {class} — {qualifier}` label in the Status language table. A refinement keeps the supplied document's own heading case
- Use `*   [ ]` for checklist items
- Keep ordered procedures as numbered lists
- Keep tables, code fences, blockquotes, links, identifiers, and literal copy in their source-supported form. A phrase the source sets in backticks is literal copy, a rule's own wording as much as an identifier, so it appears word for word in the sentence that states that rule, even where that sentence repeats its bold label, and a shorter label or a When and Then pair never stands in for it

This contract is the default for new documents. A refinement follows the supplied document's established divider, bullet, heading, and spacing style unless the user explicitly requests normalization to the ClickUp standard.

### Prose Is a First-Class Citizen

Every shape may carry full paragraphs. Label-bullet blocks and definition entries exist for genuinely enumerable content: identifiers, repeated fields, matrices. They are never a substitute for explanation. When a section's job is to make the reader understand a situation, a decision or a history, write sentences. A document that reads like a glossary when its reader needed a story has picked the wrong register, whatever its shape.

Every shape mixes two named registers. The narrative register writes full sentences with why before what and owns overviews, rationale, history and current-state storytelling. The reference register writes terse definition bullets, tables, checklists and exact identifiers and owns genuinely enumerable content. Guide and Narrative overview are narrative-dominant. Catalog is reference-dominant. Behavior reference and Proposal mix both. A section switches register, a paragraph never does. A Guide written entirely in the reference register has failed its reader, and so has a Catalog entry that drifts into essay.

### Readability Floor

Structure earns its place only when it makes the document faster to read. Every artifact meets these rules regardless of shape:

- One idea per paragraph, roughly two to five sentences. The moment a paragraph starts covering a second topic, split it
- Open every section and every paragraph with its takeaway, then the supporting detail
- Put evidence and citation links at the end of the sentence or bullet they support. Never chain more than two links inside one sentence, and never interleave link after link mid-sentence
- A checklist item is a short bold imperative lead plus at most two supporting sentences. Longer rationale moves into the prose above the list
- Keep lists one level deep. A bullet that wants sub-bullets is a sign the section wants prose, a table or its own subsection
- The spacer lines shown in the scaffolds below are optional ClickUp affordances, not required output. Omit them in file exports

### Table Patterns

Use a table when the reader compares rows against each other. Use prose or a label-bullet block when the reader reads sequentially. Do not table content whose value lives in the sentences between the items. Three named patterns cover almost every legitimate table in this system:

- **Index** — stable ID beside its entry, the Catalog's navigation surface
- **Options and trade-offs** — each candidate beside its assessment, the Proposal's comparison surface
- **Conditions and outcome** — interacting rules beside their result, the Behavior reference's precedence surface

### Opening Contract

The first screen, meaning the title, the status notice and the opening of the first section, must let a no-context reader answer three questions without scrolling: what is this, who is it for and do they need it. The first paragraph of the document is its takeaway, never its table of contents. Each shape opens with its own result:

- **Guide** — what the reader can do after following it, who follows it and the starting condition
- **Catalog** — what the catalog contains, who consults it and what is explicitly out of scope
- **Behavior reference** — what behavior it explains, the system boundary and why the reader needs to predict it
- **Proposal** — the decision sought, who it affects and why it matters now, before any current-state detail
- **Narrative overview** — the situation, the stakes and the current state, as its self-sufficient-opening rule already requires

### Adaptation

- Use the smallest set of sections that serves the reader
- Each shape's adaptation notes carry a `Section | Include when` table: an optional section earns its place only when its condition holds, and the Overview plus the shape's primary body are the only mandatory sections
- Rename optional headings when the subject needs clearer product language. A Behavior reference keeps its primary body heading as `## Behavior rules` and puts the subject's wording in the `### {Rule, feature or flow}` headings beneath it
- Combine compatible sections rather than leaving empty shells
- Keep status labels beside the claims they qualify
- Do not add a table of contents unless requested
- Do not include these instructions or unused placeholders in the exported document

### Documentation Boundary

- Explain WHAT and WHY in backlog or product material; explain HOW when an engineering document requires verified technical behavior, implementation detail, or an explicitly labelled proposal
- Preserve supplied technical identifiers, code, configuration, architecture, API, schema, data-model, debugging, security, compliance, and operational details when needed for fidelity
- Technical analysis, alternatives, recommendations, examples, or designs may be authored when the document requests them; label unapproved material as proposal or recommendation
- Never fabricate shipped behavior, code behavior, implementation facts, root causes, operational evidence, approvals, or professional sign-off
- Treat legal, compliance, security, and architecture decisions as documentable subject matter. State the decision owner and authority when known; do not impersonate approval that was not supplied

### Status Language

Use the narrowest accurate label:

| Source class | Example label |
| --- | --- |
| Current behavior | `Status: Current behavior — verified for {scope}` |
| Approved direction | `Status: Approved direction — not confirmed as shipped` |
| Proposal | `Status: Proposal — not current product behavior` |
| Retired material | `Status: Retired material — retained for historical context` |
| Unknown | `Status: Unverified — source authority is not established` |

Do not add a document-wide current-behavior label when the sources are mixed. Use section-level or entry-level labels instead.

### Optional Source Basis

Include a compact source basis when readers need to understand authority or lifecycle:

```markdown
> **Source basis**
> *   **Current behavior** — {Source and verified scope}
> *   **Approved direction** — {Source and approval scope}
> *   **Proposal** — {Source and proposal status}
> *   **Retired material** — {Source and reason retained}
> *   **Unknown** — {Claim requiring verification}
```

Omit empty classes. Source basis does not replace local status labels in mixed material.

---

## 3. GUIDE TEMPLATE

Use when readers need an ordered process, practical instruction, or content standard.

Worked example: **Examples - Doc - Guide** shows one writing standard adapted across four distinct empty-state intents, including when no call to action is correct.

```markdown
# {Guide Title}

* * *
> {Status notice when the guide is not wholly verified current behavior. Omit the quote and its closing divider when one is not needed.}
* * *

## Overview
* * *
{What this guide enables, who should use it, and why the outcome matters.}
* * *
###   

### Before you start
* * *
*   **Required context** — {Input, permission, dependency, or verified starting state}
*   **Known limitation** — {Status condition, constraint, or unresolved dependency}
* * *
##   

## Process
* * *
### 1. {Step or Component}
* * *
{What must be true, why it matters, and the verified product or engineering rules that apply.}

*   **{Rule or requirement}** — {Source-supported detail}
*   **{Rule or requirement}** — {Source-supported detail}

**Example**
* * *
{Source-supported example. Preserve literal copy, code, configuration, and identifiers where supplied.}
* * *
###   

### 2. {Step or Component}
* * *
{What must be true, why it matters, and the verified product or engineering rules that apply.}

*   **{Rule or requirement}** — {Source-supported detail}
*   **{Rule or requirement}** — {Source-supported detail}
* * *
###   

### Quality checks
* * *
*   [ ] {Reader-visible, product, or engineering condition}
*   [ ] {Reader-visible, product, or engineering condition}
* * *
###   

### Boundaries and exceptions
* * *
*   **{Exception or limit}** — {Supported scope, fallback, or unknown}
*   **{Dependency or conflict}** — {What readers must not infer around}
* * *
###   

### Related guidance
* * *
*   [{Document title}]({url-or-relative-path})
```

### Guide Adaptation Notes

- Replace `Process` with a domain-specific heading when it improves retrieval
- Use component headings instead of numbered steps for a standard that is not sequential
- Keep examples adjacent to the rules they illustrate
- Do not turn unknown source rules into instructions
- For engineering guides, use source-backed code, configuration, command, API, architecture, troubleshooting, or operational detail when it helps the reader complete the documented work
- When a step carries a command, configuration change or check and the source supplies the outcome, state the expected result beside the step. When the source does not supply it, mark the step unverified rather than inventing a result
- Add a short FAQ block only when the sources show repeated questions or objections: bold question, one to three sentence source-backed answer

| Section | Include when |
| --- | --- |
| Before you start | A prerequisite, permission or known limitation would otherwise surprise the reader |
| Quality checks | Outcomes are observable and someone verifies the finished work |
| Boundaries and exceptions | Real limits or non-goals exist in the source |
| Related guidance | Supplied sources link documents the reader will actually open |

### Source Material Fit

Barter creation, copywriting, image, and tone-of-voice material demonstrates this shape through ordered anatomy, component rules, examples, and related links. Its presence in the supplied material alone does not verify those rules as current product behavior.

---

## 4. CATALOG TEMPLATE

Use when readers need to find and compare repeated entries, stable identifiers, or shared fields.

Worked example: **Examples - Doc - Catalog** shows local status labels preserved across current, approved and proposed entries in one mixed-status catalog.

```markdown
# {Catalog Title}

* * *
> {Document-wide status notice only when one status accurately covers the whole catalog. Omit the quote and its closing divider when one is not needed.}
* * *

## Overview
* * *
{What the catalog contains, who uses it, and what is explicitly outside scope.}
* * *
###   

### Shared vocabulary
* * *
*   **`{Term or identifier}`** — {Source-supported meaning}. {Local status or scope when needed.}
*   **`{Term or identifier}`** — {Source-supported meaning}. {Local status or scope when needed.}
* * *
###   

### Index
* * *

| ID | Entry | Category | Status | Source |
| ---| ---| ---| ---| --- |
| `{Stable ID}` | [{Entry name}](#{entry-anchor}) | {Category} | {Status} | {Source label or link} |
* * *
##   

## {Category}
* * *
### {Stable ID} — {Entry name}
* * *
**Status:** {Current behavior, approved direction, proposal, retired material, or unknown}

*   **Purpose** — {What outcome this entry supports and why}
*   **Trigger or context** — {Verified product or engineering trigger or context}
*   **Audience or actor** — {Recipient, system, role, or user group}
*   **Surface, channel, or interface** — {Supplied value}
*   **Event, endpoint, field, or variable** — `{Exact supplied identifier}`

{Source-supported entry detail, literal copy, code, schema, variables, constraints, or operational notes.}

**Related entries**
* * *
*   [{Stable ID} — {Entry Name}](#{entry-anchor})
* * *
###   

### {Stable ID} — {Entry name}
* * *
{Repeat only the fields that this catalog actually uses.}
* * *
###   

### Catalog boundaries
* * *
*   **{Known scope limit}** — {Effect on use or interpretation}
*   **{Unresolved conflict or missing source}** — {What remains unknown}
* * *
###   

### Sources
* * *
*   [{Source title}]({url-or-relative-path}) — {authority and lifecycle scope}
```

### Catalog Adaptation Notes

- Reuse the source's established field names and field order when they exist
- Keep IDs, casing, punctuation, events, variables, CTA labels, and YAML-like blocks exact
- Put status on each entry or field when a catalog mixes lifecycle states
- Do not create an index mapping when source files disagree about the mapping
- Keep cross-links intact; never replace a missing canonical entry with an inferred one
- Prefer divided label blocks for repeated entries; reserve tables for real comparisons, mappings, or dense indexes
- Engineering catalogs may cover APIs, endpoints, events, schemas, data fields, configuration, services, jobs, controls, or operational signals

| Section | Include when |
| --- | --- |
| Shared vocabulary | Entries reuse terms a reader could misread |
| Index | Readers need cross-entry navigation or comparison |
| Catalog boundaries | Something adjacent could be mistaken as in scope |
| Sources | Authority or lifecycle needs a compact record |

### Source Material Fit

The Notification corpus demonstrates this shape through indexes, message IDs, vocabulary, repeated fields, variables, and cross-links. It also demonstrates why local status and the conflict gate matter: active-path material may mix existing, verify, new, draft, and not-ready markers, while duplicate or incompatible IDs do not establish a safe winner.

---

## 5. BEHAVIOR REFERENCE TEMPLATE

Use when readers need to understand product or system states, rules, flows, components, combinations, boundaries, and outcomes.

Worked example: **Examples - Doc - Behavior Reference** shows a state machine with timing, offline behavior, precedence and one unresolved edge kept outside settled rules. A longer, system-scale behavior reference lives in **Examples - Doc - How It Works**: a subscription billing lifecycle explained through its states, renewal and proration, dunning retries, cancellation and precedence.

````markdown
# {Behavior Reference Title}

* * *
> {Status notice, including the verified scope or unverified limitation. Omit the quote and its closing divider when one is not needed.}
* * *

## Overview
* * *
{What product or system behavior this reference explains, who needs it, and why it matters.}
* * *
###   

### Glossary
* * *
#### Terms and states
* * *
*   **`{Exact term or state}`** — {Source-supported definition}. {Local status when needed.}
*   **`{Exact term or state}`** — {Source-supported definition}. {Local status when needed.}
* * *
###   

### Structure or context
* * *
{Explain the actors, components, boundaries, or request flow. Use a table or fenced tree only when it makes the relationship clearer.}

```{language}
{Source-supported structure, flow, formula, code, configuration, or schema excerpt}
```
* * *
###   

### States and components
* * *
`{EXACT_IDENTIFIER}`
*   {Meaning or role}
*   {Verified behavior, implementation fact, or visible outcome}
*   **Status** — {Current behavior, approved direction, proposal, retired material, or unknown}
* * *
`{EXACT_IDENTIFIER}`
*   {Meaning or role}
*   {Verified behavior, implementation fact, or visible outcome}
* * *
##   

## Behavior rules
* * *
### {Rule, feature or flow}
* * *
**1. {Rule or Step Name}**
* * *
{Source-supported condition, mechanism, and outcome.}

*   **When** — {Source-supported condition}
*   **Then** — {Source-supported product or system outcome}
*   **How** — {Verified technical behavior when relevant}
*   **Why** — {User, business, engineering, operational, security, or compliance reason when supported}
*   **Status** — {Current behavior, approved direction, proposal, retired material, or unknown}
* * *

**2. {Rule or Step Name}**
* * *
{Source-supported condition, mechanism, and outcome.}
* * *
##   

## Combinations and precedence
* * *

| Conditions | Outcome | Authority or status |
| ---| ---| --- |
| {Condition combination} | {Verified outcome} | {Source and class} |
* * *
###   

### Examples
* * *
#### {Example name}
* * *
*   **Given** — {Supported starting context}
*   **When** — {Product or system event, command, request, or condition}
*   **Then** — {Supported product, system, or operational outcome}
* * *
###   

### Boundaries and exceptions
* * *
*   **{Boundary or exception}** — {Known fallback, empty state, permission limit, failure mode, or constraint}
*   **{Unknown behavior}** — {What remains unresolved and why}
* * *
###   

### Related references
* * *
*   [{Document title}]({url-or-relative-path})
````

### Behavior Reference Adaptation Notes

- Omit `Combinations and precedence` only when rules cannot interact
- Use source terminology rather than normalizing state names
- Do not invent precedence to reconcile incompatible rules
- Keep contradictory behavior outside the settled rules and apply the conflict gate in Templates - Doc Mode
- Include verified implementation mechanisms when the engineering audience needs them
- Use explicit proposal labels for inferred designs, recommendations, troubleshooting paths, or architecture not established as current

| Section | Include when |
| --- | --- |
| Glossary | Terms or states carry non-obvious meaning |
| Structure or context | Architecture places the rules for the reader |
| Combinations and precedence | Rules can interact |
| Examples | A worked case makes prediction faster |
| Boundaries and exceptions | Unresolved or out-of-scope behavior exists |
| Related references | Cross-links exist that the reader will open |

### Source Material Fit

Feed behavior, geo-targeting, and dead-deal material demonstrates this shape through states, filtering or targeting rules, fallbacks, and outcomes. Treat present-tense wording as unverified unless authority is established. Incompatible country precedence or state visibility cannot be represented as one settled rule without a source decision.

---

## 6. PROPOSAL OR FUTURE-STATE TEMPLATE

Use when sources describe candidate behavior, a desired future state, or approved direction that is not confirmed as shipped.

Worked example: **Examples - Doc - Proposal** shows verified current context separated from candidate design while the recommendation owner and evidence gap remain open.

```markdown
# {Proposal Title}

* * *
> **Status: {Proposal or approved direction}**
> This document describes {candidate or approved} product or engineering behavior. It is not evidence of current implementation. {Add the decision or verification needed before status can change.}
* * *

## Overview
* * *
{What problem or opportunity prompted the document, who it affects, and why it matters.}
* * *
###   

### Current state
* * *
{Only verified current product or engineering behavior relevant to the proposal. Label unknowns explicitly.}
* * *
###   

### Desired outcome
* * *
{The user, business, engineering, operational, security, or compliance outcome the future state should create.}
* * *
##   

## Proposed behavior or design
* * *
### {Capability, component, rule or decision}
* * *
{What could or should change, for whom, how it could work when technical detail is required, and why.}

*   **Candidate condition or input** — {Product or technical condition}
*   **Candidate behavior or design** — {Proposed outcome, mechanism, interface, schema, architecture, or control}
*   **Evidence or rationale** — {Source, analysis, constraint, or trade-off}
*   **Status** — {Proposed, recommended, or approved direction}
* * *
###   

### {Capability, component, rule or decision}
* * *
{Repeat the smallest useful proposal block.}
* * *
###   

### Principles and constraints
* * *
*   **{Principle or non-negotiable outcome}** — {Why it governs the proposal}
*   **{Known constraint}** — {Product, technical, operational, legal, compliance, security, or delivery impact}
* * *
###   

### Options and trade-offs
* * *

| Option or direction | Benefit | Cost or risk | Evidence | Status |
| ---| ---| ---| ---| --- |
| {Candidate direction} | {Benefit} | {Cost or risk} | {Evidence or assumption} | {Proposed, recommended, approved, or unknown} |
* * *
##   

## Recommendation or decision
* * *
{State the recommendation, recorded decision, decision owner, and authority. If no decision exists, say what evidence or owner is still required.}
* * *
###   

### Dependencies and risks
* * *
*   **{Dependency}** — {Product, technical, evidence, policy, or delivery dependency}
*   **{Risk}** — {Risk to users, business, implementation, operations, security, compliance, or source confidence}
* * *
##   

## Open decisions
* * *
*   [ ] {Decision that must be made, by whom or against what evidence when known}
* * *
###   

### Out of scope
* * *
*   {Excluded behavior or decision}
* * *
###   

### Source basis
* * *
*   [{Source title}]({url-or-relative-path}) — {proposal, approved direction, current behavior, retired material, or unknown scope}
```

### Proposal Adaptation Notes

- Keep the status notice immediately below the title
- Separate verified current context from candidate future behavior
- Replace `Proposal` with `Approved direction` only when authority establishes approval
- Do not claim that approved behavior is implemented
- Preserve supplied technical alternatives as attributed source content
- When the user requests analysis, design, selection, or recommendation, develop it in the proposal and keep its status, assumptions, evidence, trade-offs, decision owner, and approval gap explicit
- Architecture, API, schema, data-model, implementation, debugging, operational, security, compliance, and code-level material may appear when relevant to the proposal
- Keep unresolved decisions visible instead of completing them with assumptions

| Section | Include when |
| --- | --- |
| Current state | Verified behavior the proposal would change exists |
| Principles and constraints | Non-negotiables genuinely shape the design |
| Options and trade-offs | Credible alternatives exist |
| Dependencies and risks | Known blockers or hazards exist |
| Open decisions | Decisions remain with named owners |
| Out of scope | Adjacent work could be assumed in |
| Source basis | Mixed authority needs a compact record |

### Source Material Fit

Feed Functions, Weighted Ranking, and proposed Notification additions demonstrate this shape through candidate rules, future-state language, trade-offs, and open decisions. They remain proposal material unless a user or authoritative source establishes a different status. Technical content may support an engineering proposal, but it does not establish that the proposed architecture is approved or shipped.

---

## 7. NARRATIVE OVERVIEW TEMPLATE

Use when the reader needs orientation and story rather than lookup or procedure: a folder README, a project status, an investigation log, a handover, a post-mortem. This is the prose-first shape; its structured blocks are sparse and earned.

Worked example: **Examples - Doc - README** shows a working-folder README that orients a newcomer in one screen, earns its reading map and keeps one open question visible.

```markdown
# {Document Title}

* * *
> {Status notice when the material is not wholly verified current behavior. Omit when it is.}
* * *

{Two to four paragraphs of real prose: what this is, why it exists, who it serves and
where things stand right now. A reader with no context should understand the situation
from this opening alone. Exact identifiers, filenames and values stay in backticks.}
##   

## {How we got here}
* * *
{Narrative paragraphs. Dates, decisions, dead ends and turning points in flowing prose,
in the order they happened. Bullets appear only for genuinely enumerable lists.}
##   

## {Where things stand}
* * *
{The present state in prose. A short label-bullet block or a small table appears ONLY
where a genuine matrix beats sentences.}

*   **{Settled point}** — {one line, only when a compact enumeration genuinely helps}
##   

## {What happens next}
* * *
{Concrete next steps or open questions in prose, with owners and gates when known.}

*   [ ] {Actionable open item}
*   [ ] {Actionable open item}
###   

### {Reading map}
* * *
{Optional. When the document orients a folder or a set of documents, say what to read
in what order and why, one line of prose per entry.}

*   [{Document}]({relative-path}) — {why the reader would open it}
```

### Narrative Overview Adaptation Notes

- Rename every heading to fit the actual story; the scaffold names are placeholders, not a contract
- Keep the opening self-sufficient: situation, stakes and state before any section break
- Convert inherited bullet lists into sentences unless the content is genuinely enumerable
- Status discipline still applies: unverified claims carry their notice, and identifiers stay exact
- Chronology beats taxonomy: order sections by how the reader builds understanding, not by category
- Use at most one analogy per concept, placed after the technical statement, and drop it when plain language is already clear
- This shape carries more voice personality than the others: react to facts, acknowledge trade-offs and name specifics rather than abstract labels, without loosening status discipline or identifier accuracy
- Add a short FAQ block only when the sources show repeated questions or objections: bold question, one to three sentence source-backed answer

| Section | Include when |
| --- | --- |
| How we got here | Prior events change how the present reads |
| What happens next | Open items or a forward path exist |
| Reading map | The folder or document set has an intended open order |

### Source Material Fit

A working folder's read-me-first document demonstrates this shape: current state up top in prose, a reading order with one-line reasons, history referenced rather than repeated. Its value is that a newcomer is oriented in one screen, which no label-bullet glossary achieves.

---

## 8. QUICK DOCUMENT ADAPTATION

Quick uses the same five shapes with less optional detail.

Worked example: **Examples - Doc - Quick** shows a Quick Guide dropping optional sections while the status notice, an explicitly unverified step and the full ClickUp contract survive.

### Quick Guide

- Keep Purpose, the ordered Process or component rules, and essential Boundaries
- Use one source-supported example only when it prevents ambiguity
- Omit optional audience or related-guidance sections when already obvious

### Quick Catalog

- Keep Purpose and Scope, the Index, and only the requested entry fields
- Preserve entry-level status and exact identifiers
- Do not compress conflicting entries into one row

### Quick Behavior Reference

- Keep Overview, Terminology when needed, Behavior rules and Boundaries
- Include precedence only when established by the sources
- Keep unknown and proposal status visible

### Quick Proposal

- Keep the status notice, Context, Desired outcome, Proposed behavior or design and Open decisions
- Keep current-state claims only when verified
- Do not remove trade-offs when their omission would make the direction misleading

Quick may reduce length. It cannot reduce factuality, source classification, conflict handling, status visibility, domain-appropriate detail, ClickUp layout compliance, or refinement fidelity.

---

## 9. REFINEMENT OVERLAY

Do not copy a new-document template over an existing document during refinement.

### Apply the Existing Structure

1. Preserve the original basename for export
2. Preserve heading text, hierarchy, and order
3. Preserve links, identifiers, tables, literal copy, and lifecycle notices outside the requested change
4. Insert or revise content in the source's established style, including divider syntax, bullet markers, heading depth, spacer headings, tables, and code fences
5. Use the smallest coherent change
6. Compare the exported result with the source baseline
7. Verify that the supplied source was not overwritten

If the user explicitly requests ClickUp normalization, apply the shared ClickUp contract to the authorized scope. Do not silently normalize a non-ClickUp refinement.

### Protected Literal Examples

- Keep `complated_applications_count` exact during an unrelated edit
- Keep Notification IDs, event names, variables, CTA labels, and YAML keys exact
- Keep exact Feed URL names and link targets exact
- Preserve proposal warnings and retired labels
- Preserve a missing-asset link and flag it rather than deleting or replacing it
- Flag malformed quotes or tags when correction is outside scope; correct them when the requested refinement explicitly includes source cleanup

---

## 10. SOURCE-CONFLICT HOLD TEMPLATE

This is an intake response, not a document artifact, so it uses the dash-bullet intake grammar of System - Interactive Mode rather than the ClickUp document contract. Use it only when the conflict gate blocks safe composition.

```markdown
Before I draft, please confirm the document's purpose and audience, which source should govern each conflict below, whether the result describes current behavior, approved direction, proposal, retired material, or unknown, and any scope that should be excluded?

- **{Conflict topic}:** `{Source A}` says {claim A}; `{Source B}` says {claim B}
- **{Authority gap}:** {Source or claim has no established lifecycle or governing scope}
- **{Duplicate}:** {Files match or overlap, but neither is declared authoritative}
```

Ask this once and wait. Do not attach a speculative draft.

---

## 11. TEMPLATE QUALITY CHECK

Before export, confirm:

- [ ] The shape matches how the audience will use the document
- [ ] Empty and irrelevant optional sections were removed
- [ ] Every material claim retains its source class
- [ ] Authority is applied only within declared scope
- [ ] Unresolved conflicts triggered one consolidated question rather than a blended draft
- [ ] Current, approved, proposed, retired, and unknown material remain distinguishable
- [ ] WHAT and WHY are clear; source-backed or explicitly proposed HOW is included when the audience needs it
- [ ] Technical behavior, architecture, code, schema, data-model, debugging, operational, legal, compliance, and security claims carry accurate evidence and status
- [ ] New documents use `* * *` dividers and `*   ` bullets; refinements preserve the source style unless normalization was requested
- [ ] Every heading is sentence case, with only proper nouns, acronyms and literal identifiers capitalized mid-heading
- [ ] Readability Floor holds: one idea per paragraph, takeaway-first sections, links at the end of what they support, checklist items short with rationale in prose
- [ ] The opening screen meets the Opening Contract for the chosen shape
- [ ] Each section holds one register, narrative or reference, and no section reads like a glossary when its reader needed a story
- [ ] The chosen shape's reader-simulation question in the Templates - Doc Mode quality checklist passes
- [ ] Every included optional section satisfies its Include when condition, and no mandatory section is missing
- [ ] A file export contains no empty spacer headings; they appear only in ClickUp-bound content
- [ ] No shipped fact, implementation behavior, root cause, evidence, approval, or sign-off was fabricated
- [ ] Supplied identifiers and literal content remain exact
- [ ] A refinement preserves its original structure and basename
- [ ] The export path follows the new-versus-refined Doc contract
- [ ] No template notes, comments, or placeholders remain in the deliverable

---

## 12. EXPORT REMINDER

New document:

```text
export/[###] - doc-[description].md
```

Refined document:

```text
export/[original-source-filename].md
```

Never overwrite the source fixture. Validate, render the Deliverable Block, re-read the rendered block, then report the export-equivalent path and a compact quality summary. This runtime writes no file, so there is nothing to verify on disk.
