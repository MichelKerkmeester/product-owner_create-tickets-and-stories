The model passed the pre-write check and composed, so this is the write gate.

**Question:** which statuses does a booking pass through, what moves it between them, and who sets Cancelled and No-show?
**Outcome:** support can see where a booking ended up and who to ask about a cancellation or a no-show.
**First glance:** Cancelled and No-show, each with its note. Both are end states, so the board draws them in light gray.
**Second glance:** the events that lead into them, "guest cancels" and "missed check-in".
**Last glance:** Pending, where every booking starts, and Completed.
**Plan:** Roamstay Product, as you named it. I can't confirm from here which plan owns the file.
**File:** the existing FigJam file `<test-file-key>`. No new file is created.
**Writes:** one new board named "Booking status", with a title, a key and a source line, at the laptop reading distance. It has 7 states and 12 transitions, and the "check in" label is the assumed one. It lands 400 pixels to the right of whatever is already on the page, so nothing existing is covered or moved.
**Extensions:** 2 single stickies inside the board, one beside Cancelled and one beside No-show:
* Cancelled: "Set by the guest, while the booking is Pending or Confirmed"
* No-show: "Set by the hotel after a missed check-in"

**Calls:** `create_session`, two reads of Figma's `figma-use` and `figma-use-figjam` skills, one `use_figma` call for the board, one `use_figma` call for the two notes and one `get_figjam` read-back. That is 6 calls. If the file's seat is Starter or View/Collab, Figma limits it to six tool calls a month, so this would use the whole allowance.
**Rollback:** delete the one board section the write returns. The notes sit inside it, so they go with it. I'd only do this after you say yes to the deletion.

Write it?