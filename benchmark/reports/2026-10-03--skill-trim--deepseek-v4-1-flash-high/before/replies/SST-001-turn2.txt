Saved the Story.

**Path:** `export/002 - Story-free-cancellation-filter.md`
Verified: read-back succeeded; 133 lines
HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: the literal strings and identifiers the source supplied, `Free cancellation until 14 Oct`, `No stays with free cancellation for these dates`, `Clear filter`, `filter_applied`, `free_cancellation`, `d MMM`, `8.13.0` and `search-service`, and the house bold-lead and `- []` grammar the Story template requires. Product Owner output-format validator: passed across 1 artifact file. The clarification file at `export/001` is untouched, and no supplied context file was modified.

**Quality summary**
*   Kind: Story, not Epic, because the work is one feature area, the filter with its card badge and empty state
*   Requirements: six groups mirroring Tomas's own organisation (filter, result card badge, empty state, tracking, release, not in this release), 24 `- []` items, every supplied number, string, version and identifier carried verbatim
*   Acceptance criteria: five outcome-led criteria over three surfaces, with no supplied value inside a Given/When/Then
*   Delivery: omitted, since nothing was requested and nothing in the source forces one
*   Budget: about 1,200 words against the 1,400 cap for a Story

**Summary**
Both Guest Support asks are in, as a requirement item and a matching criterion each: the deadline shows the property's local date so it matches the confirmation email, and the filter survives opening a property page and returning to the results. Tomas's notes carry the rest, with his exclusions kept as a constraint group named `Not in this release` and the badge untouched when the filter is off. The confirmation-email and property-page asks sit alongside his `d MMM` locale rule, which I read as compatible because one fixes the format and the other fixes which day.

**Three things to check before this goes to the squad**
*   The third expected outcome, that Guest Support gets fewer pre-booking chats, is my wording of his "most common question" line rather than an outcome he stated. Strike it if you would rather not promise it.
*   The four out-of-release items are constraint items rather than a Delivery No-gos close. Say the word if you would prefer them there.
*   The version and release lines sit in Requirements, since `8.13.0` and the web-in-the-same-week rule are hard values. Move them if the squad treats release timing as planning detail.

Next step: send the Guest Support ticket numbers if the two asks arrived on tickets, since they would give the Problem section its named evidence. Otherwise this is ready to hand to Search, and I can also break it into tasks if you want the Story with its task split.