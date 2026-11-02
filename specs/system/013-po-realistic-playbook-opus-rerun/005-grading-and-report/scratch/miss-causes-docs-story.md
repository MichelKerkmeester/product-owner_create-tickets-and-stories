# Miss causes: Doc and Story value rows

| Row | Value | Kept in | Dropped in | Class | Change in one line |
|---|---|---|---|---|---|
| SDK-001 | `## Behavior rules`, the Behavior reference primary body (`doc-templates.md:400`) | No skill run. The Project twin kept it in both runs (`<R>/replies/PDK-001-turn1.txt:27`, `<R1>/replies/PDK-001-turn1.txt:32`) | Main run T1 and T2 (`<E>/SDK-001 - 001 - doc-promotion-stacking.md:59`), round one T1 and T2 (T1 read-back line 34, `<E1>/SDK-001 - 001 - doc-discount-stacking.md:35`), each `## Stacking rules` | rule gap | `doc-templates.md:116` and Project Doc Templates :95: a Behavior reference keeps `## Behavior rules` as its primary body heading and names the subject in the H3s beneath it |
| PDK-001 | `one discount code per order` (rules note line 7) | Main run T1 and T2 (`<R>/replies/PDK-001-turn1.txt:37`, `turn2.txt:37`) | Round one T1 and T2: "**3. One code per order**" plus the cart copy, no sentence stating the rule (`<R1>/replies/PDK-001-turn1.txt:55` and 58, `turn2.txt:55` and 58) | rule gap | `doc-templates.md:73` and Project Doc Templates :52: a phrase the source sets in backticks is literal copy and appears word for word in the sentence that states its rule |
| PDK-003 | `block-level last-writer-wins` (thread line 14) | Main run T1 and T2 (`<R>/replies/PDK-003-turn1.txt:22`, `turn2.txt:20`) | Round one T2: "Protocol v3 applies last-writer-wins at the block level" (`<R1>/replies/PDK-003-turn2.txt:20`, block line 19) | scenario defect | `proposal-decision-owner.md:39` in both twins: accept the thread's words or the same rule restated, or settle RO-1 once in the root |
| SST-002 | `Do sub-pages inherit the link?` (design notes line 46) | No run | Main run T1 and T2 (`<E>/SST-002 - 001 - Story-view-only-share-links.md:36`), round one T2 (`<E1>/SST-002 - 002 - Story-view-only-share-links.md:53`), each "whether a link on a page also opens its sub-pages" | rule conflict | `story-mode.md:80` and Project Story Mode :57: add an open question the source words itself to what is carried verbatim |
| PST-002 | `Do sub-pages inherit the link?` (design notes line 46) | No run | Main run T1 and T2 (`<R>/replies/PST-002-turn1.txt:33`, `turn2.txt:34`), round one T2 (`<R1>/replies/PST-002-turn2.txt:56`), each "whether a link on a page also opens its sub-pages" | rule conflict | Same change as SST-002 |

## Conventions and scope

- Paths are relative to `AI Systems/Product Owner/`. Short forms: `<R>` is `benchmark/reports/2026-09-25--manual-testing-playbook--claude-opus-5-5-medium`, `<R1>` is `<R>/remeasure-operator-repairs/run-1`, `<E>` is `export/benchmark/skill`, `<E1>` is `<E>/remeasure-operator-repairs/run-1`, `<K>` is `claude project/knowledge`. Unqualified `doc-mode.md`, `story-mode.md`, `hvr-core.md` and `conciseness.md` sit in `sk-product-owner/references/`, and `doc-templates.md` and `story-template.md` in `sk-product-owner/assets/`.
- Project line numbers are reply lines. Every Project reply cited here is byte-identical to its `claude project/<ID> - <slug>/turn-<n>.md` (checked with `cmp`). Every skill export cited under `<E>` and `<E1>` is byte-identical to the copy in the run's `exports/export/` folder where one exists (checked with `cmp`).
- Round two (`<R>/remeasure-file-forecast/run-1/`) holds none of these rows.
- Source lines are cited at today's tree (HEAD `01200fa`, which changes no source file after `b591571`). `git diff 3023c5e b591571` touches `doc-mode.md`, `story-mode.md`, `SKILL.md`, `AGENTS.md` and the Project Doc Mode and Story Mode mirrors only on the version header and the explicit-command intake sentence, all same-line replacements, and leaves `doc-templates.md`, `story-template.md` and both of their Project mirrors untouched. Every rule line below held the same text and number in both runs.
- The three scenarios' Pass clauses are unchanged between `39bcd29` and `b591571` apart from a version line and two knowledge-file links. The main-run SDK-001 scenario (`git show 3023c5e:.../skill-document-modes/behavior-reference.md` line 37) already demanded the `## Behavior rules` body and `one discount code per order` verbatim.
- No reasoning text explains any of these choices. The round one skill and Project events carry empty thinking blocks around each write, and the main-run SDK-001 thinking at `<R>/skill/SDK-001 - behavior-reference/events-turn-1.jsonl:69` and :183 is about routing and the format check. Every statement below about why a runtime wrote what it wrote is therefore inference, and is marked so.

---

## The group questions

### Doc Mode: do supplied values and the template's mandatory section names travel unchanged?

**Values: no.** Doc Mode protects identifiers, code and "literal copy" or "literal content", and asks for everything else to be represented "accurately". It never says a supplied value, rule phrase or term of art travels word for word into a new document.

- `doc-mode.md:79` "Preserve supplied technical identifiers, implementation facts, code, architecture, APIs, schemas, data models, debugging procedures, controls, and operational evidence accurately" (Project `<K>/Product Owner - Templates - Doc Mode - v0.111.md:55`)
- `doc-mode.md:100` "Preserve semantic table, code-fence, blockquote, link, and identifier formatting" (Project :76)
- `doc-mode.md:275`, Create workflow Step 5: "Preserve supplied identifiers, implementation facts, code, configuration, diagrams-as-text, and literal content accurately" (Project :251)
- `doc-mode.md:443`, checklist: "Supplied identifiers, implementation details, code, architecture, APIs, schemas, data models, debugging procedures, and evidence are represented accurately?" (Project :417)
- `doc-templates.md:73` "Keep tables, code fences, blockquotes, links, identifiers, and literal copy in their source-supported form" (Project `<K>/Product Owner - Assets - Doc Templates - v0.107.md:52`)
- `doc-templates.md:125` "Preserve supplied technical identifiers, code, configuration, architecture, API, schema, data-model, debugging, security, compliance, and operational details when needed for fidelity" (Project :104)
- `doc-templates.md:455`, Behavior reference only: "Use source terminology rather than normalizing state names" (Project :434)
- `doc-templates.md:579`, Proposal only: "Preserve supplied technical alternatives as attributed source content" (Project :558)
- `doc-templates.md:769` "Supplied identifiers and literal content remain exact" (Project :748)
- Kernel `claude project/Custom Instructions.md:138` ends "and preserve ordered lists, tables, code fences, blockquotes, links and identifiers."

"Literal content" and "literal copy" are never defined for a new document. The one worked definition is refinement-scoped and lists identifiers: `doc-mode.md:513` "An identifier such as `complated_applications_count` remains exact during unrelated refinement, even if it appears misspelled. Notification IDs, event names, variables, CTA labels, YAML keys, and exact URL names receive the same protection." (Project :487). The word-for-word rules that do exist are refinement-only: the fidelity invariant at `doc-mode.md:302` to 312, the prohibition at `doc-mode.md:584` (Project :558), `SKILL.md:290` and `SKILL.md:385`. There is no Doc counterpart of Story Mode's hard-value list: `AGENTS.md:270` opens its value clause with "For Story intent".

**Mandatory section names: no.** The rules make the section mandatory and imply, without stating, that its heading keeps the scaffold text.

- `doc-templates.md:115` "the Overview plus the shape's primary body are the only mandatory sections" (Project :94)
- `doc-templates.md:116` "Rename optional headings when the subject needs clearer product language" (Project :95). The only rename rule. It names optional headings, so a ban on renaming the primary body is read from the word "optional", not stated
- `doc-templates.md:400` the scaffold heading `## Behavior rules` (Project :379)
- `doc-templates.md:691`, Quick only: "Keep Overview, Terminology when needed, Behavior rules and Boundaries" (Project :670)
- `doc-templates.md:766` "Every included optional section satisfies its Include when condition, and no mandatory section is missing" (Project :745). A renamed body is arguably not missing
- `SKILL.md:382`, Blocking Gates: "Template structure is followed exactly, or source structure is intentionally preserved for a refinement". Skill only. `grep -rn "followed exactly"` over `claude project/` finds no counterpart. It is qualified in practice by `doc-templates.md:116` and :117 ("Combine compatible sections rather than leaving empty shells")
- `doc-mode.md:91` names the section by role only: "H2 anchors major sections such as the Overview and the primary body section" (Project :67)

Pushing the other way, in the same file the runtime reads whole: `doc-templates.md:650`, Narrative overview: "Rename every heading to fit the actual story; the scaffold names are placeholders, not a contract" (Project :629), and `doc-templates.md:288`, where the Catalog's primary body is the placeholder `## {Category}` (Project :267). The playbook itself accepts a renamed primary body for the Proposal shape (see SDK-001 below).

### Story Mode: does line 75 cover an open question's wording, and does line 80 push the other way?

**Line 75 does not cover it.** `story-mode.md:75`: "Supplied hard values travel into Requirements verbatim. A number, a size, a spacing, a heading level, a limit, a token, a button order or an exact string the source states is copied into a constraint bullet with its value intact, in the source's own units and notation, inside backticks." Its subject is hard values, and it routes an exact string "into a constraint bullet". The `**Open:**` line is kept apart from the constraint bullets: `story-mode.md:327` "The `**Open:**` line sits directly under the requirement name's divider, above the constraint bullets ... The constraint bullets then state only the settled constraints". A question the source cannot yet answer is the opposite of a supplied hard value. The same limit holds at `story-template.md:111` "Copy each number, size, spacing, heading level, limit, exact string and button order into a constraint bullet". The only reading under which line 75 reaches the question is "an exact string the source states", which the design notes' backticks invite and the constraint-bullet destination rules out.

**Line 80 pushes the other way.** `story-mode.md:80`: "Source prose is material, never copy. The Human Voice rules apply to what the artifact says, so a hedge, an opener, a filler phrase or a vague qualifier in the source is rewritten as a fact, an open constraint or a plain condition. Only exact product copy, identifiers and values are carried verbatim, inside backticks." A decision question is none of product copy, identifier or value, and an `**Open:**` line is an open constraint. The Open slot then asks for a description rather than the source's words: `story-mode.md:332` "**Open:** {the part that is not decided}. {Who decides it, or what evidence settles it.}", with `story-mode.md:327` "Write the undecided part and what settles it." `story-template.md:112` adds "source hedges are rewritten as facts or open constraints rather than carried into the artifact's prose".

Project mirrors: `<K>/Product Owner - Templates - Story Mode - v0.403.md:52` (line 75), :57 (line 80), :303 (line 327), :308 (line 332), and `<K>/Product Owner - Assets - Story Template - v0.100.md:92` and :93. A `diff` of skill lines 75, 80 and 332 against Project lines 52, 57 and 308 printed nothing, so the text is identical.

---

## SDK-001: `## Behavior rules`

**1. The source.** The value is a template section name, not an attachment value: `doc-templates.md:400` `## Behavior rules` in the Behavior reference scaffold (Project `<K>/Product Owner - Assets - Doc Templates - v0.107.md:379`). The fixture's own heading is `## Current rules` (`benchmark/fixtures/companies/fernhouse/fernhouse-promotions-rules.md:5`), and the request asks "how discount codes and automatic promotions stack" (`skill-document-modes/behavior-reference.md:31`).

**2. The demand.** `sk-product-owner/manual-testing-playbook/skill-document-modes/behavior-reference.md:39` "saves and reads back a Behavior reference in the doc lane on the first number with an Overview and a `## Behavior rules` body". Line 67 of the same file: "a Behavior reference with an Overview and `## Behavior rules`, the two sections the shape cannot drop (`doc-templates.md` lines 115 and 400)". A missed Pass clause fails the row (`manual-testing-playbook.md:150`).

**3. What was written.** In both runs Turn 2 edited the Turn 1 file in place (`<R>/results.csv` and `<R1>/results.csv`, SDK-001 rows), so each run holds one independent draft of the heading.

- Main run T1: `## Stacking rules`, content line 59 of the Write at `<R>/skill/SDK-001 - behavior-reference/events-turn-1.jsonl:154`
- Main run T2: `<E>/SDK-001 - 001 - doc-promotion-stacking.md:59` `## Stacking rules`
- Round one T1: `## Stacking rules` at line 34 of the read-back returned at `<R1>/skill/SDK-001 - behavior-reference/events-turn-1.jsonl:105`
- Round one T2: `<E1>/SDK-001 - 001 - doc-discount-stacking.md:35` `## Stacking rules`

Kept in no skill run. Contrast: the Project twin PDK-001 wrote `## Behavior rules` on every turn of both runs, `<R>/replies/PDK-001-turn1.txt:27`, `<R>/replies/PDK-001-turn2.txt:27`, `<R1>/replies/PDK-001-turn1.txt:32`, `<R1>/replies/PDK-001-turn2.txt:32`, from the same template text.

**4. The rules.** Every rule for and against is listed under the group question above. In short:

- For, all implicit about the heading text: `doc-templates.md:115`, :116 (by the word "optional"), :400, :766, and the skill-only `SKILL.md:382`
- Against: `doc-templates.md:116` itself, whose trigger "clearer product language" fits "stacking", the user's own verb. `doc-templates.md:650` and :288 show scaffold headings renamed by design in two other shapes. The playbook accepts a renamed primary body for the Proposal: `skill-document-modes/proposal-decision-owner.md:39` asks only for "an Overview and a proposed-design or options body", and both proposal runtimes named theirs `## Options` (`<E1>/SDK-003 - 002 - doc-sync-conflict-options.md:30`, `<R1>/replies/PDK-003-turn2.txt:43`) with that clause graded Met (`<R1>/grading-notes.md:823` for SDK-003 and :885 for PDK-003)

No rule for this artifact kind states that the primary body keeps its scaffold heading.

**5. The cause class: rule gap.** The heading text is bound only by inference from the word "optional" in `doc-templates.md:116`, while `doc-templates.md:650`, :288 and the Proposal Pass clause show scaffold headings being renamed with approval elsewhere. The Project kept the name in both runs under the same template lines and without `SKILL.md:382`, and the skill renamed it in both runs with that extra gate, a split the rules do not explain. That the split is runtime variance acting inside an unstated rule is inference. Evidence that would move it: to `runtime fault` if the operator rules that `doc-templates.md:115` with :116 and `SKILL.md:382` already fix the heading text, or if a trace showed the runtime weighed the scaffold name and chose to rename it.

**6. The smallest change.** `sk-product-owner/assets/doc-templates.md:116`, current text: "- Rename optional headings when the subject needs clearer product language". Proposed: "- Rename optional headings when the subject needs clearer product language. A Behavior reference keeps its primary body heading as `## Behavior rules` and puts the subject's language in the `### {Rule, feature or flow}` headings beneath it". Counterpart: `<K>/Product Owner - Assets - Doc Templates - v0.107.md:95`, same text. It is scoped to the Behavior reference on purpose. A general "mandatory headings keep their scaffold text" rule would also bind the Proposal's `## Proposed behavior or design`, which the proposal scenarios accept renamed, and would turn both passing proposal runs into misses.

---

## PDK-001: `one discount code per order`

**1. The source.** `benchmark/fixtures/companies/fernhouse/fernhouse-promotions-rules.md:7` "1. **One code.** A customer can use `one discount code per order`. Entering a second code replaces the first, and the cart says so: "Only one code per order. Your new code has replaced the old one."" The source sets the phrase in backticks.

**2. The demand.** `sk-product-owner/manual-testing-playbook/project-document-modes/behavior-reference.md:39` "stating the current rules with `one discount code per order`, `automatic promotions first`, `exclusive`, `STAFF-`, `compare_at`, `applies_to_sale`, the `50%` cap and `0.01` `half up` rounding verbatim, and Turn 2 ... every one of those values still verbatim". Root `manual-testing-playbook.md:188` "A protected fact altered: a supplied value generalized".

**3. What was written.**

- Main run T1 `<R>/replies/PDK-001-turn1.txt:37` "A customer can use one discount code per order." under the label "**One code per order**" (line 35). Kept
- Main run T2 `<R>/replies/PDK-001-turn2.txt:37`, the same sentence. Kept
- Round one T1 `<R1>/replies/PDK-001-turn1.txt:55` "**3. One code per order**", then only When and Then bullets, the Then bullet at line 58 carrying the cart copy "Only one code per order. Your new code has replaced the old one." No sentence states the rule. Dropped
- Round one T2 `<R1>/replies/PDK-001-turn2.txt:55` and 58, identical. Dropped

Contrast, SDK-001: round one kept it, T1 read-back line 52 (`<R1>/skill/SDK-001 - behavior-reference/events-turn-1.jsonl:105`) and `<E1>/SDK-001 - 001 - doc-discount-stacking.md:53` "A customer can use one discount code per order." (without backticks). The main run reworded it, "A cart holds one discount code at a time" at content line 71 of the Write at `<R>/skill/SDK-001 - behavior-reference/events-turn-1.jsonl:154` and at `<E>/SDK-001 - 001 - doc-promotion-stacking.md:71`. Across both runtimes the phrase survived in two of four runs.

**4. The rules.**

For: `doc-mode.md:79` and :275, `doc-templates.md:73` and :769, kernel `Custom Instructions.md:138`, with their Project lines listed under the group question. None names a rule phrase. "Accurately" is met by "One code per order" beside the quoted cart copy, since the rule's meaning survives. Whether "literal content" (`doc-templates.md:769`) reaches a backticked rule phrase is undefined, and the only worked definition (`doc-mode.md:513`) lists identifiers.

Against:

- The rule slot in the scaffold, `doc-templates.md:404` to 412 (Project :383 to 391): a bold label `**1. {Rule or Step Name}**`, one prose slot "{Source-supported condition, mechanism, and outcome.}", then When, Then, How, Why and Status bullets. Round one filled the label and the When and Then bullets for rule 3 and left the prose slot empty (`<R1>/replies/PDK-001-turn1.txt:55` to 59), which is where the rule's sentence would sit
- The Project example rule "**2. Reconnection Retry**" carries no prose line, only When, Then, Why and Status bullets (`<K>/Product Owner - Examples - Doc - Behavior Reference - v0.100.md:134` onward, skill `sk-product-owner/assets/examples/doc/doc-example-behavior-reference.md:135`). PDK-001 round one read it (`<R1>/claude project/PDK-001 - behavior-reference/events-turn-1.jsonl:70`)
- `hvr-core.md:109` "**Fragmented headers.** A first sentence restating its heading. Cut it, open on substance" (Project `<K>/Product Owner - Rules - Human Voice Core - v0.100.md:109`), read by PDK-001 round one at events-turn-1.jsonl:68. The main run's surviving sentence under "**One code per order**" (`<R>/replies/PDK-001-turn1.txt:35` to 37) is exactly the shape this rule cuts
- `conciseness.md:52` "**Heading echo.** A first sentence that restates its own heading" and :67 "A heading followed by a sentence that shares its words and adds no new one is a heading echo: cut the sentence and open on substance" (Project `<K>/Product Owner - Rules - Conciseness - v0.100.md:52` and :67), summarized in the kernel at `Custom Instructions.md:90` "Cut only what a reader could rebuild from what remains". PDK-001 round one did not open the Conciseness file (its tool calls, events-turn-1.jsonl:6 to 70, are the two attachments, Doc Mode, Router Contract, Interactive Mode, Doc Templates, Human Voice Core and the Behavior Reference example)

No rule for a new Doc requires a source's backticked rule phrase to travel word for word, and three rules make cutting the one sentence that carried it a natural edit.

**5. The cause class: rule gap.** The protecting rules ask for accuracy or protect an undefined "literal content" whose one worked definition lists identifiers, and the same rules produced the phrase in two runs and lost it in two, across both runtimes. That the round one runtime cut the sentence as a fragmented header or heading echo is inference: a Project block renders once, so no earlier draft shows a cut, and no reasoning text survives. Evidence that would move it: to `rule conflict` if a trace showed the sentence cut under `hvr-core.md:109` or `conciseness.md:67`, and to `runtime fault` if the operator rules that "literal content" in `doc-templates.md:769` already covers any span a source sets in backticks.

**6. The smallest change.** `sk-product-owner/assets/doc-templates.md:73`, current text: "- Keep tables, code fences, blockquotes, links, identifiers, and literal copy in their source-supported form". Proposed: "- Keep tables, code fences, blockquotes, links, identifiers, and literal copy in their source-supported form. A phrase the source sets in backticks is literal copy, a rule's own wording as much as an identifier, so it appears word for word in the sentence that states that rule, even where that sentence repeats its bold label, and a shorter label or a When and Then pair never stands in for it". Counterpart: `<K>/Product Owner - Assets - Doc Templates - v0.107.md:52`, same text. The same line would also have caught the main run's SDK-001 "one discount code at a time".

---

## PDK-003: `block-level last-writer-wins`

**1. The source.** `benchmark/fixtures/companies/loomlist/loomlist-sync-conflict-thread.md:14` "That is protocol v3 doing what it was built to do. It is block-level last-writer-wins." Plain prose with no backticks. Also `benchmark/fixtures/companies/loomlist/loomlist-context.md:70`, a table cell "Protocol v3, block-level last-writer-wins", also plain.

**2. The demand.** `sk-product-owner/manual-testing-playbook/project-document-modes/proposal-decision-owner.md:39` "gives today's v3 `block-level last-writer-wins` as the current state", and line 67 "Today's v3 `block-level last-writer-wins` sits apart from the candidates." The clause attaches "verbatim" only to `Conflicting edit from {device name}`, and its Fail list names "changes a figure or estimate", not a mechanism name. The word-for-word reading is the orchestrator's convention, `<R1>/grading-notes.md:15` "Backticked values are graded word for word, as in the main run." The draft grader read it as Met (`<R1>/grading-notes.md:917` "The Pass clause attaches "verbatim" only to `Conflicting edit from {device name}`, so this is graded Met"), and the underlying question is still open as RO-1 (`<R1>/grading-notes.md:40`). The root carries no rule that a backticked Pass-clause value is verbatim: `grep -n -i "backtick\|word for word\|verbatim"` over `manual-testing-playbook.md` returns lines 136, 207, 479 and 867, none of them such a rule.

**3. What was written.**

- Main run T1 `<R>/replies/PDK-003-turn1.txt:22` "Protocol v3 settles conflicts with block-level last-writer-wins." Kept. That turn failed for drafting before asking, not for this
- Main run T2 `<R>/replies/PDK-003-turn2.txt:20` "Protocol v3 resolves conflicts with block-level last-writer-wins." Kept
- Round one T1: a clarification block with no current-state claim
- Round one T2 `<R1>/replies/PDK-003-turn2.txt:20` (block line 19) "Protocol v3 applies last-writer-wins at the block level." Reworded, the mechanism unchanged

Contrast, SDK-003: main run `<E>/SDK-003 - 002 - doc-sync-conflict-options.md:19` "Protocol v3 resolves conflicts with block-level last-writer-wins." and round one `<E1>/SDK-003 - 002 - doc-sync-conflict-options.md:18` "Protocol v3 is block-level last-writer-wins." Both kept.

**4. The rules.** For: `doc-mode.md:79` and :275 ("accurately"), `doc-templates.md:73` (identifiers and literal copy), `doc-templates.md:579` (technical alternatives, which covers the options and not the current state) and kernel `Custom Instructions.md:138` (identifiers), with Project lines under the group question. None requires a mechanism name's word order, and "last-writer-wins at the block level" meets "accurately". Against: nothing specific to this phrase found.

What differs between the two sides: nothing in the rules. The Doc Mode and Doc Templates mirrors carry the same lines as the skill sources, and the kernel adds only the identifiers clause at :138. The context differs only in what each run opened. SDK-003 round one read `conciseness.md` (events-turn-1.jsonl:36) and `doc-templates.md` (events-turn-2.jsonl:4 and 7). PDK-003 round one read Doc Mode (events-turn-1.jsonl:20, events-turn-2.jsonl:20), Human Voice Core (events-turn-1.jsonl:22), the Proposal example (events-turn-2.jsonl:7) and Doc Templates (events-turn-2.jsonl:11 and 13). None of these says anything about this phrase. The main-run PDK-003 kept it twice under the same kernel and mirrors, so the round one reword is inferred to be run variance.

**5. The cause class: scenario defect.** No Doc rule requires a mechanism name word for word, neither attachment marks the phrase as a literal, the Pass clause does not say verbatim for it, and the output states the same mechanism accurately. Evidence that would move it: to `rule gap` if the operator settles RO-1 as "backticked Pass-clause values are verbatim" and wants Doc Mode to carry a source's terms of art unchanged. The PDK-001 change would not reach this row, because the thread never backticks the phrase.

**6. The smallest change.** `sk-product-owner/manual-testing-playbook/project-document-modes/proposal-decision-owner.md:39`, current text: "gives today's v3 `block-level last-writer-wins` as the current state". Proposed: "gives today's v3 block-level last-writer-wins as the current state, in the thread's words or as the same rule restated, such as last-writer-wins applied per block". Counterpart: `sk-product-owner/manual-testing-playbook/skill-document-modes/proposal-decision-owner.md:39`, same text. A wider option, the operator's call: settle RO-1 once in the root beside line 150, for example "A backticked value in a Pass clause is graded word for word where the clause says verbatim or the source sets it in backticks, and elsewhere the same value in other words meets it." That reading leaves PDK-001 and SST-002 graded as today, since both values are backticked in their sources.

---

## SST-002 and PST-002: `Do sub-pages inherit the link?`

**1. The source.** `benchmark/fixtures/companies/loomlist/loomlist-view-only-links-design-notes.md:46` "`Do sub-pages inherit the link?`", backticked on its own line under `## Open question` (line 44), with "Status: not decided" at line 48 and Lena named as the one who settles it at line 54. Turn 2 (`skill-story-modes/story-forced-delivery.md:43`) says Lena "still hasn't settled the sub-page question ... so keep it open in the story" and supplies no wording of its own.

**2. The demand.** `sk-product-owner/manual-testing-playbook/skill-story-modes/story-forced-delivery.md:35` "an `**Open:**` line carries `Do sub-pages inherit the link?` and names Lena as the one who settles it, Rabbit holes repeat that question", and the Project twin `project-story-modes/story-forced-delivery.md:35`, same words. "Verbatim" in that clause attaches to the Requirements values list, not to the Open line, and the scenario's own Pass bullet at line 70 asks only that the Story "keeps the sub-page question open under an `**Open:**` line naming Lena". The row is graded word for word under `<R1>/grading-notes.md:15`.

**3. What was written.** Every Open line in every run rewords the question, and every one takes its wording from Kofi's design view at notes line 50, "A link on a page also opens its sub-pages", recast as "whether". Kept in no run.

- SST-002 main run T1: content line 33 of the Write at `<R>/skill/SST-002 - story-forced-delivery/events-turn-1.jsonl:59` "**Open:** whether a link on a page also opens its sub-pages is not decided." T2 edited it in place: `<E>/SST-002 - 001 - Story-view-only-share-links.md:36`, same opening
- SST-002 round one T2: `<E1>/SST-002 - 002 - Story-view-only-share-links.md:53` "**Open:** whether a link on a page also opens its sub-pages, and so what `Duplicate` copies."
- PST-002 main run T1 `<R>/replies/PST-002-turn1.txt:33` "**Open:** It is not decided whether a link on a page also opens its sub-pages." T2 `<R>/replies/PST-002-turn2.txt:34`, same opening
- PST-002 round one T2 `<R1>/replies/PST-002-turn2.txt:56` "**Open:** Whether a link on a page also opens its sub-pages."

Round one Turn 1 on both sides was the Story question, and it already paraphrased the question as "whether sub-pages inherit the link" (`<R1>/replies/SST-002-turn1.txt:11`, `<R1>/replies/PST-002-turn1.txt:5`), so both runtimes had the question in hand and chose a statement form for the artifact.

**4. The rules.** Every line is quoted under the group question above.

- For: `story-mode.md:75` (Project Story Mode :52) is the only candidate, and it routes an exact string into a constraint bullet, which the Open line is not (`story-mode.md:327`). `story-template.md:111` has the same limit. `story-mode.md:341` "Carry the same open question into `## Delivery` under Rabbit holes" (Project :317) keeps the Open line and Rabbit holes consistent with each other, not with the source. `SKILL.md:268`, `AGENTS.md:270` and `quality-scoring.md:155` speak only of hard values
- Against: `story-mode.md:80` (Project :57) limits verbatim carriage to "exact product copy, identifiers and values" and orders source prose "rewritten as a fact, an open constraint or a plain condition". The slot at `story-mode.md:332` (Project :308) asks for "{the part that is not decided}", and `story-mode.md:327` (Project :303) says "Write the undecided part and what settles it." Every output above follows the slot's two-sentence shape, the undecided part and then who decides. `story-template.md:112` (Project Story Template :93) repeats "source hedges are rewritten as facts or open constraints"

Both runtimes had these lines open right before writing. SST-002 round one printed `story-mode.md` lines 66 to 240 and 315 to 365 and all of `story-template.md` (`<R1>/skill/SST-002 - story-forced-delivery/events-turn-2.jsonl:8` and :10), then wrote the Story at :39. PST-002 round one read the whole Story Mode mirror (`<R1>/claude project/PST-002 - story-forced-delivery/events-turn-1.jsonl:12`) and the Story Template (events-turn-2.jsonl:8).

**5. The cause class: rule conflict.** `story-mode.md:80` limits what travels verbatim and orders the rest rewritten as an open constraint, the Open slot at :332 asks for a description, and line 75, the one rule that could protect an exact string, sends it to a constraint bullet the Open line is not. Every draft on both sides in both runs produced the same statement form, which a rule push explains and chance does not. That the runtimes followed these lines, rather than paraphrasing on their own, is inference from the matching shape and the reads just before writing. Evidence that would move it: to `scenario defect` if the operator rules that an open question is not an "exact string" and its wording does not matter, which is already how the scenario's own Pass bullet at line 70 reads, and to `runtime fault` only if line 80 were amended and a rerun still reworded.

**6. The smallest change.** `sk-product-owner/references/story-mode.md:80`, current sentence: "Only exact product copy, identifiers and values are carried verbatim, inside backticks." Proposed: "Only exact product copy, identifiers, values and an open question the source words itself are carried verbatim, inside backticks, so an `**Open:**` line quotes the source's question and then names who settles it." Counterpart: `<K>/Product Owner - Templates - Story Mode - v0.403.md:57`, same sentence. If a rerun still rewords, the next lever is the slot at `story-mode.md:332` (Project :308): "**Open:** {the part that is not decided, or the source's own question verbatim}. {Who decides it, or what evidence settles it.}"
