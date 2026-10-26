I've read the Fernhouse sources, and nothing is drawn or written yet. This is round one of the intake: the reader, the question, the outcome and the target.

**Reading:** The only source on returns is `context/fernhouse-context.md`, Key flow 6. It says there is no self-serve return today. A customer contacts CS, a CS agent creates the return in Admin and emails a return label, the warehouse checks the item, and the agent refunds. The window is 30 days from delivery. The same file says a CS agent can refund up to €200 per order and a CS lead approves anything above that, and that a refund takes 6 days on average. You supplied no screenshots, Figma frames or runbook. That leaves no return screens to draw as a user flow, so the type that fits is a process with a lane per role.

**Question 1: who reads the board, what do they ask and what can they do after?**
- Recommended: the reader is someone on Post-purchase (the team that owns `RET`) picking up returns work. The question is "who does what, and where does a return change hands between the customer, CS and the warehouse?" After reading, they can see each handoff and where the 6 day average refund time builds up.
- Why: the sources describe a hand-run process across three roles, which a laned process answers and a screen flow cannot.
- If you meant a future self-serve return in the app, say so and send the brief or screenshots. It has no source today, so I would not draw it.

**Question 2: what must the board not do?**
- Recommended: show only today's CS-led return. Leave out any self-serve step, the `RET` tracking of return parcels (listed under scope in the order-tracking brief, not current behaviour) and refund payment mechanics at the payment provider.
- Why: a board that mixes proposals into current behaviour misleads the reader, and the sources give no detail on refund mechanics.

**Question 3: is the target right?**
- Reading: you named an existing file, `<draft-file-key>`, so the board goes in as a new section beside whatever it holds, and nothing already there changes. That route needs no plan and no new file, so I read "Fernhouse Product plan" as applying only if a new file were needed. Your second paragraph names the Barter team plan for that case, which conflicts with the first.
- Recommended: write into the existing file. If it cannot be opened for writing, I stop and ask which plan you want rather than choosing between the two.
- Why: a board that lands in the wrong plan is visible to that plan's members at once.

Reply "use the recommended answers" or correct any of the three. Next comes the full playback of the settled rows, then the model, the check and a separate write gate.