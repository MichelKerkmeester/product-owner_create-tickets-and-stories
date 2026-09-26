# Member - Sharing - View-only links

* * *
_A story is used to define product requirements, acceptance criteria, etc._
_Use it as the foundation for Tasks that work towards fulfilling the acceptance criteria._

## About
* * *
This story adds a view-only link anyone can open to read a page without signing in: the Share panel row, plan limits and the viewer's view.

Design: the Sharing design file, frames `Share / View-only link`, `Share / Link settings` and `Shared page / Viewer`, from the design review on 2026-09-15.

#### Problem
* * *
Pages are shared only by email invite, as member or guest, so a reader must join the workspace. Agencies on Plus asked most, since they invite clients as guests just to read one page.

#### Solution
* * *
Sharers switch on a link that opens the page read-only, with no account and nothing of the workspace around it. Expiry, switch-off and reset each end its access, and plans set the limits.

**Expected outcomes**
* * *
*   Outsiders read a shared page without an invite or sign-in
*   Plus agencies send clients a link instead of a guest invite
*   Sharers end a link's access without removing anyone from the workspace
*   Free workspaces at the limit see a path to Plus
*   Team Admins can keep all workspace pages off public links
##   

## Requirements
* * *
**View-only link**
* * *
**Open:** whether a link also opens sub-pages is not decided. Design proposes it does, with a per-sub-page opt-out, and Engineering proposes one link per page, so no later sub-page goes public unchosen.

Lena, Product Manager, Sharing and Notifications, decides after talking with the security reviewer, with no date set and not before the build starts. The answer also settles what `Duplicate` copies.

- [] A link opens only the page it was switched on for until the open question is settled
- [] Anyone with the link reads the page without signing in

**Share panel**
* * *
- [] A new bottom Share panel row holds the switch `Anyone with the link can view`, off by default
- [] Switching it on creates the link and shows `Copy link` beside it
- [] The `Link expires` menu below offers `Never`, the default, `7 days` and `30 days`
- [] An expired link counts as off
- [] Switching off stops the link within `60 seconds`
- [] `Reset link` stops the old link within `60 seconds` and creates a new one
- [] A viewer who has the page open when the link stops gets `This link no longer works` on their next action
- [] Members with edit access, Admins and the Owner can switch it on, and guests never see it

**Plans**
* * *
- [] Active means switched on and not expired
- [] Free: up to `3` active links per workspace, `Never` expiry only
- [] Plus: unlimited active links, every expiry option
- [] Team: unlimited active links, every expiry option
- [] Team: Admins can turn view-only links off workspace-wide
- [] On Free at the limit, the switch stays visible and turning it on opens `Your workspace has 3 active links. Turn one off or upgrade to Plus to add more.`
- [] When a Team Admin turns links off, every workspace link stops within the same `60 seconds`
- [] The switch then shows off with the note `Turned off by your workspace admin`

**What a viewer sees**
* * *
- [] The page is read-only, inline databases as read-only tables
- [] A slim top bar shows the page title, workspace name and a `Try Loomlist` button
- [] No comments, page history or workspace sidebar
- [] Signed-in viewers get `Duplicate` in the top bar, copying the page to a workspace of theirs
- [] Signed-out viewers tapping `Duplicate` get a sign-in prompt
- [] Pages opened through a view-only link are served with `noindex`
- [] On iOS and Android the link opens the app if installed, otherwise the web page
* * *
##   

## Acceptance criteria
* * *
All acceptance criteria below must be met, or discuss and rescope any that cannot be met.

#### Share panel
* * *
1\. **A sharer can publish a page to anyone with the link**
* * *
*   **Given** a page editor, an Admin or the Owner
*   **When** they switch on the view-only link
*   **Then** they get a link anyone can use to read the page without signing in
*   **And** it works until it expires, is switched off or is reset
* * *
- [] _Mark as done, if the criteria are met_

2\. **A sharer can end a link's access**
* * *
*   **Given** a working view-only link
*   **When** the sharer switches it off or resets it, or it expires
*   **Then** the old link stops within the Requirements time, and a reset leaves a new working link
*   **And** a viewer on the page is told the link no longer works on their next action and sees nothing more
* * *
- [] _Mark as done, if the criteria are met_

3\. **Guests cannot publish links**
* * *
*   **Given** a guest with page access
*   **When** they open the Share panel
*   **Then** they cannot create a view-only link
* * *
- [] _Mark as done, if the criteria are met_

#### Plans
* * *
4\. **Free workspaces stay within their limit and see the way past it**
* * *
*   **Given** a Free workspace at its active-link limit
*   **When** a sharer switches on another link
*   **Then** none is created, and the sharer learns why and how to free a slot or upgrade
*   **And** switching one off frees a slot
* * *
- [] _Mark as done, if the criteria are met_

5\. **A Team Admin can take every page off public links at once**
* * *
*   **Given** a Team workspace with active links
*   **When** an Admin turns view-only links off
*   **Then** no workspace link opens its page, within the single switch-off time
*   **And** sharers see the workspace admin switched it off, not a switch they can turn back on
* * *
- [] _Mark as done, if the criteria are met_

#### Viewer
* * *
6\. **A viewer reads the page and nothing else of the workspace**
* * *
*   **Given** someone opens a working link, signed in or not
*   **When** the page loads
*   **Then** they read it, inline databases included, and cannot change anything
*   **And** comments, history and the rest of the workspace stay out of reach, and search engines skip the page
* * *
- [] _Mark as done, if the criteria are met_

7\. **A viewer can keep a copy of the page**
* * *
*   **Given** a viewer on a page opened through a link
*   **When** they duplicate it
*   **Then** a signed-in viewer gets a copy in a workspace of theirs, and a signed-out one is asked to sign in first
* * *
- [] _Mark as done, if the criteria are met_

8\. **The link opens where the viewer is**
* * *
*   **Given** a viewer on iOS or Android
*   **When** they open a view-only link
*   **Then** it opens in the Loomlist app if installed, else the browser, showing the same read-only page
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

*   Until Lena's sub-page decision lands, build for a single page and leave what `Duplicate` copies open

#### No-gos
* * *
Explicit scope exclusions and behaviors the delivery team must not introduce.

*   TBD...
* * *
