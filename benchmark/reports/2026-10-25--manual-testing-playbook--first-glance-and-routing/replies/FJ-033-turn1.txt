I've read the skill files and the Loomlist context. Two claims in your request clash with those sources, so this is the playback and nothing is written to the board yet.

**Question:** how does a block change travel from one Loomlist app to the others?
**Outcome:** leadership can see which parts carry a change from one device to the rest (assumed)
**Type:** architecture, because the question is about parts and how they connect. A sequence would answer the order of one sync instead.

**Settled by your request**
*   Desktop, web and iOS apps talk to the sync platform
*   The sync platform stores changes and reaches iPhones through Apple's push service, which the sources below contest

**Where the sources disagree with your request**
*   "Stores every change". The Loomlist context page (updated 2026-09-22) and the #sync-eng thread say protocol v3 is block-level last-writer-wins. The version that reaches the server last replaces the other, and the replaced edit is never written anywhere, page history included. Joana's conflict decision was due 2026-10-09, but the thread's pinned status is "not decided" and I have no record of the outcome.
*   "Wakes sleeping iPhones through Apple's push service". The context page says push goes out only for mentions, comment replies and shares, and that nothing else in the product sends push. iOS reminders are local notifications. Neither file describes sync waking a phone.

**Assumed**
*   Executive audience, so labels use capability words and your term "Sync Platform"
*   Laptop reading distance
*   An "Entry point" node between the apps and the platform, because the architecture layout needs a gateway lane there. It is named in capability words and marked assumed on the source line.

**Questions**
1. Which source governs the two claims?
   *   Recommended: the context page for current behavior. If the wake-up or the full change history is newer, send me the doc or the 10-09 decision and I'll draw from it with its status in the label.
   *   Why: a leadership board should not show a path the product does not run today.
   *   With no answer, the platform writes the latest version of each block, the Apple push node is left out, and both claims go under `Left out:`.
2. Should the board show Android?
   *   Recommended: draw the three apps you named and list Android under `Left out:`.
   *   Why: you named three apps, and the sources do not say how Android is woken.
3. What must the board not do?
   *   Recommended: no conflict-handling options and no offline mode plans, since both are undecided.

Is this the right reading of the board?