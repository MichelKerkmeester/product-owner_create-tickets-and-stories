Nothing is written yet. This is the write gate for the new section. The pre-write check passed (7 states, 12 transitions) and the board code composed.

- **Question:** which statuses does a Roamstay booking have, and what moves it between them?
- **Outcome:** the reader can see every status, what moves a booking on, and which statuses end it.
- **First glance:** Completed, the successful end of a stay.
- **Second glance:** the moves into Cancelled and No-show, "guest cancels" and "missed check-in".
- **Last glance:** the source line under the key.
- **Board:** the retro board, <test-file-key>. I haven't been told which plan owns it, so I'm not naming one.
- **Writes:** one new section, "Booking status lifecycle", at laptop reading distance. It has 7 states and 12 transitions, a key and a source line. Confirmed is a group around Upcoming and In stay. The source line reads "Left out: refunds, payment steps and any No-show window".
- **Placement:** it lands 400 pixels to the right of everything on the board, at the far right end. The two existing "Booking status" sections stay untouched. I gave the new one a different title so a later revision can tell the three apart.
- **Extensions:** none.
- **Calls:** one `use_figma` write and one `get_figjam` read-back. The session is already open. If the board's plan is a Starter plan, these count against its six-call monthly limit.
- **Rollback:** delete the new section by its returned id, and only on your separate yes.

Should I write this third "Booking status lifecycle" section to the board? Say no and the board stays as it is. My earlier recommendation still stands, because the existing two sections already show this lifecycle.