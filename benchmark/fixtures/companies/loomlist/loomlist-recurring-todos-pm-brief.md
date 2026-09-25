# Recurring to-dos, PM brief

Brief from Ines, Product Manager, To-dos and Reminders. Posted in the To-dos team space on 2026-09-08.
For the iOS, Android, Web and BE engineers on To-dos and Reminders, and for Design. Talked through at planning on 2026-09-10, and the answers from that session are folded in below.

## Why now

Repeating to-dos are the most requested to-do feature we have. The feedback board holds 212 requests since January, and 38 Plus workspaces named it in the renewal survey as the reason they keep a second app for chores and routines. Today people copy a to-do by hand every week, or set a reminder far ahead and keep moving it.

## What members get

A to-do with a due date can repeat. The member opens the to-do's detail sheet and taps Repeat. A to-do without a due date shows Repeat greyed out with the hint `Add a due date to repeat`.

| Option | Next due date |
|--------|---------------|
| Daily | The next day |
| Weekdays | The next weekday, Monday through Friday |
| Weekly | Same weekday next week |
| Monthly | Same day next month |
| Custom | Every N days, weeks or months, with N from 1 to 99 |

Monthly keeps to the day of the first due date. A series that starts on the 31st lands on the 30th in April and on the 31st again in May.

Ends sits under Repeat and has three choices:
- Never, the default
- On date, which stops the series after the last occurrence on or before that date
- After, which stops the series after a set number of occurrences, from 1 to 365

Only one occurrence exists at a time. When the member checks it off, the next one appears on the same page with the next due date. Assignee and reminder carry over, and the reminder keeps the same local time.

The to-do's menu gets Skip this one. It moves the to-do to its next due date without marking it done. A skipped occurrence still counts toward an After limit.

## Limits

A workspace can hold 500 repeating to-dos that have not ended. At that point Repeat stays visible but opens a sheet that says `This workspace has 500 repeating to-dos. End one to add another.` Checked-off and ended series do not count.

## Time zones

Next due dates are worked out in the owner's time zone, the same rule the Overdue chip and reminders follow. If the to-do is reassigned, the next occurrence uses the new owner's zone. A teammate in another zone sees the owner's date with the zone shown.

## Plans and rollout

Repeat is for Plus and Team workspaces. On Free it shows with a Plus badge and opens the upgrade sheet.

Everything ships behind the workspace flag `recurring_todos`. iOS, Android, Web and BE all ship dark first. Once all three clients are out, Data turns the flag on for a sample of Plus and Team workspaces and widens it from there.

We call it working when 10% of weekly active Plus and Team workspaces have at least one repeating to-do 8 weeks after the flag is on for everyone.

## Who builds what

| Area | Owner | Scope |
|------|-------|-------|
| iOS | FE, To-dos and Reminders | Repeat and Ends pickers, Custom interval, Skip this one, repeat icon on the to-do row |
| Android | FE, To-dos and Reminders | Same as iOS |
| Web | FE, To-dos and Reminders | Same as iOS. Desktop gets it through the web client |
| BE | BE, To-dos and Reminders | Next occurrence on check-off and skip, Ends, the 500 limit, handing the next reminder to reminders-service |

Design frames are `Recurring to-dos / Repeat picker`, `Recurring to-dos / Custom interval` and `Recurring to-dos / Occurrence menu`. Anouk has them ready for review.

## Tracking

Data wants two events. `todo_repeat_set` carries `repeat` set to `daily`, `weekdays`, `weekly`, `monthly` or `custom`. `todo_occurrence_skipped` fires on Skip this one. Yara reviews the tracking plan before client work starts.

## Out of scope

- Repeating a whole page or a database row
- Repeating from the date the to-do was checked off, as in every 3 days after I finish
- A different time for each weekday
- Any Support console change

## Still open

Whether a series shows its past occurrences in the to-do's activity. Not needed for the first release. I will decide after the flag reaches everyone.
