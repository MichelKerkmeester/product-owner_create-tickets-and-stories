Nothing is written yet. This is the write gate, and it asks about the write alone.

**Purpose:** the board answers "what does a Roamstay guest see and pay at each outcome of changing their booking dates?" The first glance is `New price?` and its three exits.

**Target:** the existing FigJam file `<test-file-key>`, with no new file. The plan is Roamstay Product as you gave it. I haven't checked that this plan owns the file, because `whoami` only lists the plans your account belongs to.

**What will be written:** one board section titled `Change booking dates`, with 9 nodes, 11 connectors, 5 labelled decision exits and the 2 zones `Find a room` and `Settle the price`. The board also gets its subtitle, a key and the source line from the look pass. It lands 400 pixels to the right of everything already on the page, so it covers nothing there. The composed code passed the pre-write check and is 44,866 characters, under the 50,000 limit of one call. I'm planning no extensions.

**Settings it draws at:** balanced detail, a mixed audience and laptop reading distance.

**Calls it will spend (3):**

1. `create_session` on the file key
2. One `use_figma` call that composes the board
3. One `get_figjam` call that reads it back

If the file's owner has you on a Starter plan or a View or Collab seat, Figma allows only six tool calls a month. Read tools count against it, so this write would use 3 of the 6.

**Rollback:** the file isn't new, so nothing is deleted at file level. To undo the write I'd delete the one board section the write returns, through `use_figma`, and only after you say yes to that deletion separately. The board also carries a small tag under the `productowner` namespace holding its title, the write time and its counts, which a later session uses to find it.

Do you say yes to writing this board to `<test-file-key>` with these 3 calls? I recommend yes. The model passed the check, the composed code fits one call, and a wrong result is undone by deleting one section after your separate yes.