The model passes the pre-write check (7 nodes, 6 connectors, 0 crossings) and composes into one `use_figma` call. Here is what the write would do.

**Question:** which screens does a Fernhouse customer pass through to start a return in the app, and where do they choose?
**Outcome:** a reader can follow a return from the order list to a confirmed return and see where the 30 day window sends the customer to Contact support.
**First glance:** Return confirmed with QR code, the goal the flow reaches.
**Second glance:** Drop-off point or courier pickup, the choice that leads to it.
**Last glance:** Contact support, the exit after 30 days.
**Plan:** Fernhouse Product, as you stated. I can't confirm from here which plan owns the file.
**File:** the existing FigJam file `<test-file-key>`. No new file is created.
**Writes:** one composed board named "Start a return", added to that file beside what is already on the page. It has 7 nodes and 6 connectors in three zones (Find the order, Request the return and Done), plus a title, a key and a source line, at the Laptop reading distance. The nodes, in order:
1. Order list
2. Order detail: Start a return
3. Within 30 days? (Yes goes on to the reason list, No goes to Contact support)
4. Pick a reason
5. Drop-off point or courier pickup
6. Return confirmed with QR code
7. Contact support

**Not drawn:** the sources don't say whether a screen follows the method choice, such as picking a drop-off point or booking a courier. The board therefore shows the choice as one screen that leads to the confirmation. The free pickup over €100 stays off the board as a proposal.
**Extensions:** none.
**Calls:** `create_session`, a `get_figjam` read of the file before the write to check for an existing "Start a return" board, one `use_figma` and one `get_figjam` read-back. If the account is on a Starter plan or a View or Collab seat, these count against its six tool calls a month.
**Rollback:** delete the one board section the write returns, which removes everything drawn inside it. I would do that only on your yes, and the rest of the file is not touched.

Write it?