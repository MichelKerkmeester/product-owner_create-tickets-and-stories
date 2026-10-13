claude project/PTK-003 - 001 - task-label-webhook-duplicates-and-late-labels.md | 17 | 13 | Changed | "The carrier's engineer said an idempotency header is planned but could not give a date." (cut: "An idempotency header is planned, undated." The carrier's engineer as source is gone, so a reported, undated intention now reads as a flat plan with no owner named)
claude project/PTK-003 - 001 - task-label-webhook-duplicates-and-late-labels (turn 2).md | 17 | 13 | Changed | "The carrier's engineer said an idempotency header is planned but could not give a date." (same change as turn 1)
claude project/PTK-003 - 001 - task-label-webhook-duplicates-and-late-labels (turn 2).md | 17 | 13 | Changed | "This work has to be live before the November peak." (cut: "It must be live before the November peak." placed right after "An idempotency header is planned, undated.", so "It" now reads as the carrier's header, not this task)
claude project/PTK-003 - 001 - task-label-webhook-duplicates-and-late-labels.md | 95 | 88 | Dropped | "copies the label file into its own storage, as for `label.created`" (where the label file goes is stated nowhere in the cut file)
claude project/PTK-003 - 001 - task-label-webhook-duplicates-and-late-labels (turn 2).md | 96 | 89 | Dropped | "copies the label file into its own storage, as for `label.created`" (same as turn 1)
claude project/PST-002 - NNN - Story-member-sharing-view-only-links.md | 46 | 43 | Changed | "Members with edit access to the page, Admins and the Owner can turn the switch on" (cut: "Editing members", which drops the per-page condition and can read as a workspace role; AC3's title "Only people who can edit the page" still carries it)
claude project/PST-002 - NNN - Story-member-sharing-view-only-links (turn 2).md | 47 | 44 | Changed | "Members with edit access to the page, Admins and the Owner can turn the switch on" (same as turn 1)
claude project/PST-002 - NNN - Story-member-sharing-view-only-links.md | 40 | 37 | Dropped | "Turning the switch on creates the link and shows `Copy link` next to the switch" (the placement "next to the switch" is gone)
claude project/PST-002 - NNN - Story-member-sharing-view-only-links (turn 2).md | 41 | 38 | Dropped | "Turning the switch on creates the link and shows `Copy link` next to the switch" (same as turn 1)
claude project/PST-002 - NNN - Story-member-sharing-view-only-links (turn 2).md | 180 | 174 | Changed | "What `Duplicate` copies is the only part of the viewer that depends on it" (cut: "Only what `Duplicate` copies depends on it", which drops "of the viewer" and so claims nothing else in the story depends on the sub-page decision)
claude project/PST-001 - NNN - Story-free-cancellation-filter.md | 96 | 90 | Changed | "after booking that rate plan, the deadline in the confirmation email is the same date" (cut: "the booking confirmation email shows the same date", which makes the match unconditional; a guest who books a different rate plan gets a different deadline)
skill/SDK-004 - 002 - doc-activity-emails-catalog.md | 89 | 87 | Changed | "The `summary-sender` job, which runs hourly on Mondays and picks the Owners and Admins whose local time is Monday 09:00 in that hour" (cut: "hourly on Mondays for Owners and Admins then at 09:00 local", which loses how each hourly run selects recipients)

Files read: 8 (snapshot and cut for each). Problems found: 12, across 5 files. skill/SIR-001 - 002 - Epic-guest-loyalty-points.md and skill/STK-006 - 002 - task-booking-funnel-events.md have none.

## Verdicts on the cuts the writer flagged

PTK-003, both turns
- "Joris traced both problems": fine. It is background on who did the diagnosis. Joris is still named in References as the author of the working notes, and no requirement depends on it.
- Idempotency header: Changed, listed above. The attribution carried a hedge (the carrier's engineer said it, with no date), and the cut states it as fact. In turn 2 the cut also moves the November deadline onto the header.
- Polling out of scope: fine. The one reason, that every POST and GET shares the `20 requests per second` limit with POSTs at up to 14 around the cut-off, still stands. "polling several hundred pending labels would make labels arrive later in the busiest hour" spells out what follows from that reason. It gives no second reason.
- "arrive before the first has finished processing" to "concurrent deliveries": fine, same condition.
- "more than one shipment" to "two shipments": fine. "never has two" reads as two or more.
- The outcome paragraph ("After this task...") and requirement 5's "12 missing labels only landed after 21:00": fine. The first repeats requirements 1, 2, 4 and 5. The second repeats About (cut line 11).
- Turn parity: the shared sentences have the same wording in both cut turns. The only differences are the ones the snapshots already had: the November sentence, the 8-second timeout items, the extra turn 1 GET checklist item and the turn 2 Definition of done.

PST-002, both turns
- Sub-page inheritance wording in the Open note: fine. Both proposals, Engineering's reason, Lena, the security reviewer, no date and the `Duplicate` dependency all stay.
- Rabbit holes pointing at the Open note: fine in turn 1, because the note in the same file carries the whole thing. In turn 2 the added line "Only what `Duplicate` copies depends on it" is Changed, listed above.
- "the decision will not land before the build starts" to "and not before the build starts": fine, same timing.
- "copies the page into a workspace of theirs" to "to a signed-in viewer's workspace": fine. It is still one of the viewer's own workspaces, and the sign-in condition stays.
- "member with edit access to a page" to "Page editors" in Solution: fine, since "page" stays. The Requirements line "Editing members" is the one that lost the page and is listed above.
- "The plan decides how many active links a workspace can keep and which expiry options it gets" cut from Solution: fine, the Plans section carries both.
- Turn parity: the shared sentences have the same wording in both cut turns. The only differences are the ones the snapshots already had: Problem, the agency outcome, the Open note split, and Rabbit holes.

PST-001
- Criterion 2 no longer names the rate plan booked: Changed, listed above.
- Deadline wording ("check-in minus the partner's cancellation window, so `14 days` means 14 days before"): fine.
- "deadline has passed does not count" merged into "unexpired": fine, same condition in Requirements and AC1.

SDK-004
- EM-03 recipients "Everyone in the thread": fine. Sent when still limits it to a thread the recipient started or replied in.
- Boundary entries "Unknown" and "Unnamed in the sources": fine. Both still record that the sources leave the point open.
- Index cells "On event" and "local time": fine. Rules define local time as the profile time zone.
- The three removed repeats (mention-in-reply under EM-02 and EM-03, and the trailing 07:00 UTC stale note): fine. The rules list, the table and the EM-01 section still carry them.

SIR-001
- "Guests earn no points" folded into "no points scheme": fine.
- "A completed stay earns nothing toward the next": fine, same fact.
