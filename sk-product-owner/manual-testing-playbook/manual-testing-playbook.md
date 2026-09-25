---
title: "Product Owner: Manual Testing Playbook"
description: "Operator-facing directory, execution policy and release-readiness guide for the two-runtime Product Owner manual validation package."
version: 1.0.0.1
---

# Product Owner: Manual Testing Playbook

This package turns the Product Owner contract into 14 reproducible conversations across two runtimes. The skill set (`S`-prefixed IDs) runs the system from `AGENTS.md` with `sk-product-owner/` loaded. The Project set (`P`-prefixed IDs) runs the same system from `claude project/Custom Instructions.md` with that system's knowledge documents attached. The root owns shared policy and indexing. Each linked scenario file owns one synchronized Turn 1 prompt, a conversation chain, one nine-field execution table and current source anchors.

---

### Result persistence

<!-- MANUAL_PLAYBOOK_RESULT_PERSISTENCE_CONTRACT -->
A scenario run is complete only after its `PASS`, `FAIL` or `SKIP` outcome and reason are persisted into `benchmark/reports/<dated-run-label>/`. Generated report Markdown is renderer-owned and never hand-authored.

---

## 1. OVERVIEW

The playbook covers 14 scenarios in two mirrored sets of seven, grouped under ten category folders. No alternate or supplemental scenario files are part of the package.

### Coverage map

| Category | IDs | Count | Primary surface |
|---|---|---:|---|
| Skill identity | `SID-001` | 1 | Skill delivery contract handover |
| Skill backlog modes | `STK-001`, `SBG-001` | 2 | Task and Bug filesystem delivery |
| Skill document modes | `SDK-001`, `SDK-002` | 2 | Doc gate, ClickUp grammar and conflict stop |
| Skill story modes | `SST-001` | 1 | Story shape with verbatim hard values |
| Skill interactive routing | `SIR-001` | 1 | Ambiguous intake and clarification export |
| Project identity | `PID-001` | 1 | Project Deliverable Block handover |
| Project backlog modes | `PTK-001`, `PBG-001` | 2 | Task and Bug Deliverable Blocks |
| Project document modes | `PDK-001`, `PDK-002` | 2 | Doc gate and conflict stop in a Project |
| Project story modes | `PST-001` | 1 | Story shape Deliverable Block |
| Project interactive routing | `PIR-001` | 1 | Ambiguous intake and clarification block |

### Two runtimes, one system

Both sets test the same Product Owner contract against the surface that actually runs it, never one system tested twice. A skill-side reply is only genuine when it names a real readable path under `export/` and prints the read-back verification line. A Project-side reply is only genuine when it renders the Deliverable Block as a Canvas Artifact, or as its own block where the runtime has no Canvas panel (section 5), reports `Export-equivalent path:` and claims no file was written. A reply that could have come from either runtime fails the scenario that produced it. The handover files `SID-001` and `PID-001` carry the four greps that prove the vocabulary split, and every other scenario names its runtime's handover as a precondition.

### Realistic test model

1. Prepare a disposable copy of `Product Owner/` for skill-side runs, or a fresh Claude Project holding the kernel and knowledge documents for Project-side runs
2. Start a fresh session unless the scenario explicitly continues the same conversation
3. Submit every turn exactly as written
4. Capture the assistant response, retained state and filesystem changes after every turn
5. Record `PASS`, `FAIL` or a specifically justified `SKIP`

Run every scenario against the real runtime. Do not mock responses.

### No-feature-catalog exception

This skill has no canonical feature catalog. Scenario files link directly to current skill, reference, asset and Project sources. Section 18 is the source cross-reference.

### Natural Turn 1 coverage

At least two scenarios per set open with a Turn 1 that carries no command token, no leading slash and no dollar-prefixed flag: `SDK-001`, `SST-001` and `SIR-001` on the skill side, `PDK-001`, `PST-001` and `PIR-001` on the Project side. The reason is measured rather than stylistic: the 2026-09-16 comparison run on Barter Deal Templates gave two readers the same six prompts, one restricted to that system's Project package and one to its skill, and found that, on that system, a user naming an energy in plain words is covered by no rule in either packaging.

---

## 2. GLOBAL PRECONDITIONS

1. Work only in a disposable project copy for skill-side runs, never inside the authoritative `sk-product-owner/` tree
2. Confirm `AGENTS.md`, `sk-product-owner/` and a writable `export/` directory exist before skill-side runs
3. Attach `claude project/Custom Instructions.md` plus the full `claude project/knowledge/` set before Project-side runs
4. Run the runtime's handover scenario first: `SID-001` leads the `S` set and `PID-001` the `P` set. A failed handover is flagged, never a stop (section 5, Handovers in an automated run)
5. Record `export/` baselines before each skill-side scenario
6. Use a fresh session per ID and keep follow-up turns inside that same ID and session
7. Do not use production credentials, private partner data or live ClickUp access, and never let a ClickUp push become part of a verdict
8. Remove only scenario-created files after evidence capture

No scenario in this package is destructive. Skill-side runs only add new `export/` files inside the disposable copy and Project-side runs write nothing, so precondition 8 is the only cleanup path needed.

### Side-effect ledger

| Turn | Files before | Files after | Created | Modified | Deleted | Allowed? |
|---|---|---|---|---|---|---|
| 1 | Operator capture | Operator capture | Exact paths | Exact paths | Exact paths | Yes/No with reason |

Clarification turns may create only the expected `-clarification` export on the skill side. Project-side runs create no files at all.

---

## 3. GLOBAL EVIDENCE REQUIREMENTS

- Runtime identifier and profile (skill CLI run or Claude Project)
- Exact prompts and the full response after every turn
- Per-turn state-retention notes
- Per-turn side-effect ledger on the skill side
- Resource or knowledge-routing notes when observable
- Export read-back proof on the skill side, or Deliverable Block capture on the Project side
- The `HVR self-scan:` line from every delivery response
- Final `PASS`, `FAIL` or justified `SKIP` with rationale

---

## 4. DETERMINISTIC COMMAND NOTATION

- `sandbox:` prepares or inspects the disposable project copy
- `session:` starts or continues a conversation in the runtime under test
- `user:` submits the exact text shown for a turn
- `filesystem:` records and reads allowed artifacts, skill side only
- `canvas:` inspects the rendered Deliverable Block, Project side only, and reads the reply text where the runtime has no Canvas panel
- `operator:` compares observed behavior with the contract
- `->` separates sequential steps

### Prompt synchronization gate

For every ID, the scenario-contract `Prompt`, the execution-table `Exact Prompt` and the root summary `Prompt` text must match character for character. The `Real user request` line is natural human voice and is not part of this gate.

---

## 5. REVIEW PROTOCOL AND RELEASE READINESS

### Scenario acceptance rules

A scenario passes only when the exact sequence ran, every turn matched expected behavior, prior facts remained intact, the ledger contains only allowed changes and any returned path matches the delivery evidence for that runtime.

- `PASS`: every required check is true
- `FAIL`: any critical signal, state, artifact or boundary is wrong
- `SKIP`: a named sandbox or runtime blocker prevents execution and no safe deterministic fallback exists

Each scenario's Fail bullet names the likely failures and is not a complete list. A turn that misses any Pass clause fails the scenario even when no Fail example describes the miss, so there is no verdict between `PASS` and `FAIL`.

### Clarification turns

A clarification is a delivery on both runtimes. `references/interactive-mode.md` line 85 exports it like any other deliverable and line 93 reports its path exactly as an artifact delivery does. The `Product Owner - System - Interactive Mode` knowledge file says the same for the Project at lines 62 and 70. The `HVR self-scan:` line belongs to every delivery response (`SKILL.md` line 217, `Custom Instructions.md` line 89). Every turn-1 clarification check in this package therefore includes these:

- Skill side: the question-only file saved under its lane's `-clarification` name and read back, and a reply carrying its path, the `Verified: read-back succeeded; N lines` line and the `HVR self-scan:` line. Whether the reply also prints the question is not graded either way. `references/interactive-mode.md` asks the user the question, while `AGENTS.md` Section 2 keeps a full artifact out of chat and the file is that artifact. The tension is logged as a follow-up finding
- Project side: the question rendered as its own block, then `Export-equivalent path:` with the `-clarification` name and the `HVR self-scan:` line

### Rendering without a Canvas panel

The kernel delivers every artifact as a Canvas Artifact in the side Canvas panel and renders the Deliverable Block before any commentary (`Custom Instructions.md` lines 76 and 85). A terminal run, the playbook runner included, gives the Project runtime no Canvas panel. There the block counts as rendered when the artifact or the clarification question sits in the reply as one delimited block, either fenced or opened by its own heading and closed where the `Export-equivalent path:` line begins. Commentary before the block is a response-ordering defect. Record it, and let it fail a scenario only when the scenario tests delivery shape, as Defect severity says. `PID-001` is such a scenario. `canvas:` steps read the reply text, and the panel baseline is empty. The kernel asks for the rendering and the `Export-equivalent path:` label, not for the words, so no reply is graded on printing `Canvas Artifact` or `Deliverable Block`. Record which form the block took.

### Export names

The `[description]` part of every path a scenario names is illustrative, because the rules fix the pattern and not the slug (`SKILL.md` lines 207 and 208, `Custom Instructions.md` lines 222 to 227). Grade the artifact word (`task`, `bug`, `doc`, `PRD` or `intake`) and the `-clarification` suffix on both runtimes. On the skill side grade the order too, with the clarification first and the artifact on the next number. On the Project side `[NNN]` is a placeholder the human reconciles (`Custom Instructions.md` line 232), so number order is not graded there.

### Handovers in an automated run

Every scenario runs in its own fresh sandbox or conversation, so a handover hands nothing on to the scenarios after it. The playbook runner runs `SID-001` and `PID-001` first but does not hold the rest of a set on their verdict. Grade every scenario in both sets, whatever the handovers return. When a handover fails, state that failure at the top of the run report, before any other result, and name the runtime whose other verdicts it puts in question. A scenario whose precondition says its handover passed reads, in an automated run, as the handover having run first in its own session. Its verdict gates nothing.

### Identity handover rule

`SID-001` and `PID-001` prove the runtime, not only the artifact. A reply that could have come from either runtime is a `FAIL`. The proof is graded on Turn 1, because both Turn 2 prompts ask about the delivery and so invite the runtime to name it. The skill side must name a real readable `export/` path and print the read-back confirmation fixture `Verified: read-back succeeded` with its line count. The Project side must render the Deliverable Block, in the form Rendering without a Canvas panel describes when there is no panel, and report `Export-equivalent path:` while claiming no file was written. The skill proof string is `read-back succeeded` and the Project proof string is `Canvas Artifact`. Each handover file carries the four greps that show a proof string appears only in its own identity file. The Project string proves the packaging through those greps and is not required in a reply.

### Defect severity

Record both the verdict and the severity that drove it.

Blocking, any one of which is a `FAIL`:

- An invented fact: a requirement, value, status, approval or behavior the user never supplied
- A protected fact altered: a supplied value generalized, a conflict silently resolved or a proposal promoted to current behavior
- A path claim with no readable file behind it on the skill side, or any file claim at all on the Project side
- A missing `HVR self-scan:` line or a count that was never taken
- Process material inside a delivered artifact body: scores, self-scan lines, mode or energy headers outside a line-1 HTML comment

Advisory, recorded without failing unless the scenario tests delivery shape:

- Response ordering and commentary length
- Progress-note verbosity

### Release readiness rule

The system is ready only when every scenario has evidence, no scenario is `FAIL`, every handover is `PASS`, every `SKIP` names a real blocker and no blocking triage item remains. Documentation validation alone does not prove runtime readiness.

---

## 6. ORCHESTRATION AND WAVE PLANNING

| Wave | Scenarios | Isolation |
|---|---|---|
| 1 | `SID-001`, `PID-001` | One fresh session per runtime, handovers run first |
| 2 | `STK-001`, `SBG-001`, `PTK-001`, `PBG-001` | Separate export baselines per runtime |
| 3 | `SDK-001`, `SDK-002`, `PDK-001`, `PDK-002` | Separate doc baselines, clarification exports allowed |
| 4 | `SST-001`, `PST-001` | Story baselines per runtime |
| 5 | `SIR-001`, `PIR-001` | Intake clarification baselines |

One coordinator owns exact prompts, sandbox isolation, ledgers and final verdicts. Workers may execute independent IDs in separate sandboxes or Projects.

---

## 7. SKILL IDENTITY (`SID-001`)

### SID-001 | Skill identity handover

#### Description

Verify the skill runtime proves itself through the filesystem delivery contract on a routine task request.

#### Scenario contract

Prompt: `$quick $task Create a task for the payout pause toggle. Brands pause a pending payout for 24 hours with a required reason, and QA needs checklist items for the toggle, the reason field and the creator banner.`

Desired user-visible outcome: A saved export, a path-first reply and the skill-only delivery lines.

#### Test execution

> **Feature file:** [SID-001](skill-identity/identity-handover.md)

---

## 8. SKILL BACKLOG MODES (`STK-001..SBG-001`)

### STK-001 | Task command flow

#### Description

Verify `$task` context collection, wait state and canonical task export delivery.

#### Scenario contract

Prompt: `$task I need a task for the creator payout pause feature.`

Desired user-visible outcome: One task-context question followed by a validated task export.

#### Test execution

> **Feature file:** [STK-001](skill-backlog-modes/task-command-flow.md)

### SBG-001 | Bug report flow

#### Description

Verify `$bug` evidence intake and the fixed bug-report structure.

#### Scenario contract

Prompt: `$bug The payout pause toggle silently reverts to off.`

Desired user-visible outcome: One evidence question followed by a compliant bug export.

#### Test execution

> **Feature file:** [SBG-001](skill-backlog-modes/bug-report-flow.md)

---

## 9. SKILL DOCUMENT MODES (`SDK-001..SDK-002`)

### SDK-001 | Doc guide delivery

#### Description

Verify a no-token doc request reaches the source gate and produces a ClickUp-shaped guide.

#### Scenario contract

Prompt: `Document how the notification retry pipeline works for the support team. I will paste the engineering notes.`

Desired user-visible outcome: One consolidated source question followed by a ClickUp-formatted doc export.

#### Test execution

> **Feature file:** [SDK-001](skill-document-modes/doc-guide-delivery.md)

### SDK-002 | Doc conflict gate

#### Description

Verify contradictory sources stop drafting behind one consolidated clarification.

#### Scenario contract

Prompt: `$doc Write a behavior reference for the payout pause feature from these two notes. Note A says the pause holds for 24 hours then releases automatically. Note B says the pause holds until the brand clears it manually.`

Desired user-visible outcome: A clarification export listing the conflict, then one doc export after the user resolves authority.

#### Test execution

> **Feature file:** [SDK-002](skill-document-modes/doc-conflict-gate.md)

---

## 10. SKILL STORY MODES (`SST-001`)

### SST-001 | Story shape hard values

#### Description

Verify story-intake clarification, Story shape selection and verbatim hard values in Requirements.

#### Scenario contract

Prompt: `Turn these notes into a PRD for the payout pause feature.`

Desired user-visible outcome: One story-intake question followed by a house-format Story export naming its kind.

#### Test execution

> **Feature file:** [SST-001](skill-story-modes/story-shape-hard-values.md)

---

## 11. SKILL INTERACTIVE ROUTING (`SIR-001`)

### SIR-001 | Ambiguous intake energy choice

#### Description

Verify the comprehensive question opens with the energy choice and exports an intake clarification.

#### Scenario contract

Prompt: `I need to get something into the backlog for the creator payout flow but I am not sure what shape it should take.`

Desired user-visible outcome: One energy-first question saved as an intake clarification, then a quick task export.

#### Test execution

> **Feature file:** [SIR-001](skill-interactive-routing/ambiguous-intake-energy-choice.md)

---

## 12. PROJECT IDENTITY (`PID-001`)

### PID-001 | Project identity handover

#### Description

Verify the Project runtime proves itself through the Deliverable Block contract on a routine task request.

#### Scenario contract

Prompt: `$quick $task Create a task for the payout pause toggle. Brands pause a pending payout for 24 hours with a required reason, and QA needs checklist items for the toggle, the reason field and the creator banner.`

Desired user-visible outcome: A Canvas Artifact, an export-equivalent label and no file claim.

#### Test execution

> **Feature file:** [PID-001](project-identity/identity-handover.md)

---

## 13. PROJECT BACKLOG MODES (`PTK-001..PBG-001`)

### PTK-001 | Task command flow

#### Description

Verify `$task` context collection, wait state and the Task Deliverable Block.

#### Scenario contract

Prompt: `$task I need a task for the creator payout pause feature.`

Desired user-visible outcome: One task-context question followed by a task block and an export-equivalent label.

#### Test execution

> **Feature file:** [PTK-001](project-backlog-modes/task-command-flow.md)

### PBG-001 | Bug report flow

#### Description

Verify `$bug` evidence intake and the fixed bug-report structure inside a Deliverable Block.

#### Scenario contract

Prompt: `$bug The payout pause toggle silently reverts to off.`

Desired user-visible outcome: One evidence question followed by a compliant bug block.

#### Test execution

> **Feature file:** [PBG-001](project-backlog-modes/bug-report-flow.md)

---

## 14. PROJECT DOCUMENT MODES (`PDK-001..PDK-002`)

### PDK-001 | Doc guide delivery

#### Description

Verify a no-token doc request reaches the source gate and produces a ClickUp-shaped guide block.

#### Scenario contract

Prompt: `Document how the notification retry pipeline works for the support team. I will paste the engineering notes.`

Desired user-visible outcome: One consolidated source question followed by a ClickUp-formatted doc block.

#### Test execution

> **Feature file:** [PDK-001](project-document-modes/doc-guide-delivery.md)

### PDK-002 | Doc conflict gate

#### Description

Verify contradictory sources stop drafting behind one consolidated clarification block.

#### Scenario contract

Prompt: `$doc Write a behavior reference for the payout pause feature from these two notes. Note A says the pause holds for 24 hours then releases automatically. Note B says the pause holds until the brand clears it manually.`

Desired user-visible outcome: A clarification block listing the conflict, then one doc block after the user resolves authority.

#### Test execution

> **Feature file:** [PDK-002](project-document-modes/doc-conflict-gate.md)

---

## 15. PROJECT STORY MODES (`PST-001`)

### PST-001 | Story shape hard values

#### Description

Verify story-intake clarification, Story shape selection and verbatim hard values in Requirements.

#### Scenario contract

Prompt: `Turn these notes into a PRD for the payout pause feature.`

Desired user-visible outcome: One story-intake question followed by a house-format Story block naming its kind.

#### Test execution

> **Feature file:** [PST-001](project-story-modes/story-shape-hard-values.md)

---

## 16. PROJECT INTERACTIVE ROUTING (`PIR-001`)

### PIR-001 | Ambiguous intake energy choice

#### Description

Verify the comprehensive question opens with the energy choice and delivers an intake clarification block.

#### Scenario contract

Prompt: `I need to get something into the backlog for the creator payout flow but I am not sure what shape it should take.`

Desired user-visible outcome: One energy-first question labelled as an intake clarification, then a quick task block.

#### Test execution

> **Feature file:** [PIR-001](project-interactive-routing/ambiguous-intake-energy-choice.md)

---

## 17. AUTOMATED VALIDATION CROSS-REFERENCE

| Check | Coverage | Playbook overlap |
|---|---|---|
| [`../../benchmark/router/run_fixtures.sh`](../../benchmark/router/run_fixtures.sh) | Router differential against `route_contract.py` | `STK-001`, `SBG-001`, `SDK-001`, `SST-001`, `SIR-001` and Project mirrors |
| [`../../benchmark/format/run_fixtures.sh`](../../benchmark/format/run_fixtures.sh) | Output-format gate on this system's instruction surface | All delivered artifact shapes |
| [`../../benchmark/parity/`](../../benchmark/parity/) scripts | Kernel-to-skill parity and residency checks | `PID-001`, `SID-001` |
| Playbook package validator | Paths, IDs, sections, prompts, tables, links | This package |
| Real manual execution | Runtime behavior and side effects | `SID-001..PIR-001` |

---

## 18. SOURCE CROSS-REFERENCE INDEX

| Feature ID | Feature name | Category | Feature file | Primary source |
|---|---|---|---|---|
| SID-001 | Skill identity handover | Skill identity | [SID-001](skill-identity/identity-handover.md) | [`AGENTS.md`](../../AGENTS.md) |
| STK-001 | Task command flow | Skill backlog modes | [STK-001](skill-backlog-modes/task-command-flow.md) | [`task-mode.md`](../references/task-mode.md) |
| SBG-001 | Bug report flow | Skill backlog modes | [SBG-001](skill-backlog-modes/bug-report-flow.md) | [`bug-mode.md`](../references/bug-mode.md) |
| SDK-001 | Doc guide delivery | Skill document modes | [SDK-001](skill-document-modes/doc-guide-delivery.md) | [`doc-mode.md`](../references/doc-mode.md) |
| SDK-002 | Doc conflict gate | Skill document modes | [SDK-002](skill-document-modes/doc-conflict-gate.md) | [`doc-mode.md`](../references/doc-mode.md) |
| SST-001 | Story shape hard values | Skill story modes | [SST-001](skill-story-modes/story-shape-hard-values.md) | [`story-mode.md`](../references/story-mode.md) |
| SIR-001 | Ambiguous intake energy choice | Skill interactive routing | [SIR-001](skill-interactive-routing/ambiguous-intake-energy-choice.md) | [`interactive-mode.md`](../references/interactive-mode.md) |
| PID-001 | Project identity handover | Project identity | [PID-001](project-identity/identity-handover.md) | [`Custom Instructions.md`](../../claude%20project/Custom%20Instructions.md) |
| PTK-001 | Task command flow | Project backlog modes | [PTK-001](project-backlog-modes/task-command-flow.md) | [`Custom Instructions.md`](../../claude%20project/Custom%20Instructions.md) |
| PBG-001 | Bug report flow | Project backlog modes | [PBG-001](project-backlog-modes/bug-report-flow.md) | [`Custom Instructions.md`](../../claude%20project/Custom%20Instructions.md) |
| PDK-001 | Doc guide delivery | Project document modes | [PDK-001](project-document-modes/doc-guide-delivery.md) | [`Custom Instructions.md`](../../claude%20project/Custom%20Instructions.md) |
| PDK-002 | Doc conflict gate | Project document modes | [PDK-002](project-document-modes/doc-conflict-gate.md) | [`Custom Instructions.md`](../../claude%20project/Custom%20Instructions.md) |
| PST-001 | Story shape hard values | Project story modes | [PST-001](project-story-modes/story-shape-hard-values.md) | [`Custom Instructions.md`](../../claude%20project/Custom%20Instructions.md) |
| PIR-001 | Ambiguous intake energy choice | Project interactive routing | [PIR-001](project-interactive-routing/ambiguous-intake-energy-choice.md) | [`Custom Instructions.md`](../../claude%20project/Custom%20Instructions.md) |
