The model passes the check: 6 tables and 6 relationships, with each table showing only its keys. Nothing has been written to Figma yet. I need your OK on where the board goes first.

**The destination doesn't work as you asked, for two reasons:**
- **No Roamstay Product plan:** your Figma account belongs to three plans: <figma-plan-3> (Starter), <figma-plan-1> (Pro) and <figma-plan-2> (Pro). None of them is a Roamstay Product plan.
- **The existing file is off-limits:** Flow Mode only writes into a new board or a board this work created. `<test-file-key>` was made elsewhere, so I can't add to it.

That leaves your fallback: a new FigJam file in the **<figma-plan-1>** plan, kept in drafts with no project.

**Purpose:** show how the Roamstay stays tables relate, with partner tables kept apart from guest tables, so support can trace a booking to its guest, room, rate plan and payments.

**Reading order**
- **First glance:** `bookings`, the table that links both sides
- **Second glance:** the two groups, guests and payments on the left, properties, rooms and rate plans on the right
- **Can wait:** the individual key columns

**What gets written**
- One framed board titled "Roamstay stays model"
- A guest group: `guests`, `bookings`, `payments`
- A partner group: `properties`, `rooms`, `ratePlans`
- The 6 relationships, each with its label and cardinality
- Each table's primary and foreign keys
- A key explaining the symbols, and a source line
- No extras such as notes or pins

**Figma calls:** four. `create_new_file` makes the file, `create_session` opens it, one `use_figma` call draws the board and `get_figjam` reads it back to check it. Your Barter seat is Full, so the Starter plan's monthly call limit doesn't apply.

**Undoing it:** delete the new draft file. Nothing else changes.

Should I create the new file in <figma-plan-1> drafts and draw the board there?