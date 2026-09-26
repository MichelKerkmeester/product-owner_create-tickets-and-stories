# Epic - Partner Hub - Self-onboarding

* * *
## About
* * *
Self-onboarding lets an independent property set itself up in Partner Hub and go live after an Ops agent checks the finished listing. Today an Ops agent builds every new property by hand.
This Epic is split into six child stories, one per onboarding stage, and all six ship in the first release. Each child story carries its own detailed requirements and acceptance criteria.

### Problem
* * *
Every new property on Roamstay is set up by hand. A partner fills in a short sign-up form, then an Ops agent collects photos, room types, rates, policies, city tax, bank details and identity documents by email, builds the listing in Back office and makes it live. Most partners who drop off do so while they wait for an agent to reply, not while they fill anything in. On exit calls they say they signed up, heard nothing for days and listed their rooms somewhere else.

**The following issues rise from that:**
*   Median time from sign-up to go-live is 11 business days
*   38% of partners who sign up never go live: 813 of 2,140 sign-ups from January to June 2026
*   Each property takes an Ops agent about 4.5 hours of work, spread across the whole wait
*   640 properties are waiting in the queue today
###   

### Goal
* * *
Independent properties with up to 40 rooms set themselves up in Partner Hub and go live in a median of 3 business days, with no Ops agent doing the setup. Ops agents only check a finished listing before it goes live.

Target: 1,500 properties live through self-onboarding by 2027-06-30. Roamstay has 18,000 properties live today.

**Direct user/Roamstay benefits:**
*   Partners move through setup at their own pace instead of waiting for an agent's email
*   Fewer partners give up and list their rooms elsewhere before go-live
*   Ops agent time per new property drops from the full setup to a single review
###   

### Solution
* * *
In order to get there, we will:
*   Take the partner through six stages in Partner Hub, in order, with the option to save and come back at any point
*   Verify the partner before anything else: email and phone confirmed, and the business registration number checked against the country's business register
*   Let the partner build the whole listing themselves: property profile and photos, room types and rates, policies and city tax
*   Collect bank account details and the owner's identity document in Partner Hub, and hold payouts until both checks pass
*   Send every finished listing to a Go-live review queue in Back office, where an Ops agent checks it within 1 business day and approves it or sends it back with a reason per stage
*   Pilot the Go-live review queue with Bram, Ops Lead, and his agents
*   Keep properties with more than 40 rooms, chains and properties that run a channel manager on assisted onboarding

## Scope
* * *
Each child story owns one onboarding stage and carries its own detailed requirements and acceptance criteria, including the tracking for its stage.

#### Partner Hub
* * *
*   Partner Hub - Self-onboarding - Sign-up and verification
*   Partner Hub - Self-onboarding - Property profile and photos
*   Partner Hub - Self-onboarding - Rooms and rates setup
*   Partner Hub - Self-onboarding - Policies and city tax
*   Partner Hub - Self-onboarding - Payout details and identity checks

#### Back office
* * *
*   Back office - Self-onboarding - Go-live review queue

#### Added Later
* * *
This capability belongs to the epic but does not block the first release.

**Channel manager connection**
*   Let a property that runs a channel manager self-onboard by connecting it, instead of staying on assisted onboarding. Connecting a channel manager is its own integration project
* * *
##   

## Acceptance criteria
* * *
These are release-level outcomes.
Each child story carries the detailed criteria for its own screens and states.

1\. **An in-scope partner goes from sign-up to go-live without an Ops agent doing the setup**
* * *
*   **Given** an independent hotel, guesthouse or apartment building with up to 40 rooms and no channel manager
*   **When** the partner completes all six stages in Partner Hub
*   **Then** the finished listing reaches the Go-live review queue with no Ops agent having set up any part of it
*   **And** the partner can leave at any stage and come back to where they stopped, with their saved work intact
* * *
- [ ] _Mark as done, if the criteria are met_

2\. **No property goes live or gets paid before its checks pass**
* * *
*   **Given** a self-onboarded property
*   **When** its identity check or its go-live review has not passed
*   **Then** the property is not bookable in the Guest app
*   **And** no payout is sent until the bank account and the owner's identity document have both passed and the listing has passed its go-live review
* * *
- [ ] _Mark as done, if the criteria are met_

3\. **Every finished listing gets a clear review decision**
* * *
*   **Given** a finished listing in the Go-live review queue
*   **When** an Ops agent reviews it in Back office
*   **Then** the listing is either approved and goes live, or sent back to the partner with a reason for each stage that needs a change
*   **And** the review covers the city tax rule on every listing
* * *
- [ ] _Mark as done, if the criteria are met_

4\. **Out-of-scope properties stay on the assisted path**
* * *
*   **Given** a property with more than 40 rooms, a chain or a property that runs a channel manager
*   **When** its partner signs up
*   **Then** the partner stays on assisted onboarding with a partner manager and is not taken through self-onboarding
* * *
- [ ] _Mark as done, if the criteria are met_

5\. **The squad can tell whether self-onboarding works**
* * *
*   **Given** properties onboarded through self-onboarding
*   **When** the Partner squad reviews the results
*   **Then** it can see the median time from sign-up to go-live, the time spent in each stage and the drop-off per stage, against today's 38%
*   **And** it can see the share of listings sent back from the Go-live review queue with their reasons, and guest complaints about wrong city tax or wrong photos in each property's first 90 days live
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
*   Partner squad sizes the five Partner Hub stories and owns Partner Hub and `partner-service`
*   Ops Tools squad sizes the Go-live review queue, including how it holds 1 business day as volume grows, together with the Partner squad
*   Payments squad sizes the payout details and the handover to the payment provider for payouts

#### Rabbit holes
* * *
Areas that could waste effort, create ambiguity or distract from the intended outcome.

*   Telling an out-of-scope property apart at sign-up: the brief does not say how Partner Hub learns a property's room count, chain status or channel manager use
*   Business register coverage: the registration check runs against each country's business register, and the brief does not say which countries' registers are covered in the first release

#### No-gos
* * *
Explicit scope exclusions and behaviors the delivery team must not introduce.

*   No self-onboarding for properties with more than 40 rooms or for chains. They stay on the assisted path with a partner manager
* * *
