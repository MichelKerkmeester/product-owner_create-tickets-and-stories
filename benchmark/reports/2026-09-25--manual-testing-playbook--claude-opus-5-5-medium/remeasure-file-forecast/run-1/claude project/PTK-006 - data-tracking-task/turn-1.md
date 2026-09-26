```markdown
# Booking funnel events task: questions before drafting

Nadia's tracking plan gives me the triggers, properties and reasons. Five decisions still change what the task says, so I need them before drafting.

**1. Scope and title**

The plan gives this work to three owners, and a task title carries one discipline code. Which one should this task cover?

- Client events on iOS, Android and web together (`search_submitted`, `property_viewed`, `room_selected`, `checkout_started`, `payment_submitted`), titled `FE - Guest app - TRK - Booking funnel client events`
- `booking_confirmed` in `booking-service`, owned by the Booking squad, titled `BE - Guest app - TRK - booking_confirmed server event`
- A parent task with one subtask per owner. If you want this, should the Data team's dashboard move from `checkout_complete` to `booking_confirmed` be one of the subtasks, or stay out of scope?

**2. Plan status**

The plan is draft v0.3, and comments closed at the Booking squad refinement on 2026-09-24. Did v0.3 come out of that refinement unchanged, or did anything change that I should include?

**3. `date_changed`**

This event is still proposed. Its properties aren't agreed, and nobody has decided whether it fires once per tap in the date picker or once when the guest applies the new range. Should I leave it out, or include it with a decision you give me?

**4. `room_selected` timing**

Nadia agreed that Android can send `room_selected` after the price call returns, so the event carries `total_amount_minor`. Does that apply to all three platforms, or only to Android while iOS and web send it on the tap?

**5. `checkout_complete` and links**

- `events-collector` stops accepting `checkout_complete` on 2026-11-01, and that change belongs to the Data team. Should the client task include a check that the apps keep sending `checkout_complete` unchanged until that date?
- Do you have links to the tracking plan, related tickets or an epic? If not, I'll name the tracking plan in plain text and won't make up URLs
```

Export-equivalent path: `export/001 - task-booking-funnel-events-clarification.md`

HVR self-scan: 0 hard blockers. Fixed: none. Kept with reason: none.

Your request clearly asks for a task, but I have questions before I can write it:

- **Scope:** The plan splits the build across three owners. Your title convention needs one discipline code per task, so the scope choice changes the title, the owner and most of the checklist.
- **Draft status:** The plan is still marked draft v0.3, and the refinement where comments closed happened two days ago.
- **Open decisions:** `date_changed` hasn't been agreed yet, and it's unclear whether the `room_selected` timing change covers every platform or just Android.

I'll write the task once you answer.