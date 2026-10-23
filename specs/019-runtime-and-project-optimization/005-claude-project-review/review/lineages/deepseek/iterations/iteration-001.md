# Review Iteration 001 — Correctness and traceability of the kernel and knowledge against the skill sources

**Review target:** `specs/z-staging-po-019r` (Product Owner claude.ai Project packaging)
**Iteration:** 1 of 3
**Focus:** kernel and knowledge correctness against the skill sources, and rule loss from the 2026-10-21 kernel cuts (`git diff HEAD -- "claude project/Custom Instructions.md"`).
**Lineage:** `specs/z-staging-po-019r/review/lineages/deepseek` (session `fanout-deepseek-1792598333413-h7kxu3`, generation 1)

## Dimension

Correctness and traceability. The sources are `sk-product-owner/` and `sk-create-figjam/`; the held-to artifacts are `Custom Instructions.md` and the 62 files in `claude project/knowledge/`, with `claude project/README.md`, `README.md` and `SYNC.md` read for the package's own claims about that set.

## Files Reviewed

| File | What was checked |
| --- | --- |
| `AI Systems/Product Owner/claude project/Custom Instructions.md:1-906` | rule blocks, Flow exception propagation, router code, knowledge table, example count |
| `AI Systems/Product Owner/claude project/Custom Instructions.md` (HEAD diff) | every deleted sentence tested against the current kernel plus all 62 knowledge files for rule loss |
| `AI Systems/Product Owner/claude project/knowledge/*.md` (62 files) | skill-only mechanics residue, cross-file contradictions with the kernel |
| `AI Systems/Product Owner/claude project/knowledge/Product Owner - Rules - Flow Quality Rubric.md:1-100` | loading instruction, gate checklist |
| `AI Systems/Product Owner/claude project/knowledge/Product Owner - System - Interactive Mode.md:32-95, 176-230` | intake rules, energy language, board second round |
| `AI Systems/Product Owner/claude project/knowledge/Product Owner - Templates - Flow Mode.md:1-410` | connector mechanics named against the vendored packets |
| `AI Systems/Product Owner/claude project/README.md:1-194` | upload set, source-to-mirror map, version claims |
| `AI Systems/Product Owner/README.md:20-25, 660-700` | counts and route claims |
| `AI Systems/Product Owner/SYNC.md:1-100` | manual parity method, review notes, version fields |
| `AI Systems/Product Owner/sk-product-owner/SKILL.md`, `sk-product-owner/references/interactive-mode.md`, `sk-create-figjam/references/quality-rubric.md`, `sk-create-figjam/references/types/user-flow.md` | the source side of each finding |

## Findings by Severity

P0: 0 · P1: 2 · P2: 3

### P0 Findings

None. No security exposure, no spec contradiction that removes a rule outright, and the 2026-10-21 rule-loss audit found no rule that the cut deleted without leaving an equivalent elsewhere.

### P1 Findings

#### 1. R1-P1-001 — The kernel's ALWAYS list still states the Deliverable-Block and ClickUp-offer rules without the Flow exception it grants three lines later

**Severity:** P1 (correctness / internal contradiction)
**Evidence:** `[SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:82]` reads "1. Always deliver the output as a Canvas Artifact, rendered in the side Canvas panel, never only inline in chat." `[SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:92]` reads "6. After the block, reply only in the Delivery Reply Shape that Section 9 states, closing on the ClickUp delivery offer when the ClickUp connector is present." `[SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:91]` (ALWAYS 5) carves Flow Mode out. `[SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:255]` states "Flow Mode's deliverable is a FigJam board, so it renders no Deliverable Block and no export-equivalent path." `[SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:236]` and `[SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:237]` carry the same carve-out in strict sequence steps 7 and 8.

**Why it matters:** `sk-create-figjam/` produces a board and nothing else, so the first and sixth ALWAYS rules instruct the runtime to do the two things Flow Mode forbids (render a Canvas Deliverable Block, close on a ClickUp offer). ALWAYS rules are the first rules a runtime reads, and they are the only rules in the kernel that state these two obligations without a qualifier. The kernel already knows the exception in ALWAYS 5, so the list is internally inconsistent rather than silent.

**Claim adjudication**

- `type`: cross_file_contradiction
- `claim`: ALWAYS 1 and ALWAYS 6 obligate a Deliverable Block and a ClickUp closing offer for every delivery, including Flow Mode, which the same kernel forbids for Flow Mode.
- `evidenceRefs`: `Custom Instructions.md:82`, `Custom Instructions.md:92`, `Custom Instructions.md:91`, `Custom Instructions.md:236-237`, `Custom Instructions.md:255`
- `counterevidenceSought`: read the whole ALWAYS block (82-96), Section 9 strict sequence (230-240) and Flow Mode Delivery (251-260) for a qualifier inside rules 1 and 6. None exists in either rule. ALWAYS 5 and strict steps 6-8 name the exception explicitly, which is the counterevidence: a runtime that reads the full block can resolve the conflict in Flow Mode's favour.
- `alternativeExplanation`: the ALWAYS list may be read as a summary of the common case with Flow treated as an exception elsewhere, and the same dedupe that moved eight rules into one place may have deliberately left the list summary-shaped.
- `finalSeverity`: P1, not P0: the exception is stated in the same block and in Section 9, so the contradiction is resolvable by a reader who follows the whole block. It is not P2, because the two conflicting instructions sit in the rules a runtime is told to apply always, and a Flow delivery that follows rule 1 renders the wrong artifact entirely.
- `confidence`: high
- `downgradeTrigger`: a Flow run in the Project playbook that renders the board, prints `Read-back:` and no Deliverable Block, with ALWAYS 1 and 6 present in the kernel.
- `fix changes`: `AI Systems/Product Owner/claude project/Custom Instructions.md` (rules 1 and 6 gain the same "except Flow Mode" qualifier ALWAYS 5 carries; the SYNC note records the kernel bump).

#### 2. R1-P1-002 — "Just do it" selects Quick energy in the knowledge mirrors and in the skill, but the kernel's router code and its Quick row do not know the phrase

**Severity:** P1 (traceability / routing drift)
**Evidence:** `[SOURCE: AI Systems/Product Owner/claude project/knowledge/Product Owner - System - Interactive Mode.md:51]` says request-framing "quick, fast, no-questions or just-do-it language selects Quick energy" and that such a request "never Raw". `[SOURCE: AI Systems/Product Owner/claude project/knowledge/Product Owner - System - Interactive Mode.md:220]` lists `just do it` inside `energy_language.quick`. `[SOURCE: AI Systems/Product Owner/sk-product-owner/references/interactive-mode.md:74]` and `[SOURCE: AI Systems/Product Owner/sk-product-owner/references/interactive-mode.md:243]` carry the same two statements, so the mirrors are faithful to their source. `[SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:131]` lists the Quick signals as "`$quick`, `$q`, quick, fast, no questions" with no just-do-it. `[SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:511]` to `[SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:518]` is the `natural_quick` regex, which matches only quick/fast forms and `no[ -]?questions`. `[SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:74]` declares Section 11 "the authority for exact routing behaviour", and `[SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:37]` claims "This kernel is aligned with its uploaded Project Knowledge mirrors." `[SOURCE: AI Systems/Product Owner/SYNC.md:81]` records the 2026-10-21 change as carrying just-do-it wording into both Knowledge mirrors and says "the kernel's Flow row, its intake paragraph and its Flow Mode Delivery say the same" — it does not.

**Why it matters:** A Project turn that says "just do it" is routed STANDARD by the kernel code, while the Interactive Mode knowledge file the kernel routes to says QUICK. That changes intake (Quick may skip routine Task and Bug questioning), the phase flow and the artifact size the user gets. The kernel is the Project's routing authority precisely because retrieval is unreliable, so the disagreement is not a harmless paraphrase.

**Claim adjudication**

- `type`: cross_file_contradiction
- `claim`: the kernel's router code and Quick row omit the `just do it` energy signal that the kernel's own knowledge mirror and the skill source both define.
- `evidenceRefs`: `Custom Instructions.md:131`, `Custom Instructions.md:511-518`, `Custom Instructions.md:74`, `knowledge/Product Owner - System - Interactive Mode.md:51`, `knowledge/Product Owner - System - Interactive Mode.md:220`, `sk-product-owner/references/interactive-mode.md:74`, `sk-product-owner/references/interactive-mode.md:243`, `SYNC.md:81`
- `counterevidenceSought`: searched the kernel for `just do it`, `just-do-it`, `energy_language` and a second Quick detector; none exists. Checked whether the kernel delegates detection to the knowledge doc; `Custom Instructions.md:74` and `:230` keep detection in the kernel's own code.
- `alternativeExplanation`: the phrase may be treated as an energy hint the model applies from the knowledge doc regardless of the router value, and the router's STANDARD result may be overridden by retrieval of Interactive Mode.
- `finalSeverity`: P1: the outcome is a wrong energy level on a common phrasing, and the kernel contradicts both its own knowledge mirror and the source the mirror was written from. Not P0, because no rule is lost — the Quick behaviour is still reachable when the knowledge file is retrieved.
- `confidence`: high
- `downgradeTrigger`: a Project or playbook run that says "just do it" and shows Quick processing and the Quick intake skip.
- `fix changes`: `AI Systems/Product Owner/claude project/Custom Instructions.md` (Quick row at 131 and the `natural_quick` regex at 511-518), plus the kernel H1 bump and a `SYNC.md` note.

### P2 Findings

#### 3. R1-P2-001 — The Flow Quality Rubric mirror still tells the reader to load a skill file path that does not exist in the Project

**Severity:** P2 (maintainability / parity residue)
**Evidence:** `[SOURCE: AI Systems/Product Owner/claude project/knowledge/Product Owner - Rules - Flow Quality Rubric.md:11]` reads "The type's reference in `references/types/` was loaded and its judged-by-hand rules were applied". `[SOURCE: AI Systems/Product Owner/sk-create-figjam/references/quality-rubric.md:28]` carries the same line, so the residue was copied rather than introduced by the mirror. The manual parity method requires the opposite treatment: `[SOURCE: AI Systems/Product Owner/SYNC.md:11]` says to "drop loading conditions, routed-by lines, file-path routing and benchmark references, keep the decision rules, output shapes and examples". `[SOURCE: AI Systems/Product Owner/claude project/README.md:107]` makes the same promise: each knowledge file "carries the decision rules and examples without the skill-only mechanics."

**Why it matters:** A Project has no `references/types/` directory; the matching Knowledge doc is `Product Owner - Templates - Flow Type - {Type}`. As written, the first TYPE FIT checkbox cannot be satisfied by the document the Project actually has, and a runtime that reads it literally looks for a path that never resolves. Every other Flow mirror uses Knowledge titles, so this is one surviving line rather than a class.

**Fix changes:** `AI Systems/Product Owner/claude project/knowledge/Product Owner - Rules - Flow Quality Rubric.md` (name the Knowledge document, e.g. "The chosen type's Flow Type document was consulted and its judged-by-hand rules were applied").

#### 4. R1-P2-002 — The package README contradicts itself and the kernel on how many worked examples ship and which routes exist

**Severity:** P2 (documentation gap)
**Evidence:** `[SOURCE: AI Systems/Product Owner/README.md:24]` says "four task shapes, a fixed bug report, five Doc shapes and the Barter house Story and Epic, with 21 worked examples". `[SOURCE: AI Systems/Product Owner/README.md:664]` says "`knowledge/` holds 62 files: 34 core documents … and the 28 worked examples". `[SOURCE: AI Systems/Product Owner/claude project/knowledge/]` holds 28 example files (5 Task, 4 Bug, 7 Doc, 5 Story, 7 Flow), and `[SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:222]` states "The twenty-eight example documents". `[SOURCE: AI Systems/Product Owner/README.md:21]` says "nine scored topics resolve each request to Task, Bug, Doc, Story or Interactive", omitting Flow, while `[SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:127]` routes `$flow` and `$figjam` and `[SOURCE: AI Systems/Product Owner/README.md:196]` tells the operator to upload all 62 files.

**Why it matters:** The README is the page an operator reads before uploading. Two counts of the same set differ eight files apart in one file, and the feature summary describes a five-route system while the package ships six. The upload instruction itself is correct, so this misinforms rather than breaks an upload.

**Fix changes:** `AI Systems/Product Owner/README.md` (lines 21 and 24).

#### 5. R1-P2-003 — The kernel's ask-first rules enumerate every command except `$flow` and `$figjam`

**Severity:** P2 (documentation gap / completeness)
**Evidence:** `[SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:115]` says "`$task`, `$bug`, `$doc`, `$story` and `$epic` still ask their mode's context-specific question … and so do `$t`, `$b`, `$d`, `$s` and `$e` and the `$prd` and `$p` aliases." `[SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:9]` likewise bounds the consolidated-question rule to "Task, Bug, Story, Epic and Doc". The kernel's own Flow route is `[SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:127]`, and `[SOURCE: AI Systems/Product Owner/claude project/knowledge/Product Owner - Templates - Flow Mode.md:42]` gives Flow its own intake rounds and gate.

**Why it matters:** The kernel's clauses read as closed enumerations of the commands that ask before drafting. Flow does ask — its own Brief rounds do — so the lists are incomplete rather than wrong, and a reader can conclude `$flow` is exempt from intake. The Flow row and the Flow Delivery section carry the real rule, which keeps this P2.

**Fix changes:** `AI Systems/Product Owner/claude project/Custom Instructions.md` (lines 9 and 115 name Flow's own intake instead of leaving it out).

## Traceability Checks

| Protocol | Status | Evidence |
| --- | --- | --- |
| `spec_code` (core) | partial | The spec's four focus questions map to iterations 1-3. Iteration 1 answers the first two: the kernel and knowledge were read against their sources (partial coverage of 62 files, see Ruled out) and the 2026-10-21 cut was tested for rule loss (pass, no loss). |
| `checklist_evidence` (core) | notApplicable | `specs/z-staging-po-019r/` carries no `checklist.md`; the staging folder is a review scope, not a lifecycle folder. |
| `skill_agent` (overlay) | partial | `sk-product-owner/SKILL.md:291` and `sk-product-owner/references/interactive-mode.md:74,243` agree with their mirrors; the kernel lags them on Quick energy (R1-P1-002). |
| `agent_cross_runtime` (overlay) | notApplicable | No agent definition is part of the reviewed package. |
| `feature_catalog_code` (overlay) | notApplicable | No feature catalog file is part of the reviewed package. |
| `playbook_capability` (overlay) | deferred | The playbook's Flow and Quick scenarios are read in iteration 3 if budget allows; the repository playbook grades the CLI packaging, not the Project. |

## Rule-loss audit (the 2026-10-21 kernel cut)

Every sentence deleted from `Custom Instructions.md` at HEAD was tested against the union of the current kernel and all 62 knowledge files. Eight rules were deliberately deduped into one place each, as `[SOURCE: AI Systems/Product Owner/SYNC.md:83]` records. The only deleted statements with no verbatim survivor are reformulations with the rule intact:

- "Technical alternatives, recommendations and designs may be documented …" survives as `[SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:29]` ("Technical alternatives, recommendations and designs are valid Doc content when labelled as a proposal").
- "Never claim that an architecture or technical recommendation is approved merely because Doc Mode produced it" survives in the same line ("never approved merely because Doc Mode produced them"), and "Never claim external approval or professional authority that was not supplied" survives as `[SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:21]` ("Never fabricate … approval, authority or professional sign-off").
- "This line is the count itself rather than an assertion that a count was taken" survives as `[SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:109]` NEVER 5 ("never report a count that was not actually taken").
- "The Project has no file system" survives as `[SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:2]` ("cannot write or read local files").

Result: no rule was lost by the cut. The two P1 findings are contradictions that the cut left in place, not gaps it created.

## Ruled out

- **A deleted rule in the 2026-10-21 cut.** Every deleted sentence was matched against the current kernel plus all knowledge files; the survivors are reformulations (above). No finding.
- **The four shared rule files drill.** `[SOURCE: AI Systems/Product Owner/claude project/README.md:107]` declares the four shared rule files byte copies of their cards in the shared knowledge folder, so their Project-side filesystem wording is the declared state, not drift. No finding.
- **Story versus Epic shape drift.** The kernel's Story paragraph (`Custom Instructions.md:159`) and Template - Story Mode now agree that a Story opens on `## Problem` and an Epic on `## About`; checked against `sk-create-figjam` and `sk-product-owner` sources. No finding.
- **Example count of 28.** Counted the knowledge directory: 5 Task, 4 Bug, 7 Doc, 5 Story, 7 Flow. The kernel's "twenty-eight" is correct; only the README bullet is stale (R1-P2-002).

## SCOPE VIOLATIONS

- **Gateway run directory mistyped, corrected and disclosed.** The first attempt to record this iteration's state record passed `--run-directory "$(pwd)"` while the shell was at the repository root, so the gateway created `deep-review-ledger/`, `deep-review-audit-ledger/` and `.legacy-projection-watermarks/` at the repository root and its append landed there (frame 1 carried this iteration's `deep-review.ledger.iteration-recorded` event and idempotency key, which confirmed the frame was this run's own write). No reviewed file and no other path was touched. The three directories were removed to return the tree to its pre-call state, and the record was then written with the workflow's own relative run directory `specs/z-staging-po-019r/review/lineages/deepseek`, where it is ledger sequence 2 and the projection now carries the iteration row. Recorded here rather than silently repaired because the write happened outside this lineage's surface.
- **Coverage-graph seed not run.** `step_seed_coverage_graph` calls `upsert.cjs --spec-folder specs/z-staging-po-019r`, which writes the shared coverage graph outside this lineage directory. It was skipped, so the iteration records carry no `graphEvents` and the reducer reports `graphConvergenceScore: 0`. This is a deliberate scope decision, not a failure.

## Open Questions

- The live claude.ai Project's own retrieval behaviour is not observable from the repository, so whether a runtime resolves ALWAYS 1 against Flow Mode in practice cannot be settled here (see R1-P1-001's downgrade trigger).

## Next Dimension

Iteration 2: end-user setup UX for the ClickUp and Figma connectors in Claude Desktop and claude.ai, against `AI Systems/Media Editor/USER-GUIDE.md`.

Review verdict: CONDITIONAL
