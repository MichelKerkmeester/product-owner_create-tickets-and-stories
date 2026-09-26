# Epic - Partner Hub - Self-onboarding

* * *
## About
* * *
Self-onboarding lets independent properties with up to 40 rooms set themselves up in Partner Hub and go live without an Ops agent doing the setup. Ops agents check the finished listing in Back office before it goes live.
This epic is split into six child stories, one for each onboarding stage. All six ship in the first release.

### Problem
* * *
Today an Ops agent sets up every new property by hand. A partner fills in a short sign-up form, then an Ops agent collects the rest by email: photos, room types, rates, policies, city tax, bank details and identity documents. The agent then builds the listing in Back office and makes it live. Most partners who drop off leave while they wait for an agent to reply, not while they fill anything in. On exit calls, partners say they signed up, heard nothing for days and listed their rooms somewhere else.

**The following issues rise from that:**
*   The median time from sign-up to go-live is 11 business days
*   38% of partners who sign up never go live: 813 of 2,140 sign-ups from January to June 2026
*   Each property takes an Ops agent about 4.5 hours of work, spread across the whole wait
*   640 properties are waiting in the queue today
###   

### Goal
* * *
Independent properties with up to 40 rooms set themselves up in Partner Hub and go live in a median of 3 business days, with no Ops agent doing the setup. Ops agents only check a finished listing before it goes live. The target is 1,500 properties live through self-onboarding by 2027-06-30. For scale, Roamstay has 18,000 properties live today.

**Direct partner/Roamstay benefits:**
*   Partners no longer wait for an agent's reply before they can go live, and that wait is where most of them drop off
*   Partners can save their progress at any stage and come back to it later
*   Ops agents check finished listings instead of building them
*   Every listing passes identity checks and a go-live review before guests can book it

**How we'll know it works:**
*   The median time from sign-up to go-live, and the time spent in each stage
*   Drop-off per stage, compared with today's 38%
*   The share of listings the Go-live review queue sends back, and the reasons
*   Guest complaints about wrong city tax or wrong photos on self-onboarded properties in their first 90 days live
###   

### Solution
* * *
In order to get there, we will:
*   Move property setup into Partner Hub as six stages, done in order, which the partner can save and come back to at any point
*   Check the partner's business registration, identity document and bank account before any payout is made
*   Check photo size and resolution when a photo is uploaded, so blurry or tiny photos never reach the listing
*   Send every finished listing to a Go-live review queue in Back office, where an Ops agent checks it within 1 business day, city tax included
*   Keep properties with more than 40 rooms, chains and properties that run a channel manager on assisted onboarding

## Scope
* * *
Each child story owns one onboarding stage and carries its own detailed requirements and acceptance criteria. The Partner squad owns the work in Partner Hub and `partner-service`. The Ops Tools squad builds the Go-live review queue in Back office. The Payments squad owns payout details and the handover to the payment provider for payouts.

#### Sign-up
* * *
*   Partner Hub - Self-onboarding - Sign-up and verification: email and phone confirmed, and the business registration number checked against the country's business register

#### Property setup
* * *
*   Partner Hub - Self-onboarding - Property profile and photos: address and map pin, description, facilities, and at least 8 photos of up to 20 MB each
*   Partner Hub - Self-onboarding - Rooms and rates setup: room types with their occupancy, a base price per night and at least one rate plan, either free cancellation or non-refundable
*   Partner Hub - Self-onboarding - Policies and city tax: check-in and check-out times, a cancellation policy for each rate plan, house rules and the city tax rule, charged per adult per night or per stay

#### Payouts
* * *
*   Partner Hub - Self-onboarding - Payout details and identity checks: the bank account and the owner's identity document, checked by the identity verification provider, with no payout until both checks pass

#### Go-live
* * *
*   Back office - Self-onboarding - Go-live review queue: an Ops agent checks the finished listing within 1 business day, then approves it or sends it back with a reason for each stage

#### Added Later
* * *
These capabilities belong to the epic but do not block the first release.

**Channel manager connection**
*   Connecting a channel manager is its own integration project. Until it ships, properties that run a channel manager stay on assisted onboarding
* * *
##   

## Acceptance criteria
* * *
These are release-level outcomes.
Each child story carries the detailed criteria for its own screens and states.

1\. **A partner goes live without an Ops agent doing the setup**
* * *
*   **Given** an independent property with up to 40 rooms that does not run a channel manager
*   **When** the partner completes all six stages in Partner Hub
*   **Then** the finished listing reaches the Go-live review queue without an Ops agent collecting any details by email
*   **And** once an Ops agent approves it, the property is bookable in the Guest app
* * *
- [ ] _Mark as done, if the criteria are met_

2\. **A partner can stop at any stage and pick up where they left off**
* * *
*   **Given** a partner partway through any of the six stages
*   **When** they leave Partner Hub and come back later
*   **Then** everything they saved is still there
*   **And** they continue from the stage where they stopped
* * *
- [ ] _Mark as done, if the criteria are met_

3\. **No property goes live and no payout is made before the checks pass**
* * *
*   **Given** a self-onboarded property whose bank account or owner's identity document has not passed its check
*   **When** a payout would otherwise be due
*   **Then** no payout is made until both checks pass
*   **And** the property goes live only after an Ops agent approves it in the Go-live review queue
* * *
- [ ] _Mark as done, if the criteria are met_

4\. **Every finished listing is reviewed within 1 business day**
* * *
*   **Given** a finished listing in the Go-live review queue
*   **When** an Ops agent checks it in Back office
*   **Then** the agent approves it or sends it back within 1 business day
*   **And** the city tax rule is checked on every listing, and a listing sent back carries a reason for each stage it returns
* * *
- [ ] _Mark as done, if the criteria are met_

5\. **Properties outside the scope stay on assisted onboarding**
* * *
*   **Given** a property with more than 40 rooms, a chain or a property that runs a channel manager
*   **When** it signs up
*   **Then** it goes through assisted onboarding instead of self-onboarding
*   **And** properties with more than 40 rooms and chains are assigned a partner manager
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
*   The Ops Tools squad sizes the Go-live review queue with the Partner squad so it stays within 1 business day as volume grows

#### Rabbit holes
* * *
Areas that could waste effort, create ambiguity or distract from the intended outcome.

*   The countries whose business registers the sign-up check uses are not named yet. Settle the list before the Sign-up and verification story is sized
*   Only an Owner can change payout details in Partner Hub. The Payout details and identity checks story settles whether an Owner has to complete that whole stage

#### No-gos
* * *
Explicit scope exclusions and behaviors the delivery team must not introduce.

*   No self-onboarding for properties with more than 40 rooms or for chains. They stay on the assisted path with a partner manager
*   No self-onboarding in the first release for properties that run a channel manager. Connecting a channel manager is listed under Added Later
* * *
