```markdown
# Epic clarification - Offline mode

I'll write the Epic from Oskar's brief and the Loomlist product context. Before drafting, I need the unresolved decisions below in one response:

**1. How the child stories split**
The split decides the whole `## Scope` section:
- Four stories, one per area Oskar names: offline reading, offline editing and creation, sync on reconnect, the offline indicator and storage settings
- Three stories, one per platform (iOS, Android, Desktop), each covering all four areas
- A hybrid: one `## Scope` group per area, with a platform story inside each

Confirm also whether the child stories should be named as plain text in `## Scope` or drafted as Story artifacts alongside the Epic.

**2. How the Epic carries the sync conflict-handling decision**
Oskar's brief leaves conflict handling to Joana on 2026-10-09, and two of the four areas cannot be finalised before it lands:
- State the decision as a blocking dependency in the Epic, and write release-level acceptance criteria for all four areas
- Hold the two dependent areas (offline editing and creation, sync on reconnect) as named placeholders in `## Scope`, and write release-level criteria for the two that can start first

**3. Links for `#### **References**`**
The brief points at the `#sync-eng` thread, Marta's `lost-edit` tickets and the April to August cancellation survey, with no URLs:
- Send the links that belong in `#### **References**`, or I will omit the section rather than invent one
```

Export-equivalent path: `export/001 - Epic-offline-mode-clarification.md`

Routed artifact kind: **Epic** (Oskar's four areas are an initiative split across child stories, so it is not a Story). I did not draft it, because the child-story set is the one decision you flagged as unsettled, and the Epic's `## Scope` is built from exactly that set. Writing it now would mean choosing your split and your dependency handling for you.

Quality status: this is the question-only block, so no artifact gates run yet. The block holds the three open items and nothing else, with source identifiers (`#sync-eng`, `lost-edit`, `2026-10-09`) preserved exactly.

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: the hyphen in the title separator, which is the house topic-title shape.

Additions of mine to strike if they do not fit: the per-platform and hybrid split options, and the second option under item 2. Both are choices I am offering rather than anything the brief states.

What I read as settled from the sources: Web out of scope and Desktop in, all four areas for Q1 2027, and the success measures as release-level outcomes.

Reply with the split and the other two answers, and the Epic comes next.