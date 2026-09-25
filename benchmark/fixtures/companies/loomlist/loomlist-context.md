# Loomlist product context

Internal context page kept by Elif, Product Operations, in the Product space. Last updated 2026-09-22.
Read it before writing a ticket, a doc or a brief for any Loomlist team. Ask Elif when something here looks wrong.

## Product and surfaces

Loomlist is a workspace app for pages, databases and to-dos. A workspace holds pages and a page holds blocks. A block can be text, a heading, a to-do, an image, a file or an inline database. Members work in the same workspace from any surface, and sync-service keeps every device on the same version of each block.

| Surface | What it is | Who uses it |
|---------|------------|-------------|
| Desktop | App for macOS and Windows. It wraps the web client in a native window and adds a quick capture shortcut and its own update channel | Members who keep Loomlist open all day |
| Web | The web client in a browser, deployed several times a week | Everyone, and the only surface for billing changes |
| iOS | Native app for phones and tablets | Members on the move, mostly reading and checking off to-dos |
| Android | Native app for phones and tablets | Same as iOS |
| Support console | Internal back office for the Support team | Support agents and the Support lead |

Desktop adds nothing of its own beyond the capture shortcut. A change to the web client reaches Desktop users the next time Desktop loads, with no Desktop release.

## Personas and roles

Workspace roles decide what a person can do in one workspace. A person can hold a different role in each workspace they belong to.

| Role | Can do | Billed |
|------|--------|--------|
| Owner | Everything an Admin can, plus billing, plan changes and deleting the workspace. One per workspace | Yes |
| Admin | Invite and remove members, change workspace settings, see every page | Yes |
| Member | Create, edit and share pages they can open | Yes |
| Guest | Open only the pages shared with them, with view or edit access as set by the sharer | No |

Plans are set per workspace.

| Plan | Price | Members | Page history |
|------|-------|---------|--------------|
| Free | No charge | Up to 5 members | 7 days |
| Plus | €8 per member per month | No limit | 30 days |
| Team | €14 per member per month | No limit | 90 days, plus an audit log and workspace-wide sharing controls |

Personas the teams write for:
- Dana, a freelancer planning client work alone on Free
- Theo, who runs a 12-person agency on Plus and assigns to-dos across projects
- Mireille, operations manager at a 60-person company on Team, who cares about access and audit
- The support agent, who works tickets in the Support console and can see workspace settings, plan, devices and sync status, but not page content without a support access grant from the Owner

## Glossary

| Term | Meaning |
|------|---------|
| Workspace | The top container. Holds pages, members, guests, a plan and settings |
| Page | A document made of blocks. Pages nest, so a page can hold sub-pages |
| Block | One unit on a page: text, heading, to-do, image, file, embed or inline database |
| Database | A page whose rows are pages, with typed properties and saved views |
| View | A saved filter and sort over a database, shown as a table, board or calendar |
| To-do | A block with a checkbox, an optional due date, an optional assignee and an optional reminder |
| To-do owner | The member a to-do is assigned to, or its creator when it has no assignee. Not the workspace Owner role |
| To-dos view | The workspace-wide list of every to-do the member can open, with filter chips on top |
| Reminder | A time on a to-do when Loomlist tells the to-do owner about it |
| Share | Giving a member or a guest access to a page, with view or edit access |
| Sync session | One exchange between a device and sync-service: the device uploads changed blocks and pulls newer ones |
| Conflict | Two devices changing the same block between their sync sessions |
| Page history | Earlier versions of a page, kept for the window the plan allows |
| Mention | Typing @ and a member name in a page or comment |

## Services and integrations

| Service | Owns | Notes |
|---------|------|-------|
| pages-service | Pages, blocks, databases, views, page history | Every other service reads block data through it |
| todos-service | To-dos, due dates, assignees, the To-dos view queries | Reads the to-do owner's time zone from the member profile |
| sync-service | Sync sessions, device cursors, conflict handling | Protocol v3, block-level last-writer-wins |
| reminders-service | Reminder storage and the UTC time each reminder is due | Hands the due time to each device of the to-do owner |
| notifications-service | Email and push notifications | Email goes out through the email delivery provider |
| share-service | Page access, member and guest invites, access checks | Answers every "can this person open this page" question |
| billing-service | Plans, seats, invoices | Card payments go through the payment provider |
| analytics-ingest | Client and server events | Feeds the warehouse the Data team queries |

Reminders reach people in two ways. On iOS and Android the app schedules them as local notifications on the device, from the UTC time reminders-service hands over. On Web and Desktop a reminder shows in the app only, as a banner and a badge on the To-dos view, and only while the app is open.

Push notifications for mentions, comment replies and shares go out through each mobile platform's push service. Nothing else in the product sends push.

## Teams and discipline codes

| Team | Covers | Lead |
|------|--------|------|
| Pages and Databases | PAGE, DB | Hugo, Engineering Manager |
| To-dos and Reminders | TODO, REM | Ines, Product Manager |
| Sync | SYNC, OFFL | Joana, Engineering Manager, Sync |
| Sharing and Notifications | SHARE, NOTIF | Lena, Product Manager |
| Mobile Platform | iOS and Android releases | Oskar, Product Manager, Mobile |
| Support Tools | Support console | Farid, Engineering Manager |
| Data | Tracking plans, dashboards | Yara, Data Lead |

Every task and bug carries one discipline code:

| Code | Meaning |
|------|---------|
| FE | Front end work in one client: Desktop, Web, iOS or Android |
| BE | Back end work in one or more services |
| BO | Support console work |
| FS | Work that needs front end and back end changes together, or a parent that splits into both |
| DATA | Tracking plans, events, dashboards |
| DS | Design system components and tokens |

Task and bug titles follow `{Discipline} - {Platform} - {Feature code} - {Title}`. Platform is Desktop, Web, iOS or Android. Work with no single platform drops that segment, which covers all BE, BO, DATA and DS work and any FS parent that spans platforms.

Examples:
- `FE - Android - REM - Snooze from the notification`
- `FE - Web - DB - Calendar view drag to reschedule`
- `BE - SYNC - Retry budget for stalled uploads`
- `BO - SHARE - Show guest access in the Support console`

Story and epic titles carry no discipline code and no feature code. They read as a path to the work, such as `Member - To-dos - Bulk complete` or `Epic - Platform - Workspace templates`.

## Feature codes

| Code | Area |
|------|------|
| PAGE | Pages, blocks, nesting, page history |
| DB | Databases, properties, views |
| TODO | To-dos, the To-dos view, due dates, assignees |
| REM | Reminders |
| SYNC | Sync protocol, devices, conflicts |
| SHARE | Sharing, invites, guest access |
| NOTIF | Email and push notifications |
| OFFL | Behavior without a connection |
| BILL | Plans, seats, invoices |

## Platforms and app versions

| Platform | Version | Released | Minimum OS |
|----------|---------|----------|------------|
| iOS | 5.3.2 | 2026-09-15 | iOS 16 |
| Android | 5.3.0 | 2026-09-02 | Android 9 |
| Desktop | 5.3.1 | 2026-09-09 | macOS 13, Windows 10 |
| Web | No store version | Deploys continuously | Current and previous major version of each supported browser |

iOS and Android ship every two weeks and roll out over 7 days. Desktop 5.3.1 is the version of the native shell only. The web client inside it is whatever build Web runs that day, so a Desktop bug report names both the shell version and the web build.

Web sends its build number where the apps send a version, for example `web-2026.09.22.3`.

## Currencies and locales

Plan prices are set in EUR and listed per currency in the billing price list, never converted at checkout.

| Currency | Notes |
|----------|-------|
| EUR | Default |
| USD | |
| GBP | |
| JPY | No minor unit, amounts in whole yen |
| BRL | |

A workspace's billing currency is fixed at its first payment.

The app ships in en-US, de-DE, fr-FR, es-ES, ja-JP and pt-BR. en-US is the default and the fallback for a missing string. Dates and times follow the member's locale. The week starts on Sunday for en-US, ja-JP and pt-BR, and on Monday for de-DE, fr-FR and es-ES.

Due dates, the Overdue chip and reminders all use the owner's time zone, meaning the to-do owner's profile time zone, set from the device at sign-up and changeable in profile settings. A member viewing someone else's to-do sees its date in the owner's time zone, with the zone shown when it differs from their own.

## Key flows

**Add a to-do.** A member types `[]` or picks To-do from the block menu. They can add a due date, an assignee and a reminder from the to-do's detail sheet. The to-do appears in the To-dos view for everyone who can open its page.

**Filter the To-dos view.** Three chips sit above the list: All, Assigned to me and Overdue. One chip is active at a time and All is the default. Overdue shows to-dos not checked off whose due date is before today in the owner's time zone. The list sorts by due date, and to-dos with no due date sit at the bottom.

**Get a reminder.** The member picks a local date and time. reminders-service turns it into a UTC time and hands it to every device the to-do owner is signed in on. iOS and Android schedule local notifications. Web and Desktop show the reminder in the app only.

**Share a page.** From the Share panel a member invites a member or a guest by email and picks view or edit access. share-service checks access on every open. A guest sees only the pages shared with them and never the workspace sidebar.

**Edit on two devices.** Each device uploads changed blocks in a sync session and pulls newer ones. When two devices change the same block between their sync sessions, sync-service keeps the version that reaches it last. The other edit is not kept anywhere, including page history.

**Receive email.** notifications-service sends mention, comment reply, share, invite and summary emails through the email delivery provider. Each member manages their emails in their notification settings.

## Known constraints

- There is no offline mode. The mobile apps keep the open page on screen but cannot open another page without a connection
- An edit made while the connection is gone is retried until the app closes, then lost
- Sync protocol v3 has no merge and no conflict copy. Changing the protocol needs every client on a version that speaks the new one
- Reminders on Web and Desktop show in the app only, so a member with the app closed gets nothing
- Pages are shared by invite only. There is no public link to a page
- Page history keeps what reached sync-service. An edit that lost a conflict never appears in it
- A database holds up to 50,000 rows and a page up to 10,000 blocks
- The Support console cannot open page content without a support access grant from the workspace Owner

## Analytics conventions

- Event names follow `object_action` in snake_case with the action in the past tense, for example `page_created`, `todo_completed`, `reminder_set` and `filter_selected`
- Every event carries `workspace_id`, `user_id`, `platform`, `app_version` and `plan`
- `user_id` is hashed before it leaves the client, and page titles and block text never go into an event
- Enum values are lowercase snake_case, so the To-dos view sends `filter_selected` with `filter` set to `all`, `assigned_to_me` or `overdue`
- Timestamps are UTC in ISO 8601 and the server adds `received_at`
- New events go into a tracking plan the Data team reviews before any client work starts
