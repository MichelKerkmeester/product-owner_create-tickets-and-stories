Path: `export/002 - doc-deal-type-split.md`
Verified: read-back succeeded; 30 lines
HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.
Quality: Source safety pass, Shape fit pass, ClickUp layout pass, Readability pass, Voice pass | Kind: Doc (Catalog) | Energy: Standard

The Doc is a short catalog of Barter deal types with an index table for each type's share of deals. It's written for the product team and is marked Unverified, because no real figures exist yet: the share column reads "Not supplied" until a data owner sends them. Trends over time, revenue per type and breakdowns by market are out of scope.

I couldn't run the output format checker on this file, because `validate-output-format.cjs` isn't in this checkout.

### Open items
1. **Figures**
   - **Situation:** No real data was supplied, so every share is blank. The 60, 30 and 10 split from the pie test was made up and isn't in the Doc
   - **Open:** Send the figures with their source, owner and the period they cover
2. **Deal types**
   - **Situation:** Image, Video and Story come from the test model and haven't been checked against the product
   - **Open:** Confirm the list, or add the missing types or an "other" group
3. **Purpose and audience**
   - **Situation:** I assumed the product team reads it to see which deal types brands pick most
   - **Open:** Confirm, or name the readers and what they need to decide
4. **Status**
   - **Situation:** I assumed it shows the current split, so the status line will name a period once figures arrive
   - **Open:** Say if it should cover a past period or a target split instead
5. **Shape and scope**
   - **Situation:** I used the short table you were offered first and left out trends, revenue and markets
   - **Open:** Say if you want deal type definitions or any of those added

Want me to change anything?