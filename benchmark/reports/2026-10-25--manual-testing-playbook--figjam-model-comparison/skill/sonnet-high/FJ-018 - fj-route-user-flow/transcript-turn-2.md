# FJ-018 turn 2 transcript

**User:** Use your recommended answers.

**Assistant:**

Nothing is written yet. These are the rows as I read them, and I haven't drawn or checked a model yet.

**Question:** which screens does a customer pass through to return an item, and where does the 30 day check stop them?
**Outcome:** a reader can follow a return from an opened order to the confirmation and see where it ends early.

**Settled by your message and your answers**
- Entry: the customer opens an order
- Exit: the confirmation, or the not-eligible screen when the order is older than 30 days
- Actor: the customer on every move, with the age check running automatically after the reason
- Choices: the age check, then refund or store credit
- Scope: the customer's side only, with no CS, Admin or warehouse steps, no refund timing or amounts, and nothing after the not-eligible screen

**Assumed**
- The source is the returns doc as you summarised it, with its status unknown. The board's source line will say "status not confirmed". Telling me the status would settle this.
- Detail is balanced and the audience is mixed, so the labels use the doc's own words. The reading distance is Laptop.
- The doc's wording rules, so the check reads "Order older than 30 days?".

**Still open:** none.

**Outline**
- The line the board answers: "Which screens does a customer pass through to return an item, and where does the 30 day check stop them?"
- Nodes in drawing order, 7 against a budget of 9:
  1. Open an order, the start
  2. Pick item and reason
  3. Order older than 30 days?
  4. Not eligible, an exit
  5. Refund or store credit, one screen
  6. Print the label
  7. Return confirmed, the goal
- Connectors, 6:
  - Open an order to Pick item and reason, labelled "Tap Return an item", since that tap is the one trigger you named
  - Pick item and reason to the age check
  - Yes to Not eligible
  - No to Refund or store credit
  - Refund or store credit to Print the label
  - Print the label to Return confirmed
- Dropped by the remove test: "Return an item" as a node of its own, because it is the tap and not a screen

**Two framings**
- Recommended: the happy path on one straight line, with Not eligible beside the age check. It shows the path and the exit at once.
- The alternative: Refund and Store credit as two nodes that rejoin. That costs two more nodes and adds nothing, because no source says the paths differ.

**Look, proposed**
- Return confirmed is the green goal and the first glance.
- Not eligible is a plain exit beside the main line.
- No zones, because 7 nodes read on one line and a zone would add frames without information.
- Title: "Return an item"
- Subtitle: "How a Fernhouse customer returns an item, from an opened order to a confirmed return"
- Source line: "Source: returns doc as relayed in the request, status not confirmed. Left out: CS, Admin and warehouse steps, refund timing, anything after Not eligible."

**Critique questions for the gate**
1. Does the eye go first to the node the board most needs read?
2. Does any node or connector fail the remove test?
3. Is the Not eligible exit easy to spot?
4. Does the board answer the line above without the doc beside it?

**Finding to carry:** the company context says there is no self-serve return today, that CS creates the return and emails the label, and that the 30 days run from delivery. Your flow has the customer starting the return and counts from the order. I'll draw it as the doc states it and name the difference in the reply.

Is this the right reading of the board?
