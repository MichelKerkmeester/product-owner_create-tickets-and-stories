```markdown
# Stay limits in the date picker, one question left

Thanks. The scope is set: one FE task for iOS, Android and web, no parent, Search squad, 8.13.0 train, search-service unchanged, and QA in en-GB and en-US. Three gaps remain, and the acceptance criteria depend on them.

**1. Where the apps get the limits**

- Can the apps already read the 30-night limit, the 365-day window and the property minimum, and from which field?
- If they cannot, which ticket delivers those values, given that search-service stays unchanged?

**2. When a value fails to load**

- When a limit can't load, should the picker stay open with no limit applied, or block selection until it loads?

**3. Saved dates under a property minimum**

- A saved range that breaks a limit is cleared, so should a range shorter than the property minimum be cleared too?

**4. Defaults I'll apply**

Unless you say otherwise, I'll use `SRCH` as the feature code, the device time zone for "today", and the frame name `Date picker / Stay limits` without a link. Once you reply, I'll draft the task as a new Deliverable Block.
```

Export-equivalent path: export/NNN - task-stay-limits-date-picker-clarification.md

Quality status: clarification only, no draft yet.

The scope answers are recorded. Three questions remain because the acceptance criteria turn on them: whether the apps can read the limit values today, what the picker does when a value fails to load, and how a saved range under a property minimum is treated. I've also applied the earlier defaults, `SRCH` and the device time zone, and named them in the block so you can strike either one.

One note for the train: Android shipped as 8.12.1 for the 8.12 train because the store turned back 8.12.0. If 8.13.0 follows that pattern, the Android build may read 8.13.1, so the task will name the train without per-platform build numbers.

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.