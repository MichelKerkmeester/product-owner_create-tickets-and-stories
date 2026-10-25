Both diagrams pass `flow_check.py`, and nothing is written yet. This is the playback and the write gate, and the write waits for your yes.

**What the board answers:** In what order do the guest app, the booking API, the payment provider and the partner hub exchange messages at checkout, on a good card and on a declined one? After reading it, the payments team can see when the room is held, when it is confirmed or released, and who is told.

**Plan and file:** Roamstay Product, as you named it. I write into the existing FigJam file `<test-file-key>` as new board sections. I do not call `create_new_file` or `whoami`, because the file already exists and its plan was set when it was made. I have not confirmed that the file sits in that plan.

**What gets written:** One path per diagram, so the decline gets its own board. Each board has a title, a subtitle, numbered messages, a key and a source line, and they sit side by side in reading order.
- Board 1, "1. Checkout payment, card authorised": 4 participants and 7 messages
  - `POST /bookings`
  - Hold the room
  - Authorise card
  - Authorised
  - Confirm the hold
  - Booking confirmed (to PartnerHub)
  - `201 Created`
- Board 2, "2. Checkout payment, card declined": 3 participants and 6 messages
  - `POST /bookings`
  - Hold the room
  - Authorise card
  - Declined
  - Release the hold
  - `402 Card declined`

**Glance lines:**
- First: the hold is placed before the card is authorised and only confirmed after it
- Second: the partner hub is told before the app gets its 201
- Last: the source line and the key

**Assumed (tell me if any is wrong):**
- The reader is the payments team, and the outcome is knowing when the hold is placed, confirmed or released. No source states either.
- The brief is current behavior, not a proposal. You quoted its steps in your message and I have no brief file, so I drew only what you quoted.
- The hub message is a plain call with no reply, because the brief gives none. If it is fire-and-forget, the arrow changes to an open head.
- You did not give these labels, so they are my wording: "Authorised", "Declined", "Booking confirmed", "201 Created" and "402 Card declined".
- Board 2 leaves out the partner hub, because the brief does not say it is told on a decline.
- The board is drawn for a laptop reading distance.

**Calls:** `create_session`, two `use_figma` calls (one per board) and `get_figjam` for the read-back. I load Figma's `figma-use` and `figma-use-figjam` skills first. On a Starter plan or a View or Collab seat, Figma allows six tool calls a month, and this plan uses about five of them.

**Extensions:** none.

**Rollback:** I delete the two board sections the write returns, after a separate yes from you. The file stays.

Write it? Reply "board 1 only" to skip the decline.