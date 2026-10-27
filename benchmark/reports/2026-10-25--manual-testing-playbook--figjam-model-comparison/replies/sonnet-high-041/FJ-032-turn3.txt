The model passed the pre-write check and composed into a single `use_figma` call. Nothing has been written to the board.

**Question:** which statuses does a Roamstay booking have, and what moves it between them?

**Outcome:** the retro team can say what each status means and which statuses end a booking.

**First glance:** Confirmed, the composite section around Upcoming and In stay. It is the largest tinted shape, so the eye lands there first.

**Second glance:** Pending, the first state, drawn light blue where every booking starts.

**Last glance:** the three end states (Completed, Cancelled and No-show) in light gray with heavy outlines, and the source line. They stay readable without competing.

**File:** `<draft-file-key>`, the existing retro board. It needs no plan or new file, because the board goes in as a new section beside "Sprint retro".

**Writes:** one composed board section titled "Booking status". It holds 7 states and 12 transitions, with a title, a subtitle, a key and a source line, at laptop reading distance. It lands to the right of "Sprint retro", clear of it. Nothing already on the board changes, and no section there shares this title.

**Extensions:** none.

**Calls:** one `use_figma`, one `get_figjam` read-back, and one more `get_figjam` read of the file. That last read compares "Sprint retro" with the read I took earlier, so I can confirm it was left as it was. Figma limits a Starter plan and a View or Collab seat to six tool calls a month, and the session and board reads so far count toward that.

**Rollback:** delete the one "Booking status" section the write returns. I'd do that only after you say yes to a question that names it.

Shall I write it to the board?