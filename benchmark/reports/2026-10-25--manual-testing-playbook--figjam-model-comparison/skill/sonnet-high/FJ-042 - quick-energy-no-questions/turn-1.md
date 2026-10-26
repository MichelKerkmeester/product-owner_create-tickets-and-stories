I haven't written anything to Figma. The only damaged-item material in the repo is invented, so this is the Quick playback and the board waits for your answer.

**Sources**
- Your request names no runbook, screenshots, ticket or Figma link for the damaged-item flow.
- The one damaged-item match is `sk-create-figjam/assets/examples/process-fernhouse-refund.md`. It says every step in it is invented, so drawing from it would put a made-up process on a shared board.
- `context/fernhouse-carrier-tracking-api-facts.md` has a carrier `DAMAGED` exception code. That is an event, not a customer flow.
- `context/fernhouse-context.md` describes returns in general (Key flow 6) and nothing damage-specific.

**Brief rows**
- Reader: assumed, the Fernhouse product and CS teams. A named reader would settle it.
- Question: assumed, who does what in a damaged-item claim and where it changes hands.
- Type: assumed, a process with three lanes (Customer, CS agent and Warehouse operator). Returns already hand off from CS to the warehouse, and a user flow would need screens that don't exist.
- Entry, exit and decisions: unasked, because there is nothing to read them from.
- Sources: none.

That is more than two rows assumed or unasked, so the draw-ready threshold isn't met and I won't draw.

**Target**
- The board goes into `<draft-file-key>` as a new section beside what it already holds.
- No `create_new_file` is needed, so the Fernhouse Product plan and the Barter drafts fallback don't apply. I took the explicit file key over the plan wording, and I'm marking that as assumed.
- The write still stops at the gate for its own yes, because it touches a shared file.

Reply with the support runbook, screenshots, a ticket or a Figma link, and I'll draw the process from it. Or should I draw the general returns flow from Key flow 6 instead, with the damage-specific steps listed as left out? I recommend the first, because the second would leave the board mostly gaps.