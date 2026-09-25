<!-- Mode: Task | Template: quick task v0.101 | Energy: Quick -->

# Payout pause toggle

### About

---

Brands can pause a pending payout for 24 hours when something needs checking before the money moves. The pause needs a reason, so the brand states why it is holding the payout, and the creator sees a banner, so a delayed payout is never a silent surprise.

This task covers the toggle, the required reason field and the creator banner. QA verifies each of the three through the checklists below.

### Requirements

---

1.  **Pause toggle**

---

A brand turns the pause on for a pending payout and the payout holds for 24 hours. The toggle applies to pending payouts only, because a payout that is no longer pending has nothing left to hold.

**Checklist**

- [ ] The toggle is available on a pending payout
- [ ] The toggle is not available on a payout that is not pending
- [ ] Turning the toggle on with a valid reason pauses the payout for 24 hours
- [ ] A paused payout shows the paused state to the brand
- [ ] The payout does not move while the pause is active
- [ ] The payout returns to pending when the 24 hours end
- [ ] Turning the toggle off during the pause ends the pause

---

2.  **Required reason field**

---

The reason is mandatory, so the pause cannot start without one. This keeps every pause explainable to the creator and to the team reviewing it later.

**Checklist**

- [ ] The reason field is shown when the brand turns the toggle on
- [ ] The pause cannot be confirmed while the reason is empty
- [ ] A reason made only of spaces counts as empty
- [ ] An empty reason shows an error message on the field
- [ ] The entered reason is saved with the pause
- [ ] Cancelling before confirming leaves the payout unpaused and discards the reason

---

3.  **Creator banner**

---

The creator sees a banner on a payout that is paused, so the delay is explained where they look for their payout. The banner exists only while the pause is active.

**Checklist**

- [ ] The banner appears for the creator when the pause starts
- [ ] The banner shows only on the paused payout
- [ ] The banner tells the creator the payout is paused
- [ ] The banner disappears when the pause ends after 24 hours
- [ ] The banner disappears when the brand turns the pause off early
- [ ] A payout that was never paused shows no banner
