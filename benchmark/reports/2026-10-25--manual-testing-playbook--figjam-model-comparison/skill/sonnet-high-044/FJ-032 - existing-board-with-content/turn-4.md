The model passed the pre-write check as a state diagram with 7 states and 12 transitions, and it composed cleanly into a board of 12 nodes and 12 connectors. The tool that traces label wrapping couldn't run on this machine. I read the labels by hand instead, and the longest, "missed check-in [from Upcoming]", is 31 characters, so I don't expect a single word alone on a last line.

**Question:** which statuses can a Roamstay booking have, and what moves it between them?
**Outcome:** the product, engineering and support team agree every status and its exits before the next story is written.
**First glance:** Pending, the light blue start state, since your request names no state to stress.
**Second glance:** Upcoming and In stay, the states inside Confirmed, read with the Confirmed section that frames them.
**Last glance:** Completed, Cancelled and No-show, the end states.
**File:** your existing FigJam file <draft-file-key>. The write adds a new section named "Booking status" about 400 pixels to the right of Sprint retro. Sprint retro and its six stickies are not touched.
**Writes:** one composed board with a title, subtitle, key and source line, at the laptop reading distance, with detail balanced and the audience mixed.
**Extensions:** none.
**Left out:**
* Declined-card and expiry paths, which you asked me to keep off the board.
* A cancel guard for the stay. The board shows a guest cancelling from Confirmed, including during In stay, as you stated.

**Calls:**
* One `use_figma` to compose the board.
* One `get_figjam` to read it back.
* One more `get_figjam` to confirm Sprint retro is unchanged.
* No `whoami` and no `create_new_file`, since the file already exists.
* The two reads I already spent count toward Figma's six-call monthly allowance if your account is on a Starter plan or has a View or Collab seat.

**Rollback:** I delete the one new "Booking status" section, only after a reply that names it.

Do you want me to write this board to the file?