I've built and checked the model and composed the board code, and I read your file once. Next I need your yes to write.

The check passed with 7 states and 12 transitions. The composer produced 12 nodes and 12 connectors to read back. Your file holds nothing yet, so there is no same-titled section to clash with. The check couldn't trace label wrapping because Node failed to load a library here. I read the labels by hand and none is long.

**Question:** which statuses does a Roamstay booking pass through, and which of them end it?
**Outcome:** support can read every booking status and spot the three that end a booking.
**First glance:** Cancelled, marked with the pink outline by the focus line, because two moves reach it.
**Second glance:** Pending, the light blue first state where every booking starts. Then Upcoming and In stay, read with the Confirmed section around them.
**Last glance:** Completed and No-show, the other two end states. Each is light gray with a heavy outline, like Cancelled.
**Plan and file:** Roamstay Product, file `<draft-file-key>`. The board lands as a new section in that file and nothing already there changes. I'm not creating a new file.
**Writes:** one composed board titled "Booking status", with 7 states and 12 transitions, a key and a source line, at the Laptop reading distance. Cancel is drawn as written, so it leaves the whole Confirmed section, In stay included.
**Left out:** what happens to a Pending booking whose card is never authorised, because the request is silent.
**Extensions:** none.
**Calls:** one `use_figma` call and one `get_figjam` read-back, which are the two calls left. I already spent a session call and one read. Read tools count toward the monthly cap on a Starter plan or a View or Collab seat.
**Rollback:** delete the one new board section the write returns, through `use_figma`, and only on its own yes. You can also remove it by hand in FigJam.

Write it?