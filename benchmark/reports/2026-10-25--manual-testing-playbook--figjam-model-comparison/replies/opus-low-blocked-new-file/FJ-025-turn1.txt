Before anything goes on a board, here's how I've read the brief. Please confirm it or correct it.

**Question the board answers:** What happens between a guest tapping pay and getting an answer, when the card is accepted and when it's declined?
**Outcome:** A sequence diagram with one success path and one declined path, read top to bottom.

**From the payments brief:**
- Participants: Guest app, Booking API, Payment provider, Partner hub
- Guest app → Booking API: post the booking
- Booking API holds the room
- Booking API → Payment provider: authorise the card
- If the card is authorised: Booking API confirms the hold, notifies the Partner hub, and replies 201 to the Guest app
- If the card is declined: Booking API releases the hold and replies 402 to the Guest app

**Assumed (correct any of these):**
- "Holds the room" and "confirms the hold" happen inside the Booking API, so I'll draw them as notes on it, not as calls to a separate inventory service. The brief doesn't name one.
- Nothing is sent to the Partner hub on a decline.
- The Booking API waits for the Partner hub before replying 201. The brief only gives the order, not whether that call blocks.
- The first thing the reader should see is the declined path (402).

**On where it goes:** You asked for a new board, but you also gave the key of an existing file, <test-file-key>. I can only write to a new file or to a board this work created, and I can't add a page to an existing FigJam file. So I can't write into that file as asked. I'll set out the options when I ask you to approve the write.

Is this reading right, including the four assumptions?

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.