The model passed the pre-write check, and the board code composed. Nothing has been written to Figma yet.

**Question:** who does what, and where does a damaged-item claim change hands?
**Outcome:** a reader can see which team owns each step of the refund and where the claim moves between teams.
**First glance:** the three team lanes and who owns each step.
**Second glance:** "Damage clear?", the CS check that sends the claim on or back to the customer.
**Last glance:** the source line naming what the board doesn't cover.
**File:** the existing FigJam file `<test-file-key>`, which you named in place of a new file. I take it to belong to the Fernhouse Product plan as you said, but I can't verify that from here. The board lands as a new section 400 pixels right of whatever is already on the page, so it covers nothing.
**Writes:** one composed board named "Damaged-item refund".
* 3 lanes, each with its own tint: Customer, CS, Warehouse
* 7 nodes and 7 connectors
* 2 labelled decision exits (Clear, Unclear)
* Title, subtitle, key and source line
* Laptop reading distance, no step in focus, and "Refund released" as the goal

**Extensions:** none.
**Left out:** a rejection after the second photo, a failed inspection and a limit on second photos. None of these are in your description, so the source line names them as not covered.
**Calls:** `create_session`, one `use_figma` and one `get_figjam` read-back. I'll load Figma's `figma-use` and `figma-use-figjam` skills first. On a Starter plan or a View or Collab seat, Figma caps tool calls at six a month.
**Rollback:** delete the one board section the write returns, only after you say yes to that deletion. Nothing else in the file is touched.

Write it?