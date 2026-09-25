# View-only share links, design notes

Notes by Kofi, Product Designer, Sharing, written up after the design review on 2026-09-15.
Frames are in the Sharing design file: `Share / View-only link`, `Share / Link settings` and `Shared page / Viewer`. Lena and Caio were in the review.

## What we are adding

Today a page can only be shared by inviting a member or a guest. This adds a link anyone can open without signing in, read-only.

## Share panel

A new row sits at the bottom of the Share panel with the switch `Anyone with the link can view`. It is off by default. Turning it on creates the link and shows Copy link next to the switch.

Under the switch, the Link expires menu lists Never, 7 days and 30 days. Never is the default. An expired link counts as off.

Turning the switch off stops the link working within 60 seconds. Reset link does the same for the old link and creates a new one. Someone who already has the page open gets `This link no longer works` on their next action.

Members with edit access to the page, Admins and the Owner can turn the switch on. Guests never see it.

## Plans

| Plan | View-only links |
|------|-----------------|
| Free | Up to 3 active links per workspace, with Never as the only expiry |
| Plus | No limit, every expiry option |
| Team | No limit and every expiry option. Admins can turn view-only links off for the whole workspace |

An active link is one that is switched on and not expired. On Free at the limit, the switch stays visible and turning it on opens `Your workspace has 3 active links. Turn one off or upgrade to Plus to add more.`

When a Team Admin turns view-only links off, every link in the workspace stops within the same 60 seconds and the switch shows as off with the note `Turned off by your workspace admin`.

## What a viewer sees

- The page read-only, with any inline database as a read-only table
- The page title, the workspace name and a Try Loomlist button in a slim top bar
- No comments, no page history, no workspace sidebar
- Duplicate in the top bar for viewers who are signed in, which copies the page into a workspace of theirs
- A sign-in prompt instead, when a viewer who is not signed in taps Duplicate

Every page opened through a view-only link is served with `noindex`, so search engines leave it out.

On iOS and Android the link opens the app when it is installed, and the web page otherwise.

## Open question

`Do sub-pages inherit the link?`

Status: not decided

Design's view, mine: yes. A link on a page also opens its sub-pages, with a switch on each sub-page to leave it out. In the research sessions, readers who followed a link inside a shared page and hit a sign-in wall stopped reading.

Engineering's view, from Caio, Backend Engineer, Sharing: no. Each page gets its own link. Otherwise a sub-page someone adds next month becomes public without anyone choosing that.

Lena, Product Manager, Sharing and Notifications, settles it after she has talked it through with the security reviewer. No date is set. Until then the frames show the link on a single page only, and nothing in the viewer frames depends on the answer except what Duplicate copies.
