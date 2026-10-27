Nothing is written yet. All five areas on one board would run far past the per-board node budget, so I need your pick for the first board.

Reading:
* **Destination:** file `<draft-file-key>`, as a new section beside what it already holds. A file you name needs no plan lookup and no `create_new_file`, so the Fernhouse Product plan name changes nothing about the write.
* **Returns and refunds:** Fernhouse context covers both. There is no self-serve return. The customer contacts CS, a CS agent creates the return in Admin and emails a label, the warehouse checks the item and the agent refunds. A CS agent can refund up to €200 per order and a CS lead approves above that.
* **Warehouse:** key flow 4 covers it. A paid order goes to the warehouse system, shipping-service gets a label by webhook, the 15:00 cut-off feeds the 18:00 collection, and pallet items go in a booking file at 16:00.
* **Signup:** the context only says accounts-service handles sign-in and guests check out by email. It has no screens or steps.
* **Billing:** the context only says the payment provider authorises at checkout. It has no invoice or billing steps.

Question: Which flow goes on the first board, and as which diagram type?

Recommended: returns and refunds together as one process board, with lanes for the customer, the CS agent and the warehouse operator, and the €200 approval as its decision.

Why: it is one hand-off chain, every step is stated in the context, and the reader's question is "who does what and where does work change hands", which is a process.

The other three would be later boards, each named under `Left out:`. Warehouse can follow from the same context. Signup needs screenshots or a doc. Billing needs you to say what it covers, such as checkout payment, refund payouts or invoicing.