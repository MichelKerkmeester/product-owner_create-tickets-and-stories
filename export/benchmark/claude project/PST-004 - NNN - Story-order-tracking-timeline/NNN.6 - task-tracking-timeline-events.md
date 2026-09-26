# DATA - TRACK - Tracking timeline events

## About

---

These two events show whether customers use the timeline or still leave for the carrier's page, against the goal of fewer WISMO contacts. No FE task can send an event before its tracking plan row exists, so this comes first.

**Story**

---

- [Customer - Order tracking - Order page timeline](<NNN - Story-order-tracking-timeline.md>)

**Related tasks**

---

- [FE - Web - TRACK - Order page tracking timeline](<NNN.3 - task-web-tracking-timeline.md>)
- [FE - iOS - TRACK - Order page tracking timeline](<NNN.4 - task-ios-tracking-timeline.md>)
- [FE - Android - TRACK - Order page tracking timeline](<NNN.5 - task-android-tracking-timeline.md>)

### Requirements

---

**Tracking plan rows**

---

**Checklist**

- [] One row for tracking timeline views on the order page
- [] One row for carrier link taps
- [] Event names follow `object_action` in snake_case with a past-tense verb
- [] Each event carries `platform`, `app_version`, `market`, `locale` and `customer_type`
