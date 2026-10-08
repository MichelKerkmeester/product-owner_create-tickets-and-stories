```markdown
# Stay limits in the date picker, before drafting

I'll create the FE task for the stay limits from Ines's handover notes. The notes cover the states, copy, platforms and exclusions, so these questions cover only what they leave open. Please answer them all in one reply.

**1. Title and feature code**

- Shall I use `FE - Guest app - SRCH - Stay limits in the date picker` as the title?
- The picker sits under `SRCH`, but the property page sits under `PROP`, so should the task stay `SRCH`?

**2. Where the limits come from**

- The 30-night and 365-day limits come from search-service config, so can the Guest app read them today?
- If it cannot, which ticket brings those values to the apps?
- The property minimum comes with the property details, so is it already in the property page data?

**3. Values that fail to load**

- When a limit can't load, should the picker stay open with no limit applied, or block selection until it loads?

**4. Saved dates under a property minimum**

- A saved range that breaks a limit is cleared, so should a range shorter than the property minimum be cleared too?

**5. Time zone for today**

- The 365-day window counts from today, so should today follow the guest's device time zone?

Unless you say otherwise, I'll use the device time zone.

**6. Figma reference**

- Please send the link to the `Date picker / Stay limits` frame for References.

Once you reply, I'll draft the task as a new Deliverable Block.
```

Export-equivalent path: export/NNN - task-stay-limits-date-picker-clarification.md

Quality status: clarification only, no draft yet.

The handover notes arrived and cover the states, copy, edge cases and exclusions, so the question covers only the gaps: title and feature code, where the limit values come from, what happens when a value fails to load, saved dates under a property minimum, the time zone for "today" and the Figma link. I've proposed `SRCH` and the device time zone, so reply with a change if either is wrong. The task comes next as a new Deliverable Block once you answer.

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.