The model passes the pre-write check and composes. I read the existing file first, and its page is empty. Nothing is written yet.

**Check:** `PASSED`, process with 6 nodes, 6 connectors and 4 lanes, 0 crossing pairs.

**Model**
- **Customer lane:** "Reports the damage to CS".
- **CS agent lane:**
  - "Create return, email label"
  - the decision "Refund over €200?"
  - the end "Refund issued"
- **Warehouse operator lane:** "Check the item".
- **CS lead lane:** "Approve the refund". The decision's "Yes" exit goes to this step, and its "No" exit goes straight to the refund.
- **Board text:** the source line says the damage-specific steps are not in any source.
- **Added lane:** I added the CS lead lane to the three lanes in the playback. Admin permissions say a CS lead approves refunds above €200, and that handoff is the only branch in the flow.

**Question:** who handles a damaged-item claim at Fernhouse, and where does it change hands?
**Outcome:** a reader can see which team owns each step, from the customer's contact to the refund.
**First glance:** "Refund over €200?", the CS agent's decision. It is the one branch, and it decides whether the claim goes to a CS lead.
**Second glance:** "Create return, email label", the step where the claim passes from CS to the warehouse.
**Last glance:** the source line, which says what no source covers.

**Plan:** Fernhouse Product, as you supplied it. I haven't verified that the file belongs to that plan.
**File:** the existing FigJam file `<draft-file-key>`. The board goes in as a new section, and nothing already there changes. It creates no new file.
**Writes:** one composed board titled "Damaged-item claim", with a title, subtitle, key and source line, at Laptop reading distance, balanced detail and a mixed audience.
**Extensions:** none.
**Calls:** one `use_figma` and one `get_figjam` read-back. I've already spent the session and the file read.
**Rollback:** delete the one board section the write returns. That needs its own yes, and I won't delete anything else.

Write it?