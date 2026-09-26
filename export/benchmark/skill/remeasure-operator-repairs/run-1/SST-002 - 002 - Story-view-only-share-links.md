# Member - Sharing - View-only share links

* * *
_A story is used to define product requirements, acceptance criteria, etc._
_Use it as the foundation for Tasks that work towards fulfilling the acceptance criteria._

## About
* * *
A page gets a link that anyone can open without signing in, read-only. This story covers the link switch and its settings in the Share panel, the limits each plan puts on links and the page a viewer sees when they open one on Web, iOS or Android.

### Problem
* * *
Today a page can only be shared by inviting a member or a guest. Agencies on Plus asked for view-only links more than anyone else, because they invite clients as guests only so the client can read one page. In the design research sessions, readers who hit a sign-in wall stopped reading.

### Solution
* * *
A member who can edit a page turns on one switch in the Share panel and copies a link. Anyone with the link reads the page without an account, and the member keeps control: the link can expire, be reset or be turned off, and it stops working shortly after. Plans set how many links a workspace can hold and which expiry options it gets, and Team Admins can turn links off for the whole workspace.

#### **Expected outcomes**
* * *
*   Agencies on Plus share a page with a client without adding the client as a guest
*   Clients read a shared page without creating an account or signing in
*   Members, Admins and Owners can take back access to a shared page at any time
##   

## Requirements
* * *
**Share panel**
* * *
*   A new row at the bottom of the Share panel holds the switch `Anyone with the link can view`, per the `Share / View-only link` frame
*   The switch is off by default
*   Turning the switch on creates the link and shows `Copy link` next to the switch
*   The `Link expires` menu under the switch lists `Never`, `7 days` and `30 days`, with `Never` as the default, per the `Share / Link settings` frame
*   An expired link counts as off
*   Turning the switch off stops the link working within `60 seconds`
*   `Reset link` stops the old link working within `60 seconds` and creates a new link
*   A viewer who already has the page open when the link stops working gets `This link no longer works` on their next action
*   Members with edit access to the page, Admins and the Owner can turn the switch on
*   Guests never see the switch

**Plans**
* * *
*   Free: up to `3` active links per workspace, with `Never` as the only expiry option
*   Plus: no limit on active links, every expiry option
*   Team: no limit on active links, every expiry option, and Admins can turn view-only links off for the whole workspace
*   An active link is a link that is switched on and not expired
*   On Free at the limit, the switch stays visible and turning it on opens `Your workspace has 3 active links. Turn one off or upgrade to Plus to add more.`
*   When a Team Admin turns view-only links off, every link in the workspace stops working within the same `60 seconds`
*   While a Team Admin has links turned off, the switch shows as off with the note `Turned off by your workspace admin`

**What a viewer sees**
* * *
**Open:** whether a link on a page also opens its sub-pages, and so what `Duplicate` copies. Lena decides with the security reviewer, with no date set, and the decision lands after the build starts.

*   Opening a link needs no sign-in
*   The page is read-only, and any inline database on it shows as a read-only table, per the `Shared page / Viewer` frame
*   The top bar carries the page title, the workspace name and a `Try Loomlist` button
*   The viewer never exposes comments, page history or the workspace sidebar
*   For a signed-in viewer, `Duplicate` in the top bar copies the page into a workspace of theirs
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
1\. **A member shares a page with anyone through a link**
* * *
*   **Given** a member with edit access to a page on a Plus workspace
*   **When** they turn on the view-only link and copy it
*   **Then** anyone who opens the link reads the page without signing in
*   **And** the link keeps working until it expires, is reset or is turned off
* * *
- [ ] _Mark as done, if the criteria are met_

2\. **Turning a link off or resetting it takes access back**
* * *
*   **Given** a page with an active view-only link that someone has open
*   **When** a member turns the link off, resets it or the link expires
*   **Then** the old link stops opening the page within the window set in Requirements
*   **And** the person who has the page open is told the link no longer works on their next action
* * *
- [ ] _Mark as done, if the criteria are met_

3\. **Guests and view-only members cannot create a link**
* * *
*   **Given** a guest, or a member with view access only, opens the Share panel of a page
*   **When** they look for the view-only link
*   **Then** they cannot turn a link on, and a guest does not see the switch at all
* * *
- [ ] _Mark as done, if the criteria are met_

#### Plans
* * *
4\. **Free workspaces stay within their link limit**
* * *
*   **Given** a Free workspace that already has the maximum number of active links
*   **When** a member turns on the link for another page
*   **Then** no new link is created and the member is told how to free a link or upgrade
*   **And** the only expiry option offered on Free is the one Requirements allows
* * *
- [ ] _Mark as done, if the criteria are met_

5\. **A Team Admin turns links off for the whole workspace**
* * *
*   **Given** a Team workspace with active view-only links on several pages
*   **When** an Admin turns view-only links off for the workspace
*   **Then** every link in the workspace stops opening its page within the window set in Requirements
*   **And** members opening the Share panel see the switch off with the reason
* * *
- [ ] _Mark as done, if the criteria are met_

#### Viewer
* * *
6\. **A viewer reads the page and nothing else of the workspace**
* * *
*   **Given** someone who opens a view-only link, signed in or not
*   **When** the page loads
*   **Then** they can read the page and any inline database on it, and cannot change anything
*   **And** they cannot reach comments, page history or the workspace sidebar
*   **And** the page does not appear in search engine results
* * *
- [ ] _Mark as done, if the criteria are met_

7\. **A viewer can copy the page into their own workspace**
* * *
*   **Given** a viewer on a page opened through a view-only link
*   **When** they tap Duplicate while signed in
*   **Then** the page is copied into a workspace of theirs
*   **And** a viewer who is not signed in is asked to sign in instead
* * *
- [ ] _Mark as done, if the criteria are met_

8\. **The link opens where the viewer is**
* * *
*   **Given** a viewer who taps a view-only link on an iOS or Android phone or tablet
*   **When** Loomlist is installed on the device
*   **Then** the page opens in the app
*   **And** when the app is not installed, the page opens on the web
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

#### External dependencies
* * *
Constraints outside the team's control that gate delivery, with no date the team can set.

*   **Security reviewer, with Lena** - settle whether a link on a page also opens its sub-pages, which blocks sub-page behavior and what `Duplicate` copies. Date: TBD...

#### Rabbit holes
* * *
Areas that could waste effort, create ambiguity or distract from the intended outcome.

*   Sub-page inheritance is open and will not be settled before the build starts. Design (Kofi) proposes that a link also opens sub-pages, with a switch on each sub-page to leave it out. Engineering (Caio) proposes one link per page, so a sub-page added later never becomes public without anyone choosing that. Building either way before Lena decides risks rework on link access and `Duplicate`

#### No-gos
* * *
Explicit scope exclusions and behaviors the delivery team must not introduce.

*   TBD...
* * *
