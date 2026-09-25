I haven't drafted the bug report or the story yet. You used both `$bug` and `$story`, so I've saved one question for you to answer first.

Path: `export/001 - intake-wishlist-cross-device-clarification.md`
Verified: read-back succeeded; 25 lines
HVR self-scan: 0 hard blockers. Fixed: Oxford comma in the list of example child stories. Kept with reason: none.

Quality summary: the file holds only the question. Each option has its own fields and nothing is written in advance.

The two context files point to a story, not a bug. The app wishlist is saved on the phone and the web wishlist is saved to the account. Teun (iOS engineer) confirmed on 2026-09-22 that it was built this way and that nothing changed in 4.8.0 or 4.8.2. A bug report would have no correct behavior to compare against. Maud's CS note calls it a bug, and Lotte hasn't decided yet whether the apps should change.

Please reply with:
- **Which artifact:** a story, an epic (a set of stories) or a bug.
- **Lotte's decision:** has she approved changing the apps, or should I write it as a proposal waiting on her?
- **Customers without an account:** should their app wishlist keep working, and should it survive a new phone or a reinstall?
- **Merging the lists:** when a customer signs in with a list on the phone and another on web, what happens if the two together pass the 50-item limit?
- **Measure of success:** fewer wishlist contacts to CS, fewer complaints, or something else.

If you pick bug, I need a source that says what the correct behavior should be.