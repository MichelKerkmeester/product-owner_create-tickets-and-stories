# FE - Web - TODO - Due today filter chip

## About

---

The To-dos view on Web gets a Due today chip directly after Overdue. The chip shows the to-dos a member has not checked off whose due date is today in the to-do owner's time zone. It reuses the existing chip component and follows the same single active chip behavior and due date sort as the other chips.

A member can see today's open to-dos with one click, without scanning the full list. Desktop gets the chip through the web client, so Desktop needs no separate change. iOS and Android follow later.

### Requirements

---

1.  **Chip and filter**

---

The Due today chip sits in the existing row of filter chips, after Overdue. It reuses the existing chip component, and no Figma reference applies. The list under the chip uses the same rules as the other chips, including the owner's time zone.

**Checklist**

- [] The Due today chip sits directly after the Overdue chip
- [] The chip reuses the existing chip component
- [] Only one chip is active at a time, as it is for All, Assigned to me and Overdue
- [] The All chip stays the default active chip
- [] The list under the chip shows to-dos not checked off whose due date is today in the to-do owner's time zone
- [] The list under the chip sorts by due date, as the other chips do
- [] To-dos with no due date and checked-off to-dos do not appear under the chip

---

2.  **Analytics**

---

Picking the chip sends the existing filter event with the new filter value. The Data team has already added the value to the tracking plan, so no new event is needed.

**Checklist**

- [] Picking the Due today chip sends `filter_selected` with `filter` set to `due_today`
- [] The other chips keep sending their current `filter` values

> Desktop receives the chip through the web client, so no Desktop change is in scope. iOS and Android are out of scope and follow later. No other feature depends on this chip.
