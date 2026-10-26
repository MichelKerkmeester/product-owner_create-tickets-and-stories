The model passed the pre-write check (6 entities, 6 relationships) and composed, so this is the write gate. Nothing is on the board yet.

```mermaid
erDiagram
    %% title: Stays model
    %% subtitle: The six tables behind a stay, with the guest tables apart from the partner tables
    %% source: Source: your request, keys implied by the joins. Left out: the columns support asks about, not supplied.
    %% zone: Guest side: Guest, Booking, Payment
    %% zone: Partner side: Property, Room, RatePlan
    %% focus: Booking
    Guest ||--o{ Booking : makes
    Room ||--o{ Booking : "is reserved by"
    RatePlan ||--o{ Booking : prices
    Booking ||--o{ Payment : holds
    Property ||--|{ Room : offers
    Property ||--|{ RatePlan : publishes
    Guest { key id PK }
    Booking { key id PK, key guestId FK, key roomId FK, key ratePlanId FK }
    Payment { key id PK, key bookingId FK }
    Property { key id PK }
    Room { key id PK, key propertyId FK }
    RatePlan["Rate Plan"] { key id PK, key propertyId FK }
```

**Question:** which entities exist, which keys join them and how many of each?

**Outcome:** a reader can see the six stay tables, how they join and which tables sit on the guest side or the partner side.

**First glance:** Booking, the table every other stay table joins. It carries the pink accent.

**Second glance:** the three foreign keys on Booking that tie it to the guest, the room and the rate plan.

**Last glance:** Property, the partner table that offers rooms and publishes rate plans.

**File:** `<draft-file-key>`, the existing FigJam file you named. The board goes in as a new section, and the file is empty, so nothing already there changes. This needs no plan and no new file, so the Roamstay Product and Barter plans don't come into it.

**Writes:**
- One composed board with 6 entities, 6 relationships and 12 key lines, in two zones: guest side and partner side.
- A title, a key and a source line.
- Drawn at laptop reading distance.
- Key lines use the neutral type word `key`, because no source gives column types.
- The columns support asks about are not drawn, so the board's source line says so.

**Extensions:** none.

**Calls:** one `use_figma` to compose the board and one `get_figjam` to read it back. The read of the empty file is already spent. If the file's plan is Starter, or you have a View or Collab seat, Figma allows six tool calls a month, and read tools count against it.

**Rollback:** delete the one board section the write returns. That removes everything drawn in it and leaves the rest of the file alone. I'd only do that after a second question that names the board.

Write it?