The model passes the pre-write check (6 entities, 6 relationships) and the composer builds it. No columns arrived, so I took my fallback: keys only, with key names that follow convention. Nothing is written yet. This is the plan for the write.

```mermaid
erDiagram
    %% title: Stays model
    %% subtitle: The six stay tables and the keys that join them, guest side apart from partner side
    %% source: Sources: the request and the Roamstay context note. Key names are conventions. Left out: every non-key column, until the schema note arrives.
    %% zone: Guest side: Guest, Booking, Payment
    %% zone: Partner side: Property, Room, RatePlan
    %% focus: Booking
    Guest ||--o{ Booking : makes
    Booking ||--o{ Payment : holds
    Room ||--o{ Booking : "is reserved by"
    RatePlan ||--o{ Booking : prices
    Property ||--o{ Room : offers
    Property ||--o{ RatePlan : publishes
    Guest { string id PK }
    Booking { string id PK, string guestId FK, string roomId FK, string ratePlanId FK }
    Payment { string id PK, string bookingId FK }
    Property { int id PK }
    Room { string id PK, int propertyId FK }
    RatePlan["Rate plan"] { string id PK, int propertyId FK }
```

(The block above is condensed to one line per entity. The checked model has one attribute per line.)

```text
Question: which stay tables exist, which keys join them and how many of each?
Outcome: a support or product reader sees the six tables, the key behind each join, and which tables sit on the guest side and which on the partner side.
First glance: Booking, the table every other stay table joins.
Second glance: the three foreign keys on Booking that tie it to the guest, the room and the rate plan.
Last glance: Property, the partner table that offers rooms and publishes rate plans.
File: <test-file-key>, the existing FigJam file. Plan: Roamstay Product, as you named it.
Writes: one composed board section, 6 entities and 6 relationships in two zones, with a title, a key and a source line, at laptop reading distance. It lands to the right of whatever the file already holds.
Extensions: none.
Calls: create_session, one use_figma and one get_figjam read-back.
Rollback: delete the one board section the write returns, only after you say yes to that deletion.
```

Assumed in this model:
- **Many sides:** I drew zero or more on the many side of every join, because the request gives no minimum. Booking to Payment is zero or more, as agreed.
- **Key types:** Property's id is an int because the Roamstay context calls it a numeric property ID. The other key types are placeholders, and the source line says key names are conventions.
- **Email-only guests:** the context says a guest can book with an email address only. Whether such a booking has a guest row isn't in the sources, so the board draws Guest to Booking as you stated it.

Write it?