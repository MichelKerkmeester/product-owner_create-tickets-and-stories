<figma-url>
Read-back: 6 of 6 entities, 6 of 6 relationships, 12 of 12 attributes, 2 of 2 zones, first glance: Booking
Left out: the columns support asks about, not supplied. Only the keys the joins imply are drawn.
Finding: The board shows `PK id key` because no source gives column types, so `key` stands in for a type. Send the schema note and I'll recompose with the real names and types. The old section is deleted only on its own yes, once I name it.
Finding: The cardinalities are as you accepted them. Booking to Payment is 1 to 0..n, and Property to Room and Property to Rate plan are 1 to 1..n. They are still your reading, not a schema fact.
Finding: The board is a new section in `<draft-file-key>`, which was empty, and nothing was created in the Roamstay Product or Barter plans. I didn't check which plan owns the file.
Finding: The read-back confirmed the zones, entity fields, connector endpoints and crow's-foot caps. It lists connector names, not label text, so I checked the six labels against the composing call's return and the screenshot.
HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: "offers" (your own verb for Property to Room, a literal label and not the banned copula).