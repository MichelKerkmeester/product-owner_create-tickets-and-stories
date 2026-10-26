Before I draw anything, this is how I read the request. Nothing is written to FigJam yet.

**Question:** which Loomlist offline mode work runs when, and what holds the release?
**Outcome:** a reader sees the order of the work, the critical path and the date the release lands.
**Reader:** assumed to be the people in the Loomlist Product plan, with a mixed audience, balanced detail and a laptop reading distance. Naming a different reader settles it.
**Type:** gantt. A list would lose the overlap between the sync engine and the conflict screen work, and the point where integration waits on both.

The dates below follow from your start and durations. Release is the only date you didn't state, so check it.

| Task | After | Starts | Ends | Length |
|---|---|---|---|---|
| Conflict screen design | none | 2 Nov 2026 | 16 Nov | 2 weeks |
| Sync engine | none | 2 Nov 2026 | 23 Nov | 3 weeks |
| Conflict screen build | design | 16 Nov | 30 Nov | 2 weeks |
| Desktop and iOS integration | sync engine and screen build | 30 Nov | 7 Dec | 1 week |
| Beta for 5 percent of workspaces | integration | 7 Dec | 21 Dec | 2 weeks |
| Release (milestone) | beta | 21 Dec 2026 | none | none |

**Settled by your message:** every row above, as approved direction. I read that class from your "not yet approved" on Android. Tell me if the core plan is still a draft.

**Left out:** Android in the next quarter. It is a proposal with no start or length, and a gantt row needs both. I won't estimate them. The board's source line will name it as not yet approved, so nothing implies it is committed.

**Finding:** the sync engine ends on 23 Nov, a week before the screen build. It carries a week of slack, so the path into integration runs through design and the screen build. You called integration the critical path.

**Recommended answers (they stand as assumed if you don't change them):**
* What the board must not do: show Android as approved or dated, so it gets no bar and no date
* Critical tag: Integration only, as you said, with nothing tagged active because no work starts before 2 Nov
* Framing: one axis in three sections (Design, Build, Launch) with arrows for each dependency. This shows the slack and the join at integration. The alternative is a milestones-only view of the beta and release, which is shorter but hides both
* Title: "Offline mode launch", with the first glance on Integration

If you'd rather show the whole chain, I'd tag design, screen build and integration and leave the sync engine plain.

Is this the right reading of the board?