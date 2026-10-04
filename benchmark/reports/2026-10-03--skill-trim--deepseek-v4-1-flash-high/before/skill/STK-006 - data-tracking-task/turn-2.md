Path: `export/002 - task-funnel-event-checks-and-dashboard-migration.md`

Verified: read-back succeeded; 76 lines

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none — the draft uses backticks for literal identifiers (`events-collector`, `booking_complete`, dates, property names) and the `---` dividers are the required Task structure, so no blocked term survives to be named.

Quality summary: titled `DATA - Guest app - TRK - ...` per your convention, since the task is the Data team's own work under `TRK`. Scope is the three things you named: checking each event in `events-collector` as its squad ships it, moving the funnel dashboard to `booking_confirmed`, and having the collector drop `checkout_complete` on 2026-11-01. The FE and BE tasks sit in `**Related tasks**` as unlinked plain text, because you said they come later. Values travel as the plan writes them (`YYYY-MM-DD`, `total_amount_minor`, `source` set to `server`, `session_id`, `app_version`, the 2026-11-01 date). `date_changed` is kept out with a note, since the refinement left it `proposed` with its picker point still open.

Two additions you did not supply, so you can strike them: the check against the old dashboard while both events still arrive, and the check that no dashboard, report or alert still reads `checkout_complete` before the drop. The first came from the plan's overlap window, the second from the drop needing a clean cutover.

The task now covers the Data side only, with the client events and `booking_confirmed` left to the later FE and BE tasks you named. Say the word if you want those two tasks drafted next, or if `date_changed` should move in once Search settles the tap question.