The model passes the pre-write check and the composer has built the board. This is the write gate.

**Question:** which statuses exist and what moves a booking between them?
**Outcome:** the retro board's readers can see every booking status and what moves a booking between them.

**First glance:** In stay. It changed from Confirmed, which I proposed earlier. The composer can only mark a plain state, not a section like Confirmed, so the accent goes on the state that sits behind two of the guards. Say so if you'd rather mark another state.
**Second glance:** the exits out of Confirmed, which are check-out, guest cancels and missed check-in.
**Last glance:** Pending, where every booking starts.

**File:** `<test-file-key>`, your existing retro board. I'm not creating a new file, and you haven't told me which plan owns it.

**Writes:**

*   One new board section titled "Booking status", with 7 states and 12 transitions (6 of them labelled events, plus 6 start and end arrows).
*   Confirmed is a section holding Upcoming and In stay, and the end states are drawn in light gray.
*   The board has a title, a subtitle, a key and a source line, at laptop reading distance.
*   It lands 400 px to the right of everything already on the page. Nothing already on the board is moved, edited or deleted.

**Left out:** payment failure, expiry on Pending and refunds, because your message states none of them.
**Extensions:** none.
**Calls:** `create_session`, one `get_figjam` read of the board before the write, one `use_figma` and one `get_figjam` read-back. That is 4 calls, and one more if a node needs `get_screenshot`. Figma limits a Starter plan or a View or Collab seat to 6 tool calls a month, and read calls count against that.
**Rollback:** delete the one board section the write returns. I'd do that only after a separate yes naming it.

Write it?