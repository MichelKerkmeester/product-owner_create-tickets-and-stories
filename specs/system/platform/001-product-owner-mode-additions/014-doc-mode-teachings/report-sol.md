I’ll inspect the three teaching sources first, then evaluate Doc Mode and its examples against the extracted mechanisms. The final response will follow the requested report format and remain read-only.
SKILL ROUTING: `sk-doc` is the primary match (0.935 confidence). I’ll use its document-quality lens without invoking an authoring or file-writing workflow.
The teaching sources share a strong pattern: choose the artifact shape before drafting, separate narrative from reference detail, and finish with type-aware checks rather than one generic quality rule. I’m now testing whether Doc Mode already covers those mechanisms or only their surface form.
# Doc Mode Teachings Report — GPT-5.6-Sol

## 1. What the teaching sources actually do (mechanisms, not vibes)

### Source 1: Root `README.md`

**1. Decision-first opening**  
**Location:** `README.md:3-20`  
A two-column value table explains the system's major layers before any setup or architecture detail appears. The following “Reasons to try it” list converts those capabilities into reader outcomes, so a newcomer can decide whether to continue within one screen.

**2. Narrative before system detail**  
**Location:** `README.md:53-67`  
The Overview opens with a concrete problem: AI assistants forget project context. It then introduces the system as the answer before presenting the architecture diagram, which gives the technical detail a reason to exist.

**3. Alternating prose and reference rhythm**  
**Location:** `README.md:207-1262`  
Feature sections move between plain-language explanations, diagrams, short lists, tables and implementation detail. Most sections begin with what the feature does or why it matters, then descend into mechanics and references.

**4. Explicit navigation for a very long document**  
**Location:** `README.md:26-47` and section-level `<!-- ANCHOR:... -->` comments  
The table of contents and paired anchor comments make a 1,500-line document addressable by section. This is effective in this specific repository, although it conflicts with `create-readme` guidance that forbids both mechanisms.

**5. FAQ as objection handling**  
**Location:** `README.md:1414-1461`  
The FAQ answers practical adoption questions in short question-and-answer pairs. It handles likely blockers such as runtime support, optional subsystems and local data behavior without forcing those explanations into the main narrative.

### Source 2: `sk-doc/create-readme`

**1. Artifact-first routing**  
**Location:** `.opencode/skills/sk-doc/create-readme/SKILL.md`, sections 2, 5, 6 and 7  
The workflow chooses among a general README, code-folder README and install guide before drafting. Decision trees also permit “no document” when inline or parent documentation already provides enough orientation.

**2. Evidence-first authoring contract**  
**Location:** `SKILL.md`, sections 3 and 4  
The author must inspect the target folder, nearby documentation, package files, configuration and real commands before writing. Unconfirmed files, metrics, APIs and capabilities are forbidden.

**3. Progressive disclosure with time targets**  
**Location:** `references/readme/types_and_voice.md`, section 3  
The reader gets identity in roughly 10 seconds, relevance in 30 seconds, a working path in two minutes and full reference detail only when needed. This turns “be scannable” into an observable information-ordering rule.

**4. Two-tier voice**  
**Location:** `references/readme/types_and_voice.md`, section 4  
Narrative prose explains purpose and value while reference blocks carry exact parameters, configuration and signatures. The workflow specifies where each register belongs rather than merely asking for a balance between prose and structure.

**5. Conditional section contracts**  
**Location:** `SKILL.md:197-285` and `assets/readme_template.md:46-65`  
Each section has an “include when” condition. Templates are scaffolds to trim, not forms that must be completed, which prevents empty FAQ, troubleshooting or configuration sections.

**6. Executable documentation checks**  
**Location:** `SKILL.md:288-363` and `references/install_guide/quality_and_standards.md`  
Procedural guides pair commands with expected output and validation checkpoints. A failure that would invalidate later steps receives a STOP instruction and troubleshooting path.

### Source 3: `sk-doc/shared`

**1. Type-aware structural enforcement**  
**Location:** `shared/references/core_standards.md` and `shared/assets/template_rules.json`  
Validation changes by document type rather than applying one universal shape. Required, recommended and optional sections carry blocking, warning or informational severity.

**2. Two-stage validation pipeline**  
**Location:** `shared/references/validation.md`, section 2  
`validate_document.py` handles blocking format checks, then `extract_structure.py` produces structured evidence for quality assessment. This separates mechanical validity from editorial judgment.

**3. Transparent DQI scoring**  
**Location:** `shared/references/validation.md`, section 4  
DQI divides quality into Structure, Content and Style with visible point allocation and named quality bands. The score is reproducible and diagnoses where improvement is needed, although some raw metrics reward document size rather than reader success.

**4. Scored Human Voice Rules**  
**Location:** `shared/references/hvr_rules.md`  
Voice is enforced through hard blockers, weighted deductions and a publish threshold. The rules cover punctuation, sentence structure, unsupported claims, inflated language and repetitive AI patterns.

**5. Machine-readable authoring contracts**  
**Location:** `shared/assets/skill_contract.json` and `shared/assets/template_rules.json`  
Required fields, section order, naming, size limits and severity definitions live in structured assets. Validators and authoring guidance can therefore share the same contract instead of depending only on prose.

**6. Evergreen current-state rule**  
**Location:** `shared/references/evergreen_packet_id_rule.md`  
Runtime documentation cites stable feature names, commands and source anchors instead of mutable project-history identifiers. Historical packet information stays in historical records rather than leaking into current-state documentation.

## 2. Gap analysis

### Where Doc Mode is weaker

- **The first screen has no shape-specific success test.** The templates request an Overview, but they do not define what a Guide, Catalog, Behavior reference or Proposal must let the reader understand immediately.
- **“Prose is a first-class citizen” lacks an assembly pattern.** Doc Mode does not specify the useful rhythm found in the teaching sources: takeaway prose, structured evidence and reader consequence.
- **The existing six-dimension scoring is backlog-biased.** `depth-framework.md` measures clarity through acceptance criteria, actionability through concrete steps and mechanism depth through avoiding implementation detail. Those tests do not fit a Catalog, Behavior reference, Narrative overview or source-safe Proposal.
- **Optionality is asserted but not operationalized.** Each Doc template contains many sections, while no per-shape contract identifies the minimum body and exact conditions for including the rest.
- **Procedural verification is underspecified.** A Guide can include commands and operational instructions, but its template does not require expected results or recovery at dependency-sensitive checkpoints.
- **The examples counterteach parts of v0.102.** The Catalog and Proposal examples use five-column tables, while the Behavior example uses three columns. Guide and Proposal checklist items also predate the short bold-imperative Readability Floor.
- **The example set is incomplete.** Five adaptive shapes exist, but only four worked Doc examples are retrievable. Narrative overview has no filled fixture.
- **There is no reader-question closure pass.** FAQ is correctly not mandatory, but the workflow never checks whether likely reader questions were answered somewhere appropriate.

### Where Doc Mode is already stronger

- **Source safety is far stronger.** The teaching sources prohibit invention, but Doc Mode adds five claim classes, scoped authority and a hard conflict hold.
- **Mixed-status handling is stronger.** Doc Mode can safely represent current behavior, approved direction, proposals, retired material and unknowns in one artifact.
- **Refinement fidelity is substantially stronger.** It protects filenames, headings, links, identifiers, tables, literal copy and lifecycle labels while requiring the smallest coherent change.
- **Proposal discipline is stronger.** Decision ownership, evidence gaps, status and approval boundaries are explicit.
- **Artifact adaptation is broader.** Guide, Catalog, Behavior reference, Proposal and Narrative overview cover more reader jobs than README-oriented document types.
- **The ClickUp contract is more exact.** Divider grammar, bullet markers, status blockquotes and export behavior are defined for the real delivery surface.
- **The Readability Floor is more useful than raw style quotas.** It governs paragraph focus, takeaway order, link placement, checklist length and list depth without rewarding document bulk.

## 3. Recommendations for Doc Mode (the core of the report)

### 1. Bring templates and examples into the v0.102 contract

**Target:** `skill/assets/doc-templates.md`, sections 4 through 6, plus all files under `skill/assets/examples/doc/`.

**Change:** Replace the Catalog's five-column index with `Entry | Classification`, using labeled line breaks inside the second cell for category, status and source. Replace Behavior's precedence table with `Conditions | Outcome and authority`, and Proposal's options table with `Option | Assessment`, where the assessment cell contains benefit, cost, evidence and status on separate lines. Rewrite Guide quality checks and Proposal open decisions as short bold imperatives, then update all Doc example versions to v0.102 and sync the corresponding Claude Project knowledge mirrors.

**Why:** Retrieved examples teach behavior more forcefully than abstract rules. The current fixtures violate the two-column limit and partially counterteach the newest Readability Floor.

**Disposition:** Import the teaching sources' contract-to-example alignment, while adapting every table to the Product Owner limit.

**Effort:** Medium.

### 2. Add a first-screen reader contract for every shape

**Target:** `skill/references/doc-mode.md`, section 5 Step 4 and section 7. Mirror the rule in `skill/assets/doc-templates.md`, section 2 and each shape's opening placeholder.

**Change:** Require the first content screen to establish the reader, the job the document supports, the immediate value and the governing status or scope. Define the shape-specific result: a Guide names the outcome and starting condition, a Catalog names what can be found and compared, a Behavior reference names the system boundary and governing model, a Proposal names the decision sought and why it matters now, and a Narrative overview states the situation, stakes and current state.

For Guide and Narrative overview only, permit an optional two-column `Reader need | What this document provides` table when at least three distinct reader outcomes exist. Do not make the table mandatory.

**Why:** This imports the root README's strongest opening mechanism without turning engineering documents into marketing pages. Readers can decide relevance before encountering detailed structure.

**Disposition:** Adapt.

**Effort:** Small.

### 3. Define the narrative-to-reference rhythm

**Target:** `skill/assets/doc-templates.md`, section 2 “Prose Is a First-Class Citizen” and the adaptation notes under all five shapes.

**Change:** Add this section assembly rule: open with a takeaway paragraph, follow with structured evidence only when the content is genuinely comparable or enumerable, then close with the implication, decision or next action when one exists. For mixed audiences, put the narrative explanation before identifiers, tables, code or configuration.

Require each worked example to demonstrate this rhythm at least once. Do not require every section to contain all three parts.

**Why:** This converts an abstract preference for prose into a repeatable writing mechanism. It preserves story while keeping technical reference material easy to scan.

**Disposition:** Import.

**Effort:** Small.

### 4. Add two-column section inclusion contracts

**Target:** `skill/assets/doc-templates.md`, immediately before sections 3 through 7.

**Change:** Add a `Section | Include when` table for each shape. Keep only the Overview and the shape's primary body mandatory, then state exact inclusion conditions for vocabulary, index, prerequisites, precedence, examples, alternatives, risks, chronology, next steps and reading maps.

Use these thresholds:

- Guide checks appear when outcomes are observable.
- Catalog indexes appear when readers need cross-entry navigation or comparison.
- Behavior precedence appears only when rules can interact.
- Proposal alternatives appear only when credible alternatives exist.
- Narrative history appears only when prior events change interpretation of the current state.

**Why:** “Remove optional sections” is too easy for a model to ignore when a large scaffold is present. Include-when contracts resist template completion bias while preserving adaptive structure.

**Disposition:** Import.

**Effort:** Medium.

### 5. Add a Doc-specific interpretation of the existing quality scores

**Target:** `skill/references/doc-mode.md`, section 10. Add one routing sentence to `skill/SKILL.md`, section 3 Test phase, stating that the selected mode defines each score's interpretation.

**Change:** Keep the existing six dimensions and floors, but define their Doc meaning in a two-column table:

- **Completeness:** The reader's job, status, boundaries and material gaps are covered. Optional template sections do not count.
- **Clarity:** The governing answer is findable quickly and mixed statuses remain local to their claims.
- **Actionability:** A Guide can be followed, a Catalog can be searched and compared, a Behavior reference predicts outcomes, a Proposal supports a decision and a Narrative overview orients a newcomer.
- **Accuracy:** Claims carry correct evidence, scope and lifecycle status. A well-labeled unknown does not lower accuracy.
- **Relevance:** Every section serves the reader contract and no padding remains.
- **Mechanism Depth:** The document explains WHY and audience-appropriate HOW without promoting proposals into fact.

State that source-safety, conflict and ClickUp failures block export regardless of score.

**Why:** Doc Mode already has scoring infrastructure. A mode overlay is smaller and safer than importing DQI, and it corrects criteria that currently assume backlog artifacts.

**Disposition:** Adapt.

**Effort:** Medium.

### 6. Add dependency-sensitive verification checkpoints to Guides

**Target:** `skill/assets/doc-templates.md`, section 3 Guide Template and Guide Adaptation Notes. Add a matching item to `skill/references/doc-mode.md`, section 10 Content.

**Change:** When a Guide contains commands, configuration or an ordered procedure, require each dependency-sensitive checkpoint to state the check, expected observable result and recovery or stop condition. Use prose, fenced output or a two-column `Check | Expected result` table.

Only add a stop condition when continuing would cause cascading failure. Every command and expected result must remain source-backed or explicitly labeled as illustrative or proposed.

**Why:** This imports the install-guide packet's most useful operational mechanism without forcing five STOP blocks or an eleven-section document.

**Disposition:** Adapt.

**Effort:** Small.

### 7. Add a reader-question closure pass

**Target:** `skill/references/doc-mode.md`, section 5 Step 6 and section 10. Add a short note to `skill/assets/doc-templates.md`, section 2 Adaptation.

**Change:** During validation, identify two to five questions the intended reader is most likely to ask after reading the opening. Confirm that each answer exists in the main document. Add an FAQ only when several recurring, cross-cutting questions do not fit naturally into the primary sections, and keep each answer to two or three sentences with status or evidence where needed.

**Why:** This imports the root README's FAQ mechanism without making FAQ a default section. It detects missing reader answers that structural checks cannot find.

**Disposition:** Adapt.

**Effort:** Small.

### 8. Add the missing Narrative overview fixture

**Target:** Create `skill/assets/examples/doc/doc-example-narrative-overview.md`, add its worked-example link to `skill/assets/doc-templates.md` section 7 and update the example-count wording in `skill/SKILL.md` section 5. Mirror it as `claude project/knowledge/Product Owner - Examples - Doc - Narrative Overview - v0.102.md` through the existing sync workflow.

**Change:** The example should orient a newcomer within its opening screen, tell a short chronology, state the present condition, identify next actions and end with a reading map. Keep structured blocks sparse, retain local source statuses and use no table wider than two columns.

**Why:** Narrative overview is the shape most dependent on voice and section rhythm, yet it is the only shape without a retrievable example. A separate on-demand fixture keeps the always-loaded template from growing further.

**Disposition:** Import the worked-fixture mechanism.

**Effort:** Medium.

## 4. Small cross-mode suggestions

- **Task Mode:** In `skill/references/task-mode.md` section 4, clarify that DEPTH Actionability means testable outcomes and acceptance signals, not implementation steps. This would prevent the generic scoring language from leaking HOW into backlog tasks.
- **Bug Mode:** In `skill/references/bug-mode.md` section 3, require any diagnostic command or log query to include the expected observable result and the first point where actual behavior diverges. Keep missing evidence as `Not provided`.
- **Story Mode:** No structural import is needed. Its narrative-first contract, tier selection and observable scenarios already capture the strongest teaching mechanisms.

## 5. Do NOT import

- **Do not import README anchor comments or a mandatory table of contents.** They conflict with the ClickUp delivery model, and `create-readme` itself forbids them. The first-screen contract and clear headings provide the useful navigation benefit without hidden markers.
- **Do not import numbered ALL CAPS headings or the blockquote tagline as universal Doc grammar.** They belong to the teaching packet's README house style, not to Product Owner's adaptive ClickUp artifacts.
- **Do not import tables wider than two columns.** Several teaching templates use three to five columns, but those tables become difficult to read in ClickUp and directly violate the Product Owner limit.
- **Do not import DQI unchanged.** Word count, heading count, code-block count and table presence can reward bulk, especially in Catalogs and Proposals. Use the existing six scores with the Doc-specific interpretation instead.
- **Do not import fixed content quotas.** Requirements such as three examples, five troubleshooting entries or five STOP blocks should not apply across all Doc shapes. Include content when the reader job requires it.
- **Do not import the README packet's current-state-only rule.** Doc Mode intentionally and safely supports approved direction, proposals, retired material and unknowns. Its lifecycle model is stronger.
- **Do not import skill frontmatter, version derivation or advisor-routing metadata into generated documents.** Those mechanisms improve the teaching skill's maintainability but add no reader value to ClickUp deliverables and increase dual-package sync cost.
- **Do not import “Reasons to try it” or FAQ as mandatory sections.** Adapt the value-first opening and reader-question check, but avoid marketing language and empty Q&A scaffolds in technical references.
