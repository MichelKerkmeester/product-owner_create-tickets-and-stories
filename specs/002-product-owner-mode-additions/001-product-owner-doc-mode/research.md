---
title: "Product Owner Doc Mode Research"
description: "Source audit, authority analysis, conflict inventory, and packaging implications for Product Owner Doc Mode."
trigger_phrases:
  - "product owner doc mode"
  - "documentation source authority"
  - "document refinement fidelity"
  - "documentation corpus conflicts"
importance_tier: "high"
contextType: "research"
---

# Product Owner Doc Mode Research

This record preserves the evidence used to specify Doc Mode. It is an analysis artifact, not a declaration that the feature is implemented or that every source describes production behavior.

<!-- SPECKIT_TEMPLATE_SOURCE: research | v1.0 -->

---

<!-- ANCHOR:metadata -->
## 1. METADATA

- **Research ID**: RESEARCH-010
- **Related specification**: [spec.md](spec.md)
- **Status**: Complete for specification authoring
- **Started**: 2026-07-14
- **Completed**: 2026-07-14
- **Supplemental layout and engineering-scope audit**: 2026-07-14
- **Researcher**: Codex
- **Method**: Read-only inspection of the Product Owner package and the supplied documentation corpus
- **Implementation status at research completion**: Not implemented; the packet was implemented and verified afterward

The inspected source corpus remains read-only. No conclusion in this file authorizes edits to Product Owner files, Barter-deal documents, Notification documents, or Feed documents.
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:scope-method -->
## 2. SCOPE AND METHOD

The investigation covered four source groups:

1. The current Product Owner skill, its interactive resources, its CLI-facing guide and sync contract, and its Claude Project package.
2. All eight Markdown files in the Barter-deals folder.
3. All active, conceptual, and legacy Notification Markdown files, plus the conceptual raw-candidate data file.
4. Only the five Feed files named in the specification request.

The audit recorded document structure, raw Markdown layout, explicit status language, directory placement, identifiers, links, duplication, contradictions, packaging versions, and checksum state. It did not infer production truth from a recent timestamp, a canonical-sounding heading, or duplicate wording.

Source authority was evaluated in this order:

1. Explicit authority designated by the user for the current request.
2. Explicit status or authority statements inside a source.
3. Repository placement, including `z_concept` and `z_legacy`.
4. Corroborating evidence from independent sources.

Recency alone does not establish authority. Byte-identical duplicates are one claim repeated, not independent corroboration.

**Primary source roots**:

- `Product Owner/`
- `z — Context/Documentation/Barter deals/`
- `z — Context/Documentation/Notifications/`
- `z — Context/Documentation/Feed/`
<!-- /ANCHOR:scope-method -->

---

<!-- ANCHOR:product-owner-baseline -->
## 3. CURRENT PRODUCT OWNER BASELINE

### Existing capability

The source skill is version `0.2.0` and supports Task, Bug, Interactive, and Quick routing. Task and Bug are artifact intents. Quick is currently represented as a mode and is checked before semantic routing, so adding Doc naively would allow `$quick` to erase the chosen document intent.

The current command detector uses substring-oriented matching. That is insufficient for the requested exact `$doc` and `$d` commands because text such as `$document`, `$docs`, `$debug`, or an incidental `$d` substring could be misclassified.

Existing preservation rules are task-focused. They protect task sections and references, but do not define fidelity for an existing document's heading hierarchy, table relationships, identifiers, literal copy, link labels, URLs, reference definitions, or filename.

No source-authority model or conflict gate exists. The current package cannot distinguish current behavior, approved direction, proposal, retired material, and unknown material before composing a document.

The existing export protocol covers task and bug artifacts only. The user guide is stale relative to the live resources: it names old Task and Bug versions, describes obsolete upload names and context directories, uses `export/[###]-description.md`, and treats Quick as a standalone mode.

### Interactive and package gaps

Interactive Mode `0.402` and Interactive Response Templates `0.100` gather task-or-bug inputs only. Their state and prompt shapes do not ask for document purpose, audience, source authority, current-versus-proposed status, or create-versus-refine intent.

The Claude Project kernel is `0.1.0` and mirrors the same task/bug-only contract. Its knowledge directory currently contains nine mirrored files. Those mirrors are byte-identical to their source counterparts, but the Custom Instructions checksum recorded by the Claude package manifest is stale:

- Recorded SHA-256 prefix: `1d204472b5735899`
- Observed SHA-256 prefix: `b8b2e8ad3bc5d231`

### Sources

- `Product Owner/AGENTS.md`
- `Product Owner/skill/SKILL.md`
- `Product Owner/skill/references/interactive_mode.md`
- `Product Owner/skill/assets/interactive_response_templates.md`
- `Product Owner/README.md`
- `Product Owner/SYNC.md`
- `Product Owner/claude project/Custom Instructions.md`
- `Product Owner/claude project/README.md`
- `Product Owner/claude project/knowledge/`
<!-- /ANCHOR:product-owner-baseline -->

---

<!-- ANCHOR:corpus-inventory -->
## 4. CORPUS INVENTORY

### Barter-deal documents

All eight Markdown files were inspected:

- `z — Context/Documentation/Barter deals/Barter deal - Creation Guide.md`
- `z — Context/Documentation/Barter deals/Barter deal - Copywriting.md`
- `z — Context/Documentation/Barter deals/Barter deal - Geo Targeting.md`
- `z — Context/Documentation/Barter deals/Barter deal - Image(s).md`
- `z — Context/Documentation/Barter deals/Tone of Voice.md`
- `z — Context/Documentation/Barter deals/Tone of Voice - MINISO.md`
- `z — Context/Documentation/Barter deals/Tone of Voice - Moco Museum.md`
- `z — Context/Documentation/Barter deals/Tone of Voice - Storytel.md`

### Active Notification documents

Fourteen active-path Markdown files were inspected:

- `z — Context/Documentation/Notifications/Index-20260708144237.md`
- `z — Context/Documentation/Notifications/Vocabulary-20260708144203.md`
- `z — Context/Documentation/Notifications/Custom Collections-20260707134100.md`
- `z — Context/Documentation/Notifications/Creator/Account-20260706142711.md`
- `z — Context/Documentation/Notifications/Creator/Announcement-20260706142716.md`
- `z — Context/Documentation/Notifications/Creator/Reactionary-20260708144324.md`
- `z — Context/Documentation/Notifications/Creator/Reminder-20260707134018.md`
- `z — Context/Documentation/Notifications/Creator/Reminder-20260708144327.md`
- `z — Context/Documentation/Notifications/Partner/Account-20260706145235.md`
- `z — Context/Documentation/Notifications/Partner/Announcement-20260706145400.md`
- `z — Context/Documentation/Notifications/Partner/Reactionary-20260708143918.md`
- `z — Context/Documentation/Notifications/Partner/Reactivation-20260706150316.md`
- `z — Context/Documentation/Notifications/Partner/Reminder-20260708144029.md`
- `z — Context/Documentation/Notifications/Internal/Email-20260706151845.md`

### Conceptual Notification material

Six conceptual Markdown files and one raw candidate file were inspected:

- `z — Context/Documentation/Notifications/z_concept/README.md`
- `z — Context/Documentation/Notifications/z_concept/Broader Logic.md`
- `z — Context/Documentation/Notifications/z_concept/Channel Pairing Model.md`
- `z — Context/Documentation/Notifications/z_concept/New Notifications.md`
- `z — Context/Documentation/Notifications/z_concept/Proposed additions.md`
- `z — Context/Documentation/Notifications/z_concept/Worked Examples.md`
- `z — Context/Documentation/Notifications/z_concept/candidates-raw.jsonl`

### Legacy Notification material

All six legacy Markdown files were inspected:

- `z — Context/Documentation/Notifications/z_legacy/Emails/Account.md`
- `z — Context/Documentation/Notifications/z_legacy/Emails/Creator.md`
- `z — Context/Documentation/Notifications/z_legacy/Emails/Internal.md`
- `z — Context/Documentation/Notifications/z_legacy/Emails/Partner.md`
- `z — Context/Documentation/Notifications/z_legacy/Mobile (Push).md`
- `z — Context/Documentation/Notifications/z_legacy/SMS.md`

### Named Feed documents

The Feed audit was deliberately limited to these five files:

- `z — Context/Documentation/Feed/Feed - How it Works.md`
- `z — Context/Documentation/Feed/Feed - Dead Deals.md`
- `z — Context/Documentation/Feed/Feed - Patterns.md`
- `z — Context/Documentation/Feed/Feed - Feed Functions.md`
- `z — Context/Documentation/Feed/Feed - Weighted Ranking & Intelligent Discovery.md`

Other Feed files were not used as authority for this packet.
<!-- /ANCHOR:corpus-inventory -->

---

<!-- ANCHOR:source-classification -->
## 5. SOURCE CLASSIFICATION FINDINGS

Doc Mode needs five explicit source classes: current behavior, approved direction, proposal, retired material, and unknown.

| Source or source group | Classification supported by evidence | Reason |
| --- | --- | --- |
| Barter-deal folder | Unknown | The files read as operational guidance, but no inspected source establishes folder-level authority or production verification. |
| Notification Vocabulary | Current behavior within its declared delivery-policy scope | It explicitly says it wins for that policy and states in-app delivery as canonical, with no fallback batching and no partner push. |
| Other active-path Notification files | Mixed; classify per section or field | Markers include `# exists`, `# exists, verify`, `# new`, and `# source export`. Some copy is `DRAFT` and some Figma state is `NOT READY`. |
| Notification `z_concept/README.md`, Broader Logic, Channel Pairing Model, New Notifications, and Worked Examples | Retired material | The concept package explicitly retires these artifacts. |
| Notification `z_concept/Proposed additions.md` | Proposal | It is a future additions backlog, not verified behavior. |
| Notification `z_concept/candidates-raw.jsonl` | Retired exploratory material | It is raw candidate data under the retired concept area. |
| Notification `z_legacy/` | Retired material | Directory placement is explicit lifecycle evidence. |
| Feed - How it Works | Unknown, pending behavior verification | It uses present-tense behavior claims but contains no sufficient authority declaration. |
| Feed - Dead Deals | Unknown, with an internal contradiction | It calls itself canonical, but conflicting visibility statements prevent safe acceptance as a coherent current-behavior source. |
| Feed - Patterns | Unknown; possibly current or approved direction | Its prescribed patterns lack a verified status statement. |
| Feed - Feed Functions | Proposal | It explicitly says it is not final production behavior and implementation might differ. |
| Feed - Weighted Ranking & Intelligent Discovery | Proposal | It defines what the updated system could become and says implementation may differ. |

An active directory is not enough to classify every sentence as current behavior. Status labels, disclaimers, and field-level markers must travel with extracted content.

**Sources**:

- `z — Context/Documentation/Notifications/Vocabulary-20260708144203.md`
- `z — Context/Documentation/Notifications/z_concept/README.md`
- `z — Context/Documentation/Notifications/z_concept/Proposed additions.md`
- `z — Context/Documentation/Notifications/z_legacy/`
- `z — Context/Documentation/Feed/Feed - How it Works.md`
- `z — Context/Documentation/Feed/Feed - Dead Deals.md`
- `z — Context/Documentation/Feed/Feed - Patterns.md`
- `z — Context/Documentation/Feed/Feed - Feed Functions.md`
- `z — Context/Documentation/Feed/Feed - Weighted Ranking & Intelligent Discovery.md`
<!-- /ANCHOR:source-classification -->

---

<!-- ANCHOR:conflict-inventory -->
## 6. CONFLICT AND AMBIGUITY INVENTORY

The corpus proves that a documentation workflow cannot merge plausible-looking sources silently. The following conflicts require a declared winner or one consolidated clarification question.

### Notifications

1. The Notification Index maps creator account items A2 and A3 differently from Creator Account.
2. The Index lists partner account items A5, A6, A7, and A8, while Partner Account defines only A5 reset and A6 payment.
3. Partner Account says payment failure arms M8 Payment Retry, while Partner Reminder defines M8 as Submitted Content Review.
4. The Index lists CR1 without a corresponding source entry.
5. The two Creator Reminder files are byte-identical, with SHA-256 `b3030417f3eaa1666dc1245c1d028e0f4c74a7fd044e3508e74957b69aa124fd`, but neither establishes which filename is authoritative.
6. Retired concept files point to canonical paths that do not exist in the inspected tree.
7. A retired candidate proposes a held push digest, while the active Vocabulary forbids notification rollup.

### Barter deals

8. The Creation Guide includes `Story` as a requirement, while Copywriting and the general Tone of Voice guidance omit it.
9. The Storytel example ends its headline with a full stop despite the stated headline rules.
10. Geo Targeting says home-country rules apply and current location never overrides them. Feed - How it Works introduces a current-coordinate country or fallback rule without a compatible decision order.

### Feed

11. Feed Functions preserves hard filters before weighted scoring. Weighted Ranking argues that scoring should replace near-miss exclusion. Both can be proposals, but they cannot be represented as one settled rule.
12. Patterns requires opt-in before showing broader results. Feed Functions describes a final fallback that automatically drops a rule.
13. Feed - Dead Deals gives contradictory visibility treatment for `REACTIVATION_PENDING`.

### Gate behavior derived from the conflicts

- If one source is explicitly authoritative for the disputed scope, use it and retain the weaker source's status or disclaimer.
- If authority is unclear, stop composition and ask once for the unresolved purpose, audience, source winner, and current-versus-proposed status.
- Do not settle a conflict through chronology, directory proximity, filename confidence, or majority wording.
- Do not convert a proposal, draft, retired artifact, or `exists, verify` marker into a production fact.

**Sources**:

- `z — Context/Documentation/Notifications/Index-20260708144237.md`
- `z — Context/Documentation/Notifications/Creator/Account-20260706142711.md`
- `z — Context/Documentation/Notifications/Creator/Reminder-20260707134018.md`
- `z — Context/Documentation/Notifications/Creator/Reminder-20260708144327.md`
- `z — Context/Documentation/Notifications/Partner/Account-20260706145235.md`
- `z — Context/Documentation/Notifications/Partner/Reminder-20260708144029.md`
- `z — Context/Documentation/Notifications/Vocabulary-20260708144203.md`
- `z — Context/Documentation/Barter deals/Barter deal - Creation Guide.md`
- `z — Context/Documentation/Barter deals/Barter deal - Copywriting.md`
- `z — Context/Documentation/Barter deals/Barter deal - Geo Targeting.md`
- `z — Context/Documentation/Barter deals/Tone of Voice.md`
- `z — Context/Documentation/Barter deals/Tone of Voice - Storytel.md`
- `z — Context/Documentation/Feed/Feed - How it Works.md`
- `z — Context/Documentation/Feed/Feed - Dead Deals.md`
- `z — Context/Documentation/Feed/Feed - Patterns.md`
- `z — Context/Documentation/Feed/Feed - Feed Functions.md`
- `z — Context/Documentation/Feed/Feed - Weighted Ranking & Intelligent Discovery.md`
<!-- /ANCHOR:conflict-inventory -->

---

<!-- ANCHOR:document-shapes -->
## 7. DOCUMENT-SHAPE EVIDENCE

The corpus supports four adaptive shapes. A single universal template would either flatten important structures or force empty sections.

### Guide

The Barter creation material follows a guide pattern: purpose, ordered anatomy, per-component rules, examples, and links to the next relevant guidance. It is the appropriate fixture for testing an instructional document without treating every rule as independently verified production behavior.

**Representative sources**:

- `z — Context/Documentation/Barter deals/Barter deal - Creation Guide.md`
- `z — Context/Documentation/Barter deals/Barter deal - Copywriting.md`
- `z — Context/Documentation/Barter deals/Barter deal - Image(s).md`
- `z — Context/Documentation/Barter deals/Tone of Voice.md`

### Catalog

The Notification set follows a catalog pattern: an index, stable message IDs, a shared vocabulary, repeated entry fields, template variables, delivery rules, and cross-links. Catalog generation must preserve local status markers because one file can mix existing, unverified, new, draft, and exported material.

**Representative sources**:

- `z — Context/Documentation/Notifications/Index-20260708144237.md`
- `z — Context/Documentation/Notifications/Vocabulary-20260708144203.md`
- `z — Context/Documentation/Notifications/Creator/Account-20260706142711.md`
- `z — Context/Documentation/Notifications/Partner/Reminder-20260708144029.md`

### Product-behavior reference

The behavior-oriented documents organize around overview, glossary, states, combinations, rules, examples, boundaries, and outcomes. This shape fits Feed behavior, Geo Targeting, Dead Deals, and engineering-system behavior when authoritative sources establish the technical facts, provided unknown or contradictory claims remain labelled.

**Representative sources**:

- `z — Context/Documentation/Barter deals/Barter deal - Geo Targeting.md`
- `z — Context/Documentation/Feed/Feed - How it Works.md`
- `z — Context/Documentation/Feed/Feed - Dead Deals.md`

### Proposal or future-state document

Proposal material needs a prominent status warning, a current-versus-future split, candidate principles or rules, trade-offs, and unresolved decisions. Architecture or technology choices found in a source may be preserved as supplied proposal content. When requested, Doc Mode may also develop and endorse a recommendation or selection, provided the document keeps its evidence, assumptions, decision owner, approval gap, and proposed or recommended status explicit.

**Representative sources**:

- `z — Context/Documentation/Notifications/z_concept/Proposed additions.md`
- `z — Context/Documentation/Feed/Feed - Feed Functions.md`
- `z — Context/Documentation/Feed/Feed - Weighted Ranking & Intelligent Discovery.md`

### Engineering documentation is subject matter, not a fifth shape

`Feed - How it Works.md` combines a business explanation with exact engineering identifiers, comparison tables, a structural tree, cache values, filtering logic, and language-tagged code fences. `Feed - Feed Functions.md` combines product goals with technical function names, rulesets, formulas, sort fields, and proposal status. The corpus therefore contradicts a categorical engineering-document exclusion.

The safe distinction is authority, not subject matter:

- Doc Mode may create an API guide, schema or event catalog, architecture or code-behavior reference, engineering runbook, or technical proposal when authoritative sources establish the facts and procedures.
- The existing four shapes still apply because they describe how readers use the document.
- Doc Mode may preserve and explain supplied architecture, interfaces, schemas, data flows, implementation behavior, operational commands, and code examples.
- Doc Mode may author code examples, compare technical options, recommend a direction, or record a selection when the requested artifact calls for it and the result stays explicitly proposed or recommended. It must not mutate or execute a production system, fabricate operational evidence or current facts, infer unsupported root causes, or claim approval or professional sign-off that was not supplied.

### ClickUp-native raw Markdown grammar

The four Feed fixtures named by the user were re-read completely as raw artifacts. Their shared grammar is stronger than rendered Markdown equivalence:

- The divider token is `* * *`. Across Dead Deals, Feed Functions, How it Works, and Patterns it appears 56, 117, 33, and 105 times respectively. None uses compact `***` or `---` as its document divider.
- The title is followed by one blank line and then the opening divider.
- An optional one-line status or scope blockquote is enclosed by the opening and closing dividers. Feed Functions and How it Works use this form.
- Every non-empty body heading is followed immediately by `* * *`. Content starts after the divider, not between the heading and divider.
- Unordered list items use `*   ` exactly. None of the four fixtures uses `- ` unordered bullets.
- Compact definition entries use `*   **Term** — definition`, while expanded entries use a bold or code label, adjacent prose or bullets, and `* * *` between entries.
- Heading depth follows topology: H2 for chapters, H3 for features, entities, or surfaces, and H4 for local rules, algorithms, states, components, or numbered steps. The fixtures sometimes skip a level when the visual structure calls for it.
- Empty same-level headings such as `##   `, `###   `, and `####   ` act as vertical spacers between substantial sibling sections. They are not used inside every compact sequence. Bare trailing headings in Dead Deals and Feed Functions are export residue and should not be generated in new documents.
- Tables are used for actual mappings and comparisons. The raw ClickUp separator form is `| ---|`, not the generic scaffold's `| --- |`.
- Fenced blocks retain purpose-specific language tags such as `sql`, `diff`, and `markdown`. Inline identifiers, labels, and links remain at the point where they are explained.

The document types apply the grammar differently:

| Fixture | Structural evidence |
| --- | --- |
| Feed - Dead Deals | H2 chapters, H3 glossary groups, H4 flow steps and local rules; code-labelled states, definition bullets, and one outcome matrix |
| Feed - Feed Functions | Status quote between dividers; H1 chapters, H2 concepts, H3 functions, H4 ruleset/algorithm blocks; adjacent Current/Future/Goal labels |
| Feed - How it Works | Scope quote between dividers; H2 Overview/Features, H3 numbered features, H4 components and function identifiers; tables and technical fences |
| Feed - Patterns | H2 domains, H3 surfaces, H4 patterns and steps; bold module-label blocks divided by `* * *` |

This evidence supports shared layout primitives plus adaptive semantic structure. It does not support copying one outline universally. For refinements, the source document remains the formatting authority unless the user explicitly requests normalization; even a non-ClickUp source must not be silently converted.
<!-- /ANCHOR:document-shapes -->

---

<!-- ANCHOR:fidelity-hazards -->
## 8. SOURCE-FIDELITY HAZARDS

Refinement is riskier than new drafting because seemingly cosmetic cleanup can change meaning or erase evidence.

The following elements must be preserved unless the requested edit explicitly targets them:

- Source filename.
- Heading text, hierarchy, and order.
- Link labels, URLs, and reference definitions.
- Identifiers, including Notification IDs, event names, YAML keys, template variables, CTA names, and exact Feed URL names.
- Identifier casing and punctuation.
- Tables, column order, and row relationships.
- Untouched literal copy and formatting.
- List-marker choice, divider spelling and placement, heading/spacer scheme, table syntax, blockquotes, and fenced-block language tags.
- Status labels, proposal warnings, retirement notices, and verification qualifiers.

Known fixture-specific hazards include:

- Preserve the legacy typo `complated_applications_count` exactly when refining source material.
- The Notification catalog's IDs, events, variables, CTA fields, and YAML-like structures are semantic data, not prose to normalize.
- Brand examples contain literal quoted copy and external links that must remain intact.
- `Barter deal - Image(s).md` refers to a missing `deal-card-types.png` asset. Doc Mode should flag the missing dependency rather than invent an image or delete the reference.
- `Barter deal - Copywriting.md` contains malformed quote formatting around lines 89 and 108 and an unmatched `</u>` around line 141. Refinement must surface these defects instead of silently correcting them outside requested scope.
- Directory placement is lifecycle evidence. Moving retired or conceptual text into an unlabelled current-behavior section would change its status.

**Sources**:

- `z — Context/Documentation/Barter deals/Barter deal - Copywriting.md`
- `z — Context/Documentation/Barter deals/Barter deal - Image(s).md`
- `z — Context/Documentation/Barter deals/Tone of Voice - MINISO.md`
- `z — Context/Documentation/Barter deals/Tone of Voice - Moco Museum.md`
- `z — Context/Documentation/Barter deals/Tone of Voice - Storytel.md`
- `z — Context/Documentation/Notifications/`
- `z — Context/Documentation/Feed/Feed - Feed Functions.md`
<!-- /ANCHOR:fidelity-hazards -->

---

<!-- ANCHOR:routing-implications -->
## 9. ROUTING AND WORKFLOW IMPLICATIONS

Doc must be an artifact intent, while Quick remains an energy override. Product and engineering documentation use the same artifact intent. The evidence supports these routing rules:

- Exact standalone `$doc` and `$d` select Doc intent.
- `$document`, `$docs`, `$debug`, and incidental text containing `$d` do not.
- `$quick $doc ...` and `$doc $quick ...` both resolve to Doc intent with Quick energy.
- `$quick` may reduce length or choose a reasonable shape, but it cannot bypass factuality, authority, conflict, or status gates.
- “Create a task to document X” stays Task intent because the requested artifact is a task.
- “Document how X works” selects Doc intent.
- “Document this API,” “write an architecture reference from these sources,” “explain this data flow,” and “create an engineering runbook from these verified procedures” select Doc intent.
- “Choose an architecture and document the recommendation” is Doc; the resulting direction remains proposed until authority establishes otherwise. “Implement this API” and “debug this live failure” are not converted into Doc requests merely because documentation would be useful afterward.
- “Document bug behavior” selects Doc intent; “write a bug report about documentation” selects Bug intent.
- Explicit bug-report evidence, reproduction steps, and expected-versus-observed framing select Bug.
- UI refinement remains Task unless the user explicitly asks for a Bug artifact.
- Conflicting explicit artifact commands or unresolved multi-artifact wording route to one consolidated clarification question.

Creation needs purpose, audience, source set, authority, and current-versus-proposed status before drafting. Refinement additionally treats the source document as the structural baseline, applies the smallest requested change, preserves the filename, and stops if supplemental sources conflict.

The safety boundary is source- and status-based rather than subject-based. Doc Mode may document verified product and engineering behavior; preserve or explain supplied architecture, interfaces, schemas, data flows, code behavior, operational procedures, and implementation choices; and author technical analysis, examples, recommendations, or selections when they remain visibly proposed or recommended. It must not mutate or execute a production system, fabricate current facts or evidence, infer unsupported root causes, hide approval gaps, or claim external approval or professional sign-off that was not supplied.

**Sources**:

- `Product Owner/skill/SKILL.md`
- `Product Owner/skill/references/interactive_mode.md`
- `Product Owner/skill/references/task_mode.md`
- `Product Owner/skill/references/bug_mode.md`
- `Product Owner/skill/assets/interactive_response_templates.md`
<!-- /ANCHOR:routing-implications -->

---

<!-- ANCHOR:packaging-implications -->
## 10. RESOURCE, VERSION, AND PACKAGING IMPLICATIONS

The smallest coherent release changes the source skill, Doc resources, interactive intake, public guide, export contract, sync inventory, and Claude mirrors together.

| Resource | Current | Planned |
| --- | ---: | ---: |
| `Product Owner/skill/SKILL.md` | 0.2.0 | 0.3.0 |
| `Product Owner/skill/references/doc_mode.md` | Absent | 0.100 |
| `Product Owner/skill/assets/doc_templates.md` | Absent | 0.100 |
| `Product Owner/skill/references/interactive_mode.md` | 0.402 | 0.403 |
| `Product Owner/skill/assets/interactive_response_templates.md` | 0.100 | 0.101 |
| `Product Owner/README.md` | 0.096 | 0.097 |
| `Product Owner/claude project/Custom Instructions.md` | 0.1.0 | 0.2.0, aligned to Skill 0.3.0 |

`Product Owner/AGENTS.md` and `Product Owner/SYNC.md` are unversioned but need contract updates. Task Mode `0.301`, Bug Mode `0.201`, DEPTH `0.201`, Task Templates `0.100`, Bug Report Template `0.100`, and Human Voice Rules `0.210` do not require behavior changes for this feature.

The Claude package should replace the three changed mirrors, add two Doc mirrors, retain the six unchanged mirrors, update its upload inventory, remove stale version filenames, and regenerate every recorded checksum. The resulting knowledge set contains eleven files:

- System Skill `0.3.0`.
- Interactive Mode `0.403`.
- Interactive Response Templates `0.101`.
- New Doc Mode reference `0.100`.
- New Doc Templates asset `0.100`.
- The unchanged DEPTH, Task Mode, Bug Mode, Task Templates, Bug Report Template, and Human Voice Rules mirrors.

The sync direction remains source skill to Claude package under `Product Owner/SYNC.md`. This repository does not provide a derivation script for that package, so parity must be verified by filenames, byte comparison, version references, and checksum-manifest validation.

New documents export to `export/[###] - doc-[description].md`. A refinement exports under the original source filename. Neither workflow overwrites a supplied source fixture. CLI delivery remains export-first; Claude delivery uses an artifact block and reports the same export-equivalent path.

**Sources**:

- `Product Owner/skill/SKILL.md`
- `Product Owner/skill/references/depth_framework.md`
- `Product Owner/skill/references/task_mode.md`
- `Product Owner/skill/references/bug_mode.md`
- `Product Owner/skill/assets/task_templates.md`
- `Product Owner/skill/assets/bug_report_template.md`
- `Product Owner/README.md`
- `Product Owner/SYNC.md`
- `Product Owner/claude project/README.md`
- `Product Owner/claude project/knowledge/`
<!-- /ANCHOR:packaging-implications -->

---

<!-- ANCHOR:recommendation -->
## 11. RECOMMENDATION

Add a dedicated Doc intent rather than stretching Task Mode. A task describes work to be done; a document records sourced product or engineering behavior, guidance, a catalog, or a proposed future state. Keeping those artifacts distinct preserves Task and Bug compatibility and makes “create a task to document X” different from “document X.”

Use one adaptive Doc template asset with four shapes rather than one rigid universal outline. Shape selection should change organization, not truth standards or allowed subject matter: every shape applies the same source classification, status retention, conflict gate, source-safe technical boundary, and refinement-fidelity rules.

Use the Feed fixtures' ClickUp-native grammar for new documents. Share the exact divider, bullet, heading-adjacency, spacer, table, quote, fence, and repeated-entry primitives across the four shapes, then adapt hierarchy to the reader's purpose. Preserve an existing source's grammar during refinement unless normalization is explicitly requested.

Treat the supplied corpus as read-only fixtures. It is valuable because it contains realistic ambiguity, mixed lifecycle states, duplicate material, missing dependencies, malformed copy, stable identifiers, and direct contradictions. Those properties are test inputs for Doc Mode, not defects to repair during specification work.

At research completion, the remaining implementation work was operational rather than conceptual: add the feature to the source and Claude packages, regenerate the Custom Instructions checksum during synchronization, and leave corpus conflicts unresolved until an authority owner answers them. The package and checksum work was subsequently completed; unresolved corpus conflicts remain deliberate Doc Mode gate fixtures.
<!-- /ANCHOR:recommendation -->

---

<!-- ANCHOR:research-boundaries -->
## 12. RESEARCH BOUNDARIES

- This audit does not verify application runtime behavior.
- “Current behavior” appears only where a source explicitly establishes authority for the relevant scope.
- No source document was modified, corrected, renamed, moved, or normalized.
- No architecture, framework, data model, or implementation approach was selected.
- Engineering documentation was analyzed as supported subject matter; this research did not itself choose a product architecture, and it does not treat a documented recommendation as implementation, approval, or professional sign-off.
- Feed conclusions are limited to the five named files; adjacent Feed documents were not used.
- The packet remains a standard Level 3 specification, not a phased parent specification.

Research handoff complete: implementation and verification evidence now lives in [implementation-summary.md](implementation-summary.md). The remaining external action is the documented live claude.ai Project upload and smoke matrix.
<!-- /ANCHOR:research-boundaries -->
