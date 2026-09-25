I've written the free cancellation filter up as a **Story** for the Search squad. It uses everything in Tomas's notes plus both Guest Support asks.

Path: `export/002 - Story-free-cancellation-filter.md`
Verified: read-back succeeded; 144 lines
HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.

Quality summary: every number and exact piece of text in Tomas's notes is copied unchanged into Requirements, including `8.13.0`, `d MMM`, `Free cancellation until 14 Oct`, the Lisbon test counts (1,146 and 312) and `filter_applied` / `free_cancellation`. His "Not in this release" list is a group called "Unchanged in this release". There are 7 acceptance criteria. There's no Delivery section, because you didn't ask for one and nothing is left open. There's no References section either, because I had no links.

**Where the Guest Support asks went:**
- **Badge date:** it shows the property's local date, and there's an acceptance criterion for a guest searching from another time zone. This fits with Tomas's `d MMM` rule: the locale only sets how the date is written, not which date it is.
- **Going back to results:** the filter stays on when a guest opens a property and goes back. It sits alongside Tomas's rules: it stays on when dates or guests change and turns off on a new search from the home screen.

**Things I added that nobody gave me, so you can remove them:**
- Criterion 6 checks that search is unchanged for guests who leave the filter off. That extends Tomas's point that result cards stay as they are.
- Criterion 7 checks that the event reaches `events-collector`. That comes from the analytics rules in the company background, not from Tomas.
- The two expected outcomes are my own wording of the "Why" in Tomas's notes.

**One gap I left alone:** neither source says which time zone decides whether a deadline "has passed" for hiding a stay from results. Guest Support's ask covers the date shown on the badge. It doesn't cover the rule for what shows up in results, so Dario or Tomas may want to settle it.