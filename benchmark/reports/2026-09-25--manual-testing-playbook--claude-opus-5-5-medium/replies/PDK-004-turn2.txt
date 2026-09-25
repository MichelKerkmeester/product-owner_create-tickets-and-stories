```markdown
# Loomlist activity emails

* * *
> Status: Current behavior — the six activity emails notifications-service sends, with the daily digest at 08:00 in the recipient's local time
* * *

## Overview
* * *
This catalog lists the six emails Loomlist sends about activity in a workspace, EM-01 to EM-06. For each one it gives the trigger, who gets it, the timing, the Settings > Notifications switch and the template that renders it. Support agents can use it to answer "why did I get this email" or "why didn't I", and Notifications engineers can use it to check a template before they change it.

Sign-in codes, receipts and plan emails are out of scope because the Accounts and Billing teams own them and other services send them. Push notifications are out of scope too.
* * *

### Shared vocabulary
* * *
*   **Recipient's local time** — The time zone on the recipient's profile. Every scheduled email uses it
*   **Settings > Notifications** — The screen where a person turns emails on or off. It has one switch each for EM-01 to EM-04 and EM-06, and all five are on by default. EM-05 has no switch
*   **Footer** — A line at the end of the email that opens Settings > Notifications in the app. Every email except EM-05 has one
*   **Guest** — A person who can open only the pages shared with them, with view or edit access. Guests are not billed
*   **Email delivery provider** — The outside service notifications-service hands every email to. The sender name is always Loomlist
*   **Version suffix** — The `_v{n}` at the end of a template name, such as `_v4` in `tpl_digest_v4`. It goes up whenever a template variable is added or removed
* * *

### Index
* * *

| ID | Email | Sent when | Timing | Can be turned off | Template |
| ---| ---| ---| ---| ---| --- |
| EM-01 | [Daily digest](#em-01-daily-digest) | The recipient has unread activity from the last 24 hours in pages they follow | Every day at 08:00 in the recipient's local time. Not sent when there is nothing unread | Yes | `tpl_digest_v4` |
| EM-02 | [Mentioned in a page](#em-02-mentioned-in-a-page) | Someone mentions the recipient in a page or a comment | When it happens | Yes | `tpl_mention_v2` |
| EM-03 | [Comment reply](#em-03-comment-reply) | Someone replies in a comment thread the recipient started or replied in | When it happens | Yes | `tpl_comment_reply_v2` |
| EM-04 | [Page shared with you](#em-04-page-shared-with-you) | A member shares a page with the recipient | When it happens | Yes | `tpl_page_shared_v3` |
| EM-05 | [Workspace invite](#em-05-workspace-invite) | Someone invites the recipient to a workspace | When it happens | No | `tpl_workspace_invite_v5` |
| EM-06 | [Weekly summary](#em-06-weekly-summary) | Activity across the workspace over the last 7 days, for Owners and Admins only | Monday 09:00 in the recipient's local time | Yes | `tpl_weekly_summary_v1` |
* * *

### Rules that apply to all six
* * *
These rules hold for every entry below. Check them before you look for anything specific to one email.

*   **Language** — An email goes out in the recipient's app language: en-US, de-DE, fr-FR, es-ES, ja-JP or pt-BR. A missing string falls back to en-US
*   **Time zone** — Scheduled emails use the time zone on the recipient's profile
*   **Mention inside a reply** — A mention inside a comment reply sends EM-02 only, never EM-02 and EM-03 together
*   **Guests** — Guests get EM-02, EM-03 and EM-04 for the pages shared with them. They never get EM-01 or EM-06
*   **Footer** — Every email except EM-05 ends with a line that opens Settings > Notifications
*   **Sender** — Every email goes out through the email delivery provider with the sender name Loomlist
* * *

## Activity emails
* * *

### EM-01 Daily digest
* * *
The daily digest collects unread activity from the last 24 hours in one email, grouped by page with the newest page first.

*   **Sent when** — The recipient has unread activity from the last 24 hours in pages they follow
*   **Who gets it** — Owners, Admins and Members with unread activity. Never guests
*   **Timing** — Every day at 08:00 in the recipient's local time. Not sent when there is nothing unread
*   **Can be turned off** — Yes, from its switch in Settings > Notifications
*   **Template** — `tpl_digest_v4`
*   **Variables** — `recipient_name`, `workspace_name` and `items`, capped at 20 items grouped by page
*   **Sent by** — The `digest-sender` job, which builds the list for each recipient and hands the batch to the email delivery provider
*   **Last test send** — 2026-09-03

The digest lists mentions, comment replies, pages shared with the recipient and to-dos assigned to them. An item the recipient has opened in the app since the last digest drops out.

A member who turns the digest off still gets [EM-02](#em-02-mentioned-in-a-page) and [EM-03](#em-03-comment-reply) for each event, unless those are off too.
* * *

### EM-02 Mentioned in a page
* * *
EM-02 tells the recipient that someone typed @ and their name in a page or a comment.

*   **Sent when** — Someone mentions the recipient in a page or a comment
*   **Who gets it** — The person mentioned, including a guest on a page shared with them
*   **Timing** — When it happens
*   **Can be turned off** — Yes, from its switch in Settings > Notifications
*   **Template** — `tpl_mention_v2`
*   **Variables** — `actor_name`, `page_title` and a 140-character `excerpt` around the mention
*   **Sent by** — The mention event
*   **Last test send** — 2026-08-27

A mention inside a comment reply sends EM-02 only, so the recipient does not also get [EM-03](#em-03-comment-reply) for that reply.
* * *

### EM-03 Comment reply
* * *
EM-03 tells the recipient that someone replied in a comment thread they are part of.

*   **Sent when** — Someone replies in a comment thread the recipient started or replied in
*   **Who gets it** — Everyone who started or replied in the thread, including a guest on a page shared with them
*   **Timing** — When it happens
*   **Can be turned off** — Yes, from its switch in Settings > Notifications
*   **Template** — `tpl_comment_reply_v2`
*   **Variables** — `actor_name`, `page_title` and `reply_excerpt`
*   **Sent by** — The reply event
*   **Last test send** — 2026-08-27

When the reply mentions the recipient, they get [EM-02](#em-02-mentioned-in-a-page) instead of EM-03.
* * *

### EM-04 Page shared with you
* * *
EM-04 tells the recipient that a member gave them access to a page.

*   **Sent when** — A member shares a page with the recipient
*   **Who gets it** — The person the page is shared with, member or guest
*   **Timing** — When it happens
*   **Can be turned off** — Yes, from its switch in Settings > Notifications
*   **Template** — `tpl_page_shared_v3`
*   **Variables** — `actor_name`, `page_title` and `access`, which reads view or edit
*   **Sent by** — The share event in share-service
*   **Last test send** — 2026-09-09
* * *

### EM-05 Workspace invite
* * *
EM-05 is the only activity email a person cannot turn off, so it has no switch in Settings > Notifications and no footer.

*   **Sent when** — Someone invites the recipient to a workspace
*   **Who gets it** — The invited person
*   **Timing** — When it happens
*   **Can be turned off** — No
*   **Template** — `tpl_workspace_invite_v5`
*   **Variables** — `actor_name`, `workspace_name` and an invite token that expires after 14 days
*   **Last test send** — 2026-09-09
* * *

### EM-06 Weekly summary
* * *
The weekly summary gives Owners and Admins a count of the last 7 days of workspace activity.

*   **Sent when** — The workspace had activity in the last 7 days
*   **Who gets it** — Every Owner and Admin of the workspace. Never Members or guests
*   **Timing** — Monday 09:00 in the recipient's local time
*   **Can be turned off** — Yes, from its switch in Settings > Notifications
*   **Template** — `tpl_weekly_summary_v1`
*   **Variables** — The four workspace counts and the five most edited pages
*   **Sent by** — The `summary-sender` job, which runs every hour on Mondays and picks the Owners and Admins whose local time is Monday 09:00 in that hour
*   **Last test send** — 2026-08-31

The summary counts pages created, pages edited, to-dos completed and new members, then lists the five most edited pages. A workspace with no activity that week gets no summary.
* * *

## Reference notes
* * *

### Checks before changing a template
* * *
Run these three checks on any template change. The version bump matters most, because a job built for the old variables then fails loudly instead of sending a broken email.

*   [ ] **Render all six locales in the preview tool.** Read the ja-JP and de-DE versions for overflow
*   [ ] **Send a test to the team inbox.** Note the date in the notifications-service template inventory
*   [ ] **Bump the version suffix when a variable is added or removed**
* * *

### Catalog boundaries
* * *
*   **Digest time in the template inventory** — The inventory lists the EM-01 schedule as daily at 07:00 UTC. That line is out of date. The digest goes at 08:00 in the recipient's local time
*   **Digest time choice** — Recipients cannot pick their own digest time. It comes up in feedback now and then and is not planned
*   **Reminders** — Loomlist sends no reminder email. Reminders show in the app or as local notifications on the phone
*   **Other emails** — Sign-in codes, receipts and plan emails come from other services and teams
*   **Push notifications** — Not covered here
* * *

### Sources
* * *
*   Email notifications spec, Lena, Product Manager, Sharing and Notifications, last edited 2026-07-14 — triggers, timing, recipients, rules for all six and the digest send time
*   Email template inventory, notifications-service, Mateo, Backend Engineer, Notifications, last edited 2026-09-11 — template names, variables, jobs, test sends, locales and change checks. Its 07:00 UTC digest schedule is out of date
*   Loomlist product context, Elif, Product Operations, last updated 2026-09-22 — background definitions for roles and guests
```

Export-equivalent path: `export/002 - doc-loomlist-activity-emails.md`

HVR self-scan: 0 hard blockers. Fixed: took the em dash out of the entry headings (`EM-01 Daily digest` instead of `EM-01 — Daily digest`). Kept with reason: em dashes in `*   **Term** — definition` bullets and in the `Status: Current behavior — …` label, which the ClickUp format and status label allow.

Quality:
- **Source safety: pass.** I used only your three files. The 08:00 local digest time follows your ruling, and the page marks the inventory's 07:00 UTC as out of date.
- **Shape fit: pass.** It's a catalog: an index linked to one entry per email, with the Support details first and the template details below them in each entry.
- **Layout: pass.** It uses ClickUp dividers and bullets with sentence-case headings. I left out spacer headings because this is a file export. I'll add them if you want it pushed to ClickUp.
- **Readability: pass.** Each entry opens with a one-line summary, and lists stay one level deep.
- **Voice: pass.**

Some things in the page aren't stated word for word in your sources, so please check them:

- **Out-of-date note:** the line about the inventory's 07:00 UTC time comes from your answer, not from either file.
- **"Who gets it" for EM-02 to EM-05:** the spec only names the event that sends each email, so I wrote these lines from the trigger and the guest rule.
- **Guest definition:** this comes from the context page.
- **EM-05 and guests:** your sources don't say whether a guest can get an invite email, so the page doesn't say either.
- **EM-05 sender:** the inventory doesn't say what sends it, so its entry has no "Sent by" line.

Want me to create this as a ClickUp doc?