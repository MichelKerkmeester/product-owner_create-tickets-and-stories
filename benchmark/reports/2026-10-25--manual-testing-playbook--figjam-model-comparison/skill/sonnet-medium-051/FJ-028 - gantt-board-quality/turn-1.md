Round one of the intake, before I model anything. Nothing is written to the board yet.

What your request settles so far:
* Type: gantt, which fits "which tasks are active when"
* Target: a new section in FigJam file <test-file-key> in the Loomlist Product plan, so "new board" means a section beside what the file already holds, and nothing already on it changes
* Chain: design 2 weeks, sync engine 3 weeks, conflict screen build 2 weeks after design, integration 1 week after both builds, beta 2 weeks, release
* Anchor: design and sync engine both start 2 November 2026
* Dates (assumed): these durations put the release on 21 December 2026, counting calendar weeks with no holiday gaps, because the FigJam gantt cannot skip weekends or holidays
* Left open: Android, unapproved and undated

**1. Reader, question and outcome**
Reading: no reader is named. The board answers "which tasks are active when, and what gates the release".
Question: Who reads it, and what should they decide afterwards?
Recommended: product and engineering leads in the Loomlist Product plan, deciding whether the plan and the release date hold
Why: the chain and the critical path are what they would challenge first

**2. What the board must not do, and the critical tag**
Reading: Android has no start date or duration and is not approved, and a gantt bar needs a start. You named integration as the critical path. By the dates, the sync engine ends 23 November and the build ends 30 November, so the sync engine has one week of slack. Design and build sit on the same chain as integration.
Question: What must the board not show, and which bars carry the critical tag?
Recommended: no Android bar, with Android named under Left out as an unapproved proposal, and the critical tag on integration alone, as you said it
Why: a dateless bar would be an invented date, and the tag follows your word instead of my reading of the chain

**3. Detail level, audience and reading distance**
Reading: no reader is named, so I read an internal planning audience at a laptop. The chart is five bars and one milestone.
Question: Which detail level, audience and distance?
Recommended: Balanced, Mixed, Laptop
Why: five bars and a milestone fit a laptop read, and a mixed audience gets plain task names

Take the recommended answers, or correct any of them?