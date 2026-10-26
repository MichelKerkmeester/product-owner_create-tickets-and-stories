I haven't drawn or written anything yet. I'm at the first intake round, and it has a gap I can't fill without you: you didn't send a source for the booking statuses, and Flow Mode never invents states or transitions. I saved no file, since Flow Mode only ever delivers a board.

I've noted the target file, `<test-file-key>`. Before writing I'll ask for a yes that names that file, which plan it's in and how to undo the write. Nothing goes on the board until you give that yes.

**Round one**

1. **Source**
   - Reading: The only booking states in this workspace are in `context/roamstay-context.md`. That's Roamstay, a hotel marketplace, not Barter. It describes four states:
     - `payment_pending`: the booking waits here after the guest pays.
     - Confirmed: the payment provider's webhook moves the booking here.
     - Expired: a booking still in `payment_pending` after 30 minutes ends here.
     - Cancelled: the guest cancels under Trips before the free-cancellation deadline, or through Guest Support after it.
   - Question: Whose booking lifecycle is this, and which source lists its statuses and what moves a booking between them?
   - Recommended: Send the status list (for example a schema, enum or spec) for the product you mean. If you meant Roamstay, confirm that file as the source.
   - Why: A state diagram needs every state and the event behind each move. Without a source, each one would be a guess.

2. **Reader, question and outcome**
   - Reading: The request names the topic but not the reader.
   - Question: Who will read this board, and what should they be able to decide after reading it?
   - Recommended: Product and engineering in the Booking squad. The board would answer: "Which statuses can a booking hold, and what moves it between them?" They'd use it to check edge cases, such as expiry and late cancellation, before planning work.
   - Why: The reader's question decides how much detail the board shows and which state gets the highlight colour.

3. **What the board must not do**
   - Reading: The request doesn't limit the scope.
   - Question: What should this board leave out?
   - Recommended: Leave out payment-provider internals, refund mechanics and the screens. Show statuses and their triggers only.
   - Why: Those belong on a sequence or user-flow board, and leaving them out keeps this one readable on a laptop.

If a question goes unanswered, I'll use my recommendation, mark it as assumed and list it in the playback before the write gate.

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.