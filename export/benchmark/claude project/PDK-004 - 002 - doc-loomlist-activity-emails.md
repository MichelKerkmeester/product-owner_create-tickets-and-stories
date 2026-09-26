# Loomlist activity emails

* * *
> Status: Current behavior — the six activity emails notifications-service sends, digest at 08:00 local time
* * *

## Overview
* * *
This catalog lists the six workspace activity emails Loomlist sends, EM-01 to EM-06, for Support agents answering "why did I get this email" or "why didn't I" and Notifications engineers checking a template before changing it.

Out of scope: sign-in codes, receipts and plan emails, owned by the Accounts and Billing teams, and push notifications.
* * *

### Shared vocabulary
* * *
*   **Settings > Notifications** — Switches for EM-01 to EM-04 and EM-06, on by default, none for EM-05
*   **Guest** — An unbilled person with view or edit access to shared pages only
*   **Email delivery provider** — The outside service that sends every email for notifications-service
*   **Version suffix** — The `_v{n}` ending a template name, such as `_v4` in `tpl_digest_v4`, raised when a variable is added or removed
* * *

### Index
* * *

| ID | Email | Sent when | Timing | Can be turned off | Template |
| ---| ---| ---| ---| ---| --- |
| EM-01 | [Daily digest](#em-01-daily-digest) | Unread activity from the last 24 hours in followed pages | Daily 08:00 local time, unless nothing is unread | Yes | `tpl_digest_v4` |
| EM-02 | [Mentioned in a page](#em-02-mentioned-in-a-page) | A mention in a page or comment | When it happens | Yes | `tpl_mention_v2` |
| EM-03 | [Comment reply](#em-03-comment-reply) | A reply in a thread the recipient started or replied in | When it happens | Yes | `tpl_comment_reply_v2` |
| EM-04 | [Page shared with you](#em-04-page-shared-with-you) | A member shares a page with them | When it happens | Yes | `tpl_page_shared_v3` |
| EM-05 | [Workspace invite](#em-05-workspace-invite) | An invite to a workspace | When it happens | No | `tpl_workspace_invite_v5` |
| EM-06 | [Weekly summary](#em-06-weekly-summary) | Workspace activity in the last 7 days, Owners and Admins only | Monday 09:00 local time | Yes | `tpl_weekly_summary_v1` |
* * *

### Rules that apply to all six
* * *
*   **Language** — The recipient's app language (en-US, de-DE, fr-FR, es-ES, ja-JP or pt-BR), falling back to en-US per missing string
*   **Time zone** — Scheduled emails use the profile time zone, called local time here
*   **Mention inside a reply** — Sends EM-02 only, never EM-03 too
*   **Guests** — Get EM-02, EM-03 and EM-04 for pages shared with them, never EM-01 or EM-06
*   **Footer** — A closing line that opens Settings > Notifications, on every email except EM-05
*   **Sender** — The email delivery provider, as Loomlist
* * *

## Activity emails
* * *

### EM-01 Daily digest
* * *
Grouped by page, newest page first.

*   **Sent when** — Unread activity from the last 24 hours in followed pages
*   **Who gets it** — Owners, Admins and Members, never guests
*   **Timing** — Daily at 08:00 local time, unless nothing is unread
*   **Can be turned off** — Yes
*   **Template** — `tpl_digest_v4`
*   **Variables** — `recipient_name`, `workspace_name` and `items`, capped at 20
*   **Sent by** — The `digest-sender` job, which builds each recipient's list and hands the batch to the email delivery provider
*   **Last test send** — 2026-09-03

It lists mentions, replies, shared pages and assigned to-dos not opened since the last digest.

Digest off, a member gets [EM-02](#em-02-mentioned-in-a-page) and [EM-03](#em-03-comment-reply) unless those are off too.
* * *

### EM-02 Mentioned in a page
* * *
*   **Sent when** — A mention in a page or a comment
*   **Who gets it** — The person mentioned, guests included
*   **Timing** — When it happens
*   **Can be turned off** — Yes
*   **Template** — `tpl_mention_v2`
*   **Variables** — `actor_name`, `page_title` and a 140-character `excerpt` around the mention
*   **Sent by** — The mention event
*   **Last test send** — 2026-08-27
* * *

### EM-03 Comment reply
* * *
*   **Sent when** — A reply in a thread the recipient started or replied in
*   **Who gets it** — Thread starters and repliers, guests included
*   **Timing** — When it happens
*   **Can be turned off** — Yes
*   **Template** — `tpl_comment_reply_v2`
*   **Variables** — `actor_name`, `page_title` and `reply_excerpt`
*   **Sent by** — The reply event
*   **Last test send** — 2026-08-27
* * *

### EM-04 Page shared with you
* * *
*   **Sent when** — A member shares a page with the recipient
*   **Who gets it** — The member or guest it is shared with
*   **Timing** — When it happens
*   **Can be turned off** — Yes
*   **Template** — `tpl_page_shared_v3`
*   **Variables** — `actor_name`, `page_title` and `access`, view or edit
*   **Sent by** — The share event in share-service
*   **Last test send** — 2026-09-09
* * *

### EM-05 Workspace invite
* * *
The only activity email with no switch and no footer.

*   **Sent when** — An invite to a workspace
*   **Who gets it** — The invited person
*   **Timing** — When it happens
*   **Can be turned off** — No
*   **Template** — `tpl_workspace_invite_v5`
*   **Variables** — `actor_name`, `workspace_name` and an invite token expiring after 14 days
*   **Last test send** — 2026-09-09
* * *

### EM-06 Weekly summary
* * *
*   **Sent when** — Workspace activity in the last 7 days
*   **Who gets it** — Every Owner and Admin, never Members or guests
*   **Timing** — Monday 09:00 local time
*   **Can be turned off** — Yes
*   **Template** — `tpl_weekly_summary_v1`
*   **Variables** — The four workspace counts and the five most edited pages
*   **Sent by** — The `summary-sender` job, hourly on Mondays for Owners and Admins at local 09:00
*   **Last test send** — 2026-08-31

It counts pages created, pages edited, to-dos completed and new members, and a week with no activity sends none.
* * *

## Reference notes
* * *

### Checks before changing a template
* * *
The version bump matters most, so a job built for old variables fails loudly rather than sending a broken email.

*   [] **Render all six locales in the preview tool:** Check ja-JP and de-DE for overflow
*   [] **Send a test to the team inbox:** Note the date in the template inventory
*   [] **Bump the version suffix when a variable is added or removed**
* * *

### Catalog boundaries
* * *
*   **Digest time in the template inventory** — Its daily 07:00 UTC for EM-01 is out of date, and 08:00 local holds
*   **Digest time choice** — Recipients cannot pick it, an occasional request that is not planned
*   **Reminders** — No email, as reminders show in the app or as local phone notifications
* * *

### Sources
* * *
*   Email notifications spec, Lena, Product Manager, Sharing and Notifications, last edited 2026-07-14: triggers, timing, recipients and shared rules
*   Email template inventory, notifications-service, Mateo, Backend Engineer, Notifications, last edited 2026-09-11: templates, variables, jobs, test sends, locales and checks
*   Loomlist product context, Elif, Product Operations, last updated 2026-09-22: roles and guests
