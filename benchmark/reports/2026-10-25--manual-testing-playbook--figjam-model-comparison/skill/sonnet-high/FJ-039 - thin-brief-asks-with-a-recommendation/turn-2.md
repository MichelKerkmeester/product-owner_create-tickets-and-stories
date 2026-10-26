Before I draw anything, this is how I read the request. Nothing is modelled or written yet.

**Question:** who does what in a Fernhouse return today, and where does it change hands between the customer, CS and the warehouse?

**Outcome:** a Post-purchase reader can see which role owns each step from the first contact to the refund, and where the CS lead steps in. That is a process with four lanes.

**Settled by the sources:** `context/fernhouse-context.md` is the only source and counts as current behavior.
- Key flow 6 gives the steps, the 30 days from delivery and the 6 day average refund time.
- Personas and roles gives the CS agent's €200 refund limit and the CS lead's approval above it.

**Outline (userIntent first):**
0. Who does what in today's CS-led return, and where does it change hands
1. Ask CS within 30 days of delivery (customer, start)
2. Create the return and email the label (CS agent)
3. Check the item (warehouse operator)
4. Refund over €200? (CS agent, decision)
5. Approve the refund, on Yes (CS lead)
6. Customer refunded (CS agent, end)
7. Edges: 1 to 2, 2 to 3, 3 to 4, 4 to 6 on No, 4 to 5 on Yes, 5 to 6

Remove test: steps 2 and 3 of the source's list ("creates the return in Admin" and "emails a return label") always travel together and are one actor, so they are one node. That gives 6 nodes and 6 connectors, inside the 12 and 16 a laned process allows.

**Two framings:**
- *Recommended:* the main line runs across the board on one straight route from the customer's ask to the refund, with the CS lead's approval as a single branch below it. It shows every handoff and costs one extra lane for one step.
- *The alternative:* a decision tree with no lanes. It drops the lane for the CS lead but hides who owns each step, which is the question the reader brought.

**The look, my recommended choices:**
- **Accent:** the end, "Customer refunded". Nothing in the source says which handoff is slowest, so no step is put in focus on a delay it does not state.
- **Glances:** first the refunded end, second the warehouse check, the one step another team owns before the refund, and last the CS lead's approval above €200.
- **Detail, audience and distance:** balanced, mixed and Laptop. The labels use Fernhouse's own words.
- **Zones:** none, because the lanes already group the steps.
- **Title:** "How a Fernhouse return runs today".
- **Subtitle:** "Who does what from the customer's first contact to the refund, which takes 6 days on average".
- **Source line:** it names the context note, with the left-out items below.
- **Critique questions for the gate:**
  - Does the eye land on the refunded end first?
  - Do the 30 day window and the €200 limit read without the source beside them?
  - Does any step read as owned by two roles?
  - Is a CS lead lane worth a band for one step?

**Left out, named gaps the source does not state:**
- The customer sending the item back. The source goes from the emailed label straight to the warehouse check
- What happens when the warehouse check fails
- What CS does outside the 30 day window
- Any self-serve return, which does not exist today
- Tracking for return parcels, which the order-tracking brief puts out of scope for its own story

**Assumed, with what would settle it:** the €200 approval applies to the refund at the end of a return. The context note states the limit for refunds in general and says the agent refunds a return, so it joins two sections. A CS runbook or your word would settle it. If it is wrong, the CS lead lane and the decision come off and the board shrinks to 4 nodes.

**Still open:** none.

Is this the right reading of the board?