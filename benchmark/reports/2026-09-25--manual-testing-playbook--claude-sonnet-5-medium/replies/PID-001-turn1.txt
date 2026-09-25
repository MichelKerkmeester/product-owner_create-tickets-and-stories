Deliverable Block (Canvas Artifact):

````markdown
<!-- Mode: Task | Template: Quick Task v0.101 | Energy: Quick -->
# Add a 24-hour pause toggle for pending payouts

### About

---

Brands need a way to hold a pending creator payout while they resolve a problem with the deliverable or the deal. Add a pause toggle that holds a pending payout for 24 hours and requires a reason, so every pause is explained. Show the creator a banner so a held payout is never a surprise.

### Requirements

---

1.  **Payout pause toggle**

---

Brands can pause a pending payout for 24 hours. The pause applies only to a payout that is still pending.

**Checklist**

- [ ] The toggle appears on a pending payout
- [ ] The toggle does not appear on a payout that is no longer pending
- [ ] Turning the toggle on with a valid reason pauses the payout for 24 hours
- [ ] Turning the toggle on without a valid reason does not pause the payout
- [ ] A paused payout is not released during the 24-hour window
- [ ] The payout returns to its normal pending flow when the 24 hours end
- [ ] The paused state persists after a page refresh and on a new session
- [ ] The toggle shows a clear on and off state

---

2.  **Pause reason field**

---

The reason is required so the pause can be audited and explained to the creator.

**Checklist**

- [ ] The reason field is shown when the brand turns the toggle on
- [ ] The field is marked as required
- [ ] Submitting with an empty field is blocked and shows an inline error
- [ ] Submitting with only whitespace is treated as empty
- [ ] The entered reason is saved with the pause
- [ ] The saved reason is visible to the brand on the paused payout
- [ ] Cancelling before submitting leaves the payout unpaused and clears the field

---

3.  **Creator banner**

---

Creators must see that their payout is paused so they are not left guessing when it will arrive.

**Checklist**

- [ ] A banner appears for the creator while their payout is paused
- [ ] The banner states that the payout is paused
- [ ] The banner states when the pause ends
- [ ] The banner is not shown for a payout that is not paused
- [ ] The banner disappears when the 24-hour pause ends
- [ ] The banner text matches the pause state after a page refresh
````

Export-equivalent path: `export/NNN - task-payout-pause-toggle.md`

HVR self-scan: 0 hard blockers. Fixed: none needed. Kept with reason: none.

Quality: Quick energy, so no intake question. The task covers WHAT and WHY only and has no `[Assumes]` tags or process material in the body.

Assumptions to correct:
- **Early unpause:** the brief only says "24 hours", so I didn't add a way for the brand to lift a pause early.
- **Reason visibility:** I made the reason visible to the brand only. Say so if the creator banner should show it.
- **Banner copy:** I didn't write the wording. The checklist only requires that the banner says the payout is paused and when the pause ends.
- **Repeat pauses:** I didn't cap how many times a brand can pause the same payout.
- **Related links:** I didn't add Epic, Figma or related-task links because none were supplied.

If the ClickUp connector is available, I can publish this to ClickUp once you approve it. Nothing has been pushed.