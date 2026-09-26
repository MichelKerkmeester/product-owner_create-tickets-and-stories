# Member - Sharing - View-only share links

* * *
_A story is used to define product requirements, acceptance criteria, etc._
_Use it as the foundation for Tasks that work towards fulfilling the acceptance criteria._

## About
* * *
This story adds a link that anyone can open to read a page without signing in. It covers the new switch in the Share panel, the link limits for each plan, the Team Admin control for the whole workspace and the page a viewer sees on Web, iOS and Android.

The design is in Kofi's frames `Share / View-only link`, `Share / Link settings` and `Shared page / Viewer` in the Sharing design file, from the design review on 2026-09-15.

### Problem
* * *
Today the only way to share a page is to invite someone as a member or a guest, because Loomlist has no public link to a page. Agencies on Plus asked for a link more than any other group. Right now they invite each client as a guest only so the client can read one page. In research sessions, readers who followed a link and hit a sign-in wall stopped reading.

### Solution
* * *
A member can turn on a read-only link for a page and send it to a client, who reads the page without an account or an invite. The sharer chooses how long the link lasts and can turn it off or replace it at any time, so a client's access doesn't depend on guest membership. Each plan sets how many links a workspace can have active, and on Team an Admin can turn links off for the whole workspace, so access stays with the people who manage it.

#### **Expected outcomes**
* * *
*   Agencies on Plus share a page with a client by link instead of inviting the client as a guest
*   Clients read a shared page without an account or a sign-in step
*   Sharers and Team Admins can end link access at any time
##   

## Requirements
* * *
**Share panel**
* * *
*   A new row at the bottom of the Share panel holds the switch `Anyone with the link can view`
*   The switch is off by default
*   Turning the switch on creates the link and shows `Copy link` next to the switch
*   The `Link expires` menu sits under the switch with the options `Never`, `7 days` and `30 days`, with `Never` as the default
*   An expired link counts as off
*   Turning the switch off stops the link working within `60 seconds`
*   `Reset link` stops the old link within the same `60 seconds` and creates a new one
*   Someone who has the page open through a link that was turned off, reset or has expired gets `This link no longer works` on their next action
*   Members with edit access to the page, Admins and the Owner can turn the switch on
*   Guests never see the switch

**Plans**
* * *
*   An active link is one that is switched on and not expired
*   Free: up to `3` active links per workspace, with `Never` as the only expiry option
*   Plus: no limit on active links, every expiry option
*   Team: no limit on active links, every expiry option
*   On Free at the limit, the switch stays visible, and turning it on opens `Your workspace has 3 active links. Turn one off or upgrade to Plus to add more.`
*   Team Admins can turn view-only links off for the whole workspace
*   When a Team Admin turns view-only links off, every link in the workspace stops within the same `60 seconds`
*   After a Team Admin turns links off, the switch shows as off with the note `Turned off by your workspace admin`

**What a viewer sees**
* * *
*   The page opens without signing in and is read-only, with any inline database shown as a read-only table
*   A slim top bar shows the page title, the workspace name and a `Try Loomlist` button
*   The viewer page has no comments, no page history and no workspace sidebar
*   Viewers who are signed in get `Duplicate` in the top bar, which copies the page into a workspace of theirs
*   A viewer who is not signed in and taps `Duplicate` gets a sign-in prompt
*   Every page opened through a view-only link is served with `noindex`
*   On iOS and Android the link opens the app when it is installed, and the web page when it isn't

**Sub-pages**
* * *
**Open:** `Do sub-pages inherit the link?` Lena, Product Manager, Sharing and Notifications, decides after talking it through with the security reviewer, and the answer will not be ready before the build starts. The answer also decides what `Duplicate` copies.

*   The link opens the page it was turned on for, as the frames show
* * *
##   

## Acceptance criteria
* * *
All acceptance criteria below must be met, or discuss and rescope any that cannot be met.

#### Share panel
* * *
1\. **A sharer can create, copy and control a link**
* * *
*   **Given** a member with edit access, an Admin or the Owner has a page open
*   **When** they turn on the view-only link in the Share panel
*   **Then** a link is created that they can copy and send straight away
*   **And** they can set when it expires, turn it off or reset it from the same place
*   **And** a guest who opens the Share panel never sees the option
* * *
- [ ] _Mark as done, if the criteria are met_

2\. **A link that is off stops working for everyone who has it**
* * *
*   **Given** a viewer has a page open through a view-only link
*   **When** the link is turned off, reset or expires
*   **Then** the link stops opening the page for anyone who has it
*   **And** the viewer who has the page open is told the link no longer works on their next action
* * *
- [ ] _Mark as done, if the criteria are met_

#### Plans
* * *
3\. **A Free workspace at its limit knows how to add another link**
* * *
*   **Given** a Free workspace has the most active links its plan allows
*   **When** a member tries to turn on another link
*   **Then** no new link is created
*   **And** the member is told how to free a link or which plan removes the limit
* * *
- [ ] _Mark as done, if the criteria are met_

4\. **A Team Admin can stop every link in the workspace**
* * *
*   **Given** a Team workspace has active view-only links
*   **When** an Admin turns view-only links off for the workspace
*   **Then** every link in the workspace stops opening its page
*   **And** members see in the Share panel that an admin turned links off
* * *
- [ ] _Mark as done, if the criteria are met_

#### Viewer
* * *
5\. **A client reads the page without an account**
* * *
*   **Given** a client who is not a member or a guest of the workspace has a view-only link
*   **When** they open it in a browser
*   **Then** they read the page without signing in and cannot change it
*   **And** the page stays out of search engine results
* * *
- [ ] _Mark as done, if the criteria are met_

6\. **A signed-in viewer can keep a copy of the page**
* * *
*   **Given** a viewer is reading a page through a view-only link
*   **When** they choose to duplicate it
*   **Then** a viewer who is signed in gets a copy of the page in a workspace of theirs
*   **And** a viewer who is not signed in is asked to sign in first
* * *
- [ ] _Mark as done, if the criteria are met_

7\. **A link on a phone opens in the app when it is installed**
* * *
*   **Given** a viewer taps a view-only link on iOS or Android
*   **When** the link opens
*   **Then** the page opens in the Loomlist app when it is installed, and on the web otherwise
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

*   `Do sub-pages inherit the link?` is open until Lena decides with the security reviewer, after the build starts. Design proposes yes, with a switch on each sub-page to leave it out. Caio, Backend Engineer, Sharing, proposes no, one link per page, so a sub-page added later never becomes public without someone choosing it. What `Duplicate` copies depends on the answer

#### No-gos
* * *
Explicit scope exclusions and behaviors the delivery team must not introduce.

*   TBD...
* * *
