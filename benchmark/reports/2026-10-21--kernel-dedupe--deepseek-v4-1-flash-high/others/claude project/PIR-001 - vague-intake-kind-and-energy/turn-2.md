```
# Epic - Guest - Loyalty points

* * *
## About
* * *
Loyalty points give a guest a reason to book the next stay on Roamstay. A guest joins from Account, earns points when a stay completes and spends them at checkout on a Pay now booking. The balance and its history sit under Account.
This Epic is split into several child stories, each owning one part of that lifecycle and carrying its own detailed requirements and acceptance criteria.

#### Problem
* * *
Today 19% of guests book a second stay within 12 months, against a target of 25% by the end of 2027. Roamstay has no loyalty scheme and no member-only prices, so a guest who has stayed is treated like one who never booked. Nothing records what those stays earned, so the second stay is worth no more than the first.

**The following issues rise from that:**
*   A guest who has completed a stay has nothing waiting for them on return
*   The Account area keeps no running record of what those stays earned
*   A second booking is treated like a first one
*   A guest who books with an email address only has no account to hold a balance
####   

#### Goal
* * *
Raise repeat bookings from 19% of guests within 12 months to 25% by the end of 2027, so a returning guest has something of their own to come back to.

**Direct user/Roamstay benefits:**
*   A guest sees a balance grow with every completed stay
*   A returning guest can pay less at checkout without a code to remember
*   Roamstay wins the second stay on more than price
*   The repeat rate becomes something the team can move and measure
####   

#### Solution
* * *
In order to get there, we will:
*   Let a signed-in guest join the programme from Account, so earning has somewhere to land
*   Award points when a stay completes, so the balance follows stays the guest actually took
*   Show the balance and its history under Account, so a guest can see what they hold
*   Let a guest apply points at checkout on a Pay now booking, where Roamstay takes the payment and can take less

The value of a point and who carries its cost are not decided. This Epic sets no number for either, so the story that spends points waits on that decision.

## Scope
* * *
Each child story owns one part of the loyalty lifecycle and carries its own detailed requirements and acceptance criteria. Every story lands in the Guest app on iOS, Android and web.

#### Join
* * *
*   Guest - Account - Join the loyalty programme

#### Earn
* * *
*   Guest - Loyalty points - Earn points on completed stays

#### Balance
* * *
*   Guest - Account - Points balance and history

#### Spend
* * *
*   Guest - Checkout - Spend points on Pay now

* * *
##   

## Acceptance criteria
* * *
These are release-level outcomes.
Each child story carries the detailed criteria for its own screens and states.

1 ) **A guest joins and earns from a completed stay**
* * *
*   **Given** a signed-in guest who has joined the programme
*   **When** they complete a stay
*   **Then** its points appear in their balance
*   **And** a stay that is not completed earns nothing
* * *
- [] _Mark as done, if the criteria are met_

2 ) **The guest sees what they hold and where it came from**
* * *
*   **Given** a guest who has earned or spent points
*   **When** they open Account
*   **Then** their current balance shows
*   **And** the history lists each entry with the stay or booking behind it
* * *
- [] _Mark as done, if the criteria are met_

3 ) **Points lower what a Pay now booking costs**
* * *
*   **Given** a guest with a points balance at checkout
*   **When** they choose Pay now and apply points
*   **Then** the amount they pay falls by the points they applied
*   **And** their balance falls by the same points
* * *
- [] _Mark as done, if the criteria are met_

4 ) **A Pay at property booking leaves the balance untouched**
* * *
*   **Given** a guest with a points balance at checkout
*   **When** they choose Pay at property
*   **Then** no points are offered or applied to that booking
*   **And** the guest's balance is unchanged
* * *
- [] _Mark as done, if the criteria are met_
* * *
##   
```

Export-equivalent path: `export/NNN - Epic-loyalty-points.md`
HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.
Quality: every floor met | Kind: Epic | Energy: Deep

The Epic frames points as the route to 25% repeat bookings by the end of 2027, from 19% today. It carries a Goal, four child stories named as plain text across Join, Earn, Balance and Spend, and four release-level criteria. It has no Requirements section and no Delivery close, since you asked for neither and nothing forced them.

### Open items
1. **Point value**
   - **Situation:** You said the point value is undecided, so the Epic states none and no criterion names one
   - **Open:** Settle it before the spend story is picked up, since checkout cannot apply a point with no value
2. **Cost of a point**
   - **Situation:** The Epic records that who carries the cost is undecided, without naming a party
   - **Open:** Confirm that stays open rather than being settled by this Epic
3. **Email-only guests**
   - **Situation:** I read earning as signed-in only, because an email-only booking has no account to hold a balance
   - **Open:** Confirm those guests are outside the first release or strike the signed-in wording
4. **What a history entry shows**
   - **Situation:** I added that each history entry names the stay or booking behind it, which you did not supply
   - **Open:** Strike it if the history needs only the points and a date
5. **When the balance falls at checkout**
   - **Situation:** The criterion has the balance fall by the points applied, and a Pay now booking waits in `payment_pending` for up to 30 minutes before it confirms
   - **Open:** Confirm whether the balance falls at application or at confirmation
6. **Stays that do not complete**
   - **Situation:** I added that a stay which is not completed earns nothing, as the other side of earning on completed stays
   - **Open:** Confirm a cancelled or non-refundable stay earns nothing

Want me to change anything?