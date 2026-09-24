The answers give enough direction: standalone task, the WHAT, the WHY and three acceptance conditions. Task Mode resumes, and the flat numbered-group shape fits because the task carries three testable outcomes and no design links or dependencies were supplied.

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

---

Export-equivalent path: `export/002 - task-creator-payout-pause.md`

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: the bold `**Checklist**` and numbered-group labels, which the Task template fixes, and the supplied acceptance wording, which Accuracy requires to stay faithful.

Quality: pass. All six floors clear, Actionability leading as the Task shape expects, every checklist item ending in something a tester can observe. Structure, WHAT/WHY focus, HVR and factual safety all checked.

Summary: a standalone task with About plus three numbered requirement groups, one per supplied acceptance condition. The reason requirement carries the supplied "reason field" wording, the indicator group covers both the paused and the not-paused case so the criterion is testable in both directions, and the payout history group covers QA's verification path. No references, epic or related-ticket sections were added because none were supplied or named.

Two assumptions you can correct: the payout row is the creator-facing payouts list, and the payout history is the existing surface QA already uses. Neither had a supplied link, so neither got a fabricated URL.

Next step: if you want this adjusted, name the group and the change. The clarification block above stays as delivered and this file keeps its lane number.