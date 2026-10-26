I haven't written anything to the board, because I have no source for the booking statuses yet.

**What I found**
- File `<draft-file-key>` holds three Loomlist boards: block sync, push delivery and the offline mode launch plan. None of them mentions bookings. A new board would go in as a new section to the right of them, and nothing already there would change.
- `context/` has only a fragment of a booking lifecycle, in the Roamstay notes. A Pay now booking waits in `payment_pending` until the payment provider's webhook confirms it, then moves to confirmed. It expires after 30 minutes if still pending. The Pay at property path and all later statuses (check-in, cancellation, completion and so on) are not described.
- The booking states in the packet's worked example are invented for that example, so I won't use them as a source.

**Round one**
1. **Source and product.** Reading: you mean Roamstay's bookings, but the file is Loomlist's and no statuses doc was supplied. Question: which doc or ticket states the statuses and what moves a booking between them? Recommended: paste or link the statuses doc. If none exists, I draw only the `payment_pending` slice above, labelled partial, and name every other status as a gap under `Left out:`. Why: a partial real lifecycle beats a full invented one.
2. **Reader and outcome.** Reading: nothing in the request says who reads the board. Recommended: support and PM, who need to see which statuses exist and what triggers each move, drawn at balanced detail on a laptop. Why: that is the question a state diagram answers.
3. **What the board must not do.** Recommended: no status or trigger the source doesn't state, and nothing proposed drawn as current behavior. Why: a guessed transition reads as a fact.

An unanswered question stands as its recommended answer, marked assumed, and I'll name it in the playback before any write.