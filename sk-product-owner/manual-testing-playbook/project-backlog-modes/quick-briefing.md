---
title: "PBR-003 -- Quick briefing"
description: "Validates that `$quick $briefing` skips intake and renders one small briefing inside the indicator scope."
version: 1.0.0.0
---

# PBR-003 -- Quick briefing

This scenario runs a Loomlist `$quick $briefing` request for the offline indicator and checks that intake is skipped and the scope stays small.

---

## 1. OVERVIEW

A Mobile Platform PM asks with `$quick $briefing` for the offline indicator alone, from the offline mode epic brief. The brief covers reading, editing, sync on reconnect and a storage screen as well, and it leaves the conflict decision with Joana until 2026-10-09. The runtime should read Quick as an energy and `$briefing` as the artifact, skip routine intake and deliver the one small briefing the request names.

### Why this matters

A Quick briefing is the shortest valid one, and the risk is the briefing growing back into the whole epic. The marker and the waiting count are one design question. The storage screen, the 500 page cap and the sync timing belong to other work.

---

## 2. SCENARIO CONTRACT

- Objective: Verify that `$quick $briefing` skips routine intake and renders one small briefing for the indicator alone with no unrequested scope and no invented number
- Real user request: `$quick $briefing The offline marker and the count of waiting changes in the Desktop top bar, from Oskar's offline brief in context/loomlist-offline-mode-brief.md. Product context is in context/loomlist-context.md.`
- Prompt: `$quick $briefing The offline marker and the count of waiting changes in the Desktop top bar, from Oskar's offline brief in context/loomlist-offline-mode-brief.md. Product context is in context/loomlist-context.md.`
- Attachments: [loomlist-context.md](../../../benchmark/fixtures/companies/loomlist/loomlist-context.md), [loomlist-offline-mode-brief.md](../../../benchmark/fixtures/companies/loomlist/loomlist-offline-mode-brief.md)
- Runtime profile: project, from `Custom Instructions.md` with the full `claude project/knowledge/` set attached
- Precondition: `PID-001` identity handover passed in the project runtime before this scenario starts, and both attachments sit at `context/<basename>` before the Canvas panel baseline is recorded
- Expected execution process: Start a fresh Project conversation, submit Turn 1 and inspect the rendered briefing
- Expected signals: Quick is an energy and `$briefing` the artifact, so routine intake is skipped (`Product Owner - Templates - Briefing Mode.md` line 34, `Product Owner - System - Interactive Mode.md` line 276). The title follows the briefing form (`Product Owner - Templates - Briefing Mode.md` line 82). Audiences and facets follow lines 85 and 86 of that file and the scaffold in `Product Owner - Assets - Design Briefing Template.md` lines 27 to 96. The title reads `Briefing - ` with no team lead and names the area in full, such as `Briefing - Desktop - Offline Mode - Offline Indicator`. The briefing holds the three core sections `## About`, `## Briefing` and `## Requirements` as H2 with a `* * *` divider directly under every heading and nowhere else. Every other section is removed whole unless the brief supports it. There is one audience, so Requirements carries no audience heading and starts on its first facet, with at least two facets such as `**Display**` and `**Visibility**`, each holding `- []` items a design review can tick. The briefing covers the marker in the top bar and the count of changes waiting to sync, and no storage screen, no offline reading rule and no sync timing. It writes no number, range or threshold for the marker that the brief does not give. A decision the brief leaves open, such as how conflicting edits are handled, appears only under `## Open Questions` with Joana named, or in the reply under Open items. The briefing carries no table and no bullet ending in a full stop
- Desired user-visible outcome: One small briefing for the offline marker and the waiting changes count, rendered with no question asked first
- Size band (advisory): 20 to 50 lines of briefing body
- Pass/fail: PASS if one briefing renders as its Deliverable Block with its `Export-equivalent path:` and the `HVR self-scan:` line, with no question asked first and no file claimed, and it holds the three core sections, a single audience with at least two facets of `- []` items, stays inside the indicator scope and writes no number the brief does not give for the marker. FAIL if it asks the intake question first, saves a clarification, adds the storage screen, the 500 page cap, the 1 GB cap or the sync timing as scope, writes a threshold for when the marker shows, leads the title with a team or writes a table. A claim of a local save also fails
- Record `SKIP` only when a named sandbox or runtime blocker prevents execution, never for a soft or inconclusive result

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `$quick $briefing The offline marker and the count of waiting changes in the Desktop top bar, from Oskar's offline brief in context/loomlist-offline-mode-brief.md. Product context is in context/loomlist-context.md.` | Read `$quick` as energy and `$briefing` as the artifact, read both attachments, skip routine intake, render one small briefing as its Deliverable Block with its export-equivalent label and the `HVR self-scan:` line, and claim no file | Briefing intent with Quick energy, the Desktop surface and the indicator scope stay selected | Rendered briefing block, its label and the no-file-write statement |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$quick $briefing The offline marker and the count of waiting changes in the Desktop top bar, from Oskar's offline brief in context/loomlist-offline-mode-brief.md. Product context is in context/loomlist-context.md.`

### Commands

1. `sandbox: stage both attachments at context/ -> canvas: record the Canvas panel baseline`
2. `session: start a fresh Project conversation -> user: submit Turn 1 exactly`
3. `canvas: inspect the rendered briefing -> operator: check the title, the sections, the facets and the scope against the request and the brief`

### Expected

Step 1 fixes the baseline with `context/` holding the two attachments. Step 2 returns one briefing block with no question. Step 3 finds the three core sections, a single audience, at least two facets and no scope beyond the indicator.

### Evidence

Capture the reply, the rendered block and its export-equivalent label, and the sections and facets of the briefing.

### Pass / fail

- **Pass**: One small briefing with no question first, the three core sections, one audience, at least two facets and no scope beyond the indicator, and no file claim
- **Fail**: The runtime asks first, widens the scope past the indicator or writes a number the brief does not give for the marker, or claims a local save

### Failure triage

1. Check how Quick narrows intake in `Product Owner - Templates - Briefing Mode` and `Product Owner - System - Interactive Mode`
2. Check the title, section and facet rules in `Product Owner - Templates - Briefing Mode` and the scaffold in `Product Owner - Assets - Design Briefing Template`
3. Remove any scope the request did not name and any number the brief does not give for the indicator

| Feature ID | Feature name | Scenario name / objective | Exact prompt | Exact command sequence | Expected signals | Evidence | Pass/fail criteria | Failure triage |
|---|---|---|---|---|---|---|---|---|
| PBR-003 | Quick briefing | Verify `$quick $briefing` skips routine intake and renders one small briefing for the indicator alone with no unrequested scope and no invented number | `$quick $briefing The offline marker and the count of waiting changes in the Desktop top bar, from Oskar's offline brief in context/loomlist-offline-mode-brief.md. Product context is in context/loomlist-context.md.` | 1. Stage and baseline -> 2. Submit Turn 1 fresh -> 3. Inspect the briefing | Step 2: briefing rendered with no question. Step 3: three core sections, one audience, indicator scope only | the reply, the rendered block and its export-equivalent label, and the sections and facets of the briefing | PASS if no question is asked and the briefing stays in scope. FAIL otherwise | 1. Check how Quick narrows intake. 2. Check the title, section and facet rules. 3. Remove any scope the request did not name and any number the brief does not give for the indicator |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy, Ticket realism rubric and root summary |
| [`Custom Instructions.md`](../../../claude%20project/Custom%20Instructions.md) | Line 92 briefing route, line 83 explicit commands ask first, line 69 title rule, line 259 clarification label, line 253 briefing label |
| [`Product Owner - Templates - Briefing Mode.md`](../../../claude%20project/knowledge/Product%20Owner%20-%20Templates%20-%20Briefing%20Mode.md) | Line 34 critical rules, line 82 title, lines 85 and 86 audiences and facets, line 89 source wording, line 95 spacing, line 63 build work stays Task |
| [`Product Owner - Assets - Design Briefing Template.md`](../../../claude%20project/knowledge/Product%20Owner%20-%20Assets%20-%20Design%20Briefing%20Template.md) | Lines 27 to 96 briefing scaffold and its notes for use |
| [`Product Owner - System - Interactive Mode.md`](../../../claude%20project/knowledge/Product%20Owner%20-%20System%20-%20Interactive%20Mode.md) | Line 276 Briefing Mode entry and flow |
| [`Product Owner - Assets - Interactive Response Templates.md`](../../../claude%20project/knowledge/Product%20Owner%20-%20Assets%20-%20Interactive%20Response%20Templates.md) | Line 87 briefing context question |
| [loomlist-context.md](../../../benchmark/fixtures/companies/loomlist/loomlist-context.md) | Company context |
| [loomlist-offline-mode-brief.md](../../../benchmark/fixtures/companies/loomlist/loomlist-offline-mode-brief.md) | The source the request names |
| [`PID-001`](../project-identity/identity-handover.md) | Runtime precondition and identity proof |

---

## 5. SOURCE METADATA

- Group: Project backlog modes
- Playbook ID: PBR-003
- Runtime: project
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `project-backlog-modes/quick-briefing.md`
