```markdown
# Order tracking Story clarification

I'll create a new Story with its tasks as one bundle. Before drafting, I need the decisions below in one response.

**Task split:** The brief lists six tasks: the BE tracking webhook, BE `Packed`, FE Web, FE iOS, FE Android and DATA. Confirm that split, or name another. The DATA task has to land before any FE task sends an event, so its place in the order matters.

**Owning service:** The carrier webhook lands on shipping-service, and the status the customer sees sits with orders-service. Which service stores the tracking events and changes the order status: shipping-service, orders-service or both? Name the owner of each step.

**Failed delivery:** Yusuf's note gives four exception codes, `NOT_HOME`, `ADDRESS_PROBLEM`, `DAMAGED` and `REFUSED`. The brief maps all four to `Delivery failed`, but the note describes a next working day retry only after `NOT_HOME`. Confirm that all four show `Delivery failed`. Then say which of them show a reason, and give the reason copy for each, since the brief supplies none. Maud from CS says yes for not home and no for anything that sounds like "our fault", which does not settle `ADDRESS_PROBLEM`, `DAMAGED` or `REFUSED`.

**Parcel point:** A `DL` with `delivered_to` set to `parcel_point` means the parcel was dropped at a parcel point, not collected by the customer. Should the timeline show `Delivered` for it, or other copy?

**Estimate time zone:** Each carrier window carries its own UTC offset, and UK time runs an hour behind Amsterdam for most of the year. Should the window show in the customer's market time, or in Amsterdam time everywhere?

**Lost delivered event:** A tracking event the carrier drops after its retries is gone for good, and the carrier offers no tracking history. A lost `DL` therefore leaves the order on its last status. Accept that, or does the Story need a fallback for it?

**Web layout:** Design has mocked the timeline for the apps only. Will the web layout arrive before drafting, or should the FE Web task point at the design link once it exists? Send the link to the app mock either way.

**Validation:** Unless you correct a point, the draft titles the Story `Customer - Order tracking - Status timeline`, keeps the brief's six statuses in their order, and uses Yusuf's carrier rules as written.
```

Export-equivalent path: `export/NNN - Story-order-tracking-clarification.md`

Artifact kind: Story, with its tasks as one bundle. `$story` asks before it drafts, so nothing is drafted yet. I read Hamid's brief, Yusuf's carrier notes and the company context. The block flags where the brief and the carrier note disagree on failed delivery and on the parcel point. The Story comes next once you answer, and it takes the next number in its lane.

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.