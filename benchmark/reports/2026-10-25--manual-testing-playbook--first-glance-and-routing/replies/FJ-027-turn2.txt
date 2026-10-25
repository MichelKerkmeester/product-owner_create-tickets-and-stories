The model passes the pre-write check and composes. Nothing is written yet.

**Check results**
* The ER check passed with 6 entities and 6 relationships.
* The composer produced the board code at 45,187 characters, which fits one `use_figma` call.
* The check counted 12 attributes, all keys.

**Choices that follow your answers**
* **Columns:** keys only. Support's columns aren't supplied, so the source line on the board says so, and I'm not inventing any.
* **Key names:** `id`, `guestId`, `roomId`, `ratePlanId`, `propertyId` and `bookingId`. These are assumed, and the source line says that too.
* **Payments:** a booking holds 0..n payments.
* **Cardinalities:** a guest makes 0..n bookings. A booking reserves one room and is booked under one rate plan, so a room or a rate plan has 0..n bookings. A property offers 0..n rooms and publishes 0..n rate plans.
* **Lines:** the guest-booking, booking-payment, property-room and property-rate-plan links are solid. The booking-to-room and booking-to-rate-plan links are dashed, and the key explains both.
* **Reading distance:** Laptop, with balanced detail.

**Gate**
* **Question:** which stay tables exist, which keys join them and how many of each?
* **Outcome:** Guest Support can see the six tables, how they join and which side of the model each sits on.
* **First glance:** Booking, the table that joins the guest, the room and the rate plan.
* **Second glance:** the `guestId`, `roomId` and `ratePlanId` keys on Booking.
* **Last glance:** Property, the partner table that offers rooms and rate plans.
* **File:** `<test-file-key>`, an existing file. I add one new board section to it and create no new file. You named the Roamstay Product plan, and I haven't verified that this file belongs to it.
* **Writes:** one composed board titled "Stays model", with 6 entities and 6 relationships in two zones, guest side and partner side, plus a title, subtitle, key and source line.
* **Extensions:** none.
* **Calls:** one `use_figma` to compose and one `get_figjam` to read it back. If the file's plan is Starter, or you have a View or Collab seat, the earlier read of the whole file already used one of that month's six calls.
* **The old board:** it has the same title, so I'll compose the new board beside it first and read it back. Deleting the old "Stays model" section is a separate question that waits for its own yes, and until then both boards stay.
* **Rollback:** delete the new board section by the id the write returns, only after you say yes to that deletion.

Write it?