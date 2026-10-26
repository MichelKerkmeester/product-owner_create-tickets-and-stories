This is intake round one, and nothing has been written to the board yet.

**Blocker: no Figma write tool is connected.** I searched the tools available this turn for `use_figma`, `get_figjam`, `whoami`, `create_new_file` and `generate_diagram`, and none are connected here. The `fj` route can't draw a gantt chart, so I can't write the board into `<draft-file-key>` until the Figma MCP connection is available. I can finish the intake and the model check now. The write then waits on the connection and on your yes at the gate.

**What I read from your request**

* **Target:** the existing file `<draft-file-key>`, with the board added as a new section beside what it holds and nothing already there touched. The Barter team plan drafts fallback applies only if that file can't be reached, so no plan or `create_new_file` call is planned
* **Type:** gantt, because the question is which work runs when
* **Dates:** I read "2 November" as 2026 from today's date. Durations are calendar weeks, with no weekend or holiday exclusions
  * Design: 2 Nov to 16 Nov
  * Sync engine: 2 Nov to 23 Nov
  * Conflict screen build: after design, 16 Nov to 30 Nov
  * Integration: after the sync engine and the screen build, so 30 Nov to 7 Dec, because the screen build ends later
  * Beta: 7 Dec to 21 Dec
  * Release: milestone on 21 Dec
* **Design:** I read this as the conflict screen design, since the screen build follows it. Marked assumed, and the label would say "Conflict screen design"

**Three questions**

1. **Reader and outcome**
   * Reading: your request names no reader or question
   * Recommended: the product and engineering team, asking which work runs when before the offline mode release and what Integration waits on. After reading, they can see the order, the dates and where the release lands (21 Dec)
   * Why: that is what the six tasks and their dependencies carry
2. **What the board must not do**
   * Reading: you named six items and their order
   * Recommended: no owners, no estimates, no beta size and nothing beyond those six items
   * Why: your request states none of those, and I won't invent them
3. **First glance**
   * Reading: you didn't say what holds the release, and the dates show that Integration waits on the screen build rather than the sync engine (30 Nov against 23 Nov)
   * Recommended: draw Integration as the focus and tag nothing `crit`
   * Why: tagging the whole path design, screen build, Integration, beta would mean every bar is critical, so none stands out. And you haven't named a critical path

Reply "yes" to take all three recommendations, or correct any of them. Your answer settles the reading and writes nothing, so the playback and the write gate each follow as their own message.