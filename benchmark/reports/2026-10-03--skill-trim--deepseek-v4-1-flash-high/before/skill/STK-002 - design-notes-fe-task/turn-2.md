**Path:** `export/001 - task-stay-limits-date-picker.md` (updated in place, same basename as the delivered task)

**Verified:** read-back succeeded; 186 lines

**HVR self-scan:** 0 hard blockers. Fixed: none. Kept with reason: `backstop`, the term you used for the unchanged `search-service` check, and the backticked `8.13.0` train number as a literal identifier.

**Quality summary**
*   Scope: one FE task, iOS, Android and web together, no parent, Search squad, `8.13.0` train
*   Backend boundary: `search-service` is explicitly left unchanged, with its own `30-night` check kept as the backstop, and no service work inside the task
*   Verification: new group 9 carries QA sign-off on all three platforms and in `en-GB` and `en-US`
*   Requirements, copy table, edge cases and out-of-scope boundaries carry over unchanged, with supplied values still verbatim
*   Size: 892 words, inside the 900-word task budget

**Summary**
The task now reads as a single front-end ticket for iOS, Android and web with no parent, carried by the Search squad on the `8.13.0` train. The 30-night rule in `search-service` stays as it is and is named as the backstop, so the picker stops the range earlier while the server check keeps guarding search. A new Verification group records QA sign-off across all three platforms in `en-GB` and `en-US`.

Two things I added beyond the design notes: the release-train and no-parent context, and the backstop plus QA sign-off checks. Both come from your direction, so strike them if either is not meant to live in the ticket.