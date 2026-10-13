I'll start by exploring the directory structures of both the teaching sources and the system under improvement, then read everything systematically.
Let me explore the subdirectories and read the key files in parallel.
Now let me read the shared references (the quality backbone), the create-readme reference groups, and explore the Product Owner skill structure.
Now the critical files. Let me read the main Doc Mode files and the create-readme reference details.
Now the second main-focus file plus supporting materials. Let me read doc-templates.md, the examples directory, and the SKILL.md.
Let me read one doc example to see actual output, the README template scaffold, and the Product Owner's own HVR reference to complete my picture.
Let me read the tail of SKILL.md (quality dimensions, escalate section) and skim the cross-mode references briefly.
I have read all three teaching sources (the README exemplar, the create-readme workflow packet with all its references and templates, and the shared quality backbone including HVR, DQI, validation, and core standards) and the full Doc Mode system (doc-mode.md v0.102, doc-templates.md v0.102, the SKILL.md router, the guide example, the Product Owner's own HVR, and skimmed the cross-mode references). Here is my report.

---

# Doc Mode Teachings Report — glm-5.2

## 1. What the teaching sources actually do (mechanisms, not vibes)

### Source A: README.md (tone and structure exemplar)

**A1. Value-first opener before any prose.** The file opens with a 2-column "Core layer / What it adds" table, then a "Reasons to try it" badge-and-bullet block, all before the first `---`. A reader gets the product's entire value proposition in under 10 seconds without reading a sentence of narrative. (`README.md:3-22`)

**A2. Anchor-comment section navigation.** Every major section is wrapped in `<!-- ANCHOR:... -->` / `<!-- /ANCHOR:... -->` pairs and a Table of Contents links to them. This is a maintainable, machine-readable section map that the TOC and tooling both consume. (`README.md:26-47`, `49-118`, etc.)

**A3. Narrative prose carries the story between scannable blocks.** The Overview opens "AI coding assistants have amnesia. Every session starts from zero." (README.md:57). Argumentative, voiced prose sits between dense reference tables and ASCII diagrams. The file never degrades into a pure bullet glossary, even though it is packed with tables and code blocks.

**A4. Section rhythm via dividers and `&nbsp;` spacers.** H2 sections separate with `---`, and `&nbsp;` lines create breathing room before heavy blocks (README.md:51, 228, 247, etc.). The rhythm is consistent: heading, divider, prose lead-in, structured detail, spacer, next heading.

**A5. FAQ as a real closing section.** A dedicated FAQ answers the questions an evaluator actually asks, in short Q/A form, rather than burying them in prose.

### Source B: create-readme/ (README-authoring workflow packet)

**B1. Read-evidence-first mandate with a never-invent list.** SKILL.md §3 step 1 and §4 step 3 forbid inventing "commands, files, APIs, metrics, features or capabilities." The workflow reads the target folder, package files and config before drafting. This is a no-fabrication rule scoped to the authoring task. (`create-readme/SKILL.md:168`, `182`)

**B2. Progressive disclosure as an explicit staging model.** `types_and_voice.md` §3 names four time-boxed stages: title+tagline (10s), overview (30s), quick start (2min), full docs (as needed). Each stage answers a different reader question. This is a concrete opener contract, not a vague "be scannable." (`references/readme/types_and_voice.md:50-61`)

**B3. Two-tier voice named and assigned to sections.** `types_and_voice.md` §4 splits narrative tier (explain what/why, analogies, plain language, active voice) from reference tier (terse parameter tables, config, tool signatures). It names which sections use which: narrative in Overview/Quick Start/Features-3.1, reference in Features-3.2/Configuration/Related Documents. (`types_and_voice.md:65-86`)

**B4. Per-section output quality contract.** `quality_and_checklist.md` §3 has a table mapping each section to concrete requirements: Overview needs "2-3 sentence description + at least one table," Quick Start needs "numbered steps, copy-paste commands, verification command," Features needs "grouped by category, usage examples." These verify the output itself, not the process. (`quality_and_checklist.md:44-58`)

**B5. Decision trees for type and install-guide selection.** SKILL.md §2 ships ASCII decision trees: "Is this a project root? YES → general README; NO → is it a reusable component?..." and the install-guide tree. These are deterministic tiebreakers that reduce selection errors. (`create-readme/SKILL.md:142-160`)

**B6. Template-as-scaffold, never-as-placeholder.** §4 step 10 and §9 "Never" mandate removing unused sections instead of leaving placeholders, and the pre-publish checklist enforces "no `[PLACEHOLDER]` markers." (`SKILL.md:190`, `431-434`)

### Source C: shared/ (cross-packet quality backbone)

**C1. Document Quality Index (DQI): deterministic 0-100 score.** `validation.md` §4 computes a score from Structure (40: checklist pass rate), Content (30: word count, heading density, code examples, tables, links) and Style (30: H2 format, dividers, intro paragraph). Bands: Excellent 90-100, Good 75-89, Acceptable 60-74, Needs Work <60. Every point is measurable, not subjective. (`shared/references/validation.md:178-247`)

**C2. HVR point-penalty scoring model.** `hvr_rules.md` scores from 100 with hard blockers (-5), soft deductions (-2/-1), a first-match-wins precedence model, and pass thresholds (85+ publish-ready, 70-84 needs revision, <70 failing). This turns voice rules into a countable score. (`shared/references/hvr_rules.md:36-46`, `429-440`)

**C3. Document-type detection and per-type enforcement levels.** `core_standards.md` §3 detects type by filename/path priority and assigns enforcement: SKILL is Strict (blocks on missing frontmatter/sections), README is Flexible, Spec is Loose. Structural violations split into safe auto-fixes (filename, H2 case, missing separator) and blocking ones (missing required sections, wrong order). (`core_standards.md:56-87`, `97-153`)

**C4. Named table patterns with placement guidance.** `writing_patterns.md` §5 gives five concrete table shapes: "How This Compares" (capability comparison in Overview), "Key Statistics" (metrics at a glance), "Key Features," "Before/After," "Parameter" (reference tier). Each says where it goes and what it carries. (`references/readme/writing_patterns.md:124-171`)

**C5. Two-stage validation pipeline with runnable gates.** `validation.md` §2 pairs `validate_document.py` (format gate, exit 0 required) with `extract_structure.py` (structure extraction + DQI). The first is a hard blocker; the second feeds AI assessment. (`validation.md:42-92`)

**C6. Analogy budget and voice-personality rules.** HVR §4 and writing_patterns §4 cap analogies ("one per concept," "max 2 'Think of it as/like' per document," "place after the technical statement") and hvr §5 demands personality (have opinions, acknowledge complexity, emotional specificity). These prevent both analogy-slop and voiceless correctness. (`hvr_rules.md:166-176`, `299-328`; `writing_patterns.md:107-122`)

---

## 2. Gap analysis

### Where Doc Mode is already stronger (do not touch these)

**Source safety architecture.** Doc Mode's five source classes, scoped authority order, and conflict-hold gate (doc-mode.md §3-4) are far more rigorous than create-readme's "read evidence first, never invent." create-readme has no concept of mixed-status files, no conflict arbitration, no lifecycle labeling. This is Doc Mode's clearest advantage and the teaching sources have nothing comparable.

**Refinement fidelity invariant.** Doc Mode's refinement workflow (doc-mode.md §6, doc-templates.md §9) preserves filename, heading hierarchy, links, identifiers, tables, literal copy, dividers and status markers outside the requested change. create-readme writes "current-state only" documents and never edits existing structure at this fidelity. Doc Mode solves the harder problem.

**Status discipline.** Source-status labels that travel with claims and the "do not add a document-wide current-behavior label when sources are mixed" rule (doc-templates.md §2) have no equivalent in the teaching sources.

**Prose-as-first-class-citizen guard.** doc-templates.md §2's explicit rule that "label-bullet blocks exist for genuinely enumerable content, never as a substitute for explanation" is stronger than anything in create-readme, which assumes READMEs are table-heavy by default.

**ClickUp output grammar.** The `* * *` divider + `*   ` bullet + spacer-heading contract is a real, checkable output grammar. create-readme's style guidance is softer.

### Where Doc Mode is weaker (real gaps)

**No concrete opening contract.** Only the Narrative overview shape has a self-sufficient-opening rule. The Guide, Catalog, Behavior reference and Proposal templates open with bare `{What this guide enables...}` placeholders. There is no progressive-disclosure staging, no "value-first block before prose" concept, and no rule saying what the first thing the reader sees must accomplish. The teaching sources' strongest mechanism (the value-table + reasons-to-try opener) is absent.

**No two-tier voice naming.** Doc Mode distinguishes prose from structured blocks but never names a register split. The Guide example (doc-example-guide.md) is actually excellent narrative-tier writing, but the concept is not generalized into a rule, so a writer could produce an all-reference-register Guide or an all-narrative Catalog with no guidance to stop them.

**Quality checklist is process-oriented, not output-oriented.** Doc Mode's checklist (doc-mode.md §10, doc-templates.md §11) asks "Creation or refinement identified correctly?" and "Material claims classified?" These verify the workflow was followed. They do not verify the artifact: no "every section opens with its takeaway," no "no placeholder text remains," no per-shape content bar. create-readme's per-section quality contract is the missing piece.

**No named table patterns or when-tables-beat-prose guidance.** Doc Mode says "tables for real comparisons, mappings, or dense indexes" (doc-templates.md §2) but gives no named patterns. The teaching sources give five. Doc Mode reinvents the decision each time.

**No shape selection decision tree.** doc-mode.md §5 Step 4 lists five shapes. With no tiebreaker, a request that could fit two shapes ("document how our notification states work" could be Catalog or Behavior reference) gets no deterministic routing.

**No analogy or voice-personality budget for the prose shapes.** The Product Owner HVR has voice-personality rules, but Doc Mode never tells the writer when to apply them or how the Narrative overview's register differs from a Behavior reference's. The prose-first shapes are where personality matters most and where guidance is thinnest.

---

## 3. Recommendations for Doc Mode

Listed highest-leverage first.

### R1. Add an Opening Contract to each adaptive shape
**Target:** `skill/assets/doc-templates.md` §3 (Guide), §4 (Catalog), §5 (Behavior reference), §6 (Proposal), §7 (Narrative overview).
**Change:** After each shape's "Use when..." line, add a 2-3 sentence "Opening Contract" block stating what the first thing the reader sees must accomplish. For Guide: "Open with what this enables, who uses it and why the outcome matters, in 2-4 sentences before the first section break. A reader who reads only the opening knows whether this document is for them." For Catalog: "Open with what the catalog contains, who uses it and what is explicitly out of scope." For Behavior reference: "Open with what behavior this explains, who needs it and why it matters." For Proposal: "Open with the problem or opportunity, who it affects and why it matters, before any current-state detail." For Narrative overview, the self-sufficient-opening rule already exists, so add only: "An optional compact value block (what this is, who it's for, current state) may precede the prose opening when the reader benefits from a 10-second scan before reading." This ports progressive disclosure (mechanism B2) and the value-first opener (mechanism A1) without importing anchor comments or TOCs.
**Why:** Today the templates leave the opening to inference. A concrete contract makes every shape open with the reader's "should I care?" answered first, which is the single highest-impact readability improvement.
**Effort:** Small. Prose additions to five existing sections, no new files.

### R2. Convert the quality checklist from process-verification to output-verification
**Target:** `skill/references/doc-mode.md` §10 (Quality Checklist), mirrored in `skill/assets/doc-templates.md` §11 (Template Quality Check).
**Change:** Add an "Output Quality" subsection to each checklist with items that verify the artifact, not the workflow. Build on the existing Readability Floor rather than restating it. Candidate items: "Every section opens with its takeaway, then supporting detail," "No section reads like a glossary when its reader needed a story (prose is a first-class citizen)," "No template instructions, conditional comments or placeholder text remain in the export," "Optional sections that add no value were removed, not left as empty shells," "Status labels sit beside the claims they qualify, not in a distant notice." Keep the existing Intake/Source Safety/Content sections, which are genuinely valuable.
**Why:** The current checklist confirms the writer ran the process. An output checklist catches the failure mode where the process was followed but the artifact is still weak (glossary-as-guide, leftover placeholders, orphaned status notices). This ports mechanism B4 (per-section output quality) without importing DQI scoring (which would conflict with DEPTH's six dimensions).
**Effort:** Small-medium. Adds one subsection to two existing checklists.

### R3. Name the two-tier voice and assign it to shapes
**Target:** `skill/references/doc-mode.md` §7 (Adaptive Document Shapes), with a short cross-reference from `doc-templates.md` §2 (Prose Is a First-Class Citizen).
**Change:** Add a "Voice Register" paragraph to §7. State that every shape mixes two registers: narrative tier (explain what, why and how, plain language, active voice, analogies where they clarify) and reference tier (terse label-bullet blocks, definition lists, tables and code fences). Assign them: Guide and Narrative overview are narrative-dominant; Catalog is reference-dominant; Behavior reference and Proposal mix both. Add one line: "A Guide written entirely in reference tier has picked the wrong register for its reader."
**Why:** This generalizes the excellent writing already in the Guide example into a rule the writer can apply to the other shapes. It ports mechanism B3 (two-tier voice) without changing the ClickUp grammar or HVR.
**Effort:** Small. One paragraph in doc-mode.md, one cross-reference line in doc-templates.md.

### R4. Add a shape selection decision tree to Step 4
**Target:** `skill/references/doc-mode.md` §5 Step 4 (Select the Adaptive Shape).
**Change:** Replace the current bare list of five shapes with an ASCII decision tree that routes by reader need, keeping the five shapes intact. For example: "Does the reader follow an order or apply a standard? YES → Guide. Does the reader locate and compare repeated entries? YES → Catalog. Does the reader understand states, rules and outcomes? YES → Behavior reference. Does the material describe what might or should change? YES → Proposal. Does the reader need orientation and story? YES → Narrative overview." Keep the existing list below the tree as reference.
**Why:** A request like "document how our notification states work" fits both Catalog and Behavior reference. A decision tree gives a deterministic first match instead of leaving the choice to inference. This ports mechanism B5 (decision trees) at near-zero cost.
**Effort:** Small. Replaces a list with a tree in one section.

### R5. Add named table patterns and a when-tables-beat-prose rule
**Target:** `skill/assets/doc-templates.md` §2 (Shared Application Rules), after the existing "tables for real comparisons" line.
**Change:** Add a short "Table Patterns" subsection naming three patterns adapted to the 2-column constraint that the invariants enforce: "Index" (ID + entry, already used in the Catalog), "Options and trade-offs" (option + benefit/cost, already used in the Proposal), "Combinations and precedence" (conditions + outcome, already used in the Behavior reference). Add one rule: "Use a table when the reader compares rows against each other. Use prose or a label-bullet block when the reader reads sequentially. Do not table content whose value is in the sentence between the items." This names patterns Doc Mode already uses implicitly and makes the choice explicit.
**Why:** Doc Mode currently says "tables for real comparisons" and then leaves the writer to decide. Named patterns (mechanism C4) reduce inconsistent table use and prevent the glossary-as-guide failure.
**Effort:** Small. One subsection, three named patterns, one rule line.

### R6. Add an analogy budget and voice-personality note to the Narrative overview
**Target:** `skill/assets/doc-templates.md` §7 (Narrative Overview Template), in the Adaptation Notes.
**Change:** Add two bullet points to the adaptation notes: "Use one analogy per concept at most, placed after the technical statement, not before. Drop it when plain language is already clear" (porting the analogy budget from mechanism C6) and "The Narrative overview carries more voice personality than the other shapes: react to facts, acknowledge trade-offs and name specifics rather than abstract labels. This does not override status discipline or identifier accuracy."
**Why:** The Narrative overview is the prose-first shape where voice matters most, and it is the only shape with no personality guidance. The Product Owner HVR already has voice-personality rules (Section 0.3), so this connects an existing resource to the shape that needs it most. No new voice rules, just a pointer.
**Effort:** Small. Two bullets in one existing adaptation-notes section.

### R7. Add a "no placeholders survive export" hard check to the ClickUp Layout checklist
**Target:** `skill/references/doc-mode.md` §10 (ClickUp Layout subsection).
**Change:** Add one checklist item: "No template scaffold text, `{...}` placeholders, or instruction comments remain in the exported document." This is distinct from the existing "No template instructions, conditional comments, or placeholder text in the final document" item in §9 Delivery Standards, because it places the check in the layout gate where the writer is already verifying divider and bullet grammar, making it a single-pass catch.
**Why:** create-readme's pre-publish checklist treats placeholder removal as a first-class check (mechanism B6). Doc Mode mentions it in Delivery Standards but not in the layout gate. The layout gate is where the writer is already doing mechanical verification, so this is the cheapest place to catch leftover scaffolding.
**Effort:** Small. One checklist line.

---

## 4. Small cross-mode suggestions

1. **Task Mode:** Adopt the "verify references resolve" principle from create-readme's read-evidence-first mandate. When a task lists related tickets, links or dependencies, the checklist could require confirming they resolve before export, rather than trusting pasted content. (Small, one checklist item in `task-mode.md`.)

2. **Bug Mode:** Borrow create-readme's "expected output for verification commands" pattern. Reproduction steps could pair each "When" action with the expected vs actual result, making repro steps self-verifying rather than narrative. (Small, a format note in `bug-mode.md`.)

3. **Story Mode:** Apply the two-tier voice split to the story artifact. The Connextra line and acceptance scenarios are narrative tier; Definition of Ready and Definition of Done gates are reference tier. Naming this could prevent stories where the criteria read like prose and the value reads like a checklist. (Small, one paragraph in `story-mode.md`.)

4. **Interactive Mode:** The disambiguation-checklist pattern from create-readme (UNKNOWN_FALLBACK_CHECKLIST) is already present and well-implemented in the Product Owner router. No change needed.

---

## 5. Do NOT import

**Anchor-comment navigation and Table of Contents.** The README exemplar uses `<!-- ANCHOR:... -->` pairs and a TOC. Doc Mode explicitly forbids a TOC unless requested, and ClickUp-bound content uses divider grammar, not anchor comments. Importing these would conflict with the ClickUp contract and add maintenance cost for no reader benefit in the target medium.

**Numbered ALL-CAPS H2 headings (`## 1. OVERVIEW`).** create-readme and core_standards mandate these. Doc Mode artifacts use content headings followed by `* * *` dividers, not numbered ALL-CAPS headings. These are competing structural grammars. Do not blend them.

**DQI deterministic scoring (Structure 40 / Content 30 / Style 30).** Doc Mode already has DEPTH's six-dimension qualitative floors (Completeness, Clarity, Actionability, Accuracy, Relevance, Mechanism Depth). Importing DQI would create a second, competing scoring system that scores different things (word count, heading density) and would confuse the writer about which gate governs. The per-section output-quality checks in R2 capture the useful part without the competing score.

**Runnable validation scripts (`validate_document.py`, `extract_structure.py`).** These belong to the sk-doc ecosystem and target skill/README/spec files, not ClickUp-bound deliverables. Doc Mode cannot run them, and the dual-packaged skill carries sync cost for any new tooling. The manual checklist is the correct mechanism here.

**The blockquote-tagline-immediately-after-H1 pattern.** create-readme places a one-sentence tagline right after the title. Doc Mode places a status blockquote between dividers, which carries source-safety information. Replacing or layering taglines would dilute the status-notice mechanism that is central to Doc Mode's source discipline.

**Three-column tables.** The invariants cap documentation tables at 2 columns. create-readme uses 3-column tables liberally (section/when/content; parameter/type/default). Do not import those shapes. R5 deliberately adapts patterns to the 2-column constraint.

**Frontmatter on export artifacts.** create-readme recommends frontmatter for discoverable docs. Doc Mode deliverables are ClickUp-bound markdown artifacts, not skill files. Frontmatter would render as literal text in ClickUp. Keep frontmatter on the skill's own reference and asset files, where it already lives, not on exports.
