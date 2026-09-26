# Member - Sharing - View-only links

* * *
_A story is used to define product requirements, acceptance criteria, etc._
_Use it as the foundation for Tasks that work towards fulfilling the acceptance criteria._

## About
* * *
This story adds a view-only link to a Loomlist page. Anyone who has the link can read the page without signing in. It covers the new Share panel row, the link limits on each plan, the Team Admin switch that turns links off for the whole workspace, and what a viewer sees on Web, iOS and Android.

### Problem
* * *
Today the only way to share a page is to invite someone as a member or a guest. There is no public link. Agencies on Plus asked for a link more than anyone else. Right now they invite clients as guests only so those clients can read a single page.

### Solution
* * *
A person who can already edit a page gets one switch that turns a read-only link on or off. Their client opens the page without an account, and nobody has to add a guest to the workspace. Plan limits and the Team Admin switch decide how widely links can be used, so a workspace that cares about access keeps control of what leaves it.

#### **Expected outcomes**
* * *
*   Agencies on Plus can share a page with a client through a link instead of a guest invite
*   Clients read a shared page without creating a Loomlist account
*   A Team Admin can stop every view-only link in the workspace at once
* * *
##   

## Requirements
* * *
**Share panel**
* * *
*   A new row sits at the bottom of the Share panel, with the switch `Anyone with the link can view`
*   The switch is off by default
*   Turning the switch on creates the link and shows `Copy link` next to the switch
*   The `Link expires` menu under the switch lists `Never`, `7 days` and `30 days`, and `Never` is the default
*   An expired link counts as off
*   Turning the switch off stops the link working within `60 seconds`
*   `Reset link` stops the old link working within `60 seconds` and creates a new one
*   A viewer who already has the page open sees `This link no longer works` on their next action
*   Members with edit access to the page, Admins and the Owner can turn the switch on
*   Guests never see the switch

**Plans**
* * *
*   Free allows up to `3` active links per workspace, and `Never` is the only expiry option
*   Plus has no link limit and every expiry option
*   Team has no link limit and every expiry option
*   A link is active when it is switched on and not expired
*   On Free at the limit the switch stays visible, and turning it on opens `Your workspace has 3 active links. Turn one off or upgrade to Plus to add more.`
*   On Team, Admins can turn view-only links off for the whole workspace
*   When a Team Admin turns view-only links off, every link in the workspace stops working within `60 seconds`
*   While workspace links are off, the switch shows as off with the note `Turned off by your workspace admin`

**What a viewer sees**
* * *
**Open:** `Do sub-pages inherit the link?` Lena, Product Manager, Sharing and Notifications, decides after talking it through with the security reviewer. No date is set, and the decision will come after the build starts. Until then the frames show the link on a single page only, and what `Duplicate` copies depends on the answer.

*   Opening the link needs no sign-in
*   The page is read-only, and any inline database shows as a read-only table
*   The top bar shows the page title, the workspace name and a `Try Loomlist` button
*   The viewer gets no comments, no page history and no workspace sidebar
*   For a signed-in viewer the top bar shows `Duplicate`, which copies the page into one of their own workspaces
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
1\. **A person who can edit a page can hand out a read-only link to it**
* * *
*   **Given** a member with edit access, an Admin or the Owner has the Share panel open on a page
*   **When** they turn on the view-only link and copy it
*   **Then** anyone who opens that link can read the page without signing in and cannot change it
*   **And** a guest who opens the Share panel on the same page never sees the option
* * *
- [ ] _Mark as done, if the criteria are met_

2\. **A link that is turned off, reset or expired stops opening the page**
* * *
*   **Given** someone holds a view-only link to a page
*   **When** the sharer turns the link off or resets it, or the link expires
*   **Then** the old link stops opening the page within the cut-off set in Requirements
*   **And** someone who already has the page open is told the link no longer works on their next action
* * *
- [ ] _Mark as done, if the criteria are met_

#### Plans
* * *
3\. **A Free workspace at its limit learns how to add another link**
* * *
*   **Given** a Free workspace already has the maximum number of active links
*   **When** a member turns on another link
*   **Then** no new link goes live, and the member sees how to free one up or upgrade
*   **And** in every workspace the expiry choices match the workspace's plan
* * *
- [ ] _Mark as done, if the criteria are met_

4\. **A Team Admin can turn off every view-only link in the workspace**
* * *
*   **Given** a Team workspace has active view-only links
*   **When** an Admin turns view-only links off for the workspace
*   **Then** every link in the workspace stops opening its page within the cut-off set in Requirements
*   **And** the switch on each page shows as off and says the workspace admin turned it off
* * *
- [ ] _Mark as done, if the criteria are met_

#### Viewer
* * *
5\. **A viewer reads the page and sees nothing else of the workspace**
* * *
*   **Given** someone opens a view-only link
*   **When** the page loads on Web, iOS or Android
*   **Then** they can read the page and its inline databases, and they cannot edit or comment on it, open its history or see the workspace sidebar
*   **And** search engines leave the page out of their results
*   **And** on iOS and Android the link opens in the Loomlist app when it is installed and in the browser otherwise
* * *
- [ ] _Mark as done, if the criteria are met_

6\. **A viewer can copy the page into their own workspace**
* * *
*   **Given** a viewer is reading a page through a view-only link
*   **When** they tap `Duplicate`
*   **Then** a signed-in viewer gets a copy of the page in the workspace they choose
*   **And** a viewer who is not signed in is asked to sign in first
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

*   `Do sub-pages inherit the link?` is still undecided and will not be settled before the build starts. Lena decides after talking it through with the security reviewer
*   Design's view: a link on a page also opens its sub-pages, and each sub-page has a switch to leave itself out. In research sessions, readers who hit a sign-in wall on a linked sub-page stopped reading
*   Engineering's view, from Caio: each page gets its own link, because otherwise a sub-page someone adds later becomes public without anyone choosing that
*   Building sub-page inheritance or the sub-page switch before the decision could waste effort. The same goes for fixing what `Duplicate` copies

#### No-gos
* * *
Explicit scope exclusions and behaviors the delivery team must not introduce.

*   TBD...
* * *
