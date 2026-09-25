# Email notifications spec

Written by Lena, Product Manager, Sharing and Notifications, in the Notifications team space.
Last edited 2026-07-14.

This page covers the six emails Loomlist sends about activity in a workspace. Sign-in codes, receipts and plan emails sit with the Accounts and Billing teams and are not listed here. Push notifications for mentions, replies and shares are a separate page.

## The six emails

| ID | Email | Sent when | Timing | Can be turned off |
|----|-------|-----------|--------|-------------------|
| EM-01 | Daily digest | The recipient has unread activity from the last 24 hours in pages they follow | Every day at 08:00 in the recipient's local time. Not sent when there is nothing unread | Yes |
| EM-02 | Mentioned in a page | Someone mentions the recipient in a page or a comment | When it happens | Yes |
| EM-03 | Comment reply | Someone replies in a comment thread the recipient started or replied in | When it happens | Yes |
| EM-04 | Page shared with you | A member shares a page with the recipient | When it happens | Yes |
| EM-05 | Workspace invite | Someone invites the recipient to a workspace | When it happens | No |
| EM-06 | Weekly summary | Activity across the workspace over the last 7 days, for Owners and Admins only | Monday 09:00 in the recipient's local time | Yes |

## Rules that apply to all six

- The recipient's local time comes from the time zone on their profile
- An email goes out in the recipient's app language, with en-US when a string is missing
- A mention inside a comment reply sends EM-02 only, never EM-02 and EM-03 together
- Guests get EM-02, EM-03 and EM-04 for the pages shared with them, and never EM-01 or EM-06
- Every email except EM-05 carries a footer line that opens Settings > Notifications
- Settings > Notifications shows one switch per email for EM-01 to EM-04 and EM-06, all on by default

## Daily digest

The digest groups unread activity by page, newest page first. It lists mentions, comment replies, pages shared with the recipient and to-dos assigned to them. An item the recipient has opened in the app since the last digest drops out.

A member who turns the digest off in Settings > Notifications still gets EM-02 and EM-03 for each event, unless those are off too.

## Weekly summary

The weekly summary counts pages created, pages edited, to-dos completed and new members for the workspace, with the five most edited pages. It goes to every Owner and Admin at Monday 09:00 in the recipient's local time. A workspace with no activity that week gets no summary.

## Not in this spec

- Push notifications
- Email for reminders, which show in the app or as local notifications on the phone
- A choice of digest time, which comes up in feedback now and then and is not planned
