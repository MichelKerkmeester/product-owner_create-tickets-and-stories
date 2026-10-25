I haven't touched the FigJam file, and nothing is saved to `export/`. The board is a sequence diagram, because your question is the order of messages between parties. Three questions come first, each with the answer I'd take if you don't reply.

**Settled so far**
* Target: the existing file `<test-file-key>`, as a new board inside it rather than a new file, in the Roamstay Product plan
* Parties: GuestApp, BookingApi, PaymentProvider and PartnerHub
* Happy path from your wording: post the booking, hold the room, authorise the card, confirm the hold, tell the partner hub, answer 201
* Declined card from your wording: release the hold, answer 402
* Not in your wording: I'd read the provider as answering the authorise call ("Authorised" or "Declined"), and the hub message as fire-and-forget

**Round 1 of 3**

1. Reader and outcome
   * Reading: you name the calls but not who reads the board
   * Question: who is the board for, and what should they be able to do after reading it?
   * Recommended: Booking and Payments engineers, who can read the checkout calls in order with paths and status codes
   * Why: the brief is API calls and status codes, which is engineer-level detail

2. Scope
   * Reading: a sequence draws one path per board because a branch would render flat, and your wording holds two paths
   * Question: should the declined card be a second board in the same file, and what must neither board show?
   * Recommended: two boards. "Checkout payment, happy path" has 4 parties and 7 messages. "Checkout payment, declined card" has 3 parties and 6 messages. Neither shows webhooks, `payment_pending` or retries
   * Why: both paths fit the sequence budget of 5 parties and 12 messages, and your wording names no webhook or retry step

3. Source authority
   * Reading: the payments brief isn't in the workspace, so I worked from your wording. `context/roamstay-context.md` says only `payments-service` talks to the payment provider. It also says Pay now holds the booking in `payment_pending` until the provider's webhook confirms. Your wording has the booking API calling the provider directly and answering 201 in the same run
   * Question: which source governs, and is the brief current behavior, approved direction or a proposal?
   * Recommended: your payments brief governs, drawn as current behavior, with the webhook step listed under `Left out:`
   * Why: you named the brief as the source, and the context file describes the Pay now path in prose only

If you skip any of these, I'll proceed on the recommended answer and mark it assumed in the playback. The playback comes next, then the write gate as its own message. The write is two `use_figma` calls (one per board) plus a `get_figjam` read-back, and it only happens on your yes to the gate.