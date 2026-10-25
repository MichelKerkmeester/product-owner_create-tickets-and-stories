The pre-write check passed: 7 states and 12 transitions. The composer built the board code, so this is the write gate.

**Question:** which statuses can a Roamstay booking have, and what moves it between them?
**Outcome:** a reader can see every booking status and the event behind each move.
**First glance:** the end states Completed, Cancelled and No-show, drawn in light gray.
**Second glance:** the events leading into them: check out, guest cancels and missed check-in.
**Last glance:** Pending, where every booking starts.

**File:** your existing board `<test-file-key>`. You didn't name its plan, so I'm not stating one.
**Writes:**
- One new board section titled "Booking status lifecycle", with 7 states and 12 transitions, a title, a key and a source line. It lands to the right of everything already on the page, at the Laptop reading distance.
- It is a third copy of a lifecycle the board already draws twice. I gave it a different title so it can't be confused with the two "Booking status" sections.
- Check-in as the trigger from Upcoming to In stay is still my assumption.

**Extensions:** none.
**Calls:** one `use_figma` and one `get_figjam` read-back. On a Starter plan, or with a View or Collab seat, Figma allows six tool calls a month, and the reads I've already made count against that.
**Rollback:** delete the one new section, only after you say yes to the deletion. Nothing existing is touched.

Write it?