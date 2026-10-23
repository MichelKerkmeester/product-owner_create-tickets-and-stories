The plan and two source gaps need one answer before I write.

**Reading**
The Fernhouse context (`context/fernhouse-context.md`) covers sign-in and accounts through `accounts-service`, returns and refunds through `orders-service` and CS, the warehouse through the warehouse system and `shipping-service`, and payments through the payment provider. It gives the guest/account distinction at checkout but no signup steps, and it has no billing service or billing flow.

**Question**
1. Which plan owns the new board? The account holds `<figma-plan-1>` (Pro, full seat), `<figma-plan-2>` (Pro, member) and `<figma-plan-3>` (Starter, view). None is called `Fernhouse Product`. If it is a project inside one of them, send the project link.
2. Does billing mean the customer payment and refund through the payment provider, or Finance's carrier invoices?
3. Does the board cover the five named areas only, or all seven key flows in the context: browse and cart, checkout, promotions, fulfilment, after dispatch, returns and wishlist?

**Recommended**
Use `<figma-plan-1>`, treat billing as the customer payment and refund through the payment provider, and keep the board to the five named areas. Draw two process diagrams with lanes on one new FigJam file: `1. Buy and ship` for signup, order, payment, warehouse and delivery, then `2. Return and refund` for the return and the refund, with the warehouse check between them. Both are checked against the diagram rules and pass.

**Assumed until you correct it**
The reader is the Fernhouse product team. The question is how an order moves from signup to refund and where work changes hands. Signup is one entry step because the context has no signup screens. The customer posts the item back with the emailed return label, which the context implies but does not state. The 30-day window, the €200 CS refund limit, promotions, tracking and wishlist stay off the board and go under `Left out:`.

If you want a system map or signup screens instead, say so and send the signup or billing source.