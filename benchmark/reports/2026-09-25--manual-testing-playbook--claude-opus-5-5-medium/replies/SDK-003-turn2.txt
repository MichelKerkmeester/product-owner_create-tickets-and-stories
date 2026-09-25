I've written the proposal for the Sync and Mobile engineers and Marta to read before Joana decides on 2026-10-09. It covers all three options with their cost and trade-offs, and says where each person in the thread landed.

Path: `export/002 - doc-sync-conflict-options.md`
Verified: read-back succeeded; 149 lines
HVR self-scan: 0 hard blockers. Fixed: two commas before "and" in two-item lists, one awkward sentence about Oskar. Kept with reason: em dashes in the `*   **Term** — definition` bullets and the `Status: … — …` labels, which are the two sanctioned ClickUp shapes.

**Quality summary**
- **Source safety:** pass. How v3 behaves today is labelled current, the three options are labelled as proposals, and Joana's interim plan is labelled as her stated direction rather than a decision. Every figure and cost estimate names the person who gave it
- **Shape fit:** pass. It follows the proposal layout, with one table comparing the options and one showing each person's position
- **ClickUp layout:** pass. The validator script isn't in this workspace, so I checked the layout by hand
- **Readability and voice:** pass

**Things I added that aren't in the thread.** Please strike any you don't want:
- **Open decision: how Option B handles to-do fields.** The thread only describes B merging block text, not checkbox or due-date changes
- **Open decision: mixed-version rollout.** Nothing covers what happens while some clients still run v3
- **Open decision: the message to members once a change ships.** This comes from Marta's original question about what Support tells people
- **Release-cycle note under risks.** From the context page: the mobile apps ship every two weeks, and Desktop runs the web client so it gets Web changes without its own release
- **Caveat under the figures.** The 0.8% counts sync sessions and the 33 of 40 counts tickets, so the two shouldn't be combined

Offline plans are left out. The doc says Oskar's input was about offline editing and lists it as out of scope. Tomasz's options doc and the `Sync / Conflict copy` frame are marked as not supplied, so the options go only as far as the thread describes them.