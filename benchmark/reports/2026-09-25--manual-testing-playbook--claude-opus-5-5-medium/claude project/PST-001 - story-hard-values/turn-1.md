```markdown
# Guest - Search - Free cancellation filter, clarification

Tomas's notes already cover the filter, the result card badge, the empty state, tracking and the release. The points below are all that's still needed before drafting. Please answer them in one reply.

**Guest Support asks:** Paste both asks as Guest Support wrote them. For each one, should it go into this Story or be recorded as a follow-up? The two most likely to overlap with Tomas's "Not in this release" list are the badge on the property page and the map view. If an ask goes against one of his exclusions, does his list win, or has he agreed to the change?

**Filter persistence:** The notes say the filter stays on when the guest changes dates or guests, and turns off when they start a new search from the home screen. Does it also stay on when the guest changes the number of rooms, or edits the destination from the results screen?

**Price filter:** When both filters are on, should the Price range match against the free cancellation price shown on the card, rather than the cheapest rate overall?

**Delivery section:** Do you want Estimation, Rabbit holes and No-gos in the Story? If yes, Tomas's four exclusions go under No-gos. If no, the Story ends on Acceptance criteria and the exclusions go in the Solution text.

**Links:** Please send links to Ines's frames and to Tomas's notes for the References section. Without them, I'll leave References out rather than fill it with placeholders.
```

Export-equivalent path: `export/NNN - Story-free-cancellation-filter-clarification.md`

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.

I've held off drafting until the two Guest Support asks arrive, because they could add requirements or clash with Tomas's exclusions. Writing the Story now would mean rewriting it once they come in. The block above lists everything that's still open, including those asks, so one reply from you is enough.

It will be a **Story** (not an Epic) titled `Guest - Search - Free cancellation filter`. Tomas's notes give me enough for the Requirements section. That includes the exact values, the badge format, the empty-state copy, the `filter_applied` event with `filter_name` set to `free_cancellation`, the `8.13.0` release and the rule that search-service ships first.

**Next step:** send the two Guest Support asks together with your answers above, and I'll write the full Story.