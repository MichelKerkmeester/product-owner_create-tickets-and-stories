# Creator payout pause

### About

---

Creators with pending payouts have no way to see that a payout is paused or why. When a payout is paused, its reason must be stored, so the pause stays explainable after the fact and support and QA can trace it.

This task adds a pause indicator for pending payouts, stores the reason for each pause and makes the pause verifiable in the payout history.

### Requirements

---

1.  **Stored pause reason**

---

The reason a payout is paused must be stored with the pause, and the reason field is required. A pause cannot exist without its reason, so anyone reading the payout later can see why it was paused.

**Checklist**

- [ ] The pause reason is stored whenever a payout is paused
- [ ] The reason field is required, so a pause cannot be saved without a reason

---

2.  **Pause indicator in the payout row**

---

A payout row for a pending payout shows whether that payout is paused, so the creator sees the pause without leaving the payout.

**Checklist**

- [ ] The payout row shows the pause indicator for a pending payout that is paused
- [ ] A pending payout that is not paused shows no pause indicator

---

3.  **Pause verifiable in the payout history**

---

The payout history carries the pause, so QA can verify there that a payout was paused.

**Checklist**

- [ ] The payout history shows the pause for a payout that is paused, so QA can verify it there
