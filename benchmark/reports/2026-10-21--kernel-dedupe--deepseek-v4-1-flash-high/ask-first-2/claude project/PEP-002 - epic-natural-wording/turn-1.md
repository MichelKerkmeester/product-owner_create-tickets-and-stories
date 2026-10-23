```markdown
# Epic - Platform - Offline mode - clarification

Two decisions change the Epic itself, so I need them before drafting.

**1. Child-story split**
The brief names four areas and three platforms, and it already separates the areas by what can start before Joana's conflict decision lands.

My recommendation: one child story per area, four in all, with the per-platform work as tasks inside each.
- Reason: the dependency line already splits the areas by start date, so a per-platform split repeats the same sync work in three places
- A per-platform split gives twelve child stories and hides that conflict handling blocks two of the four areas on every platform
- Choose per platform and I will name the twelve in Scope, grouped by platform

**2. Desktop, given Web is out of scope**
The brief puts Desktop in scope and Web out. The product context says Desktop wraps the web client and adds nothing beyond the capture shortcut, so offline on Desktop needs the web client to keep the local copy and the queue.

My recommendation: count the web client's offline work as in scope where Desktop needs it, and leave the browser tab out.
- Reason: it is the only reading where Desktop ships offline without a second client
- The alternative is a Desktop-only store and queue that the web client never gets, which is new work on a client that has none today
- Tell me which team owns that work, because it decides whether a child story spans platforms
```

Export-equivalent path: `export/NNN - Epic-offline-mode-clarification.md`
HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.
Quality: not scored, clarification only | Kind: Epic | Energy: Standard

The brief supplies the Problem, Goal, platforms, scope, dependency, target and success measures, so the Epic body is ready to write. What it does not settle is how the child stories group, and that is what fills `## Scope` with names rather than guesses. The second question is the one conflict between the brief and the product context that no source resolves.

### Open items
1. **Epic title segment**
   - **Situation:** The work spans iOS, Android and Desktop, so the H1 uses `Epic - Platform - Offline mode`
   - **Open:** Say if you would rather name Mobile, or list the three surfaces

Answer in one message and I'll draft the Epic.