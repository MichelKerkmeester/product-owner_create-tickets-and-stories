Nothing is written to the board yet. This is intake round 1 of 3.

**Settled so far**
- **Target:** the existing file `<test-file-key>`, as a new board section, with no new file. You named the Fernhouse Product plan, so the write gate will state it as the plan you supplied.
- **Source:** Key flows item 6 in `fernhouse-context.md`, plus the glossary's 30-day return window and the CS refund limits. It is the only source for returns, and it describes current behavior.
- **What it states:** the customer contacts CS. A CS agent creates the return in Admin and emails a return label. The warehouse checks the item and the agent refunds. A CS agent can refund up to €200 per order, and a CS lead approves anything above that.

**1. Which return flow**
- Reading: the context says there is no self-serve return today, and no source describes one.
- Question: do you want today's CS-led flow, or a proposed self-serve flow?
- Recommended: today's CS-led flow.
- Why: it is the only one a source supports, and drawing a self-serve flow would mean inventing its steps.

**2. Reader, question and outcome**
- Reading: no source names who the board is for.
- Question: who reads it, and what do they need to decide afterwards?
- Recommended: a Post-purchase team member or PM scoping `RET` work. The board answers "who does what, in which order, from a customer's first contact to the refund". Afterwards the reader can see where work changes hands.
- Why: that question points to a process diagram with a lane per role (Customer, CS agent, Warehouse operator and CS lead). A user flow would need screens, and none were supplied.

**3. What the board must not do**
- Reading: the order tracking brief puts tracking for return parcels out of scope. The sources describe no email copy or label API for returns.
- Question: what should this board refuse to show?
- Recommended: no proposed self-serve steps, no return-parcel tracking and no label or email mechanics.
- Why: each would add nodes the reader does not need to follow who does what.

Rounds 2 and 3 will ask about the decisions the source leaves open. These include what happens after the 30-day window, what the warehouse check can conclude, and when the CS lead step applies. If you skip a question, I take the recommended answer and mark it assumed in the playback before the gate.