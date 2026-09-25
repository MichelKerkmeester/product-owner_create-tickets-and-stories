# Epic - Partner - Self-onboarding

* * *
## About
* * *
Partner Hub self-onboarding replaces the hand setup Ops agents do today for new properties. The work is split into six child stories, one per stage in Freya's brief, and all six ship in the first release.

### Problem
* * *
Every new property on Roamstay is set up by hand. A partner fills in a short sign-up form, then an Ops agent collects photos, room types, rates, policies, city tax, bank details and identity documents by email and builds the listing in Back office. Most partners who drop out do so while they wait for an agent to reply, not while they fill anything in. On exit calls they say they heard nothing for days and listed their rooms somewhere else.

**The following issues rise from that:**
*   Median time from sign-up to go-live is 11 business days
*   38% of sign-ups never go live, which is 813 of the 2,140 partners who signed up from January to June 2026
*   Each property takes an Ops agent about 4.5 hours of work, spread across the whole wait
*   640 properties are waiting in the queue today
###   

### Goal
* * *
Independent properties with up to 40 rooms set themselves up in Partner Hub and go live in a median of 3 business days, with no Ops agent doing the setup. Ops agents only check a finished listing before it goes live.

Target: 1,500 properties live through self-onboarding by 2027-06-30. For scale, Roamstay has 18,000 properties live today.

**Direct user/Barter benefits:**
*   Partners move forward on their own schedule instead of waiting for an agent's reply, where most drop-off happens today
*   Ops agents spend their time on reviewing a finished listing, not on collecting details by email and building it
*   Fake listings, wrong city tax and poor photos are caught before a guest can book the property
###   

### Solution
* * *
In order to get there, we will:
*   Move property setup into Partner Hub as six stages the partner completes in order, with the option to save and come back at any point
*   Put identity checks and an Ops agent review in front of go-live, and hold payouts until the bank account and identity checks pass
*   Keep properties with more than 40 rooms and chains on the assisted path with a partner manager, and keep properties that run a channel manager on assisted onboarding until the channel manager connection ships

#### **References**
* * *
Sources
*   Partner self-onboarding in Partner Hub, strategy brief, Freya, Director of Partner Growth, 2026-09-22
*   Roamstay company context, Leila, Product Operations Lead, last reviewed 2026-09-18

## Scope
* * *
Each child story owns one stage and carries its own detailed requirements and acceptance criteria. All six stages ship in the first release. Partner squad owns stages 1 to 4 in Partner Hub and `partner-service`. Payments squad owns payout details and the handover to the payment provider in stage 5. Ops Tools squad builds the Go-live review queue in Back office for stage 6, and Bram, Ops Lead, has agreed to pilot it with his agents.

#### Getting verified
* * *
*   Partner - Self-onboarding - Sign-up and verification: email and phone confirmed, business registration number checked against the country's business register

#### Building the listing
* * *
*   Partner - Self-onboarding - Property profile and photos: address and map pin, description, facilities and at least `8` photos of up to `20 MB` each, with size and resolution checked on upload
*   Partner - Self-onboarding - Rooms and rates setup: room types with their occupancy, a base price per night and at least one rate plan, either free cancellation or non-refundable
*   Partner - Self-onboarding - Policies and city tax: check-in and check-out times, the cancellation policy per rate plan, house rules and the city tax rule, per adult per night or per stay

#### Getting paid
* * *
*   Partner - Self-onboarding - Payout details and identity checks: bank account and the owner's identity document, checked by the identity verification provider, with no payout before both pass. Only a Partner Hub Owner can change payout details

#### Going live
* * *
*   Ops agent - Self-onboarding - Go-live review queue: an Ops agent checks the finished listing in Back office within `1 business day`, including the city tax rule on every listing, then approves it or sends it back with a reason per stage

#### Added Later
* * *
Capabilities that belong to the epic but do not block the first release.

**Channel manager connection**
*   Lets a partner who runs a channel manager connect it during self-onboarding, which is its own integration project. Until it ships, these partners stay on assisted onboarding
* * *
##   

## Acceptance criteria
* * *
These are release-level outcomes.
Each child story carries the detailed criteria for its own screens and states.

1\. **An eligible partner goes live without an Ops agent doing the setup**
* * *
*   **Given** an independent hotel, guesthouse or apartment building with up to 40 rooms that runs no channel manager
*   **When** the partner completes all six stages in Partner Hub and an Ops agent approves the listing
*   **Then** the property becomes bookable in the Guest app
*   **And** no Ops agent entered any of the property's setup details
- [ ] _Mark as done, if the criteria are met_

2\. **A partner can stop and continue later**
* * *
*   **Given** a partner who leaves part-way through any stage
*   **When** they come back to Partner Hub
*   **Then** they continue from where they stopped, with everything they saved still in place
- [ ] _Mark as done, if the criteria are met_

3\. **Nothing goes live or pays out before the checks pass**
* * *
*   **Given** a self-onboarded property whose identity check has not passed or whose listing an Ops agent has not approved
*   **When** a guest searches for stays at that property
*   **Then** the property is not bookable
*   **And** no payout is sent to the partner until both the bank account and identity checks pass
- [ ] _Mark as done, if the criteria are met_

4\. **A sent-back listing tells the partner what to fix**
* * *
*   **Given** a finished listing in the Go-live review queue
*   **When** the Ops agent sends it back
*   **Then** the partner sees each stage that needs changes with the agent's reason for it
*   **And** the partner can resubmit the listing for review once those stages are fixed
- [ ] _Mark as done, if the criteria are met_

5\. **Ineligible properties stay on the assisted path**
* * *
*   **Given** a property with more than 40 rooms, a chain or a property that runs a channel manager
*   **When** the partner signs up
*   **Then** the property is set up through assisted onboarding with a partner manager rather than self-onboarding
- [ ] _Mark as done, if the criteria are met_

6\. **The squads can see whether self-onboarding works**
* * *
*   **Given** self-onboarded properties moving through the six stages
*   **When** the Partner squad reviews results
*   **Then** it can see the median time from sign-up to go-live and the time spent in each stage
*   **And** it can see drop-off per stage against today's 38%, the share of listings sent back from the Go-live review queue with their reasons and guest complaints about wrong city tax or wrong photos in each property's first 90 days live
- [ ] _Mark as done, if the criteria are met_
* * *
##   

## Delivery
* * *
#### Estimation
* * *
Each squad sizes its own child stories before planning closes: Partner squad for stages 1 to 4, Payments squad for the payout details in stage 5 and Ops Tools squad for stage 6, including the queue capacity it sizes with Partner Growth.

*   TBD...

#### Rabbit holes
* * *
Areas that could waste effort, create ambiguity or distract from the intended outcome.

*   The brief does not say how a property with more than 40 rooms, a chain or a property that runs a channel manager is identified at sign-up and moved to the assisted path
*   The business registration check runs against each country's business register, and Roamstay lists properties across Europe and the United States
*   The photo step checks resolution on upload, and the brief sets no minimum resolution
*   The Go-live review queue has to hold `1 business day` as volume grows toward 1,500 self-onboarded properties

#### No-gos
* * *
Explicit scope exclusions and behaviors the delivery team must not introduce.

*   Self-onboarding for properties with more than 40 rooms or for chains
*   An Ops agent building or editing a self-onboarded listing's setup instead of reviewing it
*   A payout before the bank account and identity checks pass
* * *
