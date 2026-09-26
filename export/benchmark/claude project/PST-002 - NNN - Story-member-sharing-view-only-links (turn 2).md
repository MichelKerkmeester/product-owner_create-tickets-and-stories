# Member - Sharing - View-only links

* * *
_A story is used to define product requirements, acceptance criteria, etc._
_Use it as the foundation for Tasks that work towards fulfilling the acceptance criteria._

## About
* * *
A view-only link lets anyone read a page without signing in or editing. Designs: the `Share / View-only link`, `Share / Link settings` and `Shared page / Viewer` frames in the Sharing design file, reviewed 2026-09-15.

#### Problem
* * *
Today a page is shared only by inviting a member or guest by email. Agencies on Plus asked for this most, since they invite clients as guests just to read one page.

#### Solution
* * *
When a page editor turns the link on in the Share panel, holders read the page without an account and see nothing else of the workspace.

**Expected outcomes**
* * *
*   An agency sends a client one page to read without a guest invite
*   Link holders read without an invite or account
*   A link stops when the sharer or a Team Admin turns it off
*   Linked pages stay out of search engines
*   Viewers can duplicate the page or try Loomlist from it
* * *
##   

## Requirements
* * *
**Share panel**
* * *
**Open:** whether a page's link also opens its sub-pages. Design proposes yes, with a per-sub-page opt-out. Engineering proposes one link per page, so a later sub-page never goes public by default.

Lena decides after talking with the security reviewer, with no date set, and not before the build starts. The answer settles what `Duplicate` copies.

- [] A new bottom Share panel row holds `Anyone with the link can view`, off by default
- [] Switching on creates the link and shows `Copy link` next to the switch
- [] `Link expires` below lists `Never`, `7 days` and `30 days`, default `Never`
- [] An expired link counts as off
- [] Switching off stops the link within `60 seconds`
- [] `Reset link` stops the old link within `60 seconds` and makes a new one
- [] Once it stops, an open viewer's next action shows `This link no longer works`
- [] Members with edit access to the page, Admins and the Owner can switch it on
- [] Guests never see the switch

**Plans**
* * *
- [] Free: up to `3` active links per workspace, `Never` expiry only
- [] Plus and Team: unlimited active links and every expiry option
- [] On Team, Admins can turn links off workspace-wide
- [] An active link is switched on and not expired
- [] On Free at the limit, the switch stays visible and opens `Your workspace has 3 active links. Turn one off or upgrade to Plus to add more.`
- [] A Team Admin switch-off stops every workspace link within `60 seconds`
- [] While off, each switch shows off with the note `Turned off by your workspace admin`

**What a viewer sees**
* * *
- [] The page opens read-only without sign-in
- [] An inline database shows as a read-only table
- [] A slim top bar shows page title, workspace name and a `Try Loomlist` button
- [] No comments, page history or workspace sidebar show
- [] Top bar `Duplicate` copies the page to a signed-in viewer's workspace
- [] For a signed-out viewer, `Duplicate` prompts sign-in instead
- [] Linked pages are served with `noindex`
- [] On iOS and Android, links open the app if installed, else the web
* * *
##   

## Acceptance criteria
* * *
All acceptance criteria below must be met, or discuss and rescope any that cannot be met.

#### Share panel
* * *
1\. **A sharer can turn on a view-only link and hand it out**
* * *
*   **Given** an editor, Admin or Owner in the Share panel
*   **When** they switch the link on
*   **Then** anyone can open the page from a copyable link, signed in or not
*   **And** it keeps their chosen expiry from the plan's options
* * *
- [] _Mark as done, if the criteria are met_

2\. **A link that is off, reset or expired stops opening the page**
* * *
*   **Given** someone has the page open through a link
*   **When** the sharer turns it off or resets it, or it expires
*   **Then** the old link stops within the Requirements window, and the viewer's next action says so
*   **And** after a reset, the new one works
* * *
- [] _Mark as done, if the criteria are met_

3\. **Only people who can edit the page can create a link**
* * *
*   **Given** a guest or a member without edit access
*   **When** they open the Share panel
*   **Then** they cannot turn a link on, and guests do not see the switch
* * *
- [] _Mark as done, if the criteria are met_

#### Plans
* * *
4\. **A Free workspace at its link limit is told why it cannot add another**
* * *
*   **Given** a Free workspace at its link maximum
*   **When** a member switches on another link
*   **Then** no link is made, and the limit message offers freeing a slot or upgrading
*   **And** once one is turned off or expires, a new one can go on
* * *
- [] _Mark as done, if the criteria are met_

5\. **A Team Admin can turn off every link in the workspace**
* * *
*   **Given** a Team workspace with active links
*   **When** an Admin turns links off workspace-wide
*   **Then** every link stops within the Requirements window
*   **And** each Share panel shows the switch off with the workspace admin note
* * *
- [] _Mark as done, if the criteria are met_

#### What a viewer sees
* * *
6\. **Someone without an account can read the page and nothing more**
* * *
*   **Given** a signed-out person opens a link on the web
*   **When** the page loads
*   **Then** they read it and inline databases but change nothing
*   **And** comments, page history and workspace sidebar are out of reach
* * *
- [] _Mark as done, if the criteria are met_

7\. **Pages shared by link stay out of search results**
* * *
*   **Given** a page with an active link
*   **When** a search engine reaches it through the link
*   **Then** the page stays out of its results
* * *
- [] _Mark as done, if the criteria are met_

8\. **A viewer can take a copy, or is asked to sign in first**
* * *
*   **Given** a viewer has a linked page open
*   **When** they tap Duplicate
*   **Then** a signed-in viewer gets a copy in their workspace
*   **And** a signed-out viewer is asked to sign in instead
* * *
- [] _Mark as done, if the criteria are met_

9\. **A link opens in the app on phones that have it**
* * *
*   **Given** someone opens a link on iOS or Android
*   **When** Loomlist is installed
*   **Then** the page opens in the app
*   **And** otherwise it opens on the web
* * *
- [] _Mark as done, if the criteria are met_
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

*   Sub-page inheritance, open under Share panel until after the build starts
*   What `Duplicate` copies is the only part of the viewer that depends on it

#### No-gos
* * *
Explicit scope exclusions and behaviors the delivery team must not introduce.

*   TBD...
* * *
