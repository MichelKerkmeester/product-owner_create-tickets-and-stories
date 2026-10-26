Nothing is drawn or written yet. This is the playback: what I read, what I assumed, and the outline I'd draw.

**Board sentence**

Who handles each step of a Fernhouse return today, from the customer's first contact to the refund, and where the work changes hands.

**Brief**

| Row | Value | Status |
|---|---|---|
| Reader, Question, Outcome | Fernhouse Product. The question is the sentence above. After reading, they can name every role in a return and each handoff between them | assumed, from your yes to the recommendations |
| Scope | Today's CS-handled return only. The self-serve idea is out | assumed, from your yes |
| Entry | The customer contacts CS, within 30 days of delivery | captured |
| Exit | The agent refunds the customer | captured |
| Actors | Customer, CS agent, warehouse operator | captured |
| Decisions | One: a refund over €200 needs a CS lead | assumed, see below |
| Sources and class | `context/fernhouse-context.md`, Key flows item 6 and Personas and roles. Current behavior, last updated 2026-09-18 | captured |

Two readings go past what the source states:
- **Customer sends the item back.** The source jumps from the emailed label to the warehouse check. I'd add one customer step between them, marked medium confidence, because the warehouse can't check an item that never arrived.
- **€200 approval on return refunds.** Personas says an agent refunds up to €200 per order and a CS lead approves more. Key flows only says "the agent refunds". I'd apply the limit to return refunds.

**Outline** (lane, step, row)
1. Customer: "Contacts CS" (start, entry)
2. CS agent: "Create the return in Admin"
3. CS agent: "Email a return label"
4. Customer: "Send the item back" (inferred)
5. Warehouse operator: "Check the item"
6. CS agent: "Refund over €200?" (decision, assumed)
7. CS lead: "Approve the refund"
8. CS agent: "Refund the customer"
9. Customer: "Customer refunded" (end, exit)

Edges run 1 to 2 to 3 to 4 to 5 to 6. From 6, "Yes" goes to 7 and then 8, and "No" goes straight to 8. Then 8 goes to 9. That is 9 edges, and 7 of them cross a lane, so the lane changes on almost every move. That is the finding a list can't show as well, so a diagram earns its place. Nothing can be removed without losing a handoff. It sits within the laned process budget of 12 nodes and 16 connectors.

**Left out, because the source is silent**
- A request outside the 30 days
- An item that fails the warehouse check
- Who pays and arranges the return shipping
- The refund email

**Two framings**
- **Happy path with the approval branch** (recommended). It shows only what the source states. It reads fast and doesn't pretend to know the exits.
- **Full exit map.** It adds the outside-window and failed-check exits. Both would be drawn as `Unknown`, which makes the board look more complete than the sources are.

**Look**
- **Accent:** the end, "Customer refunded". No source gives step delays, so I can't honestly mark a slowest handoff. The 6-day average goes in the subtitle.
- **Detail, audience, distance:** Balanced, Mixed, Laptop
- **Zones:** the four lanes only (Customer, CS agent, Warehouse operator, CS lead), with no extra zone lines
- **Title:** "Fernhouse return today"
- **Subtitle:** "How a return runs today, from the customer's first contact to the refund. About 1,900 requests a month, 6 days on average to refund."
- **Source line:** "Sources: Fernhouse company context, 2026-09-18. Left out: requests outside 30 days, failed item checks, return shipping, the refund email."
- **Critique questions** the gate will answer about the sketch:
  - Where does the eye go first, and is that the node the board most needs read?
  - Can each of the 7 handoffs be followed without a crossing?
  - Does any step have two owners?
  - Does the board still read in greyscale?

Is this reading right? In particular, are you happy with the added "Send the item back" step and the €200 limit applying to return refunds? My recommendation is yes to both and to everything above. If so, say so and I'll move to the check and the write gate.