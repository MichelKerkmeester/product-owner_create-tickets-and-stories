<figma-url>
Read-back: 4 of 4 states plus the start and end dots, 6 of 6 transitions, 5 of 5 labelled transitions, labels read visually, first glance: the refund or store credit choice
Left out: back and cancel moves, the request states none. The reason list, refund timing and the 30-day return window, not in the request.
HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.

I took "use your recommendation" as a yes to the gate, so I wrote the board as planned. It's a new section in the existing file, placed to the right of the existing content. The write returned no warnings. Node and connector counts matched the model (6 nodes, 6 connectors). Both transitions into Confirmation exist, joining the same two states.

**Findings from the screenshot**
* **"choose refund" connector:** its arc rises from the middle of the "choose store credit" line, so it can read as branching off that line instead of leaving "Refund or store credit". The composer lets two moves between the same pair of states share a start point. Fix: give the confirmation two states, one for refund and one for store credit. That adds a state, and the request mentions only one confirmation.
* **Subtitle:** it wraps and leaves "flow" alone on the second line. Fix: shorten it, for example "The states a customer passes through when starting a return, drawn as a proposed self-serve flow".

Both fixes mean recomposing the board and then deleting the old section, each with its own yes. I've changed nothing on the board.

**Assumptions I'm still carrying**
* **Reader:** Post-purchase and Storefront, agreeing the flow before stories are written.
* **Status:** the subtitle says "proposed self-serve flow", because the Fernhouse context says there is no self-serve return today. If it's approved direction, I'll change the subtitle.

**Rollback:** delete board section 58:2830. I'll do that only after your separate yes.

Do you want me to recompose with the two fixes?