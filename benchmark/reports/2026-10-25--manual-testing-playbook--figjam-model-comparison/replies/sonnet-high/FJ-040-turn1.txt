Nothing is written to the board yet. This is intake round 1 of 3, and the write waits for the playback and then its own yes.

**Settled so far**
- Target: file `<draft-file-key>`, each board added as a new section beside what the file holds, with nothing already on it touched. A named file needs no `create_new_file` and no plan, so the Fernhouse Product plan is not used.
- Source: `context/fernhouse-context.md`, updated 2026-09-18, class current behavior. It covers checkout payment (key flow 2), fulfilment (flow 4) and returns (flow 6). It covers sign-in only as a role line.
- Detail balanced, audience mixed and laptop distance, all assumed.
- Fallback conflict: if the file can't be opened, your first sentence says the Fernhouse Product plan and your last says the Barter team plan in drafts. I would stop and ask then, not pick one.

The whole product can't be one board. A user flow holds 9 nodes, and each area asks a different question, so each needs its own type.

**1. Reader, question and outcome**
- Reading: the context doc says every team reads it before writing a ticket, so the reader looks like a Fernhouse team member picking up an area they don't own.
- Question: who reads the boards, what must they answer, and what must the boards not do?
- Recommended: a product or engineering team member new to an area. Each board answers who does what and which service owns it. The boards show no step the doc doesn't state.
- Why: it matches how the doc is used and keeps guessed steps off the boards.

**2. Split and types**
- Reading: five areas, five different questions.
- Question: should each area get its own board?
- Recommended: five boards in this order:
  - Signup: user flow
  - Returns: process, with lanes for Customer, CS agent and Warehouse operator
  - Refunds: process, with the €200 agent limit and CS lead approval above it
  - Warehouse: process, from paid order to the 18:00 collection, with the 15:00 cut-off and the 16:00 pallet booking
  - Billing: held until question 3 is settled
- Why: returns end where refunds begin, and one board per area stays inside each budget. Five composes plus read-backs can pass the six tool calls a month that a Starter plan or a View or Collab seat allows, so the gate will list the call count.

**3. Signup and billing sources**
- Reading: the doc has no signup steps beyond "guests give an email at checkout". For billing it has payment through the payment provider and refund payout, and no subscriptions or invoices.
- Question: what do signup and billing cover here, and which source shows their steps?
- Recommended: send signup screenshots, a Figma flow or a doc, and say what billing means. Without them I draw the three boards the doc supports and list signup and billing under `Left out:`.
- Why: a partial board of the real system beats a polished one of an imagined system.

Do the recommended answers work, or what should change?