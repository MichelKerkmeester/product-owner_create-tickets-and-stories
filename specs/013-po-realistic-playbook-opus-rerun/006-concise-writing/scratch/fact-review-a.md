skill/SDK-001 - 001 - doc-promotion-stacking.md | 242 | 242 | Changed | "The cap is met by cutting the code's share. The note does not say what happens when the automatic promotion alone passes 50%, with or without a code"
skill/SDK-003 - 001 - doc-sync-conflicts-lost-edits-clarification.md | 9 | 9 | Changed | "The two files agree on how v3 behaves today, and I found no conflicting claims between them."
skill/SDK-004 - 001 - doc-activity-emails-reference-clarification.md | 7 | 3 | Changed | "The newer edit date doesn't settle it on its own"
skill/SDK-003 - 002 - doc-sync-conflict-options.md | 121 | 123 | Dropped | "The context page notes that iOS and Android ship every two weeks and roll out over 7 days, and that Desktop runs the web client"

Files read: 42 (27 with a diff, 15 identical to the snapshot). Problems found: 4, all low severity.

## What each problem is

1. SDK-001, line 242. The edit reads "What happens with or without a code, since the cap cuts only the code's share". The word "only" asserts the cap never reduces the automatic promotion. That is the exact case the note leaves open, so a hedge became a claim. Rules 6 and the order block (lines 49, 121, 124) say the code's share is cut, not that nothing else can be.
2. SDK-003 clarification, line 9. "I found no conflicting claims" became "with no conflicting claims". The writer's own check became a flat statement about the sources.
3. SDK-004 clarification, before line 7, after line 3. "doesn't settle it on its own" became "nor does the newer edit date settle it". The qualifier is gone, so the date goes from a partial factor to no factor.
4. SDK-003 options, before line 121, after lines 122 and 123. The bullet was split. "per the context page" now sits only on the iOS and Android sub-bullet. The Desktop sub-bullet ("Desktop runs the web client, so a Web change reaches Desktop without a Desktop release") no longer names its source anywhere in the file.

## Noted, not counted

- SIR-001 clarification, line 17: the bold label "**2. Why it matters**" became "**2. What points should achieve**". It is a reword, not a cut, and bold labels fall outside the script's heading check. The two questions under it are unchanged, so no fact moved.
- SDK-002 runbook, line 19: "long after the fix" was cut. "some hours away" on the same line still carries the delay, so it counts as kept.
- PST-002 turn 2, line 13 and SEP-002 clarification, line 7: "since" now joins two sentences the original set side by side. The original already implied that link, so it counts as kept.

## Files with a diff and no problem

- skill/SDK-001 - 001 - doc-promotion-stacking.md, apart from line 242. The dropped "Everything under Stacking rules is current behavior" sentence is kept at lines 5 to 7, 60, 235 and 256. The context cut from the open questions is kept at lines 83 and 89.
- skill/SDK-002 - 001 - doc-payment-webhook-failures-clarification.md
- skill/SDK-002 - 002 - doc-payment-webhook-failures-runbook.md. The INC-0412 fix timing moved from line 64 to line 67.
- skill/SDK-004 - 002 - doc-activity-emails-catalog.md. "Not sent when there is nothing unread" and "A workspace with no activity that week gets no summary" are kept at lines 45 and 48.
- skill/SEP-001 - 001 - Epic-partner-self-onboarding.md
- skill/SEP-002 - 001 - Epic-offline-mode-clarification.md
- skill/SEP-002 - 002 - Epic-offline-mode.md
- skill/SEP-003 - 001 - Epic-self-serve-returns.md
- skill/SIR-001 - 001 - intake-guest-loyalty-points-clarification.md, apart from the label noted above
- skill/SIR-002 - 001 - intake-wishlist-cross-device-clarification.md
- skill/SIR-002 - 002 - Story-wishlist-saved-to-account-in-apps.md
- skill/SST-001 - 002 - Story-free-cancellation-filter.md
- skill/SST-002 - 001 - Story-view-only-share-links.md
- skill/SST-003 - fernhouse-save-card-draft.md
- skill/SST-004 - 001 - Story-order-tracking/001 - Story-order-tracking.md
- skill/SST-004 - 001 - Story-order-tracking/001.4 - task-tracking-webhook.md
- claude project/PST-001 - NNN - Story-free-cancellation-filter-clarification.md
- claude project/PST-001 - NNN - Story-free-cancellation-filter.md
- claude project/PST-002 - NNN - Story-member-sharing-view-only-links (turn 2).md
- claude project/PST-002 - NNN - Story-member-sharing-view-only-links.md
- claude project/PST-003 - fernhouse-save-card-draft (turn 2).md
- claude project/PST-003 - fernhouse-save-card-draft.md
- claude project/PST-004 - NNN - Story-order-tracking-timeline/NNN - Story-order-tracking-timeline (turn 2).md
- claude project/PST-004 - NNN - Story-order-tracking-timeline/NNN - Story-order-tracking-timeline.md

## Files identical to the snapshot

- skill/SIR-001 - 002 - Epic-guest-loyalty-points.md
- skill/SST-001 - 001 - Story-free-cancellation-filter-clarification.md
- skill/SST-004 - 001 - Story-order-tracking/001.1 - task-ios-tracking-timeline.md
- skill/SST-004 - 001 - Story-order-tracking/001.2 - task-android-tracking-timeline.md
- skill/SST-004 - 001 - Story-order-tracking/001.3 - task-web-tracking-timeline.md
- claude project/PST-004 - NNN - Story-order-tracking-timeline/NNN.1 - task-ios-tracking-timeline.md
- claude project/PST-004 - NNN - Story-order-tracking-timeline/NNN.1 - task-tracking-webhook.md
- claude project/PST-004 - NNN - Story-order-tracking-timeline/NNN.2 - task-android-tracking-timeline.md
- claude project/PST-004 - NNN - Story-order-tracking-timeline/NNN.2 - task-packed-status.md
- claude project/PST-004 - NNN - Story-order-tracking-timeline/NNN.3 - task-web-tracking-timeline (turn 2).md
- claude project/PST-004 - NNN - Story-order-tracking-timeline/NNN.3 - task-web-tracking-timeline.md
- claude project/PST-004 - NNN - Story-order-tracking-timeline/NNN.4 - task-ios-tracking-timeline.md
- claude project/PST-004 - NNN - Story-order-tracking-timeline/NNN.4 - task-tracking-webhook.md
- claude project/PST-004 - NNN - Story-order-tracking-timeline/NNN.5 - task-android-tracking-timeline.md
- claude project/PST-004 - NNN - Story-order-tracking-timeline/NNN.6 - task-tracking-timeline-events.md
