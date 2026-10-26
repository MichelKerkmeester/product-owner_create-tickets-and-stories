Both models pass the pre-write check and both compose. One change from the playback: board 2 has 3 participants, not 4. The partner hub takes no part in a declined checkout, and the check refuses a participant that sends and receives nothing.

**Question:** in what order do the guest app, the booking API, the payment provider and the partner hub exchange messages when a guest pays at checkout?
**Outcome:** the product and engineering team can follow the checkout calls in order for an authorised card and for a declined card, and see where the room hold is released.

**First glance:**
* Board 1: Authorise card, the call to the payment provider that decides the checkout.
* Board 2: 402 Card declined, the answer the guest app gets.

**Second glance:**
* Board 1: Authorised, the reply that lets the booking API confirm the hold and answer 201.
* Board 2: Declined, the reply that makes the booking API release the hold.

**Last glance:**
* Board 1: Tell the partner hub, which comes after the confirmation.
* Board 2: Post the booking, the start both paths share.

**File:** the existing FigJam file `<draft-file-key>`. The boards land as new sections beside what it already holds, and nothing already there changes. Because the file exists, no plan is chosen and no new file is created. I can't see which plan the file sits in, so I'm relying on your word that it is Roamstay Product. If the file turns out not to be writable, I'll stop and ask before creating anything. Your fallback of a new file in the Barter team plan, in drafts and with no project, would need its own yes.

**Writes:**
* Board 1, "1. Checkout payment, card authorised": 4 participants and 7 numbered messages.
* Board 2, "2. Checkout payment, card declined": 3 participants and 6 numbered messages.

Each board has a title, a subtitle, a key and a source line, at the Laptop reading distance. Board 2 lands 400 pixels to the right of board 1, so you start at board 1.

**Extensions:** none.
**Calls:** `create_session`, one `get_figjam` read of the file before the write, two `use_figma` calls and one `get_figjam` read-back. That is up to 5 calls. A Starter plan or a View or Collab seat is limited to six tool calls a month, so this would use most of that allowance.
**Rollback:** delete the two board sections the writes return. That runs only on a reply that names them.

Write both boards into the file?