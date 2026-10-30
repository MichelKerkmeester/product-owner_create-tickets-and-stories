<figma-url>
Read-back: 6 of 6 entities, 6 of 6 relationships, 22 of 22 attributes, first glance: Booking
Left out: columns for guests, properties and rooms, because the schema note names none
Finding: the three payment states (authorised, captured, refunded) did not reach the Payment card, which shows `status string`, because the composer drops a column comment. Fix: put the three values in the type slot (`authorised | captured | refunded`) in the model and compose again, then delete the old "Stays model" section (1:3) on its own yes. Want that?
HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: "offers", the source's own relationship verb on the Property to Room line.