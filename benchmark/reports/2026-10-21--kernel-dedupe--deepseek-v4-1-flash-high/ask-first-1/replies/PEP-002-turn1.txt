```markdown
# Epic - Offline mode - open questions before drafting

* * *
Four points stand between Oskar's brief and the draft. Each one opens with what the brief and the product context already show, then the answer I recommend and why.

## 1. Child story split

- **Sources show:** The brief names four areas: offline reading, offline editing and creation, sync on reconnect, offline indicator and storage settings
- **Sources show:** Each of the four runs on iOS, Android and Desktop
- **Recommended:** The four areas as the story spine, with each story's iOS, Android and Desktop work as tasks inside it
- **Reason:** Joana's conflict decision splits along the same four areas, so reading and the indicator can start first
- **Reason:** A per-platform split would put the undecided conflict work into three separate stories
- **Other option:** Twelve stories, one per area per platform, each naming its platform and release

## 2. Desktop in scope

- **Sources show:** The brief puts Desktop in scope and keeps Web out, because a browser tab cannot keep a local copy between visits
- **Sources show:** The product context says Desktop wraps the web client in a native window and adds only a capture shortcut
- **Sources show:** A web client change reaches Desktop users with no Desktop release
- **Recommended:** Keep Desktop in scope as the brief states, and treat offline support there as a Desktop shell capability rather than a web client one
- **Reason:** The brief's own reason for excluding Web otherwise undercuts Desktop
- **Other option:** Drop Desktop from the Epic and cover iOS and Android only

## 3. Joana's decision and the exclusions

- **Sources show:** Joana decides conflict handling on 2026-10-09, and offline editing and sync on reconnect cannot be finalised before then
- **Sources show:** The brief excludes Web, choosing which pages to keep offline, searching pages not on the device and offline access in the Support console
- **Recommended:** Name the decision as a dated dependency in Scope and add the optional `## Delivery` close
- **Recommended:** Rabbit holes then carries the undecided conflict handling, and No-gos carries the four exclusions
- **Reason:** No-gos is the house section for an exclusion list, and an open decision reads best beside the estimate
- **Other option:** No Delivery close, with the dependency in Scope and the exclusions stated in About prose

## 4. Reading of the retention rule

- **Sources show:** The device keeps the 500 most recently opened pages with their blocks, inline databases and to-dos, capped at 1 GB, whichever comes first
- **Sources show:** Choosing which pages to keep offline is out of scope
- **Recommended:** Members get no pin or manual choice, so recency and the cap alone decide what stays
- **Reason:** The brief gives recency and the cap as the whole retention rule, so a member choice would be a second rule nobody supplied
- **Other option:** A member can keep a chosen page past both limits
```

Export-equivalent path: `export/001 - Epic-offline-mode-clarification.md`
HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.
Quality: not scored, clarification only | Kind: Epic | Energy: Standard

The kind is Epic rather than Story because the brief frames an initiative across child stories with a goal and no requirements of its own. Four points are open, and the split question is the one that decides the whole Scope section, so nothing is drafted until it is settled. The brief's evidence, the four areas, the two success measures and the Q1 2027 target all travel into the draft once these land.

### Open items
None identified

Answer in one message and I'll draft the Epic.