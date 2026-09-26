# Epic - Partner Hub - Self-onboarding

* * *
## About
* * *
Independent properties with up to 40 rooms set up in Partner Hub, and an Ops agent only checks the listing in Back office. Six child stories, one per stage, all ship in the first release.

The Partner squad owns the epic, Ops Tools the Go-live review queue and Payments payout details.

#### Problem
* * *
After a short sign-up form, an Ops agent emails for photos, room types, rates, policies, city tax, bank details and identity documents, then builds each Roamstay listing in Back office by hand.

Most dropouts leave after days waiting for a reply, and list elsewhere.

**The following issues rise from that:**
*   Median sign-up to go-live: 11 business days
*   38% never go live: 813 of 2,140 sign-ups, January to June 2026
*   About 4.5 Ops agent hours per property, spread across the wait
*   640 properties waiting in the queue today
####   

#### Goal
* * *
Eligible properties go live in a median of 3 business days with no Ops setup. The target is 1,500 self-onboarded properties live by 2027-06-30, against 18,000 Roamstay properties live today.

**Direct partner/Roamstay benefits:**
*   Partners set up at their own pace, not waiting days for email
*   Ops agents check listings instead of building them

**How we'll know it works:**
*   Median time to go-live, and per stage
*   Drop-off per stage, against today's 38%
*   Share sent back from review, with reasons
*   Guest complaints about wrong city tax or wrong photos on self-onboarded properties in their first 90 days live
####   

#### Solution
* * *
In order to get there, we will:
*   Move setup into Partner Hub as six ordered stages, with save and come back anytime
*   Two checks before go-live: the identity verification provider on the owner's identity document, and an Ops agent on the listing
*   Hold payouts until bank account, identity document and go-live review all pass
*   Check every listing's city tax rule in review, because a wrong rule changes what a guest pays
*   Pilot the Go-live review queue with Bram, Ops Lead, and his agents

## Scope
* * *
Each child story owns one stage, with its own requirements and criteria.

#### Partner setup in Partner Hub
* * *
The Partner squad owns these, and Payments owns payout details and their handover to the payment provider.

*   Partner Hub - Self-onboarding - Sign-up and verification
*   Partner Hub - Self-onboarding - Property profile and photos
*   Partner Hub - Self-onboarding - Rooms and rates setup
*   Partner Hub - Self-onboarding - Policies and city tax
*   Partner Hub - Self-onboarding - Payout details and identity checks

#### Go-live review in Back office
* * *
The Ops Tools squad builds this stage.

*   Back office - Self-onboarding - Go-live review queue

#### Added Later
* * *
These do not block the first release.

**Channel manager connection**
*   Channel manager partners connect it during self-onboarding, as its own integration project
* * *
##   

## Acceptance criteria
* * *
Release-level outcomes, with detailed criteria in each child story.

1\. **A partner takes an eligible property from sign-up to a finished listing on their own**
* * *
*   **Given** an independent property with up to 40 rooms and no channel manager
*   **When** the partner completes the six Partner Hub stages in order
*   **Then** the listing reaches the Go-live review queue with no Ops setup
*   **And** the partner can save and resume at any stage without losing input
* * *
- [] _Mark as done, if the criteria are met_

2\. **No property goes live or gets a payout before its checks pass**
* * *
*   **Given** a self-onboarded listing
*   **When** its identity checks or go-live review have not passed
*   **Then** it is not bookable in the Guest app
*   **And** no payout goes out
* * *
- [] _Mark as done, if the criteria are met_

3\. **Every finished listing gets a review decision within 1 business day**
* * *
*   **Given** a listing in the Go-live review queue
*   **When** an Ops agent reviews it in Back office
*   **Then** the agent approves it or returns it with a reason per stage within 1 business day
*   **And** the review covers the city tax rule
*   **And** an approved property becomes bookable in the Guest app
* * *
- [] _Mark as done, if the criteria are met_

4\. **Properties outside the self-onboarding segment stay on the assisted path**
* * *
*   **Given** a property over 40 rooms, a chain property or a channel manager partner
*   **When** the partner signs up
*   **Then** it stays on assisted onboarding
* * *
- [] _Mark as done, if the criteria are met_

5\. **The release shows how self-onboarding performs**
* * *
*   **Given** self-onboarded properties
*   **When** the Partner squad reviews the release
*   **Then** median time to go-live, time and drop-off per stage and the sent-back share with reasons are available
*   **And** guest complaints about wrong city tax or photos in their first 90 days live are counted
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

*   Go-live review queue capacity: it must hold 1 business day as volume grows, and Ops Tools sizes it with the Partner squad

#### No-gos
* * *
Explicit scope exclusions and behaviors the delivery team must not introduce.

*   Self-onboarding for chains or properties over 40 rooms, which stay assisted with a partner manager
*   First-release self-onboarding for channel manager partners, until the Added Later connection ships
* * *
