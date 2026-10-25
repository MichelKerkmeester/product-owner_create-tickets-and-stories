Nothing is written yet. This is how I read the request, and the board waits for your answer.

**Question:** who does what in a damaged-item refund, and where does the claim change hands?

**Outcome:** a reader can see which of the customer, CS and the warehouse owns each step. They can also see the point where an approved claim moves from CS to the warehouse.

**Type:** a process with three lanes, Customer, CS agent and Warehouse operator, in the order work reaches them.

**Settled by your runbook text**
* Customer: reports damage with a photo through the help form, and sends a second photo when asked
* CS agent: checks the photo, then either approves clear damage on the spot or asks for a second photo, and the check repeats when the second photo arrives
* Warehouse operator: gets the approved claim in the warehouse queue, books a courier pickup, inspects the item on arrival and releases the refund
* Highlight: the CS to warehouse handoff, which is "Approve the claim" and the crossing into the warehouse queue
* Target: a new board added inside the existing file <test-file-key>. I read "new board" as a new board section and "rather than a new file" as the instruction that decides it, so nothing already in the file is touched

**Left out:** the pickup skipped under €20. The runbook says it is a pilot that is not yet live, so it is a proposal and not current behavior.

**Gap named, not drawn:** the runbook gives no path for an item that fails inspection. I won't invent one, and the board will say so in its source line.

**Assumed:** balanced detail, a mixed audience and Laptop reading distance.

Three points are still open. If you skip them, I proceed on the recommendation and mark it assumed.

1. **Who reads the board**
   * Reading: the request names no reader.
   * Recommended: CS and warehouse leads who need to see where a claim waits between teams.
   * Why: a handoff highlight is a question about ownership.
2. **What the board must not do**
   * Reading: the runbook mixes live steps with one pilot rule.
   * Recommended: it must not show the €20 pilot as live, and it must not name services or tools.
   * Why: either would send a reader away with a wrong picture of today's process.
3. **Which decisions go to the claims table**
   * Reading: "every decision is logged" could mean only the CS photo check or also the warehouse steps.
   * Recommended: draw one dashed log link from the CS check ("Damage clear?"), with the claims table in the CS lane.
   * Why: the check is the only step the runbook calls a decision, and the claims table is the only place named for logging.

Is this the right reading of the board?