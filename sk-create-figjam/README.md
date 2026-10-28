---
title: "sk-create-figjam"
description: "FigJam diagram packet of the Product Owner hub: picks the diagram type, checks a Mermaid model of it and composes it into a framed FigJam board."
trigger_phrases:
  - "sk-create-figjam"
  - "$flow"
  - "$figjam"
  - "figjam flow"
  - "figjam diagram"
version: 1.0.13.0
---

# sk-create-figjam

> Draws a FigJam diagram of the type the reader's question needs, from screenshots, a Figma flow, a product doc, a schema or a plan, and composes the checked model into a framed board with a title, zones, colour by kind and a key.

---

## 1. OVERVIEW

This packet is Flow Mode, the one Product Owner mode whose deliverable is a board rather than a file. The hub `../SKILL.md` picks it for `$flow`, `$figjam` and FigJam output wording. The hub `../ROUTER.md` maps a Flow request to this packet's pair, and `SKILL.md` adds the files for the chosen type.

It draws seven types, each answering one reader question: a user flow, a laned process, an architecture, a sequence, a state diagram, an ER diagram and a gantt chart. Before any model it interviews the user in rounds until a nine-row Brief is ready to draw: every question carries the AI's reading of the input and a recommended answer, and an unanswered one proceeds on that recommendation, marked assumed and named in the playback before the gate. A diagram is written as a Mermaid model with a provenance table that ties every item to its source. `scripts/flow_check.py` holds the model to its type's rules before anything is written, `references/quality-rubric.md` asks what a script cannot, and the write waits for a yes naming the plan, the file, any extension and the rollback. `scripts/compose_board.py` then fills `assets/compose-board.js` from the checked model, and one `use_figma` call draws the board: a title and subtitle, the diagram on an 8 pixel grid with every node coloured by its kind, tinted zones, routed connectors, a key and a source line. Every board is drawn in the design `assets/figjam-design.md` holds: what each colour means, the first-glance accent, the type sizes, the lines, the zone tints and the key's words. A team edits that one file to restyle every board, and a token that would break a contrast or hue floor falls back to its shipped value with a `DESIGN` line that the reply turns into a finding. Notes the model cannot carry go on afterwards as numbered pins or stickies through `references/hybrid-workflow.md`. The reply is the board URL on its first line, a read-back line measured on the board, an `Extensions:` line when there are any, a `Left out:` line whenever the board leaves out a cut, a split, a later board or a point the sources left open, a `Finding:` line for each finding or question and the HVR self-scan line last. Nothing is saved to `../export/`.

---

## 2. GALLERY

Real boards this packet composed on a fictional test file and rendered through the Figma REST API. Each type board and the dense flow is the best board of its type that Claude Sonnet 5.5 high drew in the shipped design file, with the v1.0.6.0 composer on 2026-10-26 or, for the process board, the v1.0.7.0 skill and, for the state board, the v1.0.11.0 skill on 2026-10-27. They show the outlines that keep kinds apart in greyscale, and the user flow, process, architecture, state and gantt keys carry the `Leads to` entry. Only the existing-board image is older. [`assets/screenshots/README.md`](assets/screenshots/README.md) names the playbook scenario, the model and the scorecard result behind each one.

**User flow.** The pink outline on the green Confirmation with QR code goal is the first glance. Three zones run left to right, Find the order, Request the return and Done. Each decision is a yellow diamond with labelled exits, the dashed orange Contact support pill shows where the flow leaves and Drop-off point and Courier pickup reach the goal from two sides.

![A user flow board for starting a return, with three zones and the 30-day decision highlighted](assets/screenshots/user-flow-board.png)

**Process.** One lane per role, Customer, CS agent and Warehouse, each in its own tint. The pink outline sits on the Approve the claim step, which logs each decision to a violet Claims table store and hands the claim to the warehouse queue. The Damage clear? decision sends an unclear photo back to the customer as an input step that loops to it. The key names kinds and no team. The run that drew it fails its PASS line on Composition, because the green Refund released goal, left out of the glance plan, reads before the decision the run planned as the second glance.

![A laned refund process where the highlighted Approve the claim step logs to a Claims table and hands off to a warehouse queue](assets/screenshots/process-board.png)

**Architecture.** Six zones run left to right from Clients through Edge, Services, Events and Stores to Outside. The sync-service node carries the pink outline and the key gives the reason, In focus: Writes every block change. The change stream is an orange queue and the blocks database a violet cylinder. Dashed edges mark the async and outside calls and the three live sockets run both ways, the same as the key.

![An architecture board for a block sync service across six zones](assets/screenshots/architecture-board.png)

**Sequence.** The four participants are white and repeat at the top and the bottom, and numbered pins mark the seven steps beside each sender's lifeline. The pink heavy arrow on step 3, Authorise the card, is the focus, replies are dashed and the async Tell the hub message is blue. Each message is in plain words, such as Post the booking, and the source line names the declined-card path as left out.

![A sequence board for a checkout payment with seven numbered steps](assets/screenshots/sequence-board.png)

**State.** Pending is the blue first state, and card authorised moves it into Confirmed, a composite zone that runs from Upcoming through check in to In stay. Completed, No-show and Cancelled are gray final states in one column, each with its end dot, and no transition crosses another. Cancelled carries the pink outline as the end state two statuses lead to, with its own key entry. The run that drew it passes at 22 of 22: its plan follows the board as drawn, and Cancelled leads the end states for both readers.

![Roamstay booking status state diagram with a Confirmed composite and pink Cancelled end](assets/screenshots/state-board.png)

**ER.** A Guest side zone and a Partner side zone keep the two halves apart. Each entity lists its PK and FK columns. Each line names the relationship with its cardinality and carries the matching crow's-foot mark at both ends. Booking carries the pink outline. The board shows key columns only, because the run had no schema note.

![An ER board with six entities split into guest and partner zones](assets/screenshots/er-board.png)

**Gantt.** A weekly date axis runs across the top and Design, Build and Rollout are tinted zones. Each bar shows its length, the critical bars carry a heavy outline, the integration week carries the pink outline and a yellow diamond marks the release on 21 December. An arrow runs from each bar's right end onto the top of the work that waits on it, and two arrowheads crowd into Desktop and iOS integration. The source line names Android as left out.

![A gantt board for a launch plan with three phases and a release milestone](assets/screenshots/gantt-board.png)

**Written onto an existing board.** In FJ-032 this state diagram was added to a board that already held content, which the write left in place. The overview shows the new section only. Completed carries the pink outline as the first glance this time, because the gate planned it first. The board predates v1.0.6.0, because the rerun's FJ-032 board scored 19 and failed on Composition and Reply.

![A state board for a booking lifecycle written onto a board with existing content](assets/screenshots/state-on-existing-board.png)

**Dense flow at the node budget.** Nine nodes and two decisions with five labelled exits, No, Yes, Higher, Lower and Same, and no connector crossing another. The pink outline sits on the three-way New price? decision and the key gives the reason, the only three-way choice. The run that drew it fails its PASS line on its reply, which opened on a cleanup line, not on the board.

![A dense user flow board for changing booking dates with a three-way decision](assets/screenshots/dense-flow-board.png)

---

## 3. QUICK START

```text
$flow the location change from these screenshots
make a FigJam flow from the signup doc
$figjam the booking status lifecycle from the bookings doc
put the launch plan on a FigJam gantt chart
```

Check a model by hand:

```bash
python3 sk-create-figjam/scripts/flow_check.py model.md
python3 sk-create-figjam/scripts/flow_check.py --self-test
python3 sk-create-figjam/scripts/compose_board.py model.md --diagram 1 --out board.js
python3 sk-create-figjam/scripts/compose_board.py --design-check
python3 sk-create-figjam/scripts/compose_board.py --self-test
```

A flowchart that is not a user flow starts with `%% type: process` or `%% type: architecture`. The check exits 0 when every diagram passes, 1 when a rule fails and 2 when the file cannot be read. For a user flow, a process or an architecture it also prints five layout measures, the widest rank, the longest path, connectors per step, the average label length and the crossing pairs, and fails a model outside their budgets. When `node` is on the path it also prints a `Label:` line for each node label the board would wrap with one word alone on its last line, or one `Label: skipped` line when it could not trace the board, and a label stranded at only one of the two widths FigJam wraps at reads `may leave`. On a user flow or a process it prints a `Glance:` line, the order a reader meets the nodes, and a `Row:` line for a main-row line that bends off its row. With `--notes <id>,<id>` it prints a `Sides:` line per noted node with the side and alignment its sticky takes. None of these lines fails the check. The composer exits 0 with the code written and a `COMPOSED` line naming the counts the read-back will look for, 1 when the model fails the check or the code would not fit one `use_figma` call, and 2 when the file or the diagram cannot be read. `--design-check` prints the design a board is drawn in with its measured contrast and exits 1 on any design warning. The self-test needs `node` on the path to syntax-check the code it fills.

---

## 4. STRUCTURE

[`SKILL.md`](SKILL.md) Section 3 holds the packet's file map, one line per path, so this README does not restate it.

---

## 5. HOW IT FITS

The packet shares the Product Owner bootstrap in `../AGENTS.md`, so the persona and the self-scan apply here. It reads `hvr-core.md` and `conciseness.md` from `../sk-product-owner/references/` instead of keeping its own copy. The `fj` write route uses the vendored `../mcp-figma/` packet for `figma-ds-cli` mechanics.

The Product Owner router still knows both commands. A conflict such as `$task $flow` stays there and asks one question, and a Flow route that reaches it hands off here.

The claude.ai Project has no hub, so it keeps Flow Mode as a mode of the one kernel. Its Flow Knowledge files mirror this packet's references and assets where they apply inside a Project, as `../SYNC.md` records.

---

## 6. RELATED DOCUMENTS

| Document | Purpose |
|---|---|
| [`../SKILL.md`](../SKILL.md) | The hub, stage one routing |
| [`../ROUTER.md`](../ROUTER.md) | The hub stage two leaf map |
| [`../sk-product-owner/SKILL.md`](../sk-product-owner/SKILL.md) | The Product Owner packet |
| [`../mcp-figma/SKILL.md`](../mcp-figma/SKILL.md) | The vendored Figma transport packet |
| [`../SYNC.md`](../SYNC.md) | The parity note for the Claude Project package |
