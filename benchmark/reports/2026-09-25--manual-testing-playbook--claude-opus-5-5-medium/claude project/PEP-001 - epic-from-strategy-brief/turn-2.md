```markdown
# Epic - Partner Hub - Self-onboarding

* * *
## About
* * *
Independent properties with up to 40 rooms set themselves up in Partner Hub, from sign-up to a finished listing. An Ops agent only checks that listing in Back office before it goes live. The work splits into six child stories, one per onboarding stage, and all six ship in the first release. The Partner squad owns the epic. The Ops Tools squad builds the Go-live review queue and the Payments squad owns payout details.

### Problem
* * *
Every new property on Roamstay is set up by hand. A partner fills in a short sign-up form. An Ops agent then collects photos, room types, rates, policies, city tax, bank details and identity documents by email, builds the listing in Back office and makes it live. Most partners who drop out leave while they wait for an agent to reply, not while they fill anything in. On exit calls they say they signed up, heard nothing for days and listed their rooms somewhere else.

**The following issues rise from that:**
*   The median time from sign-up to go-live is 11 business days
*   38% of partners who sign up never go live: 813 of 2,140 sign-ups from January to June 2026
*   Each property takes an Ops agent about 4.5 hours of work, spread across the whole wait
*   640 properties are waiting in the queue today
###   

### Goal
* * *
Independent properties with up to 40 rooms set themselves up in Partner Hub and go live in a median of 3 business days, with no Ops agent doing the setup. Ops agents only check a finished listing before it goes live.

The target is 1,500 properties live through self-onboarding by 2027-06-30. Roamstay has 18,000 properties live today.

**Direct partner/Roamstay benefits:**
*   Partners set up at their own pace and can save and come back at any point, instead of waiting days for an email reply
*   Ops agents check finished listings instead of spending about 4.5 hours building each one

**How we'll know it works:**
*   Median time from sign-up to go-live, and time spent in each stage
*   Drop-off per stage, against today's 38%
*   Share of listings sent back from the Go-live review queue, and the reasons
*   Guest complaints about wrong city tax or wrong photos on self-onboarded properties in their first 90 days live
###   

### Solution
* * *
In order to get there, we will:
*   Move partner setup into Partner Hub as six stages the partner completes in order, with save and come back at any point
*   Keep two checks before go-live: the identity verification provider checks the owner's identity document, and an Ops agent reviews the finished listing in Back office
*   Hold every payout until the bank account, the identity document and the go-live review have all passed
*   Check the city tax rule on every listing during the go-live review, because a wrong rule changes what a guest pays
*   Keep properties with more than 40 rooms, chains and partners who run a channel manager on the assisted path
*   Pilot the Go-live review queue with Bram, Ops Lead, and his agents

## Scope
* * *
Each child story owns one onboarding stage and carries its own detailed requirements and acceptance criteria. A partner moves through the stages in order, and all six ship in the first release.

#### Partner setup in Partner Hub
* * *
The Partner squad owns these stages. The Payments squad owns payout details and the handover to the payment provider for payouts.

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
Capabilities that belong to the epic but do not block the first release.

**Channel manager connection**
*   Partners who run a channel manager connect it during self-onboarding instead of staying on assisted onboarding. Connecting one is its own integration project
* * *
##   

## Acceptance criteria
* * *
These are release-level outcomes.
Each child story carries the detailed criteria for its own screens and states.

1\. **A partner takes an eligible property from sign-up to a finished listing on their own**
* * *
*   **Given** an independent property with up to 40 rooms that runs no channel manager
*   **When** the partner completes the six stages in Partner Hub in order
*   **Then** the finished listing reaches the Go-live review queue without an Ops agent setting up any part of it
*   **And** the partner can save and come back at any stage without losing what they entered
* * *
- [ ] _Mark as done, if the criteria are met_

2\. **No property goes live or gets a payout before its checks pass**
* * *
*   **Given** a self-onboarded listing
*   **When** its identity checks or its go-live review have not passed
*   **Then** the property is not bookable in the Guest app
*   **And** no payout goes to the partner
* * *
- [ ] _Mark as done, if the criteria are met_

3\. **Every finished listing gets a review decision within 1 business day**
* * *
*   **Given** a finished listing in the Go-live review queue
*   **When** an Ops agent reviews it in Back office
*   **Then** the agent approves it or sends it back with a reason per stage within 1 business day
*   **And** the review covers the city tax rule on every listing
*   **And** an approved property becomes bookable in the Guest app
* * *
- [ ] _Mark as done, if the criteria are met_

4\. **Properties outside the self-onboarding segment stay on the assisted path**
* * *
*   **Given** a property with more than 40 rooms, a chain property or a partner who runs a channel manager
*   **When** the partner signs up
*   **Then** the property stays on assisted onboarding
* * *
- [ ] _Mark as done, if the criteria are met_

5\. **The release shows how self-onboarding performs**
* * *
*   **Given** properties onboarded through self-onboarding
*   **When** the Partner squad reviews the release
*   **Then** the median time from sign-up to go-live, the time spent in each stage, the drop-off per stage and the share of listings sent back with their reasons are all available
*   **And** guest complaints about wrong city tax or wrong photos on these properties in their first 90 days live are counted
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

#### Rabbit holes
* * *
Areas that could waste effort, create ambiguity or distract from the intended outcome.

*   Go-live review queue capacity: the queue has to hold its 1 business day as volume grows, and the Ops Tools squad sizes it with the Partner squad

#### No-gos
* * *
Explicit scope exclusions and behaviors the delivery team must not introduce.

*   Self-onboarding for properties with more than 40 rooms or for chains, which stay on the assisted path with a partner manager
*   Self-onboarding in the first release for partners who run a channel manager. They stay on assisted onboarding until the channel manager connection under Added Later ships
* * *
```

Export-equivalent path: `export/002 - Epic-partner-hub-self-onboarding.md`

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: `TBD...` in Estimation, because it's the fixed Delivery placeholder.

**Quality:** The Epic has a Goal, six separate child stories and an Added Later group. Its acceptance criteria describe what the whole release delivers, not screen detail. It has no Requirements section. The 8-photo minimum, 20 MB limit and city tax rule types will go in the child stories.

**Summary:** I wrote the Epic with one child story per stage, all six in the first release. Freya's Goal and target are copied word for word, and connecting a channel manager is under Added Later.

**Things I added or decided that you didn't specify, so strike any you don't want:**
- **Title:** I used `Epic - Partner Hub - Self-onboarding`. The Go-live review story is titled `Back office - …` because that's where the screen lives.
- **Benefits label:** I changed "Direct user/Barter benefits" to "Direct partner/Roamstay benefits", since this product is Roamstay.
- **Delivery section:** I added it because Freya's brief asks for something the squads can size before planning closes. Estimation is left as TBD. The Rabbit hole is her queue-capacity risk, and the No-gos are her exclusions.
- **Criterion 4 (the eligibility check):** None of the six stages clearly owns deciding who stays on the assisted path. Sign-up and verification is the likely owner.
- **Criterion 5 (measurement):** No child story owns the tracking behind it. It's worth deciding whether that goes into each stage story or into a separate Data item.
- **Solution:** I included the Bram pilot from the brief.

**Next step:** Confirm or strike the points above. After that, the six child stories can be written from the Scope bullets.