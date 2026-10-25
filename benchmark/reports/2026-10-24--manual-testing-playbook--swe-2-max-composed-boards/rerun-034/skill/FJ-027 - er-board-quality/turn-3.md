The model passes the pre-write check (6 entities, 6 relationships, 12 attributes) and composes into one `use_figma` call. This is the write gate. Nothing has been written yet.

**Question:** which entities exist, which keys join them and how many of each?
**Outcome:** a Guest Support agent can see the six stay tables, how they join and which sit on the guest side and which on the partner side.
**First glance:** Booking, the table every other stay table joins.
**Second glance:** the foreign keys on Booking that tie it to the guest, the room and the rate plan.
**Last glance:** Property, the partner table that offers rooms and publishes rate plans.
**Plan and file:** Roamstay Product, as you named it. The write goes into the existing file `<test-file-key>`, so there is no `create_new_file`. I haven't confirmed the file sits in that plan.
**Writes:** one board section titled "Stays model", landing 400 pixels right of whatever the file already holds. It has:
* 6 entities and 6 relationships in two zones, guest side (Guest, Booking, Payment) and partner side (Property, Room, Rate Plan)
* a title, a key and a source line, at Laptop reading distance
* a solid line for each relationship, with its cardinality in the label

**Assumed on the board:**
* Every table has an `id` primary key.
* The foreign keys are `guestId`, `roomId` and `ratePlanId` on Booking, `bookingId` on Payment, and `propertyId` on Room and Rate Plan.
* Each key is typed `uuid`.
* A booking always has a guest, one room and one rate plan.
* A property may have no rooms or rate plans yet.
* A booking may have no payments.

The source line says the key names are assumed. **Left out:** every column beyond the keys, since no schema note was supplied.
**Extensions:** none.
**Calls:** `create_session` for the file, one `use_figma` and one `get_figjam` read-back. If the file is on a Starter plan or you have a View or Collab seat, Figma allows six tool calls a month and read tools count. This write would spend three of them.
**Rollback:** delete the one board section the write returns. That deletion waits for its own yes from you.

Write it?