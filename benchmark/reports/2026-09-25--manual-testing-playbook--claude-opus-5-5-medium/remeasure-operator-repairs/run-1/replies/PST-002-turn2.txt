````markdown
# Member - Sharing - View-only links

* * *
_A story is used to define product requirements, acceptance criteria, etc._
_Use it as the foundation for Tasks that work towards fulfilling the acceptance criteria._

## About
* * *
This story adds a view-only link to a page. Anyone with the link can read the page without signing in, and the member who shares it can switch the link off, reset it or let it expire. The Share panel, the plan limits and the page a reader sees through the link are all in scope.

### Problem
* * *
Today a page opens only for someone invited as a member or a guest. Nobody can hand out a page to read without an invite and a sign-in. Agencies on Plus asked for this change most, because today they invite a client as a guest only so the client can read one page.

### Solution
* * *
Give the page a link that anyone can open read-only, with no account. People who can already edit the page turn the link on from the Share panel. They keep control of it after that, because they can switch it off, reset it or set it to expire. The workspace plan decides how many links can be active and which expiry options are available. On Team, Admins can also turn links off for the whole workspace.

#### **Expected outcomes**
* * *
*   A client can read a shared page from a link, with no guest invite and no sign-in
*   A link that is switched off, reset or expired stops working for everyone who holds it
*   Pages opened through a link stay out of search engines
##   

## Requirements
* * *
**Share panel**
* * *
*   A new row sits at the bottom of the Share panel with the switch `Anyone with the link can view`
*   The switch is off by default
*   Turning the switch on creates the link and shows `Copy link` next to the switch
*   The `Link expires` menu sits under the switch and lists `Never`, `7 days` and `30 days`
*   `Never` is the default expiry
*   An expired link counts as off
*   Turning the switch off stops the link working within `60 seconds`
*   `Reset link` stops the old link working within `60 seconds` and creates a new one
*   Someone who already has the page open gets `This link no longer works` on their next action
*   Members with edit access to the page, Admins and the Owner can turn the switch on
*   Guests never see the switch

**Plans**
* * *
*   An active link is one that is switched on and not expired
*   Free allows up to `3` active links per workspace, with `Never` as the only expiry
*   Plus has no link limit and every expiry option
*   Team has no link limit and every expiry option
*   On Team, Admins can turn view-only links off for the whole workspace
*   On Free at the limit the switch stays visible, and turning it on opens `Your workspace has 3 active links. Turn one off or upgrade to Plus to add more.`
*   When a Team Admin turns view-only links off, every link in the workspace stops working within `60 seconds`
*   While a Team Admin has links turned off, the switch shows as off with the note `Turned off by your workspace admin`

**What a viewer sees**
* * *
**Open:** Whether a link on a page also opens its sub-pages. The answer also decides what `Duplicate` copies. Lena settles it with the security reviewer, and no date is set.

*   Opening the link needs no sign-in
*   The page opens read-only, with any inline database as a read-only table
*   A slim top bar holds the page title, the workspace name and a `Try Loomlist` button
*   Comments, page history and the workspace sidebar are not shown
*   Signed-in viewers see `Duplicate` in the top bar, and it copies the page into a workspace of theirs
*   A viewer who is not signed in and taps `Duplicate` gets a sign-in prompt instead
*   Every page opened through a view-only link is served with `noindex`
*   On iOS and Android the link opens the app when it is installed and the web page otherwise
* * *
##   

## Acceptance criteria
* * *
All acceptance criteria below must be met, or discuss and rescope any that cannot be met.

#### Share panel
* * *
1\. **A member who can edit a page can hand out a link to read it**
* * *
*   **Given** a member with edit access, an Admin or the Owner has the Share panel open on a page
*   **When** they turn on the view-only link
*   **Then** a link is created that they can copy right away and send to anyone
*   **And** a guest who opens the same Share panel never sees the option
* * *
- [ ] _Mark as done, if the criteria are met_

2\. **A link stops working once the sharer ends it**
* * *
*   **Given** a page has an active view-only link
*   **When** the sharer switches it off or resets it, or the link reaches its expiry
*   **Then** the old link stops opening the page for everyone who holds it, within the time the Share panel promises
*   **And** a reader who already has the page open is told on their next action that the link no longer works
* * *
- [ ] _Mark as done, if the criteria are met_

#### Plans
* * *
3\. **A Free workspace at its limit is told why and what to do next**
* * *
*   **Given** a Free workspace already has as many active links as its plan allows
*   **When** a member tries to turn on another link
*   **Then** no new link is created, and the member sees why and the two ways forward: turn a link off or upgrade
* * *
- [ ] _Mark as done, if the criteria are met_

4\. **A Team Admin can close every link in the workspace at once**
* * *
*   **Given** a Team workspace has active view-only links on several pages
*   **When** an Admin turns view-only links off for the workspace
*   **Then** every link in the workspace stops opening its page
*   **And** anyone who opens a Share panel in that workspace sees that the link is off because of the workspace admin
* * *
- [ ] _Mark as done, if the criteria are met_

#### Viewer
* * *
5\. **Anyone with the link can read the page and nothing else**
* * *
*   **Given** someone who is not a member or a guest of the workspace has a working link
*   **When** they open it on any surface
*   **Then** they read the page without signing in, with no way to edit it and no way into the rest of the workspace
*   **And** on iOS and Android the link opens in the app when it is installed, and on the web otherwise
*   **And** the page does not show up in search engine results
* * *
- [ ] _Mark as done, if the criteria are met_

6\. **A reader can take a copy of the page into their own workspace**
* * *
*   **Given** a reader has a page open through a view-only link
*   **When** they choose to duplicate it
*   **Then** a reader who is signed in gets a copy of the page in a workspace of theirs
*   **And** a reader who is not signed in is asked to sign in first
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

*   **Security reviewer** - talks the sub-page question through with Lena before she settles it. Until then, sub-page behavior and what `Duplicate` copies stay undecided. Date: TBD...

#### Rabbit holes
* * *
Areas that could waste effort, create ambiguity or distract from the intended outcome.

*   Whether a link on a page also opens its sub-pages. Design wants sub-pages included, with a switch on each sub-page to leave it out, because readers in research sessions stopped reading when a link inside a shared page hit a sign-in wall. Engineering wants each page to get its own link, so that a sub-page added later never becomes public without someone choosing that. Lena decides after talking it through with the security reviewer

#### No-gos
* * *
Explicit scope exclusions and behaviors the delivery team must not introduce.

*   TBD...
* * *
````

Export-equivalent path: `export/002 - Story-view-only-share-links.md`

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: `TBD...` in the Delivery slots, because it's a fixed house placeholder. Quoted product copy in backticks stays exactly as it appears in Kofi's notes.

I wrote this as a **Story**. It passes the quality checks. Every value in Kofi's notes is under Requirements, grouped the way his notes group them. The acceptance criteria describe what users get and don't repeat those values.

- **Sub-page question:** it's an **Open:** line on the viewer group, as you asked. That also adds the `## Delivery` section, where the same question is repeated under Rabbit holes. Because it's undecided, no acceptance criterion says what `Duplicate` copies beyond the page itself.
- **Agency need:** I used your note about agencies on Plus for the Problem section.

**Things I decided that you can change:**
- **Title and role:** I used `Member - Sharing - View-only links`, with the sharing member as the role.
- **Scope:** I kept the Team Admin switch-off and opening links in the iOS and Android apps in this Story, because Kofi's notes give values for both.
- **Security reviewer:** I added them as an external dependency with no date. If they're part of the Sharing team, that line should move into Estimation instead.
- **Left empty:** References has no entries because no frame URLs were supplied. Estimation and No-gos are left as `TBD...`.

**Not covered because the notes don't say:**
- Whether a Member with view access sees the switch disabled or doesn't see it at all
- How the Link expires menu looks on Free
- What happens to links over the limit of 3 when a workspace moves down to Free

If you want the ClickUp connector to push this, tell me and I'll do it only once you confirm.