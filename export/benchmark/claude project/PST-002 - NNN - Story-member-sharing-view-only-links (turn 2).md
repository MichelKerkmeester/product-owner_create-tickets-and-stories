# Member - Sharing - View-only links

* * *
_A story is used to define product requirements, acceptance criteria, etc._
_Use it as the foundation for Tasks that work towards fulfilling the acceptance criteria._

## About
* * *
This story adds a view-only link to a page, so anyone with the link can open and read it without signing in or changing anything. It covers the Share panel switch, each plan's link limits and what a viewer sees. The designs are the `Share / View-only link`, `Share / Link settings` and `Shared page / Viewer` frames in the Sharing design file, reviewed on 2026-09-15.

### Problem
* * *
Today the only way to share a page is to invite a member or a guest by email. Agencies on Plus have asked for this change most, since they now invite clients as guests only so that a client can read one page.

### Solution
* * *
People who can already edit a page can turn on a view-only link from the Share panel. The link holder reads the page without an account and sees nothing else of the workspace.

The sharer stays in control after the link goes out, because a link can be turned off, reset or left to expire, and a Team workspace can turn every link off at once. The plan decides how many active links a workspace can keep and which expiry options it gets.

#### **Expected outcomes**
* * *
*   An agency sends a client one page to read without inviting the client as a guest
*   Anyone with the link reads the page without an invite or an account
*   A link stops working once the sharer or a Team Admin turns it off
*   Pages opened through a link stay out of search engines
*   A viewer who wants to keep the page can duplicate it or try Loomlist from the page itself
* * *
##   

## Requirements
* * *
**Share panel**
* * *
**Open:** whether a page's link also opens its sub-pages. Design proposes it does, with a switch on each sub-page to leave it out. Engineering proposes one link per page, so a sub-page added later never becomes public unless someone chooses that.

Lena decides after talking with the security reviewer. No date is set, and the decision will not land before the build starts. The answer settles what `Duplicate` copies.

*   A new row sits at the bottom of the Share panel with the switch `Anyone with the link can view`
*   The switch is off by default
*   Turning the switch on creates the link and shows `Copy link` next to the switch
*   The `Link expires` menu sits under the switch and lists `Never`, `7 days` and `30 days`, with `Never` as the default
*   An expired link counts as off
*   Turning the switch off stops the link working within `60 seconds`
*   `Reset link` stops the old link working within `60 seconds` and creates a new one
*   A viewer who already has the page open when the link stops gets `This link no longer works` on their next action
*   Members with edit access to the page, Admins and the Owner can turn the switch on
*   Guests never see the switch

**Plans**
* * *
*   Free allows up to `3` active links per workspace, with `Never` as the only expiry option
*   Plus has no limit on active links and every expiry option
*   Team has no limit on active links and every expiry option
*   On Team, Admins can turn view-only links off for the whole workspace
*   An active link is one that is switched on and not expired
*   On Free at the limit, the switch stays visible and turning it on opens `Your workspace has 3 active links. Turn one off or upgrade to Plus to add more.`
*   When a Team Admin turns view-only links off, every link in the workspace stops working within `60 seconds`
*   While a Team Admin has view-only links turned off, each switch shows as off with the note `Turned off by your workspace admin`

**What a viewer sees**
* * *
*   A view-only link opens the page read-only without signing in
*   An inline database shows as a read-only table
*   A slim top bar shows the page title, the workspace name and a `Try Loomlist` button
*   The page shows no comments, no page history and no workspace sidebar
*   For a signed-in viewer, `Duplicate` in the top bar copies the page into a workspace of theirs
*   A viewer who is not signed in and taps `Duplicate` gets a sign-in prompt instead of a copy
*   Every page opened through a view-only link is served with `noindex`
*   On iOS and Android the link opens the app when it is installed, and the web page otherwise
* * *
##   

## Acceptance criteria
* * *
All acceptance criteria below must be met, or discuss and rescope any that cannot be met.

#### Share panel
* * *
1\. **A sharer can turn on a view-only link and hand it out**
* * *
*   **Given** a member with edit access to a page, an Admin or the Owner has the Share panel open
*   **When** they turn on the view-only switch
*   **Then** the page gets a link that anyone can open without signing in, ready to copy from the panel
*   **And** the link keeps the expiry they picked from the options their plan allows
* * *
- [ ] _Mark as done, if the criteria are met_

2\. **A link that is off, reset or expired stops opening the page**
* * *
*   **Given** someone has the page open through a view-only link
*   **When** the sharer turns the link off or resets it, or the link reaches its expiry
*   **Then** the old link stops opening the page within the window set in Requirements, and the viewer is told on their next action that the link no longer works
*   **And** after a reset, the new link opens the page
* * *
- [ ] _Mark as done, if the criteria are met_

3\. **Only people who can edit the page can create a link**
* * *
*   **Given** a guest, or a member without edit access to the page
*   **When** they open the Share panel
*   **Then** they cannot turn on a view-only link, and a guest does not see the switch at all
* * *
- [ ] _Mark as done, if the criteria are met_

#### Plans
* * *
4\. **A Free workspace at its link limit is told why it cannot add another**
* * *
*   **Given** a Free workspace already has the maximum number of active links
*   **When** a member turns on the switch on another page
*   **Then** no new link is created, and the member sees the limit message with the ways to free a slot or upgrade
*   **And** once one of the links is turned off or expires, the workspace can turn on a new one
* * *
- [ ] _Mark as done, if the criteria are met_

5\. **A Team Admin can turn off every link in the workspace**
* * *
*   **Given** a Team workspace with active view-only links
*   **When** an Admin turns view-only links off for the workspace
*   **Then** every link in the workspace stops opening its page within the window set in Requirements
*   **And** the Share panel on each page shows the switch as off and says the workspace admin turned it off
* * *
- [ ] _Mark as done, if the criteria are met_

#### What a viewer sees
* * *
6\. **Someone without an account can read the page and nothing more**
* * *
*   **Given** a person who is not signed in opens a view-only link on the web
*   **When** the page loads
*   **Then** they can read the page, inline databases included, and cannot change anything on it
*   **And** they cannot reach comments, page history or the workspace sidebar
* * *
- [ ] _Mark as done, if the criteria are met_

7\. **Pages shared by link stay out of search results**
* * *
*   **Given** a page with an active view-only link
*   **When** a search engine reaches the page through the link
*   **Then** the page is left out of that search engine's results
* * *
- [ ] _Mark as done, if the criteria are met_

8\. **A viewer can take a copy, or is asked to sign in first**
* * *
*   **Given** a viewer has a page open through a view-only link
*   **When** they tap Duplicate
*   **Then** a signed-in viewer gets a copy of the page in a workspace of theirs
*   **And** a viewer who is not signed in is asked to sign in instead
* * *
- [ ] _Mark as done, if the criteria are met_

9\. **A link opens in the app on phones that have it**
* * *
*   **Given** a person opens a view-only link on iOS or Android
*   **When** Loomlist is installed on the device
*   **Then** the page opens in the app
*   **And** on a device without the app, the page opens on the web
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

*   Sub-page inheritance is still open: one link that also opens sub-pages, each with a switch to leave it out, or a separate link per page
*   Lena decides after talking it through with the security reviewer, with no date set
*   The decision will not land before the build starts
*   What `Duplicate` copies is the only part of the viewer that depends on it

#### No-gos
* * *
Explicit scope exclusions and behaviors the delivery team must not introduce.

*   TBD...
* * *
