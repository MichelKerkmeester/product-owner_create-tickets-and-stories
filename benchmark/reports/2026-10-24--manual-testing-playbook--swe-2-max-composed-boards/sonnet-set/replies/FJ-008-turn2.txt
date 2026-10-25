<figma-url>
Read-back: 6 of 6 entities, 6 of 6 relationships, 12 of 12 attributes, first glance: Booking. The board was written in <figma-plan-3>, a new file named "Stays model".
Left out: every non-key column, because you asked for keys only.
Finding: the Guest to Booking line crosses the Room and Rate Plan lines to Booking at one point. It drops straight through the "prices" label, so it can read as joining Rate Plan.
Finding: the six cardinality labels were read from the screenshot, because the read tool does not return connector text. Their two ends and direction were checked from the connector ids.
Finding: `roomId` sits on Booking, as you described it. `context/roamstay-context.md` says one booking holds up to 8 rooms. A Booking-to-Room junction would fit that, so say if you want it.
HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.

I can fix the crossing by changing the model and composing the board again. The old board would only be deleted after your second yes, and a recompose spends about three more of the six monthly calls. Do you want me to try it?