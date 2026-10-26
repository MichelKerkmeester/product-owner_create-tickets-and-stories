Nothing is written yet. This is intake round 1 of 3, and the write has its own gate later.

**Target:** I'll write a new section beside what's already in file `<draft-file-key>`. That needs no plan and no new file. You said the board is open in Figma Desktop, so I'll assume that is this file and confirm it with a read at the gate.

**Type:** user flow, because your steps are screens and two choices. By my count it is 8 nodes, inside the 9-node budget.

**1. Reader, question, outcome**
- Reading: your message lists the steps but doesn't say who reads the board or what it must settle.
- Recommended: the reader is the Fernhouse team building the return flow. The question is "Which screens does a customer pass through to return an item, and where does the 30 day check stop them?" The outcome is that the reader can follow a return from an opened order to the confirmation and see where it ends early.
- Why: that is the question your steps already answer.

**2. What must the board not do?**
- Reading: your steps cover only the customer's side, up to the confirmation.
- Recommended: no CS, Admin or warehouse steps, no refund timing or amounts, and nothing after the not-eligible screen, since no step follows it in what you gave me.
- Why: it keeps the board to the path you described and adds no steps no source states.

**3. Source status and a conflict**
- Reading: I don't have the returns doc as a file, only your summary of it. `context/fernhouse-context.md` (updated 2026-09-18) says there is no self-serve return today. The customer contacts CS, an agent creates the return in Admin and emails the label, and the 30 days run from delivery. Your flow has the customer starting the return and printing the label, and it counts from the order.
- Question: is this flow current behavior, approved direction or a proposal? Do the 30 days run from the order or from delivery?
- Recommended: draw it as the doc states it, with the check worded "Order older than 30 days?". Mark the status unknown and say "status not confirmed" in the board's source line.
- Why: I can't call it current behavior against that context file, and I won't claim an approval nobody gave me. If you don't answer, it stands as assumed and shows in the playback. The order-versus-delivery difference goes on a `Finding:` line either way.

Reply with answers or "use the recommended answers". The playback comes next. Round 2 will ask about the entry screen and the surface (web or app).