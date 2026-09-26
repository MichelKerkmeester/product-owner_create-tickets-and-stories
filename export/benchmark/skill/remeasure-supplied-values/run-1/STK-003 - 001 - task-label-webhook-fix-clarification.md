I'll create the BE task for Joris. The scope, sources and owner are clear. Before drafting, I need the unresolved decisions below in one response:

**Title and links:** Is `BE - SHIP - Label webhook handling under slow downstream calls` right, or do you want other wording? Noor exported the thread "to attach to the label webhook ticket". Is that an existing ticket I should sync to, or is this a new task? Any Epic, related tasks or ticket links to carry?

**Duplicate-shipment guard:** Point 3 of the thread applies the guard "before creating a shipment again after a failure". Should it cover only that re-create path, or every `POST /v1/shipments` for a parcel? Which statuses count as an open shipment: `label_pending` only, or `label_ready` as well?

**Open carrier question:** The API notes leave one question open: can a `label.failed` with `SERVICE_UNAVAILABLE` be followed by a `label.created` for the same shipment? Should the task carry this as an open question for Joris, or do you have the carrier's answer?

**10-minute GET results:** The thread says what happens when the GET finds a ready label. When the GET returns `label_failed`, should it follow the same handling as the matching `label.failed` event? When it gets a `429`, should it wait for `Retry-After`, given that POSTs and GETs share the `20 requests per second` limit?

**Failure codes out of scope:** Does handling for `ADDRESS_INVALID` and `OTHER` stay as it is today, with this task changing only the `SERVICE_UNAVAILABLE` path?

**Validation:** Should QA include a test that repeats the 2026-09-15 conditions, with the warehouse system answering in 6 to 9 seconds? Pass would mean no duplicate labels and a label stored for every order paid before the `15:00` cut-off in time for the 18:00 collection.
