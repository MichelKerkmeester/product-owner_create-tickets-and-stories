```markdown
# Member - Sharing - View-only links

* * *
## Problem
* * *
Today a page can only be shared by inviting a member or a guest, so anyone outside the workspace needs an invite before they can read a single page. Agencies on Plus invite their clients as guests only so the clients can read one page. Agencies on Plus asked for this most, which makes them the first group this change serves.
* * *
##   

## Solution
* * *
Anyone with a link reads the page without signing in, so a client who needs one page no longer needs an invite into the workspace. A member with edit access, an Admin or the Owner creates the link from the Share panel, and the link can be switched off, reset or set to expire. A signed-in reader can copy the page into their own workspace from the top bar.

**Expected outcomes**
* * *
*   An agency shares one page with a client without inviting the client into the workspace
*   A shared link stops working for everyone who holds it when it is switched off, reset or expires
*   A page opened through a link stays out of search results
* * *
##   

## Requirements
* * *
**Share panel**
* * *
- [] The row is labelled `Anyone with the link can view`, sits at the bottom of the Share panel and is off by default
- [] Turning the switch on creates the link and shows `Copy link` beside the switch
- [] The `Link expires` menu lists `Never`, `7 days` and `30 days`, with `Never` as the default
- [] An expired link counts as off
- [] Members with edit access to the page, Admins and the Owner can turn the switch on
- [] Guests do not see the switch

**Turning a link off**
* * *
- [] Switching the link off stops it working within `60 seconds`
- [] `Reset link` stops the old link within `60 seconds` and creates a new link
- [] A viewer who already has the page open sees `This link no longer works` on their next action

**Plans**
* * *
- [] Free allows up to `3` active links per workspace, with `Never` as the only expiry
- [] Plus allows no link limit and offers every expiry option
- [] Team allows no link limit and offers every expiry option
- [] An active link is switched on and not expired
- [] On Free at the limit, the switch stays visible, and turning it on opens `Your workspace has 3 active links. Turn one off or upgrade to Plus to add more.`

**Workspace admin switch**
* * *
- [] On Team, Admins can turn view-only links off for the whole workspace
- [] Turning them off stops every link in the workspace within `60 seconds`
- [] The switch shows as off with the note `Turned off by your workspace admin`

**Viewer page**
* * *
- [] A viewer sees the page read-only, with any inline database as a read-only table
- [] A viewer sees no comments, no page history and no workspace sidebar
- [] A top bar shows the page title, the workspace name and a `Try Loomlist` button
- [] A signed-in viewer sees `Duplicate` in the top bar, which copies the page into a workspace of theirs
- [] A viewer who is not signed in and taps `Duplicate` sees a sign-in prompt

**Search indexing**
* * *
- [] Every page opened through a view-only link is served with `noindex`

**Mobile opening**
* * *
- [] On iOS and Android the link opens the app when it is installed, and the web page otherwise

**Link scope**
* * *
**Open:** The question `Do sub-pages inherit the link?` is not decided. Lena settles it with the security reviewer, and no date is set.

- [] A view-only link opens the page it is created on
* * *
##   

## Acceptance criteria
* * *
All acceptance criteria below must be met, or discuss and rescope any that cannot be met.

#### Share panel
* * *
1\. **A link opens the page for anyone who has it, without a sign-in**
* * *
*   **Given** a member with edit access to a page, an Admin or the Owner is on the Share panel
*   **When** they switch on `Anyone with the link can view`
*   **Then** anyone with the link opens the page read-only, without signing in
*   **And** search engines leave the page out of their results
* * *
- [] _Mark as done, if the criteria are met_

2\. **A switched-off or reset link stops working for everyone**
* * *
*   **Given** a viewer has a page open through a link
*   **When** a member with edit access switches the link off, or resets it
*   **Then** the old link stops opening the page for anyone
*   **And** the viewer sees `This link no longer works` on their next action
* * *
- [] _Mark as done, if the criteria are met_

3\. **An expired link stops working**
* * *
*   **Given** a link set to expire
*   **When** its expiry passes
*   **Then** the link stops opening the page
*   **And** the switch reads as off
* * *
- [] _Mark as done, if the criteria are met_

#### Plans
* * *
4\. **A Free workspace at its link limit cannot add another link**
* * *
*   **Given** a Free workspace is at its active link limit
*   **When** a member turns on another link
*   **Then** no link is added
*   **And** the member sees the limit message
* * *
- [] _Mark as done, if the criteria are met_

#### Viewer
* * *
5\. **A reader who is not signed in sees the page and nothing around it**
* * *
*   **Given** a viewer who is not signed in opens a page through a link
*   **When** the page loads
*   **Then** the viewer reads the page read-only, with no comments, page history or workspace sidebar
*   **And** the viewer sees the page title, the workspace name and `Try Loomlist` in a top bar
* * *
- [] _Mark as done, if the criteria are met_

6\. **A signed-in viewer copies the page into their own workspace**
* * *
*   **Given** a viewer who is signed in opens a page through a link
*   **When** they tap `Duplicate` in the top bar
*   **Then** the page is copied into a workspace of theirs
* * *
- [] _Mark as done, if the criteria are met_

7\. **A viewer who is not signed in is asked to sign in before copying**
* * *
*   **Given** a viewer who is not signed in opens a page through a link
*   **When** they tap `Duplicate`
*   **Then** they see a sign-in prompt
* * *
- [] _Mark as done, if the criteria are met_

#### Workspace admin
* * *
8\. **A Team admin turns every link in the workspace off at once**
* * *
*   **Given** a Team workspace has active links
*   **When** its Admin turns view-only links off for the whole workspace
*   **Then** every link in the workspace stops opening its page
*   **And** the switch shows as off with the note `Turned off by your workspace admin`
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
*   **Security reviewer** - talks the sub-page question through with Lena, who settles it after that, blocked until then: the sub-page part of link scope. Date: TBD...

#### Rabbit holes
* * *
*   Building sub-page inheritance, or a per-sub-page switch, before the sub-page question is decided. Open: `Do sub-pages inherit the link?`

#### No-gos
* * *
*   TBD...
* * *
```

Export-equivalent path: `export/002 - Story-view-only-share-links.md`

Artifact kind: Story, from the `$story` command. I did not split it into an Epic. The four surfaces it covers (Share panel, Plans, Viewer, Workspace admin) are the reason to revisit that if the team wants child stories.

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.

Things I added or chose, so you can strike them:

- **Title segment:** `Member` and `Sharing` are my choices. Change them if the team names the persona differently.
- **Security reviewer:** I listed it as an external dependency because the notes say Lena settles the question after talking it through with the security reviewer, with no date. It is not a formal sign-off as far as the notes show.
- **Delivery section:** the `**Open:**` line forces it, so it is written. Estimation and No-gos stay `TBD...` because the notes give nothing for them.
- **No link added on a full Free workspace:** criterion 4 says no link is added at the limit. The notes imply this from the limit message but do not state it.

The business problem is thinner than the Problem section needs. The notes and your message give the user cost and Plus demand, but no revenue or retention figure. The context page lists guests as not billed, so inviting a client as a guest costs the agency no seat. The business case for this Story needs another reason, and you may want to add one before the Story goes to the team.

There is no ClickUp connector in this session, so I have not offered a push.