```markdown
I'll draft the Epic for offline mode. Oskar's brief settles the Problem, the Goal, the four areas, the platforms, the Q1 2027 target and two release outcomes, so these are the only decisions I need in one response before drafting:

**Child story split, the blocking one:**
- Four child stories, one per area Oskar names: offline reading, offline editing and creation, sync on reconnect, offline indicator and storage settings
- One set per platform, so three groups under iOS, Android and Desktop
- Four areas split per platform inside each area, which follows how task titles carry one platform
- Say if you want it framed differently, because this decides how Scope is grouped and how many stories the Epic commits to

**Desktop as a story of its own:**
- The product context says Desktop wraps the web client, adds only the capture shortcut, and picks up a web-client change the next time Desktop loads, with no Desktop release
- A Desktop story therefore ships on a Web build rather than a Desktop release
- Should Desktop carry its own child story, or ride the shared client while the Epic claims the surface

**Conflict handling, which is not settled:**
- Joana decides how sync-service resolves conflicting edits on 2026-10-09, and offline editing and creation and sync on reconnect cannot be finalised before that lands
- Option A: carry it as an `**Open:**` line under those two areas, repeat the question in Rabbit holes and add an `#### External dependencies` entry dated `TBD...`
- Option B: hold the whole Epic until the decision lands, which also delays offline reading and the indicator, the two areas the brief says can start first

**Delivery section:**
- Whether to add Estimation, Rabbit holes and No-gos, since the open conflict decision forces the section in even without a request
- Whether the brief's Out of scope list becomes the No-gos as written: Web, choosing which pages to keep offline, searching pages the device does not hold, Support console

**Title:**
- `# Epic - Member - Offline mode`, taking the persona the Goal names
- Or a surface segment such as `# Epic - Mobile - Offline mode`, given iOS, Android and Desktop ship it and Web does not

**References:**
- Links for the brief, the `#sync-eng` thread, Marta's `lost-edit` tickets or a design, or I omit References entirely, because it never holds an invented link

**Validation:**
- What am I likely to assume incorrectly about the four areas
- Does the team read all four areas as one release, or does the Q1 2027 target only bind the two that do not depend on Joana
```

Export-equivalent path: `export/001 - Epic-offline-mode-clarification.md`

HVR self-scan: 0 hard blockers. Fixed: none needed. Kept with reason: `**Open:**`, `#### External dependencies` and `TBD...`, the fixed Epic-lane tokens, plus `#sync-eng`, `lost-edit` and `# Epic - Member - Offline mode` as preserved identifiers and literal title forms.

Artifact kind: Epic, confirmed by "write an epic" and by the brief carrying no requirements of its own, only four areas that delegate to child stories. No artifact is drafted this turn because the child-story split is the one thing you called unsettled, and it decides the whole `## Scope` section.

Two things I noticed while reading both files, so you can strike them if you disagree. First, Desktop is not a release lane in the usual sense, which is why the per-platform split needs your call rather than mine. Second, the brief's dependency and its Q1 2027 target may bind different sets of areas, since offline reading and the indicator can start before 2026-10-09 and the other two cannot.

Answer the fields above and the Epic comes next, with the release-level acceptance criteria built from the two outcomes the brief already states.