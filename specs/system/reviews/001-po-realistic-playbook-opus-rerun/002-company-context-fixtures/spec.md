---
title: "Feature Specification: Phase 2, company context fixtures"
description: "The new Product Owner scenarios are set at three fictional companies and cite source files that do not exist yet. This phase scopes the three company context documents and the 22 source attachments, fixes every file name phase 003 cites, and lists the hard values the grader checks verbatim."
trigger_phrases:
  - "company context fixtures"
  - "roamstay loomlist fernhouse"
  - "fixture manifest"
  - "scenario attachments"
importance_tier: "important"
contextType: "implementation"
---
<!-- SPECKIT_TEMPLATE_SOURCE: spec-core | v2.2 -->
# Feature Specification: Phase 2, company context fixtures

<!-- SPECKIT_LEVEL: 2 -->
---

<!-- ANCHOR:metadata -->
## 1. METADATA

| Field | Value |
|-------|-------|
| **Level** | 2 |
| **Priority** | P1 |
| **Status** | Complete |
| **Created** | 2026-09-25 |
| **Branch** | `main` |
| **Parent Spec** | ../spec.md |
| **Phase** | 2 of 5 |
| **Predecessor** | 001-story-prefix-and-bundle |
| **Successor** | 003-playbook-rewrite |
| **Handoff Criteria** | All 25 manifest files exist, hold every hard value in their row, pass the em dash grep and the Human Voice lint, and are committed in both repos |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:phase-context -->
## Phase Context

This is **Phase 2** of the packet that rewrites the Product Owner manual testing playbook around realistic tickets for three fictional companies, then reruns both packagings on claude-opus-5-5 at effort medium.

**Scope Boundary**: new files under `AI Systems/Product Owner/benchmark/fixtures/companies/` only. No skill, kernel, knowledge, playbook or runner file changes in this phase.

**Dependencies**:
- The approved plan's scenario catalog, 23 scenarios per side
- The engineering corpus in `Product Context/Tasks & Stories/`, for the density and vocabulary real handover material carries
- `AI Systems/Product Owner/benchmark/grader/lint_replies.py`, run on one file at a time with `--brief`

**Deliverables**:
- `roamstay-context.md`, `loomlist-context.md` and `fernhouse-context.md`
- 22 source attachments, named exactly as the manifest below states
- A values check in this phase's `scratch/` that reads the manifest table and greps every hard value in its file

**Changelog**:
- When this phase closes, refresh the matching file in ../changelog/ using the parent packet number plus this phase folder name.
<!-- /ANCHOR:phase-context -->

---

<!-- ANCHOR:problem -->
## 2. PROBLEM & PURPOSE

### Problem Statement
Phase 003 rewrites the playbook so 46 scenarios produce tickets for Roamstay, Loomlist and Fernhouse. Each of those tickets needs company facts for its names, surfaces, versions and numbers, and 18 of the 23 scenario pairs also need source material beyond the prompt: support tickets, a log excerpt, team chat threads, PM briefs, design notes, API notes and two drafts. None of it exists yet. Without fixed file names and fixed values, phase 003 cannot write a scenario's attachments, and a Pass clause has nothing to check verbatim.

### Purpose
Every scenario attaches files that exist, and every value a Pass clause checks sits verbatim in the file that supplies it.
<!-- /ANCHOR:problem -->

---

<!-- ANCHOR:scope -->
## 3. SCOPE

### In Scope
- Three company context documents of 150 to 250 lines, one per company
- 22 source attachments: 6 for Roamstay, 9 for Loomlist, 7 for Fernhouse
- The manifest below, which fixes every file name, kind, citing scenario and hard value
- The writing rules every fixture follows, and the checks that prove them
- Commits in the Barter repo and in the Product Owner public repo

### Out of Scope
- Scenario files, prompts, the playbook root and the runner's `- Attachments:` parser - phase 003 owns them
- Skill, kernel and knowledge sources - phase 001 owns the only source change in this packet
- Running any scenario - phase 004, after the operator approves the scenario plan
- A README or index inside the fixtures folder - the playbook root links the folder in phase 003

### Files to Change

| File Path | Change Type | Description |
|-----------|-------------|-------------|
| `AI Systems/Product Owner/benchmark/fixtures/companies/roamstay/` | Create | `roamstay-context.md` and 6 attachments |
| `AI Systems/Product Owner/benchmark/fixtures/companies/loomlist/` | Create | `loomlist-context.md` and 9 attachments |
| `AI Systems/Product Owner/benchmark/fixtures/companies/fernhouse/` | Create | `fernhouse-context.md` and 7 attachments |
| `AI Systems/Product Owner/specs/013-po-realistic-playbook-opus-rerun/002-company-context-fixtures/scratch/check_manifest_values.py` | Create | Reads the manifest table and greps each hard value in its file. The packet is gitignored, so it is never committed |

### Writing rules

These are decisions, not suggestions. A writer who cannot meet one stops and reports it.

1. **Vendors by role.** Third-party vendors appear by role only: the payment provider, the parcel carrier, the pallet carrier, the warehouse system, the email delivery provider, the map provider. A real vendor name would invite that vendor's real behavior into a reply, and grading would then have to rule on facts no fixture gave. Internal services carry invented kebab-case names such as `booking-service`. iOS, Android, macOS, Windows and the web are platforms and keep their names
2. **Nothing real.** No company, product or brand name, Barter included, and no comparison with a real product. People appear by a fictional first name and a role, never a surname and never a name from the Barter corpus
3. **No links.** No URL of any kind. A design reference names a frame, such as `Date picker / Stay limits`, and a document is named by its title
4. **Every scenario attaches its company's context document.** 18 of the 23 also attach the sources the scenario table below lists
5. **Markdown only.** Every fixture is a `.md` file. A log excerpt sits in a fenced block inside its file
6. **Dates.** Every date falls in 2026 and no later than `2026-09-25`, except the targets and deadlines the manifest names
7. **Handover shapes.** Each attachment is what a PM, support agent or engineer would hand over: a note, thread, ticket, log, brief or draft, opening with where it came from, who wrote it and when. Only the parent task and the save-card draft take a Product Owner template shape
8. **Human Voice hard checks.** No em dash, semicolon, curly quote, bullet line ending in a full stop, second ellipsis or hard blocker word from `AI Systems/Product Owner/sk-product-owner/references/hvr-core.md` section 3, for example leverage, seamless, robust or utilize. The lint treats a fixture as prose, so all of these fail it
9. **No test vocabulary.** No scenario ID, and none of the words playbook, benchmark, fixture, scenario or grader. A runtime that reads them learns it is under test
10. **Context document sections.** Eleven H2 headings, in this order: `Product and surfaces`, `Personas and roles`, `Glossary`, `Services and integrations`, `Teams and discipline codes`, `Feature codes`, `Platforms and app versions`, `Currencies and locales`, `Key flows`, `Known constraints`, `Analytics conventions`. The discipline code section states the task and bug title pattern and says that story and epic titles carry no discipline code, matching `references/story-mode.md`
11. **Values are pasted.** Each backticked value in a file's manifest row is copied into the file character for character. `€18.00` never becomes `€18`

### Scenario attachments

The Project twin of each skill scenario (`SID` to `PID`, `STK` to `PTK`, `SBG` to `PBG`, `SDK` to `PDK`, `SST` to `PST`, `SEP` to `PEP`, `SIR` to `PIR`) attaches the same files.

| Scenario | Company | Artifact | Attachments |
|----------|---------|----------|-------------|
| SID-001 | Loomlist | Task, `Due today` filter chip | `loomlist-context.md` |
| STK-001 | Fernhouse | Quick copy task, free-shipping banner | `fernhouse-context.md` |
| STK-002 | Roamstay | FE task, date picker stay limits | `roamstay-context.md`, `roamstay-date-picker-design-notes.md` |
| STK-003 | Fernhouse | BE task, label webhook idempotency and retries | `fernhouse-context.md`, `fernhouse-carrier-label-api-notes.md`, `fernhouse-carrier-label-thread.md` |
| STK-004 | Loomlist | Parent task, recurring to-dos | `loomlist-context.md`, `loomlist-recurring-todos-pm-brief.md` |
| STK-005 | Loomlist | Android subtask of a supplied parent | `loomlist-context.md`, `loomlist-recurring-todos-parent-task.md` |
| STK-006 | Roamstay | DATA task, booking funnel events | `roamstay-context.md`, `roamstay-booking-funnel-tracking-plan.md` |
| SBG-001 | Fernhouse | Quick bug, iOS cart badge | `fernhouse-context.md` |
| SBG-002 | Roamstay | Standard bug, Android total without city tax | `roamstay-context.md`, `roamstay-support-ticket-58213.md` |
| SBG-003 | Loomlist | Complex bug, reminders late after DST | `loomlist-context.md`, `loomlist-reminders-dst-log-excerpt.md`, `loomlist-reminders-dst-user-reports.md` |
| SDK-001 | Fernhouse | Behavior reference, discount stacking | `fernhouse-context.md`, `fernhouse-promotions-rules.md` |
| SDK-002 | Roamstay | Runbook, payment webhook failures | `roamstay-context.md`, `roamstay-payment-webhook-incident-notes.md` |
| SDK-003 | Loomlist | Proposal, sync conflicts | `loomlist-context.md`, `loomlist-sync-conflict-thread.md` |
| SDK-004 | Loomlist | Catalog behind the conflict gate | `loomlist-context.md`, `loomlist-notification-spec.md`, `loomlist-email-template-inventory.md` |
| SST-001 | Roamstay | Story, free cancellation filter | `roamstay-context.md`, `roamstay-free-cancellation-pm-notes.md` |
| SST-002 | Loomlist | Story, view-only share links | `loomlist-context.md`, `loomlist-view-only-links-design-notes.md` |
| SST-003 | Fernhouse | Story refinement of a rough draft | `fernhouse-context.md`, `fernhouse-save-card-draft.md` |
| SST-004 | Fernhouse | Story with nested Tasks, order tracking | `fernhouse-context.md`, `fernhouse-order-tracking-pm-brief.md`, `fernhouse-carrier-tracking-api-facts.md` |
| SEP-001 | Roamstay | Epic, Partner Hub self-onboarding | `roamstay-context.md`, `roamstay-partner-self-onboarding-brief.md` |
| SEP-002 | Loomlist | Epic, offline mode | `loomlist-context.md`, `loomlist-offline-mode-brief.md` |
| SEP-003 | Fernhouse | Quick epic, self-serve returns | `fernhouse-context.md` |
| SIR-001 | Roamstay | Vague intake, loyalty points | `roamstay-context.md` |
| SIR-002 | Fernhouse | Conflicting commands on one input | `fernhouse-context.md`, `fernhouse-wishlist-feedback.md` |

### Manifest

Each file lives at `AI Systems/Product Owner/benchmark/fixtures/companies/<company>/<file>`, with the company in lowercase. Phase 003 cites these names exactly. The last column holds only values: every backticked span in it must appear verbatim in that file, and the values check reads this table to prove it. `Cited by` lists skill IDs, and each Project twin cites the same file.

| File | Company | Kind | Cited by | Hard values the grader checks |
|------|---------|------|----------|-------------------------------|
| `roamstay-context.md` | Roamstay | context | STK-002, STK-006, SBG-002, SDK-002, SST-001, SEP-001, SIR-001 | `Guest app`, `Partner Hub`, `Back office`, `Guest`, `Partner`, `Ops agent`, `Guest Support`, `search-service`, `booking-service`, `payments-service`, `partner-service`, `events-collector`, `the payment provider`, `FE`, `BE`, `BO`, `FS`, `DATA`, `DS`, `{Discipline} - {Surface} - {Feature code} - {Title}`, `SRCH`, `PROP`, `BOOK`, `PAY`, `PHUB`, `ONB`, `TRK`, `OPS`, `8.12.0`, `8.12.1`, `2026-09-16`, `EUR`, `GBP`, `USD`, `CHF`, `SEK`, `en-GB`, `en-US`, `de-DE`, `fr-FR`, `es-ES`, `it-IT`, `nl-NL`, `30 nights`, `365 days`, `25 results`, `8 rooms`, `City tax`, `Pay now`, `Pay at property`, `payment_pending`, `30 minutes`, `18,000`, `no loyalty or points scheme`, `object_action`, `app_version`, `session_id`, `_minor`, `filter_applied` |
| `roamstay-date-picker-design-notes.md` | Roamstay | notes | STK-002 | `Date picker / Stay limits`, `1 night`, `30 nights`, `14 nights`, `365 days`, `This property has a 3-night minimum`, `Stays can be up to 30 nights`, `Select check-out date`, `Show prices` |
| `roamstay-booking-funnel-tracking-plan.md` | Roamstay | draft | STK-006 | `search_submitted`, `property_viewed`, `room_selected`, `checkout_started`, `payment_submitted`, `booking_confirmed`, `property_id`, `check_in`, `check_out`, `nights`, `guests`, `currency`, `total_amount_minor`, `source`, `server`, `booking-service`, `checkout_complete`, `deprecated`, `2026-11-01`, `date_changed`, `proposed` |
| `roamstay-support-ticket-58213.md` | Roamstay | ticket | SBG-002 | `58213`, `2026-09-21`, `RS-7Q4K2M`, `8.12.1`, `8.12.0`, `2026-09-16`, `3 nights`, `2 adults`, `Pay now`, `Total €387.00`, `Total €405.00`, `€3.00`, `€18.00`, `€258.00`, `€270.00`, `14 chats`, `High` |
| `roamstay-payment-webhook-incident-notes.md` | Roamstay | notes | SDK-002 | `INC-0412`, `2026-09-09`, `47 minutes`, `1,284`, `1,190`, `94`, `71`, `payment_pending`, `30 minutes`, `/v2/psp/webhooks`, `401`, `8 attempts`, `24 hours`, `payments.webhook.4xx_rate`, `5%`, `5 minutes`, `2026-09-10`, `Payments / Webhooks`, `psp-replay`, `psp-reconcile`, `15 minutes`, `#payments-oncall`, `1 hour`, `proposed` |
| `roamstay-free-cancellation-pm-notes.md` | Roamstay | notes | SST-001 | `Free cancellation`, `Free cancellation until 14 Oct`, `d MMM`, `14 days`, `Price`, `Star rating`, `312 stays`, `No stays with free cancellation for these dates`, `Clear filter`, `filter_applied`, `filter_name`, `free_cancellation`, `8.13.0` |
| `roamstay-partner-self-onboarding-brief.md` | Roamstay | brief | SEP-001 | `11 business days`, `3 business days`, `38%`, `1,500`, `2027-06-30`, `40 rooms`, `8 photos`, `20 MB`, `1 business day`, `channel manager`, `Sign-up and verification`, `Property profile and photos`, `Rooms and rates setup`, `Policies and city tax`, `Payout details and identity checks`, `Go-live review queue` |
| `loomlist-context.md` | Loomlist | context | SID-001, STK-004, STK-005, SBG-003, SDK-003, SDK-004, SST-002, SEP-002 | `Desktop`, `Web`, `iOS`, `Android`, `wraps the web client`, `sync-service`, `reminders-service`, `notifications-service`, `share-service`, `the email delivery provider`, `local notifications`, `in the app only`, `Support console`, `Owner`, `Admin`, `Member`, `Guest`, `Free`, `Plus`, `Team`, `€8 per member per month`, `€14 per member per month`, `FE`, `BE`, `BO`, `FS`, `DATA`, `DS`, `{Discipline} - {Platform} - {Feature code} - {Title}`, `PAGE`, `DB`, `TODO`, `REM`, `SYNC`, `SHARE`, `NOTIF`, `OFFL`, `5.3.2`, `5.3.0`, `5.3.1`, `macOS 13`, `Windows 10`, `v3`, `block-level last-writer-wins`, `All`, `Assigned to me`, `Overdue`, `owner's time zone`, `EUR`, `USD`, `GBP`, `JPY`, `BRL`, `en-US`, `de-DE`, `fr-FR`, `es-ES`, `ja-JP`, `pt-BR`, `object_action`, `workspace_id`, `app_version` |
| `loomlist-recurring-todos-pm-brief.md` | Loomlist | brief | STK-004 | `Repeat`, `Daily`, `Weekdays`, `Weekly`, `Monthly`, `Custom`, `1 to 99`, `Ends`, `Never`, `On date`, `After`, `365`, `Skip this one`, `500`, `recurring_todos`, `10%`, `Plus`, `owner's time zone`, `iOS`, `Android`, `Web`, `BE` |
| `loomlist-recurring-todos-parent-task.md` | Loomlist | ticket | STK-005 | `FS - TODO - Recurring to-dos`, `FE - iOS - TODO - Recurring to-dos`, `FE - Android - TODO - Recurring to-dos`, `FE - Web - TODO - Recurring to-dos`, `BE - TODO - Recurrence engine`, `Daily`, `Weekdays`, `Weekly`, `Monthly`, `Custom`, `1 to 99`, `Skip this one`, `365`, `500`, `recurring_todos`, `owner's time zone` |
| `loomlist-reminders-dst-log-excerpt.md` | Loomlist | log | SBG-003 | `reminders-service`, `rem_8f31c2`, `Europe/Amsterdam`, `platform=android`, `app_version=5.2.3`, `local_time=09:00`, `tz_offset=+01:00`, `tz_offset=+02:00`, `scheduled_utc=2026-03-30T08:00:00Z`, `2026-03-29` |
| `loomlist-reminders-dst-user-reports.md` | Loomlist | ticket | SBG-003 | `LL-20931`, `LL-20944`, `LL-20958`, `117`, `reminder-late`, `2026-03-29`, `2026-04-05`, `5.2.3`, `5.2.4`, `09:00`, `10:00`, `07:30`, `08:30`, `editing the reminder and saving it`, `2026-10-25` |
| `loomlist-sync-conflict-thread.md` | Loomlist | thread | SDK-003 | `block-level last-writer-wins`, `v3`, `0.8%`, `40`, `lost-edit`, `Option A`, `Option B`, `Option C`, `field-level`, `three-way merge`, `CRDT`, `Conflicting edit from {device name}`, `Joana`, `Engineering Manager, Sync`, `2026-10-09`, `not decided` |
| `loomlist-notification-spec.md` | Loomlist | notes | SDK-004 | `EM-01`, `EM-02`, `EM-03`, `EM-04`, `EM-05`, `EM-06`, `Daily digest`, `Mentioned in a page`, `Comment reply`, `Page shared with you`, `Workspace invite`, `Weekly summary`, `08:00`, `recipient's local time`, `Monday 09:00`, `Settings > Notifications` |
| `loomlist-email-template-inventory.md` | Loomlist | notes | SDK-004 | `EM-01`, `EM-02`, `EM-03`, `EM-04`, `EM-05`, `EM-06`, `Daily digest`, `Mentioned in a page`, `Comment reply`, `Page shared with you`, `Workspace invite`, `Weekly summary`, `07:00 UTC`, `Monday 09:00`, `tpl_digest_v4`, `tpl_mention_v2`, `tpl_comment_reply_v2`, `tpl_page_shared_v3`, `tpl_workspace_invite_v5`, `tpl_weekly_summary_v1` |
| `loomlist-view-only-links-design-notes.md` | Loomlist | notes | SST-002 | `Anyone with the link can view`, `Never`, `7 days`, `30 days`, `60 seconds`, `3 active links`, `Free`, `Plus`, `Team`, `noindex`, `Duplicate`, `Do sub-pages inherit the link?`, `not decided` |
| `loomlist-offline-mode-brief.md` | Loomlist | brief | SEP-002 | `23%`, `31%`, `500 most recently opened pages`, `1 GB`, `30 seconds`, `Web is out of scope`, `block-level last-writer-wins`, `2026-10-09`, `Offline reading`, `Offline editing and creation`, `Sync on reconnect`, `Offline indicator and storage settings`, `Q1 2027` |
| `fernhouse-context.md` | Fernhouse | context | STK-001, STK-003, SBG-001, SDK-001, SST-003, SST-004, SEP-003, SIR-002 | `Web`, `iOS`, `Android`, `Admin`, `the warehouse system`, `the parcel carrier`, `the pallet carrier`, `the payment provider`, `Customer`, `CS agent`, `Warehouse operator`, `Merchandiser`, `cart-service`, `checkout-service`, `promotions-service`, `orders-service`, `shipping-service`, `FE`, `BE`, `BO`, `FS`, `DATA`, `DS`, `{Discipline} - {Surface} - {Feature code} - {Title}`, `CART`, `CHK`, `PROMO`, `SHIP`, `TRACK`, `RET`, `ACCT`, `WISH`, `4.8.0`, `4.8.2`, `EUR`, `GBP`, `nl-NL`, `nl-BE`, `fr-BE`, `de-DE`, `fr-FR`, `en-GB`, `Free shipping on orders over €50`, `Free shipping on orders over £45`, `15:00`, `30 kg`, `120 cm`, `99+`, `30 days`, `€4.95`, `£3.95`, `1,900`, `6 days`, `object_action`, `app_version`, `market` |
| `fernhouse-carrier-label-api-notes.md` | Fernhouse | notes | STK-003 | `POST /v1/shipments`, `GET /v1/shipments/{shipment_id}`, `label.created`, `label.failed`, `/webhooks/carrier/labels`, `event_id`, `X-Carrier-Signature`, `HMAC-SHA256`, `5 seconds`, `5 attempts`, `1 min, 5 min, 15 min, 1 h, 6 h`, `24 hours`, `20 requests per second` |
| `fernhouse-carrier-label-thread.md` | Fernhouse | thread | STK-003 | `#fulfilment-eng`, `2026-09-16`, `2026-09-15`, `37 duplicate labels`, `€0.42`, `12 orders`, `15:00`, `event_id`, `7 days`, `10 minutes`, `30 minutes`, `#fulfilment-alerts`, `more than 5`, `polling only`, `rejected` |
| `fernhouse-promotions-rules.md` | Fernhouse | notes | SDK-001 | `one discount code per order`, `automatic promotions first`, `exclusive`, `STAFF-`, `compare_at`, `applies_to_sale`, `50%`, `€50`, `£45`, `0.01`, `half up`, `gift card`, `2026-05-01`, `retired` |
| `fernhouse-save-card-draft.md` | Fernhouse | draft | SST-003 | `# PRD - Checkout - Save card for next time`, `**Checklist**`, `Save this card for next time`, `unchecked by default`, `You can save up to 5 cards`, `Card ending 7031`, `Expires 08/28`, `CVC`, `€150`, `£130`, `Account > Payment methods`, `Remove this card?`, `guest checkout` |
| `fernhouse-order-tracking-pm-brief.md` | Fernhouse | brief | SST-004 | `Order placed`, `Packed`, `Shipped`, `Out for delivery`, `Delivered`, `Delivery failed`, `PU`, `IT`, `OD`, `DL`, `EX`, `Arriving Thursday 1 October`, `Between 10:00 and 14:00`, `90 days`, `30 kg`, `120 cm`, `BE tracking webhook` |
| `fernhouse-carrier-tracking-api-facts.md` | Fernhouse | notes | SST-004 | `tracking.updated`, `/webhooks/carrier/tracking`, `PU`, `IT`, `OD`, `DL`, `EX`, `eta_window`, `occurred_at`, `out of order`, `event_id`, `X-Carrier-Signature`, `5 attempts`, `1 min, 5 min, 15 min, 1 h, 6 h` |
| `fernhouse-wishlist-feedback.md` | Fernhouse | notes | SIR-002 | `412`, `2026-07-01`, `2026-09-20`, `50 items`, `4.8.0`, `4.8.2`, `saved on the device`, `saved to the account` |

### Shared values

A value in this table is identical in every file listed. Both rows of the manifest carry it, so the values check enforces it, and the orchestrator's read confirms no file states a second value for the same fact.

| Fact | Value | Files |
|------|-------|-------|
| Roamstay stay limits | `30 nights`, `365 days` | `roamstay-context.md`, `roamstay-date-picker-design-notes.md` |
| Roamstay app versions | `8.12.0` iOS, `8.12.1` Android released `2026-09-16` | `roamstay-context.md`, `roamstay-support-ticket-58213.md` |
| Roamstay pending payments | `payment_pending` expires after `30 minutes` | `roamstay-context.md`, `roamstay-payment-webhook-incident-notes.md` |
| Roamstay filter event | `filter_applied` | `roamstay-context.md`, `roamstay-free-cancellation-pm-notes.md` |
| Loomlist sync model | `block-level last-writer-wins`, protocol `v3` | `loomlist-context.md`, `loomlist-sync-conflict-thread.md`, `loomlist-offline-mode-brief.md` |
| Loomlist conflict decision date | `2026-10-09` | `loomlist-sync-conflict-thread.md`, `loomlist-offline-mode-brief.md` |
| Loomlist recurrence rules | repeat options, `1 to 99`, `365`, `500`, `recurring_todos`, `Skip this one` | `loomlist-recurring-todos-pm-brief.md`, `loomlist-recurring-todos-parent-task.md` |
| Loomlist DST change | `2026-03-29`, Android `5.2.3` | `loomlist-reminders-dst-log-excerpt.md`, `loomlist-reminders-dst-user-reports.md` |
| Loomlist plans | `Free`, `Plus`, `Team` | `loomlist-context.md`, `loomlist-view-only-links-design-notes.md` |
| Fernhouse free shipping | `€50`, `£45` | `fernhouse-context.md`, `fernhouse-promotions-rules.md` |
| Fernhouse app versions | `4.8.0` iOS, `4.8.2` Android | `fernhouse-context.md`, `fernhouse-wishlist-feedback.md` |
| Fernhouse dispatch cut-off | `15:00` | `fernhouse-context.md`, `fernhouse-carrier-label-thread.md` |
| Parcel carrier webhooks | `event_id`, `X-Carrier-Signature`, `5 attempts` at `1 min, 5 min, 15 min, 1 h, 6 h` | `fernhouse-carrier-label-api-notes.md`, `fernhouse-carrier-tracking-api-facts.md` |
| Pallet carrier threshold | `30 kg`, `120 cm` | `fernhouse-context.md`, `fernhouse-order-tracking-pm-brief.md` |

### Status traps and worked facts

Each row is a fact a faithful artifact has to keep as the file states it. The writer gets the wording of the label and the arithmetic right, and the file never explains why the trap is there.

| File | Fact | How the file carries it |
|------|------|-------------------------|
| `roamstay-booking-funnel-tracking-plan.md` | `date_changed` is not agreed | Its row is marked `proposed` |
| `roamstay-booking-funnel-tracking-plan.md` | `checkout_complete` stops | Marked `deprecated`, removal on `2026-11-01` |
| `roamstay-support-ticket-58213.md` | The charge is right and the display is wrong | The guest was charged `€405.00`, which is `€387.00` plus `€18.00` city tax (`€3.00` per adult per night, 2 adults, 3 nights). Android showed `Total €387.00`. The agent's 2-night test showed `€258.00` and charged `€270.00`. 1-night stays and iOS show the right total |
| `roamstay-payment-webhook-incident-notes.md` | A dual-secret window is not built | A follow-up to accept the old and new signing secret for `1 hour` during a rotation, marked `proposed`. The numbers add up: `1,190` recovered plus `94` expired is `1,284` |
| `loomlist-reminders-dst-log-excerpt.md` | The excerpt shows evidence, not a cause | After `2026-03-29` a `09:00` reminder in `Europe/Amsterdam` belongs at `07:00:00Z`. The excerpt shows it at `scheduled_utc=2026-03-30T08:00:00Z` with `tz_offset=+01:00`, which fires at `10:00` local, next to a reminder created after the change with `tz_offset=+02:00`. No line names a root cause |
| `loomlist-reminders-dst-user-reports.md` | Two issues on two platforms | Android `5.2.3`: one-off reminders set for `09:00` arrive at `10:00`. iOS `5.2.4`: daily reminders set for `07:30` arrive at `08:30` every day until the user fixes it by `editing the reminder and saving it`. Web and desktop users report nothing, since reminders there show in the app only. The next change is on `2026-10-25` |
| `loomlist-sync-conflict-thread.md` | No decision was made | `Option B` has supporters and is never agreed. The thread ends `not decided`, with `Joana`, `Engineering Manager, Sync`, as decision owner and `2026-10-09` as the date |
| `loomlist-view-only-links-design-notes.md` | One open question | `Do sub-pages inherit the link?` stays `not decided`, with who settles it |
| `loomlist-offline-mode-brief.md` | Conflict handling is not settled | Names the `2026-10-09` sync decision as a dependency |
| `loomlist-notification-spec.md` and `loomlist-email-template-inventory.md` | The digest send time conflicts | The spec says `08:00` in the recipient's local time and never mentions `07:00`. The inventory says `07:00 UTC` and never mentions `08:00`. Every other entry agrees. Neither file calls itself canonical, approved or authoritative, or calls the other outdated or retired. Their last-edited dates differ, and a newer date does not settle authority |
| `fernhouse-carrier-label-thread.md` | Polling was dropped | Polling only was proposed once and `rejected` in the thread, with the rate limit as the reason |
| `fernhouse-promotions-rules.md` | Two codes on one order are gone | Allowed until `2026-05-01`, `retired` since |
| `fernhouse-save-card-draft.md` | Deliberately rough | `PRD -` H1, a `**Checklist**` build list under Requirements, no `## Acceptance criteria` section, at most one ellipsis |
| `loomlist-recurring-todos-parent-task.md` | Deliberately finished | The house parent-task shape from `assets/task-templates.md` section 3, the four subtask titles as backticked plain text, no links |
| `fernhouse-wishlist-feedback.md` | Bug or story is genuinely unclear | Support calls it a bug. The app has never saved wishlists to the account, while web always has |
<!-- /ANCHOR:scope -->

---

<!-- ANCHOR:requirements -->
## 4. REQUIREMENTS

### P0 - Blockers (MUST complete)

| ID | Requirement |
|----|-------------|
| REQ-001 | Exactly the 25 files the manifest names exist at their paths under `AI Systems/Product Owner/benchmark/fixtures/companies/`, and no other file sits there |
| REQ-002 | Each company context document is 150 to 250 lines and carries the eleven H2 sections writing rule 10 names, in that order |
| REQ-003 | Every backticked value in a file's manifest row appears verbatim in that file |
| REQ-004 | No fixture contains an em dash (U+2014) |
| REQ-005 | Every fixture passes `benchmark/grader/lint_replies.py --brief` as a single file |
| REQ-006 | The two given inputs keep their deliberate shape: the parent task follows the house parent-task shape with its four subtask titles as backticked plain text, and the save-card draft opens with `# PRD - ` and carries a `**Checklist**` build list. No other fixture carries a Product Owner template marker |
| REQ-007 | The two digest sources disagree on the digest send time and on nothing else, and neither declares authority, approval, lifecycle or retirement for any claim |
| REQ-008 | The fixtures are fictional and self-contained: no URL, no name from the brand deny list, no mention of Barter, no real person, and no scenario ID or test vocabulary |

### P1 - Required (complete OR user-approved deferral)

| ID | Requirement |
|----|-------------|
| REQ-009 | Every file name starts with its company slug, is lowercase kebab-case ASCII ending in `.md`, and contains none of `review`, `readme`, `benchmark` or `testing-playbook`, which the runner's sandbox build and isolation proof react to |
| REQ-010 | A value in the shared-values table is identical in every file that carries it, and no fixture states a second value for the same fact outside the digest pair |
| REQ-011 | Each attachment is 20 to 150 lines and names its source, its author by first name and role, and a 2026 date no later than `2026-09-25` within its first 5 lines |
| REQ-012 | The fixtures are committed in the Barter repo and in the Product Owner public repo, the public commit carries no attribution line, and nothing is pushed before the operator's go-ahead |

> Acceptance criteria for these requirements live in `acceptance-criteria.md`,
> which is the document that decides whether this packet may close.
<!-- /ANCHOR:requirements -->

---

<!-- ANCHOR:success-criteria -->
## 5. SUCCESS CRITERIA

- **SC-001**: Phase 003 writes each scenario's `- Attachments:` bullet from the scenario attachments table without inventing a name
- **SC-002**: Every value a phase 003 Pass clause checks is found with `grep -F` in a file the scenario attaches
<!-- /ANCHOR:success-criteria -->

---

<!-- ANCHOR:risks -->
## 6. RISKS & DEPENDENCIES

| Type | Item | Impact | Mitigation |
|------|------|--------|------------|
| Risk | A writer paraphrases a hard value, `€3.00` written as `€3` | High | Writing rule 11, and the values check greps each literal |
| Risk | Fixture prose trips the lint: a semicolon in a log line, a bullet ending in a full stop | Med | Writing rule 8 names every hard check, and the lint runs per file |
| Risk | The digest pair leaks a winner through a status word or a "source of truth" line, so the conflict gate never fires | High | REQ-007 and its two greps |
| Risk | A fixture names a scenario ID or the benchmark, and the runtime learns it is under test | High | Writing rule 9 and the test-vocabulary grep |
| Risk | A real vendor name brings that vendor's real behavior into a reply | Med | Writing rule 1 and the brand grep |
| Risk | The SST-003 refinement keeps the draft's basename, so `export/fernhouse-save-card-draft.md` has no `[###] - ` prefix | Med | Phase 003 makes the collector and the Export names rule accept a refinement basename. The name holds no `prd`, so phase 001's `PRD-` grep stays clear of it |
| Risk | A value changes after phase 003 cites it | Med | Change the manifest first, then the fixture, then the scenario, and rerun the values check |
| Dependency | The approved scenario catalog | Names and values would drift from the scenarios | Green, frozen in the plan |
| Dependency | The `opus-medium` agent definition | Writers would run at a different effort | Fall back to the Agent tool's `model: opus`, and say so in the goal log |
| Dependency | Operator go-ahead for the push | Commits stay local | Push only on the go-ahead, Barter through the barter account |
<!-- /ANCHOR:risks -->

---


---

<!-- ANCHOR:nfr -->
## L2: NON-FUNCTIONAL REQUIREMENTS

### Performance
- **NFR-P01**: Three writers run at once, one per company
- **NFR-P02**: Every check in `plan.md` section 5 runs in under a minute on the 25 files

### Security
- **NFR-S01**: No string shaped like a real secret, API key, signing secret or full card number. A card appears only by its last four digits
- **NFR-S02**: The Product Owner public repo commit carries no attribution line

### Reliability
- **NFR-R01**: A fixture value changes only after the manifest changes
- **NFR-R02**: No em dash in any fixture or in this phase's documents
<!-- /ANCHOR:nfr -->

---

<!-- ANCHOR:edge-cases -->
## L2: EDGE CASES

### Data Boundaries
- A hard value holds a character the lint bans: change the value in the manifest, never the lint
- A value appears in two forms in one file, `€18.00` and `€18`: use the manifest form everywhere in that file
- A context document runs past 250 lines: cut glossary and flow prose, never a manifest value

### Error Scenarios
- A writer adds a file the manifest does not name: delete it, since REQ-001 is an exact set
- A check fails after a fix: rerun every check, not only the one that failed

### State Transitions
- A writer stops midway: a fresh writer rewrites that company's folder whole from the same brief
- The operator changes a value after the commit: the manifest changes first, then the fixture, in a new commit
<!-- /ANCHOR:edge-cases -->

---

<!-- ANCHOR:complexity -->
## L2: COMPLEXITY ASSESSMENT

| Dimension | Score | Notes |
|-----------|-------|-------|
| Scope | 12/25 | 25 new markdown files in three folders, no code outside a scratch check |
| Risk | 9/25 | The fixtures decide what grading can check |
| Research | 6/20 | Corpus shape, lint rules and runner behavior already read |
| **Total** | **27/70** | **Level 2** |
<!-- /ANCHOR:complexity -->

---

<!-- ANCHOR:questions -->
## 10. OPEN QUESTIONS

- May the phase 002 writers run beside phase 001? The two phases touch no file in common, and the parent's transition rule asks each phase to validate before the next begins. The orchestrator decides.
<!-- /ANCHOR:questions -->

---
