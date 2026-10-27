---
title: "sk-create-figjam: Manual Testing Playbook"
description: "Operator-facing directory for the FigJam diagram packet: type choice for all seven types, the pre-write check, the board write with its gate, extension and read-back, scored board quality for every type, creation variant and the board design, the boundaries with the Product Owner packet and routing recall for type detection."
version: 1.0.10.0
---

# sk-create-figjam: Manual Testing Playbook

> **EXECUTION POLICY**: Every scenario runs for real against the live packet, with no mocks or stubs. Acceptable verdicts are `PASS`, `FAIL` or `SKIP`, and every `SKIP` names the specific runtime blocker, such as the hosted Figma MCP being unavailable. A run that died before it finished is none of the three, as the run integrity rule in Section 5 sets out.

This playbook tests the `sk-create-figjam` packet of the Product Owner hub. The root is the directory, the review protocol and the orchestration guide, and each scenario file holds its own execution truth. Hub routing scenarios live in `../../manual-testing-playbook/`. The Product Owner Flow scenarios `SFL-001` and `PFL-001`, which cover the skill and the claude.ai Project runtimes, live in `../../sk-product-owner/manual-testing-playbook/`.

Canonical package artifacts:
- `manual-testing-playbook.md`
- `type-choice/`
- `pre-write-check/`
- `board-write/`
- `board-quality/`
- `board-creation/`
- `boundaries/`
- `intra-routing-recall/`

---

### Result persistence

<!-- MANUAL_PLAYBOOK_RESULT_PERSISTENCE_CONTRACT -->
A scenario run is complete only after its `PASS`, `FAIL` or `SKIP` outcome, its reason and its evidence paths are recorded by hand in `../../benchmark/reports/<dated-run-label>/`. An incomplete run is recorded in the same place under its own name, with its cause. Generated report Markdown is renderer-owned and never hand-authored.

---

## 1. OVERVIEW

The packet picks a diagram type from the reader's question, checks a Mermaid model of it, gates the write and reads the board back. The scenarios cover each step for the seven types Flow Mode draws: user flow, process, architecture, sequence, state, ER and gantt. The validator derives the census from the tree, so no count is kept here. Every request uses the fictional Fernhouse, Loomlist and Roamstay companies.

Coverage note (2026-10-20): every type has a type-choice or board-write scenario, a scored board and a routing scenario. The board writes and scored boards need the hosted Figma MCP or Figma Desktop with `figma-ds-cli`, and record SKIP without them.

### Realistic Test Model

1. A realistic request is given to the Product Owner runtime with this packet loaded
2. The runtime picks the type, models, checks and gates, stops at each stop Flow Mode requires before a write and writes only after the gate's yes
3. The operator captures the replies, the tool calls and any check runs
4. A scenario passes only when the process and the visible outcome both hold

### What Each Feature File Should Explain

- The realistic request and why the behavior matters
- The exact prompt and the command sequence
- The expected signals, the evidence, the verdict rules and the triage
- The packet files that justify the scenario

---

## 2. GLOBAL PRECONDITIONS

1. The working directory is the Product Owner repository root
2. Python 3.9 or later is on the path, and `PYTHONPYCACHEPREFIX` points at a scratch folder outside the repository
3. `SKILLED` points at the shared `.skilled` folder for the routing scenarios' topology gate
4. Scratch models live outside the repository and are deleted after the run
5. Record which Figma routes are reachable before any board-write scenario: the hosted Figma MCP with `use_figma` for the composed route and `generate_diagram` for the fallback, and Figma Desktop with the figma-ds-cli daemon
6. Board-write scenarios write to a new FigJam file in a plan the operator owns. The rollback is deleting that file, and no existing board is a target

---

## 3. GLOBAL EVIDENCE REQUIREMENTS

- The user request and the prompt used
- Every reply, verbatim
- Every tool call, with each check run's output and exit status
- The model the check read, with its provenance table
- For a board write, the board URL and the operator's own count of what the board holds
- For a scored board, the planned glance order, the overview screenshot, the colour and greyscale reading screenshots, the two readers' reading orders and answers and the scorecard with one reason, one location and one fix per score
- The verdict with its reason

### Board Quality Scorecard

Every board-quality and board-creation scenario scores the written board at two zooms, from two screenshots of it. The overview screenshot holds the whole board in one frame. The reading screenshot is taken at 100% zoom, and a greyscale copy shows whether the meaning survives without colour. The measures come from `sk-create-figjam/references/quality-rubric.md` Sections 3, 6 and 7 and `sk-create-figjam/references/style-guide.md`. The layout thresholds are this playbook's own.

The operator writes down the glance order the model plans before the first screenshot, so Composition compares a planned order with the order the board shows.

**The overview zoom.** Four dimensions, each 0, 1 or 2, scored on the whole board in one frame.

- **Composition.** 2: the board reads in the planned glance order, and the element the request is about comes first. 1: the order holds and one part comes before that element. 0: two parts read in the reverse of the planned order. The title block is the frame entry and never counts as a part of the glance order. Lanes and zones read as part of the frame on every type, like the title block, and never count as parts, but the nodes inside them do. On a state board the states inside a composite are parts, planned second with their section as `sk-create-figjam/references/types/state.md` Section 5 sets out. A state board is planned as drawn, so the state the focus line marks, or the most telling member of a group the request names such as the end states, is the element the request is about, and the board scores 2 when that state leads its glance line and the rest of the order holds. When `sk-create-figjam/references/quality-rubric.md` Section 3 makes the requested element the second glance, as on a revision that changes an end other than a failure end, the board scores 2 when that element holds the planned second glance and the rest of the order holds. On such a revision the entry, the decisions and every other main-row node the rubric plans last cost no point when they read before the changed end. On a user flow or a process the plan names every node the board draws, the main row the composer draws in the second glance line and every node off it in the last, as `sk-create-figjam/references/quality-rubric.md` Section 3 sets out, so the planned order inside a glance line is path order and the entry and the goal in one line carry no order between them. Content the file held before the write sits outside the glance order, like the title block. A part the plan does not name that reads at or before the planned second glance costs one point, as one part read out of order does. Two fresh readers read each scored board, and a part costs a point only when both readers read it early or out of order
- **Crossings.** 2: no connector crosses another. 1: one crossing. 0: two or more
- **Shared trunks.** Two runs the composer's path estimate keeps at least 56 pixels apart are never a trunk, even where FigJam draws its elbows closer, as `sk-create-figjam/references/style-guide.md` Section 7 sets out. 2: every connector runs alone between its shapes, or a trunk carries only the edges the model draws as one path. 1: one trunk joins two edges the model draws apart. 0: two or more
- **Label collisions.** 2: no two labels touch, and each label sits nearer its own connector than any other. 1: one pair touches. 0: a label covers another or reads as another connector's

**The reading zoom.** Four dimensions, each 0, 1 or 2, scored on the 100% screenshot and its greyscale copy.

- **Fidelity.** Scored against the run's own checked model. 2: every read-back count matches the model and every label matches it word for word. 1: the counts match and one label differs. 0: a count differs. A count or label the scenario expects and the run's model left out is an expected-signal miss, not a Fidelity loss
- **Legibility.** 2: no label is cut off, wrapped mid-word or smaller than its neighbours. 1: one label wraps awkwardly. 0: a label is cut off or unreadable
- **Signal.** 2: every colour the key lists matches its entry and the role `sk-create-figjam/assets/figjam-design.md` gives it, every mark it leaves out passes the rule below, the accent the model sets, a `style` line on a user flow or a process or an optional `%% focus:` line on another type, sits on the element the request names and the greyscale copy answers the reader questions as the colour one does. An accent `sk-create-figjam/references/quality-rubric.md` Section 3 keeps on the goal, as on a revision that changes an end other than a failure end, sits where the request needs it. 1: the accent sits on a different element. 0: a colour the key does not explain and the rule below does not cover, more than one accent in the model or meaning lost in greyscale. Meaning lost in greyscale is a reader question the colour copy answers and the greyscale copy cannot. Two kinds that share a shape differ by outline, as `sk-create-figjam/references/style-guide.md` Section 1 sets out. They score 0 when the board draws two such kinds with the same outline and fills under 25 luma apart, or when a node of either kind carries its meaning by fill alone
- **Clarity.** A fresh reader, a person or a new model session given only the two colour screenshots, answers the scenario's three questions. 2: three correct. 1: two correct. 0: one or none

**Marks the key does not list.** The key holds one sample per kind, line and arrow the board uses and nothing else, so three marks are absent from it by design: a zone or lane tint, a note pin and a legend sticky. A grader scores them against `sk-create-figjam/references/style-guide.md` and the active design in `sk-create-figjam/assets/figjam-design.md`, and never counts their absence from the key as a Signal fault.

- **A zone or lane tint** is a light section tint drawn from the active design's zone cycle, blue, orange, teal, yellow and violet as shipped. A zone skips a tint any kind inside it draws and the tint of any zone it faces along its row or its column, so it never hides its members and neighbouring zones read apart. It means nothing, so two zones in different tints are not two meanings
- **A note pin** is the violet preset with a white digit, and a sequence's step pins are the exception because the key names them `Step number`
- **A legend sticky** takes one colour from the sticky palette, one colour per legend by default

Each counts against Signal only when its colour is outside its palette in the style guide, or when it carries meaning by colour alone with no label to say so. A colour on a drawn node that the key does not list is still a Signal fault.

**The invariants.** Four checks, one point each, scored between the first and the last read.

- **Hygiene, no node touched.** Passes when every node the write drew keeps the position, size and style it was written with. The board section a gated extension widens to hold its notes is the one exception, because `references/hybrid-workflow.md` grows it and returns its size before the call for the rollback
- **Hygiene, no label covered.** Passes when no extension, pin or sticky covers a drawn label
- **Hygiene, nothing else changed.** Passes when no node, section or sticky the run did not create changed
- **Hygiene, nothing exported.** Passes when no file was written to `export/` and no Mermaid, HTML, SVG or PNG file was left behind. The paired artifact's own re-save at its existing export path, which `references/flow-mode.md` Section 8 owns, is the one exception

**The reply.** Two points, scored on the reply text.

- **Reply.** 2: the board URL first, then `Read-back:`, any `Extensions:`, `Left out:` and `Finding:` lines and the `HVR self-scan:` line last, every count true. 1: every line present and true, out of order, or with any text after the `HVR self-scan:` line, even one sentence. 0: a line missing or a count false

A scored board totals 22 points: 8 from the overview zoom, 8 from the reading zoom, 4 from the invariants and 2 from the reply. It passes at 18 or more, with Composition, Fidelity, Reply and all four invariant checks at full marks and no scored dimension at 0. The scorecard is one part of a scored scenario's verdict: the scenario passes only when every expected signal is present as well, as the acceptance rules in Section 5 set out.

Every point lost carries a location and a fix. The location names the shape or the connector by its label and says where it sits in the frame. The fix is a change to the model that is composed again after a yes, or a composer limit the writer cannot move. A point lost with no location or no fix is unmeasured, and an unmeasured point cannot count as a pass.

When Crossings, Shared trunks, Label collisions or Legibility loses a point, the triage records whether the model caused it or the composer did, because the composer owns the geometry and composed nodes are never moved.

---

## 4. DETERMINISTIC COMMAND NOTATION

- Shell commands are written `bash: <command>` and run from the repository root
- Conversation steps are written `session:`, `user:` and `operator:`
- Environment setup is written `sandbox:`
- `<scratch>` is a folder outside the repository
- `->` separates sequential steps
- Every stop Flow Mode makes before a write gets its own `user:` turn with its own wording, because the runner drops a repeated turn. The intake round answers `Use your recommended answers.`, the playback answers `Yes, that reading is right.` and the write gate answers `Yes, go ahead.` A scenario with no intake turn is one whose prompt settles every Brief row. When its run asks an intake round anyway, the operator answers it with the recommended answers before sending the next turn. Each intake round a run opens before the playback beyond those the scenario's expected signals name, up to the energy cap, moves every later turn number in the scenario's expected signals by one, so `Turn 1 ends on the playback` reads as the reply after the last intake round
- A scenario's frontmatter may carry a `driver:` key for the automated run driver. `driver: operator-only` marks a scenario whose setup the driver cannot perform, such as an open Figma Desktop file or a design file edited before the session, so a model run leaves it out and the operator runs it by hand. `driver: new-file` marks a scenario the driver runs with no file pin, so the plan pick and the new file are tested. A scenario with no `driver:` key runs with the pin

---

## 5. REVIEW PROTOCOL AND RELEASE READINESS

### Inputs Required

1. This file and the scenario files under each category folder
2. The evidence above for every executed scenario
3. Triage notes for every outcome that is not `PASS`

### Scenario Acceptance Rules

For each executed scenario, check:

1. The preconditions held
2. The prompt and the commands ran as written
3. Every expected signal is present
4. The evidence is complete and readable
5. The verdict names its reason

Scenario verdict:
- `PASS`: every acceptance check is true
- `FAIL`: an expected signal is missing, the output contradicts the contract or a critical check failed
- `SKIP`: a named sandbox or runtime blocker prevents execution
- Incomplete run: the run began and died before it finished, as the run integrity rule below sets out. It is not a verdict

### Run Integrity

A run is complete only when every turn of the scenario's command sequence was answered and the evidence the scenario names exists. A run that ends earlier has measured nothing past its last answered turn. The usual causes are the runner's timeout, a provider rate limit, a dropped session and a reply cut at the output cap.

- Rerun it in a fresh session once the cause clears, and score the rerun alone. Before a board-write rerun, delete the file the dead run created, because no existing board is a target
- Keep the dead run's evidence and name its cause in the record
- When the run cannot be rerun, record it as an incomplete run with the cause, the last turn answered and the evidence kept. It is not a `SKIP`, because a `SKIP` names a blocker that stopped the scenario before it began, and it is not a `FAIL`, because the packet was never shown to break
- Evidence from before the run died still counts. A breach it already shows, such as a write before the gate's yes, is a `FAIL`
- A rerun follows an incomplete run only. A run that finished and failed stays a `FAIL`, and its rerun never replaces it

### Feature Verdict Rules

- `PASS`: every mapped scenario is `PASS`
- `FAIL`: any mapped scenario is `FAIL`
- `SKIP`: every mapped scenario is blocked by a named sandbox or runtime blocker
- Unrated: a mapped scenario stands as an incomplete run and no other mapped scenario is `FAIL`

Hard rule: a `FAIL` on any scenario that writes to a board, or on the check self-test `FJ-004`, fails the release.

### Release Readiness Rule

The packet is releasable only when no scenario is `FAIL` or an incomplete run, `FJ-004` and every routing scenario are `PASS`, every scenario in the root index has a file, and no blocking triage item stays open.

### Root-vs-Feature Rule

This file holds the shared policy and short summaries. Each scenario file holds its own execution truth and caveats.

---

## 6. SUB-AGENT ORCHESTRATION AND WAVE PLANNING

### Purpose

This section plans the order of a full run. It is not a runtime support matrix.

### Operational Rules

1. Wave 1 runs the shell scenarios with no model runtime: FJ-004, FJ-005, FJ-006, FJ-014, FJ-015, FJ-016, FJ-043 and the routing scenarios
2. Wave 2 runs the conversational type-choice and boundary scenarios, each in a fresh session
3. Wave 3 runs the board writes one at a time, because they share one Figma account: FJ-007, FJ-008, FJ-009, FJ-017, FJ-018, FJ-019
4. Wave 4 runs the scored boards one at a time, and each Clarity read uses a reader who has not seen an earlier board of the same request: FJ-022, FJ-023, FJ-024, FJ-025, FJ-026, FJ-027, FJ-028, FJ-029, FJ-030, FJ-031, FJ-032, FJ-033, FJ-034, FJ-035, FJ-036, FJ-044, FJ-045. FJ-045 edits the shipped design file, so no other scenario runs until its restore step passes
5. After each wave, record the evidence and the verdicts before the next wave starts
6. Record the evidence paths for every scenario in the final report

### What Belongs In Per-Feature Files

- The real user request and the prompt
- The expected process, including which Figma route a write uses
- The desired user-visible outcome
- Scenario-specific caveats and isolation constraints

---

## 7. TYPE CHOICE (`FJ-001`, `FJ-002`, `FJ-003`, `FJ-010`, `FJ-011`, `FJ-012`, `FJ-013`)

Each request becomes a checked model of the type the reader's question needs, and a request the board cannot hold is named as such before any tool call.

### FJ-001 | A sequence picked from an API brief

#### Description

Verify that a request for the order of calls between services becomes a checked sequence model and a gate that waits, with no board written.

#### Scenario Contract

Prompt: `$figjam draw the Roamstay checkout payment as a sequence diagram on a new board in our Roamstay Product plan. From the payments brief: the guest app posts the booking, the booking API holds the room, asks the payment provider to authorise the card, confirms the hold, tells the partner hub and answers the app with 201.`

Expected signals: Turn 1 ends on the playback, which names the sequence type, and shows no model and no write. Turn 2 carries a `sequenceDiagram` model with four declared participants and no aliases, notes or fragments, shows a check run whose last result is `PASSED` with exit 0 and ends on a gate that waits. No write tool is called

Desired user-visible outcome: A checked sequence model of the payment and a gate that waits

#### Test Execution

> **Feature File:** [FJ-001](type-choice/sequence-from-api-brief.md)
> **Catalog:** none, the packet has no feature catalog

### FJ-002 | Two types fit, so one question

#### Description

Verify that a request that an architecture and a sequence both answer gets one question about the reader's question before any model is written.

#### Scenario Contract

Prompt: `make a FigJam diagram of how Loomlist block sync works`

Expected signals: The reply asks exactly one question, names the architecture and the sequence by the question each answers, writes no model, runs no check and calls no write tool

Desired user-visible outcome: One plain question that lets the user pick the board they need

#### Test Execution

> **Feature File:** [FJ-002](type-choice/two-types-fit-asks.md)
> **Catalog:** none, the packet has no feature catalog

### FJ-003 | A kind Flow Mode does not draw

#### Description

Verify that a request for a mindmap is refused plainly with the nearest useful form offered, and no board tool is called.

#### Scenario Contract

Prompt: `$figjam a mindmap of the Roamstay launch themes: guest trust, partner onboarding, pricing and reviews`

Expected signals: The reply says Flow Mode does not draw a mindmap, offers a table or a list in a Doc and calls no Figma tool

Desired user-visible outcome: A plain refusal with a useful alternative

#### Test Execution

> **Feature File:** [FJ-003](type-choice/unsupported-kind-offers-nearest.md)
> **Catalog:** none, the packet has no feature catalog

### FJ-010 | A user flow from a product doc

#### Description

Verify that a screen-by-screen request becomes a user flow of at most 9 nodes with labelled decision exits and a gate that waits.

#### Scenario Contract

Prompt: `$flow make a FigJam flow of Fernhouse returns on a new board in our Fernhouse Product plan. From the returns doc: the customer opens an order, taps Return an item, picks the item and a reason, and if the order is older than 30 days they see a not-eligible screen. Otherwise they choose a refund or store credit, print the label and see a confirmation.`

Expected signals: Turn 1 ends on the playback and shows no model. Turn 2 carries a model with at most 9 nodes, every decision exit labelled, camelCase ids and no `%% type:` line, the check prints `user flow: ok` with exit 0, and the gate waits. No write tool is called

Desired user-visible outcome: A checked returns flow and a gate that waits

#### Test Execution

> **Feature File:** [FJ-010](type-choice/user-flow-from-product-doc.md)
> **Catalog:** none, the packet has no feature catalog

### FJ-011 | A laned process with the handoff in focus

#### Description

Verify that work that changes hands between teams becomes a process with one lane per actor and one `style` line that puts the handoff step in focus, where each lane takes the neutral pair or no style.

#### Scenario Contract

Prompt: `draw how a Fernhouse damaged-item refund moves between the customer, a CS agent and the warehouse as a FigJam process on a new board in our Fernhouse Product plan, and highlight the handoff to the warehouse`

Expected signals: Turn 1 ends on the playback and shows no model. Turn 2 carries a model that opens with `%% type: process`, holds 2 to 6 lanes, each with the neutral pair `#F5F5F5` and `#B3B3B3` or no style, and carries one `style` line from the style guide on the step that hands the work to the warehouse and no `linkStyle`. The check prints `process: ok` with exit 0. The gate waits

Desired user-visible outcome: A checked laned process and a gate that waits

#### Test Execution

> **Feature File:** [FJ-011](type-choice/laned-process-from-handoffs.md)
> **Catalog:** none, the packet has no feature catalog

### FJ-012 | An architecture through the six lanes

#### Description

Verify that a system request becomes an architecture in Figma's six lanes with no styling, cut to budget with the cut named and a gate that names the composed board in its lanes.

#### Scenario Contract

Prompt: `draw the services behind Loomlist block sync as a FigJam architecture diagram on a new board in our Loomlist Engineering plan: desktop, web and iOS clients, an API gateway, sync-service, a push worker, the blocks database, file storage, a change stream and Apple's push service`

Expected signals: Turn 1 ends on an intake round that asks for the calls between the parts with a recommended answer for each, and shows no model. Turn 2 ends on the playback and shows no model. Turn 3 carries a model with at most 9 nodes, no `style` or `classDef`, dotted edges for async and external calls, a `Left out:` line naming file storage, the check prints `architecture: ok`, and the gate names the composed board in its six lanes and waits

Desired user-visible outcome: A checked architecture with the cut named and a gate that waits

#### Test Execution

> **Feature File:** [FJ-012](type-choice/architecture-with-layout-code.md)
> **Catalog:** none, the packet has no feature catalog

### FJ-013 | A timeline offered as a gantt chart

#### Description

Verify that a request for a timeline, which Flow Mode does not draw, is named as such and offered as a gantt chart with each event as a milestone.

#### Scenario Contract

Prompt: `$figjam a timeline of the Loomlist offline mode milestones: design done 16 November, beta on 7 December, release on 21 December`

Expected signals: The reply names the timeline as a kind Flow Mode does not draw, offers a gantt chart with milestones and calls no Figma tool

Desired user-visible outcome: A clear offer of the nearest drawable type

#### Test Execution

> **Feature File:** [FJ-013](type-choice/timeline-offers-gantt.md)
> **Catalog:** none, the packet has no feature catalog

---

## 8. PRE-WRITE CHECK (`FJ-004`, `FJ-005`, `FJ-006`, `FJ-014`, `FJ-015`, `FJ-016`, `FJ-043`)

The check refuses what the composer or the generated fallback would drop or mangle, and its self-test proves every rule fires. These run from a shell with no model runtime.

### FJ-004 | The self-test covers every type

#### Description

Verify that the check's self-test passes every planted defect and every template, example and Project mirror of all seven types.

#### Scenario Contract

Prompt: `As the operator, run the sk-create-figjam self-test against the packet. Verify every check passes and every template and example is read. Return the summary line and exit status.`

Expected signals: The self-test ends `<n> of <n> self-test checks passed` with exit 0, and every template and example prints `PASSED`. A sandbox install that leaves out `claude project/` prints `SKIP  <file> is not in this install` for each Project mirror, which is expected there, because `benchmark/gates/run_gates.sh` runs the same self-test in the repository with the mirror present

Desired user-visible outcome: A self-test that proves every rule fires

#### Test Execution

> **Feature File:** [FJ-004](pre-write-check/self-test-every-type.md)
> **Catalog:** none, the packet has no feature catalog

### FJ-005 | A sequence with an alias and a note is refused

#### Description

Verify that the check refuses a sequence model that uses an alias and a note, naming each rule.

#### Scenario Contract

Prompt: `As the operator, run the sk-create-figjam check on a sequence model with a terse participant id G aliased as GuestApp and a note. Verify it fails and names all three rules. Return the output and exit status.`

Expected signals: The output names the alias, the note and the short id, ends `FAILED 1 of 1 diagram(s)` and exits 1

Desired user-visible outcome: A refusal that says what to change

#### Test Execution

> **Feature File:** [FJ-005](pre-write-check/planted-defect-refused.md)
> **Catalog:** none, the packet has no feature catalog

### FJ-006 | A pie block is refused by the check

#### Description

Verify that the check refuses a Mermaid block whose kind Flow Mode does not draw.

#### Scenario Contract

Prompt: `As the operator, run the sk-create-figjam check on a pie chart model. Verify it fails and points at the type table. Return the output and exit status.`

Expected signals: The output names a pie block as undrawable, points at `references/flow-mode.md` Section 3 and exits 1

Desired user-visible outcome: A refusal that points at the nearest drawable type

#### Test Execution

> **Feature File:** [FJ-006](pre-write-check/unsupported-header-refused.md)
> **Catalog:** none, the packet has no feature catalog

### FJ-014 | A ten-node user flow is refused

#### Description

Verify that the check refuses a user flow of 10 nodes and tells the writer to split it.

#### Scenario Contract

Prompt: `As the operator, run the sk-create-figjam check on a straight user flow of 10 nodes. Verify it fails on the node budget. Return the output and exit status.`

Expected signals: The output reads `10 nodes, at most 9: split the flow` and exits 1

Desired user-visible outcome: A refusal that names the budget

#### Test Execution

> **Feature File:** [FJ-014](pre-write-check/user-flow-over-budget.md)
> **Catalog:** none, the packet has no feature catalog

### FJ-015 | An off-palette fill is refused

#### Description

Verify that the check refuses a fill that is not one of FigJam's light pairs and points at the style guide.

#### Scenario Contract

Prompt: `As the operator, run the sk-create-figjam check on a user flow whose end node is filled #00FF00. Verify it fails on the palette. Return the output and exit status.`

Expected signals: The output reads `fill #00ff00 is not a FigJam light fill: pick a pair from references/style-guide.md` and exits 1

Desired user-visible outcome: A refusal that points at the palette

#### Test Execution

> **Feature File:** [FJ-015](pre-write-check/off-palette-colour-refused.md)
> **Catalog:** none, the packet has no feature catalog

### FJ-016 | A styled architecture is refused

#### Description

Verify that the check refuses an otherwise valid architecture that carries one `style` line.

#### Scenario Contract

Prompt: `As the operator, run the sk-create-figjam check on the Loomlist architecture example with one style line added. Verify it fails on styling alone. Return the output and exit status.`

Expected signals: The output reads `the block carries styling: the architecture layout colours each lane itself, drop it`, names no other rule and exits 1

Desired user-visible outcome: A refusal that names styling as the one defect

#### Test Execution

> **Feature File:** [FJ-016](pre-write-check/architecture-styling-refused.md)
> **Catalog:** none, the packet has no feature catalog

### FJ-043 | A rank of five steps is refused

#### Description

Verify that the check measures the layout of a legal user flow and refuses one whose widest rank holds five steps.

#### Scenario Contract

Prompt: `As the operator, run the sk-create-figjam check on a user flow whose start branches into five parallel steps. Verify it fails on the layout measures. Return the output and exit status.`

Expected signals: The output reads `a rank holds 5 steps, at most 4: split the flow so a rank reads at a glance` and exits 1, and a passing model prints its widest rank, longest path, connectors per step, label average and crossing pairs beside the counts

Desired user-visible outcome: A refusal that names the layout measure and its budget

#### Test Execution

> **Feature File:** [FJ-043](pre-write-check/layout-measures-refuse-a-wide-rank.md)
> **Catalog:** none, the packet has no feature catalog

---

## 9. BOARD WRITE (`FJ-007`, `FJ-008`, `FJ-009`, `FJ-017`, `FJ-018`, `FJ-019`)

The gate, the write, the extension and the read-back. Scenarios that need a Figma route record SKIP with that route named as the blocker when it is unavailable.

### FJ-007 | The gate names a planned extension

#### Description

Verify that a state diagram request that asks for notes the model cannot carry ends on a gate that names the notes as an extension, before any write.

#### Scenario Contract

Prompt: `$figjam the Roamstay booking status lifecycle on a new board in our Roamstay Product plan, and add a short note on Cancelled and on No-show saying who sets each, so support knows who to ask. Pending until the card is authorised, then Confirmed, which covers Upcoming and In stay. Check-out ends it as Completed. A guest can cancel while Pending or Confirmed, and the hotel marks No-show after a missed check-in.`

Expected signals: Turn 1 ends on the playback and writes nothing. After the playback's yes, the model's header is `stateDiagram-v2` with no styling and the check passes. Turn 2 ends on the gate, which names the plan, a new file, the composed state diagram, two single-sticky notes on Cancelled and NoShow, the calls the write will spend and the rollback, then waits. The gate plans no colour step, because the composer already draws the end states light gray and names them Final state in the key. No write tool is called

Desired user-visible outcome: A checked state model and a gate that names both writes

#### Test Execution

> **Feature File:** [FJ-007](board-write/gate-names-extension.md)
> **Catalog:** none, the packet has no feature catalog

### FJ-008 | A written ER diagram is read back

#### Description

Verify that with the hosted Figma MCP connected, a yes writes an ER diagram, the board is read back node by node and the reply carries the measured counts.

#### Scenario Contract

Prompt: `$figjam an ER diagram of the Roamstay stays model on a new board in our Roamstay Product plan: a guest makes bookings, a booking holds payments, a room is reserved by bookings, a rate plan prices bookings, and a property offers rooms and publishes rate plans. Keep the keys only.`

Expected signals: Turn 1 ends on the playback and writes nothing. Turn 2 ends on the gate and writes nothing. Turn 3 calls `whoami`, `create_new_file`, one `use_figma` and one `get_figjam`, and replies with the board URL first, a `Read-back:` line counting entities, relationships and attributes, and the `HVR self-scan:` line

Desired user-visible outcome: A board link with counts measured on the board

#### Test Execution

> **Feature File:** [FJ-008](board-write/write-and-read-back.md)
> **Catalog:** none, the packet has no feature catalog

### FJ-009 | A gantt chart with no route

#### Description

Verify that a yes on a gantt chart with no hosted Figma MCP names the missing route, says the `fj` route cannot draw a gantt chart, offers the checked model and claims no board.

#### Scenario Contract

Prompt: `put the Loomlist offline mode launch plan on a FigJam gantt chart in a new board in our Loomlist Product plan. Design starts 2 November for two weeks, the sync engine takes three weeks from the same day, the conflict screen build follows design for two weeks, integration starts when both are done for one week, then a two-week beta and the release.`

Expected signals: Turn 1 ends on the playback and writes nothing. Turn 2 ends on the gate, which names the missing route in place of the plan and the calls, and writes nothing. Turn 3 names the hosted Figma MCP as not connected and what it needs, says the `fj` route cannot draw a gantt chart, offers the checked model and prints no board URL or `Read-back:` line

Desired user-visible outcome: A plain account of the missing route with the checked model to keep

#### Test Execution

> **Feature File:** [FJ-009](board-write/gantt-with-no-route.md)
> **Catalog:** none, the packet has no feature catalog

### FJ-017 | Notes land after the write

#### Description

Verify that after a yes that named notes, the state diagram is composed with one `use_figma` call and the notes are added with a second `use_figma` call inside the board as single stickies, no composed node moves and the reply carries an `Extensions:` line.

#### Scenario Contract

Prompt: `$figjam the Roamstay booking status lifecycle on a new board in our Roamstay Product plan, and add a short note on Cancelled and on No-show saying who sets each, so support knows who to ask. Pending until the card is authorised, then Confirmed, which covers Upcoming and In stay. Check-out ends it as Completed. A guest can cancel while Pending or Confirmed, and the hotel marks No-show after a missed check-in.`

Expected signals: When every side of Cancelled or NoShow is taken, Turn 2's gate says so and offers pins with a legend or a recompose with more room, the run follows the option the operator picks and the two-call and `Extensions:` signals apply only to the single-sticky option. Turn 1 ends on the playback and Turn 2 ends on the gate, and both write nothing. Turn 3 calls `use_figma` twice, once to compose the board and once to add the two notes as single stickies, with no pin and no legend column. It moves no composed node, draws no colour, places the second sticky below or to the left of its node when the two noted nodes sit on adjacent rows and replies with the board URL, a `Read-back:` line, `Extensions: 2 of 2 notes, 0 overlaps`, a `Finding:` line naming any sticky that sits below or left of its node and the `HVR self-scan:` line

Desired user-visible outcome: A board with a note beside Cancelled and beside NoShow and both writes counted

#### Test Execution

> **Feature File:** [FJ-017](board-write/hybrid-extension-written.md)
> **Catalog:** none, the packet has no feature catalog

### FJ-018 | A user flow through the fj fallback

#### Description

Verify that with no hosted route but `figma-ds-cli` reachable, a user flow is written node by node into the FigJam file open in Figma Desktop after a gate that names it.

#### Scenario Contract

Prompt: `$flow make a FigJam flow of Fernhouse returns in the board I have open in Figma Desktop. From the returns doc: the customer opens an order, taps Return an item, picks the item and a reason, and if the order is older than 30 days they see a not-eligible screen. Otherwise they choose a refund or store credit, print the label and see a confirmation.`

Expected signals: Turn 1 ends on the playback and writes nothing. Turn 2 writes nothing and ends on the gate, which names the open FigJam file from `fj info`. Turn 3 uses only create verbs, never `fj delete` or `fj eval`, and replies with a `Read-back:` line counting nodes, connectors and labelled exits

Desired user-visible outcome: The flow on the open board with counts measured by `fj nodes -l`

#### Test Execution

> **Feature File:** [FJ-018](board-write/fj-route-user-flow.md)
> **Catalog:** none, the packet has no feature catalog

### FJ-019 | An architecture composed in its six lanes

#### Description

Verify that with the hosted Figma MCP connected, one `use_figma` call composes the architecture with its lanes as columns and the read-back counts its lanes.

#### Scenario Contract

Prompt: `draw the services behind Loomlist block sync as a FigJam architecture diagram on a new board in our Loomlist Engineering plan: desktop, web and iOS clients, an API gateway, sync-service, a push worker, the blocks database, file storage, a change stream and Apple's push service`

Expected signals: Turn 1 writes nothing and ends on an intake round that asks for the calls between the parts with a recommended answer for each. Turn 2 ends on the playback and writes nothing. Turn 3 ends on the gate and writes nothing. Turn 4 writes after the gate's yes. The one `use_figma` call carries the code `compose_board.py` printed. The board holds six lane sections as columns, left to right as client, gateway, service, async, datastore and external, with each part inside its lane. The reply's `Read-back:` line counts nodes, connectors and lanes. When `use_figma` is not connected and the generated fallback runs, its one `generate_diagram` call also carries `useArchitectureLayoutCode: "FIGMA_DIAGRAM_2026"`, which is recorded as a secondary signal

Desired user-visible outcome: An architecture board in lanes with counts measured on it

#### Test Execution

> **Feature File:** [FJ-019](board-write/architecture-write-lanes.md)
> **Catalog:** none, the packet has no feature catalog

---

## 10. BOARD QUALITY (`FJ-022`, `FJ-023`, `FJ-024`, `FJ-025`, `FJ-026`, `FJ-027`, `FJ-028`, `FJ-044`, `FJ-045`)

One written board per diagram type, scored on the board quality scorecard in Section 3 at two zooms. The overview screenshot scores composition, crossings, shared trunks and label collisions. The 100% screenshot scores fidelity, legibility and signal. The four hygiene checks and the reply close the run. Each scenario names three reader questions with its answers, so clarity is measured, not judged. Two more check the design every type is drawn in: the seven types side by side under the shipped design, and a broken design that falls back token by token.

### FJ-022 | User flow board quality

#### Description

Verify that a written user flow is legible, laid out left to right in three zones, draws its goal and its exit by kind and answers a fresh reader's questions from the screenshot alone.

#### Scenario Contract

Prompt: `$flow how a Fernhouse customer starts a return in the app, on a new board in our Fernhouse Product plan. From the app and the returns doc: the order list, the order detail with a Start a return button, a list of return reasons, a choice between a drop-off point and a courier pickup, and a confirmation with a QR code. Returns are open for 30 days after delivery, after that the app shows Contact support. A free pickup for orders over 100 euros is a proposal under review.`

Expected signals: Turn 1 ends on the playback and writes nothing. Turn 2 ends on the gate and writes nothing. Turn 3 writes after the gate's yes. The board holds every node of the model within 9, every connector and 2 of 2 decisions with every exit labelled, left to right in three zones. The goal Return confirmed is light green and Contact support is a light orange exit. The reply carries `Left out:` naming the proposal. The scorecard totals at least 18 of 22, with Composition, Fidelity, the four Hygiene checks and Reply at full marks and no scored dimension at 0

Desired user-visible outcome: A board that reads in its planned order at both zooms, with every count measured

#### Test Execution

> **Feature File:** [FJ-022](board-quality/user-flow-board-quality.md)
> **Catalog:** none, the packet has no feature catalog

### FJ-023 | Process board quality

#### Description

Verify that a written process keeps each step in its lane, puts the one handoff step the request names in focus and reads in greyscale.

#### Scenario Contract

Prompt: `make a FigJam process of how a Fernhouse damaged-item refund moves between the customer, CS and the warehouse, on a new board in our Fernhouse Product plan, and highlight the handoff to the warehouse. From the support runbook: the customer reports damage with a photo through the help form. A CS agent checks the photo, approves clear damage on the spot and asks for a second photo when it is unclear. An approved claim goes to the warehouse queue, where an operator books a courier pickup, inspects the item on arrival and releases the refund. Every decision is logged in the claims table. Refunds under 20 euros skip the pickup, a pilot that is not yet live.`

Expected signals: Turn 1 ends on the playback and writes nothing. Turn 2 ends on the gate and writes nothing. Turn 3 writes after the gate's yes. The board holds 8 of 8 nodes, 8 of 8 connectors, 1 of 1 decision with both exits labelled and 3 of 3 lanes, each step in its lane. The only mark is Approve the claim drawn in focus in light pink with the pink outline and named In focus in the key. Every other step keeps the colour of its kind. The greyscale copy still answers Q3 from the lane labels. The scorecard totals at least 18 of 22, with Composition, Fidelity, the four Hygiene checks and Reply at full marks and no scored dimension at 0

Desired user-visible outcome: A board that reads in its planned order at both zooms, with every count measured

#### Test Execution

> **Feature File:** [FJ-023](board-quality/process-board-quality.md)
> **Catalog:** none, the packet has no feature catalog

### FJ-024 | Architecture board quality

#### Description

Verify that a written architecture places every part in its layout lane, draws asynchronous calls dotted and lets a fresh reader trace a request.

#### Scenario Contract

Prompt: `draw the services behind Loomlist block sync as a FigJam architecture diagram on a new board in our Loomlist Engineering plan: desktop, web and iOS clients, an API gateway, sync-service, a push worker, the blocks database, file storage, a change stream and Apple's push service. Clients hold a live socket to the gateway, sync-service writes every block change and publishes it to the change stream, and the push worker reads the stream and wakes sleeping iOS devices.`

Expected signals: Turn 1 ends on the playback and writes nothing. Turn 2 ends on the gate and writes nothing. Turn 3 writes after the gate's yes. The board holds 9 of 9 nodes, 8 of 8 connectors and 6 of 6 lanes, with the three event edges dotted. No node carries a fill the model set, the dotted edges stay distinct in the greyscale copy, and the reply names file storage under `Left out:`. The scorecard totals at least 18 of 22, with Composition, Fidelity, the four Hygiene checks and Reply at full marks and no scored dimension at 0

Desired user-visible outcome: A board that reads in its planned order at both zooms, with every count measured

#### Test Execution

> **Feature File:** [FJ-024](board-quality/architecture-board-quality.md)
> **Catalog:** none, the packet has no feature catalog

### FJ-025 | Sequence board quality

#### Description

Verify that a written sequence keeps participants in call order left to right, keeps reply arrows distinct from calls and lets a reader follow one booking.

#### Scenario Contract

Prompt: `$figjam draw the Roamstay checkout payment as a sequence diagram on a new board in our Roamstay Product plan. From the payments brief: the guest app posts the booking, the booking API holds the room, asks the payment provider to authorise the card, confirms the hold, tells the partner hub and answers the app with 201. A declined card releases the hold and returns 402.`

Expected signals: Turn 1 ends on the playback and writes nothing. Turn 2 ends on the gate and writes nothing. Turn 3 writes after the gate's yes. The board holds 4 of 4 participants and 7 of 7 messages, participants left to right as GuestApp, BookingApi, PaymentProvider and PartnerHub. Replies are dashed and the async message has an open arrow, both still distinct in greyscale, and the reply names the declined path under `Left out:`. The scorecard totals at least 18 of 22, with Composition, Fidelity, the four Hygiene checks and Reply at full marks and no scored dimension at 0

Desired user-visible outcome: A board that reads in its planned order at both zooms, with every count measured

#### Test Execution

> **Feature File:** [FJ-025](board-quality/sequence-board-quality.md)
> **Catalog:** none, the packet has no feature catalog

### FJ-026 | State board quality

#### Description

Verify that a written state diagram has its end states drawn light gray by the composer, the Confirmed composite drawn as a named zone around its substates and every transition labelled, with no tint.

#### Scenario Contract

Prompt: `$figjam the Roamstay booking status lifecycle on a new board in our Roamstay Product plan, and colour the end states so support can spot them. Pending until the card is authorised, then Confirmed, which covers Upcoming and In stay. Check-in moves Upcoming to In stay. Check-out ends it as Completed. A guest can cancel while Pending or Confirmed, and the hotel marks No-show after a missed check-in.`

Expected signals: Turn 1 ends on the playback and writes nothing. Turn 2 ends on the gate and writes nothing. Turn 3 writes after the gate's yes. The board holds every state of the model, every transition with its label and the Confirmed composite as a named zone around Upcoming and InStay. Completed, Cancelled and NoShow are light gray, as the key's Final state entry says. No tint sits behind them. No extension call is made and the reply carries no `Extensions:` line. The scorecard totals at least 18 of 22, with Composition, Fidelity, the four Hygiene checks and Reply at full marks and no scored dimension at 0

Desired user-visible outcome: A board that reads in its planned order at both zooms, with every count measured

#### Test Execution

> **Feature File:** [FJ-026](board-quality/state-board-quality.md)
> **Catalog:** none, the packet has no feature catalog

### FJ-027 | ER board with domain zones quality

#### Description

Verify that a written ER diagram keeps every relationship's two ends and cardinality readable and separates the guest and partner tables with two `%% zone:` sections.

#### Scenario Contract

Prompt: `make a FigJam ER diagram of the Roamstay stays model on a new board in our Roamstay Product plan, and group the partner tables apart from the guest tables. From the schema note: guests, bookings, payments, properties, rooms and rate plans. A guest makes bookings, a booking reserves one room under one rate plan and holds its payments, and a property offers rooms and publishes rate plans. Keep the keys and the few columns support asks about.`

Expected signals: Turn 1 ends on the playback and writes nothing. Turn 2 ends on the gate and writes nothing. Turn 3 writes after the gate's yes. The board holds 6 of 6 entities, 6 of 6 relationships with their labels and every attribute of the model, in 2 of 2 zones. The Guest side zone holds Guest, Booking and Payment and the Partner side zone holds Property, Room and Rate Plan. Neither zone covers a label. Each relationship's cardinality reads from the marks at its two ends and from its label, such as `makes (1 to 0..n)`, at 100% zoom. No extension call is made and the reply carries no `Extensions:` line. The scorecard totals at least 18 of 22, with Composition, Fidelity, the four Hygiene checks and Reply at full marks and no scored dimension at 0

Desired user-visible outcome: A board that reads in its planned order at both zooms, with every count measured

#### Test Execution

> **Feature File:** [FJ-027](board-quality/er-board-quality.md)
> **Catalog:** none, the packet has no feature catalog

### FJ-028 | Gantt board quality

#### Description

Verify that a written gantt chart keeps task order, dependencies and the milestone readable, marks the critical task and lets a reader find the release date.

#### Scenario Contract

Prompt: `put the Loomlist offline mode launch plan on a FigJam gantt chart in a new board in our Loomlist Product plan. Design starts 2 November 2026 with two weeks of conflict-screen design, the sync engine takes three weeks from the same day, the conflict screen build follows its design for two weeks, and desktop and iOS integration starts when both builds are done, one week, and is the critical path. Then a two-week beta for 5 percent of workspaces and the release. Android follows in the next quarter, not yet approved.`

Expected signals: Turn 1 ends on the playback and writes nothing. Turn 2 ends on the gate and writes nothing. Turn 3 writes after the gate's yes. The board holds 3 of 3 sections, 5 of 5 tasks and 1 of 1 milestone in the model's order. Integration carries the critical marking and the reply names Android under `Left out:`. Every `after` in the model is drawn as an arrow from the bar it names, and the reader reads order from the bars and the arrows, not the bar lengths. The scorecard totals at least 18 of 22, with Composition, Fidelity, the four Hygiene checks and Reply at full marks and no scored dimension at 0

Desired user-visible outcome: A board that reads in its planned order at both zooms, with every count measured

#### Test Execution

> **Feature File:** [FJ-028](board-quality/gantt-board-quality.md)
> **Catalog:** none, the packet has no feature catalog

### FJ-044 | Seven boards read as one family

#### Description

Verify that the seven shipped examples composed under the shipped design share one title block, one type scale, one key layout and order, one set of line looks and one zone tint rule.

#### Scenario Contract

Prompt: `As the operator, compose the seven sk-create-figjam examples onto one new FigJam file in a plan you own and compare their furniture: the title block, the type sizes, the key, the line looks and the zone tints. Return the seven overview screenshots and the comparison.`

Expected signals: The design check exits 0 with `THEME {}`. Each example prints a `COMPOSED` line drawn in the design `FigJam default` with no `DESIGN` line. Every board opens on the same title block, every key is a light gray section titled `Key` with its entries in the design file's kind order and `In focus` last, every connector is gray except an async message and the accent, participants are white and no zone shares a hue with a node inside it. Every board scores 2 on the rubric's `Matches the active design` criterion

Desired user-visible outcome: Seven boards that a reader who has learned one can read without learning the others

#### Test Execution

> **Feature File:** [FJ-044](board-quality/design-family-across-types.md)
> **Catalog:** none, the packet has no feature catalog

### FJ-045 | A broken design falls back with named findings

#### Description

Verify that a design file with a pink zone tint, the accent's pair on a role and an unknown group still draws the board in the shipped value for each bad token, and that the reply names each fallback on its own `Finding:` line.

#### Scenario Contract

Prompt: `$flow how a Fernhouse customer starts a return in the app, on a new board in our Fernhouse Product plan. From the app and the returns doc: the order list, the order detail with a Start a return button, a list of return reasons, a choice between a drop-off point and a courier pickup, and a confirmation with a QR code. Returns are open for 30 days after delivery, after that the app shows Contact support.`

Expected signals: The design check prints three `DESIGN` lines naming `shadow`, `role.goal` and `zone.cycle` and exits 1. The compose prints the same three lines and a `COMPOSED` line ending `3 design warnings`. The board is written after the gate's yes with a light green goal that is not pink, no pink zone and the accented node read back as the first glance, the reply carries three `Finding:` lines above the `HVR self-scan:` line and the restored design file shows no change. A fresh reader answers from the colour screenshot. Q1: What does a customer see more than 30 days after delivery? Answer: Contact support. Q2: Which two ways can the item go back? Answer: a drop-off point or a courier pickup. Q3: Where does a return end? Answer: Return confirmed with a QR code.

Desired user-visible outcome: A board drawn in the shipped look for the three bad tokens, and a reply that says which tokens fell back and why

#### Test Execution

> **Feature File:** [FJ-045](board-quality/broken-design-falls-back.md)
> **Catalog:** none, the packet has no feature catalog

---

## 11. BOARD CREATION (`FJ-029`, `FJ-030`, `FJ-031`, `FJ-032`, `FJ-033`, `FJ-034`, `FJ-035`, `FJ-036`)

The ways a board gets made beyond one fresh write: a split across two diagrams, pins and a legend, a revision, a board that already holds content, a leadership audience, a colour request answered with lanes, the fj route and a flow at the budget. Each is scored on the same scorecard.

### FJ-029 | A flow over budget split into two boards in one file

#### Description

Verify that a request too long for one user flow becomes two composed boards in one file, the second composed into the first one's file, titled `1. Sign up` and `2. Workspace setup`, placed left to right 400 pixels apart with no overlap and the reply naming the board to open first.

#### Scenario Contract

Prompt: `$flow the Loomlist signup and first workspace setup on a new board in our Loomlist Product plan. From the onboarding doc: the landing page, sign up with email or Google, verify the email code, where a wrong code shows an error with a resend, pick a free or team plan, where a team plan asks for teammates' emails and lets you skip, name the workspace, pick a template or start blank, and the editor opens with a welcome tip.`

Expected signals: Turn 1 ends on the playback and writes nothing. Turn 2 ends on the gate and writes nothing. Turn 3 writes after the gate's yes. The file holds two composed boards, Sign up and Workspace setup, each within 9 nodes and titled `1. Sign up` and `2. Workspace setup`, the second 400 pixels to the right of the first with its top level, with one shared hand-off label where the first ends and the second starts. The second `use_figma` call carries the first call's fileKey, the boards do not overlap and neither sits inside the other. Each title reads as its ordinal and the diagram's name. The read-back line names `start here: 1. Sign up`, that one line counts both diagrams and `Left out:` names the split. The scorecard totals at least 18 of 22, with Composition, Fidelity, the four Hygiene checks and Reply at full marks and no scored dimension at 0

Desired user-visible outcome: A board that reads in its planned order at both zooms, with every count measured

#### Test Execution

> **Feature File:** [FJ-029](board-creation/split-flow-one-board.md)
> **Catalog:** none, the packet has no feature catalog

### FJ-030 | Numbered pins with a sticky legend

#### Description

Verify that three notes the request asks for land as violet numbered pins on the named nodes with a matching sticky column inside the board to the right, covering no label.

#### Scenario Contract

Prompt: `$flow how a Fernhouse customer starts a return in the app, on a new board in our Fernhouse Product plan. From the app and the returns doc: the order list, the order detail with a Start a return button, a list of return reasons, a choice between a drop-off point and a courier pickup, and a confirmation with a QR code. Returns are open for 30 days after delivery, after that the app shows Contact support. A free pickup for orders over 100 euros is a proposal under review. Pin the three places support says customers give up, with a note on each: the reason list, where there are too many reasons, the drop-off or pickup choice, where the pickup fee is unclear, and the 30-day cut-off, where there is no warning before day 30.`

Expected signals: Turn 1 ends on the playback and writes nothing. Turn 2 ends on the gate and writes nothing. Turn 3 writes after the gate's yes. The board holds the flow of FJ-022, 3 of 3 pins and 3 of 3 legend stickies. Each pin is 48 by 48 in violet `#874FFF` with a white digit on its node's top-left corner, or on the top vertex of a diamond such as the drop-off or pickup choice, and is named `pin:1` to `pin:3`. The stickies are named `note:1` to `note:3` and stand in one column inside the board, 200 pixels to the right of the diagram, each starting with its number. The board is widened to hold the column and no composed node moves. No pin or sticky covers a label and the sticky colour shows as a palette swatch in FigJam's picker. The reply carries `Extensions: 3 of 3 pins, 3 of 3 legend stickies, 0 overlaps`. The scorecard totals at least 18 of 22, with Composition, Fidelity, the four Hygiene checks and Reply at full marks and no scored dimension at 0

Desired user-visible outcome: A board that reads in its planned order at both zooms, with every count measured

#### Test Execution

> **Feature File:** [FJ-030](board-creation/pins-and-legend.md)
> **Catalog:** none, the packet has no feature catalog

### FJ-031 | A revision replaces the diagram on its own board

#### Description

Verify that a change to a written flow composes the new board first, reads it back, then after its own yes deletes the old board section found by its tag and leaves one board in the file.

#### Scenario Contract

Prompt: `change the Fernhouse return flow on that board: after 30 days the app now shows Request an exception instead of Contact support`

Expected signals: Turn 1 reads the board with get_figjam, ends on the playback and writes nothing. Turn 2 ends on the gate for the compose and writes nothing. Turn 3 composes the new board, reads it back, asks before deleting in a question that names the old board by its title and its write time and deletes nothing. Turn 4 deletes the old board section. The file ends with one board, every node of the model within 9 and every connector, with Request an exception in place of Contact support. The new board is composed and read back before anything is deleted. The gate's yes covers the compose and never the delete. The delete waits for its own yes, asked after the read-back. It removes only the old board section found by its tag. The operator's sticky is untouched and the compose call carries the same fileKey. The scorecard totals at least 18 of 22, with Composition, Fidelity, the four Hygiene checks and Reply at full marks and no scored dimension at 0

Desired user-visible outcome: A board that reads in its planned order at both zooms, with every count measured

#### Test Execution

> **Feature File:** [FJ-031](board-creation/revision-same-board.md)
> **Catalog:** none, the packet has no feature catalog

### FJ-032 | A write onto a board with content

#### Description

Verify that a diagram composed into an existing board lands clear of the content already there and changes none of it.

#### Scenario Contract

Prompt: `$figjam add the Roamstay booking status lifecycle to our existing retro board <fileKey of the prepared board>. Pending until the card is authorised, then Confirmed, which covers Upcoming and In stay. Check-out ends it as Completed. A guest can cancel while Pending or Confirmed, and the hotel marks No-show after a missed check-in.`

Expected signals: Turn 1 ends on the playback and writes nothing. Turn 2 ends on the gate and writes nothing. Turn 3 writes after the gate's yes. The board holds every state and labelled transition of the model, and every node that was on the board before, at its old position. The prepared stickies and section keep their count, positions and sizes between the two reads. The new board lands 400 pixels to the right of the rightmost existing content with its top level with the highest node there, and its bounds overlap none of them. The scorecard totals at least 18 of 22, with Composition, Fidelity, the four Hygiene checks and Reply at full marks and no scored dimension at 0

Desired user-visible outcome: A board that reads in its planned order at both zooms, with every count measured

#### Test Execution

> **Feature File:** [FJ-032](board-creation/existing-board-with-content.md)
> **Catalog:** none, the packet has no feature catalog

### FJ-033 | An architecture written for leadership

#### Description

Verify that the same system asked for a leadership audience lands with capability names and fewer parts than the engineering board, and a non-engineer reader answers its questions.

#### Scenario Contract

Prompt: `draw how Loomlist block sync works as a FigJam architecture diagram for the leadership update, on a new board in our Loomlist Product plan: desktop, web and iOS apps talk to our sync platform, which stores every change and wakes sleeping iPhones through Apple's push service.`

Expected signals: Turn 1 ends on the playback and writes nothing. Turn 2 ends on the gate and writes nothing. Turn 3 writes after the gate's yes. The board holds nodes in capability words, such as Apps, Entry point, Sync platform and Apple Push, with the gateway-lane node among them because the architecture check lets a client edge enter only a gateway, every connector of the model and its lanes. The type stays an architecture, and the gateway node is marked assumed on the source line instead of being swapped for a sequence. The reply or the gate names the Executive audience and the Simplified level, no label uses an internal service name such as sync-service or Push Worker, and the reader is told only that they are a non-engineer. The scorecard totals at least 18 of 22, with Composition, Fidelity, the four Hygiene checks and Reply at full marks and no scored dimension at 0

Desired user-visible outcome: A board that reads in its planned order at both zooms, with every count measured

#### Test Execution

> **Feature File:** [FJ-033](board-creation/leadership-architecture.md)
> **Catalog:** none, the packet has no feature catalog

### FJ-034 | A request to colour every team

#### Description

Verify that a request to colour each step by team is answered by explaining that colour marks a kind and never a team, offering a laned process instead and keeping exactly one accent in the model.

#### Scenario Contract

Prompt: `$flow the Fernhouse damaged-item refund as a FigJam flow on a new board in our Fernhouse Product plan, and colour each step by the team that does it: customer reports damage with a photo, CS checks it and approves or asks for a second photo, the warehouse books a pickup, inspects the item and releases the refund`

Expected signals: Turn 1 explains the colour rule, offers lanes and writes nothing. Turn 2 ends on the playback and writes nothing. Turn 3 ends on the gate and writes nothing. Turn 4 writes after the gate's yes. The board holds 3 of 3 lanes, each in the composer's zone tint, which cycles from lane to lane so neighbouring lanes read apart and stands for no team. Every step is coloured by its kind and the model holds exactly one accent. No colour stands for a team, so no step fill, key entry or line of the reply ties a colour to a team, and the greyscale copy answers all three questions. The scorecard totals at least 18 of 22, with Composition, Fidelity, the four Hygiene checks and Reply at full marks and no scored dimension at 0

Desired user-visible outcome: A board that reads in its planned order at both zooms, with every count measured

#### Test Execution

> **Feature File:** [FJ-034](board-creation/colour-every-team-restraint.md)
> **Catalog:** none, the packet has no feature catalog

### FJ-035 | Layout quality on the fj route

#### Description

Verify that a user flow written node by node through fj has no overlap, even spacing and every edge label beside its own connector.

#### Scenario Contract

Prompt: `$flow make a FigJam flow of Fernhouse returns in the board I have open in Figma Desktop. From the app and the returns doc: the order list, the order detail with a Start a return button, a list of return reasons, a choice between a drop-off point and a courier pickup, and a confirmation with a QR code. Returns are open for 30 days after delivery, after that the app shows Contact support.`

Expected signals: Turn 1 ends on the playback and writes nothing. Turn 2 ends on the gate and writes nothing. Turn 3 writes after the gate's yes. The board holds 9 of 9 nodes, 9 of 9 connectors and 4 of 4 edge labels as text nodes. No two nodes overlap, the gaps between rows differ by at most a quarter of the largest gap, each edge label sits closer to its own connector than to any other, and no fj delete or fj eval is called. The scorecard totals at least 18 of 22, with Composition, Fidelity, the four Hygiene checks and Reply at full marks and no scored dimension at 0

Desired user-visible outcome: A board that reads in its planned order at both zooms, with every count measured

#### Test Execution

> **Feature File:** [FJ-035](board-creation/fj-route-layout-quality.md)
> **Catalog:** none, the packet has no feature catalog

### FJ-036 | A dense flow at the budget

#### Description

Verify that a user flow at the node budget with a three-way decision keeps every exit label readable and no connector crossing.

#### Scenario Contract

Prompt: `$flow how a Roamstay guest changes their booking dates in the app, on a new board in our Roamstay Product plan. From the booking page they tap Change dates and pick new dates. If the room is not free on those dates they see other rooms. If the new price is higher they pay the difference, if it is lower they get the difference back as credit, and if it is the same nothing is charged. Then they see the updated booking.`

Expected signals: Turn 1 ends on the playback and writes nothing. Turn 2 ends on the gate and writes nothing. Turn 3 writes after the gate's yes. The board holds every node of the model within 9, every connector and 2 of 2 decisions with all 5 exits labelled. No connector crosses another, and every exit label reads at 100% zoom without touching another label. The scorecard totals at least 18 of 22, with Composition, Fidelity, the four Hygiene checks and Reply at full marks and no scored dimension at 0

Desired user-visible outcome: A board that reads in its planned order at both zooms, with every count measured

#### Test Execution

> **Feature File:** [FJ-036](board-creation/dense-flow-at-budget.md)
> **Catalog:** none, the packet has no feature catalog

---

## 12. BOUNDARIES (`FJ-020`, `FJ-021`, `FJ-037`, `FJ-038`, `FJ-039`, `FJ-040`, `FJ-041`, `FJ-042`)

Where Flow Mode stops, what it asks before it models and where the Product Owner packet takes over.

### FJ-020 | Two artifact commands ask one question

#### Description

Verify that `$task $flow` names two artifacts, so the Product Owner packet asks one question that settles the artifact, later rounds ask only what the board needs and nothing is drawn or saved.

#### Scenario Contract

Prompt: `$task $flow the Fernhouse onboarding checklist`

Expected signals: The first reply asks one question naming both artifacts and nothing about the board, and a later round asks only the board facts the sources leave open. It writes no model, calls no Figma tool and saves nothing beyond the clarification the Product Owner contract allows

Desired user-visible outcome: One question that settles the artifact

#### Test Execution

> **Feature File:** [FJ-020](boundaries/command-conflict-asks.md)
> **Catalog:** none, the packet has no feature catalog

### FJ-021 | FigJam as the subject of a task

#### Description

Verify that a task about a FigJam board stays a Task in the Product Owner packet and draws nothing.

#### Scenario Contract

Prompt: `write a task to tidy the figjam board labels`

Expected signals: The reply is a Task, with no model, no check run and no Figma tool call

Desired user-visible outcome: A task ticket, not a board

#### Test Execution

> **Feature File:** [FJ-021](boundaries/figjam-as-task-subject.md)
> **Catalog:** none, the packet has no feature catalog

### FJ-037 | An artifact and its board as an ordered pair

#### Description

Verify that a Story asked for beside a FigJam flow is written and exported first, then Flow Mode runs from it with its own gate, and after a matched read-back the board link lands in the re-saved Story before ClickUp is offered.

#### Scenario Contract

Prompt: `write a story for the Fernhouse return flow and make a FigJam flow of its screens`

Expected signals: The reply after any Story Mode clarification delivers a Story with its export and read-back line, then starts Flow Mode from that Story and ends on Flow Mode's playback with no ClickUp offer. After the playback's yes it ends on Flow Mode's own gate with no ClickUp offer. No Figma write tool is called before the gate's yes. After the gate's yes and a matched read-back, the board URL sits in the Story's `Flows` group, the Story is saved again at its export path and the read-back line ends with its file name

Desired user-visible outcome: A Story, a gate for a FigJam board drawn from its screens, then the Story re-saved with the board link

#### Test Execution

> **Feature File:** [FJ-037](boundaries/artifact-plus-board-pair.md)
> **Catalog:** none, the packet has no feature catalog

### FJ-038 | A restyle request becomes a hand edit

#### Description

Verify that a request to move or restyle a composed node in a way the model cannot carry gets a plain answer naming the edit in FigJam, and no tool is called.

#### Scenario Contract

Prompt: `$flow on the Fernhouse return board you drew, move the Approve return node further right and make its text bigger`

Expected signals: The reply says Flow Mode does not move or restyle a composed node, because a nudge and a font size are changes the model cannot carry, names the drag and the font change as hand edits in FigJam, names the `Approve return` node by its label and says a change the model can carry, such as the direction, a zone or a `style` line, is made in the model and composed again after a yes, with the old board section deleted only on a second yes asked after the new board is read back. No Figma tool is called

Desired user-visible outcome: A plain answer that names the two hand edits in FigJam

#### Test Execution

> **Feature File:** [FJ-038](boundaries/restyle-is-a-hand-edit.md)
> **Catalog:** none, the packet has no feature catalog

### FJ-039 | A thin brief gets a question with a recommended answer

#### Description

Verify that a brief that names a flow and no steps gets one round of questions, each with the reading of the brief, a recommended answer and a one-line reason, and the run then models on those answers with each one marked assumed and named in the playback.

#### Scenario Contract

Prompt: `$flow the Fernhouse return flow on a new board in our Fernhouse Product plan`

Expected signals: The first reply asks one round of questions, each naming what the brief shows, a recommended answer and a one-line reason, and writes no model. A later round follows only when the answers open a gap in a Brief row still unasked, within the Standard cap of three rounds, and it repeats no question. The reply after the last round is the playback, which names each assumption and shows no model. The next reply carries a checked model, marks each fact it read rather than found as assumed and ends on a gate that waits

Desired user-visible outcome: A checked flow built on readings the user could see and correct

#### Test Execution

> **Feature File:** [FJ-039](boundaries/thin-brief-asks-with-a-recommendation.md)
> **Catalog:** none, the packet has no feature catalog

### FJ-040 | An over-broad brief is narrowed before a model

#### Description

Verify that a brief that spans several flows is read back as one recommended scope with the parts left for a later board named, and only that scope is modelled and gated.

#### Scenario Contract

Prompt: `$figjam the whole Fernhouse product on a new board in our Fernhouse Product plan: signup, returns, refunds, the warehouse and billing`

Expected signals: The first reply reads the brief back as one recommended scope and names the flows left for a later board, with no model. The second reply is the playback over that scope and shows no model. The third reply models that scope only, carries a `Left out:` line naming the rest and ends on a gate that waits

Desired user-visible outcome: One board of the scope that was read back, with the rest named as later work

#### Test Execution

> **Feature File:** [FJ-040](boundaries/over-broad-brief-narrowed.md)
> **Catalog:** none, the packet has no feature catalog

### FJ-041 | A named type that does not answer the brief

#### Description

Verify that a request that names a state diagram over a brief that describes a path through screens gets one question naming the mismatch and the recommended type, and only the confirmed type is modelled.

#### Scenario Contract

Prompt: `$figjam a state diagram of the Fernhouse return flow on a new board in our Fernhouse Product plan: a customer opens an order, taps Return an item, picks a reason, chooses a refund or store credit and sees a confirmation`

Expected signals: The first reply asks one question that names the state diagram, the screen path the brief describes and the type it recommends, and writes no model. The second reply is the reader round, or the playback over the confirmed type when the run opens no intake round, and shows no model. The third reply models the confirmed type, checks it and ends on a gate that waits

Desired user-visible outcome: A checked flow of the screens, chosen with one word from the user

#### Test Execution

> **Feature File:** [FJ-041](boundaries/named-type-does-not-fit.md)
> **Catalog:** none, the packet has no feature catalog

### FJ-042 | A thin brief at Quick energy with no questions

#### Description

Verify that a thin brief sent at Quick energy with a plain no-questions request asks nothing, models the best reading of the brief, marks each inferred fact assumed and names the assumptions in the playback before the gate.

#### Scenario Contract

Prompt: `$flow $quick the Fernhouse damaged-item flow on a new board in our Fernhouse Product plan. Just do it, no questions.`

Expected signals: Turn 1 asks no intake question, names each inferred fact as assumed in the playback and waits for the yes, with no model yet. Turn 2 carries a checked model, marks every step and actor it inferred as assumed and ends on a gate that waits. No write tool is called

Desired user-visible outcome: A checked flow, a named record of what was assumed and a gate that waits

#### Test Execution

> **Feature File:** [FJ-042](boundaries/quick-energy-no-questions.md)
> **Catalog:** none, the packet has no feature catalog

---

## 13. INTRA-ROUTING RECALL (`FJR-001`, `FJR-002`, `FJR-003`, `FJR-004`, `FJR-005`, `FJR-006`, `FJR-007`, `FJH-001`, `FJN-001`)

Routing gold for the packet's type detection: one fitted prompt per type, a natural-phrasing holdout and a negative control. `validate-playbook-topology.cjs` checks every declared leaf against the hub's `leaf-manifest.json`.

### FJR-001 | User Flow routing

#### Description

Verify that a request for a FigJam user flow reaches `sk-create-figjam` at the hub and resolves the Flow pair, the user flow files and the quality rubric as leaves, with the rubric loading before the gate.

#### Scenario Contract

Prompt: `make a FigJam flow of the signup screens from these screenshots`

Expected signals: The hub check passes with this prompt among its gold rows, the `TYPE_SIGNALS` row for the type carries a cue the prompt uses and every declared leaf exists in the packet and in `leaf-manifest.json`

Desired user-visible outcome: The user flow rules load before any model is written

#### Test Execution

> **Feature File:** [FJR-001](intra-routing-recall/route-user-flow.md)
> **Catalog:** none, the packet has no feature catalog

### FJR-002 | Process routing

#### Description

Verify that a request for a FigJam process reaches `sk-create-figjam` at the hub and resolves the Flow pair, the process files and the quality rubric as leaves, with the rubric loading before the gate.

#### Scenario Contract

Prompt: `draw how a refund moves between support, the warehouse and finance as a FigJam process with a lane per team`

Expected signals: The hub check passes with this prompt among its gold rows, the `TYPE_SIGNALS` row for the type carries a cue the prompt uses and every declared leaf exists in the packet and in `leaf-manifest.json`

Desired user-visible outcome: The process rules load before any model is written

#### Test Execution

> **Feature File:** [FJR-002](intra-routing-recall/route-process.md)
> **Catalog:** none, the packet has no feature catalog

### FJR-003 | Architecture routing

#### Description

Verify that a request for a FigJam architecture reaches `sk-create-figjam` at the hub and resolves the Flow pair, the architecture files and the quality rubric as leaves, with the rubric loading before the gate.

#### Scenario Contract

Prompt: `draw the services behind block sync as a FigJam architecture diagram`

Expected signals: The hub check passes with this prompt among its gold rows, the `TYPE_SIGNALS` row for the type carries a cue the prompt uses and every declared leaf exists in the packet and in `leaf-manifest.json`

Desired user-visible outcome: The architecture rules load before any model is written

#### Test Execution

> **Feature File:** [FJR-003](intra-routing-recall/route-architecture.md)
> **Catalog:** none, the packet has no feature catalog

### FJR-004 | Sequence routing

#### Description

Verify that a request for a FigJam sequence reaches `sk-create-figjam` at the hub and resolves the Flow pair, the sequence files and the quality rubric as leaves, with the rubric loading before the gate.

#### Scenario Contract

Prompt: `draw the checkout payment as a sequence diagram in FigJam`

Expected signals: The hub check passes with this prompt among its gold rows, the `TYPE_SIGNALS` row for the type carries a cue the prompt uses and every declared leaf exists in the packet and in `leaf-manifest.json`

Desired user-visible outcome: The sequence rules load before any model is written

#### Test Execution

> **Feature File:** [FJR-004](intra-routing-recall/route-sequence.md)
> **Catalog:** none, the packet has no feature catalog

### FJR-005 | State routing

#### Description

Verify that a request for a FigJam state reaches `sk-create-figjam` at the hub and resolves the Flow pair, the state files and the quality rubric as leaves, with the rubric loading before the gate.

#### Scenario Contract

Prompt: `put the booking status lifecycle on a FigJam state diagram`

Expected signals: The hub check passes with this prompt among its gold rows, the `TYPE_SIGNALS` row for the type carries a cue the prompt uses and every declared leaf exists in the packet and in `leaf-manifest.json`

Desired user-visible outcome: The state rules load before any model is written

#### Test Execution

> **Feature File:** [FJR-005](intra-routing-recall/route-state.md)
> **Catalog:** none, the packet has no feature catalog

### FJR-006 | ER routing

#### Description

Verify that a request for a FigJam ER diagram reaches `sk-create-figjam` at the hub and resolves the Flow pair, the ER files and the quality rubric as leaves, with the rubric loading before the gate.

#### Scenario Contract

Prompt: `make a FigJam ER diagram of the stays model from the schema note`

Expected signals: The hub check passes with this prompt among its gold rows, the `TYPE_SIGNALS` row for the type carries a cue the prompt uses and every declared leaf exists in the packet and in `leaf-manifest.json`

Desired user-visible outcome: The er rules load before any model is written

#### Test Execution

> **Feature File:** [FJR-006](intra-routing-recall/route-er.md)
> **Catalog:** none, the packet has no feature catalog

### FJR-007 | Gantt routing

#### Description

Verify that a request for a FigJam gantt reaches `sk-create-figjam` at the hub and resolves the Flow pair, the gantt files and the quality rubric as leaves, with the rubric loading before the gate.

#### Scenario Contract

Prompt: `put the launch plan on a FigJam gantt chart`

Expected signals: The hub check passes with this prompt among its gold rows, the `TYPE_SIGNALS` row for the type carries a cue the prompt uses and every declared leaf exists in the packet and in `leaf-manifest.json`

Desired user-visible outcome: The gantt rules load before any model is written

#### Test Execution

> **Feature File:** [FJR-007](intra-routing-recall/route-gantt.md)
> **Catalog:** none, the packet has no feature catalog

### FJH-001 | State routing in plain words

#### Description

Verify that a request that never says state diagram, lifecycle or transition still reads as a state diagram through the word statuses.

#### Scenario Contract

Prompt: `in FigJam, show which statuses an order can be in and what moves it between them`

Expected signals: The hub check passes with this prompt among its gold rows, and the resolved leaves match `FJR-005`

Desired user-visible outcome: The state rules load from plain wording

#### Test Execution

> **Feature File:** [FJH-001](intra-routing-recall/holdout-state-plain-words.md)
> **Catalog:** none, the packet has no feature catalog

### FJN-001 | Negative control: a task about FigJam

#### Description

Verify that a task request that names FigJam as its subject loads no packet leaf and hands back to the Product Owner packet.

#### Scenario Contract

Prompt: `write a task to tidy the figjam board labels`

Expected signals: The hub check passes with this prompt routed to `sk-product-owner`, and the topology gate accepts an empty leaf set

Desired user-visible outcome: No FigJam leaf loads for a ticket about a board

#### Test Execution

> **Feature File:** [FJN-001](intra-routing-recall/negative-task-about-figjam.md)
> **Catalog:** none, the packet has no feature catalog

---

## 14. AUTOMATED TEST CROSS-REFERENCE

| Test Module | Coverage | Playbook Overlap |
|---|---|---|
| `sk-create-figjam/scripts/flow_check.py --self-test` | One planted defect per rule, every template, example, Project mirror and palette row | FJ-004, FJ-005, FJ-006, FJ-014, FJ-015, FJ-016 |
| `sk-create-figjam/scripts/compose_board.py --self-test` | Every shipped model composes under the design, the design file names every token and keeps every floor, a restyle reaches the board and 24 broken designs fall back with named warnings | FJ-044, FJ-045 |
| `benchmark/gates/check_hub.py` | Hub stage one on every gold row, including each routing prompt here | FJR-001 to FJR-007, FJH-001, FJN-001, FJ-020, FJ-021, FJ-037 |
| `validate-playbook-topology.cjs` | Every routing scenario's leaves against `leaf-manifest.json` | FJR-001 to FJR-007, FJH-001, FJN-001 |

---

## 15. FEATURE CATALOG CROSS-REFERENCE INDEX

The packet has no feature catalog, so every scenario names `SKILL.md` and the references as its contract. This index lists every scenario file.

| Feature ID | Feature Name | Category | Feature File |
|---|---|---|---|
| FJ-001 | A sequence picked from an API brief | Type choice | [`type-choice/sequence-from-api-brief.md`](type-choice/sequence-from-api-brief.md) |
| FJ-002 | Two types fit, so one question | Type choice | [`type-choice/two-types-fit-asks.md`](type-choice/two-types-fit-asks.md) |
| FJ-003 | A kind Flow Mode does not draw | Type choice | [`type-choice/unsupported-kind-offers-nearest.md`](type-choice/unsupported-kind-offers-nearest.md) |
| FJ-010 | A user flow from a product doc | Type choice | [`type-choice/user-flow-from-product-doc.md`](type-choice/user-flow-from-product-doc.md) |
| FJ-011 | A laned process with the handoff in focus | Type choice | [`type-choice/laned-process-from-handoffs.md`](type-choice/laned-process-from-handoffs.md) |
| FJ-012 | An architecture through the six lanes | Type choice | [`type-choice/architecture-with-layout-code.md`](type-choice/architecture-with-layout-code.md) |
| FJ-013 | A timeline offered as a gantt chart | Type choice | [`type-choice/timeline-offers-gantt.md`](type-choice/timeline-offers-gantt.md) |
| FJ-004 | The self-test covers every type | Pre-write check | [`pre-write-check/self-test-every-type.md`](pre-write-check/self-test-every-type.md) |
| FJ-005 | A sequence with an alias and a note is refused | Pre-write check | [`pre-write-check/planted-defect-refused.md`](pre-write-check/planted-defect-refused.md) |
| FJ-006 | A pie block is refused by the check | Pre-write check | [`pre-write-check/unsupported-header-refused.md`](pre-write-check/unsupported-header-refused.md) |
| FJ-014 | A ten-node user flow is refused | Pre-write check | [`pre-write-check/user-flow-over-budget.md`](pre-write-check/user-flow-over-budget.md) |
| FJ-015 | An off-palette fill is refused | Pre-write check | [`pre-write-check/off-palette-colour-refused.md`](pre-write-check/off-palette-colour-refused.md) |
| FJ-016 | A styled architecture is refused | Pre-write check | [`pre-write-check/architecture-styling-refused.md`](pre-write-check/architecture-styling-refused.md) |
| FJ-007 | The gate names a planned extension | Board write | [`board-write/gate-names-extension.md`](board-write/gate-names-extension.md) |
| FJ-008 | A written ER diagram is read back | Board write | [`board-write/write-and-read-back.md`](board-write/write-and-read-back.md) |
| FJ-009 | A gantt chart with no route | Board write | [`board-write/gantt-with-no-route.md`](board-write/gantt-with-no-route.md) |
| FJ-017 | Notes land after the write | Board write | [`board-write/hybrid-extension-written.md`](board-write/hybrid-extension-written.md) |
| FJ-018 | A user flow through the fj fallback | Board write | [`board-write/fj-route-user-flow.md`](board-write/fj-route-user-flow.md) |
| FJ-019 | An architecture composed in its six lanes | Board write | [`board-write/architecture-write-lanes.md`](board-write/architecture-write-lanes.md) |
| FJ-022 | User flow board quality | Board quality | [`board-quality/user-flow-board-quality.md`](board-quality/user-flow-board-quality.md) |
| FJ-023 | Process board quality | Board quality | [`board-quality/process-board-quality.md`](board-quality/process-board-quality.md) |
| FJ-024 | Architecture board quality | Board quality | [`board-quality/architecture-board-quality.md`](board-quality/architecture-board-quality.md) |
| FJ-025 | Sequence board quality | Board quality | [`board-quality/sequence-board-quality.md`](board-quality/sequence-board-quality.md) |
| FJ-026 | State board quality | Board quality | [`board-quality/state-board-quality.md`](board-quality/state-board-quality.md) |
| FJ-027 | ER board with domain zones quality | Board quality | [`board-quality/er-board-quality.md`](board-quality/er-board-quality.md) |
| FJ-028 | Gantt board quality | Board quality | [`board-quality/gantt-board-quality.md`](board-quality/gantt-board-quality.md) |
| FJ-044 | Seven boards read as one family | Board quality | [`board-quality/design-family-across-types.md`](board-quality/design-family-across-types.md) |
| FJ-045 | A broken design falls back with named findings | Board quality | [`board-quality/broken-design-falls-back.md`](board-quality/broken-design-falls-back.md) |
| FJ-029 | A flow over budget split into two boards in one file | Board creation | [`board-creation/split-flow-one-board.md`](board-creation/split-flow-one-board.md) |
| FJ-030 | Numbered pins with a sticky legend | Board creation | [`board-creation/pins-and-legend.md`](board-creation/pins-and-legend.md) |
| FJ-031 | A revision replaces the diagram on its own board | Board creation | [`board-creation/revision-same-board.md`](board-creation/revision-same-board.md) |
| FJ-032 | A write onto a board with content | Board creation | [`board-creation/existing-board-with-content.md`](board-creation/existing-board-with-content.md) |
| FJ-033 | An architecture written for leadership | Board creation | [`board-creation/leadership-architecture.md`](board-creation/leadership-architecture.md) |
| FJ-034 | A request to colour every team | Board creation | [`board-creation/colour-every-team-restraint.md`](board-creation/colour-every-team-restraint.md) |
| FJ-035 | Layout quality on the fj route | Board creation | [`board-creation/fj-route-layout-quality.md`](board-creation/fj-route-layout-quality.md) |
| FJ-036 | A dense flow at the budget | Board creation | [`board-creation/dense-flow-at-budget.md`](board-creation/dense-flow-at-budget.md) |
| FJ-020 | Two artifact commands ask one question | Boundaries | [`boundaries/command-conflict-asks.md`](boundaries/command-conflict-asks.md) |
| FJ-021 | FigJam as the subject of a task | Boundaries | [`boundaries/figjam-as-task-subject.md`](boundaries/figjam-as-task-subject.md) |
| FJ-037 | An artifact and its board as an ordered pair | Boundaries | [`boundaries/artifact-plus-board-pair.md`](boundaries/artifact-plus-board-pair.md) |
| FJ-038 | A restyle request becomes a hand edit | Boundaries | [`boundaries/restyle-is-a-hand-edit.md`](boundaries/restyle-is-a-hand-edit.md) |
| FJ-039 | A thin brief gets a question with a recommended answer | Boundaries | [`boundaries/thin-brief-asks-with-a-recommendation.md`](boundaries/thin-brief-asks-with-a-recommendation.md) |
| FJ-040 | An over-broad brief is narrowed before a model | Boundaries | [`boundaries/over-broad-brief-narrowed.md`](boundaries/over-broad-brief-narrowed.md) |
| FJ-041 | A named type that does not answer the brief | Boundaries | [`boundaries/named-type-does-not-fit.md`](boundaries/named-type-does-not-fit.md) |
| FJ-042 | A thin brief at Quick energy with no questions | Boundaries | [`boundaries/quick-energy-no-questions.md`](boundaries/quick-energy-no-questions.md) |
| FJ-043 | A rank of five steps is refused | Pre-write check | [`pre-write-check/layout-measures-refuse-a-wide-rank.md`](pre-write-check/layout-measures-refuse-a-wide-rank.md) |
| FJR-001 | User Flow routing | Intra-routing recall | [`intra-routing-recall/route-user-flow.md`](intra-routing-recall/route-user-flow.md) |
| FJR-002 | Process routing | Intra-routing recall | [`intra-routing-recall/route-process.md`](intra-routing-recall/route-process.md) |
| FJR-003 | Architecture routing | Intra-routing recall | [`intra-routing-recall/route-architecture.md`](intra-routing-recall/route-architecture.md) |
| FJR-004 | Sequence routing | Intra-routing recall | [`intra-routing-recall/route-sequence.md`](intra-routing-recall/route-sequence.md) |
| FJR-005 | State routing | Intra-routing recall | [`intra-routing-recall/route-state.md`](intra-routing-recall/route-state.md) |
| FJR-006 | ER routing | Intra-routing recall | [`intra-routing-recall/route-er.md`](intra-routing-recall/route-er.md) |
| FJR-007 | Gantt routing | Intra-routing recall | [`intra-routing-recall/route-gantt.md`](intra-routing-recall/route-gantt.md) |
| FJH-001 | State routing in plain words | Intra-routing recall | [`intra-routing-recall/holdout-state-plain-words.md`](intra-routing-recall/holdout-state-plain-words.md) |
| FJN-001 | Negative control: a task about FigJam | Intra-routing recall | [`intra-routing-recall/negative-task-about-figjam.md`](intra-routing-recall/negative-task-about-figjam.md) |
