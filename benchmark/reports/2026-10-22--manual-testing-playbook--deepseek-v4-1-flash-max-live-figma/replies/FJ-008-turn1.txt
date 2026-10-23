For product and engineering to agree the stays model before build: one ER diagram of six tables, keys only, answering which tables exist, which keys join them and how many of each.

Keys here means primary and foreign keys, not every unique column.

| Table | Keys |
|---|---|
| Guest | id PK |
| Booking | id PK, guestId FK, roomId FK, ratePlanId FK |
| Payment | id PK, bookingId FK |
| Property | id PK |
| Room | id PK, propertyId FK |
| Rate Plan | id PK, propertyId FK |

Guest makes bookings, a booking holds payments, a room is reserved by bookings, a rate plan prices bookings, and a property offers rooms and publishes rate plans. The six relationships are yours. The key columns are read off them.

Two readings to confirm:

- `uuid id` is the primary key on every table, with foreign keys named after the parent (`guestId`, `roomId`, `ratePlanId`, `bookingId`, `propertyId`). If the schema uses bigint or prefixed references, say which
- Booking to Payment is one or more payments per booking, so a pay-at-property booking with no payment row would need zero or more. Property to Room and Property to Rate Plan are one or more each

The plan is the one blocker. No plan named Roamstay Product is in the plans this Figma connection can see. The three it can see are <figma-plan-1> (pro, Full seat, admin), <figma-plan-2> (pro, member seat) and <figma-plan-3> (starter, View seat, six tool calls a month). I recommend <figma-plan-1> If Roamstay Product is a project folder rather than a plan, name the plan that holds it, because the diagram tool takes a plan and cannot target a project folder.

**What I'll write**

- File: a new FigJam file, created by the write
- Diagram: ER, named "Stays model", 6 tables, 6 relationships, 12 key columns
- Dials: simplified detail, mixed audience, laptop distance
- Extensions: none
- Read: one `get_figjam` read-back with a screenshot
- Rollback: delete the new file
- Glance: first the Booking table where four relationships meet, second the Property split into rooms and rate plans, last the key column on each table

Reply `<figma-plan-1>, yes` to write it, or name the plan you meant.