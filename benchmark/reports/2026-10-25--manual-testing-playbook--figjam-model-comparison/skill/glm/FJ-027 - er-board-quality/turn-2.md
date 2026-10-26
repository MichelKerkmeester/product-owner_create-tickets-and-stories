COMPOSED with no design warnings: 6 entities, 6 relationships, 49,043 characters, inside the one-call limit. The rubric walk holds (every entity and edge is stated by the request, the three glance lines are written, provenance is all current behavior). The gate is its own reply, so this waits for your yes before anything is written.

**Question:** which entities exist, which fields join them and how many of each?
**Outcome:** a reader can see the six stay tables, how they join and which tables sit on the guest side and which on the partner side
**First glance:** Booking, the table every other stay table joins
**Second glance:** the keys on Booking that tie it to the guest, the room and the rate plan
**Last glance:** Property, the partner table that offers rooms and rate plans
**Plan:** Roamstay Product, the plan you named. **File:** the existing FigJam file with key `<test-file-key>`, not a new file
**Writes:** one composed board, 6 entities and 6 relationships in two zones, guest side and partner side, 26 attributes, with a title, a subtitle, a key and a source line, at the Laptop reading distance. It lands beside what the file already holds, 400 pixels to the right of it
**Extensions:** none
**Calls:** create_session, one `get_figjam` read of the file before the write, one `use_figma` compose and one `get_figjam` read-back
**Rollback:** delete the one board section the write returns, only on its own yes

The sketch, the checked model:

```mermaid
erDiagram
    %% title: Stays model
    %% subtitle: The tables behind a stay, split into the guest side and the partner side
    %% source: Sources: the stays schema note and support ticket 58213. Left out: the schema note's other columns.
    %% zone: Guest side: Guest, Booking, Payment
    %% zone: Partner side: Property, Room, RatePlan
    Guest ||--o{ Booking : makes
    Booking ||--|{ Payment : holds
    Room ||--o{ Booking : "is reserved by"
    RatePlan ||--o{ Booking : prices
    Property ||--|{ Room : offers
    Property ||--|{ RatePlan : publishes
    Guest {
        uuid id PK
        string email UK
    }
    Booking {
        uuid id PK
        uuid guestId FK
        uuid roomId FK
        uuid ratePlanId FK
        string reference UK
        date checkIn
        date checkOut
        int adults
        decimal total
        string status
    }
    Payment {
        uuid id PK
        uuid bookingId FK
        decimal amount
        date capturedAt
    }
    Property {
        uuid id PK
        decimal cityTax "per adult per night or per stay"
    }
    Room {
        uuid id PK
        uuid propertyId FK
        int capacity
    }
    RatePlan["Rate Plan"] {
        uuid id PK
        uuid propertyId FK
        decimal pricePerNight
        string paymentOption "Pay now | Pay at property"
        bool refundable
    }
```

Write it?