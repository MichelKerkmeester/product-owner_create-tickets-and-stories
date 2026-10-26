I haven't started the board. Your request fits two diagram types, so I need to know which one you want first.

**Reading:** The only source here is `context/fernhouse-context.md` (Lotte's company context, updated 2026-09-18).
- **Returns, refunds and the warehouse:** these have documented steps. A CS agent creates the return in Admin, the warehouse checks the item and the agent refunds. For fulfilment, orders-service sends the paid order to the warehouse system, shipping-service gets a label from the parcel carrier, and the 15:00 cut-off feeds the 18:00 collection.
- **Signup:** the source has no signup steps. It covers only sign-in, saved addresses and guest checkout, with accounts-service as the owner.
- **Billing:** the source has no billing system. It covers payment at checkout through the payment provider, and refunds going back out.
- **Target:** I'll add the board as a new section in file `<draft-file-key>`, beside what is already there. That needs no plan and no new file, so the Fernhouse Product plan only matters if I had to create one. I would fall back to the Barter team plan, in drafts with no project, only if that file can't be written.

**Question:** What does the reader of this board want answered?
- An **architecture** answers "what parts make up Fernhouse and how do they connect?"
- A **process with lanes** answers "who does what, in which order, and where does work change hands?"

**Recommended:** Architecture, as one overview board of the five areas.

**Why:** The source names a service or third party for all five areas. It has process steps for only three of them, so a process board would leave signup and billing empty. The detailed return and refund process would then be a second board, listed under `Left out:`, and a signup user flow would need screens or a doc first.