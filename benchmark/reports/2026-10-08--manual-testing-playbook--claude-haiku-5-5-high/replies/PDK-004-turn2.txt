```markdown
# Activity emails catalog

* * *
> Status: Current behavior — as recorded in the email spec (last edited 2026-07-14) and the template inventory (last edited 2026-09-11). Send times follow the spec.
* * *

## Overview
* * *

This catalog lists the six activity emails Loomlist sends about workspace activity. Support agents use it to explain what a member received and when. Notifications engineers use it to check each template and its variables.

Send times and recipient rules follow the email spec. Template IDs, variables and locales come from the template inventory. Sign-in codes, receipts, plan emails, reminders and push notifications are out of scope.

### Shared vocabulary
* * *

*   **Recipient** — The member or guest an email is sent to
*   **Local time** — The time in the recipient's profile time zone
*   **Template ID** — The identifier an email renders from, with a version suffix that changes when its variables change
*   **Footer** — The line at the end of an email that opens Settings > Notifications

### Index
* * *

| ID | Email | Template | Sent when | Can be turned off |
| --- | --- | --- | --- | --- |
| `EM-01` | [Daily digest](#em-01-daily-digest) | `tpl_digest_v4` | Daily, 08:00 local time | Yes |
| `EM-02` | [Mentioned in a page](#em-02-mentioned-in-a-page) | `tpl_mention_v2` | When someone mentions the recipient | Yes |
| `EM-03` | [Comment reply](#em-03-comment-reply) | `tpl_comment_reply_v2` | When someone replies in a thread the recipient started or replied in | Yes |
| `EM-04` | [Page shared with you](#em-04-page-shared-with-you) | `tpl_page_shared_v3` | When a member shares a page with the recipient | Yes |
| `EM-05` | [Workspace invite](#em-05-workspace-invite) | `tpl_workspace_invite_v5` | When someone invites the recipient to a workspace | No |
| `EM-06` | [Weekly summary](#em-06-weekly-summary) | `tpl_weekly_summary_v1` | Monday, 09:00 local time | Yes |

## The six emails
* * *

### EM-01: Daily digest
* * *

*   **Sent when** — The recipient has unread activity from the last 24 hours in pages they follow
*   **Timing** — Every day at 08:00 in the recipient's local time, skipped when nothing is unread
*   **Recipients** — Owners, Admins and Members, never Guests
*   **Content** — Mentions, comment replies, pages shared with the recipient and to-dos assigned to them, grouped by page with the newest page first
*   **Opened items** — An item the recipient opened in the app since the last digest drops out
*   **Variables** — `recipient_name`, `workspace_name` and `items`, which holds up to 20 entries
*   **Template** — `tpl_digest_v4`
*   **Can be turned off** — Yes, in Settings > Notifications, and EM-02 and EM-03 still arrive for each event unless they are off too
*   **Footer** — Yes, opens Settings > Notifications

### EM-02: Mentioned in a page
* * *

*   **Sent when** — Someone mentions the recipient in a page or a comment
*   **Timing** — When the mention happens
*   **Recipients** — The mentioned member or guest
*   **Variables** — `actor_name`, `page_title` and `excerpt`, a 140-character excerpt around the mention
*   **Template** — `tpl_mention_v2`
*   **Can be turned off** — Yes
*   **Footer** — Yes, opens Settings > Notifications
*   **Mention in a reply** — A mention inside a comment reply sends EM-02 only

### EM-03: Comment reply
* * *

*   **Sent when** — Someone replies in a comment thread the recipient started or replied in
*   **Timing** — When the reply happens
*   **Recipients** — The recipient who started the thread or replied in it, including guests on shared pages
*   **Variables** — `actor_name`, `page_title` and `reply_excerpt`
*   **Template** — `tpl_comment_reply_v2`
*   **Can be turned off** — Yes
*   **Footer** — Yes, opens Settings > Notifications
*   **Mention in a reply** — A reply that mentions the recipient sends EM-02 only

### EM-04: Page shared with you
* * *

*   **Sent when** — A member shares a page with the recipient
*   **Timing** — When the share happens
*   **Recipients** — The member or guest the page is shared with
*   **Variables** — `actor_name`, `page_title` and `access`, which reads `view` or `edit`
*   **Template** — `tpl_page_shared_v3`
*   **Can be turned off** — Yes
*   **Footer** — Yes, opens Settings > Notifications

### EM-05: Workspace invite
* * *

*   **Sent when** — Someone invites the recipient to a workspace
*   **Timing** — When the invite happens
*   **Recipients** — The invited person
*   **Variables** — `actor_name`, `workspace_name` and an invite token that expires after 14 days
*   **Template** — `tpl_workspace_invite_v5`
*   **Can be turned off** — No
*   **Footer** — None, since the email cannot be turned off

### EM-06: Weekly summary
* * *

*   **Sent when** — Activity across the workspace over the last 7 days
*   **Timing** — Monday at 09:00 in the recipient's local time
*   **Recipients** — Owners and Admins only
*   **Variables** — Four workspace counts (pages created, pages edited, to-dos completed and new members) and the five most edited pages
*   **Template** — `tpl_weekly_summary_v1`
*   **Can be turned off** — Yes
*   **Footer** — Yes, opens Settings > Notifications
*   **No activity** — A workspace with no activity that week gets no summary

## Rules that apply to all six
* * *

*   The recipient's local time comes from the time zone on their profile
*   Each email goes out in the recipient's app language, with en-US when a string is missing
*   Every template is available in en-US, de-DE, fr-FR, es-ES, ja-JP and pt-BR
*   Guests get EM-02, EM-03 and EM-04 for pages shared with them, and never EM-01 or EM-06
*   Every email except EM-05 ends with a footer line that opens Settings > Notifications
*   Settings > Notifications has one switch each for EM-01 to EM-04 and EM-06, all on by default

### Boundaries and exceptions
* * *

*   **Retired digest schedule** — The 07:00 UTC schedule in the template inventory no longer applies, so the digest goes at 08:00 local time
*   **Out of scope** — Push notifications, reminders, sign-in codes, receipts and plan emails
*   **Digest time choice** — A choice of digest time is not planned

### Sources
* * *

*   **Email notifications spec** — Lena, last edited 2026-07-14, for send times, recipient rules, footers and switches
*   **Email template inventory** — Mateo, last edited 2026-09-11, for template IDs, variables and locales
*   **Loomlist product context** — Elif, last updated 2026-09-22, background only
```

Export-equivalent path: export/NNN - doc-activity-emails-catalog.md

HVR self-scan: 0 hard blockers. Fixed: em dash in headings, changed to colons. Kept with reason: em dash in the `**Term** — definition` lines and the status notice, both sanctioned for ClickUp Doc output.

Quality status:
- Source safety: attention. Status is current behavior by your designation. I did not check it against the live system or the sending code.
- Shape fit: pass. Catalog with stable IDs, shared fields and an index.
- ClickUp layout: pass. Spacer headings are omitted, so I can add them if this goes straight to a ClickUp paste.
- Readability: pass.
- Voice: pass.

The catalog covers the six emails with send times from the spec and template details from the inventory. The 07:00 UTC schedule appears only as retired material, and push is excluded.

Three things need a check before this is shared:
- The 20-item digest cap comes only from the inventory. The spec does not mention it.
- The inventory's digest schedule row and its job description still show 07:00 UTC, so Mateo should update them.
- The product context page's "Receive email" flow does not name the daily digest, so Elif should review it.

I left out the inventory's job names (`digest-sender`, `summary-sender`) as internal detail. I can add them if the engineers want them.