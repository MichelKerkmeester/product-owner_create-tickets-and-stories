# Epic - Partner - Self-onboarding

* * *
## About
* * *
Partner self-onboarding lets independent properties of up to 40 rooms set themselves up in Partner Hub, through six stages, and go live without an Ops agent doing the setup. This Epic is split into six child stories, one per stage, all in the first release.

#### Problem
* * *
Every new property on Roamstay is set up by hand. A partner fills in a short sign-up form, then an Ops agent collects the rest by email and builds the listing in Back office. The median time from sign-up to go-live is 11 business days.

813 of 2,140 partners who signed up from January to June 2026 never went live, a 38% drop-off. Most of it happens while the partner waits for an agent to reply, not while they fill anything in. Each property takes an Ops agent about 4.5 hours, and 640 properties are waiting in the queue today.
####   

#### Goal
* * *
Independent properties with up to 40 rooms set themselves up in Partner Hub and go live in a median of 3 business days, with no Ops agent doing the setup. Ops agents only check a finished listing before it goes live.

Target: 1,500 properties live through self-onboarding by 2027-06-30. For scale, Roamstay has 18,000 properties live today.
####   

#### Solution
* * *
In order to get there, we will:
*   Let a partner sign up and verify, then set up the property in Partner Hub across the remaining stages, saving and coming back at any stage
*   Check each finished listing in the go-live review queue within 1 business day, then approve it or send it back with a reason for each stage
*   Hold payouts until the bank account and the owner's identity document both pass
*   Keep chains and properties above 40 rooms on the assisted path with a partner manager
*   Keep partners who run a channel manager on assisted onboarding for now

## Scope
* * *
Each child story owns one part of the lifecycle and carries its own detailed requirements and acceptance criteria.

#### Partner setup
* * *
*   Partner - Self-onboarding - Sign-up and verification
*   Partner - Self-onboarding - Property profile and photos
*   Partner - Self-onboarding - Rooms and rates setup
*   Partner - Self-onboarding - Policies and city tax
*   Partner - Self-onboarding - Payout details and identity checks

#### Go-live review
* * *
*   Back office - Self-onboarding - Go-live review queue

#### Added Later
* * *
Capability that belongs to the epic but does not block the first release.

**Channel manager connection**
*   Connect a channel manager as its own integration project, so partners who run one can self-onboard
* * *
##   

## Acceptance criteria
* * *
These are release-level outcomes.
Each child story carries the detailed criteria for its own screens and states.

1 ) **A partner goes live without an Ops agent doing the setup**
* * *
*   **Given** an independent property with up to 40 rooms and a partner signed in to Partner Hub
*   **When** the partner completes all six stages
*   **Then** an Ops agent's only step before go-live is checking the finished listing
*   **And** the listing goes live once that check approves it
* * *
- [] _Mark as done, if the criteria are met_

2 ) **Every finished listing is checked within 1 business day**
* * *
*   **Given** a finished listing in the go-live review queue
*   **When** an Ops agent reviews it
*   **Then** the listing is approved or sent back within 1 business day
*   **And** a listing sent back carries a reason for each stage it failed
* * *
- [] _Mark as done, if the criteria are met_

3 ) **No payout is sent before identity and bank checks pass**
* * *
*   **Given** a property whose bank account or owner identity document has not passed its check
*   **When** a payout falls due for that property
*   **Then** no payout is sent to the partner
*   **And** the payout is sent once both checks have passed
* * *
- [] _Mark as done, if the criteria are met_

4 ) **A partner can save at any stage and come back to it**
* * *
*   **Given** a partner who has completed some of the six stages
*   **When** they leave Partner Hub and come back later
*   **Then** every stage they saved is still there
*   **And** they can carry on from the stage they stopped at
* * *
- [] _Mark as done, if the criteria are met_
* * *
##   
