# FJ-036 turn 2 transcript

**User:** Use your recommended answers.

**Tool call:** `Read` `{"file_path": "/private/tmp/claude-501/-Users-michelkerkmeester-MEGA-Development-AI-Systems/348b59cb-58a2-4b49-8147-c40143312bc1/scratchpad/r042/tmp/FJ-036/devin-compare-bench/FJ-036/sk-create-figjam/references/quality-rubric.md"}`

**Tool result:** `Read`

```text
"1\t---\n2\ttitle: \"FigJam Diagram Quality Rubric\"\n3\tdescription: \"The taste gate a FigJam model passes before the write gate, translated from sk-design-diagram's success criteria: type fit, the remove test, signal, the check, the board, the design rubric that scores a composed board and the reply.\"\n4\tcontextType: implementation\n5\timportance_tier: important\n6\ttrigger_phrases:\n7\t  - \"figjam quality rubric\"\n8\t  - \"diagram taste gate\"\n9\t  - \"remove test\"\n10\t  - \"figjam review checklist\"\n11\t  - \"figjam design rubric\"\n12\tversion: 1.0.5.0\n13\t---\n14\t\n15\t# FigJam Diagram Quality Rubric\n16\t\n17\tThe script checks what a script can see. This rubric is the rest: whether the diagram should exist, whether every node earns its place and whether the reader can trust what lands on the board. Walk it after the check passes and before the write gate.\n18\t\n19\t**Loading Condition:** CONDITIONAL, on every Flow route before the write gate\n20\t**Purpose:** The judgement pass between the pre-write check and the gate\n21\t**Scope:** The model, the provenance table, the planned extensions and, after the write, the board and the reply\n22\t\n23\t---\n24\t\n25\t## 1. TYPE FIT\n26\t\n27\t- [ ] The type answers the reader's question, as `references/flow-mode.md` Section 3 maps it\n28\t- [ ] A table, a list or a paragraph would not do the same job. If it would, say so and offer that instead\n29\t- [ ] The type's reference in `references/types/` was loaded and i
```

**Assistant:**

Settled with your recommended answers. Here is the full playback of the reading. Nothing is drawn or written yet.

**The reading**
* Question: which screens does a Roamstay guest pass through when changing booking dates, and where do they choose?
* Outcome: the product and design team can decide what the app does in each of the three price cases
* Reader: the product and design team (assumed, a yes from you settles it)
* Entry: the booking page (captured)
* Exit: the updated booking, the only end (captured)
* Decisions: room free or not, then new price higher, lower or the same (captured)
* Actors: the guest taps, picks and pays. The availability check, the price comparison and the credit are system steps (assumed, your word settles it)
* Source and class: your description, taken as current behavior and not checked against the app (assumed, a screen or doc of the app settles it)
* Scope: left out are payment failure, host approval and cancellation rules (assumed, accepted from my recommendation)
* Dials: balanced detail, mixed audience, laptop distance (assumed)

**The outline** (8 nodes, 10 connectors, 5 labelled decision exits, inside the nine-node budget)
0. Sentence the board answers: "Which screens does a Roamstay guest pass through when changing booking dates, and where do they choose?"
1. Booking page, start (Entry)
2. Booking page to Pick new dates, labelled "Tap Change dates" (guest)
3. Pick new dates to Room free?, automatic (system)
4. Room free? to New price vs old?, exit "Yes"
5. Room free? to See other rooms, exit "No"
6. See other rooms to New price vs old?, labelled "Pick a room" (guest, **assumed**, your word or a screen settles it)
7. New price vs old? to Pay the difference, exit "Higher"
8. New price vs old? to Get the difference as credit, exit "Lower"
9. New price vs old? to Updated booking, exit "Same", with no screen of its own for "nothing charged"
10. Pay the difference to Updated booking, and Get the difference as credit to Updated booking (Exit)

The remove test cut nothing, because every node is a screen or a choice you named.

**Two framings**
* Main route with branches beside it: booking page, dates, room check, price check and updated booking sit on one line, with other rooms, pay and credit beside it. It reads fast and keeps one board, but the three price branches share the same exit
* One board per question: an availability board and a pricing board. Each is clearer, but it spends two writes and splits a flow that is short
* Recommended: the first, since eight nodes fit one board

**The look**
* Accent: the New price vs old? decision, because the three price cases are what the team decides
* Colour: no failing end and no step in focus, so the single end draws as the goal
* Zones: none, since eight nodes read in one pass
* Title: "Change booking dates"
* Subtitle: how a Roamstay guest changes the dates of a booking in the app, for the product and design team
* Source line: your description, not checked against the app, with the three exclusions named under left out

Is this reading right, or what should change?
