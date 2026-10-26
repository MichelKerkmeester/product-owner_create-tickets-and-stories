The model passed the pre-write check: 6 entities, 6 relationships, 12 attributes. It composed with no design warnings. Nothing is written yet. This is the sketch the board will draw:

```mermaid
erDiagram
    %% zone: Guest side: Guest, Booking, Payment
    %% zone: Partner side: Property, Room, RatePlan
    Guest ||--o{ Booking : makes
    Booking ||--o{ Payment : holds
    Room ||--o{ Booking : "is reserved by"
    RatePlan ||--o{ Booking : prices
    Property ||--o{ Room : offers
    Property ||--o{ RatePlan : publishes
    Guest { key id PK }
    Booking { key id PK, key guestId FK, key roomId FK, key ratePlanId FK }
    Payment { key id PK, key bookingId FK }
    Property { key id PK }
    Room { key id PK, key propertyId FK }
    RatePlan["Rate Plan"] { key id PK, key propertyId FK }
```

Question: which stay tables exist, which keys join them and how many of each?
Outcome: a reader can see the six tables, the keys that tie them together and which tables sit on the guest side and which on the partner side.
First glance: Booking, the table the guest, the room, the rate plan and the payments all join.
Second glance: the three foreign keys on Booking, guestId, roomId and ratePlanId.
Last glance: Property, the partner table at the head of rooms and rate plans.
Assumed: you did not name the support columns, so the board holds keys only. The note's real key names and column types did not reach me, so key names follow the table names and every type reads `key`. Send the real names and I fix the model before anything is written.
File: the existing FigJam file with key <draft-file-key>, which takes the board as a new section beside what it holds. Nothing already on it changes. No new file is created, so the plan is not used and the Barter drafts fallback does not apply.
Writes: one composed board, 6 entities and 6 relationships in two zones, guest side and partner side, with a title, a key and a source line, at the Laptop reading distance.
Extensions: none.
Calls: create_session, one use_figma and one get_figjam read-back. A Starter plan or a View or Collab seat has 6 tool calls a month, and the read counts against that.
Rollback: delete the one board section the write returns. It runs only on your yes to a question that names it.

Write it?