```markdown
# Epic - Offline mode - clarification

* * *
## Unresolved decisions
* * *

**1. How the child stories split**
* * *
The brief already shows four areas and the order they can start in: offline reading and the offline indicator run now, while offline editing and sync on reconnect wait on Joana's conflict decision of 2026-10-09. All four areas land on iOS, Android and Desktop.

*   **Option A, recommended:** one child story per area, four in total, each naming the three platforms it covers. His areas carry the dependency order, while a per-platform split writes the same behavior three times over
*   **Option B:** one child story per platform and area, which suits a delivery where iOS, Android and Desktop diverge. The brief shows no such divergence, and Desktop wraps the web client rather than carrying its own logic
*   **Option C:** areas as child stories, with extra platform stories only where Desktop behaves differently. This needs a reason to exist, and the brief gives none
*   **Answer:** A, B or C, or name the split you want

**2. Whether the Epic carries a Delivery section**
* * *
The brief supplies four out-of-scope items, Web, choosing which pages to keep offline, searching pages that are not on the device, and offline access in the Support console. It also supplies one undecided dependency, and neither fits Scope or the release criteria.

*   Recommended: yes. No-gos takes the four exclusions, and Rabbit holes takes the conflict-handling decision with its 2026-10-09 date
*   **Answer:** yes or no

##   
```

Export-equivalent path: `export/001 - Epic-offline-mode-clarification.md`
HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.
Quality: not scored, clarification only | Kind: Epic | Energy: Standard

The Epic itself is one draft away, because the brief covers the problem, the goal, the platforms, the target and both release measures. What the Scope section cannot be written without is the child-story split, so the question asks that and the Delivery treatment in one round. Everything else in the brief is settled and ready to draft.

### Open items
1. **Title segment**
   - **Situation:** The work spans iOS, Android and Desktop, so I plan `# Epic - Platform - Offline mode` rather than a persona segment
   - **Open:** Confirm `Platform` or name the segment you would search for
2. **Conflict dependency**
   - **Situation:** I read Joana's decision as an internal dependency inside the areas it blocks, not as an external dependency in Delivery
   - **Open:** Strike that reading if the Sync team should appear as an external blocker

Answer in one message and I'll draft the Epic.