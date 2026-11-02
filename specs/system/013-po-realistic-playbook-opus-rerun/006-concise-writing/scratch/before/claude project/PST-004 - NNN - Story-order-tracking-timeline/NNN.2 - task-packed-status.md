# BE - TRACK - Packed status from the warehouse system

### About

---

The warehouse system already reports back to orders-service when an order is packed, but the customer never sees it. This task records that report as the `Packed` status, so the timeline has a step between `Order placed` and `Shipped`.

**Story**

---

- [Customer - Order tracking - Order page timeline](<NNN - Story-order-tracking-timeline.md>)

**Related tasks**

---

- [BE - TRACK - Tracking webhook](<NNN.1 - task-tracking-webhook.md>)

### Requirements

---

**Packed status**

---

**Checklist**

- [ ] orders-service records `Packed` when the warehouse system reports the order packed
- [ ] `Packed` carries a date and time for the timeline
- [ ] `Order placed` stays tied to payment authorisation
