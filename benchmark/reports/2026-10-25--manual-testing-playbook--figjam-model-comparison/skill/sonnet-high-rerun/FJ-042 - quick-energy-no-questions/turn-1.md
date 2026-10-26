I haven't written anything to FigJam. Even on "just do it", Flow Mode needs a yes at its write gate before it touches a shared file, so this is the Quick-energy playback with no questions in it. If a row is wrong, correct it and I'll redraw the playback over that row.

**Brief** (every row below is `assumed`; the note on each says what would settle it)

| Row | Reading | Settled by |
|---|---|---|
| Reader | Post-purchase team and CS leads | Who the board is for |
| Question | Who does what, and where does a damaged-item claim change hands? | Your reader |
| Outcome | A reader can see which role owns each step from the damage report to the refund | Your reader |
| Scope | A customer reports damage on a delivered order, handled through today's CS-led return | Whether you mean a different damage flow |
| Entry | The customer contacts CS about the damaged item | Returns flow, step 6 |
| Exit | The agent refunds | Returns flow, step 6 |
| Actors | Customer, CS agent, Warehouse operator, and CS lead for refunds over €200 | `fernhouse-context.md`, Personas |
| Decisions | Within the 30-day return window, and refund over €200 | `fernhouse-context.md`, Glossary and Personas |
| Sources | `context/fernhouse-context.md`, dated 2026-09-18, current behavior | None other |

- **Type:** process with lanes. A damaged-item flow hands work between teams, so "who does what" fits better than a user flow of screens.
- **Outline:** customer reports damage, window check, agent creates the return in Admin and emails the label, customer sends the item back, warehouse checks the item, over-€200 check, CS lead approves, refund. That is about 9 nodes in 4 lanes.
- **Framing:** I recommend a happy path with the out-of-window and over-€200 branches beside it. The alternative is a full exception map, which costs a second board.
- **First glance:** the warehouse check, the point where the refund waits on another team. Second glance is the over-€200 check. Last glance is the refund.
- **Target:** I read "new board in the Fernhouse Product plan" together with your file key as a new section in the existing file `<draft-file-key>`. I won't create a new file, so the plan and the Barter drafts fallback don't come into play. I'll read the file once before the gate and name any section there that shares the title.

Left out:
- The carrier's `DAMAGED` tracking exception is a parcel flagged in transit, a different flow.
- Pallet items.
- Any self-serve path, because none exists.

Finding: no Fernhouse source describes damage handling. Photo proof, replacement versus refund and who pays return carriage appear nowhere in `context/`, so none of them are drawn. The board shows today's returns flow with damage as the reason. The "damaged-item refund" runbook in the packet's examples is a labelled fictional fixture, so I didn't use it as a source.

Unless you correct a row, I'll model it, run the check and bring the write gate next. The board is written only after your yes to that gate.