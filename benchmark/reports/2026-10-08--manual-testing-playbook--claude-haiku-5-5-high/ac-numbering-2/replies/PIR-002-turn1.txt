```markdown
# Clarification: wishlist lost on device change

Your request names both `$bug` and `$story`, so I have not drafted anything yet. The sources also show that the product decision is still open, so I need your answers in one response.

**0. How should I work this?**
- Quick - lean pass with smart defaults and minimal back-and-forth
- Deeper - take more time, read more context and apply the full phase flow

**1. Artifact:** Which should I write?
- Bug - the app or web breaks behavior that is already agreed
- Story - a PRD for changing how the wishlist works
- Epic - the change spans the app and web and needs child stories

**2. Product decision:** Should the app wishlist change? Teun (2026-09-22) confirmed the apps save it on the device by design, and Lotte has not decided whether that changes.
- Stay on the device, and change how agents explain it
- Save to the account, as web does, so the list follows the customer across devices
- Something else (describe it)

**3. Bug evidence (if Bug):** The sources contain no reproduction steps, and none says the app ever kept a list across a device change. Did it ever do so, and in which build did that stop?

**4. Scope and value:** Which customers does this serve: guest, signed in or both? What should they be able to do after the change? For a Story, this becomes the role and the value.

**5. Two-list cases:** The 39 contacts who reached the 50-item limit had a list on web and a second list in the app. Are they in scope?

**6. Sources:** I plan to use the Fernhouse company context (2026-09-18), Maud's contact summary (2026-09-21) and Teun's reply. Is any other source authoritative, such as a decision note from Lotte?

**7. Assumptions to challenge:** I am assuming the 412 contacts describe real data loss, not only the two-list confusion behind the 39 limit cases. Is that right?

Answer all parts in one reply. The artifact follows once you answer.
```

Export-equivalent path: `export/NNN - intake-wishlist-device-change-clarification.md`

This is a clarification only. The artifact comes next, once you answer.

The request has `$bug` and `$story` together, so I asked one consolidated question and drafted nothing. Lotte has not decided whether the app wishlist should move to the account, and Bug or Story depends on that answer. Question 2 is the blocking one.

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.