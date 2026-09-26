# Date picker stay limits, task intake

I'll create the FE task from Ines's notes. Before drafting, I need these decisions in one reply:

**Format & scope:** One FE task for the whole Guest app (iOS, Android and web), or one per platform? Web builds and releases on its own and has the two-month desktop layout, so a split is possible. With one task, the title would be `FE - Guest app - SRCH - Date picker stay limits`

**Property page minimum stay:** The context file says the date picker already applies a property's minimum stay on the property page. Ines's notes say the picker lets a guest pick any range today and add the minimum stay as part of this work. Which is right? And does state 5 (`This property has a 3-night minimum`) belong in this task, given the property page is `PROP` and the search date picker is `SRCH`?

**Dependencies:** The notes say the 30-night maximum and the 365-day window come from search-service config, and the minimum stay comes with the property details. Do the apps already receive all three values today, or does this task wait on a `BE` ticket? If there is one, what is its title or link?

**Design & references:** The Figma link to the `Date picker / Stay limits` frame, plus any epic, parent task or Guest Support ticket for the 23 August chats. Without links I'll name them in plain text and add no URLs

**Validation:** Anything in the notes that has changed since 2026-09-14, or anything I should leave out beyond the listed exclusions (flexible dates, weekend presets, prices in the calendar, tracking)?
