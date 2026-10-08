# Loomlist activity emails catalog

* * *

> Status: Current behavior — per the email notifications spec (last edited 2026-07-14) and the email template inventory (last edited 2026-09-11). The digest send time follows the spec, as designated for this page. The sources have not been checked against the running service or the job configuration.

* * *

## Overview
* * *

This catalog lists the six emails Loomlist sends about activity in a workspace. It is written for Support agents and Notifications engineers. Each entry gives the template, when the email goes out and who receives it.

Sign-in codes, receipts and plan emails sit with other services. Push notifications are excluded, as are reminders, which show in the app or as local notifications on the phone.

## The six emails
* * *

| ID | Email | Template | Sent when | Can be turned off |
|----|-------|----------|-----------|-------------------|
| EM-01 | Daily digest | tpl_digest_v4 | Every day at 08:00 in the recipient's local time, when there is unread activity | Yes |
| EM-02 | Mentioned in a page | tpl_mention_v2 | Someone mentions the recipient in a page or a comment | Yes |
| EM-03 | Comment reply | tpl_comment_reply_v2 | Someone replies in a comment thread the recipient started or replied in | Yes |
| EM-04 | Page shared with you | tpl_page_shared_v3 | A member shares a page with the recipient | Yes |
| EM-05 | Workspace invite | tpl_workspace_invite_v5 | Someone invites the recipient to a workspace | No |
| EM-06 | Weekly summary | tpl_weekly_summary_v1 | Monday at 09:00 in the recipient's local time, for Owners and Admins | Yes |

### EM-01 daily digest
* * *

The digest goes to each Owner, Admin and Member with unread activity from the last 24 hours in pages they follow. It is not sent when nothing is unread. Guests never receive it.

The digest groups unread activity by page, newest page first. It lists mentions, comment replies, pages shared with the recipient and to-dos assigned to them. Items the recipient has opened in the app since the last digest drop out.

*   Sent from the digest-sender job, which builds the list for each recipient
*   Template variables: recipient_name, workspace_name and items, capped at 20 items grouped by page
*   Send time: 08:00 in the recipient's local time, per the spec. The inventory's 07:00 UTC schedule is retired material, superseded for this page
*   The inventory still describes the digest-sender job at 07:00 UTC, and the three sources do not show the job configuration. Check the job before relying on the send time
*   No source defines "pages they follow", so the meaning of follow is unknown

### EM-02 mentioned in a page
* * *

The mention email goes out when someone mentions the recipient in a page or a comment.

*   Sent from the mention event
*   Template variables: actor_name, page_title and excerpt, a 140-character excerpt around the mention

### EM-03 comment reply
* * *

The reply email goes out when someone replies in a comment thread the recipient started or replied in.

*   Sent from the reply event
*   Template variables: actor_name, page_title and reply_excerpt

### EM-04 page shared with you
* * *

The share email goes out when a member shares a page with the recipient. Guests receive it for the pages shared with them.

*   Sent from the share event in share-service
*   Template variables: actor_name, page_title and access, which reads view or edit

### EM-05 workspace invite
* * *

The invite email goes out when someone invites the recipient to a workspace. It is the only email that cannot be turned off, and it has no footer.

*   Template variables: actor_name, workspace_name and an invite token that expires after 14 days

### EM-06 weekly summary
* * *

The weekly summary goes to each Owner and Admin at Monday 09:00 in the recipient's local time. It covers the last 7 days of workspace activity. A workspace with no activity that week gets no summary.

*   Sent from the summary-sender job, which runs every hour on Mondays and picks the Owners and Admins whose local time is Monday 09:00 in that hour
*   Template variables: four workspace counts for pages created, pages edited, to-dos completed and new members, plus the five most edited pages

## Roles
* * *

Recipient eligibility depends on the workspace role. The roles below are as defined on the context page.

*   **Owner** — Everything an Admin can do, plus billing, plan changes and deleting the workspace. One per workspace
*   **Admin** — Invites and removes members, changes workspace settings and sees every page
*   **Member** — Creates, edits and shares pages they can open
*   **Guest** — Opens only the pages shared with them, with view or edit access as set by the sharer

## Shared rules
* * *

*   The recipient's local time comes from the time zone on their profile. The profile time zone is set from the device at sign-up and can be changed in profile settings
*   Each email goes out in the recipient's app language, with en-US used when a string is missing
*   The six locales are en-US, de-DE, fr-FR, es-ES, ja-JP and pt-BR
*   Every email comes from the sender name Loomlist
*   Every email except EM-05 ends with a footer line that opens Settings > Notifications
*   Guests get EM-02, EM-03 and EM-04 for the pages shared with them, and never EM-01 or EM-06
*   A mention inside a comment reply sends EM-02 only, never EM-02 and EM-03 together

### Settings
* * *

*   Settings > Notifications shows one switch each for EM-01 to EM-04 and EM-06, all on by default
*   EM-05 has no switch because it cannot be turned off
*   A member who turns off the digest still gets EM-02 and EM-03 for each event, unless those are off too
