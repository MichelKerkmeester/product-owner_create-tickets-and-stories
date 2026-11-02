# Story - Fv2.5 - Feed Function - Rulesets

## Overview
* * *
**User Story**
As a creator, I want each feed collection to deliver on what its name promises:
*   New Deals should show new deals
*   Trending should show what's trending
*   For You should show deals I care about

**Problem**
Weighted scoring alone cannot guarantee a function's core promise:
*   New Deals surfaces deals that are weeks old
*   Trending surfaces deals with no traction.
*   The scoring ranks well, but it can't stop the wrong deals from entering the pool.

**Solution**
Rulesets that runs before scoring, keeping ineligible deals out.

**Documentation**
[https://app.clickup.com/90151466006/docs/2kyq4d0p-20955/2kyq4d0p-84955](https://app.clickup.com/90151466006/docs/2kyq4d0p-20955/2kyq4d0p-84955)
##   

## How rulesets work
* * *
Rulesets are hard filters applied before weighted scoring.
These help ensure a function shows deals that match its promise.

A hard filter is applied to the candidate pool before weighted scoring runs, keeping ineligible deals out. The ruleset filter decides what stays, the weighted ranking algorithms decide what order it comes in. This preserves the benefits of weighted ranking while preventing the failures that break a collection's promise.

Each ruleset has a degradation sequence, so a filter can widen gracefully instead of leaving a collection empty.

#### **Sequence**
* * *
A ruleset runs in three ordered steps:
1. **Primary** filters the pool first, then the weights rank whatever survives
2. **Relaxed** widens the rule and the weights rank again
3. **Final fallback** drops the rule entirely and sorts by the function's plain production sort instead

A plain production sort is a single-column database order, like `created_at DESC`.
No signals, no weights, no scoring, just one field deciding the order.

Step 3 matters because the weighted score can't be trusted once the rule is dropped. The signal the ruleset exists to protect is still 0 across an unfiltered pool, so ranking by the same weights would just reproduce the failure the ruleset was built to prevent.

#### **Degradation**
* * *
A function using all three tiers never ends up empty.
This mirrors the guaranteed fallback in [Patterns](https://app.clickup.com/90151466006/v/dc/2kyq4d0p-20955/2kyq4d0p-78075) (Collection rotation, Step 4).

Not every function uses all three tiers:
*   Skipping Relaxed means nothing loosens if Primary comes up short
*   Skipping Final fallback means nothing replaces the rule if every tier tried still comes up short

There's no guaranteed full list in this case, the function shows fewer deals instead.
Once the creator hits the bottom of the list, an expansion state will appear as defined in Patterns.
* * *
##   

## Definition of Ready
* * *
Check off as met; pull rulesets into a sprint only when every box is checked:
*   [x] Every ruleset's Story line is written in the Connextra form with a clear value clause
*   [x] Acceptance criteria present and testable for every ruleset
*   [x] Dependencies identified (weighted scoring live per function, Patterns expansion state available)
*   [ ] Sized by the team and each ruleset fits comfortably in a sprint
##   

## Requirements
* * *
1\. **New Deals** ← PRIO
**`(`**`new_deals_feed_url)`
* * *
**Task(s):** [019 - Implement ruleset: New Deals](019 - subtask-feed-ruleset-new.md)
* * *
**Story:** As a creator opening "New Deals", I want every deal in the collection to be recently created, so that new actually means new.

A creator opening "New Deals" expects to see recent deals.
Anything that's not recent, breaks that promise.
This ruleset stops deals older than 21 days from still scoring as new.

**Sequence**
* * *
**Primary:** `created_at ≤ 7d`
The deal was created 7 days ago or less.
* * *
**Relaxed:** `created_at ≤ 14d`, then `≤ 21d`
Widen to 14 days, then 21 days if still short.
* * *
**Final fallback:** `no_fallback`
Deals older than 21 days are excluded, not shown with no filter.
* * *

The ruleset applies a **freshness window** in **two** widening **tiers**:
1. Deals created within the last 7 days
2. Widens to 14, then 21 days if there aren't enough to fill the collection

Which means that:
*   A deal older than 21 days never appears
*   The rule never relaxes past 21 days, and there is no fallback
*   The function shows fewer deals rather than breaking its freshness promise

**Acceptance criteria**

**Scenario:** Primary window fills the collection
*   **Given** enough deals exist with `created_at ≤ 7d`
*   **When** a creator opens "New Deals"
*   **Then** only deals created 7 days ago or less enter the scoring pool

**Scenario:** Supply runs short and the window widens
*   **Given** too few deals exist within 7 days
*   **When** the ruleset degrades
*   **Then** the window widens to 14, then 21 days
*   **And** weighted scoring re-ranks after each widening

**Scenario:** The freshness promise holds at the limit
*   **Given** too few deals exist even at 21 days
*   **When** every tier has been tried
*   **Then** deals older than 21 days stay excluded and the collection shows fewer deals instead
* * *

2\. **Trending**
`(top10_deals_feed_url)`
* * *
**Task(s):** [020 - Implement ruleset: Trending](020 - subtask-feed-ruleset-trending.md)
* * *
**Story:** As a creator opening "Trending", I want every deal to show real marketplace traction, so that the hot list reflects actual activity.

A creator opening "Trending" expects to see deals with real marketplace traction.
Anything that doesn't have traction, breaks that promise.
This ruleset keeps deals with zero traction off the "what's hot" list.

**Sequence**
* * *
**Primary:** `≥ 10 application in last 14d`
At least 10 applications in the past 14 days.
* * *
**Relaxed:** `≥ 10 application in last 30d`
Widen the window to 30 days.
* * *
**Final fallback:** `completed_applications_count + upcoming_applications_count DESC`
No filter, sort by total completed plus upcoming applications.
* * *

The ruleset applies a **traction bar** in **two** widening **tiers**:
1. At least 10 applications in the last 14 days
2. Widens to 10 applications in the last 30 days if there aren't enough

Which means that:
*   A deal with no real traction never appears while the filter holds
*   If both tiers come up short, the final fallback drops the filter and sorts by `complated_applications_count + upcoming_applications_count DESC`, the existing production sort

Note: the source spells the fallback field both `completed_applications_count` (Sequence block) and `complated_applications_count` (a known legacy spelling in the codebase). Both are preserved verbatim; confirm the live column name before wiring the sort.

**Acceptance criteria**

**Scenario:** The traction bar holds
*   **Given** enough deals have at least 10 applications in the last 14 days
*   **When** a creator opens "Trending"
*   **Then** only deals clearing the traction bar enter the scoring pool

**Scenario:** The window widens
*   **Given** too few deals clear the 14-day bar
*   **When** the ruleset degrades
*   **Then** the bar widens to at least 10 applications in the last 30 days

**Scenario:** Final fallback uses the production sort
*   **Given** both windows come up short
*   **When** the final fallback runs
*   **Then** the filter drops and deals sort by `complated_applications_count + upcoming_applications_count DESC`, the existing production sort
* * *

3. **New Brands**
`(new_partners_feed_url)`
* * *
**Task(s):** [021 - Implement ruleset: New Brands](021 - subtask-feed-ruleset-new-brands.md)
* * *
**Story:** As a creator opening "New Brands", I want to see partners who recently joined Barter, so that I discover genuinely new partners instead of recycled visibility.

A creator opening "New Brands" expects to discover partners who recently joined Barter, not established partners recycling visibility.
This ruleset stops partners past their first 60 days from posing as newly joined.

**Sequence**
* * *
**Primary:** `partner_created_at ≤ 60d`
The partner joined 60 days ago or less.
* * *
**Relaxed:** `partner_created_at ≤ 120d`
Widen to 120 days.
* * *
**Final fallback:** `partner_id DESC`
No filter, sort by partner ID.
* * *

The ruleset applies a **partner-freshness window** in **two** widening **tiers**:
1. Partners who joined within the last 60 days
2. Widens to 120 days if there aren't enough to fill the collection

Which means that:
*   A partner past their first 120 days never appears while the filter holds
*   If both tiers come up short, the final fallback drops the filter and sorts by `partner_id DESC`, the existing production sort

**Acceptance criteria**

**Scenario:** The partner-freshness window holds
*   **Given** enough deals come from partners with `partner_created_at ≤ 60d`
*   **When** a creator opens "New Brands"
*   **Then** only those partners' deals enter the scoring pool

**Scenario:** The window widens
*   **Given** too few deals from partners within 60 days
*   **When** the ruleset degrades
*   **Then** the window widens to `partner_created_at ≤ 120d`

**Scenario:** Final fallback uses the production sort
*   **Given** both windows come up short
*   **When** the final fallback runs
*   **Then** the filter drops and deals sort by `partner_id DESC`, the existing production sort
* * *

4\. **Hidden Gems**
`(hidden_gem_feed_url)`
* * *
**Task(s):** [022 - Implement ruleset: Hidden Gems](022 - subtask-feed-ruleset-hidden-gems.md)
* * *
**Story:** As a creator opening "Hidden Gems", I want overlooked deals with little recent traction, so that I find opportunities others missed.

A creator opening "Hidden Gems" expects to discover overlooked deals.
This ruleset stops an unpopular deal from staying buried forever.

**Sequence**
* * *
**Primary:** `< 5 applications in last 14d`
Fewer than 5 applications in the past 14 days.
* * *
**Relaxed:** `< 10 applications in last 14d`
Widen the cap to under 10.
* * *
**Final fallback:** `last14_days_pending_applications_count + last14_days_completed_applications_count +`
`last14_days_upcoming_applications_count ASC`
No filter, sort by fewest recent applications first.
* * *

The ruleset applies a **low-application cap** in **two** widening **tiers**:
1. Fewer than 5 applications in the last 14 days
2. Widens to fewer than 10 if there aren't enough to fill the collection

Which means that:
*   A deal with high recent traction never appears while the filter holds
*   If both tiers come up short, the filter drops and deals sort by fewest recent applications first
*   The fallback sort is `last14_days_pending_applications_count + last14_days_completed_applications_count + last14_days_upcoming_applications_count ASC`, the existing production sort

**Acceptance criteria**

**Scenario:** The low-application cap holds
*   **Given** enough deals have fewer than 5 applications in the last 14 days
*   **When** a creator opens "Hidden Gems"
*   **Then** only deals under the cap enter the scoring pool
*   **And** a deal with high recent traction never appears

**Scenario:** The cap widens
*   **Given** too few deals under the 5-application cap
*   **When** the ruleset degrades
*   **Then** the cap widens to fewer than 10 applications in the last 14 days

**Scenario:** Final fallback surfaces the least-applied deals
*   **Given** both caps come up short
*   **When** the final fallback runs
*   **Then** the filter drops and deals sort by fewest recent applications first, the existing production sort
* * *

5\. **For You**
`(deals_for_me_feed_url)`
* * *
**Task(s):** [023 - Implement ruleset: For You](023 - subtask-feed-ruleset-for-you.md)
* * *
**Story:** As a creator opening "For You", I want deals that match my interests and my follower count, so that everything shown is within reach and worth my time.

A creator opening "For You" expects to see deals they can get and care about.
This ruleset keeps out deals the creator can't realistically get or isn't interested in.

**Sequence**
* * *
**Primary:** `hard interest + min-follower filter`
The deal must match one of the creator's interests, and must clear the minimum follower count
* * *
**Relaxed:** `no_relaxation`
This rule never loosens
* * *
**Final fallback:** `no_fallback`
If a deal fails the rule, it never shows
* * *

The ruleset applies **two hard filters** as an **AND** condition:
1. The deal must match at least one of the creator's interests
2. The creator's follower count must meet the deal's minimum

Which means that:
*   A deal with no interest overlap never appears
*   The rule never loosens, and there is no fallback
*   The function shows fewer deals rather than degrading relevance

**Acceptance criteria**

**Scenario:** Both hard filters pass
*   **Given** a deal matches at least one of the creator's interests
*   **And** the creator's follower count meets the deal's minimum
*   **When** a creator opens "For You"
*   **Then** the deal is eligible for the scoring pool

**Scenario:** Either filter fails
*   **Given** a deal fails the interest match or the follower minimum
*   **When** a creator opens "For You"
*   **Then** the deal never appears, with no relaxation and no fallback

**Scenario:** A short pool never degrades relevance
*   **Given** too few deals pass both filters
*   **When** the collection renders
*   **Then** it shows fewer deals and the Patterns expansion state appears at the bottom
* * *

6\. **Fit Check**
`(deals_for_my_follower_count_feed_url)`
* * *
**Task(s):** [024 - Implement ruleset: Fit Check](024 - subtask-feed-ruleset-fit-check.md)
* * *
**Story:** As a creator opening "Fit Check", I want only deals my follower count qualifies for, so that I never open a deal I cannot apply to.

A creator opening "Fit Check" expects to see deals their follower count can reach.
This ruleset keeps out deals the creator's follower count can't apply to.

**Sequence**
* * *
**Primary:** `deal_min_followers ≤ creator_followers`
The creator's follower count must meet or exceed the deal's minimum.
* * *
**Relaxed:** `no_relaxation`
This rule never loosens.
* * *
**Final fallback:** `no_fallback`
If a deal fails the rule, it never shows.
* * *

The ruleset applies **one hard filter**:
*   `deal_min_followers ≤ creator_followers`

Which means that:
*   A deal that asks for more followers than the creator has never appears
*   The rule never loosens, and there is no fallback
*   The function shows fewer deals rather than degrading relevance

**Acceptance criteria**

**Scenario:** The follower minimum is met
*   **Given** a deal where `deal_min_followers ≤ creator_followers`
*   **When** a creator opens "Fit Check"
*   **Then** the deal is eligible for the scoring pool

**Scenario:** The follower minimum is not met
*   **Given** a deal that asks for more followers than the creator has
*   **When** a creator opens "Fit Check"
*   **Then** the deal never appears, with no relaxation and no fallback

**Scenario:** A short pool never degrades relevance
*   **Given** too few deals pass the filter
*   **When** the collection renders
*   **Then** it shows fewer deals instead of loosening the rule
* * *

7\. **Your Vibe**
`(picked_for_you_feed_url)`
* * *
**Task(s):** [025 - Implement ruleset: Your Vibe](025 - subtask-feed-ruleset-your-vibe.md)
* * *
**Story:** As a creator opening "Your Vibe", I want every deal to match at least one of my interests, so that the feed keeps feeling personally picked.

A creator opening "Your Vibe" expects deals that match their interests.
This ruleset keeps the feed feeling personally picked, not random.

**Sequence**
* * *
**Primary:** `≥ 1 matching interest`
The deal must match at least one of the creator's interests.
* * *
**Relaxed:** `no_relaxation`
This rule never loosens.
* * *
**Final fallback:** `no_fallback`
If a deal fails the rule, it never shows.
* * *

The ruleset applies **one hard filter**:
*   The deal must match at least one of the creator's interests

Which means that:
*   A deal with no interest overlap never appears
*   The rule never loosens, and there is no fallback
*   The function shows fewer deals rather than degrading relevance

**Acceptance criteria**

**Scenario:** The interest match holds
*   **Given** a deal matches at least one of the creator's interests
*   **When** a creator opens "Your Vibe"
*   **Then** the deal is eligible for the scoring pool

**Scenario:** No interest overlap
*   **Given** a deal matches none of the creator's interests
*   **When** a creator opens "Your Vibe"
*   **Then** the deal never appears, with no relaxation and no fallback

**Scenario:** A short pool never degrades relevance
*   **Given** too few deals match
*   **When** the collection renders
*   **Then** it shows fewer deals instead of loosening the rule
* * *
##   

## Definition of Done
* * *
Applies to every ruleset above before its task closes:
*   [ ] The function's acceptance criteria verified against the live candidate pool
*   [ ] Unit tests cover each degradation tier and each never-appears guarantee
*   [ ] Feed response times stay within tolerance with the filter running before scoring
*   [ ] Verified on staging with production-shaped data
