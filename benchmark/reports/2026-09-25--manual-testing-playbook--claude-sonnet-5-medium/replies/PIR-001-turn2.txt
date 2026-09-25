````markdown
<!-- Mode: Task | Template: Quick task v0.101 | Energy: Quick -->

# Show payout pause reason and date on the payout detail screen

### About

---

When a payout is paused, creators currently have no way to see why. They wait, then contact support to ask. Show the reason and the date the payout was paused on the payout detail screen, so creators can understand the status themselves and know what to do next.

### Requirements

---

**Show the pause reason and pause date for paused payouts**

---

A creator who opens the detail screen of a paused payout must see the reason it was paused and the date the pause started, without leaving the screen. Payouts that are not paused stay unchanged.

**Checklist**

- [ ] A paused payout shows its pause reason on the payout detail screen
- [ ] A paused payout shows the date it was paused on the payout detail screen
- [ ] The reason and the date appear together and are clearly tied to the paused status
- [ ] The date uses the same date format as the other dates on the payout detail screen
- [ ] Payouts that are not paused show no pause reason or pause date
- [ ] When a paused payout has no recorded reason, the screen still shows the paused status and the pause date, with no empty or broken reason area
- [ ] The reason shown is the one recorded for that payout's current pause, not an earlier one
- [ ] Keep the rest of the payout detail screen, including layout, amounts and other statuses, unchanged
````

Export-equivalent path: `export/NNN - task-payout-pause-reason-detail-screen.md`

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.

Quality status: Quick energy, one perspective (the creator). The task states WHAT and WHY with a testable checklist, and it names no implementation.

Assumptions you can correct:
- **Creator-facing reasons.** I assumed the stored pause reason is already suitable to show creators. If it can hold internal or sensitive wording, I'd add a requirement for creator-safe copy.
- **Missing reason.** I did not invent fallback text. The task only requires that the screen stays clean. If you want specific copy, send it and I'll add it.
- **Scope.** This covers the payout detail screen only. I left out the payout list, notifications and any "what to do next" guidance.
- **Design links.** I added no References, Epic or Related tickets because none were supplied. Send the Figma link or parent epic name if you want them included.

Next step: save the file under the next `NNN` number, or tell me what to change.