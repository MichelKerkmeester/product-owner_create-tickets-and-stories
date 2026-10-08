```markdown
I'll create the Story and its task bundle. Before drafting, I need the decisions below in one response.

**Task split:** Hamid's brief lists six tasks: BE tracking webhook, BE Packed, FE Web, FE iOS, FE Android and DATA. Confirm that split, or tell me what changes.

- Should I add a task for the backend read that feeds the timeline to web and the apps, and which team builds it?
- Which team owns the webhook task, given it lands on shipping-service, which Fulfilment owns, while this Story sits with Post-purchase?

**Delivery failed reason:** Hamid's brief leaves open whether `Delivery failed` says why. Maud says yes for not home and no for anything that sounds like our fault. Which of `NOT_HOME`, `ADDRESS_PROBLEM`, `DAMAGED` and `REFUSED` show a reason, and who supplies the copy for each?

**Retry after a failed attempt:** The brief says the carrier usually tries again after `Delivery failed`. Yusuf's notes name a retry only after `NOT_HOME`. For `ADDRESS_PROBLEM`, `DAMAGED` and `REFUSED`, should `Delivery failed` stand as final, or does a new `OD` follow there too?

**Parcel point drops:** A `DL` with `delivered_to` set to `parcel_point` means the parcel was dropped at a parcel point, not collected. The brief maps every `DL` to `Delivered`. Should a parcel-point drop show `Delivered`, given the five carrier codes include no collection event?

**Web layout:** The brief says the web layout is still to come. Should the FE Web task wait for that design, or should I draft it now with its layout pointed at the design and left open?

**Lost events:** A dropped tracking event is gone for good, and the carrier API returns no tracking history. A missed `DL` leaves the order on its last status. Accept that as a known risk for this Story, or does it need a requirement for a fallback?

**Assumptions to challenge:** These are my working assumptions. Tell me where one is wrong.

- A mixed order shows one timeline per parcel, and its pallet items keep today's page with the pallet line.
- The delivery window shows in the local time of the market the parcel goes to.
```

Export-equivalent path: export/NNN - Story-order-tracking-clarification.md

Nothing is drafted yet. `$story` asks one question before any draft, so the Story and its tasks come once you answer. The brief and the carrier notes agree on the status codes. They diverge on retries after a failed delivery and on parcel-point drops, which the questions above cover. The NNN number is reconciled when you save outside the Project.

Artifact kind: Story, with one task file per task in its bundle. Quality status: clarification only, no artifact scored.

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.