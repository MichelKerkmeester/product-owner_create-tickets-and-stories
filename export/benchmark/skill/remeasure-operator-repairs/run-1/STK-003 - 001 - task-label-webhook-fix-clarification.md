# Label webhook fix: questions before drafting the BE task

Before I draft Joris's task, I need these decisions in one reply. Each one is left open by the thread, the carrier notes or the ticket conventions.

**Ticket:** Noor exported the thread "to attach to the label webhook ticket". Is this a new task, or does that ticket already exist and I should sync with it? For a new task, does `BE - SHIP - Label webhook queue, dedupe and straggler recovery` work as the title, and is there an Epic, parent task or related ticket to link?

**Duplicate guard scope:** Noor's point 3 guards the re-create after a failure, while her summary says "guard against a second open shipment for the same parcel". Should the guard cover every `POST /v1/shipments` for a parcel, or only the re-create? Does a shipment in `label_ready` count as open, or only one in `label_pending`?

**Failure codes:** Today only `SERVICE_UNAVAILABLE` makes the handler create the shipment again. Should the task set what happens on `ADDRESS_INVALID` and `OTHER`, or leave them as they are? The carrier has not confirmed whether a `label.created` can follow a `SERVICE_UNAVAILABLE` for the same shipment. Should the task wait for that answer or carry it as an open point?

**Straggler GET:** When the 10-minute GET finds `label_ready`, should the label be copied to our own storage the same way a webhook label is? When it finds `label_failed`, should it take the same failure path as the webhook? Should these GETs back off on `429` using `Retry-After`, since they share the 20 requests per second with the POSTs around the cut-off?

**Alerting:** Should `#fulfilment-alerts` get one post per stuck shipment or one post covering all of them, and what should a post carry so someone can act on it? Which on-call rotation gets paged?

**Verification:** How should QA prove the fix, for example by replaying events in the carrier's test environment with the handler slowed past 5 seconds? Is there a success signal you want in the task, such as the duplicate reports Wouter's shift leads post in #fulfilment-eng?

**Validation:** What am I likely to misunderstand here, and which constraint should I question?
