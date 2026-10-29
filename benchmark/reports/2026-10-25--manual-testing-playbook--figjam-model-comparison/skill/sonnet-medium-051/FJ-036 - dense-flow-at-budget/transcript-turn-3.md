# FJ-036 turn 3 transcript

**User:** Use your recommended answers.

**Tool call:** `Read` `{"file_path": "/private/var/folders/3c/zfqcqsts0kn19cgblj82gqhm0000gn/T/devin-compare-bench/FJ-036/sk-create-figjam/references/types/user-flow.md"}`

**Tool result:** `Read`

```text
"1\t---\n2\ttitle: \"FigJam Type - User Flow\"\n3\tdescription: \"A person's path through a product composed as a FigJam board: four shapes, labelled exits, colour by kind, optional zones and a nine-node budget.\"\n4\tcontextType: implementation\n5\timportance_tier: important\n6\ttrigger_phrases:\n7\t  - \"figjam user flow\"\n8\t  - \"user flow rules\"\n9\t  - \"screen flow figjam\"\n10\t  - \"merge dot\"\n11\tversion: 1.0.5.0\n12\t---\n13\t\n14\t# FigJam Type - User Flow\n15\t\n16\tA user flow is the screens and choices one person passes through to reach a goal. It is the default Flow type and the strictest, because it is drawn from screenshots and frames a reader will compare node by node.\n17\t\n18\t**Loading Condition:** CONDITIONAL, when the Flow route draws a user flow\n19\t**Purpose:** The grammar, rules, budget and read-back for a user flow\n20\t**Pairs With:** `assets/flow-templates.md`\n21\t\n22\t---\n23\t\n24\t## 1. WHEN TO USE\n25\t\n26\t**The reader's question:** which screens does a person pass through, and where do they choose?\n27\t\n28\t- A flow drawn from screenshots, from Figma frames or from a product doc that walks one person through the product\n29\t- A platform split, such as desktop and mobile, that rejoins on a later screen\n30\t- A journey, which Flow Mode does not draw as such, redrawn as the screens it visits\n31\t\n32\tUse another type when several people or teams hand work to each other (a process), when the subject is services and stores (an arc
```

**Assistant:**

**Reading so far**

* Question: which screens does a guest pass through when changing booking dates, and how does the price outcome route them
* Outcome: the product and design team can confirm each branch matches the app or point out a missing one
* Detail, audience and distance: Balanced, Mixed, Laptop
* Settled by your message: entry, exit, actor and both choices (room free, price higher, lower or same)
* Assumed, with what would settle each:
  * Reader, question and outcome as above, until you name a different reader
  * Your message describes how the app works today, until a screen or doc says otherwise
  * After the other rooms, the guest picks a room and joins the price check, until you say they go back to the dates instead
* Not asked: nothing else is open
* Left out of the board: failed payment, change-window rules, host approval and cancellation, because your message doesn't describe them

**Outline, in drawing order**

The board answers: which screens does a guest pass through to change booking dates, and how does the price outcome route them.

1. Booking page, where the flow starts (Entry)
2. Pick new dates, reached by the label "Tap Change dates" (Entry, Actors)
3. Room free? (Decisions)
4. See other rooms, on the No exit (Decisions, assumed next step)
5. New price?, with exits Higher, Lower and Same, reached from Room free? on Yes and from the other rooms with the label "Pick a room" (Decisions, assumed)
6. Pay the difference, on Higher (Decisions)
7. Difference credited, on Lower (Decisions)
8. Nothing charged, on Same (Decisions)
9. Updated booking shown, the end, reached from all three price outcomes (Exit)

That is 9 nodes and 12 connectors, so it fits the user flow budget with no merge dot. Remove test: every node is a step or choice you described, so none comes out.

**Two ways to frame it**

* One board with the main route straight across and the other rooms and the three price outcomes beside it. This shows all branches at once, and it costs a little density at the price check. I recommend this one
* Two boards, "1. Pick dates" and "2. Settle the price". Each reads more easily, but a reader has to jump between boards to see the whole flow, and the flow only just fits one board anyway

**The look**

* Colour accent: the New price? choice, because it is where the three outcomes split and the reader most needs it. The goal, Updated booking shown, is named but not coloured
* Direction: left to right
* Zones: none, because 9 nodes read without them
* Title: Change booking dates
* Subtitle: From the booking page to the updated booking, for the product and design team
* Source line: Sources: the request description, read as current app behavior. Left out: failed payment, change-window rules, host approval and cancellation

Is this reading right, or what should change?
