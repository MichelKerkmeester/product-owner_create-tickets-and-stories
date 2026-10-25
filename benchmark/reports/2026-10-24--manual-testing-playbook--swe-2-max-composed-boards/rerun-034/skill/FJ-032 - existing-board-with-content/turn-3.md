Both checks pass: 7 states and 12 transitions. I haven't written anything yet. This is the write question, and I'm reading your "go ahead" as the replace option.

**Question:** which statuses exist and what moves a booking between them?
**Outcome:** support can read every booking status, spot the statuses a booking ends in and see who sets Cancelled and No-show.
**First glance:** the end states, Completed, Cancelled and No-show, drawn in light gray.
**Second glance:** the events that lead into them: check out, guest cancels and hotel marks after a missed check-in.
**Last glance:** Pending, where every booking starts.
**File:** the existing retro board `<test-file-key>`, one new section titled "Booking status", placed 400 pixels to the right of the last content on the page. I haven't been given the board's plan, so I'm not naming one.
**Writes:** one composed section with a title, a key and a source line, at the Laptop reading distance. It has 7 states and 12 transitions, and the states read "In stay" and "No-show" as you wrote them.
**Extensions:** none.
**Calls:** Figma's `figma-use` and `figma-use-figjam` guidance, one `use_figma` and one `get_figjam` read-back.
**Rollback:** delete the new section I create, through `use_figma`, only on your yes.
**The old section:** section `62:66` stays untouched. After the read-back I'll ask separately whether to delete it, and it stays unless you say yes to that.

**Assumed:**
* The "check in" label on Upcoming to In stay isn't in your request. I took it from the existing board.
* No-show is reached from Confirmed, as on the existing board.

If you'd rather have a second copy beside the old section, say so and the delete question drops away. The write itself is the same.

Do you want me to write it?