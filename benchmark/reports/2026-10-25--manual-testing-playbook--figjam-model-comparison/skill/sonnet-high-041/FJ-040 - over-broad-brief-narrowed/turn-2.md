Scope accepted: one laned process board, "Return to refund". This is the reading I'd model from, and nothing has been drawn or written yet.

**What the sources settled**

The only source is `context/fernhouse-context.md`, whose class is current behavior. I used Key flows 6, Personas and roles, the glossary entry for the return window and the `orders-service` row.

| Row | Value | Status |
|---|---|---|
| Reader | Someone on Post-purchase, CS or Fulfilment who needs to see which role owns each step | assumed, settled by your answer |
| Question | Who does what from a return request to the refund, and where does work change hands? | captured |
| Outcome | The reader can name the owner of every step and spot the two hand-offs where work waits | assumed, settled by your answer |
| Scope | Contact to refund. Signup, billing and outbound fulfilment are left for later boards | captured |
| Entry | The customer contacts CS, within 30 days of delivery | captured |
| Exit | The agent refunds | captured |
| Actors | Customer, CS agent, Warehouse operator, CS lead | captured |
| Decisions and states | One decision: a refund over €200 needs a CS lead | captured |
| Sources and class | The company context, current behavior | captured |

**The outline, in drawing order**

The board answers one sentence: who does what from a return request to the refund, and where does work change hands?

*   Customer: "Asks CS for a return" (start) and "Sends the item back"
*   CS agent: "Create the return in Admin", "Email the return label", the decision "Refund over €200?" and "Refund the customer"
*   Warehouse operator: "Check the item"
*   CS lead: "Approve the refund"
*   End: "Refund issued"

That is 8 steps, 1 decision and 4 lanes, inside the 12-node, 16-connector budget for a laned process. The lanes run Customer, CS agent, Warehouse operator, CS lead, which is the order work first reaches them. The over-€200 decision has two exits. "Yes" goes through the CS lead and "No" goes straight to the refund.

"Sends the item back" is my reading, not a stated step. The source says the agent emails a label and the warehouse checks the item, so something travels in between. I'd draw it at medium confidence.

**Two framings**

*   Happy path with the one approval branch, which I recommend. It shows who owns each step and where work changes hands. It costs the outcomes no source states: a failed check, a request past 30 days and a lead who declines
*   Every exit drawn, including those three. It costs invented behavior, so it waits until CS or the warehouse confirms what happens

**The look, as proposed choices**

*   First glance: the green "Refund issued" end, because the question ends at the refund. No step is in focus, because no source says where the delay sits, and there is no failure end, because none is stated
*   Detail level Balanced, audience Mixed, reading distance Laptop, all assumed
*   Zones: none, because the lanes already group the steps
*   Title "Return to refund". Subtitle "How a Fernhouse return runs from the first CS contact to the refund, about 1,900 requests a month and 6 days on average". Source line naming the company context and the left-out items
*   Four glance checks for the sketch: whether the eye lands first on "Refund issued", whether you can name who sends the item back and who checks it, whether the over-€200 branch is easy to find and whether any step reads as a source fact when it isn't

**Left out so far:** signup, billing and outbound fulfilment, as later boards. A failed warehouse check, a request past 30 days, a lead declining and how the money goes back are not in any source.

Question: is this reading right?

Recommended: yes. Put the 30-day window in the start label ("Asks CS for a return") and the subtitle instead of a decision, and draw the warehouse check with a single exit. Neither the window nor the check has a stated outcome, so those paths stay under `Left out:`.

Why: a branch with no source behind it would read as current behavior. A correction to any row reruns this reading for that row alone.

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.