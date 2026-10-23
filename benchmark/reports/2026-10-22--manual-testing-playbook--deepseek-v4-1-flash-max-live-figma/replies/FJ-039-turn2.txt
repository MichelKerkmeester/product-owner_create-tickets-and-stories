**Brief**

| Row | Value |
|---|---|
| Question | Who handles a Fernhouse return, in what order, and where does the work change hands? |
| Reader | The Post-purchase team |
| Outcome | The reader can see every handoff and the €200 approval branch, then choose which handoff to measure or fix first |
| Entry and exit | The customer contacts CS within 30 days of delivery, and the flow ends when the refund is issued |
| Source | `context/fernhouse-context.md`, Key flows item 6 and Personas and roles. Every node and edge is current behavior. The source gives 1,900 requests a month and a 6-day average from first contact |

**What the board says**

- Customer contacts CS within 30 days of delivery
- CS agent creates the return in Admin
- CS agent emails a return label
- Warehouse operator checks the returned item
- The refund amount is checked against €200
- Under €200, the CS agent issues the refund
- Over €200, the CS lead approves and the CS agent issues the refund

Every node is current behavior. The label-to-warehouse edge is medium confidence because the source does not name the customer's posting step. The refund branch follows the stated €200 rule.

**Glance lines**

- First glance: the €200 approval threshold, the one step that adds a second person
- Second glance: the return parcel crossing from CS to the warehouse, the only physical handoff
- Last glance: the 30-day window on the entry node, which qualifies the whole flow

**Check:** PASSED, 7 nodes and 7 connectors, 2 labelled decision exits, 4 lanes and 0 crossing pairs

**Gate**

- Plan: <figma-plan-1> (no Fernhouse Product plan on this account)
- File: a new FigJam file, which this call creates
- Writes: one process, 4 lanes, 7 nodes and 7 connectors, named 'Fernhouse return flow', with a title text node above it
- Extensions: none
- Read calls: one whoami already spent, one get_figjam read-back and one screenshot only if the read carries none
- Rollback: delete the new file
- Left out: the customer posting the parcel (not stated in the source), step-level wait times (the source gives one 6-day average) and the path after 30 days (not stated)

Write it?