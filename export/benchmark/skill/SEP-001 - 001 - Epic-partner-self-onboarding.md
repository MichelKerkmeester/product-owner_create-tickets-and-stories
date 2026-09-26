# Epic - Partner - Self-onboarding

* * *
## About
* * *
Partner Hub self-onboarding replaces Ops agents' hand setup of new properties, in six child stories, one per stage in Freya's brief.

#### Problem
* * *
After sign-up, an Ops agent collects photos, room types, rates, policies, city tax, bank details and identity documents by email and builds the listing in Back office.

Most partners who drop out do so while waiting for an agent's reply, not while filling anything in. Exit calls say they heard nothing for days and listed elsewhere.

**The following issues rise from that:**
*   Median time from sign-up to go-live is 11 business days
*   38% of sign-ups never go live, 813 of the 2,140 from January to June 2026
*   Each property takes an Ops agent about 4.5 hours
*   640 properties wait in the queue today
####   

#### Goal
* * *
Independent properties with up to 40 rooms self-onboard and go live in a median of 3 business days.

Target: 1,500 self-onboarded properties live by 2027-06-30, against 18,000 live today.

**Direct user/Barter benefits:**
*   Partners move on their own schedule instead of waiting for a reply
*   Ops agents review finished listings instead of building them
*   Fake listings, wrong city tax and poor photos are caught before booking
####   

#### Solution
* * *
In order to get there, we will:
*   Move setup into Partner Hub as six ordered, resumable stages
*   Gate go-live on identity checks and an Ops agent review, and payouts on the checks
*   Keep properties over 40 rooms and chains on the assisted path with a partner manager
*   Keep channel manager users on assisted onboarding until that connection ships

#### **References**
* * *
Sources
*   Partner self-onboarding in Partner Hub, strategy brief, Freya, Director of Partner Growth, 2026-09-22
*   Roamstay company context, Leila, Product Operations Lead, last reviewed 2026-09-18

## Scope
* * *
All six stages ship in the first release. Partner squad owns stages 1 to 4 in Partner Hub and `partner-service`, and Payments squad owns stage 5 payout details and the payment provider handover.

Ops Tools squad builds the stage 6 Go-live review queue in Back office, which Bram, Ops Lead, agreed to pilot.

#### Getting verified
* * *
*   Partner - Self-onboarding - Sign-up and verification: email and phone confirmed, business registration number checked against the country's register

#### Building the listing
* * *
Photos are checked for size and resolution on upload, and city tax is set per adult per night or per stay.

*   Partner - Self-onboarding - Property profile and photos: address, map pin, description, facilities and at least `8` photos of up to `20 MB` each
*   Partner - Self-onboarding - Rooms and rates setup: room types with occupancy, a base price per night and at least one rate plan, free cancellation or non-refundable
*   Partner - Self-onboarding - Policies and city tax: check-in and check-out times, cancellation policy per rate plan, house rules and the city tax rule

#### Getting paid
* * *
Only a Partner Hub Owner can change payout details.

*   Partner - Self-onboarding - Payout details and identity checks: bank account and the owner's identity document, checked by the identity verification provider

#### Going live
* * *
The review checks every listing's city tax rule, and a sent-back listing carries a reason per stage.

*   Ops agent - Self-onboarding - Go-live review queue: an Ops agent approves or sends back the finished listing in Back office within `1 business day`

#### Added Later
* * *
Capabilities that belong to the epic but do not block the first release.

**Channel manager connection**
*   Connecting a channel manager during self-onboarding, its own integration project
*   Until it ships, they stay on assisted onboarding
* * *
##   

## Acceptance criteria
* * *
These are release-level outcomes.
Each child story carries the detailed criteria for its own screens and states.

1\. **An eligible partner goes live without an Ops agent doing the setup**
* * *
*   **Given** an independent hotel, guesthouse or apartment building, up to 40 rooms, no channel manager
*   **When** the partner completes all six stages and an Ops agent approves the listing
*   **Then** the property is bookable in the Guest app
*   **And** no Ops agent entered any setup details
- [] _Mark as done, if the criteria are met_

2\. **A partner can stop and continue later**
* * *
*   **Given** a partner who leaves part-way through any stage
*   **When** they come back to Partner Hub
*   **Then** they resume where they stopped, with saved work in place
- [] _Mark as done, if the criteria are met_

3\. **Nothing goes live or pays out before the checks pass**
* * *
*   **Given** a self-onboarded property without a passed identity check or an approved listing
*   **When** a guest searches for it
*   **Then** it is not bookable
*   **And** no payout is sent until the bank account and identity checks pass
- [] _Mark as done, if the criteria are met_

4\. **A sent-back listing tells the partner what to fix**
* * *
*   **Given** a finished listing in the Go-live review queue
*   **When** the Ops agent sends it back
*   **Then** the partner sees each stage to change and why
*   **And** the partner can resubmit once those are fixed
- [] _Mark as done, if the criteria are met_

5\. **Ineligible properties stay on the assisted path**
* * *
*   **Given** a property with more than 40 rooms, a chain or a channel manager
*   **When** the partner signs up
*   **Then** it goes through assisted onboarding with a partner manager
- [] _Mark as done, if the criteria are met_

6\. **The squads can see whether self-onboarding works**
* * *
*   **Given** self-onboarded properties moving through the stages
*   **When** the Partner squad reviews results
*   **Then** it sees median sign-up to go-live time and time per stage
*   **And** it sees drop-off per stage against today's 38%, sent-back share with reasons and city tax or photo complaints in the first 90 days
- [] _Mark as done, if the criteria are met_
* * *
##   

## Delivery
* * *
#### Estimation
* * *
Each squad sizes its own child stories before planning closes, and Ops Tools squad sizes the stage 6 queue capacity with Partner Growth.

*   TBD...

#### Rabbit holes
* * *
Areas that could waste effort, create ambiguity or distract from the intended outcome.

*   The brief does not say how sign-up spots properties over 40 rooms, chains or channel manager users
*   Nor does it say how such a property moves to the assisted path
*   The registration check needs a register per country across Europe and the United States
*   The brief sets no minimum photo resolution
*   The review queue has to hold `1 business day` as volume grows toward 1,500 properties

#### No-gos
* * *
Explicit scope exclusions and behaviors the delivery team must not introduce.

*   Self-onboarding for properties over 40 rooms or for chains
*   An Ops agent building or editing a self-onboarded listing's setup instead of reviewing it
*   A payout before the bank account and identity checks pass
* * *
