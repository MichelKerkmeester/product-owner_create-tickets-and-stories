```markdown
I'll write the Android subtask for Recurring to-dos. The parent and the board context cover most of it. Please answer the points below in one reply:

**Format & scope:**
- The parent lists the title as `FE - Android - TODO - Recurring to-dos`, with `FS - TODO - Recurring to-dos` as its parent. Should I keep both as written?
- The subtask can repeat the shared rules Android has to meet (repeat options, ends, occurrences, limit, time zone, plans and tracking). It can also point to the parent and list only what Android must show and do. Which do you want?
- Does Android only show the next occurrence that `BE - TODO - Recurrence engine` creates? Or does the app work out any date itself, such as a preview of the next due date in the Repeat picker?

**Requirements:**
- Reminders: Android sets up reminders as local notifications on the device. When checking off a to-do or using Skip this one creates the next occurrence, is there anything Android-specific to cover? One example is cancelling the old occurrence's notification.
- Upgrade sheet: billing changes can only be made on Web. What should the upgrade sheet on Android do for a Free workspace? Does every role see the same sheet, or only the Owner?
- Connection loss: there is no offline mode, and the app retries an offline edit until it closes. Should the next occurrence appear as soon as the member checks off the current one, or only after the engine confirms it?
- Guests with edit access: can they set or change Repeat?
- Acceptance: beyond the parent's rules, what must QA check? For example tablet layout, the six locales or Android 9.

**Design & platform:**
- Do you have Figma links for `Recurring to-dos / Repeat picker`, `Recurring to-dos / Custom interval` and `Recurring to-dos / Occurrence menu`? If not, I'll list the flow names as plain text.
- Is there translated copy for `Add a due date to repeat` and the 500-limit sheet? If not, those strings ship in en-US only and other locales fall back to en-US.

**Dependencies:**
- Does Android have to wait for `BE - TODO - Recurrence engine`, or can it be built in parallel behind `recurring_todos`?
- Is there a target Android release, or should I leave it open?

**Validation:**
- Has anything in the parent changed since Ines last edited it on 2026-09-18?
```

Export-equivalent path: `export/001 - task-android-recurring-todos-clarification.md`

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.

**Quality status:** This is a clarification only, so there's no artifact score yet. I asked all the open questions in one message and haven't answered any of them myself.

**Why I'm asking first:** `$task --subtask` means I ask before drafting. I've read the parent task and the Loomlist context page. Most of the questions come from gaps between the two:
- **Upgrade path:** the parent says Free workspaces get an upgrade sheet, but billing changes can only be made on Web.
- **Reminders:** Android schedules reminders as local notifications, so it's unclear how they carry over to each new occurrence.
- **Offline check-off:** there's no offline mode, so it's unclear when the next occurrence should appear.
- **Not covered:** the parent doesn't say whether guests can use Repeat, and it doesn't give translated copy.

I'll write the Android subtask once you've answered.