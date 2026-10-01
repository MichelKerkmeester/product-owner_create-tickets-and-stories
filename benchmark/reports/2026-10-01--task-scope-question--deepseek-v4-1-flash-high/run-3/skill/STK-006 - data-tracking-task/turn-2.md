**Path:** `export/002 - task-booking-funnel-dashboard-move.md`

**Verified:** read-back succeeded; 68 lines

**HVR self-scan:** 0 hard blockers. Fixed: none. Kept with reason: literal event, service and property identifiers and supplied values (`checkout_complete`, `booking_confirmed`, `events-collector`, `payment_pending`, `YYYY-MM-DD`, `2026-11-01`, `source` set to `server`) preserved as the tracking plan writes them.

**Quality summary:** Task Mode, Standard energy. Three numbered requirement groups cover the Data side you described: verifying each funnel event in `events-collector`, moving the funnel dashboard to `booking_confirmed` before the removal date, and dropping `checkout_complete` in the collector on `2026-11-01`. Supplied values travel verbatim in backticks, the draft status of the plan is retired now you say the refinement closed unchanged, and the remaining scope sits as a Related tasks block rather than leaking into this task.

Three judgement calls to check. First, the title surface is `Guest app`, since the four-part title convention has no Data surface and the funnel is a Guest app flow, so the title reads `DATA - Guest app - TRK - ...`. Second, I left `date_changed` out: it stays `proposed` in the unchanged table, its properties are not agreed and its client build belongs to the later FE task. Third, the future FE and BE tasks are named as backticked plain text with no invented links.

Tell me if the surface or the `date_changed` call is wrong and I'll adjust, or say the word and I'll move on to a sibling task.