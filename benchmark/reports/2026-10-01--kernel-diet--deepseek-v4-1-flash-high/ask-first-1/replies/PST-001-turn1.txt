```markdown
The Story lane is clear: one feature area, the Search squad's free cancellation filter, and Tomas's notes supply the problem, the value and the behavior. The two Guest Support asks have not arrived, so the draft waits on the four items below, answered together.

**1. Guest Support's two asks**
Send both, with the requester and the date if you have them. For each, say whether it adds behavior beyond what Tomas's notes already describe. The filter, the result card badge, the empty state and the tracking event are all specified there, so an ask that only repeats one of them changes nothing.

**2. Scope, if an ask reaches past this release**
Tomas's notes leave four things out of this release: the map view, sorting by cancellation deadline, any Partner Hub change, and a badge on the property page. If either ask lands on one of those, tell me which way to take it:
*   Keep the Story on the search filter and treat the ask as excluded
*   Fold the ask into this Story
*   Write a second Story for the ask

**3. References**
The notes carry no links. Send Ines's design frames, plus any tracking plan row or ClickUp link to carry, or say to draft without a `#### **References**` section, which the house format omits when nothing is supplied.

**4. Delivery view**
Do you want the Story to close on `## Delivery` with estimation, rabbit holes and no-gos? Tomas's `Not in this release` list becomes the No-gos and the unknowns stay `TBD...`. Otherwise the Story ends on Acceptance criteria.

Planned title: `Guest - Search - Free cancellation filter`. It follows the house `{Persona or surface} - {Area} - {Feature}` pattern, so correct the area word if the Search squad uses another. The Story covers iOS, Android and web, with `search-service` shipping first.
```

Export-equivalent path: export/001 - Story-free-cancellation-filter-clarification.md

Detected: Story Mode, Story shape. Scope, value and the supplied hard values (the `1,146` to `312` stay count, the `Free cancellation until 14 Oct` badge, the `d MMM` date pattern, the `filter_applied` event, `8.13.0`) are all readable from Tomas's notes, so the only thing holding the draft is the promised source.

Quality status: no artifact drafted, so the house-format and source-fidelity gates have nothing to score yet. No source conflicts were resolved or set aside, because none exist until the two asks land.

Two things I assumed rather than asked. I read the Guest Support ticket in context as a Booking squad defect about the Android total, not as one of your two asks. And I took "for the Search squad" as the owning squad rather than a change to who ships it.

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: `TBD...`, the Story Mode house placeholder for an unknown value rather than a prose ellipsis.

Once you answer, the Story follows as a new Deliverable Block taking the next number in that lane.