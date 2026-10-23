The connected Figma account has no plan named Fernhouse Product, so I have not created the board. The flow model is checked and ready.

**Plans the account returns**
- <figma-plan-1> (Pro plan, Full seat)
- <figma-plan-2> (Pro plan, Full seat)
- <figma-plan-3> (Starter plan, View seat)

**Reading:** the flow starts on a sold-out product page, branches on whether the customer is signed in, saves the alert to the account or to the email address, then ends with one email when the item is back in stock. It has 8 nodes and 8 connectors, with 2 labelled decision exits. Source: Lotte's spec, read as current behavior.

**Glance lines:** first, "One email sent" should win because that is the promise the flow exists to explain. Second, the signed-in and guest branch shows where the alert is captured. Last, "Item back in stock" is the trigger that starts delivery.

**Question:** which plan should own the new board? If Fernhouse Product is a project inside one of these teams, send its Figma link. If it sits under a different Figma account, connect that account and I'll re-check.
**Recommended:** <figma-plan-1>, because the account is an admin there and holds a Full seat, so the board can be edited and read back. The Starter plan is limited to six Figma tool calls a month.
**Why:** a board is visible to every member of the plan it is created in.

**Write plan**
- File: a new FigJam file, created by the write
- Content: one user flow named "Back-in-stock alerts" with 8 nodes, 8 connectors and a light green accent on "One email sent", plus a title text node
- Left out: push alerts in the app, proposal only, nobody has agreed them
- Extensions: none
- Read calls: whoami already spent, then get_figjam and a screenshot if the read carries none
- Rollback: delete the new file

Name the plan and confirm, and I'll write the board.