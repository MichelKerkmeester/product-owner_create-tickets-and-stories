```markdown
# Epic - Partner Hub - Self-onboarding

* * *
## About
* * *
Partner Hub gets self-onboarding for independent properties, so a partner can set up a property and go live without an Ops agent doing the setup. The work splits into six child stories, one per stage, and all six ship in the first release.

#### Problem
* * *
Every new property is set up by hand. An Ops agent collects the details by email and builds the listing in Back office. Median sign-up to go-live takes 11 business days, and 640 properties are waiting in the queue today.

**The following issues rise from that:**
*   38% of partners who sign up never go live, 813 of 2,140 from January to June 2026
*   Partners wait for an agent's reply and list their rooms somewhere else
*   Each property takes an Ops agent about 4.5 hours of work
####   

#### Goal
* * *
Independent properties with up to 40 rooms set themselves up in Partner Hub and go live in a median of 3 business days, with no Ops agent doing the setup. Ops agents only check a finished listing before it goes live.

Target: 1,500 properties live through self-onboarding by 2027-06-30. For scale, Roamstay has 18,000 properties live today.
####   

#### Solution
* * *
A partner sets up the property in Partner Hub through six stages in order and can save and return at any point. Ops agents check the finished listing in the go-live review queue within 1 business day, approving it or sending it back with a reason per stage. No payout goes out before both the bank and identity checks pass.
* * *
##   

## Scope
* * *
Each child story owns one stage and carries its own requirements and acceptance criteria. Properties over 40 rooms and chains stay on the assisted path with a partner manager.

#### Setup stages in order
* * *
*   Partner - Onboarding - Sign-up and verification
*   Partner - Onboarding - Property profile and photos
*   Partner - Onboarding - Rooms and rates setup
*   Partner - Onboarding - Policies and city tax
*   Partner - Onboarding - Payout details and identity checks
*   Partner - Onboarding - Go-live review

#### Added later
* * *
**Channel manager connection**
*   Connects a partner's channel manager to partner-service through the partner API
* * *
##   

## Acceptance criteria
* * *
These are release-level outcomes.
Each child story carries the detailed criteria for its own screens and states.

1 ) **Independent property goes to review without Ops setup**
* * *
*   **Given** an independent property with up to 40 rooms
*   **When** the partner completes all six setup stages
*   **Then** the finished listing goes to the go-live review queue
*   **And** no Ops agent has set up the property
* * *
- [] _Mark as done, if the criteria are met_

2 ) **Review approves or returns the listing**
* * *
*   **Given** a finished listing in the go-live review queue
*   **When** an Ops agent checks it within 1 business day
*   **Then** the agent approves the listing or sends it back
*   **And** every listing sent back gives a reason per stage
* * *
- [] _Mark as done, if the criteria are met_

3 ) **City tax is checked on every listing**
* * *
*   **Given** any listing in the go-live review queue
*   **When** an Ops agent reviews it
*   **Then** the city tax rule is checked before the listing is approved
* * *
- [] _Mark as done, if the criteria are met_

4 ) **No payout before identity and bank checks pass**
* * *
*   **Given** a partner whose bank details or owner identity check has not passed
*   **When** a payout is due
*   **Then** no payout is sent
* * *
- [] _Mark as done, if the criteria are met_
* * *
##   
```

Export-equivalent path: `export/NNN - Epic-partner-hub-self-onboarding.md`

HVR self-scan: 1 hard blocker. Fixed: Added Later to Added later (title-case heading). Kept with reason: Epic - Partner Hub - Self-onboarding, the house H1 form that capitalises each title segment.

Quality status: checked against the Epic scaffold for house grammar, heading depth, dividers, spacers and the Mark-as-done line. No Delivery section, because none was requested.

The Epic uses Freya's goal and target word for word. Nothing else in it came from you, so please check these additions and strike any you don't want:
- The four release-level acceptance criteria are my derivation from the brief. The city tax and payout criteria follow the brief's risk notes.
- The Problem paragraph and its three bullets come from the brief's "Where we are" section.
- The Scope sentence on properties over 40 rooms and chains comes from the brief's out-of-scope list.
- The Added later bullet only states what the channel manager connection is.
- The child story titles, the group name "Setup stages in order" and the Epic title are my choices. Ownership sits in the brief, not in the Scope.
- The References section is omitted because you supplied no links.

Once you've reviewed it, the six child stories can be created as plain-text bullets and linked later. No ClickUp connector is available in this session, so there's no push to offer.