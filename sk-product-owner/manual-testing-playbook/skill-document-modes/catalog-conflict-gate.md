---
title: "SDK-004 -- Catalog conflict gate"
description: "Validates the Doc conflict gate at Loomlist, which stops on the digest send time conflict between two email sources, then a ClickUp catalog of the six activity emails that carries the value the user's chosen source gives."
version: 1.0.0.0
---

# SDK-004 -- Catalog conflict gate

This scenario validates source-conflict handling when two supplied sources disagree on one fact and neither declares authority, then a catalog built after the user settles it.

---

## 1. OVERVIEW

The command fixes Doc Mode. The two email sources agree on every entry but one. `context/loomlist-notification-spec.md` sends `EM-01`, the `Daily digest`, at `08:00` in the `recipient's local time`. `context/loomlist-email-template-inventory.md` sends it at `07:00 UTC`. Neither file calls itself canonical or the other outdated, and the inventory's later last-edited date settles nothing, because a newer timestamp is not an authority rule (`doc-mode.md` lines 158 and 188). So Turn 1 must stop composition (line 184), list the conflict under one consolidated question that also covers the other open fields, export that question and wait (`AGENTS.md` line 285, `doc-mode.md` line 529). Drafting a catalog, or choosing a time, is the primary failure.

Turn 2 designates the spec for the send time, the top of the authority order (`doc-mode.md` line 170), and the inventory for the template names, since each source's authority covers only its own scope (line 175). The catalog then carries `08:00` in the recipient's local time for `EM-01`.

### Why this matters

A catalog is where Support looks when a member asks why their digest came when it did. A silently chosen or blended send time turns one source's stale claim into the answer every agent repeats, which is exactly what the conflict gate exists to stop (`AGENTS.md` line 127).

---

## 2. SCENARIO CONTRACT

- Objective: Verify the conflict stop on the digest send time, the consolidated clarification export and a ClickUp catalog that follows the user's authority decision
- Real user request: `Can you pull the six activity emails into one reference page? So far I have context/loomlist-notification-spec.md and context/loomlist-email-template-inventory.md, plus context/loomlist-context.md for background.`
- Prompt: `$doc Can you pull the six activity emails into one reference page? So far I have context/loomlist-notification-spec.md and context/loomlist-email-template-inventory.md, plus context/loomlist-context.md for background.`
- Attachments: [loomlist-context.md](../../../benchmark/fixtures/companies/loomlist/loomlist-context.md), [loomlist-notification-spec.md](../../../benchmark/fixtures/companies/loomlist/loomlist-notification-spec.md), [loomlist-email-template-inventory.md](../../../benchmark/fixtures/companies/loomlist/loomlist-email-template-inventory.md)
- Runtime profile: skill, from `AGENTS.md` with `SKILL.md` and the `sk-product-owner/` resources loaded
- Precondition: `SID-001` identity handover passed in the skill runtime before this scenario starts, and the three attachments sit unchanged at `context/loomlist-context.md`, `context/loomlist-notification-spec.md` and `context/loomlist-email-template-inventory.md` before the export baseline (root, Company context and attachments)
- Expected execution process: Start fresh, submit Turn 1, inspect the clarification export, resolve authority in Turn 2, then inspect the next doc export and compare `context/` with its baseline
- Expected signals: Turn 1 lists the `EM-01` send time conflict with both values and both sources, asks one consolidated question that also covers source set, status, shape and scope, exports `export/[###] - doc-activity-emails-clarification.md`, reads it back and replies with its path, the `Verified: read-back succeeded` line with its line count and the `HVR self-scan:` line (root section 5, Clarification turns), and creates no draft. Turn 2 saves `export/[###] - doc-activity-emails.md` on the next number as a Catalog, reads it back and replies with the path, the `Verified:` line, the `HVR self-scan:` line and one summary line each for Source safety, Shape fit, ClickUp layout, Readability and Voice (`doc-mode.md` line 412). The three `context/` files stay byte for byte unchanged
- Desired user-visible outcome: A clarification export that names the conflict, then one catalog of the six activity emails after the user says which source governs
- Size band (advisory): 80 to 180 lines in the doc body. Recorded only, never a Pass or Fail input (root section 5, Ticket realism)
- Pass/fail: PASS if Turn 1 stops with no catalog content, lists the `EM-01` conflict as `08:00` in the recipient's local time from the spec against `07:00 UTC` from the inventory, asks which source governs it, covers source set, status, shape and scope in the same question, settles nothing itself and exports the question in the doc lane with a read-back, and Turn 2 delivers a Catalog with an Overview and one entry per email under a category body, `* * *` directly under every content heading, `*   ` bullets, sentence-case headings and no empty spacer heading in the file, entries `EM-01` to `EM-06` named `Daily digest`, `Mentioned in a page`, `Comment reply`, `Page shared with you`, `Workspace invite` and `Weekly summary`, `EM-01` at `08:00` in the recipient's local time, `EM-06` at `Monday 09:00` in the recipient's local time, the templates `tpl_digest_v4`, `tpl_mention_v2`, `tpl_comment_reply_v2`, `tpl_page_shared_v3`, `tpl_workspace_invite_v5` and `tpl_weekly_summary_v1` on their own entries, no push notification entry, and nothing the three attachments do not state. FAIL if Turn 1 drafts any part of the catalog, leaves the conflict or any of the five fields out, or picks a send time itself, by the newer last-edited date or any other signal, or Turn 2 gives `07:00 UTC` as the digest send time, blends the two times, alters a name, ID or template, invents an entry or rule, or writes `---` dividers or hyphen bullets
- Record `SKIP` only when a named sandbox or runtime blocker prevents execution, never for a soft or inconclusive result

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `$doc Can you pull the six activity emails into one reference page? So far I have context/loomlist-notification-spec.md and context/loomlist-email-template-inventory.md, plus context/loomlist-context.md for background.` | Read the three attachments, detect the `EM-01` send time conflict, stop composition, export one consolidated question that lists both claims with their sources and asks which governs, together with source set, status, shape, scope and the purpose and audience the request left open, read it back and wait. Create no draft | Both sources are named and neither send time is promoted ahead of the user's decision, all three `context/` files unchanged | Turn 1 reply, clarification export, read-back line and clean draft ledger |
| 2 | `A catalog for Support agents and the Notifications engineers. On the send time the spec is right, the digest goes at 08:00 in the recipient's local time and the 07:00 UTC in the inventory is stale. Take the template names from the inventory, use only these three files, describe current behavior and leave push notifications out.` | Build the catalog with the spec governing timing and the inventory governing template names, one entry per email with its ID, name, trigger, timing, template and switch rule, `EM-01` at `08:00` in the recipient's local time, any mention of `07:00 UTC` marked stale, apply the ClickUp layout, save the next doc export, read it back and reply with the path, the `Verified:` line, the `HVR self-scan:` line and the five-line Doc summary | The authority decision holds within its scope, and no entry carries the stale time as current | Turn 2 reply, exported catalog and read-back line |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$doc Can you pull the six activity emails into one reference page? So far I have context/loomlist-notification-spec.md and context/loomlist-email-template-inventory.md, plus context/loomlist-context.md for background.`

### Commands

1. `sandbox: stage the three attachments in context/ -> filesystem: record the export and context/ baselines`
2. `session: start fresh -> user: submit Turn 1 exactly`
3. `filesystem: open the clarification export -> operator: confirm it lists the send time conflict, covers the five Doc fields and holds no catalog content -> user: submit Turn 2 in the same session`
4. `filesystem: open the new doc export -> operator: check the shape, the ClickUp layout, the six entries, the digest time and the template names against both email sources`
5. `filesystem: compare context/ with its baseline`

### Expected

Step 1 fixes both baselines. Step 2 stops the draft and produces one clarification file in the doc lane that names the conflict and both sources, much as the source-conflict hold template lays it out (`doc-templates.md` lines 732 and 744). Step 3 proves the question-only file and captures the authority decision. Step 4 finds a Catalog with an Overview and one entry per email under a category body (`doc-templates.md` lines 115, 288 and 290), `* * *` directly under each content heading, `*   ` bullets, sentence-case headings where an email name keeps its own capitals, and no empty spacer heading, since a file export never carries one (`doc-mode.md` line 97). `EM-01` reads `08:00` in the recipient's local time, and `07:00 UTC` appears nowhere as its send time. `EM-06` reads `Monday 09:00` in the recipient's local time, each template sits on its own entry and any rule the catalog repeats, such as `Settings > Notifications` or `EM-05` having no off switch, keeps the sources' wording. Step 5 finds the three attachments unchanged.

### Evidence

Capture both replies, the side-effect ledger, both export paths and read-back lines, the conflict list, the fields the question covers, the authority decision, the doc headings with divider adjacency, the bullet markers, the six entries with their times and templates, the Doc quality summary and the `context/` comparison.

### Pass / fail

- **Pass**: Turn 1 stops with one question-only clarification that lists the `08:00` against `07:00 UTC` conflict with both sources and covers source set, status, shape and scope, read back with no early draft, and the catalog carries an Overview and six entries, passes the ClickUp layout gate, gives `EM-01` the spec's `08:00` in the recipient's local time and keeps every name, ID and template exact
- **Fail**: Turn 1 drafts any catalog content, misses the conflict or one of the five fields, or picks a send time itself, or the catalog gives `07:00 UTC` as the send time, blends the two times, alters a name, ID or template, invents an entry or rule, adds push notifications, or writes `---` dividers, hyphen bullets or empty spacer headings into the file

### Failure triage

1. Check the conflict gate in `doc-mode.md` lines 184 to 188 and the rule that a newer timestamp is not authority (`doc-mode.md` line 158)
2. Compare the question with the source-conflict hold template in `doc-templates.md` line 732 and the Doc Context and Clarification Question in `interactive-response-templates.md` line 129
3. Re-read the catalog against both email sources, apply the user's designation only within its scope (`doc-mode.md` line 175) and restore any name, ID, time or template that drifted

| Feature ID | Feature name | Scenario name / objective | Exact prompt | Exact command sequence | Expected signals | Evidence | Pass/fail criteria | Failure triage |
|---|---|---|---|---|---|---|---|---|
| SDK-004 | Catalog conflict gate | Verify the digest send time conflict stop and a catalog that follows the user's authority decision | `$doc Can you pull the six activity emails into one reference page? So far I have context/loomlist-notification-spec.md and context/loomlist-email-template-inventory.md, plus context/loomlist-context.md for background.` | 1. Stage and baseline -> 2. Submit Turn 1 fresh -> 3. Inspect the clarification and submit Turn 2 -> 4. Inspect the doc export -> 5. Compare context/ | Step 2: conflict stop and one clarification naming both times. Step 3: authority resolved. Step 4: catalog with the ClickUp layout, six exact entries and the spec's digest time. Step 5: attachments unchanged | Both replies, ledger, export paths, read-back lines, conflict list, layout checks, entries, times and templates | PASS if the stop, the decision and the entries all match. FAIL otherwise | 1. Check the conflict gate. 2. Check the clarification. 3. Check times, names and templates in the export |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy, Ticket realism rubric and root summary |
| [`AGENTS.md`](../../../AGENTS.md) | The Doc escalation question, the conflict stop and the export protocol |
| [`doc-mode.md`](../../references/doc-mode.md) | Authority order, conflict gate, recency rule and ClickUp output contract |
| [`doc-templates.md`](../../assets/doc-templates.md) | Catalog shape, the source-conflict hold template and layout rules |
| [`interactive-response-templates.md`](../../assets/interactive-response-templates.md) | Doc Context and Clarification Question wording |
| [`loomlist-context.md`](../../../benchmark/fixtures/companies/loomlist/loomlist-context.md) | Attachment: Loomlist company context |
| [`loomlist-notification-spec.md`](../../../benchmark/fixtures/companies/loomlist/loomlist-notification-spec.md) | Attachment: the six emails with the digest at `08:00` in the recipient's local time |
| [`loomlist-email-template-inventory.md`](../../../benchmark/fixtures/companies/loomlist/loomlist-email-template-inventory.md) | Attachment: the six templates with the digest at `07:00 UTC` |
| [`SID-001`](../skill-identity/identity-handover.md) | Runtime precondition and identity proof |

---

## 5. SOURCE METADATA

- Group: Skill document modes
- Playbook ID: SDK-004
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `skill-document-modes/catalog-conflict-gate.md`
