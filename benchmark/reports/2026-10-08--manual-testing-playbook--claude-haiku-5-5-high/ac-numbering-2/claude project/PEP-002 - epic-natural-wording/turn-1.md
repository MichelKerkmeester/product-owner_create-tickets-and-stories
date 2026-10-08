```markdown
# Offline mode epic, clarification

I'll write the Epic from Oskar's brief. Before I draft, please answer these in one response:

**Child stories: four areas or per platform:** Should the four areas each be one child story with iOS, Android and Desktop as constraints, or should the stories split per platform? My read is the four areas, since the brief's dependency on Joana's decision splits by area, not by platform. Desktop wraps the web client, so a Desktop-only story may touch code Web also uses.

**Conflict handling:** Joana decides how sync-service resolves conflicting edits on 2026-10-09, and the options sit in #sync-eng, which I don't have. Should I wait for that decision before drafting the editing and sync stories, or draft now with those two stories marked open? Paste the thread if the options belong in Scope.

**Release criteria:** The brief's two measures are the no-connection screen share halving within 8 weeks and `lost-edit` tickets from dropped connections stopping. Should these be the Epic's release criteria, or should I add checks per area, such as the 500-page and 1 GB caps holding on device?

**Title:** Should the Epic read `Epic - Platform - Offline mode`, following the path pattern in the product context? Confirm, or name another path.
```

Export-equivalent path: `export/NNN - Epic-offline-mode-clarification.md`

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: `lost-edit` and #sync-eng, which are literal ticket and channel identifiers from the brief.

I haven't drafted the Epic yet. Your split question is one of several open decisions, and the brief says the editing and sync stories can't be finalised until Joana decides on 2026-10-09, which is tomorrow. Answer the four points above in one reply and I'll draft the Epic from there.