<!-- Mode: Task | Template: Assets - Task Templates v0.101 -->

# Creator payout pause

### About

---

Pending payouts need a way to show that they are paused and why. This task adds a pause indicator on the payout row and stores the reason a payout was paused, so a paused payout carries its own context.

The pause and its reason are visible in the payout history, so QA can verify that a payout was paused and check the reason that was given. Because the reason is required, every paused payout answers the question of why it stopped.

### Requirements

---

1.  **Required pause reason**

---

Every paused payout carries the reason it was paused. The reason is required, so a payout cannot enter the paused state without one, and it stays with the payout wherever the payout is shown or inspected.

**Checklist**

- [ ] A payout can be paused with a reason
- [ ] The reason field is required when a payout is paused
- [ ] The reason is stored with the payout

---

2.  **Pause indicator on the payout row**

---

A creator scanning their payouts sees which payouts are paused without opening each one. The payout row shows a pause indicator while that payout is paused.

**Checklist**

- [ ] The payout row shows a pause indicator while the payout is paused
- [ ] The payout row shows no pause indicator while the payout is not paused

---

3.  **Pause verification in the payout history**

---

The payout history records the pause, so QA can verify that a payout was paused and check the reason that was given.

**Checklist**

- [ ] The payout history shows that a payout was paused
- [ ] The payout history shows the pause reason
