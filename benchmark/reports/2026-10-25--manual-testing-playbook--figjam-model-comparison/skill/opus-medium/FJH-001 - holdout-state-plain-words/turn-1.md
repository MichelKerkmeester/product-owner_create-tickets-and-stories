No board has been written yet. Your request doesn't include the list of statuses or what triggers each change. The FigJam rules don't let me guess those, so this is the first round of questions. Each one has my recommended answer, so you can just say "go with your recommendations" where that fits.

**Diagram type:** a state diagram. It shows each status as a box and labels each arrow with the event that moves an order to the next status.

**Target:** the existing file `<test-file-key>`. The new board goes to the right of anything already in the file, so nothing there gets covered. I'll ask for a separate yes before writing anything.

**1. Who reads it, and what do they do with it**
- **What I can tell:** the request doesn't say.
- **Recommended:** the product team and engineers. After reading, they can agree the full list of order statuses and spot any status change that has no trigger.
- **Why:** that tells me how much detail to draw (product names for statuses, not system codes).

**2. Where the statuses come from**
- **What I can tell:** nothing you've sent names Barter's order statuses or what triggers them. The only order statuses in this workspace are in `context/fernhouse-order-tracking-pm-brief.md`. That's sample material for a fictional shop with parcel tracking, so it's probably not Barter's.
- **Question:** can you send or point me to the source? A spec, a schema or enum, a ticket or a plain list would all work.
- **Recommended:** a plain list in this shape: `status A → status B, when <event>`. Add any rule that blocks a change, for example "only before shipping".
- **Why:** each box and arrow needs a source. Without one, the board would describe a system nobody has confirmed.

**3. What the board should leave out**
- **What I can tell:** the request covers statuses and what moves an order between them, nothing else.
- **Recommended:** no screens, no notifications and no system internals. Refunds and returns stay out unless they change the order's status.
- **Why:** a state diagram stays readable at about 9 statuses. Anything extra would go in a second board.

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.