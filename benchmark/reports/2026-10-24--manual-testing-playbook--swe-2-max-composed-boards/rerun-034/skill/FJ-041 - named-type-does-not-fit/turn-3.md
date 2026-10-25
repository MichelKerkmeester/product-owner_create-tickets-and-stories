The model passes the check and composes. The write is next, and it needs your yes.

**Question the board answers:** which states a Fernhouse return passes through from the order screen to its confirmation, and which customer action moves it between them.
**Outcome:** the product and design team can agree the states and events before stories are written.

**Outline, one line per state and transition**
1. Start, then Order open
2. Order open to Choosing a reason, on "tap Return an item"
3. Choosing a reason to Choosing refund or credit, on "pick a reason"
4. Choosing refund or credit to Confirmation shown, on "choose refund"
5. Choosing refund or credit to Confirmation shown, on "choose store credit"
6. Confirmation shown, then End

I named each state after what the customer is doing at that point and each transition after the tap that leaves it. A list would work for the straight stretch, but the two-way ending is the part a list shows worst.

**Glance lines**
- First glance: the four-state path from Order open to Confirmation shown
- Second glance: the two ways out of Choosing refund or credit, both landing on the same confirmation
- Last glance: the source line saying the board comes from your description and leaves out failure paths and the reason list

The board carries no accent colour. A state diagram takes no `style` line, and the composer colours the first state light blue and the final one light gray.

**Check results**
- `flow_check.py`: PASSED, 4 states and 6 transitions, 4 of them labelled
- `compose_board.py`: COMPOSED, 6 nodes and 6 connectors to read back, 47,187 characters, under the 50,000 one call takes
- The only layout risk I can see before the write is the two parallel transitions into the confirmation. I'll look at them on the overview and report any overlap as measured.

**What the write does**
- **Plan and file:** existing file `<test-file-key>`, with Fernhouse Product recorded as the plan you named. I haven't confirmed the file sits in that plan. No new file is created, so there is no `whoami` or `create_new_file` call.
- **Written:** one framed board titled "Fernhouse return states", with subtitle, zone-free state diagram, key and source line. It lands 400 pixels to the right of whatever the page already holds. I haven't read the file's current content.
- **Extensions:** none, no pins or stickies.
- **Calls:** up to three. `create_session` on the file key, one `use_figma` call that composes the board, and one `get_figjam` read-back. On a Starter plan or a View or Collab seat, the monthly allowance is six calls and read tools count against it.
- **Dials drawn at:** balanced detail, mixed audience, laptop distance.
- **Rollback:** I delete the one board section the write returns, through `use_figma`, and only after you say yes to the deletion. Nothing else in the file is touched.

Do you approve writing this board into file `<test-file-key>`?