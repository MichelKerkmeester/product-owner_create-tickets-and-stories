**Path:** `export/002 - Epic-offline-mode.md`
`Verified: read-back succeeded; 149 lines`
`HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: `TBD...` in Estimation is the sanctioned Story Mode placeholder for an unknown size, and the template's fixed labels and the `**Open:**` line are house wording carried verbatim.`

**Quality summary**
- Kind: Epic (Story Mode, Epic shape). Split as you asked: four child stories, one per area from Oskar's brief, each covering iOS, Android and Desktop together.
- Completeness 9, Clarity 9, Actionability 8, Accuracy 9, Relevance 8, Mechanism Depth 8. Body 996 words, inside the 1,000-word Epic budget.
- Accuracy anchors: the `23%` and `31%` figures and the `lost-edit` / `#sync-eng` detail come from the brief's Problem section, `2026-10-09` and Joana's role from its Dependency section, and protocol v3 block-level last-writer-wins from the product context's Known constraints. Nothing in the artifact is unsourced.

**Summary**
The Epic frames offline mode as one initiative across iOS, Android and Desktop, splits it into the four child stories you chose, and keeps its criteria at release level so the children can carry their own detail. Four things I decided rather than asked, so you can strike or correct them: the title segment is `Platform` and the children are named `Member - Offline mode - {Area}` (Q2 went unanswered, so I used the house default), the Epic carries a `## Requirements` section even though the shape defaults to none because platform coverage, plan coverage and the Sync decision belong to no single child story, and `## Delivery` is present because the `**Open:**` line on Conflict handling forces it. Its size stays `TBD...`, and Estimation names the `Q1 2027` target.

Two hand-offs worth confirming. The per-area values stay out of the Epic by design, since requirements live in the children: `500` pages and the `1 GB` cap with images and files counting, plus eviction on the next connection, for Offline reading; the in-order queue and the online-only share, invite, move and delete actions with their controls unavailable offline for Offline editing and creation; the `30`-second upload window with oldest-first ordering for Sync on reconnect; and the top-bar marker, queued-change count and storage screen for the indicator story. Web is excluded in No-gos, alongside page selection, offline search and Support console access.

Next step is the four child stories. Say the word and I will draft them one at a time, or as a Story bundle if you want tasks attached. ClickUp delivery is available here, and it needs your explicit approval at that point.