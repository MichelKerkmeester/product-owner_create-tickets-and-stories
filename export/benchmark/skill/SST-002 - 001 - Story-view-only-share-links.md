# Member - Sharing - View-only links

* * *
_A story is used to define product requirements, acceptance criteria, etc._
_Use it as the foundation for Tasks that work towards fulfilling the acceptance criteria._

## About
* * *
This story adds a view-only link to a page: a link anyone can open without signing in, which shows the page read-only. It covers the new row in the Share panel, the plan limits on those links and what a viewer sees when they open one.

The design lives in the Sharing design file, in the frames `Share / View-only link`, `Share / Link settings` and `Shared page / Viewer`, from the design review on 2026-09-15.

### Problem
* * *
Pages are shared by invite only. To let someone read a page, a member has to invite them by email as a member or a guest, and there is no public link to a page. Someone who only needs to read a page has no way in without being added to the workspace.

Agencies on Plus asked for this most. Today they invite clients as guests only so a client can read one page, which puts the client in the workspace when all they needed was a way to read.

### Solution
* * *
The person sharing a page can switch on a link that anyone can open without an account, and the page opens read-only with nothing of the workspace around it. The sharer keeps control of the link, because it can expire, be switched off or be reset, and each of those ends access for the old link.

Plans set how far this goes, so Free workspaces get a small number of links and Team Admins can switch the feature off for the whole workspace.

#### **Expected outcomes**
* * *
*   People outside a workspace can read a shared page without being invited or signing in
*   Agencies on Plus send clients a link to read a page instead of inviting them as guests
*   Sharers can end a link's access themselves, without removing anyone from the workspace
*   Free workspaces that reach the link limit see a path to Plus
*   Team Admins can keep every page in their workspace off public links
##   

## Requirements
* * *
**View-only link**
* * *
**Open:** whether a link on a page also opens its sub-pages is not decided. Design proposes that it does, with a switch on each sub-page to leave it out. Engineering proposes one link per page, so a sub-page added later never becomes public without someone choosing that.

Lena, Product Manager, Sharing and Notifications, decides after talking it through with the security reviewer, with no date set, and the decision will not land before the build starts. The answer also settles what `Duplicate` copies.

*   A view-only link opens the page it was switched on for, and until the open question is settled it opens that page only
*   Anyone with the link can open the page without signing in
*   The link gives read-only access

**Share panel**
* * *
*   A new row sits at the bottom of the Share panel with the switch `Anyone with the link can view`
*   The switch is off by default
*   Turning the switch on creates the link and shows `Copy link` next to the switch
*   The `Link expires` menu sits under the switch with the options `Never`, `7 days` and `30 days`
*   `Never` is the default expiry
*   An expired link counts as off
*   Turning the switch off stops the link working within `60 seconds`
*   `Reset link` stops the old link working within `60 seconds` and creates a new one
*   A viewer who already has the page open when the link stops gets `This link no longer works` on their next action
*   Members with edit access to the page, Admins and the Owner can turn the switch on
*   Guests never see the switch

**Plans**
* * *
*   An active link is one that is switched on and not expired
*   Free: up to `3` active links per workspace, with `Never` as the only expiry
*   Plus: no limit on active links, every expiry option
*   Team: no limit on active links, every expiry option
*   Team: Admins can turn view-only links off for the whole workspace
*   On Free at the limit, the switch stays visible, and turning it on opens `Your workspace has 3 active links. Turn one off or upgrade to Plus to add more.`
*   When a Team Admin turns view-only links off, every link in the workspace stops working within the same `60 seconds`
*   After a Team Admin turns view-only links off, the switch shows as off with the note `Turned off by your workspace admin`

**What a viewer sees**
* * *
*   The page shows read-only, with any inline database shown as a read-only table
*   A slim top bar carries the page title, the workspace name and a `Try Loomlist` button
*   No comments, no page history and no workspace sidebar
*   Viewers who are signed in get `Duplicate` in the top bar, which copies the page into a workspace of theirs
*   A viewer who is not signed in and taps `Duplicate` gets a sign-in prompt instead
*   Every page opened through a view-only link is served with `noindex`
*   On iOS and Android the link opens the app when it is installed, and the web page otherwise
* * *
##   

## Acceptance criteria
* * *
All acceptance criteria below must be met, or discuss and rescope any that cannot be met.

#### Share panel
* * *
1\. **A sharer can publish a page to anyone with the link**
* * *
*   **Given** a member with edit access to a page, an Admin or the Owner
*   **When** they switch on the view-only link in the Share panel
*   **Then** a link exists that they can copy and send, and anyone who opens it reads the page without signing in
*   **And** the link keeps working until it expires, is switched off or is reset
* * *
- [ ] _Mark as done, if the criteria are met_

2\. **A sharer can end a link's access**
* * *
*   **Given** a page with a working view-only link
*   **When** the sharer switches it off or resets it, or the link reaches its expiry
*   **Then** the old link stops opening the page within the time Requirements sets, and a reset leaves a new working link in its place
*   **And** a viewer who has the page open is told the link no longer works on their next action, and sees no further page content
* * *
- [ ] _Mark as done, if the criteria are met_

3\. **Guests cannot publish links**
* * *
*   **Given** a guest with access to a page
*   **When** they open the Share panel
*   **Then** they have no way to create a view-only link
* * *
- [ ] _Mark as done, if the criteria are met_

#### Plans
* * *
4\. **Free workspaces stay within their limit and see the way past it**
* * *
*   **Given** a Free workspace at its active-link limit
*   **When** a sharer tries to switch on another link
*   **Then** no new link is created, and the sharer learns why and how to free a slot or upgrade
*   **And** once a link is switched off, a new one can be switched on
* * *
- [ ] _Mark as done, if the criteria are met_

5\. **A Team Admin can take every page off public links at once**
* * *
*   **Given** a Team workspace with active view-only links
*   **When** an Admin turns view-only links off for the workspace
*   **Then** no link in the workspace opens its page any longer, within the same time as a single switch-off
*   **And** sharers see that the switch is off because of the workspace admin, rather than a switch they can turn back on
* * *
- [ ] _Mark as done, if the criteria are met_

#### Viewer
* * *
6\. **A viewer reads the page and nothing else of the workspace**
* * *
*   **Given** someone opens a working view-only link, signed in or not
*   **When** the page loads
*   **Then** they can read the page, inline databases included, and cannot change anything on it
*   **And** comments, page history and the rest of the workspace stay out of reach, and search engines leave the page out of their results
* * *
- [ ] _Mark as done, if the criteria are met_

7\. **A viewer can keep a copy of the page**
* * *
*   **Given** a viewer on a page opened through a view-only link
*   **When** they choose to duplicate it
*   **Then** a signed-in viewer gets a copy of the page in a workspace of theirs, and a viewer who is not signed in is asked to sign in first
* * *
- [ ] _Mark as done, if the criteria are met_

8\. **The link opens where the viewer is**
* * *
*   **Given** a viewer on iOS or Android
*   **When** they open a view-only link
*   **Then** it opens in the Loomlist app when the app is installed, and in the browser otherwise, showing the same read-only page
* * *
- [ ] _Mark as done, if the criteria are met_
* * *
##   

## Delivery
* * *
#### Estimation
* * *
The delivery budget or expected size for the approved scope.

*   TBD...

#### Rabbit holes
* * *
Areas that could waste effort, create ambiguity or distract from the intended outcome.

*   Sub-page inheritance is not decided: design proposes that a link also opens sub-pages with a per-sub-page opt-out, and engineering proposes one link per page
*   Lena decides sub-page inheritance after the security review, with no date set, and not before the build starts
*   Until the sub-page decision lands, build against a single page and keep what `Duplicate` copies open

#### No-gos
* * *
Explicit scope exclusions and behaviors the delivery team must not introduce.

*   TBD...
* * *
