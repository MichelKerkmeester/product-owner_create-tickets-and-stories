The reading is settled: ER diagram, Guest Support as the reader, and the guest zone and partner zone as I described them. I'm assuming your yes also accepts my answers on the minimum side of the joins. Booking to Payment and Property to Room and Rate Plan are all one to zero-or-more.

I still don't have the schema note, so I haven't built the model. The note has the key and column names, and I won't invent them.

Which of these do you want?

* **Send the note.** Paste it, or list the columns support asks about for each table. I'll keep the primary and foreign keys plus those columns. This is my recommendation.
* **Keys only.** I draw each table with an `id` primary key and the foreign keys the joins imply, such as `guestId`, `roomId` and `ratePlanId` on Booking. The column names are marked assumed, and the board carries no support columns.

If you send neither, I'll take keys only. The next reply is the write gate, which names the file, what gets written and the rollback. It also lists the key names I assumed, so you can correct them before anything is drawn.