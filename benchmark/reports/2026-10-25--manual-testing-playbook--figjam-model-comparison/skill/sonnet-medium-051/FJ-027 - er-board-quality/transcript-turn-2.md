# FJ-027 turn 2 transcript

**User:** Use your recommended answers.

**Assistant:**

Before I draw anything, this is how I read the request.

Question: which entities exist, which fields join them and how many of each?
Outcome: the support team can see the six stay tables, how they join and which tables sit on the guest side and which on the partner side.
Detail level, audience and distance: balanced, mixed and laptop. All three are defaults.

Settled by the sources:
* **Entities:** your message gives six: Guest, Booking, Payment, Property, Room and Rate Plan.
* **Relationships:**
  * A guest makes bookings.
  * A booking reserves one room under one rate plan.
  * A booking holds its payments.
  * A property offers rooms and publishes rate plans.
* **Target:** the existing FigJam file `<test-file-key>` in Roamstay Product, as a new section beside what it already holds.

Assumed, with what would settle each:
* **Reader:** the support team. Settled by you naming the actual reader.
* **Scope:** this row covers three assumptions. Settled by the schema note or your correction.
  * Each table keeps keys only: a `PK` on every table and an `FK` on each join column, so Booking carries three `FK`s and Payment, Room and Rate Plan one each.
  * The cardinalities read:
    * One guest to zero or more bookings.
    * One room to zero or more bookings.
    * One rate plan to zero or more bookings.
    * One booking to one or more payments.
    * One property to one or more rooms.
    * One property to one or more rate plans.
  * The zones are a guest side (Guest, Booking, Payment) and a partner side (Property, Room, Rate Plan).

Left out: the few columns support asks about, because the note that lists them is not in the workspace. A reader asking "which field joins these?" still gets every join key.

Still open: none beyond the two assumed rows.

Is this the right reading of the board?
