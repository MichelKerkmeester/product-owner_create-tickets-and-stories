Round two. "Use the recommended answers" settles questions 1 and 2. Question 3 is still open: its recommended answer was for you to send handler code or an API doc, and nothing has come in yet. Instead, I searched the `context/` folder and found two payment sources from different products, so I need to know which one this board is about.

**Settled so far**
- Reader: engineers and the PM (assumed, from my recommendation)
- Question: in what order the parties exchange messages during one card payment at checkout (assumed)
- Outcome: the reader can agree where a failure needs handling (assumed)
- Scope: one card payment including the declined branch, with no refunds, payouts or retry loops (assumed)

**1. Product and source**
- Reading: there are two candidates.
  - `roamstay-payment-webhook-incident-notes.md` describes payments of systems that are running today. It names booking-service, payments-service and the payment provider, the `/v2/psp/webhooks` path with its 200 and 401 responses, the `payment.captured` event and bookings that leave `payment_pending` or expire after 30 minutes.
  - `fernhouse-save-card-draft.md` is a draft PRD (marked "draft, not refined yet"), so it counts as a proposal. Anything drawn from it would be labelled as proposed.
- Question: which product's checkout payment should the board show?
- Recommended: Roamstay "Pay now", using the incident notes.
- Why: they name real parties, paths and status codes, and a sequence diagram needs all three.

**2. Entry and exit**
- Reading: the notes show how the payment ends: the provider's webhook reaches payments-service, and the booking leaves `payment_pending` while the guest waits on the "Confirming your booking" screen. They don't show how the payment starts.
- Question: where does the sequence start, and where does it end?
- Recommended: start when the guest taps Pay now. End when the booking leaves `payment_pending`, either confirmed, or expired after 30 minutes if no result arrives.
- Why: both endpoints are the ones the notes use. The start of the payment would be marked assumed.

**3. Parties and the missing opening calls**
- Reading: the notes name four parties: the guest app, booking-service, payments-service and the payment provider. They don't say which service calls which to begin the charge, or how a decline comes back.
- Question: who calls whom between "Pay now" and the provider's charge, and how does a decline reach the guest?
- Recommended: guest app → booking-service → payments-service → payment provider, with a decline returned as a `payment.failed` webhook on the same path. If you don't know, send a payments-service route file or ask the Payments squad (the notes name Karim and Elif).
- Why: if I guess these calls, three or more rows end up assumed. Flow Mode only draws with at most two assumed rows, because more than that would be a diagram of a system I made up.

If you accept all three as recommended, I'll note that the opening calls are still unconfirmed and send the full playback, which waits for your answer. That is still before any model is built or anything is written to `<test-file-key>`.

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.