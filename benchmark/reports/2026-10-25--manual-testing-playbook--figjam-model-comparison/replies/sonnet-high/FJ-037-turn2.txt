Path: `export/002 - Story-fernhouse-return-flow.md`
Verified: read-back succeeded; 56 lines
HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.
Quality: every floor met | Kind: Story | Energy: Standard

The Story is a Customer story that lets someone start a return from a delivered order on web, iOS and Android without contacting CS. It carries the `30 days` return window and the three platforms as requirements, with two acceptance criteria: starting a return inside the window, and being refused outside it. I took your recommended answers, so the CS agent side in Admin is out of scope and there is no Delivery section or References block.

### Open items
1. **Return details not supplied**
   - **Situation:** Return reasons, how the label reaches the customer, the refund rule, parcel and pallet items and UK parcels were only candidates in my question, so none became a requirement
   - **Open:** Send the exact values and copy and I'll add them to Requirements
2. **Added outcomes**
   - **Situation:** I added "the customer sees that Fernhouse received the request" to the first criterion and "the customer is told why" to the second
   - **Open:** Strike either if the design gives no such message
3. **Guests**
   - **Situation:** The flow starts from an order, and a guest has no order history to come back to
   - **Open:** Confirm the Story covers signed-in customers only, or name how guests reach their order
4. **Orders not yet delivered**
   - **Situation:** The window runs from delivery, and the Story says nothing about an order still in transit
   - **Open:** Confirm such an order cannot start a return
5. **Helpdesk outcome**
   - **Situation:** "Fewer return requests reach the helpdesk" comes from the context's 1,900 a month and has no target number
   - **Open:** Add a target, or confirm none is wanted
6. **Figures**
   - **Situation:** About 1,900 requests a month and 6 days to refund come from the Fernhouse context dated 2026-09-18
   - **Open:** Nothing to confirm

Before I draw anything, this is how I read the request.
Question: which steps does a customer go through to start a return, and where does the return window stop them?
Outcome: a reader can follow a return from a delivered order to a registered return and see the exit for an order past its window.
Settled by the sources: the Story I just saved gives the steps, the `30 days` window, its exit and the three platforms.
Left out: the CS agent's return handling in Admin, which the Story keeps out of scope.
Assumed: balanced detail for a mixed audience of product and CS leads, labels in the Story's own words and one flow shared by web, iOS and Android.
Still open: the screens. No screenshot, design link or screen list was supplied, so the board shows the Story's steps and names no screen until you send them.
Is this the right reading of the board, drawn from the Story's steps until you send the screens?