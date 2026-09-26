```markdown
# Customer - Order tracking - Order page timeline: questions before drafting

I'll write the Story with its six tasks, split the way Hamid's brief lists them. Some decisions are still open in the sources, and I need them before I draft. Please answer them all in one reply.

**1. Reason for a failed delivery:**
- Hamid's brief leaves open whether `Delivery failed` shows the reason. Yusuf's notes list four `exception_code` values: `NOT_HOME`, `ADDRESS_PROBLEM`, `DAMAGED` and `REFUSED`
- Which codes show a reason, and what is the exact English copy for each?
- If this isn't decided yet, should the Story keep it as an `**Open:**` line with Maud and Hamid named as the people who decide it?

**2. Failed deliveries with no second attempt:**
- The brief only covers `NOT_HOME`, where a new `OD` moves the order back to `Out for delivery`
- After an `EX` for `ADDRESS_PROBLEM`, `DAMAGED` or `REFUSED`, what does the customer see next, and does the timeline stay on `Delivery failed`?

**3. Parcel point drop-off:**
- After a second `NOT_HOME`, the carrier sends `DL` with `delivered_to` set to `parcel_point` when it drops the parcel at the parcel point. That happens before the customer collects it
- Should this still show `Delivered`, or a different status or line? If different, what is the copy?
- Should `neighbour` show anything extra?

**4. Lost tracking events:**
- A tracking event the carrier drops is gone for good, and there is no tracking history endpoint. A missed `DL` leaves the order stuck on its last status
- Is that an accepted limit to state in the Story, or should the Story require something, such as an alert or a CS fallback?

**5. Which service stores and maps events:**
- The webhook lands on shipping-service (Fulfilment), and orders-service (Post-purchase) owns order status
- Which service stores the events and maps carrier codes to statuses? This decides the team, and it decides the feature code in the `BE` task title

**6. Web design:**
- The timeline is only mocked for the apps so far
- Should `FE - Web` go in now with an `**Open:**` line that points at the web layout, or wait until the web design exists?
- Do you have a link to the `Order page / Tracking timeline` frame for References? Without one, I'll name the frame and add no link

**7. The analytics event for tapping the carrier link:**
- The brief asks for an event for the carrier link being tapped, but it never adds a carrier link to the order page
- Is there a carrier link to add? If so, what are its copy and destination? Or does the event cover tapping the tracking number?
- Are the event names already in the Data tracking plan, or should the DATA task leave the names for Data to set?

**8. Time zone of the delivery window:**
- `eta_window` carries its own UTC offset. UK customers are one hour behind the Netherlands
- Should `Between 10:00 and 14:00` show the customer's local time, or the time exactly as the carrier sends it?

**9. Orders with parcel and pallet items:**
- How does an order with both look? One timeline per parcel, plus the pallet items with today's page and the line `The delivery company will call you to book a delivery slot`?

**10. Guest orders:**
- Guests have no order history. Is tracking for guest orders out of scope for this Story?

**11. What am I likely to get wrong:**
- Is anything in the two source notes out of date or overruled since 2026-09-21?
```

Export-equivalent path: `export/001 - Story-order-tracking-clarification.md`

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.

The request was `$story`, so this is a **Story** with its six tasks under it. Both source notes are clear on the statuses, the carrier codes, the delivery-window copy and the webhook rules. The questions above cover what they leave open or where they disagree:

- **Failure reasons and follow-up (items 1 to 3):** which reason each failed delivery shows, and what happens after one
- **Lost tracking events (item 4)**
- **Who owns the tracking service (item 5)**
- **The missing web design (item 6)**
- **The carrier-link analytics event (item 7):** the brief asks for it but never adds the link to the page
- **Remaining details (items 8 to 10):** time zones, orders with both parcel and pallet items, and guest orders

Once you answer, I'll write the Story and its six tasks as one set under the next number.