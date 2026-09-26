```markdown
I'll write the Story and its six tasks, split the way Hamid's brief lists them (BE webhook, BE `Packed`, FE Web, FE iOS, FE Android, DATA). The brief and Yusuf's notes cover the role, value, statuses, rules and scope. Before I draft, I need these decisions, all answered in one reply:

**1. Reason on `Delivery failed`:** Maud says to show the reason for `NOT_HOME` and to hide anything that sounds like our fault. What should the customer see for each of `ADDRESS_PROBLEM`, `DAMAGED` and `REFUSED`? And is there approved copy for the `NOT_HOME` reason? If this is still undecided, I'll add an **Open:** line to the requirement, which also adds a `## Delivery` section.

**2. Web layout:** Design has only mocked the apps so far. Should the FE Web task go ahead with an **Open:** line pointing at the missing web layout, or wait until design delivers it?

**3. Parcel point drop-off:** After a second `NOT_HOME`, the carrier sends `DL` with `delivered_to: parcel_point` when it drops the parcel at the parcel point, not when the customer collects it. Should that still show `Delivered`, or something else? Should the page show `neighbour` or `parcel_point` at all?

**4. Lost events:** A dropped event is gone for good, and the carrier offers no tracking history. A missed `DL` leaves the order on its last status. Should the Story treat this as an accepted limit (a Rabbit hole or No-go), or does it need to guarantee something for the customer?

**5. Carrier link:** The DATA task tracks "the carrier link being tapped", but the brief never puts a carrier link on the order page. Should each client's order page get one? If not, which link does the event track?

**6. Guests:** Guests have no order history. Is tracking for signed-in customers only, or does a guest reach an order page some other way, for example from the shipping email?

**7. Delivery window time zone:** `eta_window` comes with the carrier's UTC offset. Should the page show `Between 10:00 and 14:00` in the customer's market time? This matters for the UK.

**8. Links:** Can you share the Figma link to the `Order page / Tracking timeline` frame? Without links, References stays out of the Story.
```

Export-equivalent path: `export/001 - Story-order-tracking-clarification.md`

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.

I haven't written anything yet. The Story and task files will go under the next number, in `export/002 - Story-order-tracking/`, once you answer.

Some things I'll assume unless you correct them:
- **Title:** The Story title will be `Customer - Order tracking - Tracking timeline`.
- **Task titles:** Tasks will use the `TRACK` code, for example `BE - TRACK - Tracking webhook`.
- **Task order:** The DATA task will come before the three FE tasks. The company context requires a DATA task before any FE task sends a new event.