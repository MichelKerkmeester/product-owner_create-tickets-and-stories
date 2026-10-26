The model passed the check, but I can't write the board yet because the destination isn't settled.

**Where it can't go**
- **The file `<test-file-key>`.** Flow Mode only writes into a new file or a board it wrote itself in this work. That file is neither, so I won't write into it.
- **A "Fernhouse Product" plan.** Your Figma account doesn't have one. The plans it does have are <figma-plan-3> (Starter, View seat), <figma-plan-1> (Pro, Full seat) and <figma-plan-2> (Pro, Full seat).

**My recommendation:** use your fallback. That means a new FigJam file in the **<figma-plan-1>** plan, left in drafts with no project. Your Full seat there isn't limited to six Figma tool calls a month, so this write won't use up an allowance.

**What will be written once you confirm**
- **Question it answers:** How does a Fernhouse damaged-item refund move from the customer to CS to the warehouse, and where does the claim pass to the warehouse?
- **Outcome:** One process board, "Fernhouse damaged-item refund", with three lanes:
  - Customer
  - CS agent
  - Warehouse operator
- **Steps and connections:** 8 steps and 8 connections, including the loop back for the second photo, which is assumed. The model passed the pre-write check with no crossing lines.
- **Highlighted step:** "Send to warehouse queue", the handoff to the warehouse.
- **What the eye should land on:**
  - First: the handoff to the warehouse
  - Second: the "Damage clear?" decision and the second-photo loop
  - Can wait: the courier pickup and the inspection
- **Extra:** one sticky note saying every decision is logged in the claims table.
- **Under the key:** a source line naming the support runbook and the under-€20 pilot that was left out.

**Figma calls this will use:** `create_new_file` in <figma-plan-1>, one `use_figma` call to draw the board, one for the sticky note and `get_figjam` to read the board back.

**Undoing it:** delete the new draft file. Nothing else is touched.

Should I create the new file in <figma-plan-1> drafts and write the board there? If it should go somewhere else, tell me the plan.