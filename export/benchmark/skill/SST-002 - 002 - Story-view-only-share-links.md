# Platform - Sharing - View-only links

* * *
## Problem
* * *
Today a page can only be shared by inviting a member or a guest. Agencies on Plus asked for this most, because they invite their clients as guests only so each client can read one page. A read-only need for one page therefore takes a full invitation for each client.
* * *
##   

## Solution
* * *
A page owner turns on a view-only link from the Share panel and sends it to the client. The client reads the page as a reader, without signing in and without a workspace view around it. The owner ends access by switching the link off or resetting it, so access stays with the page owner.

**Expected outcomes**
* * *
*   A page owner shares one page read-only with a client without inviting the client
*   A client reads the shared page without signing in
*   A page owner ends a client's access by turning the link off or resetting it
* * *
##   

## Requirements
* * *
**Share panel**
* * *
- [] The switch row sits at the bottom of the Share panel, with the switch `Anyone with the link can view`, off by default
- [] Turning the switch on creates the link and shows `Copy link` next to the switch
- [] The Link expires menu lists `Never`, `7 days` and `30 days`, with `Never` as the default
- [] An expired link counts as off
- [] Turning the switch off stops the link working within 60 seconds
- [] `Reset link` stops the old link working within 60 seconds and creates a new link
- [] A viewer who has the page open gets `This link no longer works` on their next action
- [] Members with edit access, Admins and the Owner can turn the switch on
- [] Guests never see the switch

**Plans**
* * *
- [] Free allows up to 3 active links per workspace, with `Never` as the only expiry
- [] Plus allows no link limit, with every expiry option
- [] Team allows no link limit, with every expiry option, and Admins can turn view-only links off for the whole workspace
- [] An active link is switched on and not expired
- [] On Free at the limit, the switch stays visible, and turning it on shows `Your workspace has 3 active links. Turn one off or upgrade to Plus to add more.`
- [] When a Team Admin turns view-only links off, every link in the workspace stops within 60 seconds, and the switch shows as off with the note `Turned off by your workspace admin`

**Viewer page**
* * *
- [] The page is read-only, and an inline database appears as a read-only table
- [] A slim top bar shows the page title, the workspace name and a `Try Loomlist` button
- [] The viewer page has no comments, no page history and no workspace sidebar
- [] A signed-in viewer sees `Duplicate` in the top bar, which copies the page into a workspace of theirs
- [] A viewer who is not signed in gets a sign-in prompt when they tap `Duplicate`
- [] Every page opened through a view-only link is served with `noindex`

**Mobile**
* * *
- [] On iOS and Android, the link opens the app when it is installed, and the web page otherwise

**Sub-pages**
* * *
**Open:** `Do sub-pages inherit the link?` Lena, Product Manager, settles it after talking it through with the security reviewer, and no date is set. Design's view is that a link opens its sub-pages, with a switch on each sub-page to leave it out. Engineering's view (Caio, Backend Engineer) is that each page gets its own link.

- [] Until the question is settled, a view-only link covers only the page it is created on
##   

## Acceptance criteria
* * *
All acceptance criteria below must be met, or discuss and rescope any that cannot be met.

1 ) **Share one page read-only without inviting the client**
* * *
*   **Given** a Member with edit access to a page
*   **When** they turn on the view-only link and send it to a client
*   **Then** the client can read that page without signing in
* * *
- [] _Mark as done, if the criteria are met_

2 ) **Ending access stops the link for viewers**
* * *
*   **Given** a client has the page open through a view-only link
*   **When** the page owner turns the link off or resets it
*   **Then** the client can no longer read the page through the old link
*   **And** the client's next action tells them the link no longer works
* * *
- [] _Mark as done, if the criteria are met_

3 ) **An expired link stops working**
* * *
*   **Given** a view-only link has passed its expiry
*   **When** a client opens that link
*   **Then** the client cannot read the page
*   **And** the page owner sees the switch as off
* * *
- [] _Mark as done, if the criteria are met_

4 ) **A Free workspace stops at its active link limit**
* * *
*   **Given** a Free workspace has already reached its limit of active links
*   **When** an Admin turns on another view-only link
*   **Then** the new link does not become active
*   **And** the Admin sees why the link is blocked and how to add more
* * *
- [] _Mark as done, if the criteria are met_

5 ) **A Team Admin turns view-only links off for the workspace**
* * *
*   **Given** a Team workspace has active view-only links
*   **When** a Team Admin turns view-only links off for the workspace
*   **Then** every view-only link in the workspace stops opening the page for viewers
*   **And** the switch shows as off for the page owners
* * *
##   

## Delivery
* * *
#### Estimation
* * *
*   TBD...

#### External dependencies
* * *
*   **Security reviewer** - reviews the sub-page question with Lena, and the sub-page answer stays blocked until they do. Date: TBD...

#### Rabbit holes
* * *
*   Building either answer to `Do sub-pages inherit the link?` before Lena settles it could waste effort
*   The viewer frames depend on that answer only through what `Duplicate` copies

#### No-gos
* * *
*   TBD...
* * *
