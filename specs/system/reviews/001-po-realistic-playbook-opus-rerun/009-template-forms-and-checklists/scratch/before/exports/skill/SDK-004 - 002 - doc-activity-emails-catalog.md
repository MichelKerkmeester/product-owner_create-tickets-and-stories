# Loomlist activity emails

* * *
> Status: Current behavior — the six activity emails notifications-service sends, EM-01 to EM-06
* * *

## Overview
* * *

The six emails Loomlist sends about workspace activity, two scheduled and four sent the moment something happens.

Support agents use it to see why an email did or did not arrive, Notifications engineers to find its template, variables and job before a change. Push notifications, reminders and sign-in, receipt and plan emails are not covered.

### Index
* * *

| ID | Email | Template | Sent | Can be turned off |
| ---| ---| ---| ---| --- |
| `EM-01` | [Daily digest](#em-01-daily-digest) | `tpl_digest_v4` | Daily 08:00, local time | Yes |
| `EM-02` | [Mentioned in a page](#em-02-mentioned-in-a-page) | `tpl_mention_v2` | On event | Yes |
| `EM-03` | [Comment reply](#em-03-comment-reply) | `tpl_comment_reply_v2` | On event | Yes |
| `EM-04` | [Page shared with you](#em-04-page-shared-with-you) | `tpl_page_shared_v3` | On event | Yes |
| `EM-05` | [Workspace invite](#em-05-workspace-invite) | `tpl_workspace_invite_v5` | On event | No |
| `EM-06` | [Weekly summary](#em-06-weekly-summary) | `tpl_weekly_summary_v1` | Monday 09:00, local time | Yes |

### Rules that apply to all six
* * *

*   **Sender** — Loomlist, through the email delivery provider
*   **Local time** — The time zone on the recipient's profile
*   **Language** — The app language, from en-US, de-DE, fr-FR, es-ES, ja-JP and pt-BR, with en-US for missing strings
*   **Mention in a reply** — Sends EM-02 only, never EM-03 too
*   **Guests** — EM-02, EM-03 and EM-04 for pages shared with them, never EM-01 or EM-06
*   **Footer** — All but EM-05 link to Settings > Notifications in the app
*   **Settings > Notifications** — A switch each for EM-01 to EM-04 and EM-06, on by default, none for EM-05

### Why an email did not arrive
* * *

Start with role and switches, because those rule out most cases. EM-01 and EM-06 timing follows the profile time zone.

| Email | Not sent when |
| ---| --- |
| Any except EM-05 | Its switch is off in Settings > Notifications |
| EM-01 | Nothing unread from the last 24 hours in followed pages, or a guest recipient |
| EM-02, EM-03, EM-04 | A guest recipient and a page not shared with them |
| EM-03 | The reply mentions the recipient, so EM-02 goes instead |
| EM-06 | Not an Owner or Admin, or no workspace activity that week |

Items opened since the last digest drop out of the next EM-01, so it can run short.

### Before changing a template
* * *

*   [ ] **Render all six locales** in the preview tool, checking ja-JP and de-DE overflow
*   [ ] **Send a test to the team inbox** and log the date on the inventory page
*   [ ] **Bump the version suffix** when a variable is added or removed, so a job on the old variables fails loudly

## Scheduled emails
* * *

### EM-01: Daily digest
* * *

*   **Sent when** — Unread activity from the last 24 hours in followed pages
*   **Timing** — Daily 08:00, local time
*   **Recipients** — Owners, Admins and Members with unread activity, not guests
*   **Can be turned off** — Yes
*   **Template** — `tpl_digest_v4`
*   **Variables** — `recipient_name`, `workspace_name` and `items`, capped at 20 and grouped by page
*   **Built by** — The `digest-sender` job, handing each batch of lists to the email delivery provider
*   **Last test send** — 2026-09-03

It groups unread mentions, comment replies, shared pages and assigned to-dos by page, newest first. EM-02 and EM-03 keep their own switches.

The inventory's 07:00 UTC for this schedule and the `digest-sender` hand-off is stale.

### EM-06: Weekly summary
* * *

*   **Sent when** — Workspace activity in the last 7 days
*   **Timing** — Monday 09:00, local time
*   **Recipients** — Every Owner and Admin, never Members or guests
*   **Can be turned off** — Yes
*   **Template** — `tpl_weekly_summary_v1`
*   **Variables** — Four counts, pages created, pages edited, to-dos completed and new members, plus the five most edited pages
*   **Built by** — The `summary-sender` job, which runs hourly on Mondays and picks the Owners and Admins whose local time is Monday 09:00 in that hour
*   **Last test send** — 2026-08-31

## Event emails
* * *

### EM-02: Mentioned in a page
* * *

*   **Sent when** — The recipient is mentioned in a page or comment
*   **Timing** — When it happens
*   **Recipients** — The mentioned member, or a guest only on pages shared with them
*   **Can be turned off** — Yes
*   **Template** — `tpl_mention_v2`
*   **Variables** — `actor_name`, `page_title` and a 140-character `excerpt` around it
*   **Built by** — The mention event
*   **Last test send** — 2026-08-27

### EM-03: Comment reply
* * *

*   **Sent when** — A reply in a thread the recipient started or replied in
*   **Timing** — When it happens
*   **Recipients** — Everyone in the thread, guests only on pages shared with them
*   **Can be turned off** — Yes
*   **Template** — `tpl_comment_reply_v2`
*   **Variables** — `actor_name`, `page_title` and `reply_excerpt`
*   **Built by** — The reply event
*   **Last test send** — 2026-08-27

### EM-04: Page shared with you
* * *

*   **Sent when** — A member shares a page with the recipient
*   **Timing** — When it happens
*   **Recipients** — The member or guest shared with
*   **Can be turned off** — Yes
*   **Template** — `tpl_page_shared_v3`
*   **Variables** — `actor_name`, `page_title` and `access`, view or edit
*   **Built by** — The share event in share-service
*   **Last test send** — 2026-09-09

### EM-05: Workspace invite
* * *

*   **Sent when** — The recipient is invited to a workspace
*   **Timing** — When it happens
*   **Recipients** — The person invited
*   **Can be turned off** — No switch exists
*   **Template** — `tpl_workspace_invite_v5`
*   **Variables** — `actor_name`, `workspace_name` and an invite token valid for 14 days
*   **Last test send** — 2026-09-09

The only template without a footer, since it cannot be turned off.

### Catalog boundaries
* * *

*   **Other emails** — Sign-in codes, receipts and plan emails, owned by Accounts and Billing in other services
*   **Push notifications** — Not covered
*   **Reminders** — No email, reminders show in the app or as local phone notifications
*   **Digest time** — Not recipient-chosen, an occasional feedback request, not planned
*   **Digest scheduling** — Unknown how `digest-sender` times the 08:00 local send, since the inventory's step is stale
*   **Invite event** — Unnamed in the sources
*   **Support console** — Unknown whether it shows a member's notification switches

### Sources
* * *

*   **Email notifications spec** — Lena, Product Manager, Sharing and Notifications, edited 2026-07-14, governs behavior, timing and recipients, including the 08:00 local digest
*   **Email template inventory, notifications-service** — Mateo, Backend Engineer, Notifications, edited 2026-09-11, source for templates, variables, jobs, locales, test sends and checks
*   **Loomlist product context** — Elif, Product Operations, updated 2026-09-22, background only
