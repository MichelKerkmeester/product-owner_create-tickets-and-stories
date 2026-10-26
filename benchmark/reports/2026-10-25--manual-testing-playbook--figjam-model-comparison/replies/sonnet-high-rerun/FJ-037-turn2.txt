Path: `export/002 - Story-fernhouse-return-flow.md`
Verified: read-back succeeded; 64 lines
HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.
Quality: every floor met | Kind: Story | Energy: Standard

The Story lets a Fernhouse customer start a return from their order instead of contacting CS. Problem rests on the figures in `context/fernhouse-context.md`: the `30 days` window, about `1,900` requests a month and a `6 days` average refund. Requirements hold the window and the three surfaces. Three acceptance criteria cover starting a return inside the window, the window having ended, and CS receiving the request.

### Open items
1. **Recommended answers**
   - **Situation:** The first question only had recommended answers for the kind, the board target and the order. The role, value and requirements came from `context/fernhouse-context.md`: persona `Customer`, area `RET`, and the statement that no self-serve return exists today
   - **Open:** Correct the role or value if the Story should serve someone other than the customer
2. **No screens or return rules supplied**
   - **Situation:** The repository holds no returns brief and no return screens. `sk-create-figjam/assets/examples/user-flow-fernhouse-return.md` states that its screens and rules are invented, so I did not use it
   - **Open:** Send the screens or a returns brief and I'll add the exact copy and values to Requirements
3. **Surfaces**
   - **Situation:** I assumed `Web`, `iOS` and `Android`, the three customer surfaces in the company context
   - **Open:** Strike any surface the first release leaves out
4. **Handoff to CS**
   - **Situation:** The Solution and criterion 3 assume requests reach CS through today's Admin returns handling, with the warehouse check and the refund unchanged
   - **Open:** Confirm this, or name what replaces those steps
5. **After the window**
   - **Situation:** The company context gives the window and nothing about what happens after it, so criterion 2 only says no return starts and the customer is told the window has ended
   - **Open:** Say whether the customer is pointed to CS once the window has ended
6. **Guests**
   - **Situation:** A guest has no order history to start a return from, and the criteria say "customer" without separating guests from signed-in customers
   - **Open:** Confirm whether guests are in scope
7. **Received confirmation**
   - **Situation:** I added "the customer sees that the request was received" to criterion 1
   - **Open:** Strike it if the flow confirms in another way
8. **Sections left out**
   - **Situation:** References is omitted because no links were supplied, and Delivery is omitted because nobody asked for it
   - **Open:** Nothing to confirm

Before I draw anything, this is how I read the board.
Question: which screens does a customer pass through to start a return from an order, and where do they choose?
Outcome: a reader can follow a return from the order to a received request and see where the `30 days` window ends it.
Type: user flow.
Settled by the sources: the Story and the company context give the order as the start, the `30 days` window as the exit and the received request as the end.
Not settled by any source: the screens themselves. No screenshot, Figma link or screen list exists, so any screen I named would be invented.
Left out: the refund and the warehouse check, because they come after the customer's request.
Assumed: balanced detail, a mixed audience and laptop reading distance. The target is the existing FigJam file `<draft-file-key>`, as a new section beside what it holds.
Still open: the screens. My recommendation is that you send them first. If none exist yet, I draw only the steps the Story's criteria state, as a short flow named for outcomes rather than screens, with the gap named on the board's source line.
Is this the right reading of the board, or do you have the screens to send first?