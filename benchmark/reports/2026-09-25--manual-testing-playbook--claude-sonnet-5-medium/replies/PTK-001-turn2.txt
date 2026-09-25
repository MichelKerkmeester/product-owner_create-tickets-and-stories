````markdown
# Show a pause indicator on pending creator payouts and store the pause reason

### About

---

Creators cannot tell when a pending payout has been paused, and the reason for a pause is not recorded anywhere a team member can check later. This leaves creators guessing about their money and leaves support and QA without evidence of why a payout stopped.

Show a pause indicator on each paused pending payout in the payout row, require a reason whenever a payout is paused and keep that reason on record. The pause and its reason must be verifiable in the payout history. Who can pause a payout, what triggers a pause and how a payout is resumed are out of scope for this task.

### Requirements

---

1.  **Store a required pause reason**

---

A payout cannot be paused without a reason. The reason is kept with the pause so anyone reviewing the payout later can see why it was paused.

**Checklist**

- [ ] Require the reason field whenever a pending payout is paused
- [ ] Block the pause and show a validation message when the reason is empty
- [ ] Block the pause when the reason contains only whitespace
- [ ] Store the reason with the paused payout so it persists after a page reload and a new session

**User Story**

- **Given:** A pending payout that is not paused
- **When:** The payout is paused without a reason
- **Then:** The pause is rejected and the payout stays unpaused

---

2.  **Show the pause indicator in the payout row**

---

Creators need to see at a glance which pending payouts are paused. The indicator sits in the payout row so no extra screen is needed to find it.

**Checklist**

- [ ] Show the pause indicator in the payout row of every paused pending payout
- [ ] Show no indicator on pending payouts that are not paused
- [ ] Keep every other element of the payout row unchanged, including amount, date and status
- [ ] Remove the indicator when the payout is no longer paused
- [ ] Give the indicator an accessible text label so it is not conveyed by color or icon alone

---

3.  **Make the pause verifiable in payout history**

---

QA and support must be able to confirm that a pause happened and why, without database access.

**Checklist**

- [ ] Show each pause as an entry in the payout history of the affected payout
- [ ] Include the stored pause reason in the history entry
- [ ] Include the date and time the pause was recorded in the history entry
- [ ] Confirm the history entry matches the reason entered when the payout was paused
- [ ] Confirm the history shows no pause entry for a payout that was never paused
````

Export-equivalent path: `export/NNN - task-creator-payout-pause-indicator.md`

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.

**Quality summary:** The task reads as a standard, standalone feature task. It covers WHAT and WHY only, and the acceptance conditions are testable. That includes the three you gave: a required reason, the indicator in the payout row and the pause verifiable in payout history.

**Assumptions to correct if wrong:**
- Who can pause, what triggers a pause and how a payout is resumed are out of scope. You didn't mention them.
- I treated "not yet paused" and "no longer paused" as the only two states, so the indicator disappears when a payout is no longer paused.
- The pause reason appears in payout history for QA. I did not say whether creators see it in the payout row.
- The whitespace-only rejection, the validation message and the accessible label are my additions from edge-case checks. Remove any you don't want.
- I left out References, Epic and related tickets because none were supplied. Send links if you have them.

The reply is also missing a task-lane number for `NNN`, so you'll need to set it when you save the file.