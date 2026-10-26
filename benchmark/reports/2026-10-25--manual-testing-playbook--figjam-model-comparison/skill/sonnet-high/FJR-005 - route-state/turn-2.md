Here is how I read the board. Nothing has been written to the file.

**Question:** which statuses does a Roamstay booking pass through at checkout, and what moves it between them?
**Outcome:** support and PM can read the statuses a new booking can be in and the event behind each move. The board is labelled partial.

**What the sources settled**
- `context/roamstay-context.md`, "Checkout and payment" and "Known constraints" (current behavior, last reviewed 2026-09-18):
  - Pay now: the booking waits in `payment_pending` until the payment provider confirms by webhook, then moves to confirmed.
  - Pay now, no confirmation: a booking still in `payment_pending` after 30 minutes expires and its room goes back on sale.
  - Pay at property: the card is stored as a guarantee and the booking confirms at once.
- INC-0412 (`context/roamstay-payment-webhook-incident-notes.md`) repeats the same two exits from `payment_pending`: the webhook confirms it, and 30 minutes without one expires it. This is the second source behind those two moves.

**Drawn:** three states and three moves.
- Pay now enters `payment_pending`.
- Pay at property enters confirmed.
- `payment_pending` goes to confirmed on the payment confirmation webhook.
- `payment_pending` goes to expired after 30 minutes without it.

That is a small board, close to a list. I recommend drawing it anyway, because you asked for the diagram and each later status can be added once its source exists.

**Left out**
- Every status after confirmed: check-in, stay, completion, no-show. No source states them.
- Cancellation: the context describes a guest cancelling under Trips and a refund, but names no cancelled status.
- Any end of the lifecycle. The board does not mark confirmed or expired as final, because no source says so.

**Assumed**
1. Reader and outcome: support and PM, at balanced detail, a mixed audience and laptop reading distance. A different reader settles it.
2. The state name `Expired`. The source says the booking "expires" and names no status. A status name from the booking-service settles it.

**Product mismatch:** the file holds Loomlist boards, but the booking source is Roamstay's. I'm treating Roamstay as the product, because it is the only booking source in `context/`.

Is this the right reading of the board?