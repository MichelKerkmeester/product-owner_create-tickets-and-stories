# Creator payout pause indicator

### About

---

A pending payout can be paused, but a creator looking at their payouts has no way to tell it is paused, and nothing records why. This task makes a pause visible in the payout row and stores the reason with it, so a creator can see that a payout is on hold and the team can later see why it was put on hold.

The pause reason is required. A pause with no recorded reason cannot be explained to the creator or checked afterwards, which is why the reason is a condition of pausing and not an optional note. QA needs to confirm the pause from the payout history, so the history has to show it too.

This task covers the indicator, the required reason and their appearance in payout history. Who is allowed to pause a payout and how a pause ends are not part of it.

**References**

---

Page

- `Creator payouts`

### Requirements

---

1.  **Pause reason**

---

Pausing a pending payout requires a reason, and that reason is stored with the pause so it can be read back later.

**Checklist**

- [ ] The reason field is required when a pending payout is paused
- [ ] A pause with an empty reason is rejected and the payout stays unpaused
- [ ] The saved reason is stored with the pause and can be retrieved for that payout

2.  **Pause indicator**

---

A creator needs to see at a glance which pending payouts are on hold, so the indicator sits in the payout row itself and not on a separate screen.

**Checklist**

- [ ] A paused pending payout shows a pause indicator in its payout row
- [ ] A pending payout that is not paused shows no pause indicator
- [ ] The indicator is on the payout row for each paused payout when several payouts are listed

3.  **Payout history**

---

QA has to verify a pause without reading the database, so the pause is part of the payout history.

**Checklist**

- [ ] The payout history records that the payout was paused
- [ ] The payout history shows the stored pause reason for that payout
- [ ] QA can confirm a pause end to end: pause with a reason, see the indicator in the row, then find the pause and its reason in the history
