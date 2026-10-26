Your answers to questions 1 and 3 are now set. Question 2 is still open. My recommendation there only described what format to send the statuses in, so it doesn't tell me what Barter's statuses actually are. I can't draw the board until I have them.

**What's settled so far**
- **Reader:** the product team and engineers
- **Question the board answers:** which statuses can a Barter order be in, and what event moves it from one to the next?
- **What readers get from it:** they can agree the full list of statuses and spot any status change with no trigger
- **Scope:** statuses and the events between them only. No screens, notifications or system internals. Refunds and returns appear only if they change the order's status
- **Diagram type:** a state diagram, using the product's names for statuses, about 9 statuses at most
- **Target file:** the existing FigJam file `<test-file-key>`. Nothing gets written until you say yes in a separate step

**Still open**
- **The statuses:** what Barter orders can be
- **The triggers:** what event moves an order from one status to the next, and any rule that blocks a change
- **The start and end statuses:** where an order begins and where it finishes

**Question:** where can I find Barter's order statuses?
- **What I can tell:** nothing in this workspace describes Barter orders. The one list of order statuses here belongs to a fictional sample shop.
- **Recommended:** paste a plain list like `status A → status B, when <event>`, or point me to the spec, schema or ticket that defines them.
- **Why:** each box and arrow needs a source. Using the sample shop's list or guessing would put statuses on the board that Barter doesn't have.

If a source only gives some of the triggers, I'll label each missing one `Unknown trigger` and list it on the reply's `Finding:` lines.

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.