I'm treating "use your recommended answers" as the answer to round 1. Nothing is drawn or written yet. This is the playback of how I read the request, and it needs your answer before I build the model.

**Question:** who does what in each Fernhouse area, and which service owns each step?
**Reader:** a product or engineering team member picking up an area they don't own.
**Outcome:** they can see who owns each step and where work changes hands before they write a ticket.
**Must not:** show a step, branch or rule the sources don't state.

**Boards I would draw**
- **Returns:** a process with three lanes, Customer, CS agent and Warehouse operator. It starts when the customer contacts CS and ends on a hand-off to the Refunds board. The subtitle carries the 30-day window and the 6-day average from first contact.
- **Refunds:** a process with two lanes, CS agent and CS lead. It starts at "refund needed" and has one decision, over €200 per order. Over the limit goes to the CS lead and under it the agent refunds.
- **Warehouse:** a process with five lanes, orders-service, Warehouse, shipping-service, Parcel carrier and Pallet carrier. It runs from a paid order to the 18:00 collection for parcels and to the 16:00 booking file for pallets. The parcel or pallet split is the one decision. It has 11 nodes, inside the 12-node limit for a laned process.

**Settled by the sources**
- `fernhouse-context.md` (2026-09-18) gives the steps for all three boards. Class: current behavior.
- The label API notes (2026-09-11) give the shipment per parcel and the `label.created` webhook. Class: current behavior.
- The 2026-09-16 label thread proposes fixes that are not shipped. Class: proposal, so it stays off the boards.

**Left out, named**
- Outside the 30-day window: no source says what happens.
- A failed warehouse check: no source describes it.
- How a refund reaches the customer, and the refund email: no source states the mechanism or its trigger.
- What the CS lead does on a decline: not stated.
- A paid-after-15:00 order and an order holding both parcel and pallet items: not described.
- Label failures and the duplicate-label fixes: proposals only.
- Signup and billing, covered under "Still open" below.

**Assumed, two rows**
- The customer sends the item back after receiving the return label. The doc implies it and never states it, so the step is labelled to say so. Settled by a source or a screen from the returns team.
- The parcel or pallet split happens when the warehouse system receives the order, before picking. The doc names the split without saying when it happens. Settled by a Fulfilment engineer.

**Looks, assumed:** first glances are "Create the return in Admin" on Returns, "Over €200 per order?" on Refunds and the 18:00 collection on Warehouse. The dials stay balanced, mixed and laptop.

**Still open:** you sent no signup or billing source, so by the recommended answer they stay off the board and go under `Left out:`. The doc shows no signup steps and no subscriptions or invoices. If billing means paying for an order at checkout, the doc supports a short board for it, and I can add it.

Is this the right reading, including the two assumed steps and signup and billing staying out?