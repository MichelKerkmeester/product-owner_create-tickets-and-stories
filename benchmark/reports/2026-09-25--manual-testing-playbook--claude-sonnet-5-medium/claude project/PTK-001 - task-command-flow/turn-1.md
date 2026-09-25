Task Mode needs scope, requirements and acceptance criteria before I draft. Your request names only the feature, so I'm asking one question first. The question is in the block below.

````markdown
I'll create your task. Quick questions:

**Format & scope:** Is this Backend, Frontend, Mobile, Full-stack, DevOps or QA work? Is it one task, or a parent task with subtasks?

**Requirements:** What should the creator payout pause do?
- Who can pause and resume payouts (admin, support, the creator, an automated rule)?
- What triggers a pause (manual action, fraud or compliance flag, disputed payment, missing payout details)?
- Does a pause apply to one creator or a group of creators, and to all payouts or only pending ones?
- What happens to earnings while paused (accrue, hold, expire) and when payouts resume?
- Is the creator notified, and does anyone see the pause reason?

**Why it matters:** What problem does this solve today, and what does success look like?

**Acceptance criteria:** Which observable outcomes must QA be able to verify? Please include any edge cases you already know, such as a pause during a payout run in progress.

**Design & platform:** Figma links? Platforms (iOS / Android / Web / All)?

**Dependencies:** Related or dependent tickets, for example the payout provider, ledger or notification work?

**Validation:** What am I likely to misunderstand about this feature? Is a pause definitely the right model, or would a different approach (for example a payout hold or a per-payout block) fit better?
````

Export-equivalent path: `export/NNN - task-creator-payout-pause-clarification.md`

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.

Once you answer, I'll draft the task as a new block with the next number in the task lane. If you'd rather skip intake, resend with `$quick` and I'll draft from safe defaults. I'd have to assume the pause rules, so I'd flag those assumptions in my reply.