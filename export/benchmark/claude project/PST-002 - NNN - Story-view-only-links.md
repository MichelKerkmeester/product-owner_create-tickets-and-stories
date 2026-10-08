# Platform - Sharing - View-only links

* * *
## Problem
* * *
Agencies on Plus ask for this more than any other group. Today an agency that wants a client to read one page has to invite that client as a guest, because a page can only be shared by inviting a member or a guest. A guest joins the workspace to see the pages shared with them, so each client joins the workspace for a single page.
* * *
##   

## Solution
* * *
Members with edit access, Admins and the Owner turn on a link that anyone can open without signing in. The page opens read-only behind a slim top bar, and a signed-in viewer can duplicate it into a workspace of their own. A client who needs one page can read it without being invited as a guest.

**Expected outcomes**
* * *
*   Agencies on Plus share one page with a client without inviting the client as a guest
*   Clients read a shared page without signing in
*   Signed-in viewers keep a copy of a shared page in a workspace of their own
* * *
##   

## Requirements
* * *
**Link scope**
* * *
**Open:** `Do sub-pages inherit the link?` Lena settles it with the security reviewer. No date is set.
- [] Until that is settled, a view-only link opens only the page it was created on

**Share panel**
* * *
- [] The switch row sits at the bottom of the Share panel
- [] The switch reads `Anyone with the link can view` and is off by default
- [] Turning the switch on creates the link and shows `Copy link` beside the switch
- [] The `Link expires` menu sits under the switch and lists `Never`, `7 days` and `30 days`
- [] `Never` is the default expiry
- [] An expired link counts as off
- [] Turning the switch off stops the link within `60 seconds`
- [] `Reset link` stops the old link within `60 seconds` and creates a new link
- [] A viewer who has the page open sees `This link no longer works` on their next action
- [] Members with edit access, Admins and the Owner can turn the switch on
- [] Guests do not see the switch

**Plans**
* * *
- [] Free allows up to `3` active links per workspace, with `Never` as the only expiry option
- [] Plus allows no link limit and offers every expiry option
- [] Team allows no link limit and offers every expiry option
- [] Team Admins can turn view-only links off for the whole workspace
- [] An active link is switched on and not expired
- [] On Free at the limit, the switch stays visible, and turning it on shows `Your workspace has 3 active links. Turn one off or upgrade to Plus to add more.`
- [] When a Team Admin turns view-only links off, every link in the workspace stops within `60 seconds`, and the switch shows as off with `Turned off by your workspace admin`

**Viewer**
* * *
- [] The page opens read-only, with any inline database shown as a read-only table
- [] A slim top bar shows the page title, the workspace name and a `Try Loomlist` button
- [] The viewer sees no comments, no page history and no workspace sidebar
- [] Signed-in viewers see `Duplicate` in the top bar, which copies the page into a workspace of theirs
- [] A viewer who is not signed in sees a sign-in prompt when they tap `Duplicate`

**Search indexing**
* * *
- [] Every page opened through a view-only link is served with `noindex`, so search engines leave it out

**Mobile**
* * *
- [] On iOS and Android, a view-only link opens the app when it is installed and the web page otherwise
* * *
##   

## Acceptance criteria
* * *
All acceptance criteria below must be met, or discuss and rescope any that cannot be met.

#### Share panel
* * *
1 ) **Owners can turn on a link and copy it**
* * *
*   **Given** a member with edit access, an Admin or the Owner has a page open
*   **When** they turn on the switch
*   **Then** they can copy the link from the Share panel
* * *
- [] _Mark as done, if the criteria are met_

2 ) **Switching the link off ends access**
* * *
*   **Given** a viewer has a view-only page open
*   **When** the owner turns the switch off or resets the link
*   **Then** the viewer is told the link no longer works
* * *
- [] _Mark as done, if the criteria are met_

#### Plans
* * *
3 ) **Free workspaces at the link limit are told why**
* * *
*   **Given** a Free workspace has its active links at the limit
*   **When** a member turns the switch on
*   **Then** the member is told the workspace is at its link limit and how to add more
*   **And** the switch stays visible
* * *
- [] _Mark as done, if the criteria are met_

4 ) **Team Admins can close view-only links for the workspace**
* * *
*   **Given** a Team Admin
*   **When** they turn view-only links off for the workspace
*   **Then** every link in the workspace stops working
*   **And** the switch shows that an admin turned it off
* * *
- [] _Mark as done, if the criteria are met_

#### Viewer
* * *
5 ) **Viewers read the page without workspace chrome**
* * *
*   **Given** a person who is not signed in opens a view-only link
*   **When** the page loads
*   **Then** the page is read-only
*   **And** it shows no comments, page history or workspace sidebar
* * *
- [] _Mark as done, if the criteria are met_

6 ) **Signed-in viewers can duplicate a page**
* * *
*   **Given** a signed-in viewer has a view-only page open
*   **When** they tap Duplicate
*   **Then** the page is copied into a workspace they belong to
* * *
- [] _Mark as done, if the criteria are met_

7 ) **Signed-out viewers are asked to sign in before duplicating**
* * *
*   **Given** a viewer who is not signed in has a view-only page open
*   **When** they tap Duplicate
*   **Then** they are shown a sign-in prompt
* * *
- [] _Mark as done, if the criteria are met_

#### Mobile
* * *
8 ) **Mobile users open links in the app when it is installed**
* * *
*   **Given** a person has the iOS or Android app installed
*   **When** they open a view-only link
*   **Then** the link opens in the app
* * *
- [] _Mark as done, if the criteria are met_
* * *
##   

## Delivery
* * *
#### Estimation
* * *
*   TBD...

#### External dependencies
* * *
*   **Security reviewer** - sign-off on whether a view-only link covers sub-pages, with the sub-page part of the link blocked until then. Date: TBD...

#### Rabbit holes
* * *
*   Whether `Do sub-pages inherit the link?` stays open until Lena settles it with the security reviewer
*   The same answer decides what Duplicate copies from a shared page

#### No-gos
* * *
*   TBD...
* * *
