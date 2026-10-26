<figma-url>
Read-back: 6 of 6 entities, 6 of 6 relationships, 6 of 6 cardinalities matching the model, first glance: bookings
Left out: the columns support asks about, because the schema note itself wasn't in the request
Left out: any link between rooms and rate plans, because the schema summary doesn't state one
Finding: the board is a new file in <figma-plan-1> drafts with no project. The Roamstay Product plan isn't one your Figma account belongs to, and Flow Mode can't write into the existing file `<test-file-key>`.
Finding: every primary and foreign key name is inferred from the relationships, not taken from the schema, so check them against the real tables.
Finding: the rate plans table is labelled `ratePlans` because the pre-write check rejects underscores in table names. Its keys still read `rate_plan_id`.
Finding: the key marks every relationship as "Identifying", but the schema summary doesn't say whether any relationship is identifying. Treat that label as unconfirmed.
Finding: bookings, the first glance, has no highlight, because I left the focus line out of the model.
Finding: if you send the support columns, I'll redraw the board in this file.
HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.