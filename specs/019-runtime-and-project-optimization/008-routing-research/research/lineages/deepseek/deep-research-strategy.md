---
title: Deep Research Strategy - Product Owner routing, mode links and repository hygiene
description: Runtime strategy file for the deepseek fan-out lineage of packet z-staging-po-019s. Tracks research progress, focus decisions, and outcomes across ten iterations.
trigger_phrases:
  - "deep research strategy"
  - "product owner routing research"
  - "repository hygiene research"
importance_tier: normal
contextType: planning
version: 1.15.7.0
---

# Deep Research Strategy - Product Owner routing, mode links and repository hygiene

## 1. OVERVIEW

### Purpose

Persistent brain for this research lineage. Records what to investigate, what worked, what failed, and where to focus next. Read before every iteration.

### Usage

- **Init:** The lineage executor populated Topic, Key Questions, Known Context and Research Boundaries from the staging spec, the steer file and the Product Owner tree.
- **Per iteration:** the executor reads Next Focus, writes the iteration file and delta, and the reducer refreshes the machine-owned sections after each gateway append.
- **Mutability:** Section 3 and Sections 6-11A are reducer-owned. Sections 2, 4, 5, 12 and 13 are analyst-owned.

---

## 2. TOPIC

Product Owner routing in the parent hub, how its modes connect, routing in the Claude Project, README currency, dead code and documents, and code alignment with sk-code-skilled, as `specs/z-staging-po-019s/spec.md` scopes it. The research target is `AI Systems/Product Owner/`.

---

<!-- ANCHOR:key-questions -->
## 3. KEY QUESTIONS (remaining)
- [x] How does the Product Owner parent route a request to a mode, where is routing logic stated more than once, where do the copies disagree, and what is the smallest set of routing sources that still serves the CLI, the hub and the Claude Project?
- [x] Which router copies are held equal by a gate such as benchmark/router/differential.py, and which drift unchecked?
- [x] Where is a hand-off between modes undefined, duplicated or contradictory?
- [x] Is routing embedded in the right Claude Project layer, and what could shrink without losing a rule that must fire every turn?
- [x] What are the concrete, ranked routing and mode-link changes, each with the files it touches, its risk, the gate that proves it and the byte effect on the kernel?
- [x] Which README claims are stale against the files they describe?
- [x] Which scripts, functions, flags and config entries are dead code?
- [x] Which references, assets, examples and playbook files are dead documents?
- [x] How does the Product Owner's own Python, shell, JavaScript and JSON deviate from the sk-code-skilled standards?
- [x] What is the ranked synthesis of every finding, and what can the repository not settle?

<!-- /ANCHOR:key-questions -->

---

## 4. NON-GOALS

- Editing, fixing or re-designing anything under `AI Systems/Product Owner/`; this is a read-only research run.
- `Product Owner/specs/`, `Product Owner/export/`, `Product Owner/benchmark/reports/`, and the vendored packets `mcp-click-up/`, `mcp-figma/` and `mcp-code-mode/`.
- `AI Systems/Product Context`, any screenshot and any figma.com URL.
- Building a replacement router; the deliverable is findings and ranked options with cited evidence.

---

## 5. STOP CONDITIONS

- `config.maxIterations` (10) reached; convergence is telemetry only under `stopPolicy: max-iterations`.
- Three consecutive unrecoverable tool failures on the same call.

---

<!-- ANCHOR:answered-questions -->
## 6. ANSWERED QUESTIONS
- How does the Product Owner parent route a request to a mode, where is routing logic stated more than once, where do the copies disagree, and what is the smallest set of routing sources that still serves the CLI, the hub and the Claude Project?
- Which router copies are held equal by a gate such as benchmark/router/differential.py, and which drift unchecked?
- Where is a hand-off between modes undefined, duplicated or contradictory?
- Is routing embedded in the right Claude Project layer, and what could shrink without losing a rule that must fire every turn?
- What are the concrete, ranked routing and mode-link changes, each with the files it touches, its risk, the gate that proves it and the byte effect on the kernel?
- Which README claims are stale against the files they describe?
- Which scripts, functions, flags and config entries are dead code?
- Which references, assets, examples and playbook files are dead documents?
- How does the Product Owner's own Python, shell, JavaScript and JSON deviate from the sk-code-skilled standards?
- What is the ranked synthesis of every finding, and what can the repository not settle?

<!-- /ANCHOR:answered-questions -->

---

<!-- MACHINE-OWNED: START -->
<!-- ANCHOR:what-worked -->
## 7. WHAT WORKED
- Reading the hub files first and then their gates separated the live authority from the descriptive copies; running the compiled-route command settled a claim no document could settle alone (iteration 1)
- Reading the gate source instead of its README separated the four guards the prose names from the five the harness runs, and showed exactly which lanes table parity skips (iteration 2)
- Reading each mode's Hands Off To header beside its command list exposed the two contradictions quickly, because the header states the hand-off and the command list states the exception (iteration 3)
- Measuring each section's bytes rather than counting lines made the shrink candidate concrete, because Section 11 is two thirds of the lines and only 39 percent of the bytes (iteration 4)
- Ranking by gate coverage as well as by value put changes 2, 3 and 4 first, because each is a small edit with an existing gate that would prove it (iteration 5)
- Checking each number against the file or the folder rather than against another README found three stale counts and cleared every other claim (iteration 6)
- Comparing the plugin build copy file by file against its sources turned a general freshness worry into one exact stale line, which no gate reports (iteration 7)
- Testing reachability through leaf-manifest, ROUTER and the lane tables instead of the link graph answered the question with evidence and cleared 73 leaves at once (iteration 8)
- Reading the standards first and then running exactly the checks they name turned a vague style question into six named deviations and three clean results (iteration 9)
- Ranking by what produces a wrong artifact separated three contract clusters from the documentation and style findings, which would otherwise have diluted the list (iteration 10)

<!-- /ANCHOR:what-worked -->

---

<!-- ANCHOR:what-failed -->
## 8. WHAT FAILED
- The first pass treated ROUTER.md as ungated because check_hub does not read it; the skilled hub contract does, through a different gate row (iteration 1)
- The first assumption that ROUTER.md was unverified was wrong; the skilled root-router contract checks it, which is why the two maps can both be green and still disagree (iteration 2)
- The first pass assumed the Doc shape count had drifted; the five shapes match in all three files, so that lead was dropped (iteration 3)
- The first draft proposed trimming Section 11 without noticing that copy parity forbids a kernel-only edit (iteration 4)
- The first version of change 7 proposed deleting router-contract's map, which differential needs as the executed reference; the option was rewritten as an ownership decision (iteration 5)
- The first pass assumed the root README's counts would be the stale ones; it is the most current of the three documents and the gate README the oldest (iteration 6)
- The first dead-code scan folded markdown into the reference count, so a function named only in a README looked live; rerunning on code only made the result trustworthy (iteration 7)
- The first link pass compared encoded URLs and normalized paths differently, so valid claude-project links looked broken and every file looked orphaned (iteration 8)
- The first pass walked the whole tree and spent its output on specs containment copies and node_modules, which are neither in scope nor edited here (iteration 9)
- The first draft ranked every finding by severity alone and put the cheapest cosmetic fixes beside the map unification; splitting severity from order fixed it (iteration 10)

<!-- /ANCHOR:what-failed -->

---

<!-- ANCHOR:exhausted-approaches -->
## 9. EXHAUSTED APPROACHES (do not retry)
### Adding a compiled activation manifest for product-owner to make the directive live: the hub gate and the gold rows would then measure a router nobody exercised, and admission needs a scored scenario per mode first -- BLOCKED (iteration 5, 1 attempts)
- What was tried: Adding a compiled activation manifest for product-owner to make the directive live: the hub gate and the gold rows would then measure a router nobody exercised, and admission needs a scored scenario per mode first
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Adding a compiled activation manifest for product-owner to make the directive live: the hub gate and the gold rows would then measure a router nobody exercised, and admission needs a scored scenario per mode first

### Blending the P0 hand-off findings into one fix: each contract lives in a different file and needs its own scenario, and bundling them is how one gets silently dropped -- BLOCKED (iteration 10, 1 attempts)
- What was tried: Blending the P0 hand-off findings into one fix: each contract lives in a different file and needs its own scenario, and bundling them is how one gets silently dropped
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Blending the P0 hand-off findings into one fix: each contract lives in a different file and needs its own scenario, and bundling them is how one gets silently dropped

### Calling figjam assets/templates/user-flow.md dead: no such file exists, and user flow patterns live in assets/flow-templates.md, which every Flow route loads -- BLOCKED (iteration 8, 1 attempts)
- What was tried: Calling figjam assets/templates/user-flow.md dead: no such file exists, and user flow patterns live in assets/flow-templates.md, which every Flow route loads
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Calling figjam assets/templates/user-flow.md dead: no such file exists, and user flow patterns live in assets/flow-templates.md, which every Flow route loads

### Calling figjam_checks/fixtures.py dead because flow_check does not import it at module load: it is imported inside the self-test at line 211 and every planted model in it is used -- BLOCKED (iteration 7, 1 attempts)
- What was tried: Calling figjam_checks/fixtures.py dead because flow_check does not import it at module load: it is imported inside the self-test at line 211 and every planted model in it is used
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Calling figjam_checks/fixtures.py dead because flow_check does not import it at module load: it is imported inside the self-test at line 211 and every planted model in it is used

### Calling route_contract.py --self-check dead: the root README documents it as a one-sample-per-layer smoke test -- BLOCKED (iteration 7, 1 attempts)
- What was tried: Calling route_contract.py --self-check dead: the root README documents it as a one-sample-per-layer smoke test
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Calling route_contract.py --self-check dead: the root README documents it as a one-sample-per-layer smoke test

### Calling the 35 benchmark company fixtures dead: every one is named by at least one playbook scenario -- BLOCKED (iteration 8, 1 attempts)
- What was tried: Calling the 35 benchmark company fixtures dead: every one is named by at least one playbook scenario
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Calling the 35 benchmark company fixtures dead: every one is named by at least one playbook scenario

### Calling the figjam playbook's 52 scenarios unlinked: its index links them with a Feature File anchor the first extractor missed -- BLOCKED (iteration 8, 1 attempts)
- What was tried: Calling the figjam playbook's 52 scenarios unlinked: its index links them with a Feature File anchor the first extractor missed
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Calling the figjam playbook's 52 scenarios unlinked: its index links them with a Feature File anchor the first extractor missed

### Calling the five benchmark/parity wrappers dead: they are documented manual checks, and run_gates.sh explains why they are not in the automatic list -- BLOCKED (iteration 7, 1 attempts)
- What was tried: Calling the five benchmark/parity wrappers dead: they are documented manual checks, and run_gates.sh explains why they are not in the automatic list
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Calling the five benchmark/parity wrappers dead: they are documented manual checks, and run_gates.sh explains why they are not in the automatic list

### Calling the nine missing -e flags a defect: a runner that must count failures cannot exit on the first one, and run_gates.sh documents the counting behaviour -- BLOCKED (iteration 9, 1 attempts)
- What was tried: Calling the nine missing -e flags a defect: a runner that must count failures cannot exit on the first one, and run_gates.sh documents the counting behaviour
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Calling the nine missing -e flags a defect: a runner that must count failures cannot exit on the first one, and run_gates.sh documents the counting behaviour

### Counting inbound markdown links as reachability: it marked 549 files orphan, including every routed reference, because the manifest and the lane tables are the real load path -- BLOCKED (iteration 8, 1 attempts)
- What was tried: Counting inbound markdown links as reachability: it marked 549 files orphan, including every routed reference, because the manifest and the lane tables are the real load path
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Counting inbound markdown links as reachability: it marked 549 files orphan, including every routed reference, because the manifest and the lane tables are the real load path

### Counting the gold-row replay as a stage-one specification gate: it tests a replica against expectations, not the prose against the replica -- BLOCKED (iteration 2, 1 attempts)
- What was tried: Counting the gold-row replay as a stage-one specification gate: it tests a replica against expectations, not the prose against the replica
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Counting the gold-row replay as a stage-one specification gate: it tests a replica against expectations, not the prose against the replica

### Deleting the stage-one prose without moving its worked examples into hub-router.json: the examples in rules 3 and 4 are the only place the tool-signal-versus-artifact collision is explained -- BLOCKED (iteration 5, 1 attempts)
- What was tried: Deleting the stage-one prose without moving its worked examples into hub-router.json: the examples in rules 3 and 4 are the only place the tool-signal-versus-artifact collision is explained
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Deleting the stage-one prose without moving its worked examples into hub-router.json: the examples in rules 3 and 4 are the only place the tool-signal-versus-artifact collision is explained

### Looking for a Broken Full detail pointer: all 18 name one of five targets and all five exist in the knowledge folder -- BLOCKED (iteration 4, 1 attempts)
- What was tried: Looking for a Broken Full detail pointer: all 18 name one of five targets and all five exist in the knowledge folder
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Looking for a Broken Full detail pointer: all 18 name one of five targets and all five exist in the knowledge folder

### Looking for a Deep or Raw branch in the executable router: detect_energy has two returns and no other energy vocabulary -- BLOCKED (iteration 3, 1 attempts)
- What was tried: Looking for a Deep or Raw branch in the executable router: detect_energy has two returns and no other energy vocabulary
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Looking for a Deep or Raw branch in the executable router: detect_energy has two returns and no other energy vocabulary

### Looking for a Flows group in the bug report template: the scaffold has no such group, which is what makes the Bug-plus-FigJam pair unwritable -- BLOCKED (iteration 3, 1 attempts)
- What was tried: Looking for a Flows group in the bug report template: the scaffold has no such group, which is what makes the Bug-plus-FigJam pair unwritable
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Looking for a Flows group in the bug report template: the scaffold has no such group, which is what makes the Bug-plus-FigJam pair unwritable

### Looking for a gate that reads a README count: none does, which is why three documents kept the old number while one was updated -- BLOCKED (iteration 6, 1 attempts)
- What was tried: Looking for a gate that reads a README count: none does, which is why three documents kept the old number while one was updated
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Looking for a gate that reads a README count: none does, which is why three documents kept the old number while one was updated

### Looking for a gate that would prove a kernel prose deletion safe: none exists; only the hand parity review in SYNC.md covers rule retention -- BLOCKED (iteration 5, 1 attempts)
- What was tried: Looking for a gate that would prove a kernel prose deletion safe: none exists; only the hand parity review in SYNC.md covers rule retention
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Looking for a gate that would prove a kernel prose deletion safe: none exists; only the hand parity review in SYNC.md covers rule retention

### Looking for a Product Owner activation manifest for compiled routing under .skilled: no manifest exists, and the resolver falls back to legacy by design -- BLOCKED (iteration 1, 1 attempts)
- What was tried: Looking for a Product Owner activation manifest for compiled routing under .skilled: no manifest exists, and the resolver falls back to legacy by design
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Looking for a Product Owner activation manifest for compiled routing under .skilled: no manifest exists, and the resolver falls back to legacy by design

### Looking for a second Python fence or a pasted router definition in SKILL.md or routing.md: both are refused by copy parity, which is why the prose copies are prose only -- BLOCKED (iteration 2, 1 attempts)
- What was tried: Looking for a second Python fence or a pasted router definition in SKILL.md or routing.md: both are refused by copy parity, which is why the prose copies are prose only
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Looking for a second Python fence or a pasted router definition in SKILL.md or routing.md: both are refused by copy parity, which is why the prose copies are prose only

### Looking for dead code or dead documents to rank: none exists, so the ranked list is contracts, gates and documentation instead -- BLOCKED (iteration 10, 1 attempts)
- What was tried: Looking for dead code or dead documents to rank: none exists, so the ranked list is contracts, gates and documentation instead
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Looking for dead code or dead documents to rank: none exists, so the ranked list is contracts, gates and documentation instead

### Looking for tabs or missing trailing newlines in JSON: none in ten files -- BLOCKED (iteration 9, 1 attempts)
- What was tried: Looking for tabs or missing trailing newlines in JSON: none in ten files
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Looking for tabs or missing trailing newlines in JSON: none in ten files

### Moving routing out of the kernel into Knowledge: retrieval by relevance cannot guarantee a decision that must fire on every turn, and differential explicitly treats a Router Contract knowledge document as a failure -- BLOCKED (iteration 4, 1 attempts)
- What was tried: Moving routing out of the kernel into Knowledge: retrieval by relevance cannot guarantee a decision that must fire on every turn, and differential explicitly treats a Router Contract knowledge document as a failure
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Moving routing out of the kernel into Knowledge: retrieval by relevance cannot guarantee a decision that must fire on every turn, and differential explicitly treats a Router Contract knowledge document as a failure

### Quoting a kernel-only shrink of Section 11: copy parity makes the kernel and router-contract.md one edit -- BLOCKED (iteration 4, 1 attempts)
- What was tried: Quoting a kernel-only shrink of Section 11: copy parity makes the kernel and router-contract.md one edit
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Quoting a kernel-only shrink of Section 11: copy parity makes the kernel and router-contract.md one edit

### Reporting the four documented energies as a kernel bug: the kernel may legitimately offer Raw as an intake signal the resolver never emits, which is why it is an owner question rather than a defect -- BLOCKED (iteration 10, 1 attempts)
- What was tried: Reporting the four documented energies as a kernel bug: the kernel may legitimately offer Raw as an intake signal the resolver never emits, which is why it is an owner question rather than a defect
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Reporting the four documented energies as a kernel bug: the kernel may legitimately offer Raw as an intake signal the resolver never emits, which is why it is an owner question rather than a defect

### Searching for a gate that would have caught the stale plugin copy, the link drift or the four unread config entries: no gate reads any of them -- BLOCKED (iteration 10, 1 attempts)
- What was tried: Searching for a gate that would have caught the stale plugin copy, the link drift or the four unread config entries: no gate reads any of them
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Searching for a gate that would have caught the stale plugin copy, the link drift or the four unread config entries: no gate reads any of them

### Searching for a leaf that no lane names: every leaf is covered either by name or by a directory token, so the only miss is routing.md getting prose mention instead of a lane -- BLOCKED (iteration 8, 1 attempts)
- What was tried: Searching for a leaf that no lane names: every leaf is covered either by name or by a directory token, so the only miss is routing.md getting prose mention instead of a lane
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Searching for a leaf that no lane names: every leaf is covered either by name or by a directory token, so the only miss is routing.md getting prose mention instead of a lane

### Searching for a Python stderr or exit-code rule in the standard: the standard states neither, so printing gate findings to stdout and using exit codes is not a deviation -- BLOCKED (iteration 9, 1 attempts)
- What was tried: Searching for a Python stderr or exit-code rule in the standard: the standard states neither, so printing gate findings to stdout and using exit codes is not a deviation
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Searching for a Python stderr or exit-code rule in the standard: the standard states neither, so printing gate findings to stdout and using exit codes is not a deviation

### Searching for a script basename with a single reference: every basename resolved to at least a caller and its own definition -- BLOCKED (iteration 7, 1 attempts)
- What was tried: Searching for a script basename with a single reference: every basename resolved to at least a caller and its own definition
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Searching for a script basename with a single reference: every basename resolved to at least a caller and its own definition

### Searching for a zero-reference top-level function or UPPER constant in the 21 definition-bearing files: none was found, in code-only reference counting -- BLOCKED (iteration 7, 1 attempts)
- What was tried: Searching for a zero-reference top-level function or UPPER constant in the 21 definition-bearing files: none was found, in code-only reference counting
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Searching for a zero-reference top-level function or UPPER constant in the 21 definition-bearing files: none was found, in code-only reference counting

### Treating 'all 12 gates pass' as stale: run_gates.sh declares twelve entries and the four clone-time skips are exactly the ones its README names -- BLOCKED (iteration 6, 1 attempts)
- What was tried: Treating 'all 12 gates pass' as stale: run_gates.sh declares twelve entries and the four clone-time skips are exactly the ones its README names
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Treating 'all 12 gates pass' as stale: run_gates.sh declares twelve entries and the four clone-time skips are exactly the ones its README names

### Treating 'Section 7 Push Targets' as a dangling pointer: Section 7 INTEGRATION POINTS does contain a Push Targets subsection -- BLOCKED (iteration 3, 1 attempts)
- What was tried: Treating 'Section 7 Push Targets' as a dangling pointer: Section 7 INTEGRATION POINTS does contain a Push Targets subsection
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Treating 'Section 7 Push Targets' as a dangling pointer: Section 7 INTEGRATION POINTS does contain a Push Targets subsection

### Treating kernel-review.json as a live version record: its own note says nothing reads it and the live versions are the kernel H1 and the dated notes in SYNC.md -- BLOCKED (iteration 4, 1 attempts)
- What was tried: Treating kernel-review.json as a live version record: its own note says nothing reads it and the live versions are the kernel H1 and the dated notes in SYNC.md
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Treating kernel-review.json as a live version record: its own note says nothing reads it and the live versions are the kernel H1 and the dated notes in SYNC.md

### Treating leaf-manifest.json as a routing source: it is a generated inventory of (workflowMode, leaf) pairs with no intent or policy -- BLOCKED (iteration 1, 1 attempts)
- What was tried: Treating leaf-manifest.json as a routing source: it is a generated inventory of (workflowMode, leaf) pairs with no intent or policy
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Treating leaf-manifest.json as a routing source: it is a generated inventory of (workflowMode, leaf) pairs with no intent or policy

### Treating mode-registry.json aliases as hub routing keywords: they are advisor aliases (task, bug, story, epic, prd, doc, figjam, cupt) and are not read by stage one -- BLOCKED (iteration 1, 1 attempts)
- What was tried: Treating mode-registry.json aliases as hub routing keywords: they are advisor aliases (task, bug, story, epic, prd, doc, figjam, cupt) and are not read by stage one
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Treating mode-registry.json aliases as hub routing keywords: they are advisor aliases (task, bug, story, epic, prd, doc, figjam, cupt) and are not read by stage one

### Treating sk-create-figjam/ROUTER.md as an existing copy: the file is absent and a hub gate forbids it -- BLOCKED (iteration 2, 1 attempts)
- What was tried: Treating sk-create-figjam/ROUTER.md as an existing copy: the file is absent and a hub gate forbids it
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Treating sk-create-figjam/ROUTER.md as an existing copy: the file is absent and a hub gate forbids it

### Treating the 191-character component headers as line-length violations: they are the house header rule, and the 59 remaining lines are measured with comment lines exempted -- BLOCKED (iteration 9, 1 attempts)
- What was tried: Treating the 191-character component headers as line-length violations: they are the house header rule, and the 59 remaining lines are measured with comment lines exempted
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Treating the 191-character component headers as line-length violations: they are the house header rule, and the 59 remaining lines are measured with comment lines exempted

### Treating the claude project README's 63-file upload list as stale: the folder holds 63 markdown files, 35 core and 28 examples -- BLOCKED (iteration 6, 1 attempts)
- What was tried: Treating the claude project README's 63-file upload list as stale: the folder holds 63 markdown files, 35 core and 28 examples
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Treating the claude project README's 63-file upload list as stale: the folder holds 63 markdown files, 35 core and 28 examples

### Treating the compiled router as the current stage-one authority: the command returns {"servingAuthority":"legacy"} for product-owner, so the legacy rules are the live authority -- BLOCKED (iteration 1, 1 attempts)
- What was tried: Treating the compiled router as the current stage-one authority: the command returns {"servingAuthority":"legacy"} for product-owner, so the legacy rules are the live authority
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Treating the compiled router as the current stage-one authority: the command returns {"servingAuthority":"legacy"} for product-owner, so the legacy rules are the live authority

### Treating the differential corpus group named known-divergences as an exemption: compare_input applies to every corpus input with no exception list, so those two entries must now agree -- BLOCKED (iteration 2, 1 attempts)
- What was tried: Treating the differential corpus group named known-divergences as an exemption: compare_input applies to every corpus input with no exception list, so those two entries must now agree
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Treating the differential corpus group named known-divergences as an exemption: compare_input applies to every corpus input with no exception list, so those two entries must now agree

### Treating the Doc shapes as inconsistent: the five shapes are named identically in routing.md, doc-mode.md and doc-templates.md -- BLOCKED (iteration 3, 1 attempts)
- What was tried: Treating the Doc shapes as inconsistent: the five shapes are named identically in routing.md, doc-mode.md and doc-templates.md
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Treating the Doc shapes as inconsistent: the five shapes are named identically in routing.md, doc-mode.md and doc-templates.md

### Treating the root README's 21 plus 7 example split as stale: the knowledge folder holds exactly 5 Task, 4 Bug, 7 Doc, 5 Story and 7 Flow mirrors -- BLOCKED (iteration 6, 1 attempts)
- What was tried: Treating the root README's 21 plus 7 example split as stale: the knowledge folder holds exactly 5 Task, 4 Bug, 7 Doc, 5 Story and 7 Flow mirrors
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Treating the root README's 21 plus 7 example split as stale: the knowledge folder holds exactly 5 Task, 4 Bug, 7 Doc, 5 Story and 7 Flow mirrors

### Treating the routing defect count as a reason to rewrite the router: three implementations are already held equal by differential.py, and the defects are contract statements, not algorithms -- BLOCKED (iteration 10, 1 attempts)
- What was tried: Treating the routing defect count as a reason to rewrite the router: three implementations are already held equal by differential.py, and the defects are contract statements, not algorithms
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Treating the routing defect count as a reason to rewrite the router: three implementations are already held equal by differential.py, and the defects are contract statements, not algorithms

### Treating the Story-with-nested-tasks bundle as a two-artifact conflict: Story Mode explicitly says it is one dependent deliverable and only two explicit commands conflict -- BLOCKED (iteration 3, 1 attempts)
- What was tried: Treating the Story-with-nested-tasks bundle as a two-artifact conflict: Story Mode explicitly says it is one dependent deliverable and only two explicit commands conflict
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Treating the Story-with-nested-tasks bundle as a two-artifact conflict: Story Mode explicitly says it is one dependent deliverable and only two explicit commands conflict

### Treating unquoted-variable style as weak: shellcheck at info level reports nothing on any of the nine scripts -- BLOCKED (iteration 9, 1 attempts)
- What was tried: Treating unquoted-variable style as weak: shellcheck at info level reports nothing on any of the nine scripts
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Treating unquoted-variable style as weak: shellcheck at info level reports nothing on any of the nine scripts

### Trimming Section 11 to shrink the kernel: copy parity makes the kernel and router-contract.md a single edit, so a kernel-only trim cannot land -- BLOCKED (iteration 5, 1 attempts)
- What was tried: Trimming Section 11 to shrink the kernel: copy parity makes the kernel and router-contract.md a single edit, so a kernel-only trim cannot land
- Why blocked: Repeated iteration evidence ruled this direction out.
- Do NOT retry: Trimming Section 11 to shrink the kernel: copy parity makes the kernel and router-contract.md a single edit, so a kernel-only trim cannot land

<!-- /ANCHOR:exhausted-approaches -->

---

<!-- ANCHOR:ruled-out-directions -->
## 10. RULED OUT DIRECTIONS
- Looking for a Product Owner activation manifest for compiled routing under .skilled: no manifest exists, and the resolver falls back to legacy by design (iteration 1)
- Treating leaf-manifest.json as a routing source: it is a generated inventory of (workflowMode, leaf) pairs with no intent or policy (iteration 1)
- Treating mode-registry.json aliases as hub routing keywords: they are advisor aliases (task, bug, story, epic, prd, doc, figjam, cupt) and are not read by stage one (iteration 1)
- Treating the compiled router as the current stage-one authority: the command returns {"servingAuthority":"legacy"} for product-owner, so the legacy rules are the live authority (iteration 1)
- Counting the gold-row replay as a stage-one specification gate: it tests a replica against expectations, not the prose against the replica (iteration 2)
- Looking for a second Python fence or a pasted router definition in SKILL.md or routing.md: both are refused by copy parity, which is why the prose copies are prose only (iteration 2)
- Treating sk-create-figjam/ROUTER.md as an existing copy: the file is absent and a hub gate forbids it (iteration 2)
- Treating the differential corpus group named known-divergences as an exemption: compare_input applies to every corpus input with no exception list, so those two entries must now agree (iteration 2)
- Looking for a Deep or Raw branch in the executable router: detect_energy has two returns and no other energy vocabulary (iteration 3)
- Looking for a Flows group in the bug report template: the scaffold has no such group, which is what makes the Bug-plus-FigJam pair unwritable (iteration 3)
- Treating 'Section 7 Push Targets' as a dangling pointer: Section 7 INTEGRATION POINTS does contain a Push Targets subsection (iteration 3)
- Treating the Doc shapes as inconsistent: the five shapes are named identically in routing.md, doc-mode.md and doc-templates.md (iteration 3)
- Treating the Story-with-nested-tasks bundle as a two-artifact conflict: Story Mode explicitly says it is one dependent deliverable and only two explicit commands conflict (iteration 3)
- Looking for a Broken Full detail pointer: all 18 name one of five targets and all five exist in the knowledge folder (iteration 4)
- Moving routing out of the kernel into Knowledge: retrieval by relevance cannot guarantee a decision that must fire on every turn, and differential explicitly treats a Router Contract knowledge document as a failure (iteration 4)
- Quoting a kernel-only shrink of Section 11: copy parity makes the kernel and router-contract.md one edit (iteration 4)
- Treating kernel-review.json as a live version record: its own note says nothing reads it and the live versions are the kernel H1 and the dated notes in SYNC.md (iteration 4)
- Adding a compiled activation manifest for product-owner to make the directive live: the hub gate and the gold rows would then measure a router nobody exercised, and admission needs a scored scenario per mode first (iteration 5)
- Deleting the stage-one prose without moving its worked examples into hub-router.json: the examples in rules 3 and 4 are the only place the tool-signal-versus-artifact collision is explained (iteration 5)
- Looking for a gate that would prove a kernel prose deletion safe: none exists; only the hand parity review in SYNC.md covers rule retention (iteration 5)
- Trimming Section 11 to shrink the kernel: copy parity makes the kernel and router-contract.md a single edit, so a kernel-only trim cannot land (iteration 5)
- Looking for a gate that reads a README count: none does, which is why three documents kept the old number while one was updated (iteration 6)
- Treating 'all 12 gates pass' as stale: run_gates.sh declares twelve entries and the four clone-time skips are exactly the ones its README names (iteration 6)
- Treating the claude project README's 63-file upload list as stale: the folder holds 63 markdown files, 35 core and 28 examples (iteration 6)
- Treating the root README's 21 plus 7 example split as stale: the knowledge folder holds exactly 5 Task, 4 Bug, 7 Doc, 5 Story and 7 Flow mirrors (iteration 6)
- Calling figjam_checks/fixtures.py dead because flow_check does not import it at module load: it is imported inside the self-test at line 211 and every planted model in it is used (iteration 7)
- Calling route_contract.py --self-check dead: the root README documents it as a one-sample-per-layer smoke test (iteration 7)
- Calling the five benchmark/parity wrappers dead: they are documented manual checks, and run_gates.sh explains why they are not in the automatic list (iteration 7)
- Searching for a script basename with a single reference: every basename resolved to at least a caller and its own definition (iteration 7)
- Searching for a zero-reference top-level function or UPPER constant in the 21 definition-bearing files: none was found, in code-only reference counting (iteration 7)
- Calling figjam assets/templates/user-flow.md dead: no such file exists, and user flow patterns live in assets/flow-templates.md, which every Flow route loads (iteration 8)
- Calling the 35 benchmark company fixtures dead: every one is named by at least one playbook scenario (iteration 8)
- Calling the figjam playbook's 52 scenarios unlinked: its index links them with a Feature File anchor the first extractor missed (iteration 8)
- Counting inbound markdown links as reachability: it marked 549 files orphan, including every routed reference, because the manifest and the lane tables are the real load path (iteration 8)
- Searching for a leaf that no lane names: every leaf is covered either by name or by a directory token, so the only miss is routing.md getting prose mention instead of a lane (iteration 8)
- Calling the nine missing -e flags a defect: a runner that must count failures cannot exit on the first one, and run_gates.sh documents the counting behaviour (iteration 9)
- Looking for tabs or missing trailing newlines in JSON: none in ten files (iteration 9)
- Searching for a Python stderr or exit-code rule in the standard: the standard states neither, so printing gate findings to stdout and using exit codes is not a deviation (iteration 9)
- Treating the 191-character component headers as line-length violations: they are the house header rule, and the 59 remaining lines are measured with comment lines exempted (iteration 9)
- Treating unquoted-variable style as weak: shellcheck at info level reports nothing on any of the nine scripts (iteration 9)
- Blending the P0 hand-off findings into one fix: each contract lives in a different file and needs its own scenario, and bundling them is how one gets silently dropped (iteration 10)
- Looking for dead code or dead documents to rank: none exists, so the ranked list is contracts, gates and documentation instead (iteration 10)
- Reporting the four documented energies as a kernel bug: the kernel may legitimately offer Raw as an intake signal the resolver never emits, which is why it is an owner question rather than a defect (iteration 10)
- Searching for a gate that would have caught the stale plugin copy, the link drift or the four unread config entries: no gate reads any of them (iteration 10)
- Treating the routing defect count as a reason to rewrite the router: three implementations are already held equal by differential.py, and the defects are contract statements, not algorithms (iteration 10)

<!-- /ANCHOR:ruled-out-directions -->

---

<!-- ANCHOR:divergence-frontier -->
## 10A. SATURATED DIRECTIONS AND DIVERGENCE FRONTIER
- Completed pivots: 0
- Failed pivots: 0
- Audited overrides: 0
- Saturated: none yet
- Pivot lineage: none yet
- Remaining frontier: none recorded

<!-- /ANCHOR:divergence-frontier -->

---

<!-- ANCHOR:carried-forward-open-questions -->
## 11A. CARRIED-FORWARD OPEN QUESTIONS
- Which scripts, functions, flags and config entries are dead code? (iteration 1)
- Is routing embedded in the right Claude Project layer, and what could shrink without losing a rule that must fire every turn? (iteration 1)
- What are the concrete, ranked routing and mode-link changes, each with the files it touches, its risk, the gate that proves it and the byte effect on the kernel? (iteration 1)
- Which README claims are stale against the files they describe? (iteration 1)
- Which references, assets, examples and playbook files are dead documents? (iteration 1)
- What is the ranked synthesis of every finding, and what can the repository not settle? (iteration 1)
- Which router copies are held equal by a gate such as benchmark/router/differential.py, and which drift unchecked? (iteration 1)
- Where is a hand-off between modes undefined, duplicated or contradictory? (iteration 1)
- How does the Product Owner's own Python, shell, JavaScript and JSON deviate from the sk-code-skilled standards? (iteration 1)
- none (iteration 10)

<!-- /ANCHOR:carried-forward-open-questions -->

---

<!-- ANCHOR:next-focus -->
## 11. NEXT FOCUS
[All tracked questions are resolved]

<!-- /ANCHOR:next-focus -->

---

<!-- MACHINE-OWNED: END -->
## 12. KNOWN CONTEXT

- Staging spec `specs/z-staging-po-019s/spec.md` states ten questions and the in-scope file set.
- Steer file binds one question per iteration in spec order and requires `[SOURCE: path:line]` citations plus a file a fix would change.
- The Product Owner hub root holds `SKILL.md`, `ROUTER.md`, `mode-registry.json`, `hub-router.json`, `leaf-manifest.json`, `AGENTS.md`, `SYNC.md`, `README.md`, `USER-GUIDE.md`, `benchmark/`, `scripts/`, `claude project/`, `claude-plugin/` and two packets (`sk-product-owner/`, `sk-create-figjam/`) plus two vendored packets.
- A containment baseline copy of the tree exists inside this lineage; all citations name the real repository-relative path under `AI Systems/Product Owner/`.

### Bounded Context Snapshot

- Source pointers: hub routing files at the repository root, packet `SKILL.md` Section 2 in each packet, `sk-product-owner/references/routing.md` and `router-contract.md`, `benchmark/router/`, `claude project/Custom Instructions.md`, `AGENTS.md`.
- Integration points: `benchmark/gates/check_hub.py`, `benchmark/router/differential.py`, `scripts/build-plugin.py`, `scripts/vendor-sync.py`, `.skilled/skills/sk-code/sk-code-skilled/`.
- Constraints and risks: 3064 markdown files under the tree make whole-tree reads impossible; every claim must be bounded to specific lines.

---

## 13. RESEARCH BOUNDARIES
- Max iterations: 10
- Convergence threshold: 0.1 (telemetry only)
- Per-iteration budget: 24 tool calls, 10 minutes
- Progressive synthesis: true
- research/research.md ownership: workflow-owned canonical synthesis output inside this lineage
- Lifecycle branches: `new` (this run)
- Machine-owned sections: reducer controls Sections 3, 6, 7-11A
- Current generation: 1
- Started: 2026-10-21T18:11:08Z
