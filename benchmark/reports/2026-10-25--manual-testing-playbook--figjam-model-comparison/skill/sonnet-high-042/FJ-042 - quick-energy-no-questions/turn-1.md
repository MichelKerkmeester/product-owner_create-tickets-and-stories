Quick energy, so no intake rounds. I read the Fernhouse context and picked a type, and nothing has been written to Figma yet.

"Just do it" can't skip the reading check or the write gate, because the board lands in a shared plan. I asked no intake questions and filled every row from the sources, marking the guesses as assumed.

**No source covers damaged items.** `context/fernhouse-context.md` (updated 2026-09-18) describes the returns path in Key flows 6 and the roles. It has no damaged-item steps. The only damaged-item material is the worked example in `assets/examples/process-fernhouse-refund.md`, which cites a support runbook that isn't in this repo. I haven't used it as a source.

**Type: process with lanes.** The question is who handles a damaged item and where it changes hands. A user flow has no screens to chart, because the context says there is no self-serve return today.

| Row | Value | Status |
|---|---|---|
| Reader | A Fernhouse teammate who needs to see who owns each step | assumed, settled by naming the reader |
| Question | Who handles a damaged item from first contact to refund, and where does it change hands? | assumed |
| Outcome | The reader can see which role owns each step and where the €200 approval enters | assumed |
| Scope | The standard returns path, with damage as the reason it starts | assumed |
| Entry | The customer tells CS the item arrived damaged | assumed, the context says customers contact CS but never mentions damage |
| Exit | Refund issued | captured |
| Actors | Customer, CS agent, Warehouse operator, CS lead | captured |
| Decisions | One: refund over €200, where a CS lead approves | captured |
| Sources and class | `fernhouse-context.md`, current behavior | captured |

**Outline, 4 lanes, 7 nodes, 7 connectors:**
* Customer: Damage reported to CS
* CS agent: Create return, email label
* Customer: Send the item back (assumed, the context implies it without stating it)
* Warehouse operator: Check the item
* CS agent: Refund over €200?
  * Up to €200 goes straight to Refund issued
  * Over €200 goes to CS lead: Approve the refund, then Refund issued

**Look:**
* First glance: Refund issued, the goal. This is assumed, because no source says which handoff is slowest.
* Audience Mixed, detail Balanced, distance Laptop, all by default.
* Title: Damaged item: return and refund.

**Left out, none of it in the sources:**
* Damage evidence such as a photo
* Replacement instead of refund
* Who pays for the return label
* What happens after the 30-day window
* What Fernhouse does with a carrier `DAMAGED` exception

If the runbook behind that example is real Fernhouse practice, send it and I'll redraw from it. It would settle most of those gaps.

Does this reading hold, or should I change a row before the write gate?