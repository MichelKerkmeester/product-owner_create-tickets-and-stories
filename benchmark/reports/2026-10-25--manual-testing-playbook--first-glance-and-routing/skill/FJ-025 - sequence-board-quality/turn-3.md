The model passes the pre-write check and both boards compose. Nothing is written yet.

**Check**
* Board 1 passed as a sequence with 4 participants and 7 messages
* Board 2 passed as a sequence with 3 participants and 6 messages
* Each board's code fits one `use_figma` call

**Labels:** your wording gave no request path or hub message name, so the labels use your verbs. Only the status codes 201 and 402 carry specifics. If you have the real path or event name, give it to me now and I'll recompose before the write.

**Question:** in what order do the guest app, the booking API, the payment provider and the partner hub exchange messages when a guest pays at checkout?

**Outcome:** Booking and Payments engineers can read the checkout calls in order, with status codes, for an authorised card and for a declined card.

**Glances**
* Board 1, first: message 3, "Authorise the card", the call that decides the checkout
* Board 1, second: message 4, "Authorised", the answer that lets the booking API confirm the hold and answer the app
* Board 1, last: message 6, "Tell the partner hub", which doesn't hold up the 201
* Board 2, first: message 4, "Declined", the answer that sends the booking down the failure path
* Board 2, second: message 5, "Release the hold", which gives the room back before the app hears anything
* Board 2, last: message 1, "Post the booking", the same opening call as board 1

**Plan:** Roamstay Product, as you named it. `whoami` can list your plans but can't say which plan owns an existing file, so I'm relying on your word.

**File:** the existing FigJam file `<test-file-key>`. No new file is created.

**Writes:** two composed boards, "1. Checkout payment, happy path" and "2. Checkout payment, declined card". Each has a title, a one-sentence subtitle, a key and a source line, at balanced detail, engineer wording and laptop reading distance. They land 400 pixels to the right of anything already on the page, board 1 first, so they read left to right.

**Extensions:** none.

**Calls:** `create_session`, two `use_figma` calls (one per board) and two `get_figjam` read-backs, so five in all. I load Figma's `figma-use` and `figma-use-figjam` skills first. If Roamstay Product is on a Starter plan or you hold a View or Collab seat, Figma caps tool calls at six a month and reads count, so this write would use most of it.

**Rollback:** each write returns one board section id. Deleting a board means deleting that section through `use_figma`, and I only do that on a separate yes from you.

Write both boards?