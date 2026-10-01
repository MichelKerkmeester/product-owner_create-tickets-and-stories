```markdown
# Epic - Platform - Offline mode - clarification

* * *
Before I draft the Epic from Oskar's brief, I need one response covering the unresolved points below.

**Child-story set:** should the Scope section list one child story per area Oskar names, or one per platform?
*   Oskar's four areas, one story each:
    *   Offline reading
    *   Offline editing and creation
    *   Sync on reconnect
    *   Offline indicator and storage settings
*   One story per platform: iOS, Android, Desktop
*   A mix, such as one story per area with the platform difference carried inside each one
*   Desktop wraps the web client in a native window, so a per-platform split treats Desktop differently from the two native apps

**Conflict handling:** Joana decides on 2026-10-09 between Option A, Option B and Option C in the #sync-eng thread, and protocol v3 stays as it is until then. Per Oskar's brief, offline editing and creation plus sync on reconnect cannot be finalised until that decision lands
*   Keep all four areas in this Epic, with the conflict decision carried as an open dependency
*   Cover offline reading and the offline indicator now, and take the other two areas once the decision lands

**Delivery view:** do you want `## Delivery` with Estimation, Rabbit holes and No-gos in the Epic? That is where the open conflict decision and the two-week spike it waits on would sit

**References:** the Epic carries supplied links only and omits that section when none are supplied. Is there a link for `Sync conflicts, options for v3 and after`, for Oskar's brief, or for the #sync-eng thread?

**Validation:** what am I likely to assume incorrectly about the four areas, the platforms or the release-level outcomes? Confirm whether Desktop offline means the web client working offline inside the native shell, since Web is out of scope
```

Export-equivalent path: `export/001 - Epic-offline-mode-clarification.md`

Artifact kind: **Epic** (Story Mode, Epic scaffold), held at the intake gate with no draft. The child-story set decides the Scope section, and you named it as unsettled, so drafting either grouping would pick a shape for you. The brief's own dependency is a second reason to stop: I read `context/loomlist-sync-conflict-thread.md`, which is pinned as not decided with Joana deciding on 2026-10-09 between Option A, Option B and Option C, so the brief's hold on two of the four areas still stands. The thread's support for Option B is not a decision, so nothing in the Epic treats it as one.

Assumptions behind the intake, for you to strike:
* The Epic H1 would use `Platform` as its persona segment, since the work spans iOS, Android and Desktop
* Release-level acceptance criteria would come from Oskar's "How we will know it works" measures, with the screen-level detail left to the child stories
* The four areas Oskar names would be used as written, in his own wording

Answer the five points in one message and the Epic follows as a new Deliverable Block in this lane.

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: `Sync conflicts, options for v3 and after` (supplied document name), `2026-10-09` (supplied decision date), `## Delivery` (house section name), Option A, Option B and Option C (supplied option labels).