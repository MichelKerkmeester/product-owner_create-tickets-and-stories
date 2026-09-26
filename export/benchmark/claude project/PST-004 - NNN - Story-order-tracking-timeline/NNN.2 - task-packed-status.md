# BE - TRACK - Packed status from the warehouse system

### About

---

The warehouse system already tells orders-service when an order is packed, but customers never see it. This task records it as `Packed`, between `Order placed` and `Shipped`.

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

- [ ] orders-service records `Packed` on the warehouse system's packed report
- [ ] `Packed` carries a date and time
- [ ] `Order placed` stays tied to payment authorisation
