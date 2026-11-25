---
title: "Product Owner - Examples - Task - Design Briefing Minimal"
description: "Instantiates Task Templates section 7, Design Briefing. Shows the core sections and one link block."
contextType: general
importance_tier: normal
trigger_phrases: ["design briefing minimal example"]
version: 0.17.0.1
---

# Briefing - Partner - Barter Deals - Required Target Audience

## About
* * *
Target gender defaults to all genders, so partners rarely change it. Since July, about 3,000 deals were set to All Genders, 510 to female and 67 to male, which means gender scoring has almost no effect.

The field gets no default and becomes required. All Genders stays valid when the partner picks it.

## Briefing
* * *
*   The field moves from a silent default to an active choice, so gender scoring starts to count
*   The options stay as they are, and only the default and the required state change

#### **Related tasks**
* * *
*   `Briefing - Partner & Creator - Barter Deals - Desired Collab Amount & Reach Pause`

## Requirements
* * *
**Display**
- [] No option is preselected on a new deal
- [] The field is marked as required

**Validation**
- [] Create and save are blocked, with an error on the field
- [] When the field is out of view, the error takes the partner to it
- [] The error clears once an option is picked

**Existing Deals**
- [] A deal the partner does not edit keeps its stored value
- [] When the partner edits a deal, the field resets to `Not selected`
- [] Validation blocks saving that deal until the partner picks an option again
