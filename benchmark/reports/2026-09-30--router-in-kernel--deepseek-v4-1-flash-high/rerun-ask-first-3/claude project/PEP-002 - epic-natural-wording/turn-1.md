I've read the brief and the product context. Oskar's brief supplies the problem, the goal, the platforms, the four areas, the target and the success measures, but it does not name a child-story set, and you've said the split is still open. That decides the Scope of the epic, so I've rendered the one consolidated question rather than a draft.

# Epic - Platform - Offline mode - Clarification

* * *
I'll draft the offline mode epic from Oskar's brief of 2026-09-23. The brief supplies the problem, the goal, the platforms, the four areas of scope, the target and the two success measures, so the decisions below are all that stand between it and a draft.
* * *
## Child story split
* * *
Oskar's four areas are offline reading, offline editing and creation, sync on reconnect, and the offline indicator with storage settings. Choose the split the `## Scope` section should carry:
*   One child story per area, four in total
*   One child story per area on each of iOS, Android and Desktop, twelve in total
*   A mix, where the areas that touch one client split per platform and the shared sync work stays one story
* * *
## Delivery view
* * *
The brief's Out of scope list and Joana's conflict-handling decision of 2026-10-09 both need a home in the artifact. Tell me which you want:
*   Include the optional `## Delivery` section, with the exclusions in No-gos, the conflict handling in Rabbit holes and Estimation left `TBD...`
*   Leave `## Delivery` out, and carry the exclusions and Oskar's ordering into the About prose instead
* * *
## References
* * *
The brief supplies no links, so `#### **References**` stays out of the epic. Send a design file or the #sync-eng thread if the epic should point at one
* * *

Export-equivalent path: `export/[NNN] - Epic-offline-mode-clarification.md`

HVR self-scan: 0 hard blockers. Fixed: nothing needed. Kept with reason: the `TBD...` token in the Delivery option, which is the fixed house placeholder for an unsized estimate, and `[NNN]`, the number the human reconciles on save.

Quality: clarification only, so the six floors are not scored. Nothing is drafted, and no answer to either question is assumed.

The epic is waiting on two answers. Once they land I'll draft `## Scope` against the split you pick, keep the release-level acceptance criteria at release altitude (the no-connection-session drop and the `lost-edit` tickets), and leave the hard values (the 500 pages, the 1 GB cap, the 30 seconds) in the child stories where they belong. Two things worth weighing while you answer: Joana's 2026-10-09 decision gates the offline editing and sync stories, so whichever split you choose has to leave those two separable, and the brief's four areas map onto two teams, Sync and Mobile Platform, which a per-platform split would spread across both. I'll title the epic `Epic - Platform - Offline mode`, since the work spans iOS, Android and Desktop rather than one persona, and I'll drop that segment if you'd rather it carried a role.