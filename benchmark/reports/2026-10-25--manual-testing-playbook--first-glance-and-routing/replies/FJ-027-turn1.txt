I've written nothing to the board. The file already has a "Stays model" board with the same six tables, and the columns you want aren't in anything I was given.

I made one read of the file, which turned up a section named "Stays model" with a "Guest side" zone and a "Partner side" zone. It holds the six tables with keys only. Its source line says "Key names are assumed, no schema note was supplied". The schema note you mention isn't in the repo or on the board.

**How I read the request**
* **Reader and question:** Guest Support asks which stay tables exist, which keys join them and how many of each. This is an ER diagram.
* **Outcome:** a reader can see the six tables, how they join, which tables are guest side and which are partner side, and the columns support asks about.
* **Target:** a new board section inside file `<test-file-key>`. No new file is created, so the file's own plan applies. You named Roamstay Product, and I haven't checked that the file belongs to it.
* **Relationships from your list:**
  * A guest makes bookings (1 to 0..n).
  * A booking reserves one room (a room has 0..n bookings).
  * A booking has one rate plan (a rate plan has 0..n bookings).
  * A property offers rooms (1 to 0..n).
  * A property publishes rate plans (1 to 0..n).
  * I assumed the 0..n minimums where you gave no minimum.
* **Grouping:** the two zones above, with guests, bookings and payments on the guest side. Rooms, rate plans and properties go on the partner side.

**Questions**
1. **Columns.** Which columns does support ask about, and what are the key names? Please paste the schema note or list them. Recommended: if you send nothing, I draw keys only and name the columns as a gap. I won't invent column names, and the keys-only board would repeat the one already in the file.
2. **The existing "Stays model" board.** Do you want it replaced or kept? Recommended: replace it. I'd compose the new board first and read it back. Deleting the old section would then need its own yes, and until then both boards would stay in the file.
3. **Payments per booking.** Should a booking hold 0..n payments or 1..n? Recommended: 0..n. The Roamstay context says a Pay at property booking confirms at once with only a card stored, so it can have no payment.

I'll send the write gate after your answers. It will name the file, the calls and the rollback.