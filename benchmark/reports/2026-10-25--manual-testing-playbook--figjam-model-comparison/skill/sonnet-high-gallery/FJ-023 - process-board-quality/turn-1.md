Before I draw anything, this is how I read the request. Nothing has been written to FigJam.

**Type:** process. You ask who does what and where work changes hands, and a list would not show the lane changes.

**Question:** who handles a damaged-item refund claim, and where does it move from CS to the warehouse?
**Reader:** assumed to be someone on the Fernhouse team who knows the runbook only in outline. Who opens the board would settle it.
**Outcome:** a reader sees which team owns each step and notices the handoff to the warehouse first.
**File:** I read "new board" as a new section in the file you named, not a new file. The gate states the details.

**Settled by the runbook text you gave:** the customer reports damage with a photo through the help form. A CS agent checks the photo, approves clear damage on the spot and asks for a second photo when it is unclear. An approved claim goes to the warehouse queue, where an operator books a courier pickup, inspects the item on arrival and releases the refund. All of this is current behavior.

**Outline**, in drawing order:
1. Show who handles a damaged-item refund and where the claim moves from CS to the warehouse.
2. Customer lane has "Report damage with a photo" (start) and "Send a second photo".
3. CS agent lane has "Damage clear?" (exits Clear and Unclear) and "Approve the claim".
4. Warehouse lane has "Book a courier pickup", "Inspect the item" and "Refund released" (goal).
5. Seven connectors:
   * Report goes to the check.
   * Unclear goes to the second photo.
   * The second photo goes back to the check.
   * Clear goes to Approve.
   * Approve goes to Book a courier pickup, labelled "To warehouse queue".
   * Pickup goes to Inspect.
   * Inspect goes to Refund released.

**Two framings:** the laned board (recommended) shows the handoff as a connector crossing from the CS lane to the warehouse lane, at the cost of a taller board. A single chain with the owner in each label is cheaper, but then the handoff is only a word.

**The look:** the pink accent marks "Approve the claim", with the key entry "In focus: handoff to warehouse". "Refund released" is the green goal and the lanes are the zones. The title is "Damaged-item refund". The subtitle is one sentence on how a claim moves between the customer, CS and the warehouse. The source line names the runbook and what is left out.

**Gaps the runbook does not cover:** a second photo that is still unclear, and an inspection that fails. I will not draw a decline path for either.

**Assumed, each with my recommended answer:**
* **Second photo return:** it goes back to the same "Damage clear?" check. The runbook does not state this edge. Recommended because there is no other CS step for it to reach.
* **Dials:** balanced detail, mixed audience, laptop reading distance.

**Three calls I need your view on:**
* **Pilot under €20:** recommended is to leave it out and name it under "Left out", because it is not live and drawing it would show a second route to a refund. The alternative is a dashed connector labelled "Pilot, not live".
* **Claims table logging:** recommended is to leave it off the shapes and name it under "Left out". The runbook says every decision is logged but not which step writes the log. The alternative is a store in the CS lane fed by "Damage clear?".
* **Highlight:** recommended is the sending step, "Approve the claim", because the accent marks a node and not a connector. The alternative is "Book a courier pickup", the first warehouse step.

The board must not show the pilot as live or invent decline paths.

Is this the right reading of the board, including my recommended answers on those three calls?