I haven't written anything yet. The Flow Mode rules say no board write happens before an intake round, a playback and a write gate, and you haven't sent a source for the checkout payment yet. Here is round one.

**Type check:** you asked for a sequence diagram, which fits a question about the order in which parties exchange messages during checkout payment. I'll keep it unless your answers point to screens (a user flow) or payment statuses (a state diagram).

**Target file:** I'll write into `<test-file-key>` as you asked. The board goes 400 px to the right of whatever is already there, and nothing existing gets moved or deleted. The write gate will confirm the file opens as a FigJam board before any write. If it doesn't, the fallback is a new file in the Barter team plan, left in drafts with no project, as you said.

**1. Reader and outcome**
- Reading: the request names the topic and the diagram type, but not who reads the board or what they decide after reading it.
- Question: who is the board for, and what should they be able to do after reading it?
- Recommended: engineers and the PM checking how one payment call runs from the app through to the payment provider and back, so they can agree where a failure needs handling.
- Why: most readers of a sequence diagram are asking about call order and failure points.

**2. What the board must not do**
- Reading: "checkout payment" could mean the happy path only, or also refunds, retries, 3-D Secure and webhooks.
- Question: what should the board leave out?
- Recommended: show one card payment, including the declined branch. Leave out refunds, payouts and retry loops, and note them on the `Left out:` line.
- Why: a sequence diagram stays readable at about 9 to 12 messages, and refunds are a separate sequence.

**3. Sources**
- Reading: I don't have a source. A sequence needs the parties, every message in order and the status codes that matter, and I won't make up calls the checkout doesn't actually make.
- Question: what can you share that shows the real calls? Route or handler code, an API doc, a Story or Doc, or a list of steps would all work.
- Recommended: the checkout payment handler code or its API reference, plus the name of the payment provider (for example Stripe or Adyen).
- Why: code shows the true call order. Without it, every message would be marked assumed.

If you skip a question, I'll go with its recommended answer, mark it assumed and show it in the playback before anything is written.

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.