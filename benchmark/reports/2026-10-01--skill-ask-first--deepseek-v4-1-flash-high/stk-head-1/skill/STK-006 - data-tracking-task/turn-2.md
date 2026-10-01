**Path:** `export/002 - task-booking-funnel-event-validation-and-dashboard-cutover.md`
**Verified:** read-back succeeded; 77 lines
**HVR self-scan:** 0 hard blockers. Fixed: none. Kept with reason: backticked identifiers and status words (`events-collector`, `booking_confirmed`, `checkout_complete`, `_minor`, `YYYY-MM-DD`, `deprecated`, `proposed`) kept verbatim as supplied source values, and the hyphen separators in the H1 kept as the title convention's own format.

**Quality summary:** Standard energy, 3+ perspectives. Completeness, Clarity, Actionability, Relevance and Mechanism Depth clear their floors. Accuracy holds at source level: every property, service, date and status traces to the tracking plan or the Roamstay context, and the task claims nothing about plan approval.

**Summary:** The task covers the Data-owned half of the funnel work: checking each shipped event in `events-collector`, moving the funnel dashboard to `booking_confirmed` before 2026-11-01, and having `events-collector` drop the `deprecated` `checkout_complete` on its removal date. The About states why the funnel does not add up today and names the separate FE and BE tasks as the source of the events rather than folding them in. Validation checks carry the plan's exact property names, formats and values, with a blockquote note deferring the `proposed` `date_changed` to Search.

**Three additions you may want to strike or change:** the H1 uses `DATA - Guest app - TRK`, reading the surface convention as the Guest app since the funnel is the only surface it touches; the References block links `context/roamstay-booking-funnel-tracking-plan.md` as the plan source; and the `date_changed` deferral note is mine, grounded in the plan holding it as `proposed` with the picker behaviour open.

**Next step:** Tell me if the surface should read differently, and whether you want the FE and BE tasks drafted next as sibling files so the three link through `**Related tasks**`.