# FE - iOS - TRACK - Order page timeline

## About

---

The iOS app's order page shows a status timeline for each parcel, with that parcel's items under it and the delivery estimate under the current status. Customers see where a parcel is without copying its tracking number into the carrier's site.

The timeline shows the events that the BE tracking webhook task stores, so this task depends on that task.

**References**

---

Page

- `Order page / Tracking timeline` frame

**Story**

---

- [Customer - Order tracking - Order page timeline](<NNN - Story-order-tracking.md>)

### Requirements

---

### **Timeline and status**

---

1.  **Steps and current status**

---

The order page lists every step the parcel has taken, in the order the scans happened.

**Checklist**

- [] Each step shows its date and time
- [] The current status reads `Order placed`, `Packed`, `Shipped`, `Out for delivery`, `Delivered` or `Delivery failed`
- [] Each parcel of an order has its own timeline, with that parcel's items under it
- [] A scan that arrives late appears at its own point in time and does not change the current status

2.  **Delivery estimate**

---

When the carrier sends a delivery window, the estimate sits under the current status.

**Checklist**

- [] The estimate shows the day and the window on two lines, as the design mock shows: `Arriving Thursday 1 October` and then `Between 10:00 and 14:00`
- [] No estimate shows when the carrier sends no window, and the dispatch date never sets one

3.  **Failed delivery**

---

A failed delivery shows its own status, and a new out for delivery step can follow it.

**Checklist**

- [] `Delivery failed` shows no carrier reason
- [] After a `NOT_HOME` failure, a new `OD` moves the status back to `Out for delivery`

4.  **Pallet items, copy and retention**

---

Items that go by the pallet carrier have no tracking events, so they keep today's page.

**Checklist**

- [] An item that goes by the pallet carrier keeps today's page, with the line `The delivery company will call you to book a delivery slot`
- [] Status text is translated for all six locales: `nl-NL`, `nl-BE`, `fr-BE`, `de-DE`, `fr-FR` and `en-GB`
- [] Once `90 days` have passed since delivery, the order page shows the last status only
