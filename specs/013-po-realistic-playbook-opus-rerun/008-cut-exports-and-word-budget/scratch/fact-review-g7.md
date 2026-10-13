skill/STK-003 - 001 - task-label-webhook-fix.md | 124 | 108 | Dropped | "because that afternoon produced both the duplicate labels and the late labels this task removes" (the only reason given for testing with a replay of 2026-09-15)
claude project/PDK-003 - 001 - doc-sync-conflicts-lost-edits-status.md | 68 | 62 | Dropped | "The decision waits on two things nobody knows yet about B: how much storage it costs on mobile and how often the merge falls back to a copy." (with line 9, "Joana will decide on 2026-10-09, after Tomasz runs a two-week spike on Option B"). The cut keeps both unknowns as open questions but no longer says the decision waits on them, so the reason Joana deferred is gone
claude project/PDK-003 - 001 - doc-sync-conflicts-lost-edits-status.md | 72 | 66 | Dropped | "Support keeps telling members that edits made on two devices at the same time can overwrite each other" (the owner, Support, and the audience, members, appear nowhere in the cut step)
claude project/PDK-003 - 001 - doc-sync-conflicts-lost-edits-status.md | 60 | 54 | Changed | "He calls A the cheapest change that fixes the to-do half of the tickets. Yara's split puts A's coverage at a bit over half of the overwriting sessions." The cut reads "the to-do half of the tickets, which Yara's split puts at a bit over half", so Yara's figure now describes tickets. Yara split overwriting sync sessions (snapshot line 31), not tickets
claude project/PDK-003 - 002 - doc-sync-conflict-options-proposal.md | 28 | 26 | Changed | "Any change to this behavior needs client work. v3 has no merge and no conflict copy, and changing the protocol requires every client to run a version that supports the new one." The cut reads "v3 has no merge or conflict copy, so any change needs every client on the new protocol", which invents a causal "so" and says every change needs a new protocol, while Option A fits inside v3 with a client update (lines 44 and 71 of the snapshot)
claude project/PDK-003 - 002 - doc-sync-conflict-options-proposal.md | 72 | 62 | Changed | "The merge can place both text edits. Otherwise both survive, one as a conflict copy" became "or else one survives as a conflict copy", which can be read as only one edit surviving
skill/SBG-002 - 001 - bug-android-confirmation-total-missing-city-tax.md | 56 | 54 | Dropped | "so the number of affected guests can grow from here" (the rollout date stays, the stated risk that impact will grow does not)
claude project/PST-003 - fernhouse-save-card-draft (turn 2).md | 43 | 40 | Changed | "Orders whose total including shipping is over `€150`, or `£130` in the UK" became "Orders above `€150` including shipping, or `£130` in the UK", so "including shipping" now attaches to the euro threshold only and the UK threshold reads as possibly excluding shipping

Files read: 10 (each snapshot and cut file). Problems found: 8.

## Per-file verdicts

### skill/STK-003 - 001 - task-label-webhook-fix.md: 1 problem

- Merged checklist items, every condition checked:
  - 7-day retention folded into "An `event_id` processed in the last 7 days causes no new shipment, warehouse system call or second label copy": the 7-day window survives as the dedupe window, and all three "no further work" items survive. Survives.
  - Open shipment definition folded into the no-POST item: "no POST is sent if the parcel's `reference` ... has a shipment in `label_pending` or `label_ready`" keeps the trigger (`label.failed` with `SERVICE_UNAVAILABLE`), the parcel key and both open states. The concurrency item ("at most one shipment") survives. Survives.
  - The two "label arrives second" items merged into "Whichever of `label.created` and the GET delivers a label second changes nothing: no second label copy, new tracking number or warehouse system call": covers both orders. Survives.
  - "posted once, not on every check" folded into the alert item as "is posted once to `#fulfilment-alerts`". Survives.
- Requirement 6 staging-replay reason: Dropped, listed above.
- 20 requests per second reworded: About says "POSTs use 14 of the shared 20 requests per second account limit near the cut-off", which keeps the shared account limit, the 14 per second and the cut-off timing, and still gives it as the reason polling only is ruled out. Requirement 4 keeps "GETs share the 20 requests per second limit with POSTs". Survives. The 429 item now says "waits its `Retry-After` seconds" instead of "is retried after", so the retry is implied rather than stated; not counted.
- `500`, €0.42 and Finance moved into requirements: all three survive. The `500` sentence now carries "On 2026-09-15", which the snapshot framed as the same incident, so not counted as Added. "Finance checks the invoice line by line" became "which Finance checks line by line", losing the word invoice but not the check. Survives.
- Requirement 5 lost "the pack stations already wait on labels at 15:00": a second clause of the reason for the 30-minute alert; the first reason (missing the 18:00 collection ships a day late) stays, and the 15:00 cut-off stays in the About. Fine.
- The five scope points are no longer listed in the About, but they are requirements 1 to 5. Fine.

### claude project/PDK-003 - 001 - doc-sync-conflicts-lost-edits-status.md: 3 problems

- "Keep the current support message" no longer names Support or members: Dropped, listed above.
- Oskar's reason ("a phone offline for a day comes back with every edit at once") cut: his stated position and its first reason ("expects offline editing to push the 0.8% up sharply") stay, and the day-offline scenario stays in the Offline editing open question. Fine.
- Option B cost cell lost "which v3 clients do not do": "every platform needs a release, because clients must keep the base version" only makes sense if clients do not keep it today, so the current state is still inferable. Not counted, but it is now implied rather than stated.
- "A's" coverage line: Changed, listed above. Yara measured field-only share of overwriting sessions (58%); she did not measure A's coverage directly, and the snapshot's own "puts A's coverage at" was already an inference from that split.
- Decision dependency on the spike: Dropped, listed above.
- Status-line and label em dashes not reviewed, as instructed.

### claude project/PDK-003 - 002 - doc-sync-conflict-options-proposal.md: 2 problems

- Cost bullets for A and C removed and the 6 to 8 weeks figure removed from B's Cost bullet: the Options compared table keeps every cost ("About 3 weeks of server work plus a client update", "Roughly 6 to 8 weeks", "About two quarters") and every client impact (new message type inside v3, release on every platform, protocol v4 and migration). The Status line keeps that costs are Tomasz's estimates. Survives.
- "v3 stays as it is": carried by the blockquote ("protocol v3 stays as it is until then"). Survives.
- "Nobody is sizing C now": carried by the table status "not being sized" and the out-of-scope item "Sizing Option C". Survives.
- B's Cost bullet lost "which v3 clients don't": same verdict as in 001, inferable, not counted.
- Joana's two unknowns now read "pending the two measurements below", which the Open decisions list names. Survives.
- Current state sentence and table B cell: Changed, listed above.
- Status-line and label em dashes not reviewed, as instructed.

### claude project/PBG-002 - NNN - bug-android-confirmation-total-missing-city-tax.md: no problems

- "per Guest Support" trimmed from Frequency: the attribution words are gone, but the same cell names the Guest Support test phone as the reproduction and the References keep the Guest Support escalation, so the source is still readable. Not counted. Device lost "the" and "Android" only.
- "Guests read the gap as an overcharge" became "about what looks like an overcharge": same meaning; the shown-versus-charged gap stays in Observed Behavior. Fine.

### claude project/PBG-002 - NNN - bug-android-confirmation-total-missing-city-tax (turn 2).md: no problems

- Same Frequency verdict as turn 1. Device and OS lost "Android" and, in OS, "Guest Support" before "Test phone"; the Device cell in the same table still names the Guest Support test phone. Fine.
- Turn copies: a diff of the two cut files shows only the differences the two snapshots already had (Severity wording, Device and OS rows, Related bugs, the web line, the screenshot line, and "web" in Previous working behavior). Every shared sentence is worded alike.

### skill/SBG-002 - 001 - bug-android-confirmation-total-missing-city-tax.md: 1 problem

- "per Guest Support escalation" became "per Guest Support" in Frequency: attribution kept. Device and OS rows say "Test phone"; Observed Behavior keeps "On the Guest Support test phone". Fine.
- "affected guests can grow": Dropped, listed above.
- "Guests read the difference as an overcharge" to "about what looks like an overcharge": same meaning. Fine.
- "on the iOS test phone, app 8.12.0" became "on iOS 8.12.0": the device is gone, the version stays. Fine.

### claude project/PIR-001 - 002 - Epic-guest-loyalty-points.md: no problems

- "so a repeat booking looks and costs the same as a first one" cut: "a fifth stay costs what the first did" keeps the cost half in the Problem. Fine.
- "This Epic sets neither" merged: "The value of a point and who funds points are not decided, and no child story should assume either until they are" keeps both undecided items and the instruction to child stories. Fine.
- `19%` baseline sentence dropped from the Problem: the Goal keeps "from `19%` today to `25%`" with the same `12 months` window. Fine.

### claude project/PST-003 - fernhouse-save-card-draft.md: no problems

- Card data Open line no longer lists the allowed fields: the requirement directly under it keeps "only its card token, last four digits and expiry date", and the Open line keeps that the rule forbids the brand, the owner Lotte and both resolutions. Fine.
- Problem lost "so most people retyping a card have typed it before": the 68% figure stays, and the conclusion follows from it. Fine.

### claude project/PST-003 - fernhouse-save-card-draft (turn 2).md: 1 problem

- Same Card data and Problem verdicts as turn 1.
- CVC threshold: Changed, listed above.
- Turn copies: a diff of the two cut files shows only the differences the snapshots already had (the Open decline line, the CVC line, the decline copy line, the event naming line, AC 6 and renumbering, and the decline rabbit hole). The CVC line differs between turns because the snapshots differed ("including shipping" is turn 2 only). Every shared sentence is worded alike.

### skill/STK-001 - 001 - task-free-shipping-banner-copy.md: no problems

- "who pick English in the language switcher" became "reading English", and "splitting the one message customers read at a glance" was cut. Neither changes a requirement; thresholds, markets, locales, platforms, widths and the report-back to Product before release all stay.
