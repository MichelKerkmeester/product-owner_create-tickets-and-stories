I've drawn the model using your recommended answers. It passed the pre-write check and builds into one Figma call, but nothing has been written to Figma yet.

**What the board answers:** which entities hold a Roamstay stay and how they relate. With it, the product team and engineers can agree the stays data model before the build.

**What a reader sees, in order**
1. **First:** Booking, the entity at the centre that joins guest, room, rate plan and payment.
2. **Second:** the six relationships and their counts, each written in the line label, such as `makes (1 to 0..n)`.
3. **Last:** the key fields on each card and the source line, which says the keys and counts are assumed.

**The model**

```mermaid
erDiagram
    Guest ||--o{ Booking : makes
    Booking ||--o{ Payment : holds
    Room ||--o{ Booking : "is reserved by"
    RatePlan ||--o{ Booking : prices
    Property ||--o{ Room : offers
    Property ||--o{ RatePlan : publishes
    Guest { string id PK }
    Booking { string id PK; guestId FK; roomId FK; ratePlanId FK }
    Payment { string id PK; bookingId FK }
    Room { string id PK; propertyId FK }
    RatePlan["Rate Plan"] { string id PK; propertyId FK }
    Property { string id PK }
```

The block above is condensed. The checked file lists one field per line.

- **Check result:** passed, with 6 entities, 6 relationships and 12 key fields. It fits in one Figma call (48,839 of the 50,000 characters allowed).
- **Board text:** the title is "Roamstay stays model". The subtitle reads "Which entities hold a stay and how they relate, keys only". The source line reads "Request of 2026-10-26, keys and cardinality assumed".
- **Assumed:**
  - The reader is the product team and engineers.
  - Key names and counts follow my defaults: `id` keys, foreign keys as listed, and one to zero or more on every relationship as a solid line.

**The write plan**
- **File:** the existing file `<test-file-key>`. It keeps whatever plan it already belongs to, which Figma can't tell me.
- **What gets added:** one new board section, placed 400 px to the right of everything already in the file. Nothing already there is moved or deleted. No notes or stickies are added.
- **Figma calls:**
  1. `create_session` with the file key
  2. `get_figjam`, to confirm it's a FigJam file and record what's already there
  3. `use_figma`, which draws the board
  4. `get_figjam`, to read the board back and check it against the model
- **Starter-plan limit:** if the file sits in the Starter plan, these calls use most of its 6-call monthly allowance.
- **If the file can't take the board:** I stop and ask before making anything. If you then agree, I'd create "Roamstay stays model" as a new FigJam file in the <figma-plan-1> plan, in drafts with no project.
- **To undo:** delete the one board section this write creates. That happens only if you ask and name it.

Should I write this board into `<test-file-key>`?

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.