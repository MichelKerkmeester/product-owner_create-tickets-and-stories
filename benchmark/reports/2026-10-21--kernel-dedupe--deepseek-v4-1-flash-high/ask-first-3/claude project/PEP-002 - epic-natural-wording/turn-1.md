```markdown
# Epic - Platform - Offline mode - Clarification

* * *
## Settled from Oskar's brief
* * *
The brief supplies the Problem, the Goal, the platforms, the four areas and the Out of scope list. It also gives the Q1 2027 target, the two success measures and the 2026-10-09 conflict-handling decision. Web is out of scope and the Epic shape is settled, so two decisions are left.
####   
## Split of the child stories
* * *
**Oskar's four areas.** Offline reading, offline editing and creation, sync on reconnect and the offline indicator with storage settings.
**One story per platform.** iOS, Android and Desktop, each covering all four areas.

**Recommended: Oskar's four areas.**
*   The brief's dependency cuts by capability, so offline reading and the indicator can start before Joana's decision
*   One story per platform leaves all three stories blocked on that 2026-10-09 date
*   Desktop runs the web client in a native window, so Desktop work lands in the web client while browser tabs stay excluded
*   The shared limits of 500 pages, 1 GB and 30 seconds would be restated in every platform story
####   
## Delivery section
* * *
**Recommended: include one.**

The brief's four Out of scope items have no other home in the Epic shape. The 2026-10-09 conflict-handling decision belongs in Rabbit holes as the open question behind two of the four areas. Estimation stays `TBD...`.
* * *
```

Export-equivalent path: `export/NNN - Epic-offline-mode-clarification.md`
HVR self-scan: 1 hard blocker. Fixed: Oxford comma in the four-area list. Kept with reason: `TBD...` as the house Delivery placeholder.
Quality: not scored, clarification only | Kind: Epic | Energy: Standard

The question has two parts: how the child stories split and whether the Epic carries a Delivery section. I recommend Oskar's four areas, because the brief's dependency cuts by capability while one story per platform would put all three behind Joana's 2026-10-09 decision. The Epic comes next once you answer.

### Open items
1. **Epic title segment**
   - **Situation:** I used `Epic - Platform - Offline mode`, following the `Epic - Platform - ...` pattern the Loomlist context gives for cross-surface initiatives, because this work spans three clients rather than one persona
   - **Open:** Confirm `Platform`, or name a different segment such as `Member`
2. **Conflict handling placement**
   - **Situation:** I read Joana's 2026-10-09 decision as sitting inside the sync on reconnect area rather than as a child story of its own
   - **Open:** Confirm that reading, or ask for a separate decision story in the Scope

Answer in one message and I'll draft the Epic.