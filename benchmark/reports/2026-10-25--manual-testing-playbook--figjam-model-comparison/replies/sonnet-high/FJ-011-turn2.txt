**Playback: what I read and what I assumed**

I used your recommended answers for questions 1 and 3. The workspace has no damaged-item runbook, so for question 2 I read `context/fernhouse-context.md` (company context, updated 2026-09-18, owned by Lotte). It is the only Fernhouse source I found. It states the general returns flow and says nothing specific to damaged items.

**The Brief**
- Reader: CS agents and warehouse staff, accepted
- Question: who does what from the customer's contact to the refund, and where does the warehouse take over?
- Outcome: the reader sees what reaches the warehouse and what the CS agent waits for in return
- Scope: the main path, with refund amount rules, payment-provider steps and non-damage refunds out, accepted
- Entry: the customer contacts CS (stated, Key flows 6)
- Exit: the CS agent refunds (stated, Key flows 6)
- Actors: Customer, CS agent and Warehouse operator (stated, Personas and roles)
- Decisions and states: none drawn. The source names a 30-day return window, a CS lead approval above €200 and a warehouse check, but states no outcome for any of them, so all three are left out and named

**Assumed (two rows)**
- Damaged items follow the general returns flow unchanged. Settled by: your confirmation, or a pointer to a damaged-item procedure
- The customer posts the item back with the emailed label, and that is how it reaches the warehouse. The source says the label is emailed and then the warehouse checks the item, with nothing in between. Settled by: your confirmation, or how the warehouse learns a return is coming

**Finding before drawing**
The source shows no direct handoff from the CS agent to the warehouse. The item reaches the warehouse through the customer, so the highlighted handoff is the customer sending the item back and the warehouse checking it.

**Outline**
The type is a process board, left to right, with lanes Customer, CS agent and Warehouse in the order work first reaches them. The sentence the board answers is "Who does what from the customer's contact to the refund, and where the warehouse takes over".

- Nodes: Contact CS about the item (Customer), Create the return in Admin (CS agent), Email the return label (CS agent), Send the item back (Customer, assumed), Check the item (Warehouse), Refund issued (CS agent, end)
- Edges: the first four steps in that order, then "Parcel" into Check the item, then "Item checked" into Refund issued. The last edge is read from the source's order and is not stated outright
- Four of the five edges cross lanes, and "Parcel" is the warehouse handoff

**Two framings**
- Main path only, with the three left-out items named in the reply. Recommended, because every node and edge traces to the source
- Main path plus decision exits for the window, the warehouse result and the approval. It costs three exits whose destinations no source states

**The look**
- Accent: Check the item, the step where the warehouse takes over
- Zones: none, because the lanes already group the steps
- Title: Damaged-item refund
- Subtitle: Who does what from the customer's contact to the refund, and where the warehouse takes over
- Source line: the company context, with the three left-out items named
- Detail Balanced, audience Mixed and distance Laptop, all defaults

Does this reading hold, including the two assumed rows and the accent on Check the item?

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.