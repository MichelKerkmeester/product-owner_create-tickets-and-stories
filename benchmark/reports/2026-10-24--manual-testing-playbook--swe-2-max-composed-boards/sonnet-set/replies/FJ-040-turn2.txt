Nothing is written yet. This is the playback, which runs before I draw the model and ask for the write. I'll move on once you answer it.

Settled from your "go ahead":
- Reader and question: new teammates and ticket writers across the six teams ask who does what in each area and where work changes hands. The outcome is that they can name the right feature code and owning service.
- Boards: four process boards in your order, with signup left out because no source states its steps. The order is Returns, Refunds, Warehouse, Billing.
- Excluded: promotions, wishlist, order tracking, pallet carrier detail, self-serve returns (a proposal) and saved cards (a draft).
- Source: `fernhouse-context.md`, treated as current behavior. The order-tracking brief backs one billing fact, that `Order placed` is set when payment is authorised. The refund example in the skill's assets is an invented fixture, so I did not use it as a source.
- Dials: Balanced detail, Mixed audience, Laptop reading distance, all running left to right.
- Target: the existing file `<test-file-key>`, with the plan Fernhouse Product as you gave it. Each board lands as its own framed section.

Outline per board (lane in brackets):
1. Returns, with Customer, CS agent and Warehouse operator lanes. It has 6 nodes and 5 connectors.
   - Contact CS within 30 days of delivery [Customer]
   - Create the return in Admin [CS agent]
   - Email the return label [CS agent]
   - Send the item back [Customer]
   - Check the item [Warehouse operator]
   - Continue to refund, the hand-off end
2. Refunds, with Warehouse operator, CS agent and CS lead lanes. It has 5 nodes and 5 connectors.
   - Item checked [Warehouse operator]
   - Decision "Refund over €200?" [CS agent]. No goes to issue, Yes goes to the CS lead.
   - Approve the refund [CS lead], in focus because it is the only gate on this board
   - Issue the refund [CS agent]
   - Refund email sent, the end
3. Warehouse, with Orders service, Warehouse operator, Shipping service and Parcel carrier lanes. It has 9 nodes and 8 connectors.
   - Order paid, then Send the order to the warehouse system [Orders service]
   - Start picking [Warehouse operator]
   - Ask for a label per parcel [Shipping service]
   - Create the label [Parcel carrier]
   - Receive the label event [Shipping service]
   - Pack and label the parcel, then Report the order packed [Warehouse operator]
   - Collected at 18:00, the end. Its incoming connector reads "Paid before 15:00", so I draw no exit for later orders.
4. Billing, with Customer, Checkout service, Payment provider and Orders service lanes. It has 5 nodes and 4 connectors.
   - Enter payment details [Customer]
   - Open the payment session [Checkout service]
   - Authorise the payment [Payment provider]
   - Create the order [Checkout service]
   - Order placed, the end [Orders service]

Assumed, so correct these if wrong:
- "Send the item back" in Returns. The context says the warehouse checks the item but never says the customer ships it. You'd settle it by confirming the step or naming who moves the item.
- Billing means the payment at checkout and nothing else. The money going back to the payment method on a refund is not stated, so it stays off the boards.

Named gaps. I leave all of these out of the boards unless you supply the source, and they go on the reply's `Left out:` line:
- Signup steps
- What happens after a return window passes
- What happens when the item check fails
- Whether a CS lead can reject a refund
- What happens when a payment is declined
- Later orders after the 15:00 cut-off
- Discount splits on orders from before 2026-05-01

Does this reading hold? Reply "yes" to move on to the model, the pre-write check and the write gate, which will ask for its own yes. Or correct any row above.

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.