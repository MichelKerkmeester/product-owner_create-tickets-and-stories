# DATA - TRACK - Tracking timeline events

### About

---

The release goal is a drop in WISMO contacts. These two events show whether customers use the timeline and how often they still leave for the carrier's page. No FE task can send a new event until the event has a row in the tracking plan, so this task comes before the FE analytics work.

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

- [ ] One row for the tracking timeline being viewed on the order page
- [ ] One row for the carrier link being tapped
- [ ] Event names follow `object_action` in snake_case with a past-tense verb
- [ ] Each event carries `platform`, `app_version`, `market`, `locale` and `customer_type`
