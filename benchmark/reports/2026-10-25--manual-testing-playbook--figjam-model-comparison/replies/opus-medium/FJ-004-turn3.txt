Your "yes" didn't write anything yet. My last message offered two options rather than asking whether to write, and the packet only writes on a yes to its write-gate question. I took your yes as choosing option 2, the test write of a shipped example. The example passes the check and composes on this machine, so here is the gate.

**Write gate**

- **The question the board answers:** how does a Fernhouse customer start a return in the app, from the order list to a confirmed return? This is the packet's sample content, used to confirm writing and reading back from the board works on your file. It isn't Barter material.
- **The node a reader should see first:** "Return confirmed", the one highlighted node. Next a reader should notice the two decisions, "Within 30 days?" and "Drop-off or pickup?". The "Contact support" exit can wait.
- **Target:** the existing FigJam file `<test-file-key>`, as you asked. I won't create a new file. Flow Mode normally writes only to a new file or to a board this work already made. I'm treating your instruction as permission to write here instead. The board will be placed 400 px to the right of whatever is already on the page, so it won't cover anything.
- **What gets written:** one framed board titled "Start a return", using the default design:
  - 9 nodes and 9 connectors, with 2 decisions (4 labelled exits)
  - 3 zones: Find the order, Request the return and Done
  - a key and a source line
  - the composed code is 48,803 characters, under the 50,000 limit for one `use_figma` call
- **Extensions:** none.
- **Figma calls (4):**
  - `create_session` on the file
  - one `get_figjam` read before the write, to record what's already there
  - one `use_figma` call to draw the board
  - one `get_figjam` read-back, to check the board against the model and confirm existing content is untouched
- **Rollback:** delete the one tagged board section this write creates. That deletion only happens on a separate yes that names it. Nothing that was already on the file gets deleted.

Should I write this board into `<test-file-key>`?