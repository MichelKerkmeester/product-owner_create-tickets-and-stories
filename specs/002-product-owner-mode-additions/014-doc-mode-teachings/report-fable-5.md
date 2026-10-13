I've read all three teaching sources and the full Doc Mode surface (reference, templates, examples, SKILL.md routing, HVR, and the sibling modes). The deliverable is the report itself and the task forbids writing files, so I'm printing it here as my final output.

# Doc Mode Teachings Report — Claude Fable 5

## 1. What the teaching sources actually do (mechanisms, not vibes)

### Source 1: `Public/README.md` (the exemplar)

**Value-table opening** (`README.md:1-23`). Before any navigation or overview, the reader gets a two-column "Core layer / What it adds" table, a "Reasons to try it" list of bold-lead benefit bullets, and nothing else. A no-context reader can decide relevance in one screen. The mechanism is ordering: pitch first, structure second.

**Problem-story overview** (`README.md:57-64`). Section 1 opens with a four-sentence narrative of the pain ("AI coding assistants have amnesia. You explain your architecture Monday. By Wednesday, it is gone.") before any enumeration. Story establishes stakes, then the numbered layer list carries the mechanics. Prose and structure alternate deliberately rather than competing.

**Bold-lead bullet rhythm** (throughout Section 3). Nearly every feature bullet takes the form `**Benefit phrase:** supporting detail` ("**Won't quit early:** keeps going until…"). The bold fragment is scannable on its own; the tail carries the evidence. This is the single most consistent micro-pattern in the file.

**FAQ as objection handling** (`README.md:1418-1460`). The FAQ questions are adoption decisions, not trivia: "Do I need all 12 skills?", "What happens if I do not use a spec folder?", "Can I use this without the memory features?". Each answer is 2-4 sentences and honest about trade-offs ("skipped sessions… will not be recoverable").

**Section rhythm with anchors**. Numbered ALL-CAPS H2s, `---` between H2s, `&nbsp;` spacers between H4 clusters, and `<!-- ANCHOR:x -->` comments wrapping each major section for per-section retrieval. Note: this file contradicts its own authoring skill, which forbids TOCs and ANCHOR comments. The README is a public GitHub artifact class with its own rules, which matters for what to import (Section 5).

### Source 2: `sk-doc/create-readme/` (the authoring contract)

**Include-When section contracts** (`SKILL.md` §5-6, `readme_template.md` §2). Every candidate section is paired with an explicit inclusion condition and a content spec: "FAQ | Repeated questions exist | Short answers only". This converts "trim unused sections" from judgment into a checkable contract, and it works in both directions, preventing bloat and omission.

**Evidence-first authoring sequence** (`SKILL.md` §3-4). The workflow is ordered: read local evidence first, never document unconfirmed commands or files, test commands or mark them clearly as examples, show expected output for every verification command. Evidence gathering is a mandatory numbered step before drafting, not a virtue.

**Decision trees for artifact choice** (`SKILL.md` §2). Two short trees decide README vs code-folder README vs "skip and use inline comments", and install guide vs one-line command. The trees legitimize *not writing a document*, which most authoring systems never state.

**Validation checkpoints with STOP blocks** (`SKILL.md` §7). Install guides end every phase with a named checkpoint (`phase_N_complete`), a validation command, its expected output, and a STOP-if-failed instruction. Quantified floors back it: 5+ STOP blocks, 5+ troubleshooting entries, expected output for every verification command.

**Progressive-disclosure ladder with time budgets** (`references/readme/types_and_voice.md` §3). Title answers "what is this" in 10 seconds, Overview answers "should I care" in 30, Quick Start delivers a working state in 2 minutes, reference comes last. Reader time is the design unit.

**Two-tier voice with worked registers** (`types_and_voice.md` §4). One document, two named registers: a narrative tier (plain language, why-it-matters) and a reference tier (terse tables, exact signatures), each with a worked micro-example, and a per-README-type rule for which tiers apply.

### Source 3: `sk-doc/shared/` (the quality backbone)

**DQI: deterministic scored quality** (`references/validation.md` §4). A 0-100 score (Structure 40, Content 30, Style 30) computed from measurable attributes, with named bands (Excellent 90+, Good 75-89, Acceptable 60-74, Needs Work <60) and per-type quality gates (SKILL strict, README flexible, Spec loose). The transferable ideas are the *bands*, the *transparent breakdown*, and *type-aware gates*, not the mechanical point sources (word-count ranges, heading density), which are proxies.

**Two-stage validation pipeline** (`validation.md` §2). Stage 1 is a blocking format validator with exit codes; Stage 2 parses the document to JSON and generates *evaluation questions* per type ("When should I use this skill?", "Are examples practical and complete?") that the AI must answer against the draft. The questions simulate a reader; the split separates "is it well-formed" from "is it good".

**HVR with numeric scoring and rule precedence** (`references/hvr_rules.md`). Start at 100, hard blockers -5, soft deductions -2/-1, category weights, pass threshold 85, first-match-wins precedence when a term appears in multiple lists. Important honesty note: the Product Owner system already carries the *canonical superset* of this file (`skill/references/human-voice-rules.md` v0.210, symlinked, with the same precedence model). There is nothing here Doc Mode lacks.

**Enforcement levels per document type** (`references/core_standards.md` §3). Strict / moderate / loose / flexible enforcement tied to detected document type, so a working spec is never held to SKILL.md standards. Rigor is budgeted, not uniform.

**Voice personality layer** (`hvr_rules.md` §5). Beyond ban-lists: have opinions, acknowledge complexity, emotional specificity ("We expected a 10% lift. We got 2%"), controlled imperfection. Recognizes that rule-compliant sterile prose is still an AI tell.

## 2. Gap analysis

**Where Doc Mode is already stronger.** Be clear about this first, because it constrains what should be imported.

- **Source safety.** The five source classes, scoped authority order, conflict-hold gate, and consolidated single question (`doc-mode.md` §3-4) have no equivalent anywhere in sk-doc. create-readme's "never document unconfirmed commands" is a single rule; Doc Mode has a lifecycle model. Nothing in the teaching sources should touch this.
- **Refinement.** Doc Mode's fidelity invariant, protected literals, and smallest-coherent-diff workflow (§6, plus `doc-templates.md` §9) have no counterpart. create-readme only authors; it routes edits elsewhere.
- **Human Voice.** The PO system holds the canonical HVR superset with scoring and precedence. Equal or better than the teaching copy.
- **Prose discipline.** The Readability Floor plus "Prose Is a First-Class Citizen" (`doc-templates.md` §2) is a writing-mechanics layer the teaching sources express only as scattered per-section tips. The Narrative Overview shape is a genuine strength with no sk-doc equivalent.
- **Worked examples.** The four doc examples are complete, realistic artifacts with status discipline baked in. sk-doc ships fillable templates, not finished exemplars.

**Where Doc Mode is weaker.**

1. **No structured quality verdict.** §9 requires a "compact quality summary" in the response but never defines it, and §10's checklist is a private yes/no self-check. The DQI lesson, that quality reporting should be dimensioned, banded, and comparable across artifacts, is absent.
2. **Section inclusion is judgment, not contract.** The templates say "omit optional sections that add no value," but nothing states *when each section earns its place*. create-readme's Include-When tables are strictly better at this.
3. **Openings are underspecified outside Narrative Overview.** The Narrative shape demands a self-sufficient opening; Guide/Catalog/Behavior/Proposal Overviews are just "{what, who, why}" placeholders. The exemplar README's first-screen discipline and the 10s/30s disclosure ladder have no counterpart.
4. **No reader-simulation check.** extract_structure's generated evaluation questions test the draft against the reader's actual job. Doc Mode's checklist tests the draft against its own rules only.
5. **The Narrative Overview shape is incompletely wired.** It has no worked example (4 examples for 5 shapes), no Quick adaptation (`doc-templates.md` §8 still says "Quick uses the same four shapes" and lists only four), and §12's unclear-document-type recovery in `doc-mode.md` omits it from the shape list. These are outright defects, not just gaps.
6. **No expected-result convention for procedural content.** Runbooks and implementation guides are in scope, but nothing asks steps to carry observable outcomes the way install-guide checkpoints do.

## 3. Recommendations for Doc Mode

Ordered by leverage. All respect the ClickUp grammar, the source-safety invariants, HVR, the 2-column table limit, and build on (not restate) the Readability Floor.

**R1 — Include-When contracts for every shape. (medium)**
Target: `doc-templates.md`, the "Adaptation Notes" subsection of each shape (§3-7).
Change: replace the prose adaptation bullets about omitting sections with a 2-column table per shape: `Section | Include when`. Example for Guide: `Before You Start | A prerequisite, permission or known limitation would otherwise surprise the reader`, `Quality Checks | The reader hands work to someone who verifies it`, `Related Guidance | Supplied sources link to documents the reader will actually open`. Keep the existing shape-specific notes that are about fidelity (exact IDs, no invented precedence) as bullets below the table.
Why: this is the teaching sources' strongest structural mechanism. It makes the existing "smallest useful set of sections" rule checkable at draft time and at review time, and it slots directly into the §11 template quality check ("every included section satisfies its include-when condition").

**R2 — Define the "compact quality summary" as a dimensioned verdict. (small-medium)**
Target: `doc-mode.md` §9 Response Contract, plus one closing line in §10.
Change: specify the summary the response must carry: one line per dimension with a pass/attention verdict — Source safety, Shape fit, ClickUp layout, Readability Floor, Voice. Attention verdicts name the specific item (e.g. "Layout: attention — 2 headings missing trailing divider"). No numeric scores and no scripts: the dimensions map 1:1 onto the existing §10 checklist groups, so this is a reporting contract, not a new gate.
Why: DQI's real value is comparable, dimensioned quality reporting, and it is the one piece Doc Mode can adopt without scripts. It also forces the §10 checklist to actually run, since its outcome becomes user-visible. Deliberately not imported: DQI's mechanical point sources (see Section 5).

**R3 — Fix the Narrative Overview wiring: Quick adaptation, shape-count, error recovery, worked example. (medium)**
Targets: `doc-templates.md` §8 (change "the same four shapes" to five and add a Quick Narrative Overview block: keep the self-sufficient opening and Where-things-stand, drop optional Reading map and How-we-got-here when obvious, never drop status notices), `doc-mode.md` §12 Unclear Document Type (add Narrative overview to the enumerated shapes), and a new `assets/examples/doc/doc-example-narrative-overview.md` (a handover or investigation log showing prose-first opening, earned bullets, one checklist).
Why: the newest shape is the least specified and the only one without a retrieval fixture, and the "four shapes" sentence is now factually wrong. The new example file carries mirror sync cost, but the examples folder already mirrors and examples are what the mode retrieves at draft time; this is the one place a new file is worth it.

**R4 — Opening contract for all shapes. (small)**
Target: `doc-templates.md` §2, a short new subsection directly after the Readability Floor.
Change: three rules. First screen (title, status notice, Overview opening) must let a no-context reader answer "what is this, who is it for, do I need it" without scrolling. The Overview's first paragraph is the document's takeaway, not its table of contents. When the document's value is genuinely enumerable, the Overview may carry one compact 2-column orientation table (area / what the reader gets); otherwise prose. Reference the disclosure ladder in one sentence: title answers in seconds, Overview in half a minute.
Why: this generalizes the discipline Narrative Overview already has to the other four shapes, and it is the transferable core of the exemplar README's opening. It extends the takeaway-first Readability rule from paragraph level to document level without restating it.

**R5 — Reader-simulation questions in the quality checklist. (small)**
Target: `doc-mode.md` §10 Content block (five new checklist lines) with a pointer from `doc-templates.md` §11.
Change: one question per shape, answered against the draft. Guide: could the audience complete the process without opening another document? Catalog: can a reader go from the index to an entry and back in one hop? Behavior reference: given a state and an event, can the reader predict the outcome? Proposal: could any candidate item be mistaken for shipped behavior on a skim? Narrative overview: is a no-context reader oriented by the end of the opening?
Why: imports the evaluation-questions mechanism from `extract_structure.py` in prose form. It is the only checklist item type that tests the document against the reader's job rather than against the document's own rules, and it is nearly free.

**R6 — Two-register rule with micro-examples. (small)**
Target: `doc-templates.md` §2, extend "Prose Is a First-Class Citizen" (2-4 sentences plus two 1-line examples).
Change: name the two registers and their assignment. Narrative register (full sentences, why-before-what) owns Overview, current-state, history, and rationale sections. Reference register (definition bullets, tables, exact identifiers, no rhetoric) owns enumerable content. Give one line of each. State the boundary rule: a section switches register, never a paragraph mid-thought.
Why: the Readability Floor governs paragraph mechanics; nothing yet governs *register choice*, which is the actual failure mode when a Behavior reference turns into wall-to-wall label bullets or a Catalog entry drifts into essay. The two-tier voice is the teaching sources' clearest register mechanism and it names what "Prose is a first-class citizen" currently implies.

**R7 — Expected-result convention for procedural Guides. (small)**
Target: `doc-templates.md` §3 Guide Adaptation Notes (one bullet) and `doc-mode.md` §10 Content (one checklist line).
Change: when a Guide documents commands, procedures, or checks and the source supplies the outcome, each verification-bearing step carries an expected result adjacent to it ("Expected: …" in the example block or step prose). When the source does not supply the outcome, the step is flagged as unverified rather than given an invented result.
Why: the install-guide checkpoint pattern is the reason those guides are trustworthy to execute, and runbooks are explicitly in Doc Mode's scope. The no-fabrication clause keeps it inside the source-safety invariants.

**R8 — Optional FAQ element for Guides and Narrative overviews. (small)**
Target: `doc-templates.md` §3 and §7 adaptation notes (one bullet each), governed by an R1-style include-when condition: the sources show repeated questions or objections.
Change: an earned FAQ block: bold question, 1-3 sentence source-backed answer, `*   ` bullets or short paragraphs per the ClickUp contract, adoption-decision questions preferred over trivia.
Why: the exemplar's FAQ is its best objection-handling mechanism and it maps naturally onto handovers, standards guides, and onboarding docs, where the reader's unasked "but what if I don't" questions are the main comprehension risk.

## 4. Small cross-mode suggestions

1. **Task Mode** (`task-mode.md` §2): give the "Optional Context Sections" list the same Include-When treatment as R1, one condition per optional section, so section inclusion stops being taste.
2. **Bug Mode** (`bug-mode.md`): adopt the troubleshooting-pattern rule that Observed behavior leads with *what the user sees in their own words*, not internal error names, and let each reproduction step carry an observable result when the evidence supplies one.
3. **Story Mode** (`story-mode.md` quality checklist): add one reader-simulation question in the R5 style: "Could a developer cut a ticket from each requirement without asking a follow-up question?"
4. **Interactive Mode**: when intent cannot be scored, fall back to a fixed three-slot disambiguation checklist (artifact type, target or scope, expected validation), borrowed from create-readme's router fallback, instead of composing a novel question each time.

## 5. Do NOT import

- **TOC and `<!-- ANCHOR -->` navigation comments.** The exemplar README uses both, but its own authoring skill forbids them, and Doc Mode already bans generated TOCs. ANCHOR comments are retrieval infrastructure for that repo's memory engine; in a ClickUp deliverable they are noise that would also violate refinement fidelity when they leak into edits.
- **The script-based validation pipeline and DQI's mechanical point mechanics.** `validate_document.py` / `extract_structure.py` cannot run in the claude.ai Project mirror, so any script dependency splits the dual package. And DQI's word-count ranges, heading-density scores, and "3+ code blocks = full points" are proxies that would directly fight the adaptive-shape principle: a correct Quick catalog would score "Needs Work". Import the bands and dimensions (R2), never the point sources.
- **The numbered ALL-CAPS H2 house style, `---` dividers, and `&nbsp;` spacers.** All three collide with the ClickUp grammar invariants (`* * *`, spacer headings) and with refinement fidelity. Doc Mode's layout contract is settled; the teaching sources' layout is for a different renderer.
- **Hard quantified content floors** (3+ usage examples, 3+ troubleshooting entries, 5+ STOP blocks). In sk-doc these are safe because the author generates content from a live repo. In Doc Mode, where every claim needs a source class, minimum-count rules create direct pressure to fabricate or pad, the exact failure the conflict gate exists to prevent. R7 imports the *convention* without the *quota*.
- **Analogy patterns, badges, and marketing openers.** The "Reasons to try it" shields block and the librarian/filing-cabinet analogy library are public-GitHub stagecraft. Doc Mode's artifacts are internal ClickUp deliverables where an analogy quota adds an AI-tell risk the PO's own HVR already manages, and badges are meaningless off GitHub.
- **sk-doc's HVR file and multi-column reference tables.** The PO system already holds the canonical HVR superset (v0.210), so importing the derived copy would be a regression risk, and create-readme's 4-column parameter tables violate the 2-column invariant; any table pattern that survives import must be reshaped to two columns first.

One closing honesty note: the biggest thing the teaching sources have that Doc Mode lacks is *measurement*, and the biggest thing Doc Mode has that they lack is *epistemics*. The right move is to import measurement only in forms that cannot leak fabrication pressure (R2, R5, R7), and to leave Doc Mode's source-safety core exactly as it is.
