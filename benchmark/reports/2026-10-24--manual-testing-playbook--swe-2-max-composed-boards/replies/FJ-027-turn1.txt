Model passes the pre-write check and composes in one call. Here is the playback and the write gate before anything lands on the board.

**Playback**

*   Question the board answers: which tables hold a Roamstay stay, which fields join them and how do they relate
*   Outcome: a reader can trace one booking to its guest, room, rate plan, property and payments — assumed, settle it by naming who reads the board
*   Reader: assumed Guest Support agents and the Booking or Partner squads, since the request asks for the columns support cites
*   Scope: captured — the six stays tables with keys plus the support columns, the schema note's other columns left out
*   Entities, relationships and cardinalities: captured from the schema note as you quoted it, class current behavior
*   Kept columns: assumed reading of "the few columns support asks about" — Booking reference, checkIn, checkOut, status; Payment amount, status; Guest email, country; Property name, city; Room name, capacity; Rate Plan refundable, paymentOption. Settle it by naming the exact set support cites
*   Dials: Balanced detail, Mixed audience, Laptop distance — defaults, not stated in the request

**Framing.** Recommended: one board, two tinted zones — Guest side (Guest, Booking, Payment) and Partner side (Property, Room, Rate Plan). Six entities fit one board and the booking-to-room and rate-plan join is the point. The alternative, two diagrams split by domain, repeats Booking on both and splits the join that matters.

**Glance lines**

1.  First glance: Booking — every relationship on the board meets there
2.  Second glance: the two zones, which side owns which table
3.  Last glance: the attribute lines and the key

**Gate**

*   Plan: Roamstay Product as named. The account's plan list shows <figma-plan-3>, <figma-plan-1> and <figma-plan-2>; the write lands in the existing file whichever plan holds it
*   File: existing FigJam file `<test-file-key>` (confirmed a FigJam file)
*   Writes: one composed board titled Stays model — 6 entity cards, 6 relationships with cardinality labels, 26 attributes, 2 zones, title, subtitle, key and source line. It lands 400 pixels right of existing content
*   Extensions: none
*   Check: `flow_check.py` PASSED — 6 entities, 6 relationships; composes in one `use_figma` call
*   Calls still to spend: one `use_figma`, one `get_figjam` read-back
*   Rollback: delete the one board section the write returns, through `use_figma`, only after a yes to the deletion

Write it?