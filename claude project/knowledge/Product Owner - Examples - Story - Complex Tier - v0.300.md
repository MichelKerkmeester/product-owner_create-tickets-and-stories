# Product Owner - Examples - Story - Complex Tier - v0.300

Instantiates the house Story shape at Complex size: four payout types that inherit one shared release pipeline, with the shared mechanism described once in Solution, Requirements reduced to the limits and ordering the pipeline must honour, one priority marker, and outcome-led acceptance criteria grouped by surface, closing on a populated Delivery section because the request asked for a delivery view and sizing.

---

# Keystone - Payouts - Release pipeline

* * *
_A story is used to define product requirements, acceptance criteria, etc._
_Use it as the foundation for Tasks that work towards fulfilling the acceptance criteria._

## About
* * *
Keystone releases four kinds of payout to sellers: instant, standard, milestone and scheduled. Each type schedules and releases on its own today, with no shared cap, risk hold or fallback, so a seller can be paid several times within the hour, a large release can slip out without review, and a failed transfer can vanish with no record. This story routes all four types through one release pipeline that owns eligibility, risk holds, the daily cap and a shared fallback, so every payout keeps one consistent promise.

#### Problem
* * *
Every payout type runs on its own today:
*   A seller can receive an instant payout and a scheduled payout minutes apart on the same balance
*   A release above any sensible amount can settle before anyone reviews it
*   A failed transfer stops silently, with no queue and no record for support to act on
*   No type shares a limit, so a busy settlement day sends several transfers to one account within the hour

#### Solution
* * *
Route all four payout types through one shared release pipeline that owns eligibility, risk holds, the daily cap and the fallback to manual review. Each type supplies only its trigger, its amount source and its destination account. The pipeline decides whether, when and how a payout is released, so every type keeps one consistent promise.

For every candidate the pipeline runs the same ordered stages: an eligibility check on the seller's account, a risk hold on any large release, a cap check against the seller's rolling limit, then release or fallback. When candidates compete for the last release under the cap, the higher-priority type goes first and a deferred candidate keeps its own amount and destination for the next pass. Any release that fails at any stage lands in one shared manual review queue rather than dropping without a trace.

*   Each type supplies only its trigger, amount source and destination
*   The pipeline owns eligibility, risk holds, the daily cap and priority ordering
*   A blocked, deferred or failed release always lands in the manual review queue

**Expected outcomes**
* * *
*   A seller is never paid more times in a day than the shared cap allows
*   A large release is reviewed by a person before it can settle
*   A failed transfer is never lost, because it always surfaces in the manual review queue
*   Turning one payout type off leaves the other three releasing as before

#### **References**
* * *
Spec
*   [Keystone Payouts - Release Pipeline Spec](https://docs.keystone.example/payouts/release-pipeline)
* * *
##   

## Requirements
* * *
**Release limits** ← PRIO
* * *
- [] `daily_payout_cap = 3 releases per rolling 24h`, counted per seller across every payout type
- [] Any release where `amount >= 5000` goes on a risk hold instead of releasing automatically
- [] A release is evaluated against the cap and the risk threshold in that order, before any transfer is attempted

**Pipeline coverage**
* * *
- [] The pipeline handles instant, standard, milestone and scheduled payouts, and no other type
- [] Priority order when candidates compete for the last release under the cap is `instant > milestone > scheduled > standard`
- [] A scheduled payout runs on a fixed calendar, defaulting to weekly on Monday
- [] Every blocked, deferred or failed release is recorded in one shared manual review queue
* * *
##   

## Acceptance criteria
* * *
All acceptance criteria below must be met, or discuss and rescope any that cannot be met.

#### Release and cap
* * *
1\. **A payout reaches the seller quickly and inside the shared cap**
* * *
*   **Given** a seller with a payout ready to release and room left under `daily_payout_cap`
*   **When** the pipeline evaluates it
*   **Then** the money reaches the seller's destination account within minutes of becoming due
*   **And** that release counts against the cap for every other payout type, not only its own
* * *
- [] _Mark as done, if the criteria are met_

2\. **The cap defers a payout without losing it**
* * *
*   **Given** the seller's cap is used up and payouts of several types are waiting
*   **When** the pipeline runs its next pass
*   **Then** the highest-priority payout releases first
*   **And** every deferred payout waits for a later pass with its amount and destination intact, rather than being cancelled or converted to another type
* * *
- [] _Mark as done, if the criteria are met_

3\. **No payout releases before its money has cleared**
* * *
*   **Given** a milestone marked complete whose funds have not yet cleared
*   **When** the pipeline evaluates the payout
*   **Then** nothing is released while the money is not there
*   **And** it releases on the first pass after the funds clear, still subject to the shared cap
* * *
- [] _Mark as done, if the criteria are met_

#### Risk and fallback
* * *
4\. **Nothing large settles unreviewed and nothing failed disappears**
* * *
*   **Given** a payout too large to release automatically, or one whose transfer to the destination account fails
*   **When** the pipeline reaches its decision
*   **Then** the payout neither settles quietly nor drops without a trace
*   **And** it waits in the shared manual review queue with its original amount and destination, ready for a person to act on
* * *
- [] _Mark as done, if the criteria are met_

#### Type scope
* * *
5\. **Each payout type can be turned off on its own**
* * *
*   **Given** a seller has turned one payout type off
*   **When** that type's next trigger arrives
*   **Then** nothing releases for that type
*   **And** their remaining payout types keep releasing exactly as before
* * *
- [] _Mark as done, if the criteria are met_
* * *
##   

## Delivery
* * *
#### Estimation
* * *
The delivery budget or expected size for the approved scope.

*   Two sprints for one engineer: the shared pipeline and manual review queue in the first, the four type adapters in the second

#### Rabbit holes
* * *
Areas that could waste effort, create ambiguity or distract from the intended outcome.

*   Per-type overrides of the shared cap or risk threshold. Treat the shared limits as fixed and route exceptions into manual review rather than adding type-specific rules

#### No-gos
* * *
Explicit scope exclusions and behaviors the delivery team must not introduce.

*   No new payout type in this story, and the pipeline must not release any type Requirements does not list
* * *
