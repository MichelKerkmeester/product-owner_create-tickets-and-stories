Path: `export/001 - task-label-webhook-fix-clarification.md`
Verified: read-back succeeded; 18 lines
HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.

I haven't drafted the task yet. `$t` has to ask one question and wait for the answer first, so the file above holds only that question, in seven parts. The ones that matter most for the draft:

- **Which parcels the guard covers:** Noor's point 3 only guards the re-create after a failure. Her summary says "guard against a second open shipment for the same parcel", which is broader. The task needs to say which one applies, and whether a shipment that already has its label (`label_ready`) still counts as open.
- **Failure codes:** Should the task define what happens on `ADDRESS_INVALID` and `OTHER`? The carrier also hasn't confirmed whether a `label.created` can follow a `SERVICE_UNAVAILABLE`. If it can, the shipment the handler creates again would still bring a second label.
- **The 10-minute GET:** Should a label it picks up be copied to our own storage the same way a webhook label is? Should it take the same failure path? Should it back off on `429`, since it shares the 20 requests per second with the POSTs near the 15:00 cut-off?

The other parts ask:

- **Ticket:** is this a new task or the existing "label webhook ticket" Noor mentions? Is `BE - SHIP - Label webhook queue, dedupe and straggler recovery` the right title, and is there anything to link?
- **Alerting:** what should an alert post contain, and which on-call rotation gets paged?
- **Verification:** how should QA prove the fix?
- **Validation:** is there anything I'm likely to get wrong?

Once you reply, the task will be saved as `export/002 - task-label-webhook-fix.md`. The five points will be in scope, and polling only will be listed as rejected because of the rate limit.