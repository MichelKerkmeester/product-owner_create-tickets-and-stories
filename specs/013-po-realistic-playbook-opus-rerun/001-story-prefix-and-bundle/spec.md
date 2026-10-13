---
title: "Feature Specification: Phase 1, the Story prefix and the Story bundle"
description: "Product Owner Story exports still carry the PRD- word, so a Story reads as a different artifact from its Epic sibling, and nothing lets a Story ship together with the tasks that deliver it. This phase gives Story exports the Story- word in both packagings, adds the Story with nested Tasks bundle, and records the removal of the old Sonnet exports."
trigger_phrases:
  - "story export prefix"
  - "story with nested tasks"
  - "story bundle folder"
  - "prd prefix removal"
importance_tier: "important"
contextType: "implementation"
_memory:
  continuity:
    packet_pointer: "013-po-realistic-playbook-opus-rerun/001-story-prefix-and-bundle"
    last_updated_at: "2026-09-25T20:40:00Z"
    last_updated_by: "claude-opus-5-5"
    recent_action: "Scoped the Story prefix and the bundle rule"
    next_safe_action: "Record the gate baselines, then start with the skill sources"
    blockers: []
    key_files:
      - "AI Systems/Product Owner/AGENTS.md"
      - "AI Systems/Product Owner/sk-product-owner/SKILL.md"
      - "AI Systems/Product Owner/sk-product-owner/references/story-mode.md"
      - "AI Systems/Product Owner/claude project/Custom Instructions.md"
    session_dedup:
      fingerprint: "sha256:0000000000000000000000000000000000000000000000000000000000000000"
      session_id: "12f293fe-5421-46a0-b1ea-9fdc15ce0f8e"
      parent_session_id: null
    completion_pct: 0
    open_questions:
      - "Should the router send a Story plus 'create a task for each platform' to Story Mode? It routes to Task today"
      - "Phase 003 realism rubric wants discipline codes in titles, and the Story H1 rule bans BO, BE and FE codes"
    answered_questions: []
---
<!-- SPECKIT_TEMPLATE_SOURCE: spec-core | v2.2 -->
# Feature Specification: Phase 1, the Story prefix and the Story bundle

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
| **Phase** | 1 of 5 |
| **Predecessor** | None |
| **Successor** | 002-company-context-fixtures |
| **Handoff Criteria** | The `Story-` word and the bundle rule committed in both repositories, the proof grep empty, and the parity gate green on that commit. Phase 003 needs this, phase 002 does not |
<!-- /ANCHOR:metadata -->

---

<!-- ANCHOR:phase-context -->
## Phase Context

This is **Phase 1** of the packet that rewrites the Product Owner manual testing playbook around realistic tickets for three fictional companies and reruns both packagings on claude-opus-5-5 at effort medium.

**Scope Boundary**: the parent decisions D1 (the `Story-` word), D2 (the Story with nested Tasks bundle) and D4 (the old exports removed), in the Product Owner system only, both packagings. The playbook is touched only where its old scenarios would contradict the new word. Phase 003 rewrites it.

**Dependencies**:
- The parent `goal.md` decisions D1 to D7, frozen
- `AI Systems/Product Owner/SYNC.md`, the manual parity method for the Claude Project files
- The Sync Loop tools `resync_statement.py` and `repoint_rename.py`, in the Claude Project Sync Loop folder under `AI Systems/`
- The real corpus in `Product Context/Tasks & Stories/`, which grounds the bundle design below

**Deliverables**:
- The `Story-` export word and the `Story` clarification lane in every live skill, kernel, knowledge, README and declaration site
- The Story with nested Tasks bundle rule in the skill sources and, with the same meaning, in the kernel and three knowledge mirrors
- Skill 0.11.0, kernel v0.15.0, a changelog entry and a dated `SYNC.md` note that says the kernel review is pending
- Commits in the Barter repo and in the Product Owner public repo, carrying the D4 removal

**Changelog**:
- When this phase closes, refresh the matching file in ../changelog/ using the parent packet number plus this phase folder name.
<!-- /ANCHOR:phase-context -->

---

<!-- ANCHOR:problem -->
## 2. PROBLEM & PURPOSE

### Problem Statement
A new Story saves as `export/[###] - PRD-[description].md` while its sibling saves as `export/[###] - Epic-[description].md`, so the one artifact kind that Story Mode produces most often is named for a document type the system otherwise calls a Story. The prefix sits on 25 lines in 14 live files, across the skill, the kernel, two knowledge mirrors, both READMEs, the playbook and the Sync Loop declaration, plus the playbook root's list of artifact words. A Story also cannot ship with the tasks that deliver it: `AGENTS.md` treats any request for more than one artifact as independent actions and asks which one to make, so "write the story and break it into tasks" never produces a linked set. The 25 Sonnet exports in `export/benchmark/` showed both problems and were removed before this phase opened.

### Purpose
A Story exports under `Story-` in both packagings, and a Story with its task breakdown exports as one folder whose Story lists its tasks and whose tasks name the Story, with the rule stated wherever each packaging reads it.
<!-- /ANCHOR:problem -->

---

<!-- ANCHOR:scope -->
## 3. SCOPE

### In Scope
- D4: record the removal of the 25 files under `AI Systems/Product Owner/export/benchmark/`, done by the orchestrator with `git rm` in the nested repo, and carry it into both repositories' commits
- D1: the export word `PRD-` becomes `Story-`, and the clarification lane `{task|bug|doc|PRD|Epic}` becomes `{task|bug|doc|Story|Epic}`. The label "New PRD Story" becomes "New Story" beside it
- D1 keeps: the `$prd` and `$p` command aliases, the ban on a `PRD -` prefix in a Story H1, every changelog file and every dated or historical record
- D2: the Story with nested Tasks bundle, settled below
- The playbook's three live `PRD` sites, edited minimally so the old scenarios grade the new word until phase 003 replaces them
- The system README's references to the removed benchmark files, which D4 left pointing at nothing
- Version bookkeeping: skill, kernel, three knowledge mirror renames, changelog, `SYNC.md`, both READMEs and `description.json`

### Out of Scope
- Router changes. `$story` plus "break it into tasks" already routes to Story Mode by command, so `router-contract.md`, its byte-copy mirror and `route_contract.py` stay as they are
- An Epic with its child stories, or a Bug with tasks. D2 covers only a Story with nested Tasks
- The playbook rewrite, the fixtures, the run and the grading, which phases 002 to 005 own
- The `PRD refinement` label in the kernel, which names a kind of work rather than an export word
- The user's own files in `export/` outside `export/benchmark/`, which are deliverables and never system source
- Recording a kernel review, which only the operator confirms

### Files to Change

| File Path | Change Type | Description |
|-----------|-------------|-------------|
| `AI Systems/Product Owner/AGENTS.md` | Modify | D1 at lines 79 and 91. D2 exception bullet after line 197, bundle naming block, example and reply shape |
| `AI Systems/Product Owner/sk-product-owner/SKILL.md` | Modify | D1 at lines 207 and 208. D2 inside line 207 and line 252, on their existing lines. Version 0.11.0 |
| `AI Systems/Product Owner/sk-product-owner/references/story-mode.md` | Modify | D1 at lines 25 and 375. D2 Artifact Rules exception, a bundle subsection and the reply. Version v0.402 |
| `AI Systems/Product Owner/sk-product-owner/assets/story-template.md` | Modify | D1 at line 22 |
| `AI Systems/Product Owner/sk-product-owner/assets/task-templates.md` | Modify | D2 `**Story**` block and a Notes For Use bullet. Version v0.102 |
| `AI Systems/Product Owner/sk-product-owner/references/interactive-mode.md` | Modify | D1 at lines 25 and 90. D2 clarification sentence inside line 93. Version v0.405 |
| `AI Systems/Product Owner/sk-product-owner/assets/interactive-response-templates.md` | Modify | D1 at line 26 |
| `AI Systems/Product Owner/claude project/Custom Instructions.md` | Modify | H1 v0.15.0. D1 and D2 inside lines 226 and 228 |
| `AI Systems/Product Owner/claude project/knowledge/` Story Mode, Interactive Mode and Task Templates mirrors | Modify, rename | The same meaning in Project wording. v0.401 to v0.402, v0.404 to v0.405, v0.101 to v0.102 |
| `AI Systems/Product Owner/claude project/README.md` | Modify | Version claims at lines 11 and 39, the lane at line 124, one bundle smoke line |
| `AI Systems/Product Owner/README.md` | Modify | Lines 300 to 307, 477, 492, 570 to 572, 644, 725 to 737 and 763 |
| `AI Systems/Product Owner/SYNC.md` | Modify | Version claims at line 18 and a dated note, review pending |
| `AI Systems/Product Owner/sk-product-owner/` `description.json`, `README.md`, `changelog/v0.11.0.0.md` | Modify, create | Skill version and the release entry |
| `AI Systems/Product Owner/sk-product-owner/manual-testing-playbook/` root line 140 and both `story-shape-hard-values.md` line 31 | Modify | The artifact word, the two export paths and root version 1.0.0.4 |
| The Sync Loop declaration `systems.py`, lines 3799 and 3801 | Modify | Only through `resync_statement.py` and `repoint_rename.py` |
| `AI Systems/Product Owner/export/benchmark/` | Delete | The 25 Sonnet files, already staged as deleted in the nested repo |

### Bundle design (D2)

A new Story requested together with its task breakdown is one dependent deliverable. The table settles each open point against the real corpus in `Product Context/Tasks & Stories/`.

| Point | Settled answer | Grounding |
|-------|----------------|-----------|
| When it applies | A Story command or Story framing plus wording that asks for the tasks, such as "break it into tasks". Two explicit artifact commands (`$story $task`) stay a conflict | `route_request` sends `$story ... break it into tasks` to Story Mode by command today |
| Folder and names | `export/[###] - Story-[description]/` holding `[###] - Story-[description].md` and `[###].[n] - task-[description].md`, `n` counting from 1 in the Story's task order. The bundle takes one number | D2 |
| Where the Story lists its tasks | A `#### **Tasks**` block inside `## About`, after `#### **References**`, one `*   ` bullet per task in `n` order, each linking the sibling file: `*   [{Task H1}](<[###].[n] - task-[description].md>)` | The Story `FS - Partner - Barter deal - Motivation - Settings` lists its linked child tickets in an H4-bold block inside About. `FE - Fv2.5 - Feed - Sections` links sibling files in the `(<file name.md>)` form |
| Why not `## Scope` | `## Scope` marks the Epic kind, so a Story carrying it would blur the kind check the kernel and graders make | `epic-template.md` and `story-mode.md` section 2 |
| How a task names its parent | A `**Story**` block in the task's References area, between `**Epic**` and `**Parent task**`, holding `- [{Story H1}](<[###] - Story-[description].md>)`. No `**Parent task**` block, because a Story is not a task | The five Chat tasks open About with `**Story:** {LINK}`, and the Canonical Task template gives `**Epic**` and `**Parent task**` the same label, divider, bullet shape |
| Task template | Each task uses the Canonical Task template. Story Mode reads `assets/task-templates.md` under the ON_DEMAND allowance for one template asset, so the one-scaffold rule and the router's resource map stay unchanged | `SKILL.md` Resource Loading table, ON_DEMAND row |
| Task split | A split the request names is authoritative, one task per named part. With none named, the one consolidated Story question asks for it | `story-mode.md` section 2, a stated count is authoritative |
| Clarification numbering | Asked once, in the Story lane, at the top of `export/`: `export/[###] - Story-[description]-clarification.md`. The bundle then takes the next number, and the clarification stays outside the folder, untouched | `AGENTS.md` Section 2, clarification paragraph |
| Skill reply | Every file read back. The reply lists every path, Story first, each with its own `Verified: read-back succeeded; N lines` line, then one `HVR self-scan:` line counted across the whole bundle | D2 and `AGENTS.md` step 6 |
| Project reply | One Deliverable Block per file, Story first, each followed by its own `Export-equivalent path:` inside the folder, then one `HVR self-scan:` line for the set | D2 and kernel ALWAYS 5 and 6 |

The exception bullet for `AGENTS.md` Routing Compatibility, placed after line 197:

> - A new Story requested together with its task breakdown is one dependent deliverable, not independent multi-artifact actions, so it needs no question about which artifact to make. It routes to Story Mode in the Story shape and saves as one bundle folder. Story Mode still asks its own context question, and two explicit artifact commands such as `$story $task` stay a conflict

The rule lives in `AGENTS.md`, `SKILL.md`, `story-mode.md`, `task-templates.md` and `interactive-mode.md` on the skill side, and in the kernel and the Story Mode, Task Templates and Interactive Mode mirrors on the Project side.
<!-- /ANCHOR:scope -->

---

<!-- ANCHOR:requirements -->
## 4. REQUIREMENTS

### P0 - Blockers (MUST complete)

| ID | Requirement |
|----|-------------|
| REQ-001 | The 25 old Sonnet files are absent from `AI Systems/Product Owner/export/benchmark/` in the committed state of both repositories |
| REQ-002 | No live Product Owner or Sync Loop file names a `PRD-` export or a `PRD` clarification lane outside changelog files, run reports, episode logs, `export/` and dated log lines |
| REQ-003 | The `$prd` and `$p` aliases and the ban on a `PRD -` prefix in a Story H1 survive in every file that carried them before |
| REQ-004 | `AGENTS.md`, `SKILL.md`, `story-mode.md`, `task-templates.md` and `interactive-mode.md` state the bundle as settled in section 3, and the kernel and the three mirrors state the same meaning in Project wording |
| REQ-005 | Every changed declared statement is rewritten through `resync_statement.py` or `repoint_rename.py`, and residency passes |
| REQ-006 | The format gate adds no finding its baseline lacks, and the router and format fixtures, the playbook validator and the parity gate on the committed state all pass |
| REQ-007 | The kernel H1 moves to v0.15.0, and `SYNC.md` carries a dated note naming the change and saying the kernel review is pending |

### P1 - Required (complete OR user-approved deferral)

| ID | Requirement |
|----|-------------|
| REQ-008 | Skill 0.11.0, `description.json` 0.11.0.0, a `changelog/v0.11.0.0.md` entry, and every README version claim agreeing with them. The three mirrors renamed with no live reference to an old name |
| REQ-009 | No line the playbook cites by number in `SKILL.md`, the kernel or `interactive-mode.md` moves, or its citation is updated in the same change |
| REQ-010 | The playbook root's artifact-word list and both `story-shape-hard-values.md` export paths say `Story`, and the root moves to 1.0.0.4 |
| REQ-011 | The system README names no file under `export/benchmark/` that does not exist |
| REQ-012 | A sample bundle, one Story and two tasks written to this phase's `scratch/`, passes the format gate in artifact mode |
| REQ-013 | Commits land in the Barter repo and the Product Owner public repo, the public one with no attribution line, and nothing is pushed before the operator's go-ahead |

> Acceptance criteria for these requirements live in `acceptance-criteria.md`,
> which is the document that decides whether this packet may close.
<!-- /ANCHOR:requirements -->

---

<!-- ANCHOR:success-criteria -->
## 5. SUCCESS CRITERIA

- **SC-001**: The proof grep in `plan.md` prints no line, against 25 lines in 14 files on 2026-09-25
- **SC-002**: A reader of either packaging finds the bundle's folder, names, links, clarification lane and reply shape without opening the other packaging
<!-- /ANCHOR:success-criteria -->

---

<!-- ANCHOR:risks -->
## 6. RISKS & DEPENDENCIES

| Type | Item | Impact | Mitigation |
|------|------|--------|------------|
| Risk | A new kernel or `SKILL.md` line shifts a line the playbook cites | Med | Kernel and `SKILL.md` edits stay on their existing lines, and a before and after snapshot of every cited line proves it |
| Risk | A substitution whose new text contains the old text compounds in the declaration | High | `resync_statement.py --batch` skips a statement that already holds the new text. Residency runs after it |
| Risk | A repoint rewrites a dated record | Med | `repoint_rename.py` skips dated log lines and history folders. The `SYNC.md` diff is read before commit |
| Risk | The parity gate reads committed files only | Med | Run it after the commit and before any push |
| Risk | Peer sessions hold uncommitted work in the shared tree | Med | Stage named paths only. Never reset or check out |
| Risk | The format gate flags the new Tasks block or the sibling links | Low | The REQ-012 sample runs the gate on the shape before the rule ships |
| Dependency | The operator's push go-ahead | Low | Commits wait locally |
| Dependency | Kernel review by the operator | Low | Recorded as pending, never as done |
<!-- /ANCHOR:risks -->

---


---

<!-- ANCHOR:nfr -->
## L2: NON-FUNCTIONAL REQUIREMENTS

### Performance
- **NFR-P01**: The kernel keeps its 253 lines, so the Project reader's rule positions do not move
- **NFR-P02**: One `resync_statement.py --batch` call carries every declared substitution, because the declaration costs seconds to import per call

### Security
- **NFR-S01**: No credentials, tokens or raw event streams in any changed file or commit
- **NFR-S02**: The Product Owner public repo commit carries no attribution line

### Reliability
- **NFR-R01**: A kernel review is recorded only after the operator confirms it
- **NFR-R02**: No em dash in any added or changed line, checked with a grep over the diff
<!-- /ANCHOR:nfr -->

---

<!-- ANCHOR:edge-cases -->
## L2: EDGE CASES

### Data Boundaries
- A Story with one task: still a bundle, `[###].1` alone, because the request asked for the breakdown
- No split named: the Story question asks for it, and nothing is drafted until the user answers
- A refinement of a supplied Story plus new tasks: the Story keeps its source filename, so the bundle applies to a new Story only

### Error Scenarios
- One file's read-back fails after one retry: that file gets no `Path:` line, and the reply says the bundle is blocked rather than delivered
- A gate fails after an edit: stop, fix the cause in scope, rerun the whole gate

### State Transitions
- Clarification first: the clarification keeps its number at the top of `export/`, and the bundle folder takes the next one
- `$quick $story` with a named split: Quick skips routine intake and still writes the full bundle
<!-- /ANCHOR:edge-cases -->

---

<!-- ANCHOR:complexity -->
## L2: COMPLEXITY ASSESSMENT

| Dimension | Score | Notes |
|-----------|-------|-------|
| Scope | 14/25 | About 20 files in two repositories, three mirror renames |
| Risk | 12/25 | Kernel, declared statements and cited line numbers |
| Research | 8/20 | Corpus reading for the bundle, already done |
| **Total** | **34/70** | **Level 2** |
<!-- /ANCHOR:complexity -->

---

<!-- ANCHOR:questions -->
## 10. OPEN QUESTIONS

- "Write a story for X and create a task for each platform" routes to Task Mode today, because the router reads "task for" as a task about another artifact. The playbook's bundle scenario uses `$story`, which routes correctly. Changing the router is outside D2 unless the operator asks
- Phase 003's realism rubric expects a discipline code in titles, while the Story and Epic H1 rule bans `BO`, `BE` and `FE` codes. This phase leaves the H1 rule as it is, so phase 003 must grade Story and Epic titles without codes or the operator must change the rule
<!-- /ANCHOR:questions -->

---
