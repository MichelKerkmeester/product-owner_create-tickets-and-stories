# Epic - Partner Hub - Self-onboarding

* * *
## About
* * *
Partner self-onboarding moves new-property setup out of Ops agents' email threads and into Partner Hub. Independent properties with up to 40 rooms work through six stages on their own, and an Ops agent only checks the finished listing before it goes live.
This Epic is split into six child stories, one per stage, and all six ship in the first release.

### Problem
* * *
Every new property on Roamstay is set up by hand. A partner fills in a short sign-up form, then an Ops agent collects photos, room types, rates, policies, city tax, bank details and identity documents by email, builds the listing in Back office and makes it live. Most partners who drop off do so while they wait for an agent to reply, not while they fill anything in.

**The following issues rise from that:**
*   The median time from sign-up to go-live is 11 business days
*   38% of partners who sign up never go live, which is 813 of the 2,140 sign-ups from January to June 2026
*   Each property takes an Ops agent about 4.5 hours of work, spread across the whole wait
*   640 properties are waiting in the queue today
*   On exit calls, partners say they signed up, heard nothing for days and listed their rooms somewhere else
###   

### Goal
* * *
Independent properties with up to 40 rooms set themselves up in Partner Hub and go live in a median of 3 business days, with no Ops agent doing the setup. Ops agents only check a finished listing before it goes live.

Target: 1,500 properties live through self-onboarding by 2027-06-30. For scale, Roamstay has 18,000 properties live today.

**Direct partner/Roamstay benefits:**
*   A partner sets up at their own pace, saving and coming back at any point, instead of waiting days for an agent's reply
*   Ops agents check a finished listing instead of spending about 4.5 hours building each one by email
*   Fewer partners drop off during the wait for an agent, which is where most of today's losses happen

**Measured by:**
*   Median time from sign-up to go-live, and time spent in each stage
*   Drop-off per stage, against today's 38%
*   Share of listings sent back from the Go-live review queue, and the reasons
*   Guest complaints about wrong city tax or wrong photos on self-onboarded properties in their first 90 days live
###   

### Solution
* * *
In order to get there, we will:
*   Move the setup Ops agents do by email into Partner Hub as six stages the partner completes in order, saving and coming back at any point
*   Run the business, identity and bank account checks inside the flow, so no payout goes out before the bank account and identity checks pass and the Go-live review queue approves the listing
*   Replace agent-built listings with a Go-live review queue in Back office, where an Ops agent approves each finished listing or sends it back with a reason per stage
*   Keep properties with more than 40 rooms, chains and properties that run a channel manager on the assisted path

## Scope
* * *
Each child story owns one stage of the self-onboarding flow and carries its own detailed requirements and acceptance criteria. All six ship in the first release.

#### Partner setup in Partner Hub
* * *
*   Partner Hub - Self-onboarding - Sign-up and verification: email and phone confirmed, business registration number checked against the country's business register
*   Partner Hub - Self-onboarding - Property profile and photos: address and map pin, description, facilities and at least `8` photos, each up to `20 MB`, with size and resolution checked on upload
*   Partner Hub - Self-onboarding - Rooms and rates setup: room types with their occupancy, a base price per night and at least one rate plan, free cancellation or non-refundable
*   Partner Hub - Self-onboarding - Policies and city tax: check-in and check-out times, the cancellation policy per rate plan, house rules and the city tax rule, per adult per night or per stay
*   Partner Hub - Self-onboarding - Payout details and identity checks: bank account and the owner's identity document, checked by the identity verification provider, with no payout before both pass

#### Go-live review in Back office
* * *
*   Back office - Self-onboarding - Go-live review queue: an Ops agent checks the finished listing within `1 business day`, including the city tax rule on every listing, then approves it or sends it back with a reason per stage

#### Added Later
* * *
These capabilities belong to the epic but do not block the first release.

**Channel manager connection**
*   Partners who run a channel manager connect it and set themselves up in Partner Hub instead of staying on assisted onboarding
* * *
##   

## Acceptance criteria
* * *
These are release-level outcomes.
Each child story carries the detailed criteria for its own screens and states.

1\. **A partner goes live with no Ops agent doing the setup**
* * *
*   **Given** an independent property with up to 40 rooms that runs no channel manager
*   **When** its partner signs up in Partner Hub
*   **Then** the partner completes all six stages in order on their own, saving and coming back at any point
*   **And** the property goes live once an Ops agent approves the finished listing, with no setup work by an agent before that
* * *
- [ ] _Mark as done, if the criteria are met_

2\. **No listing goes live and no payout goes out before its checks pass**
* * *
*   **Given** a self-onboarded property whose identity check, bank account check or go-live review has not passed
*   **When** a guest searches for it or a payout would fall due
*   **Then** the property is not bookable in the Guest app
*   **And** no payout goes out to the partner
* * *
- [ ] _Mark as done, if the criteria are met_

3\. **Every finished listing gets a decision the partner can act on**
* * *
*   **Given** a finished listing in the Go-live review queue
*   **When** an Ops agent reviews it in Back office
*   **Then** the listing is approved or sent back within the review window the Go-live review queue story sets
*   **And** a partner whose listing is sent back sees the reason for each stage that needs changes and can fix it in Partner Hub
* * *
- [ ] _Mark as done, if the criteria are met_

4\. **Properties outside self-onboarding stay on the assisted path**
* * *
*   **Given** a property with more than 40 rooms, a chain or a property that runs a channel manager
*   **When** its partner signs up
*   **Then** the property is onboarded through the assisted path with a partner manager
* * *
- [ ] _Mark as done, if the criteria are met_
* * *
##   

## Delivery
* * *
#### Estimation
* * *
The delivery budget or expected size for the approved scope, sized by each squad before planning closes.

*   Partner squad, the five Partner Hub stages and the partner side of sent-back listings: TBD...
*   Ops Tools squad, the Go-live review queue in Back office, including the capacity to hold 1 business day as volume grows: TBD...
*   Payments squad, payout details and the handover to the payment provider for payouts: TBD...

#### External dependencies
* * *
Constraints outside the team's control that gate delivery, with no date the team can set.

*   **National business registers** - each launch country's register has to answer the business registration number check, and sign-up verification stays blocked in a country until it does. Date: TBD...

#### Rabbit holes
* * *
Areas that could waste effort, create ambiguity or distract from the intended outcome.

*   TBD...

#### No-gos
* * *
Explicit scope exclusions and behaviors the delivery team must not introduce.

*   No self-onboarding for properties with more than 40 rooms or for chains, which stay on the assisted path with a partner manager
*   No channel manager connection in this release, so partners who run one stay on assisted onboarding until the Added Later capability ships
* * *
