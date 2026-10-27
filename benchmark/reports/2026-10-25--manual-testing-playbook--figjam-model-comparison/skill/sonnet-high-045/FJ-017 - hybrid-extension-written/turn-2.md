The check passed (7 states, 12 transitions) and the board code is composed. Nothing has been written to Figma yet.

**Question:** which statuses can a Roamstay booking have, what moves it between them, and who sets Cancelled and No-show?
**Outcome:** support can read every booking status and know whether to ask the guest or the hotel about a Cancelled or No-show booking.
**First glance:** Pending, the light blue first state where every booking starts.
**Second glance:** Upcoming and In stay, the states inside Confirmed, read with the section that frames them.
**Last glance:** Cancelled, marked with the pink focus outline where it is drawn. Then Completed and No-show, the other end states, each in light gray.

**Plan:** <figma-plan-1>, the Pro plan on this account (`team::<plan-id>`). It is the only Barter plan `whoami` returns. The account has no plan named Roamstay Product, so I took your correction as the instruction.
**File:** a new FigJam file named "Booking status", created in that plan's drafts with no project.
**Writes:** one composed board with 7 states and 12 transitions, a title, a key and a source line, at the Laptop reading distance. Detail is balanced and the audience is mixed.
**Extensions:** 2 single stickies, placed 64 pixels clear of their states, to the right first:
* On Cancelled: "Set by the guest, while the booking is Pending or Confirmed"
* On No-show: "Set by the hotel after a missed check-in"

If the two end states sit too close for both stickies to stand level, the second goes below or to the left of its state, and I'll report that on a `Finding:` line.
**Left out:**
* A Pending booking whose card is never authorised, because you didn't say
* Any cancel by the hotel or the system, for the same reason

Both appear in the board's source line and in the reply.
**Calls:** `create_new_file`, `create_session`, one `use_figma` to compose the board, one `use_figma` for the two stickies and one `get_figjam` read-back.
**Rollback:** delete the new file. If you only want the notes gone, I delete the two sticky ids the extension returns, after your yes to that deletion.

Write it?