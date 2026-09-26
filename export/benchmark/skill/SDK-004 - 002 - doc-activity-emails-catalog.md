# Loomlist activity emails

* * *
> Status: Current behavior — the six activity emails notifications-service sends, EM-01 to EM-06
* * *

## Overview
* * *

This catalog lists the six emails Loomlist sends about activity in a workspace. Each entry says when the email goes out, who gets it, whether it can be turned off and which template renders it. Two emails run on a schedule and four go out the moment something happens.

Support agents use it to work out why someone did or did not get an email. Notifications engineers use it to find the template, variables and job behind an email before changing it. Push notifications, reminders and the sign-in, receipt and plan emails are not covered, as listed under Catalog boundaries.

### Index
* * *

| ID | Email | Template | Sent | Can be turned off |
| ---| ---| ---| ---| --- |
| `EM-01` | [Daily digest](#em-01-daily-digest) | `tpl_digest_v4` | Every day at 08:00, recipient's local time | Yes |
| `EM-02` | [Mentioned in a page](#em-02-mentioned-in-a-page) | `tpl_mention_v2` | When it happens | Yes |
| `EM-03` | [Comment reply](#em-03-comment-reply) | `tpl_comment_reply_v2` | When it happens | Yes |
| `EM-04` | [Page shared with you](#em-04-page-shared-with-you) | `tpl_page_shared_v3` | When it happens | Yes |
| `EM-05` | [Workspace invite](#em-05-workspace-invite) | `tpl_workspace_invite_v5` | When it happens | No |
| `EM-06` | [Weekly summary](#em-06-weekly-summary) | `tpl_weekly_summary_v1` | Monday 09:00, recipient's local time | Yes |

### Rules that apply to all six
* * *

*   **Sender** — Every email leaves through the email delivery provider with the sender name Loomlist
*   **Local time** — The recipient's local time comes from the time zone on their profile
*   **Language** — An email uses the recipient's app language, every template covers en-US, de-DE, fr-FR, es-ES, ja-JP and pt-BR, and missing strings fall back to en-US
*   **Mention in a reply** — A mention inside a comment reply sends EM-02 only, never EM-02 and EM-03 together
*   **Guests** — Guests get EM-02, EM-03 and EM-04 for the pages shared with them, and never EM-01 or EM-06
*   **Footer** — Every email except EM-05 ends with a footer line that opens Settings > Notifications in the app
*   **Settings > Notifications** — One switch per email for EM-01 to EM-04 and EM-06, all on by default, while EM-05 has no switch

### Why an email did not arrive
* * *

Start with the recipient's role and their switches, because those two rule out most of the cases below. Timing questions about EM-01 and EM-06 come down to the time zone on the recipient's profile, since both follow it.

| Email | Not sent when |
| ---| --- |
| Any except EM-05 | The recipient turned that email's switch off in Settings > Notifications |
| EM-01 | The recipient has nothing unread from the last 24 hours in pages they follow, or the recipient is a guest |
| EM-02, EM-03, EM-04 | The recipient is a guest and the page is not shared with them |
| EM-03 | The reply also mentions the recipient, so EM-02 goes out instead |
| EM-06 | The recipient is not an Owner or Admin, or the workspace had no activity that week |

An item the recipient has opened in the app since the last digest drops out of the next EM-01, so a digest can be shorter than the recipient expects.

### Before changing a template
* * *

*   [ ] **Render all six locales** in the preview tool and read the ja-JP and de-DE versions for overflow
*   [ ] **Send a test to the team inbox** and note the date on the template inventory page
*   [ ] **Bump the version suffix** when a variable is added or removed, so a job built for the old variables fails loudly

## Scheduled emails
* * *

### EM-01: Daily digest
* * *

*   **Sent when** — The recipient has unread activity from the last 24 hours in pages they follow
*   **Timing** — Every day at 08:00 in the recipient's local time
*   **Recipients** — Owners, Admins and Members with unread activity, never guests
*   **Can be turned off** — Yes
*   **Template** — `tpl_digest_v4`
*   **Variables** — `recipient_name`, `workspace_name` and `items`, capped at 20 items grouped by page
*   **Built by** — The `digest-sender` job, which builds the list for each recipient and hands the batch to the email delivery provider
*   **Last test send** — 2026-09-03

The digest groups unread activity by page, newest page first. It lists mentions, comment replies, pages shared with the recipient and to-dos assigned to them. An item the recipient has opened in the app since the last digest drops out.

Turning the digest off does not stop EM-02 and EM-03, which still go out for each event unless their own switches are off too.

The template inventory still gives 07:00 UTC for this email's schedule and for the `digest-sender` hand-off. That value is stale. The send time is 08:00 in the recipient's local time.

### EM-06: Weekly summary
* * *

*   **Sent when** — There was activity across the workspace over the last 7 days
*   **Timing** — Monday 09:00 in the recipient's local time
*   **Recipients** — Every Owner and Admin, never Members or guests
*   **Can be turned off** — Yes
*   **Template** — `tpl_weekly_summary_v1`
*   **Variables** — The four workspace counts and the five most edited pages
*   **Built by** — The `summary-sender` job, which runs hourly on Mondays and picks the Owners and Admins whose local time is Monday 09:00 in that hour
*   **Last test send** — 2026-08-31

The four counts are pages created, pages edited, to-dos completed and new members.

## Event emails
* * *

### EM-02: Mentioned in a page
* * *

*   **Sent when** — Someone mentions the recipient in a page or a comment
*   **Timing** — When it happens
*   **Recipients** — The member mentioned, but a guest only for pages shared with them
*   **Can be turned off** — Yes
*   **Template** — `tpl_mention_v2`
*   **Variables** — `actor_name`, `page_title` and a 140-character `excerpt` around the mention
*   **Built by** — The mention event
*   **Last test send** — 2026-08-27

A mention inside a comment reply sends this email and not EM-03.

### EM-03: Comment reply
* * *

*   **Sent when** — Someone replies in a comment thread the recipient started or replied in
*   **Timing** — When it happens
*   **Recipients** — Everyone who started or replied in the thread, but a guest only for pages shared with them
*   **Can be turned off** — Yes
*   **Template** — `tpl_comment_reply_v2`
*   **Variables** — `actor_name`, `page_title` and `reply_excerpt`
*   **Built by** — The reply event
*   **Last test send** — 2026-08-27

When the reply mentions the recipient, they get EM-02 instead of this email.

### EM-04: Page shared with you
* * *

*   **Sent when** — A member shares a page with the recipient
*   **Timing** — When it happens
*   **Recipients** — The member or guest the page is shared with
*   **Can be turned off** — Yes
*   **Template** — `tpl_page_shared_v3`
*   **Variables** — `actor_name`, `page_title` and `access`, which reads view or edit
*   **Built by** — The share event in share-service
*   **Last test send** — 2026-09-09

### EM-05: Workspace invite
* * *

*   **Sent when** — Someone invites the recipient to a workspace
*   **Timing** — When it happens
*   **Recipients** — The person invited
*   **Can be turned off** — No, as Settings > Notifications has no switch for it
*   **Template** — `tpl_workspace_invite_v5`
*   **Variables** — `actor_name`, `workspace_name` and an invite token that expires after 14 days
*   **Last test send** — 2026-09-09

This is the only template with no footer, since the email cannot be turned off.

### Catalog boundaries
* * *

*   **Other emails** — Sign-in codes, receipts and plan emails sit with the Accounts and Billing teams and come from other services
*   **Push notifications** — Not covered by this catalog
*   **Reminders** — There is no reminder email: reminders show in the app or as local notifications on the phone
*   **Digest time** — Recipients cannot choose when the digest arrives, a request that comes up in feedback now and then and is not planned
*   **Digest scheduling** — The sources do not describe how `digest-sender` times the 08:00 local send, because the inventory's description of that step is stale
*   **Invite event** — The sources do not name the event that sends EM-05
*   **Support console** — The sources do not say whether the Support console shows a member's notification switches

### Sources
* * *

*   **Email notifications spec** — Lena, Product Manager, Sharing and Notifications, edited 2026-07-14, governing each email's behavior, timing and recipients, including the 08:00 local digest time
*   **Email template inventory, notifications-service** — Mateo, Backend Engineer, Notifications, edited 2026-09-11, the source for template names, variables, jobs, locales, test-send dates and pre-change checks
*   **Loomlist product context** — Elif, Product Operations, updated 2026-09-22, background only

The inventory's 07:00 UTC digest schedule is stale.
