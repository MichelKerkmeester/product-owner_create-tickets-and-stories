# Email template inventory, notifications-service

Kept by Mateo, Backend Engineer, Notifications, in the notifications-service repository docs.
Last edited 2026-09-11.

The activity emails notifications-service sends, the template each one renders and when each one goes out. Every email leaves through the email delivery provider with the sender name Loomlist. Sign-in, receipt and plan emails come from other services and are not listed.

## Templates

| ID | Email | Template | Schedule | Locales |
|----|-------|----------|----------|---------|
| EM-01 | Daily digest | tpl_digest_v4 | Daily at 07:00 UTC, skipped when the recipient has nothing unread | All six |
| EM-02 | Mentioned in a page | tpl_mention_v2 | When it happens | All six |
| EM-03 | Comment reply | tpl_comment_reply_v2 | When it happens | All six |
| EM-04 | Page shared with you | tpl_page_shared_v3 | When it happens | All six |
| EM-05 | Workspace invite | tpl_workspace_invite_v5 | When it happens | All six |
| EM-06 | Weekly summary | tpl_weekly_summary_v1 | Monday 09:00 in the recipient's local time | All six |

The six locales are en-US, de-DE, fr-FR, es-ES, ja-JP and pt-BR. A missing string falls back to en-US.

## Per template

**tpl_digest_v4.** Takes `recipient_name`, `workspace_name` and `items`, capped at 20 items grouped by page. The `digest-sender` job builds the list for each Owner, Admin and Member with unread activity and hands the batch to the email delivery provider at 07:00 UTC. Last test send 2026-09-03.

**tpl_mention_v2.** Takes `actor_name`, `page_title` and a 140-character `excerpt` around the mention. Sent from the mention event. Last test send 2026-08-27.

**tpl_comment_reply_v2.** Takes `actor_name`, `page_title` and `reply_excerpt`. Sent from the reply event. Last test send 2026-08-27.

**tpl_page_shared_v3.** Takes `actor_name`, `page_title` and `access`, which reads view or edit. Sent from the share event in share-service. Last test send 2026-09-09.

**tpl_workspace_invite_v5.** Takes `actor_name`, `workspace_name` and an invite token that expires after 14 days. It is the only template with no footer, since it cannot be turned off. Last test send 2026-09-09.

**tpl_weekly_summary_v1.** Takes the four workspace counts and the five most edited pages. The `summary-sender` job runs every hour on Mondays and picks the Owners and Admins whose local time is Monday 09:00 in that hour. Last test send 2026-08-31.

## Footer

Every template except tpl_workspace_invite_v5 ends with a footer line that opens Settings > Notifications in the app.

## Checks before changing a template

- Render all six locales in the preview tool and read the ja-JP and de-DE versions for overflow
- Send a test to the team inbox and note the date in this page
- Bump the version suffix when a variable is added or removed, so a job built for the old variables fails loudly
