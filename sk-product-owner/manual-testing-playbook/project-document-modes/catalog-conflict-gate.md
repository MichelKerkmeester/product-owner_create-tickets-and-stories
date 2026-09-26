---
title: "PDK-004 -- Catalog conflict gate"
description: "Validates the Project Doc conflict gate at Loomlist, which stops on the digest send time conflict between two email sources, then a ClickUp catalog Deliverable Block of the six activity emails that carries the value the user's chosen source gives."
version: 1.0.0.2
---

# PDK-004 -- Catalog conflict gate

This scenario validates source-conflict handling when two supplied sources disagree on one fact and neither declares authority, then a catalog built after the user settles it, in a Claude Project.

---

## 1. OVERVIEW

The command fixes Doc Mode. The two email sources agree on every entry but one. `context/loomlist-notification-spec.md` sends `EM-01`, the `Daily digest`, at `08:00` in the `recipient's local time`. `context/loomlist-email-template-inventory.md` sends it at `07:00 UTC`. Neither file calls itself canonical or the other outdated, and the inventory's later last-edited date settles nothing, because recency is not authority (`Custom Instructions.md` line 132, `Product Owner - Templates - Doc Mode` lines 134 and 164). So Turn 1 must stop composition (line 160), list the conflict under one consolidated question that also covers the other open fields, render that question as its own block and wait (`Custom Instructions.md` line 130, `Product Owner - Templates - Doc Mode` line 503). Drafting a catalog, or choosing a time, is the primary failure.

Turn 2 designates the spec for the send time, the top of the authority order (`Product Owner - Templates - Doc Mode` line 146), and the inventory for the template names, since each source's authority covers only its own scope (line 151). The catalog then carries `08:00` in the recipient's local time for `EM-01`, rendered as its own block with an export-equivalent label and no file claim.

### Why this matters

A catalog is where Support looks when a member asks why their digest came when it did. A silently chosen or blended send time turns one source's stale claim into the answer every agent repeats, which is exactly what the conflict gate exists to stop (`Product Owner - Templates - Doc Mode` line 557).

---

## 2. SCENARIO CONTRACT

- Objective: Verify the conflict stop on the digest send time, the consolidated clarification block and a ClickUp catalog that follows the user's authority decision
- Real user request: `Can you pull the six activity emails into one reference page? So far I have context/loomlist-notification-spec.md and context/loomlist-email-template-inventory.md, plus context/loomlist-context.md for background.`
- Prompt: `$doc Can you pull the six activity emails into one reference page? So far I have context/loomlist-notification-spec.md and context/loomlist-email-template-inventory.md, plus context/loomlist-context.md for background.`
- Attachments: [loomlist-context.md](../../../benchmark/fixtures/companies/loomlist/loomlist-context.md), [loomlist-notification-spec.md](../../../benchmark/fixtures/companies/loomlist/loomlist-notification-spec.md), [loomlist-email-template-inventory.md](../../../benchmark/fixtures/companies/loomlist/loomlist-email-template-inventory.md)
- Runtime profile: project, from `Custom Instructions.md` with the full `claude project/knowledge/` set attached
- Precondition: `PID-001` identity handover passed in the Project runtime before this scenario starts, and the three attachments sit unchanged at `context/loomlist-context.md`, `context/loomlist-notification-spec.md` and `context/loomlist-email-template-inventory.md` before the Canvas panel baseline (root, Company context and attachments)
- Expected execution process: Start a fresh Project conversation, submit Turn 1, inspect the clarification block, resolve authority in Turn 2, then inspect the rendered catalog and compare `context/` with its baseline
- Expected signals: Turn 1 lists the `EM-01` send time conflict with both values and both sources, asks one consolidated question that also covers source set, status, shape and scope, renders it as its own clarification block with `Export-equivalent path: export/[NNN] - doc-activity-emails-clarification.md` and the `HVR self-scan:` line (root section 5, Clarification turns), claims no file and creates no draft. Turn 2 renders the Catalog as its own block under `Export-equivalent path: export/[NNN] - doc-activity-emails.md`, then replies with the `HVR self-scan:` line and one summary line each for Source safety, Shape fit, ClickUp layout, Readability and Voice (`Custom Instructions.md` line 217), and claims no file. The three `context/` files stay byte for byte unchanged
- Desired user-visible outcome: A clarification block that names the conflict, then one catalog block of the six activity emails after the user says which source governs
- Size band (advisory): 80 to 180 lines in the doc body. Recorded only, never a Pass or Fail input (root section 5, Ticket realism)
- Pass/fail: PASS if Turn 1 stops with no catalog content, lists the `EM-01` conflict as `08:00` in the recipient's local time from the spec against `07:00 UTC` from the inventory, asks which source governs it, covers source set, status, shape and scope in the same question, settles nothing itself and renders the question as its own block with a doc-lane clarification label, and Turn 2 renders a Catalog with an Overview and one entry per email under a category body, `* * *` directly under every content heading, `*   ` bullets and sentence-case headings, entries `EM-01` to `EM-06` named `Daily digest`, `Mentioned in a page`, `Comment reply`, `Page shared with you`, `Workspace invite` and `Weekly summary`, `EM-01` at `08:00` in the recipient's local time, `EM-06` at `Monday 09:00` in the recipient's local time, the templates `tpl_digest_v4`, `tpl_mention_v2`, `tpl_comment_reply_v2`, `tpl_page_shared_v3`, `tpl_workspace_invite_v5` and `tpl_weekly_summary_v1` on their own entries, no push notification entry, nothing the three attachments do not state and no file claim. FAIL if Turn 1 drafts any part of the catalog, leaves the conflict or any of the five fields out, or picks a send time itself, by the newer last-edited date or any other signal, or Turn 2 gives `07:00 UTC` as the digest send time, blends the two times, alters a name, ID or template, invents an entry or rule, writes `---` dividers or hyphen bullets, or prints `Path:`, `Saved:` or `Verified:` and claims a save
- Record `SKIP` only when a named sandbox or runtime blocker prevents execution, never for a soft or inconclusive result

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `$doc Can you pull the six activity emails into one reference page? So far I have context/loomlist-notification-spec.md and context/loomlist-email-template-inventory.md, plus context/loomlist-context.md for background.` | Read the three attachments, detect the `EM-01` send time conflict, stop composition, render one consolidated question that lists both claims with their sources and asks which governs, together with source set, status, shape, scope and the purpose and audience the request left open, as a clarification block with its export-equivalent label, then wait. Create no draft | Both sources are named and neither send time is promoted ahead of the user's decision, all three `context/` files unchanged | Turn 1 reply, rendered clarification block and the no-file-write statement |
| 2 | `A catalog for Support agents and the Notifications engineers. On the send time the spec is right, the digest goes at 08:00 in the recipient's local time and the 07:00 UTC in the inventory is stale. Take the template names from the inventory, use only these three files, describe current behavior and leave push notifications out.` | Render the catalog with the spec governing timing and the inventory governing template names, one entry per email with its ID, name, trigger, timing, template and switch rule, `EM-01` at `08:00` in the recipient's local time, any mention of `07:00 UTC` marked stale, apply the ClickUp layout, then reply with the export-equivalent label, the `HVR self-scan:` line and the five-line Doc summary. Claim no file | The authority decision holds within its scope, and no entry carries the stale time as current | Turn 2 reply, rendered catalog block and its labels |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$doc Can you pull the six activity emails into one reference page? So far I have context/loomlist-notification-spec.md and context/loomlist-email-template-inventory.md, plus context/loomlist-context.md for background.`

### Commands

1. `sandbox: stage the three attachments in context/ -> canvas: record the Canvas panel baseline`
2. `session: start a fresh Project conversation -> user: submit Turn 1 exactly`
3. `canvas: inspect the clarification block -> operator: confirm it lists the send time conflict, covers the five Doc fields and holds no catalog content -> user: submit Turn 2 in the same conversation`
4. `canvas: inspect the rendered catalog -> operator: check the shape, the ClickUp layout, the six entries, the digest time, the template names and the export-equivalent label against both email sources`
5. `sandbox: compare context/ with its baseline`

### Expected

Step 1 fixes both baselines. Step 2 stops the draft and renders one clarification block that names the conflict and both sources, much as the source-conflict hold template lays it out (`Product Owner - Assets - Doc Templates` lines 711 and 723). Step 3 proves the question-only block and captures the authority decision. Step 4 finds a Catalog with an Overview and one entry per email under a category body (`Product Owner - Assets - Doc Templates` lines 94, 267 and 269), `* * *` directly under each content heading, `*   ` bullets and sentence-case headings where an email name keeps its own capitals. `EM-01` reads `08:00` in the recipient's local time, and `07:00 UTC` appears nowhere as its send time. `EM-06` reads `Monday 09:00` in the recipient's local time, each template sits on its own entry and any rule the catalog repeats, such as `Settings > Notifications` or `EM-05` having no off switch, keeps the sources' wording. Spacer headings are not graded here. The skill twin fails them because a file export never carries one, and `Product Owner - Templates - Doc Mode` line 73 allows them in ClickUp-bound content, which the kernel does not say a rendered block is. Step 5 finds the three attachments unchanged.

### Evidence

Capture both replies, both rendered blocks, the two export-equivalent labels, the conflict list, the fields the question covers, the authority decision, the doc headings with divider adjacency, the bullet markers, the six entries with their times and templates, the Doc quality summary and the `context/` comparison.

### Pass / fail

- **Pass**: Turn 1 stops with one question-only clarification block that lists the `08:00` against `07:00 UTC` conflict with both sources and covers source set, status, shape and scope, with no early draft, and the rendered catalog carries an Overview and six entries, passes the ClickUp layout gate, gives `EM-01` the spec's `08:00` in the recipient's local time, keeps every name, ID and template exact and claims no file
- **Fail**: Turn 1 drafts any catalog content, misses the conflict or one of the five fields, or picks a send time itself, or the catalog gives `07:00 UTC` as the send time, blends the two times, alters a name, ID or template, invents an entry or rule, adds push notifications, writes `---` dividers or hyphen bullets, or the reply claims a local save

### Failure triage

1. Check the conflict gate in `Product Owner - Templates - Doc Mode` lines 160 to 164 and the recency rule in `Custom Instructions.md` line 132
2. Compare the block with the source-conflict hold template in `Product Owner - Assets - Doc Templates` line 711 and the Doc Context and Clarification Question in `Product Owner - Assets - Interactive Response Templates` line 106
3. Re-read the rendered catalog against both email sources, apply the user's designation only within its scope (`Product Owner - Templates - Doc Mode` line 151) and restore any name, ID, time or template that drifted

| Feature ID | Feature name | Scenario name / objective | Exact prompt | Exact command sequence | Expected signals | Evidence | Pass/fail criteria | Failure triage |
|---|---|---|---|---|---|---|---|---|
| PDK-004 | Catalog conflict gate | Verify the Project digest send time conflict stop and a catalog that follows the user's authority decision | `$doc Can you pull the six activity emails into one reference page? So far I have context/loomlist-notification-spec.md and context/loomlist-email-template-inventory.md, plus context/loomlist-context.md for background.` | 1. Stage and Canvas baseline -> 2. Submit Turn 1 fresh -> 3. Inspect the clarification and submit Turn 2 -> 4. Inspect the catalog block -> 5. Compare context/ | Step 2: conflict stop and one clarification block naming both times. Step 3: authority resolved. Step 4: catalog with the ClickUp layout, six exact entries, the spec's digest time and the label. Step 5: attachments unchanged | Both replies, rendered blocks, labels, conflict list, layout checks, entries, times and templates | PASS if the stop, the decision and the entries all match with no file claim. FAIL otherwise | 1. Check the conflict gate. 2. Check the clarification block. 3. Check times, names and templates in the rendered catalog |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy, Ticket realism rubric and root summary |
| [`Custom Instructions.md`](../../../claude%20project/Custom%20Instructions.md) | Project Doc intake minimum, authority order, Deliverable Block and export-equivalent contract |
| [`Product Owner - Templates - Doc Mode - v0.111.md`](../../../claude%20project/knowledge/Product%20Owner%20-%20Templates%20-%20Doc%20Mode%20-%20v0.111.md) | Project authority order, conflict gate, recency rule and ClickUp output contract |
| [`Product Owner - Assets - Doc Templates - v0.108.md`](../../../claude%20project/knowledge/Product%20Owner%20-%20Assets%20-%20Doc%20Templates%20-%20v0.108.md) | Project Catalog shape, the source-conflict hold template and layout rules |
| [`Product Owner - Assets - Interactive Response Templates - v0.103.md`](../../../claude%20project/knowledge/Product%20Owner%20-%20Assets%20-%20Interactive%20Response%20Templates%20-%20v0.103.md) | Project Doc Context and Clarification Question wording |
| [`loomlist-context.md`](../../../benchmark/fixtures/companies/loomlist/loomlist-context.md) | Attachment: Loomlist company context |
| [`loomlist-notification-spec.md`](../../../benchmark/fixtures/companies/loomlist/loomlist-notification-spec.md) | Attachment: the six emails with the digest at `08:00` in the recipient's local time |
| [`loomlist-email-template-inventory.md`](../../../benchmark/fixtures/companies/loomlist/loomlist-email-template-inventory.md) | Attachment: the six templates with the digest at `07:00 UTC` |
| [`PID-001`](../project-identity/identity-handover.md) | Runtime precondition and identity proof |

---

## 5. SOURCE METADATA

- Group: Project document modes
- Playbook ID: PDK-004
- Runtime: project
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `project-document-modes/catalog-conflict-gate.md`
