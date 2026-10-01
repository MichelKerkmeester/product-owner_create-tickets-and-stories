Path: `export/002 - task-booking-funnel-events.md`

Verified: read-back succeeded; 91 lines
HVR self-scan: 0 hard blockers. Fixed: none needed. Kept with reason: `checkout_complete`, `booking_confirmed` and `payment_pending` repeat as fixed identifiers rather than cycling synonyms, the `---` dividers and `- []` checkboxes are the Task contract, and the iOS/Android/web and property lists are source-fixed sets rather than countable triads.

Quality summary: Completeness 9, Clarity 9, Actionability 9, Accuracy 9, Relevance 9, Mechanism Depth 8. 19 checklist items, 559 words inside the 900 budget. Every event, property, service, date and status word (`deprecated`, `proposed`, `payment_pending`, `YYYY-MM-DD`, 2026-11-01) is carried as the tracking plan writes it, and the FE and BE tasks stay named rather than absorbed.

Summary: The task covers only the Data team's lane, under `TRK`, at `DATA - Guest app - TRK - Booking funnel verification and dashboard cutover`. It has three requirement groups: check every funnel event in `events-collector`, move the funnel dashboard off `checkout_complete` and on to `booking_confirmed`, and have the collector drop `checkout_complete` on 2026-11-01. The client events and `booking_confirmed` are named in Related tasks as separate work, so this task does not swallow them.

Three choices in the file you may want to strike or redirect: the discipline and surface codes (`DATA`, `Guest app`) are my read of your title convention since you gave only `TRK`; the `date_changed` deferral note is mine, because its trigger is still unsettled with Search; and the "no dashboard or report still reads `checkout_complete`" check is mine as the safety net for the removal date. Your context files are unchanged, and `export/001` stays as it was.

Next step: tell me if the codes or those three items should change, or say the word and I will offer a ClickUp delivery for this task.