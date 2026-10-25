I haven't drawn or written anything yet. I need to settle which return flow you mean, because the Fernhouse sources disagree on it.

**What I found**
- `context/fernhouse-context.md`, Key flows item 6, says there is no self-serve return today. The customer contacts CS and a CS agent creates the return in Admin and emails a label. The warehouse checks the item and the agent refunds. The window is 30 days from delivery. CS handles about 1,900 return requests a month, and a refund takes 6 days on average from first contact.
- The only other "Fernhouse return flow" is the app-screens example in `sk-create-figjam/assets/examples/`. It is a fixture with invented screens, so I'm not treating it as a source.
- You gave me no screenshots, Figma frames or returns doc.

**Where the board goes**
I'll compose it as a new board section inside file `<test-file-key>`, not a new file. The Fernhouse Product plan only matters when a file is created, so it won't affect this write. I'll name the file in the write gate and won't make any Figma calls before your yes.

**Round one**

1. Which return flow, and from what?
   - Reading: the only source in the workspace describes today's CS-handled return. No source describes an in-app flow.
   - Question: is the board today's return, or a proposed self-serve one? If it's the proposed one, please send its screens or doc.
   - Recommended: today's CS-handled return from `fernhouse-context.md`, drawn as a process with lanes for Customer, CS agent and Warehouse. Work changes hands three times, which a user flow can't show.
   - Why: it's the one flow a source states, and drawing a self-serve flow would invent screens.

2. Who reads the board, and what should they decide from it?
   - Reading: the context names the Post-purchase team as owner of returns. It also gives the 6-day refund and the 1,900 monthly requests as the pain.
   - Recommended: the Post-purchase team and CS leads. After reading, they can see where the handoffs sit and where the 6 days go.
   - Why: that matches the only numbers the sources give.

3. What must the board not do?
   - Reading: the source states four steps and the 30-day window. It gives no step for a return outside 30 days, a failed warehouse check or a label that is never used.
   - Recommended: draw only the four stated steps plus the 30-day check. Leave the unstated branches off the board and list them under `Left out:` as open points, with no invented branches.
   - Why: a partial board that matches the source is safer than a complete one that guesses.

If you skip any of these, I'll go ahead on the recommended answers and mark them assumed. Your next message can just say "accept all".