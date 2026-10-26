Before drawing anything, here's how I read the runbook. Please confirm or correct it; nothing goes onto a board yet.

**What the board answers:** How does a Fernhouse damaged-item refund move from the customer to CS to the warehouse, and where does the claim pass to the warehouse?
**Outcome:** One process diagram with three lanes. The refund is released at the end, and the step where an approved claim goes to the warehouse is the one highlighted node.

**What the runbook settles (current behavior)**
- Customer: reports the damage with a photo through the help form
- CS agent: checks the photo
- Decision "Damage clear?": yes means CS approves on the spot. Unclear means CS asks the customer for a second photo
- Handoff (highlighted): the approved claim goes to the warehouse queue
- Warehouse operator: books a courier pickup, inspects the item when it arrives, then releases the refund
- Every decision is logged in the claims table. I'll show this as one note on the board rather than a node on every step

**What I'd leave off the board**
- The rule that refunds under €20 skip the pickup. It's a pilot that isn't live yet, so drawing it would show it as current behavior. I'd list it under "Left out" when I deliver, unless you'd like it drawn in its own style and labelled "Proposed, not live"

**Open, with my recommendation**
1. **After the second photo.** The runbook doesn't say what happens next. I recommend a loop back to "CS checks photo" and marking it as assumed.
2. **Rejection.** The runbook has no path where CS rejects a claim. I recommend not drawing one and listing it as a gap.
3. **Failed inspection.** The runbook doesn't say what happens if the item doesn't show damage when the warehouse inspects it. I recommend the same: no branch drawn, listed as a gap.
4. **Look.** I'd go left to right with three zones (Customer, CS, Warehouse). Title: "Fernhouse damaged-item refund". Source line: "Support runbook".

Where the board goes comes up at the write step, once this reading is settled.

Is this reading right, including leaving the under-€20 pilot off the board?