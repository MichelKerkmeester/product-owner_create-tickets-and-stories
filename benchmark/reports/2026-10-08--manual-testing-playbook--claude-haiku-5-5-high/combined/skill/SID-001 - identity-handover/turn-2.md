Path: export/002 - task-due-today-filter-chip.md
Verified: read-back succeeded; 45 lines
HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.

Quality summary: a standalone Task in the Quick shape with two requirement groups, one for the chip and one for analytics. Every checklist item is a check a build can pass or fail, and the only source values are the ones you gave plus the context page's `filter_selected` and owner's time zone rules.

The task covers the Due today chip on Web, after Overdue, with its filter rules and the `due_today` analytics event. Desktop is covered through the web client, and iOS and Android are listed as out of scope. The clarification file (001) is unchanged.

Additions to strike if they are wrong:
- The "why" sentence in About, that a member can see today's open to-dos with one click, is my inference from the chip's purpose. You did not state a reason.
- "The All chip stays the default active chip" comes from the context page, not your message.
- "The other chips keep sending their current filter values" is a regression check I added.

Not specified and not added: empty-state copy for when no to-dos are due today.