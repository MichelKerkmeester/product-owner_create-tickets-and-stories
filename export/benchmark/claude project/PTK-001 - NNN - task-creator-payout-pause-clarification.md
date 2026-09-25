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
