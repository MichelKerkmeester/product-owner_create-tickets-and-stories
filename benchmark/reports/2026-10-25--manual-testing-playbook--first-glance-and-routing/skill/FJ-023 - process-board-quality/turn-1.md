Before I draw anything, this is how I read the request.

**Question:** who does what in a damaged-item refund, and where does the claim change hands between the customer, CS and the warehouse?

**Outcome:** a reader can follow a claim from the customer's report to the released refund and see where CS passes it to the warehouse.

**Type:** a process with three lanes, Customer, CS agent and Warehouse operator, in the order the claim reaches them. I'm using the defaults of balanced detail, a mixed audience and reading on a laptop.

**Settled by the runbook:**
* The customer reports damage with a photo through the help form.
* The CS agent checks the photo, then approves clear damage or asks for a second photo.
* An approved claim goes to the warehouse queue. There the operator books a courier pickup, inspects the item on arrival and releases the refund.
* Every decision is logged in the claims table.

**Read with medium confidence:** the second photo comes from the customer and goes back to the same check. The runbook only says CS asks for it.

**The highlight:** a connector can't carry the pink outline. It goes on "Approve the claim", the step that sends the claim over, and the connector crossing into the warehouse is labelled "Claim queued". The queue and the pickup are one move, so the queue is not a node of its own.

**Left out:** refunds under €20 skipping the pickup. It is a pilot that is not live, and the runbook doesn't say where that path rejoins the process, so I would not draw it. Two gaps are named in the reply instead of drawn: no exit when the second photo is still unclear, and no path for a failed inspection.

**Assumed, each settled by your answer:**
* The reader is the product team plus the CS and warehouse leads who own the handoff.
* "Every decision" means the CS clear-or-unclear call. I'd draw it as one dashed link to a claims table in the CS lane, and the warehouse steps would not log. A runbook line on warehouse logging would change that.

**Where it goes:** the file key you gave, not a new file. The gate confirms the details.

**Question:** is this the right reading, and is there anything the board must not show?

**Recommended:** yes as read, and the board must not show the pilot or any refusal path as current behavior.

**Why:** the runbook states neither where the pilot rejoins nor what follows a failed check, so drawing them would be guessing.