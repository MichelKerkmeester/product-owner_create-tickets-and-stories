# FE - Web - TODO - Due today filter chip

## About

---

The To-dos view's chips, All, Assigned to me and Overdue, leave members scanning the full list for to-dos due today.

Add a Due today chip on Web. Desktop gets it through the web client, and iOS and Android follow in later tasks, out of scope here.

### Requirements

---

1.  **Add the Due today chip**

---

**Checklist**

- [] Show a `Due today` chip after Overdue: All, Assigned to me, Overdue, Due today
- [] Use the existing filter chip, with no new styling
- [] Keep one chip active at a time
- [] Keep All as the default when the To-dos view opens
- [] Show the label in every shipped locale, with en-US for a missing string
- [] Desktop shows the chip on its next load, with no Desktop release

---

2.  **Show only the to-dos due today**

---

As with Overdue, "today" is the to-do owner's date, even when the viewer is on another one.

**Checklist**

- [] List every to-do the member can open that is unchecked and due today in the owner's time zone
- [] Leave out checked-off to-dos and ones due before or after today or undated
- [] Sort by due date, like the other chips
- [] When nothing is due today, keep the chip active and show an empty list, not another chip's list

---

3.  **Send filter_selected when the chip is picked**

---

`due_today` is already in the tracking plan, so no Data review blocks this.

**Checklist**

- [] Send `filter_selected` with `filter` set to `due_today` on selecting Due today
- [] Include the usual `filter_selected` properties: `workspace_id`, hashed `user_id`, `platform`, `app_version` as the web build number and `plan`
- [] Keep sending `all`, `assigned_to_me` and `overdue` unchanged
