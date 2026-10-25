The check passed and the board composed. The reading is settled, so this is the write gate. Nothing has been written yet.

**Question:** which statuses can a Roamstay booking have, and what moves it between them?
**Outcome:** support can read every booking status and spot the ones a booking ends in.
**First glance:** the three end states, Completed, Cancelled and No-show, in light gray.
**Second glance:** the events that lead into them: check out, guest cancels and missed check-in.
**Last glance:** Pending, where every booking starts.

**Plan and file:** the existing FigJam file `<test-file-key>`, which you said sits in the Roamstay Product plan. I haven't verified the plan.
**Writes:** one new board section named "Booking status", with 7 states, 12 transitions (6 of them labelled) and a title, subtitle, key and source line. The Laptop reading distance is the default. Confirmed is a composite around Upcoming and In stay. The three end states are light gray, as the composer draws them. The board lands 400 pixels to the right of the file's existing content.
**Extensions:** none.
**Left out:** Pending expiry after 30 minutes, named in the board's source line.
**Calls:** `create_session` for the file, one `use_figma` call and one `get_figjam` read-back. A Starter plan or a View or Collab seat is limited to six tool calls a month, so tell me if that applies. I'd stop and report if the limit blocks the read-back, and I wouldn't call the board done without it.
**Rollback:** delete the one board section the write returns. I'd do that only after you say yes to the deletion, and the file itself stays.

Write the board into that file?