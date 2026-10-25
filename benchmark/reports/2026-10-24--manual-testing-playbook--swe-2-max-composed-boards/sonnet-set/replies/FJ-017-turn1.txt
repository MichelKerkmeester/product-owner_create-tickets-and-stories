The state model passes `flow_check.py`, and the composer built the board code. I haven't written to your file yet. This message is the playback and the write gate in one, so one yes covers both.

**Playback**
- **Reader and question:** Support asks which statuses a booking can have and who sets Cancelled and No-show.
- **Type:** State diagram. 7 statuses and 12 transitions, within budget.
- **Model:**
  - Pending moves to Confirmed on "card authorised".
  - Confirmed holds Upcoming and In stay, joined by "check in".
  - Confirmed moves to Completed on "check out".
  - Pending and Confirmed both move to Cancelled on "guest cancels".
  - Confirmed moves to No-show on "missed check-in".
  - Completed, Cancelled and No-show are the end states.
- **First glance:** Cancelled and No-show, each with its setter.
- **Second glance:** The moves into them.
- **Last glance:** The happy path from Pending to Completed.

**Assumed, correct me if wrong**
- **No-show label:** The board says "No-show" as `NoShow`, because the diagram syntax doesn't allow a hyphen in a state id. Your wording stays in the note.
- **Where No-show starts:** The diagram syntax can't leave one status inside Confirmed. "Missed check-in" therefore leaves Confirmed as a whole, and "guest cancels" does the same. The board won't show that a missed check-in can only happen in Upcoming.
- **Which plan:** The file key replaces a new board. I can't confirm from the key that this file sits in Roamstay Product, so the write goes to the file you named.

**Gate**
- **File:** `<test-file-key>`, an existing FigJam file. No `whoami` or `create_new_file`.
- **Board:** One composed board with a title, a key and a source line. The title is "Booking status", and the source line reads "Source: the request's lifecycle description. Left out: nothing."
- **Extension, two stickies inside the board:**
  - Beside Cancelled: "Set by the guest, while Pending or Confirmed".
  - Beside No-show: "Set by the hotel after a missed check-in".
- **Calls:** `create_session`, one `use_figma` to compose, one `use_figma` for the stickies and one `get_figjam` read-back. That is 4 calls, and a screenshot read adds one. A Starter plan or a View or Collab seat has 6 tool calls a month.
- **Rollback:** Delete the new board section, which holds both stickies. I'll only delete it after a separate yes, and nothing already in the file is touched.

Write it?