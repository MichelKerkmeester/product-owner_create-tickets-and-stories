---
title: "Feature Specification: Phase 3, the playbook rewrite and the approval gate"
description: "The Product Owner playbook tests two features at toy scale, so a run on it says little about whether a ticket reads like real engineering work. This phase replaces its 14 scenarios with 46 set at three fictional companies, adds a Ticket realism rubric with its severity split settled first, extends the runner to stage attachments and keep bundles whole and stops for the operator's approval before anything runs."
trigger_phrases:
  - "playbook rewrite phase"
  - "ticket realism rubric"
  - "scenario attachments context folder"
  - "approval gate before the opus run"
importance_tier: "important"
contextType: "implementation"
---
<!-- SPECKIT_TEMPLATE_SOURCE: spec-core | v2.2 -->
# Feature Specification: Phase 3, the playbook rewrite and the approval gate

<!-- SPECKIT_LEVEL: 2 -->
---

<!-- ANCHOR:metadata -->
## 1. METADATA

| Field | Value |
|-------|-------|
| **Level** | 2 |
| **Priority** | P0 |
| **Status** | Complete |
| **Created** | 2026-09-25 |
| **Branch** | `main` |
| **Parent Spec** | ../spec.md |
| **Phase** | 3 of 5 |
| **Predecessor** | 002-company-context-fixtures |
| **Successor** | 004-opus-run |
| **Handoff Criteria** | The playbook validator and `run/selftest.py` green on a state committed in both repos, and the operator's approval of the scenario plan recorded with its date and commit SHAs |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:phase-context -->
## Phase Context

This is **Phase 3** of the packet that rewrites the Product Owner manual testing playbook around realistic tickets for three fictional companies and reruns both packagings on claude-opus-5-5 at effort medium.

**Scope Boundary**: the playbook package under `AI Systems/Product Owner/sk-product-owner/manual-testing-playbook/` and a new report folder holding the extended run tooling. The skill, kernel, knowledge files, fixtures and the Sonnet report folder are read here and never edited. No scenario runs in this phase.

**Dependencies**:
- Phase 001 committed: the `Story-` export word, the `{task|bug|doc|Story|Epic}` clarification lane, the renamed knowledge files and the bundle rule with its paths
- Phase 002 committed: the three company folders under `AI Systems/Product Owner/benchmark/fixtures/companies/` and every attachment its `spec.md` manifest names
- `AI Systems/Product Owner/benchmark/reports/2026-09-25--manual-testing-playbook--claude-sonnet-5-medium/run/`, the source of the copied scripts

**Deliverables**:
- The rewritten playbook root, version `2.0.0.0`, with the Ticket realism rubric in section 5
- 46 scenario files, 23 per runtime
- `AI Systems/Product Owner/benchmark/reports/2026-09-25--manual-testing-playbook--claude-opus-5-5-medium/` with `.gitignore` and an extended `run/` folder, `run/selftest.py` included
- The operator's recorded approval of the scenario plan

**Changelog**:
- When this phase closes, refresh the matching file in ../changelog/ using the parent packet number plus this phase folder name.
<!-- /ANCHOR:phase-context -->

---

<!-- ANCHOR:problem -->
## 2. PROBLEM & PURPOSE

### Problem Statement
Twelve of the 14 scenarios are about payout pause and two about notification retry. Their prompts carry none of the product names, teams, platforms or numbers a real ticket carries, and the Story exports use `PRD-`. A run on them measures the delivery contract and says little about whether an export reads like engineering work. The runner also cannot put company context in front of either runtime, and its collector flattens folders, so a Story with nested Tasks could be neither run nor collected.

### Purpose
Both runtimes face 23 realistic requests each, set at Roamstay, Loomlist or Fernhouse with the company's documents attached, and are graded by a realism rubric whose Blocking and Advisory split is fixed before any scenario is written. The operator approves that plan before a single turn runs.
<!-- /ANCHOR:problem -->

---

<!-- ANCHOR:scope -->
## 3. SCOPE

### In Scope
- The Ticket realism rubric in root section 5, written first, with the split below
- Re-anchoring every `file:line` citation in the root to the post-001 committed sources
- Root rewrite: intro count, coverage map, natural Turn 1 coverage, preconditions and ledger, a new "Company context and attachments" section, Clarification turns and Export names with `Story-` and the bundle path, the Identity handover rule, waves 1 to 6, 46 summary blocks, sections 17 and 18
- Deleting the 12 retired scenario files and writing the 46 in the manifest below. The two `identity-handover.md` files keep their name and are rewritten in place
- A `- Attachments:` bullet in every scenario contract, written as links to the fixtures
- The new report folder, copied from the Sonnet one and extended: the runner stages attachments into `context/`, the isolation proof checks them, the collector keeps bundle subfolders and `check_run.py` checks the model and effort
- `run/selftest.py`, the three tests and the validator run
- Commits in the Barter repo and the Product Owner public repo
- The approval gate, as the last task

### Ticket realism rubric, as settled

| Severity | Item | Boundary |
|----------|------|----------|
| Blocking | Wrong artifact word | The export word or the kind the reply names differs from the routed kind, `PRD-` for a Story included. This is the Export names check already graded, stated once |
| Blocking | A required section of the routed template missing | Required for the shape and energy the reply resolved, read from that runtime's own template: the skill asset or the Project knowledge mirror. A section the template marks optional or opt-in, such as Story `## Requirements` with no hard value or `## Delivery` nobody forced, is never required |
| Blocking | An invented fact | Exactly the Defect severity definition, the disclosed-addition exception and the whole-item naming sentence included. The rubric adds no stricter reading |
| Blocking | Placeholder or toy content | An unfilled slot (`{...}`, `{LINK}`, `TODO`, lorem ipsum) or a stand-in name or value where the turns or an attachment supply the real one. Exempt: the Project `[NNN]` path slot, the bug template's `Not provided`, Story Mode's `TBD...` in the three Delivery slots and every fixed template line |
| Blocking | Context facts ignored or altered | The artifact states a name, surface, service, number, code, platform or version the attachments or turns contradict, or puts a generic stand-in where they name the real thing the request is about. Omitting a context fact the request does not need is not a defect |
| Advisory | Size band | The artifact body's line count against the band the scenario records. Never a failure, whatever the scenario tests |
| Advisory | Commentary | Unchanged from Defect severity, its delivery-shape exception for `PID-001` included |
| Advisory | Asking for a fact an attachment already states | Recorded as it is today, never a failure |
| Advisory | A Task or Bug title with no discipline code | No routed template asks for one, so it is recorded only. Story and Epic H1s follow the skill's H1 rule, which bans `BO`, `BE` and `FE` short codes and a `PRD -` prefix, so neither the rubric nor any Pass clause expects a code there |

Existing readings that stay exactly as they are: response ordering and commentary length, progress-note verbosity, commentary before a Project block, the skill reply printing the clarification question, Project number order and the illustrative `[description]` slug.

### Out of Scope
- Running any scenario - phase 004, after approval. The runner's `--dry-run`, which sends no turn, is allowed
- Grading and the realism review - phase 005
- Editing the skill, `AGENTS.md`, the kernel or any knowledge file - phase 001 owns those
- Writing or editing any fixture - phase 002 owns them
- The Sonnet report folder - it stays as the historical record (D4)
- Prompt Improver and Deal Templates - D5
- The playbook validator and the Sync Loop scripts - read, never changed
- Pushing without the operator's go-ahead

### Files to Change

| File Path | Change Type | Description |
|-----------|-------------|-------------|
| `AI Systems/Product Owner/sk-product-owner/manual-testing-playbook/manual-testing-playbook.md` | Modify | Full rewrite, version `2.0.0.0` |
| `AI Systems/Product Owner/sk-product-owner/manual-testing-playbook/{skill,project}-*/` retired files | Delete | 12 files: `task-command-flow.md`, `bug-report-flow.md`, `doc-guide-delivery.md`, `doc-conflict-gate.md`, `story-shape-hard-values.md` and `ambiguous-intake-energy-choice.md`, each on both sides |
| `AI Systems/Product Owner/sk-product-owner/manual-testing-playbook/{skill,project}-*/<slug>.md` | Create, rewrite | The 46 files in the manifest below |
| `AI Systems/Product Owner/benchmark/reports/2026-09-25--manual-testing-playbook--claude-opus-5-5-medium/.gitignore` | Create | Copy of the Sonnet folder's ignore file |
| `.../claude-opus-5-5-medium/run/playbook_runner.py` | Create | Copy, plus attachment staging and the `context/` isolation check |
| `.../claude-opus-5-5-medium/run/collect_exports.py` | Create | Copy, plus bundle subfolders on both sides and `context/` skipped |
| `.../claude-opus-5-5-medium/run/check_run.py` | Create | Copy, default model `claude-opus-5-5`, engine, model and effort read from `manifest.json` |
| `.../claude-opus-5-5-medium/run/selftest.py` | Create | Parse, staging, isolation, collector and check_run tests with negative controls |

### Scenario file manifest

Each row is one skill file and its Project twin, same slug, in `skill-<group>/` and `project-<group>/`.

| IDs | Slug | Group | Company | Export named | Turns | Wave |
|-----|------|-------|---------|--------------|-------|------|
| SID-001, PID-001 | `identity-handover` | identity | Loomlist | task | 2 | 1 |
| STK-001, PTK-001 | `quick-copy-task` | backlog-modes | Fernhouse | task | 1 | 2 |
| STK-002, PTK-002 | `design-notes-fe-task` | backlog-modes | Roamstay | task | 2 | 2 |
| STK-003, PTK-003 | `long-be-integration-task` | backlog-modes | Fernhouse | task | 2 | 2 |
| STK-004, PTK-004 | `parent-task-with-subtasks` | backlog-modes | Loomlist | task, parent | 2 | 2 |
| STK-005, PTK-005 | `supplied-parent-subtask` | backlog-modes | Loomlist | task, subtask | 2 | 2 |
| STK-006, PTK-006 | `data-tracking-task` | backlog-modes | Roamstay | task | 2 | 2 |
| SBG-001, PBG-001 | `quick-bug` | backlog-modes | Fernhouse | bug | 1 | 3 |
| SBG-002, PBG-002 | `support-ticket-bug` | backlog-modes | Roamstay | bug | 2 | 3 |
| SBG-003, PBG-003 | `two-platform-log-bug` | backlog-modes | Loomlist | bug | 2 | 3 |
| SDK-001, PDK-001 | `behavior-reference` | document-modes | Fernhouse | doc | 2 | 4 |
| SDK-002, PDK-002 | `incident-runbook` | document-modes | Roamstay | doc | 2 | 4 |
| SDK-003, PDK-003 | `proposal-decision-owner` | document-modes | Loomlist | doc | 2 | 4 |
| SDK-004, PDK-004 | `catalog-conflict-gate` | document-modes | Loomlist | doc | 2 | 4 |
| SST-001, PST-001 | `story-hard-values` | story-modes | Roamstay | Story | 2 | 5 |
| SST-002, PST-002 | `story-forced-delivery` | story-modes | Loomlist | Story | 2 | 5 |
| SST-003, PST-003 | `story-refinement` | story-modes | Fernhouse | the source filename | 2 | 5 |
| SST-004, PST-004 | `story-with-nested-tasks` | story-modes | Fernhouse | Story folder, Story plus 4 tasks | 2 | 5 |
| SEP-001, PEP-001 | `epic-from-strategy-brief` | story-modes | Roamstay | Epic | 2 | 5 |
| SEP-002, PEP-002 | `epic-natural-wording` | story-modes | Loomlist | Epic | 2 | 5 |
| SEP-003, PEP-003 | `epic-quick-energy` | story-modes | Fernhouse | Epic | 1 | 5 |
| SIR-001, PIR-001 | `vague-intake-kind-and-energy` | interactive-routing | Roamstay | intake, then the kind Turn 2 picks | 2 | 6 |
| SIR-002, PIR-002 | `conflicting-commands` | interactive-routing | Fernhouse | intake, then the kind Turn 2 picks | 2 | 6 |

### SST-004 and PST-004 expected behavior

This follows the bundle design in `001-story-prefix-and-bundle/spec.md` section 3.

- Turn 1 uses `$story` with "break it into tasks". No scenario uses "write a story for X and create a task for each platform", which the router sends to Task Mode
- Turn 1: Story Mode asks its context question once, in the Story lane, saved as `export/[###] - Story-[description]-clarification.md` at the top of `export/`, outside any folder
- Turn 2: one bundle on the next number, `export/[###] - Story-[description]/`, holding `[###] - Story-[description].md` and `[###].1` to `[###].4 - task-[description].md` in the Story's task order: FE iOS, FE Android, FE web, BE tracking webhook
- The Story lists its tasks in a `#### **Tasks**` block inside `## About`, after `#### **References**`, one `*   ` bullet per task linking the sibling file as `(<[###].[n] - task-[description].md>)`
- Each task names the Story in a `**Story**` block beside `**Epic**`, linking `(<[###] - Story-[description].md>)`, and carries no `**Parent task**` block
- Skill reply: every path, Story first, each with its own `Verified: read-back succeeded; N lines` line, then one `HVR self-scan:` line for the whole bundle
- Project reply: one Deliverable Block per file, Story first, each followed by its own `Export-equivalent path:` inside the folder, then one `HVR self-scan:` line for the set

Per side: 7 tasks, 3 bugs, 4 stories, 3 epics, 4 docs and 1 Story with nested Tasks. Natural-wording Turn 1s: `STK-006`, `SDK-001`, `SST-001`, `SEP-002` and `SIR-001` and their twins.
<!-- /ANCHOR:scope -->

---

<!-- ANCHOR:requirements -->
## 4. REQUIREMENTS

### P0 - Blockers (MUST complete)

| ID | Requirement |
|----|-------------|
| REQ-001 | Root section 5 gains a `### Ticket realism` subsection holding the Blocking and Advisory lists in section 3 above, written before any scenario file exists. The Defect severity lists and the six existing advisory readings keep their wording, re-anchored line numbers apart |
| REQ-002 | Every `file:line` citation in the root and in the 46 scenario files points at the line that holds the cited rule on the post-001 commit |
| REQ-003 | Export names and Clarification turns use `Story-`, the lane `{task\|bug\|doc\|Story\|Epic}` and the bundle path `export/[###] - Story-[description]/`, and the graded artifact words are `task`, `bug`, `doc`, `Story`, `Epic` and `intake`. No `PRD-` export word is left in the package |
| REQ-004 | A root section "Company context and attachments" names the three companies, links their folders under `benchmark/fixtures/companies/` and states the staging rule: each attachment is copied to `context/<basename>` before the baseline on both runtimes, it is never modified and each scenario's `- Attachments:` bullet is its one list |
| REQ-005 | The root's intro count, coverage map, natural Turn 1 list, wave table, summary blocks and sections 17 and 18 describe the 46 files. The wave table uses ranges such as `STK-001..STK-006`, and `load_waves` returns the manifest's wave for every ID |
| REQ-006 | The 12 retired files are gone and the 46 manifest files exist, 23 per side, each `Sxx-nnn` with a `Pxx-nnn` twin of the same slug. Each file names the export its manifest row gives, so each side holds 7 tasks, 3 bugs, 4 stories, 3 epics, 4 docs and 1 bundle |
| REQ-007 | Twins carry identical turn inputs and identical attachment lists, and turn counts match the manifest: 1 for `STK-001`, `SBG-001` and `SEP-003` and their twins, 2 for the rest, 86 turns in all |
| REQ-008 | Every contract carries `- Attachments:` as links that resolve under `benchmark/fixtures/companies/<company>/`: the company's context file first, then each source the catalog cites, matching the phase 002 manifest. Turn 1 names each one as `context/<basename>` |
| REQ-009 | The playbook validator prints `scenarios=46 categories=10 operator=46` with `violations=0 warnings=0` and exits 0. `warnings=0` is required because `PROMPT_UNSYNCED` is only a warning |
| REQ-010 | The new report folder holds the Sonnet `.gitignore` and `run/` scripts, and the Sonnet report folder shows no diff |
| REQ-011 | The runner parses `- Attachments:`, stops before any scenario runs when a link does not resolve or two basenames collide, copies each file to `<sandbox>/context/<basename>` on both sides before the baseline snapshot and records each basename, repository-relative source and sha256 in `manifest.json` and `meta.json` |
| REQ-012 | `prove_isolation` accepts `context/` only when it holds exactly the declared attachments, byte for byte. An extra, missing or altered file aborts the run |
| REQ-013 | The collector writes a bundle as `skill/<id> - <folder>/<file>` and `claude project/<id> - <folder>/<file>`, applies the `[NNN]` slot rule to the folder name too, keeps single files where they land today and never collects `context/` |
| REQ-014 | With both tests and the validator green on a committed state, the orchestrator shows the operator a terminal table and a private artifact page holding the catalog, the companies, the attachments and the rubric, asks for approval through AskUserQuestion and records the answer with its date and SHAs. At that moment the new report folder holds no `manifest.json`, `run-status.json`, `run-log.jsonl`, `skill/` or `claude project/` |

### P1 - Required (complete OR user-approved deferral)

| ID | Requirement |
|----|-------------|
| REQ-015 | `SID-001` and `PID-001` keep the four identity greps with counts re-read on the post-001 tree and keep their `- Playbook ID:` lines, which the Sync Loop's `check_criteria.sh` counts. The Identity handover rule matches the new two-turn chain |
| REQ-016 | Each scenario records `- Size band (advisory):` as a line range of the artifact body, in its own bullet. No Pass clause and no 9-column Pass/fail cell names the size band or commentary, and none expects a discipline code in a Story or Epic H1 |
| REQ-017 | `check_run.py` defaults to `claude-opus-5-5` and reports a finding when `manifest.json` names an engine, model or effort other than `claude`, `claude-opus-5-5` and `medium` |
| REQ-018 | The phase commits land in the Barter repo and the Product Owner public repo, the public one with no attribution line, nothing is pushed without the operator's go-ahead and no changed file holds an em dash |

> Acceptance criteria for these requirements live in `acceptance-criteria.md`,
> which is the document that decides whether this packet may close.
<!-- /ANCHOR:requirements -->

---

<!-- ANCHOR:success-criteria -->
## 5. SUCCESS CRITERIA

- **SC-001**: The validator line reads `scenarios=46 categories=10 operator=46 ... violations=0 warnings=0` and `run/selftest.py` exits 0 with every planted fault caught
- **SC-002**: The operator approved the scenario plan against a named commit before any scenario ran
<!-- /ANCHOR:success-criteria -->

---

<!-- ANCHOR:risks -->
## 6. RISKS & DEPENDENCIES

| Type | Item | Impact | Mitigation |
|------|------|--------|------------|
| Dependency | Phase 001: `Story-` naming, bundle paths, renamed knowledge files | High | T001 stops the phase until 001 is committed. Every citation is re-read on that commit |
| Dependency | Phase 002: fixture names in its manifest | High | T001 stops until every named fixture exists. The selftest compares each Attachments list with that manifest |
| Risk | Prompt drift between twins, which the validator never compares across files | High | Each writer owns both twins of its group, and the selftest compares every turn and attachment list pair |
| Risk | Validator rules: forbidden `PARTIAL`, `READY`, `UNAUTOMATABLE` and `BLOCKED`, ISO dates near result words, `/Users/` or `/home/` paths, unresolved links, prompt sync reported only as a warning | Med | The writer brief lists each rule. The gate requires `warnings=0` |
| Risk | Runner parse limits: one-line cells, a cell unwrapped only when it holds exactly two backticks, a 3-letter ID prefix for waves | Med | Turn inputs hold no backtick, pipe or line break, and long context lives in attachments. The selftest asserts every turn and wave |
| Risk | Rubric severity creep, a new Blocking item turning an advisory reading into a failure | Med | The split is written before any scenario. The size band sits outside Pass/fail. CHK-FIX-002 reads the six existing readings back unchanged |
| Risk | The router sends "write a story for X and create a task for each platform" to Task Mode | Med | `SST-004` and `PST-004` use `$story` with "break it into tasks", and no scenario depends on the other phrasing |
| Risk | Another root table whose rows start with a number and hold an ID would feed `load_waves` wrong waves | Low | Only the wave table has that shape. The selftest asserts each wave |
<!-- /ANCHOR:risks -->

---


---

<!-- ANCHOR:nfr -->
## L2: NON-FUNCTIONAL REQUIREMENTS

### Performance
- **NFR-P01**: `run/selftest.py` finishes in under a minute with no model call and no network
- **NFR-P02**: The runner dry run lists all 46 rows without writing into the report folder

### Security
- **NFR-S01**: No real person, real brand, credential or developer-absolute path in any scenario or script
- **NFR-S02**: The Product Owner public repo commit carries no attribution line

### Reliability
- **NFR-R01**: No scenario turn runs before the recorded approval (D6)
- **NFR-R02**: No em dash in any changed file, and the Sonnet report folder stays byte-unchanged
<!-- /ANCHOR:nfr -->

---

<!-- ANCHOR:edge-cases -->
## L2: EDGE CASES

### Data Boundaries
- Empty input: a scenario with no `- Attachments:` bullet stops the runner at load, since every scenario attaches at least its company's context file
- Maximum length: a table cell is one line, so any context longer than a sentence goes into an attachment
- Invalid format: a turn input holding a backtick reaches the model wrapped in backticks, and a pipe splits the validator's cell. Neither may appear in a turn input

### Error Scenarios
- External service failure: a fixture renamed after this phase commits breaks the scenario link, and the validator reports `PATH_MISSING`
- Network timeout: not applicable, nothing here calls a model
- Concurrent access: a peer session editing the playbook overlaps directly, so work stops and the operator is asked

### State Transitions
- Partial completion: a writer group that stops leaves its folder half written, and the validator's orphan and index checks name the gap
- Session expiry: the operator asks for changes at the gate. The edits land, all three checks rerun, a new commit is made and the plan is shown again
<!-- /ANCHOR:edge-cases -->

---

<!-- ANCHOR:complexity -->
## L2: COMPLEXITY ASSESSMENT

| Dimension | Score | Notes |
|-----------|-------|-------|
| Scope | 18/25 | One root, 46 scenario files, four scripts, two repos |
| Risk | 12/25 | Prompt sync, rubric severity, isolation proof |
| Research | 6/20 | Validator, runner and collector read while scoping |
| **Total** | **36/70** | **Level 2** |
<!-- /ANCHOR:complexity -->

---

<!-- ANCHOR:questions -->
## 10. OPEN QUESTIONS

- None open. The orchestrator ruled on 2026-09-25:
- Every scenario attaches its company's context file as well as its source attachments
- Asking for a fact an attachment states and a Task or Bug title with no discipline code stay advisory. Story and Epic H1s are never expected to carry a code
- The report folder stays `2026-09-25--...`, and phase 004 renames it with `git mv` in both repos if the first turn runs on a later day
- Phase 002's manifest is still to come, and the orchestrator fills its names into the writer brief at T004
<!-- /ANCHOR:questions -->

---
