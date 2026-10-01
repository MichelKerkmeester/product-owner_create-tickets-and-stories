No Canvas panel is attached to this session, so the Deliverable Block is rendered here as a fenced block.

```markdown
# Epic - Platform - Offline mode - clarification

* * *
I'll draft the offline mode epic from Oskar's brief. Four decisions are open, and the first one sets the structure of `## Scope`:

**Child-story split:**
- Oskar's four areas, one child story each: offline reading, offline editing and creation, sync on reconnect, offline indicator and storage settings
- One child story per platform: iOS, Android, Desktop
- A hybrid, keeping the four area groups and naming the per-platform work inside each
- Roughly how many child stories do you expect, and should each be written in `{Persona or platform} - {Area} - {Feature}` shape

**The Sync dependency:**
- Name the offline editing and creation and sync on reconnect stories now, with Joana's conflict-handling decision of 2026-10-09 carried as an open point
- Hold those two areas back and let the first release cover offline reading and the indicator only

**Delivery view:**
- Include the optional `## Delivery` close, with estimation, rabbit holes and no-gos
- End the epic on acceptance criteria

**Links:**
- Any Figma, brief or ClickUp links to carry into `#### **References**`
- With none supplied, that section is omitted rather than left empty

**Validation:**
What am I likely to assume incorrectly about the split, the platform boundary, or which work this epic owns?
```

`Export-equivalent path: export/001 - Epic-offline-mode-clarification.md`

Quality status: parked at the Story intake gate. Artifact kind resolves cleanly to an Epic from your framing and the brief, and the child-story set is the one field that decides `## Scope`, so nothing is drafted until you settle it. The two candidate splits give different child-story counts and different Scope groups, which is why the question comes before the artifact rather than inside it.

`HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: iOS, Android, Desktop and estimation, rabbit holes, no-gos are fixed by the product's surfaces and the house template rather than authoring choices.`

The brief and the product context cover everything else the epic needs: Problem, Goal, Solution direction, the platform boundary of iOS, Android and Desktop, the Q1 2027 target, the two success measures that become release-level acceptance criteria, and the four exclusions for no-gos. Answer the open points and the epic follows as a new deliverable in this lane.