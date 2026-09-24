```markdown
# Show why a payout was paused on the payout detail screen

<!-- Task Mode - Quick Task Template v0.100 - quality gate: all six floors pass -->

### About

---

When a payout is paused, the payout detail screen does not tell the creator why. Creators then contact support for an answer the payout record already holds. Show the pause reason and the pause date on the payout detail screen so creators can see why their payout paused without asking anyone.

### Requirements

---

**Show the payout pause reason and pause date**

---

The payout detail screen is where a creator inspects a payout. When that payout has been paused, the screen should state the reason for the pause and the date the payout was paused.

**Checklist**

- [ ] Show the payout's pause reason on the payout detail screen for a payout that has been paused
- [ ] Show the date the payout was paused next to the reason
- [ ] Use the reason and the pause date stored on the payout record
- [ ] Show no pause reason and no pause date for a payout that was never paused

> Display only. This task adds no new pause reason and does not change when a payout pauses.
```

---

**Export-equivalent path:** `export/002 - task-payout-pause-reason-on-detail-screen.md`

**Quality status:** Quick energy, Task Mode, all six dimension floors pass with the gate reported as checked. Actionability decides it: every checklist item names an observable end state a QA pass can confirm. WHAT and WHY only, so no HOW such as component choice or screen layout appears.

`HVR self-scan: 0 hard blockers. Fixed: no banned terms were used, so nothing needed replacing. Kept with reason: straight quotes, sentence-case headings and checklist items without trailing full stops, each required by the Human Voice card, and the "payout" wording repeats by design because synonym cycling is the violation, not the obedience.`

**Assumptions, correctable:** The reason and pause date are already stored on the payout record, since your request names both as things to show. This is display-only, with no new pause reasons and no change to pause behavior. No platform was specified, so the task names none.

If any of that misses, tell me and I will revise. Otherwise the task is backlog-ready as it stands, and it takes the next number after the clarification if you save it into the same lane.