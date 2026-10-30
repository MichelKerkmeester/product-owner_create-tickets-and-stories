# FJ-027 turn 2 transcript

**User:** Yes, that reading is right.

**Assistant:**

Here is the full reading before I draw anything.

**Question:** which tables make up the stays model, which keys join them, and which columns hold a booking's dates and status, a payment's amount and status, and a rate plan's price and cancellation rule?
**Outcome:** Guest Support agents can find where a booking keeps its dates and status, where a payment keeps its amount, status and provider reference, and how a payment traces back to a room and a rate plan.
**Dials:** Balanced detail, Mixed audience, Laptop distance.

**What the sources settled**
* Six tables: guests, bookings, payments, properties, rooms and rate plans
* Guest side: guests, bookings, payments. Partner side: properties, rooms, rate plans
* A guest makes bookings. A booking reserves one room under one rate plan and holds its payments. A property offers rooms and publishes rate plans
* Payment columns: amount, currency, status (authorised, captured or refunded) and provider reference
* Rate plan columns: name, nightly price and cancellation rule
* Booking columns: check-in date, check-out date and status

**Outline, in drawing order**
* Six entity cards: Guest, Booking, Payment on the guest side, Property, Room, RatePlan on the partner side
* Six relationships: Guest makes Booking, Booking holds Payment, Room is reserved by Booking, RatePlan prices Booking, Property offers Room, Property publishes RatePlan
* Guest, Property and Room carry keys only, because the note names no columns for them

**Two framings**
* Two zones, guest side and partner side, which is the grouping you asked for. Booking sits on the guest side but joins two partner tables
* Three zones with Booking alone in the middle, which shows the join point more clearly but splits the grouping you asked for
* I recommend two zones, because it is your grouping and the Booking card is where the eye lands anyway

**The look**
* First glance on Booking, because every other table joins it
* Title "Stays model", with a subtitle naming the guest side and the partner side
* A source line naming the schema note, with the unnamed columns listed as left out

**Assumed, and settled by your correction or by sight of the schema**
* Keys and cardinality: an `id` primary key on every table, the foreign keys the relationships imply, and a booking reserving exactly one room and one rate plan. The note states no minimum for payments per booking or rooms and rate plans per property, so those ends are zero or more. Column types are mine too, with amounts as integers in minor units, as the Roamstay context doc says services carry money
* Reader: Guest Support agents, accepted from my recommendation and not from a source

**Still open:** none.

Is this the right reading of the board?
