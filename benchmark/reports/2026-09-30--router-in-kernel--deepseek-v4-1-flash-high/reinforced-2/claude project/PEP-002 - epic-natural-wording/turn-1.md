```markdown
# Epic - Offline mode - clarification

I'll create the Epic from Oskar's brief. Before drafting, I need the unresolved decisions below in one response.

**1. Child-story split:** What do the Scope groups and the child-story titles follow?
- By area, one story each across all three surfaces: offline reading, offline editing and creation, sync on reconnect, offline indicator and storage settings
- By platform, one story each covering all four areas: iOS, Android and Desktop
- By layer, one shared queue and sync story plus one story per surface, if the surfaces share no implementation

What the supplied sources say that bears on the choice:
- Desktop wraps the web client and adds nothing beyond the capture shortcut, so Desktop changes arrive with the next web build
- iOS and Android ship every two weeks over a 7-day rollout, so mobile work and web client work run on different clocks
- Oskar shared the brief with the Sync, Mobile Platform and Web and Desktop teams, so either split crosses teams

**2. The fourth area:** If the four areas hold, does the offline indicator and storage settings stay one story?
- The brief carries the offline marker and the waiting-change count with the storage screen, as one area
- Keep that as one story, or split the indicator from the storage screen

**3. Scope grouping:** Release waves, or one group?
- Grouped by wave, offline reading and the indicator first, with the other two areas gated behind Joana's conflict-handling decision on 2026-10-09
- One flat group, leaving the dependency to the Delivery section

**4. Delivery view:** Write `## Delivery`, or end the Epic on Acceptance criteria?
- With Delivery, the brief's four exclusions get a No-gos home
- They are Web, choosing which pages stay offline, searching pages not kept on the device and offline access in the Support console
- With Delivery, Rabbit holes carries the undecided conflict handling and Estimation carries the Q1 2027 target or `TBD...`
- Without Delivery, no section holds those exclusions

**5. Success measures:** Where do the brief's two success measures land?
- Kept in the brief and out of the Epic, since the house shape has no measurement section
- Carried into the Epic as release-level outcomes, close to the brief's own wording

**6. Epic title:** Which segment?
- I read the path as `# Epic - Platform - Offline mode`, since the work lands on iOS, Android and Desktop rather than one surface
- Name a different segment if you want one
```

Export-equivalent path: `export/001 - Epic-offline-mode-clarification.md`

Artifact kind: Epic, new, held at the intake gate. The split you flagged decides the Scope groups and every child-story title, so nothing is drafted until you answer. Send the six items in one go and the Epic takes the next number in this lane.

Quality: question validated on clarity, completeness, assumption challenge and mechanism depth at Standard energy. No artifact body yet, so nothing else is scored.

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: the `TBD...` house Delivery placeholder, the `**N. Header:**` bold intake labels the Interactive templates require, and the two three-item lists in item 1, each of which is supplied content rather than a count I chose.

Assumptions I am working from, so you can correct one: the brief governs content and the context page supplies product facts behind it, this is a new Epic rather than a refinement of an existing artifact, Joana's 2026-10-09 decision stays a dependency rather than a blocker, and the Web and Desktop team the brief names is absent from the context page's team table, which changes nothing in the Epic itself.