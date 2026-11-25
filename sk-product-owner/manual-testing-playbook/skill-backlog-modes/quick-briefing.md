---
title: "SBR-003 -- Quick briefing"
description: "Validates that `$quick $briefing` skips intake and delivers one small briefing inside the indicator scope."
version: 1.0.0.0
---

# SBR-003 -- Quick briefing

This scenario runs a Loomlist `$quick $briefing` request for the offline indicator and checks that intake is skipped and the scope stays small.

---

## 1. OVERVIEW

A Mobile Platform PM asks with `$quick $briefing` for the offline indicator alone, from the offline mode epic brief. The brief covers reading, editing, sync on reconnect and a storage screen as well, and it leaves the conflict decision with Joana until 2026-10-09. The runtime should read Quick as an energy and `$briefing` as the artifact, skip routine intake and deliver the one small briefing the request names.

### Why this matters

A Quick briefing is the shortest valid one, and the risk is the briefing growing back into the whole epic. The marker and the waiting count are one design question. The storage screen, the 500 page cap and the sync timing belong to other work.

---

## 2. SCENARIO CONTRACT

- Objective: Verify that `$quick $briefing` skips routine intake and exports one small briefing for the indicator alone with no unrequested scope and no invented number
- Real user request: `$quick $briefing The offline marker and the count of waiting changes in the Desktop top bar, from Oskar's offline brief in context/loomlist-offline-mode-brief.md. Product context is in context/loomlist-context.md.`
- Prompt: `$quick $briefing The offline marker and the count of waiting changes in the Desktop top bar, from Oskar's offline brief in context/loomlist-offline-mode-brief.md. Product context is in context/loomlist-context.md.`
- Attachments: [loomlist-context.md](../../../benchmark/fixtures/companies/loomlist/loomlist-context.md), [loomlist-offline-mode-brief.md](../../../benchmark/fixtures/companies/loomlist/loomlist-offline-mode-brief.md)
- Runtime profile: skill, from `AGENTS.md` with `SKILL.md` and the `sk-product-owner/` resources loaded
- Precondition: `SID-001` identity handover passed in the skill runtime before this scenario starts, and both attachments sit at `context/<basename>` before the export baseline is recorded
- Expected execution process: Start fresh, submit Turn 1 and inspect the briefing export on the first number
- Expected signals: Quick is an energy and `$briefing` the artifact, so routine intake is skipped (`references/briefing-mode.md` lines 43 and 79, `references/interactive-mode.md` line 299). The title follows the briefing form (`references/briefing-mode.md` line 102). Core sections, audiences and facets follow `references/briefing-mode.md` lines 103 to 106 and the scaffold in `assets/design-briefing-template.md` lines 46 to 115. The title reads `Briefing - ` with no team lead and names the area in full, such as `Briefing - Desktop - Offline Mode - Offline Indicator`. The briefing holds the three core sections `## About`, `## Briefing` and `## Requirements` as H2 with a `* * *` divider directly under every heading and nowhere else. Every other section is removed whole unless the brief supports it. There is one audience, so Requirements carries no audience heading and starts on its first facet, with at least two facets such as `**Display**` and `**Visibility**`, each holding `- []` items a design review can tick. The briefing covers the marker in the top bar and the count of changes waiting to sync, and no storage screen, no offline reading rule and no sync timing. It writes no number, range or threshold for the marker that the brief does not give. A decision the brief leaves open, such as how conflicting edits are handled, appears only under `## Open Questions` with Joana named, or in the reply under Open items. The briefing carries no table and no bullet ending in a full stop
- Desired user-visible outcome: One small briefing for the offline marker and the waiting changes count, saved and read back with no question asked first
- Size band (advisory): 20 to 50 lines of briefing body
- Pass/fail: PASS if one briefing is saved on the first number with no question asked first, read back and reported path first with the `Verified:` line and the `HVR self-scan:` line, and it holds the three core sections, a single audience with at least two facets of `- []` items, stays inside the indicator scope and writes no number the brief does not give for the marker. FAIL if it asks the intake question first, saves a clarification, adds the storage screen, the 500 page cap, the 1 GB cap or the sync timing as scope, writes a threshold for when the marker shows, leads the title with a team or writes a table
- Record `SKIP` only when a named sandbox or runtime blocker prevents execution, never for a soft or inconclusive result

### Conversation chain

| Turn | Exact user input | Expected assistant behavior | State check | Evidence |
|---|---|---|---|---|
| 1 | `$quick $briefing The offline marker and the count of waiting changes in the Desktop top bar, from Oskar's offline brief in context/loomlist-offline-mode-brief.md. Product context is in context/loomlist-context.md.` | Read `$quick` as energy and `$briefing` as the artifact, read both attachments, skip routine intake, save one small briefing on the first number, read it back and reply path first with the `Verified:` line and the `HVR self-scan:` line | Briefing intent with Quick energy, the Desktop surface and the indicator scope stay selected | Briefing export, read-back line and the ledger holding only that export |

---

## 3. TEST EXECUTION

### Prompt

- Prompt: `$quick $briefing The offline marker and the count of waiting changes in the Desktop top bar, from Oskar's offline brief in context/loomlist-offline-mode-brief.md. Product context is in context/loomlist-context.md.`

### Commands

1. `sandbox: stage both attachments at context/ -> filesystem: record the export folder baseline`
2. `session: start fresh -> user: submit Turn 1 exactly`
3. `filesystem: open the briefing export -> operator: check the title, the sections, the facets and the scope against the request and the brief`

### Expected

Step 1 fixes the baseline with `context/` holding the two attachments. Step 2 returns one briefing on the first number with no question. Step 3 finds the three core sections, a single audience, at least two facets and no scope beyond the indicator.

### Evidence

Capture the reply, the side-effect ledger, the export path and read-back line, and the sections and facets of the briefing.

### Pass / fail

- **Pass**: One small briefing with no question first, the three core sections, one audience, at least two facets and no scope beyond the indicator
- **Fail**: The runtime asks first, widens the scope past the indicator or writes a number the brief does not give for the marker

### Failure triage

1. Check how Quick narrows intake in `briefing-mode.md` and `interactive-mode.md`
2. Check the title, section and facet rules in `briefing-mode.md` and the scaffold in `design-briefing-template.md`
3. Remove any scope the request did not name and any number the brief does not give for the indicator

| Feature ID | Feature name | Scenario name / objective | Exact prompt | Exact command sequence | Expected signals | Evidence | Pass/fail criteria | Failure triage |
|---|---|---|---|---|---|---|---|---|
| SBR-003 | Quick briefing | Verify `$quick $briefing` skips routine intake and exports one small briefing for the indicator alone with no unrequested scope and no invented number | `$quick $briefing The offline marker and the count of waiting changes in the Desktop top bar, from Oskar's offline brief in context/loomlist-offline-mode-brief.md. Product context is in context/loomlist-context.md.` | 1. Stage and baseline -> 2. Submit Turn 1 fresh -> 3. Inspect the briefing | Step 2: briefing saved with no question. Step 3: three core sections, one audience, indicator scope only | the reply, the side-effect ledger, the export path and read-back line, and the sections and facets of the briefing | PASS if no question is asked and the briefing stays in scope. FAIL otherwise | 1. Check how Quick narrows intake. 2. Check the title, section and facet rules. 3. Remove any scope the request did not name and any number the brief does not give for the indicator |

---

## 4. SOURCE FILES

| File | Role |
|---|---|
| [Root playbook](../manual-testing-playbook.md) | Shared execution policy, Ticket realism rubric and root summary |
| [`AGENTS.md`](../../../AGENTS.md) | Line 84 clarification export, line 98 briefing file name, line 129 briefing title, line 340 explicit commands ask first |
| [`briefing-mode.md`](../../references/briefing-mode.md) | Line 54 critical rules, line 102 title, lines 103 to 106 sections, audiences and facets, line 109 source wording, line 115 spacing, line 83 build work stays Task |
| [`design-briefing-template.md`](../../assets/design-briefing-template.md) | Lines 46 to 115 briefing scaffold and its notes for use |
| [`interactive-mode.md`](../../references/interactive-mode.md) | Line 299 Briefing Mode entry and flow |
| [`interactive-response-templates.md`](../../assets/interactive-response-templates.md) | Line 111 briefing context question |
| [`routing.md`](../../references/routing.md) | Line 34 artifact framing without a command |
| [loomlist-context.md](../../../benchmark/fixtures/companies/loomlist/loomlist-context.md) | Company context |
| [loomlist-offline-mode-brief.md](../../../benchmark/fixtures/companies/loomlist/loomlist-offline-mode-brief.md) | The source the request names |
| [`SID-001`](../skill-identity/identity-handover.md) | Runtime precondition and identity proof |

---

## 5. SOURCE METADATA

- Group: Skill backlog modes
- Playbook ID: SBR-003
- Runtime: skill
- Canonical root source: `../manual-testing-playbook.md`
- Feature file path: `skill-backlog-modes/quick-briefing.md`
