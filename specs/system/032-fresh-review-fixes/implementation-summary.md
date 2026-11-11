---
title: "Implementation Summary"
description: "Fixes the chosen findings of a fresh review, adds three gates, redacts private identifiers from the tracked files and repairs the upstream checker items in Skilled."
trigger_phrases:
  - "fresh review fixes implementation summary"
importance_tier: "normal"
contextType: "general"
_memory:
  continuity:
    packet_pointer: "system/032-fresh-review-fixes"
    last_updated_at: "2026-11-11T17:00:00Z"
    last_updated_by: "generate-context"
    recent_action: "Completed the FigJam file map and released hub 1.0.33.0 with sk-create-figjam 1.0.20.0"
    next_safe_action: "Paste kernel v1.2.21 into the Claude Project"
    blockers: []
    key_files:
      - "benchmark/gates/check_identifiers.py"
      - "benchmark/gates/run_gates.sh"
      - "sk-product-owner/assets/doc-templates.md"
      - "claude project/Custom Instructions.md"
    session_dedup:
      fingerprint: "sha256:eaf3fb2ddc5d99133e307f268af4e59c39f3579257feb9e8d6707847b04f41ec"
      session_id: "77e809ab-7e4a-4669-a9c5-ee0fa5f7617b"
      parent_session_id: null
    completion_pct: 100
    open_questions:
      - "Should a live model benchmark run on the simplified instruction files?"
      - "Should the shared Conciseness card drop its Doc spacer example?"
      - "Should the grader read Sections 6 and 7 of the voice card?"
    answered_questions: []
---
<!-- SPECKIT_TEMPLATE_SOURCE: impl-summary-core | v2.4 -->
# Implementation Summary

<!-- SPECKIT_LEVEL: 1 -->
<!-- HVR_REFERENCE: .skilled/skills/sk-doc/sk-create-with-human-voice/references/hvr-rules.md -->

---

<!-- ANCHOR:metadata -->
## Metadata

| Field | Value |
|-------|-------|
| **Spec Folder** | 032-fresh-review-fixes |
| **Completed** | 2026-11-11 |
| **Level** | 1 |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:what-built -->
## What Was Built

A fresh Fable 5.2 review read the whole system with no prior context. Michel chose the finding groups to fix through the question tool. Every chosen finding is fixed, apart from one proposal that was judged and declined.

### Skill docs and the Project mirror

The Doc scaffolds taught an em dash and a semicolon the format gate blocks. Six em dashes and three semicolons are gone, three more than the review listed, because the Catalog scaffold carried them on its stable-ID placeholders. Spacer headings now stay in a Doc file export, as Michel decided, which matches the Story rule and the 42 spacers in the Doc examples. The feedback ticket path reads `export/{feature}/[###] - feedback-{app}-{kind}.md` with lowercase slugs and the kind `logic` or `ui-ux`. The feedback example obeys one ticket, one kind. The Flow reply and the Mark-as-done divider rule are each stated once and pointed at from the other files. `AGENTS.md` is 240 words shorter. Eight knowledge files and four kernel passages follow by hand, in kernel v1.2.20.

### Gates

`run_gates.sh` holds 19 gates, up from 15. The source format lint runs the validator on the skill files, which only the fixtures exercised before. The example lint reads 44 fenced scaffold blocks. The identifier scan fails on a ClickUp workspace id, a company email, a Figma team id or a home path in any tracked file, and prints the file, line and rule, never the value. The hub keyword check matches a `$` keyword as a whole token, so `$document` and eleven look-alikes score no intent. The grader reads its word lists from the voice card.

### Redaction

One script replaced the identifiers in 2,132 tracked files under `specs/` and `benchmark/reports/`. The account name sat in home paths, in encoded folder names and in `ls -l` owner columns, 14,165 places in all. The work email had 2, the Figma team ids 12 and the workspace id 7. The public GitHub account names and the profile link are kept. The four vendored files that held the workspace id were fixed in Skilled and pulled.

### Vendor script

A malformed `vendor.json` is a setup error with a one-line message and exit 2. It was a traceback and exit 1.

### Skilled

Three sk-doc checkers work on a repository that vendors Skilled packets. The playbook validator takes a foreign `--repo-root`. The README reference checker reads a line citation and a path with a space as the file. Catalog discovery skips record trees. The `mcp-code-mode` playbook meets its package contract. The alignment command says why a scope is empty.

### Backlog titles

Michel showed his ClickUp lists and 146 file names as the model. `AGENTS.md` now states one title rule: a title is a label, never a sentence, built from segments joined by ` - ` and running from broad to specific. A Task, Subtask or Bug leads with the team (`FE`, `BE`, `FS`, `DATA` or `DS`). A Story and a Parent task lead with the app. An Epic keeps its `Epic - ` lead and a Bug takes no `BUG` lead. When the source names no team, the one clarification question asks for it, and under `$quick` the lead is left out and listed under Open items. No title carries a date. The eight task and bug examples are renamed to the form. The rule sits in `AGENTS.md` because `sk-product-owner/SKILL.md` has a 5,000-word cap and 50 words of room.

### Sectioned Story shape

Two Stories Michel supplied became the model for a second Story shape. A large Story may write Problem and Solution as lists, split Requirements into numbered `###` sections that each open on a User flow line, and place design links at the top of a section. These are options that scale with scope and length, and the compact shape stays the default. A source covering Desktop and Mobile with differing requirements becomes one sibling Story per platform. A new worked example shows the shape on a fictional thermostat app. The `Checklist` label and nested checklist items stay banned, as Michel chose.

### Title check and alignment follow-up

A hand-run of the sk-doc checkers after the release found three things, and all are fixed. The grader README has the README heading shape. The vendored `mcp-figma` playbook no longer links into a skill this repository does not vendor, fixed upstream as v1.2.3.0 and pulled. The Skilled README reference checker reads a path written from the repository root, which took the false flags here from 72 to 31 and left all 1,005 Skilled READMEs unchanged.

The output format gate now reads the title of a backlog artifact. It reports a sentence title, a closing full stop, a leading date or a `BUG` lead as one advisory line. The check sits in this repository's validator and in the shared Sync Loop core, gated by a `titleShape` key in `systems.cjs`, and the two print byte-identical output. Twelve playbook overviews now say the title rule asks for the team lead. Hub 1.0.32.0.

### README accuracy pass

Every README this repository owns was checked against the tree, the root one by hand and the benchmark, scripts and FigJam ones by three read-only DeepSeek V4.1 Flash batches whose findings were each confirmed before an edit. The root README gained the feedback ticket path, the title rule, the sectioned Story shape and five missing entries in its tree, and its FigJam example count reads 8. `benchmark/gates/README.md` had 12 stale values: the hub self-test plants thirteen defects, rule parity reads 68 pairs and ten cited source lines had moved. `benchmark/router/README.md` now names `$flow` and `$figjam`, the quick-fallback confidence, the prose-table guard and the packet `ROUTER.md` as the home of the type table. `USER-GUIDE.md` covers feedback tickets and the team question for titles.

### FigJam file map

The Section 3 file map in `sk-create-figjam/SKILL.md` gained rows for `ROUTER.md`, `assets/screenshots/` and `manual-testing-playbook/`. The packet README dropped the sentence that named them as missing, and the screenshots README carries the packet version. This released `sk-create-figjam` 1.0.20.0 and hub 1.0.33.0. No Project file changes, because the map describes the repository folder.

### Finding outcomes

| Finding | Outcome |
|---------|---------|
| F1, F3, F5, F12, F13, F14, F15 | Fixed in the skill docs and the mirror |
| F2 | Fixed: the source format lint is a gate |
| F4 | Fixed in the tracked files, with a gate that keeps it fixed |
| F8, S1 | Fixed as narrowed. The Skilled hub contract requires the keyword block, so the check now matches whole tokens |
| F11 | Fixed with four tests |
| S2, S3, S5, S6 | Done |
| S4 | Declined. The Sync Loop declares the Task Mode tail as moved out of the kernel on purpose, and moving it back adds about 350 words to every Project turn |
| F6, F7, F9, F10 | Not chosen |

### Files Changed

| File | Action | Purpose |
|------|--------|---------|
| `sk-product-owner/` docs, `AGENTS.md`, `README.md` | Modify | Scaffolds, spacer rule, feedback path, counts, restated rules |
| `sk-create-figjam/references/flow-mode.md` | Modify | The Flow reply sentence names its `Finding:` line |
| `claude project/Custom Instructions.md`, eight knowledge files, `claude project/README.md` | Modify | Kernel v1.2.20 and the hand-written mirror |
| `benchmark/gates/run_gates.sh`, `example_lint.py`, `check_leaf_map_parity.py`, `rule_parity.py`, READMEs | Modify | Four new gate rows, scaffold lint, whole-token match |
| `benchmark/gates/check_identifiers.py` | Create | The identifier scan |
| `benchmark/grader/hvr_lint.py`, `lint_replies.py`, `README.md` | Modify | Word lists read from the card |
| `scripts/vendor-sync.py`, `scripts/tests/test_vendor_sync.py` | Modify | Exit 2 on a malformed manifest |
| `ROUTER.md` | Modify | The keyword block is a phrase hint, not a command matcher |
| `specs/`, `benchmark/reports/` | Modify | Redaction in 2,132 files |
| `mcp-click-up/`, `mcp-code-mode/`, `mcp-chrome-devtools/`, `vendor.json` | Modify | Vendor pulls |
| Sync Loop `systems.py` | Modify | Five residency statements follow the kernel |
| Version files, three changelogs, `SYNC.md` | Modify and Create | Release 1.0.30.0, 1.2.17.0 and 1.0.19.0 |
| Skilled sk-doc scripts, `mcp-code-mode` playbook, `mcp-click-up` docs, seven changelogs | Modify and Create | Upstream items |
| `AGENTS.md`, `task-mode.md`, `bug-mode.md`, `story-mode.md`, three scaffolds, eight examples, the playbook root | Modify | The title rule and the renamed examples |
| `story-template.md`, `story-example-sectioned.md`, `leaf-manifest.json` | Modify and Create | The sectioned Story shape |
| Kernel v1.2.21, sixteen knowledge files, Sync Loop `systems.py` | Modify and Create | Mirror, one new pair and three residency statements |
| Version files and two changelogs | Modify and Create | Release 1.0.31.0 and 1.2.18.0 |
<!-- /ANCHOR:what-built -->

---

<!-- ANCHOR:how-delivered -->
## How It Was Delivered

Three workers fixed separate file sets at once: the skill docs with their mirror, the gates and scripts, and Skilled. The redaction ran as one script with a dry run first and a second run to confirm zero matches. Each new gate was shown red on a scratch copy with a planted fault before it was trusted. The Skilled change was committed and published, then pulled with `vendor-sync.py sync`, which turned the identifier scan green.
<!-- /ANCHOR:how-delivered -->

---

<!-- ANCHOR:decisions -->
## Key Decisions

| Decision | Why |
|----------|-----|
| Keep spacers in a Doc export | Michel's choice. The examples already carried them and Story Mode already said so |
| Keep the hub keyword block | The parent-hub checker fails without it. The defect was the substring match |
| Leave the Task Mode tail in the knowledge file | The declaration records it as moved on purpose |
| Print no matched value in the identifier scan | A gate log is itself a tracked or shared surface |
| Leave the shared Conciseness card | Its Doc spacer example is copied into three systems, so the edit is a fleet change |
| Ask for a missing team, never guess it | Michel's choice. A wrong team lead sends the work to the wrong list |
| Design links in a section are plain lines, not bullets | The format gate blocks a plain bullet inside Requirements, and its validator has a shared twin |
<!-- /ANCHOR:decisions -->

---

<!-- ANCHOR:verification -->
## Verification

| Check | Result |
|-------|--------|
| `run_gates.sh` on the live tree | exit 0, `all 19 gates pass` |
| Source format lint with a banned word planted in a scratch copy | That gate fails and no other row changes |
| Scaffold lint on the tree before the fix, in a scratch clone | 16 lines flagged, 0 after |
| Identifier scan on the tree before the redaction, in a scratch clone | 1,900 files flagged, 0 after |
| Redaction script, second run | 0 replacements |
| `test_vendor_sync.py` | 36 tests pass, 32 before. The four new ones fail on the old script |
| Grader old against new on 9,407 report files | No difference apart from one phrase the old copy had dropped |
| `check_changelog_shape.py` | PASS for three notes here and seven upstream |
| Skilled playbook corpus | 53 PASS and 4 SKIP, unchanged |
| Skilled README checker on 1,005 READMEs | Output identical to before |
| `vendor-sync.py status` | exit 0, every entry in step |
<!-- /ANCHOR:verification -->

---

<!-- ANCHOR:limitations -->
## Known Limitations

1. **No live benchmark ran.** `AGENTS.md` and the skill files are shorter. The router fixtures and gates pass, and no model run measured the change.
2. **The Project is not updated.** Kernel v1.2.20 and eight knowledge files wait for Michel.
3. **No example teaches the Logic shape.** The feedback example is UI/UX only now. The scaffold still shows the Logic sections.
4. **The scan skips binary files.** 332 binary files and one report over 5 MB are not read. That report was checked by hand.
5. **GitHub can keep old commits.** The history of this repository was rewritten after the redaction, and 108 commit citations in 31 record files were repointed. A commit pushed before the rewrite can stay reachable by its hash on GitHub until its support purges it.
6. **The alignment command is local only.** Skilled ignores it in git, so its fix ships in no release.
7. **The grader skips two card sections.** Sections 6 and 7 hold 30 terms the format validator blocks and the grader does not read, so graded reports keep their counts.
8. **About 40 scaffold placeholders carry an Oxford comma.** No gate checks it.
9. **The title check advises and never blocks.** A refinement keeps its source title and a stated title is used as given, and the gate can see neither. It reads only an artifact that opens on `## About` or `## Problem`.
10. **Two shared fixtures print a title advisory under this system.** The two deal-shape fixtures in the Sync Loop do, and only reference parity runs them that way.
11. **`AGENTS.md` grew.** It holds 4,455 words, up from 3,974, because the title rule lives there.
<!-- /ANCHOR:limitations -->
