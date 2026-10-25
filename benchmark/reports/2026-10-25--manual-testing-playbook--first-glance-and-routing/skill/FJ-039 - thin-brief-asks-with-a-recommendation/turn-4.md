Here is the full playback of the reading. Nothing has been modelled or written yet, and the board is not at the write gate.

**What the board answers**
- **Question:** who does what, in which order, from a customer's first contact to the refund
- **Outcome:** the reader can see where work changes hands, and which refunds need a second person
- **Reader:** a Post-purchase team member or PM scoping `RET` work
- **Type:** a process diagram with four lanes: Customer, CS agent, Warehouse and CS lead

**What the source settled**
- One source, Key flows item 6 and the glossary in `fernhouse-context.md`, class current behavior
- It states the order: contact, return created in Admin, label emailed, warehouse check, refund
- It states the €200 agent limit and the CS lead approval above it

**What is assumed**
- The customer sends the parcel back between the label and the warehouse check, because no source says it
- The €200 decision sits after the warehouse check, because no source places it in the flow

**Outline in drawing order**
1. The first line is the question: who does what, in which order, from a customer's first contact to the refund
2. Customer: "Ask for a return" is the start, read from the source
3. CS agent: "Create the return in Admin"
4. CS agent: "Email the return label"
5. Customer: "Send the parcel back", assumed
6. Warehouse: "Check the item"
7. CS agent: "Refund over €200?" is the decision, with its placement assumed
8. CS lead: "Approve the refund"
9. CS agent: "Refund issued" is the end
10. Eight connectors follow that order, with two labelled exits from the decision: Yes goes to the approval and No goes straight to "Refund issued". The approval then joins "Refund issued"

**Left out, and why**
- What happens to a request after day 30, because no source says
- What the warehouse does when the check fails, because no source says
- What happens if the CS lead declines, because no source says
- Self-serve returns and return-parcel tracking, because you ruled them out

**Two framings**
- **One board:** the happy path runs across the lanes and the €200 branch sits beside it. It costs nothing in readability at 8 nodes
- **Overview and detail:** one board for the handoffs and one for the approval. It earns its place only if the board grows past about 9 nodes
- **Recommended:** one board, because the flow is short and the branch is part of the question

**Look**
- **First glance:** "Refund issued", the goal and the only accent
- **Second glance:** the handoffs between lanes
- **Last glance:** the CS lead approval, which can wait
- **Title:** Fernhouse return flow
- **Subtitle:** Who does what from a customer's return request to the refund, in today's CS-led flow
- **Source line:** the context note, plus the three left-out items above
- **Settings:** Balanced, Mixed and Laptop

Does this reading match what you want the board to say?