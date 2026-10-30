Round 1 of 3. Your message settles the type and the dates, so I only need the reader, the dials and one scope call before I model it.

**Replay of what is settled**
* Type: one gantt chart, written as a new section in the existing Loomlist Product plan file `<test-file-key>`, with nothing already on the file changed (captured)
* Tasks: conflict screen design 2 Nov 2026 for two weeks, sync engine 2 Nov for three weeks, conflict screen build after the design for two weeks, desktop and iOS integration after both builds for one week, beta for 5 percent of workspaces for two weeks, then the release (captured)
* Dates worked out from your durations: design ends 16 Nov, sync ends 23 Nov, screen build ends 30 Nov, integration ends 7 Dec, beta ends 21 Dec, so the release lands 21 Dec (derived, not estimated)
* Plan facts: design covers the merge view and the undo banner, the platform team owns the sync engine, integration covers desktop and iOS only (captured). I plan to carry the owner and the platform scope in the task names and the design scope in the subtitle (assumed)

**Question 1: the reader**
Reading: no source names who reads the board
Question: who is it for, and what should they be able to decide after reading it?
Recommended: the Loomlist product and engineering leads, asking "which tasks are active when, and what gates the release?", so they can see the build chain that sets the release date
Why: the plan is a launch plan and the question picks which bar the first glance lands on

**Question 2: the dials**
Reading: nothing in the request sets a detail level, an audience or a reading distance
Question: which settings should the board use?
Recommended: Balanced detail, Mixed audience, Laptop distance
Why: it is a seven-bar plan read by a small team at their desks, so the defaults fit

**Question 3: what the board must not do**
Reading: Android is "next quarter, not yet approved", so it has no date and is a proposal. By the dates, the longest chain runs design, screen build, integration, beta, release, and the sync engine has one week of slack. You called integration the critical path, but the beta and the release also sit on that chain
Question: should the board keep Android off the chart and mark only the chain up to integration as critical?
Recommended: keep Android off the chart and name it under `Left out:` as an unapproved proposal. Mark design, screen build and integration as critical and leave the beta and the release untagged
Why: a bar with no date would mean inventing one, and tagging every bar critical would make none of them stand out

Take the recommended answers, or correct any of them?