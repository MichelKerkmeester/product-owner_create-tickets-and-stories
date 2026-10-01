```markdown
<!-- Product Owner · Story Mode · Epic shape · intake clarification -->

**Requested deliverable:** a new Epic in the Barter house format, built from Oskar's brief. Nothing is drafted yet.

**1. The child-story split, which you flagged as unsettled.** This decides `## Scope`, so it is the one thing I cannot pick for you.
- Oskar's four areas: offline reading, offline editing and creation, sync on reconnect, offline indicator and storage settings
- One story per platform: iOS, Android, Desktop
- The four areas as scope groups, each holding a platform-level story where the platforms differ

Each cost is real. An area split keeps the shared behavior in one story per area, and that story then ships on three platforms. A platform split gives each team a story it can deliver alone, and repeats the shared behavior in each. Say which one, and if the answer is mixed, which parts follow which.

**2. The pending sync decision.** Joana decides conflict handling on 2026-10-09, and the brief says offline editing and creation and sync on reconnect cannot be finalised until then.
- Name both child stories now, carrying the dependency as an open item
- Name offline reading and the indicator only, and add the other two once the decision lands

If the conflict-handling story should name the options under discussion, send the `#sync-eng` thread, because the brief does not carry them.

**3. Desktop against Web.** The product context says Desktop wraps the web client and takes whatever build Web runs that day, with no Desktop release, and the brief rules Web out because a browser tab cannot keep a local copy between visits.
- Desktop in scope means the web client gains offline support and Desktop inherits it
- Desktop needs an offline path of its own

This decides whether a per-platform split can treat Desktop as one story.

**4. The delivery view.** `## Delivery`, holding Estimation, Rabbit holes and No-gos, is opt-in on a new Epic.
- Write it, with every unknown left as `TBD...` and the sync dependency visible there
- Leave it out, and end the Epic on its release-level acceptance criteria

**5. What I should not assume.** Oskar's brief is my only source for offline behavior. Tell me what I would get wrong from the brief alone, and whether the two measures under "How we will know it works" belong in the Goal or in the release-level acceptance criteria.
```

**Export-equivalent path:** `export/001 - Epic-offline-mode-clarification.md`

**Artifact kind:** Epic, selected by your "write an epic for offline mode" framing. Drafting is held until the five decisions land, because the child-story split is what `## Scope` is made of.

**Quality status:** Shape fit pass, Epic shape resolved and no Requirements section planned. Intake clarity pass, one consolidated question rather than a second round. House format pass, markdown dashes and no bullet ending on a full stop. Waiting, no draft produced.

**HVR self-scan:** 0 hard blockers. Fixed: none required. Kept with reason: `TBD...` is the fixed house Delivery placeholder rather than a prose ellipsis, and `finalised` preserves Oskar's own wording.

**Assumptions to strike if wrong:** I would title the Epic `# Epic - Platform - Offline mode`, using the sanctioned cross-surface value because the work lands on iOS, Android and Desktop together. I read Oskar's brief as the only source, so the `#sync-eng` options for conflict handling are absent until you send them. I read the two measures as measurement signals that sit in the Goal rather than as release-level criteria, which item 5 asks you to confirm.

**Next step:** answer the five items in one reply, and the Epic comes next as a fresh Deliverable Block in this lane.