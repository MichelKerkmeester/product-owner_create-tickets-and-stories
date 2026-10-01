```markdown
I'll create the Epic from Oskar's brief. One open decision changes how `## Scope` groups the child stories, so I need it before drafting.

**1. Child stories:**
The brief names four areas, and your two options are the two ways `## Scope` can group them.
- By area: Offline reading, Offline editing and creation, Sync on reconnect, Offline indicator and storage settings
- By platform: iOS, Android, Desktop
- If it is by platform, does each story own all four areas on that platform, or only the parts that differ there?

**2. Desktop conflict:**
The product context says Desktop wraps the web client, takes its changes with no Desktop release and adds nothing of its own beyond the capture shortcut. The brief rules Web out.
- A Desktop child story built through the web client reaches Web too, and one built only in the native shell contradicts that context
- Which constraint wins, and who owns the Desktop work?

**3. Optional, for the Epic's sections:**
- Say if you want `## Delivery`, and I will hold Estimation, Rabbit holes and No-gos for it
- Any links belong in `#### **References**`, which I omit while none are supplied

**4. Sync dependency:**
Joana settles conflict handling on 2026-10-09, and it gates Offline editing and creation and Sync on reconnect.
- Should the Epic carry that gate in `## Scope`, or leave it with the child stories it blocks?

**5. What I should not assume:**
- What am I likely to get wrong about this split, or about what the brief already settles?
```

Export-equivalent path: `export/NNN - Epic-offline-mode-clarification.md`

Artifact kind: Epic, since Oskar's brief is an initiative split across child stories with a goal and no requirements of its own. This block holds the question only, because the child-story split you raised is unfixed and it decides how `## Scope` is grouped. No epics drafted yet, and the epic comes next once you answer the five points.

Quality: shape fit pass, Clarity pass, Completeness attention on the one field I cannot resolve from the brief.

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: Oskar's four area labels as he wrote them, the three platform names and the three Delivery slots, each fixed by the product context or the house template.

Summary: the brief settles the problem, the goal, the platforms, the four areas, the storage cap, the sync behaviour, the target and both success measures, so none of that needs asking. What it leaves open for the Epic's structure is the child-story set, the Desktop constraint in the product context, and where Joana's 2026-10-09 decision shows up.