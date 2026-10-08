```markdown
# Epic - Partner Hub - Self-onboarding

* * *
## About
* * *
Partners set up their own property in Partner Hub, with no Ops agent doing the setup, and go live once an Ops agent has checked the finished listing. This Epic is split into six child stories, one per setup stage, and all six ship in the first release.

#### Problem
* * *
Every new property is set up by hand today. A partner fills in a short sign-up form, then an Ops agent collects photos, rates, policies, city tax, bank details and identity documents by email and builds the listing in Back office.

**The following issues rise from that:**
*   Median time from sign-up to go-live is 11 business days
*   38% of sign-ups never go live: 813 of 2,140 from January to June 2026
*   Most drop-off happens while the partner waits for an agent to reply, not while filling in the form
*   Each property takes an Ops agent about 4.5 hours of work, spread across the wait
*   640 properties are waiting in the queue today
####   

#### Goal
* * *
Independent properties with up to 40 rooms set themselves up in Partner Hub and go live in a median of 3 business days, with no Ops agent doing the setup. Ops agents only check a finished listing before it goes live.

Target: 1,500 properties live through self-onboarding by 2027-06-30. For scale, Roamstay has 18,000 properties live today.
####   

#### Solution
* * *
A partner moves through the six stages in order, and can save and come back at any point. Ops agents do not set up the property. They check the finished listing within 1 business day, then approve it or send it back with a reason per stage.

This release covers independent properties with up to 40 rooms and no channel manager. Chains and properties with more than 40 rooms stay on the assisted path with a partner manager.

## Scope
* * *
Each child story owns one part of the setup and carries its own detailed requirements and acceptance criteria.

#### Partner setup
* * *
*   Partner Hub - Self-onboarding - Sign-up and verification: email, phone and business registration number
*   Partner Hub - Self-onboarding - Property profile and photos: address, description, facilities and photos
*   Partner Hub - Self-onboarding - Rooms and rates setup: room types, rates and rate plans
*   Partner Hub - Self-onboarding - Policies and city tax: check-in and check-out, cancellation, house rules and city tax
*   Partner Hub - Self-onboarding - Payout details and identity checks: bank account and owner identity document

#### Go-live review
* * *
*   Back office - Self-onboarding - Go-live review queue: an Ops agent checks each finished listing within 1 business day

#### Added later
* * *
These capabilities belong to the epic but do not block the first release.

**Channel manager connection**
*   Partners who run a channel manager stay on assisted onboarding until its connection is built, as its own integration project
* * *
##   

## Acceptance criteria
* * *
These are release-level outcomes.
Each child story carries the detailed criteria for its own screens and states.

1\. **An independent property goes live without an Ops agent doing its setup**
* * *
*   **Given** an independent property with up to 40 rooms and no channel manager
*   **When** the partner completes all six stages in Partner Hub
*   **Then** the finished listing waits in the Go-live review queue
*   **And** an Ops agent only checks the listing before it goes live
* * *
- [] _Mark as done, if the criteria are met_

2\. **No payout is made before the owner's identity and bank details both pass**
* * *
*   **Given** a partner whose identity check or bank account check has not passed
*   **When** a payout falls due
*   **Then** no payout is made to the partner
*   **And** the payout waits until both checks pass
* * *
- [] _Mark as done, if the criteria are met_

3\. **Every listing is checked for city tax before it goes live**
* * *
*   **Given** a finished listing in the Go-live review queue
*   **When** an Ops agent reviews it
*   **Then** the city tax rule is checked
*   **And** the listing is approved, or sent back with a reason per stage that needs a fix
* * *
- [] _Mark as done, if the criteria are met_

4\. **A partner can save and come back at any point in the six stages**
* * *
*   **Given** a partner partway through the six stages
*   **When** the partner leaves Partner Hub and comes back later
*   **Then** the details saved so far are still there
* * *
- [] _Mark as done, if the criteria are met_
* * *
##   
```

Export-equivalent path: `export/NNN - Epic-Partner-Hub-self-onboarding.md`

Artifact kind: Epic. The Goal and target are Freya's wording, quoted as she wrote them. The Epic has six child stories in Scope, with channel manager connection under Added later, and no Requirements or Delivery section.

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: the Goal and target paragraphs, which are preserved source text from Freya's brief.

Please check these additions, which I wrote from the brief and you did not specify. Strike any you don't want:

- The four acceptance criteria are my wording, built from the brief's stage rules.
- The title is proposed, not confirmed. The Partner Hub surface is in the title and the Partner squad is not named as owner.
- Stage 5 covers the partner's payout details only. I did not add a child story for the Payments handover to the payment provider.
- Scope uses short descriptors per stage. Full stage values belong in the child stories.
- "Added later" uses sentence case. You wrote "Added Later".
- The Goal has no benefits list, since you asked for Freya's goal and target as written.
- There is no References section, because no links were supplied.
- There is no Delivery section, so the sizing request and Freya's four risks are not in the body. I can add an Estimation section if the squads need one.