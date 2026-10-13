---
title: "Feature Specification: Human Voice and Conciseness Enforcement"
description: "HVR is enforced by reference: a skill points at a 684-line document and nothing checks the output. With no hooks available and no dependency on the sk-doc packet permitted, enforcement has to come from prevention and review, not interception. This packet builds a standalone HVR integration: an always-loaded card carrying every blocker inline, a self-scan the model must emit, a validator run at review time, and a conciseness layer above HVR."
trigger_phrases:
  - "enforce human voice rules"
  - "standalone hvr integration"
  - "make output concise not robotic"
  - "conciseness standard"
  - "hvr always loaded token cost"
  - "hvr enforcement without hooks"
importance_tier: "high"
contextType: "specification"
_memory:
  continuity:
    packet_pointer: "006-human-voice-and-conciseness-enforcement"
    last_updated_at: "2026-09-02T00:00:00Z"
    last_updated_by: "claude"
    recent_action: "R3 implemented as sk-product-owner/references/conciseness.md, wired into every ALWAYS-tier surface, and the four advisory conciseness checks turned blocking. Router 33/33, format validator green across 37 sources, 15/15 format fixtures"
    next_safe_action: "Run review-kernel with a named reviewer and reason to clear the KERNEL_REVIEW_REQUIRED digest mismatch, then decide whether R6 is still worth building"
    blockers:
      - "KERNEL_REVIEW_REQUIRED, both contractInput files changed and clearing it needs a named human reviewer"
    key_files:
      - "AI Systems/z — Knowledge/Rules - Human Voice - EN - v0.210.md"
      - "AI Systems/Product Owner/sk-product-owner/references/hvr-core.md"
      - "AI Systems/Product Owner/sk-product-owner/references/conciseness.md"
      - "AI Systems/Product Owner/sk-product-owner/SKILL.md"
      - "AI Systems/Product Owner/benchmark/format/validate-output-format.cjs"
    completion_pct: 90
    open_questions:
      - "Is R6 still worth building now the validator carries a blocking HVR pass"
      - "Do the eight sibling systems adopt this now or after Product Owner proves it"
      - "Is a standalone scanner worth building, or does the card plus validator suffice"
      - "Does the hvr-core mirror take a v0.100 pin, or follow the standard's version"
    answered_questions:
      - "sk-create-with-human-voice is a reference only, not a dependency and not a merge partner"
      - "No hooks are available, so nothing fires automatically and enforcement is prevention plus review"
      - "Spec 008 does not solve conciseness, its dependency detect_shape_hint no longer exists"
      - "The Product Context HVR folder is a symlink view, the home is z — Knowledge"
      - "R1 touches all 32 router fixtures, since each asserts the ALWAYS resource list"
      - "SKILL.md and Custom Instructions.md are contractInput files appearing under four requirements each, so edits batch into one pass"
      - "The card costs 2,063 tokens, not the 800 estimated, and saves 5,400 per request rather than 6,600"
      - "The self-scan line drops the soft count, since the card carries hard blockers only"
      - "The self-scan line is delivery metadata and never artifact content, which resolves the output-warnings conflict"
      - "R5 conciseness checks ship advisory, because their vocabulary belongs to the unbuilt R3"
      - "R3 lives in Product Owner as references/conciseness.md, not in the shared standard, so eight sibling systems are unaffected"
---
# Feature Specification: Human Voice and Conciseness Enforcement

<!-- SPECKIT_LEVEL: 2 -->
<!-- SPECKIT_TEMPLATE_SOURCE: spec-core | v2.2 -->

---

## 1. METADATA

| Field | Value |
| --- | --- |
| Spec ID | 039 |
| Level | 2 |
| Status | R1, R2, R3, R4, R5 implemented and gated. R6 outstanding |
| Created | 2026-09-02 |
| Depends on | none |
| Related to | 001-product-owner-scope-aware-verbosity (superseded in intent, see 2.5) |
| Systems touched | Product Owner first, then the eight sibling systems consuming HVR |

---

## 2. PROBLEM & PURPOSE

### 2.1 Constraints that shape this packet

Two constraints set before design, and both remove options that would otherwise be obvious.

**The integration is standalone.** `sk-create-with-human-voice` in the Code_Environment tree is a reference to learn from, not a dependency. Nothing here symlinks into it, syncs from it, or calls its scripts. Its 510-line rules file is a separate document with its own history, and reconciling the two is explicitly not this packet's job.

**No hooks.** Nothing fires automatically. No `PostToolUse` nudge, no `Stop` backstop, no pre-commit. Every mechanism below is either something the model reads before writing, something the model must produce as output, or something a human or CI runs deliberately.

That second constraint is the one that matters most. Interception is off the table, so enforcement has to come from making violations hard to express and easy to spot afterwards.

### 2.2 Problem statement

HVR is enforced by reference. A skill says "apply the Human Voice Rules" and points at a document. Nothing verifies the output. Three measurements taken during this investigation show the cost.

**The always-loaded instruction files are the worst violators of the voice they teach.** Measured directly:

| File | Hard blockers |
| --- | --- |
| `sk-product-owner/SKILL.md` | 73 |
| `references/prd-mode.md` | 62 |
| `claude project/Custom Instructions.md` | 58 |
| `references/doc-mode.md` | 40 |
| `AGENTS.md` | 35 |

Overwhelmingly prose semicolons, curly quotes and em dashes, outside code fences. The model is instructed to write in a voice by documents written against it. In-context style imitation is a stronger signal than an instruction, and with no hooks available it is one of the few levers left.

**The standard costs 7,460 tokens on every request and is loaded as a pointer.** `Rules - Human Voice - EN - v0.210.md` is 27,660 characters and sits in the ALWAYS tier. Being loaded is not the same as being applied: the terms are in a document the model has seen, not in a list it is looking at while writing.

**Nothing checks output.** `validate-output-format.cjs` checks two things, bullets not ending in a full stop and no divider after a Mark-as-done line, across the skill's own sources. It ignores any path argument passed to it, so it cannot lint a produced artifact even when asked. The claude.ai kernel's strongest mechanism is a self-reported `HVR = checked` line with nothing behind it.

### 2.3 The conciseness gap

The second half of the request is output that is "as concise and clear as possible, not robotic but concise and effective". HVR does not cover this, and in one place works against it.

HVR is word- and phrase-level throughout. A document can score 100/100 and be three times too long. There is no length budget, no rule against restating the question, and no rule against a closing paragraph that accurately repeats the body. Hedges score additively, so "It's possible this could potentially fail" costs two points and passes.

The active conflict: HVR section 12 penalises `however`, `furthermore`, `moreover`, `additionally` and `consequently` from the third use. An aggressive conciseness pass reads that as licence to strip connectives, producing exactly the telegraphic output the request names as a failure. Nothing in HVR distinguishes rhetorical connectives, which are capped, from semantic ones like `because`, `so`, `unless` and `which means`, which carry the logic and must never be cut.

### 2.4 Purpose

Make the rules present at the moment of writing rather than referenced, make compliance a visible artifact rather than a claim, give review something to check against, and add a conciseness layer that defines the line between concise and robotic operationally rather than by adjective.

### 2.5 Non-goals

- Rewriting the Human Voice Rules. The content is sound, the packaging is not.
- Reconciling with `sk-create-with-human-voice`. Out of scope by constraint.
- Any harness automation. Out of scope by constraint.
- Rolling out to all systems at once. Product Owner proves it first.
- Reviving spec 008. Its dependency `detect_shape_hint()` no longer exists in the repo, and it governed which template sections appear, never sentence-level prose.

---

## 3. REQUIREMENTS

### R1 — The always-loaded card

* * *

Replace the pointer with the list. This is the highest-leverage requirement and the only one that works identically on the CLI and on claude.ai.

- Create `sk-product-owner/references/hvr-core.md`. Estimated at 800 tokens, shipped at **2,063** (7,636 bytes, 94 lines). The estimate was wrong twice: an initial build hit 1,015 tokens by omitting roughly 45 terms, and carrying the full lists costs what it costs
- Carry every punctuation ban, every blocker word, every blocker phrase and the delete-on-sight modifier list **inline as a visible list**, not behind a reference
- Add a structural-bans block naming the patterns no scanner can see: three-item enumerations, triple headers, synonym cycling, false ranges, fragmented headers, copula avoidance, significance inflation, generic conclusions
- Demote the full standard from ALWAYS to ON_DEMAND, loaded only when adjudicating a borderline case or running a scored voice pass
- Register the new file in `SYNC.md` so the compiler mirrors it into `claude project/knowledge/`

Emitting a banned token now requires overriding a list in view, rather than recalling a document. The change reduces token cost by roughly **5,400** per request against the 7,457-token standard, so it still pays for itself, but by less than the 6,600 first claimed.

**The completeness trap is real and was hit.** The first implementation carried the counts it promised and silently omitted banned metaphors, setup phrases and generalisation fixes, roughly 45 terms that had been in context while the full standard was ALWAYS-loaded. That is a coverage regression wearing the shape of a hardening. Any future trim of this card must be measured against the standard term by term, not against a token target.

### R2 — Mandatory self-scan line

* * *

Convert an unverifiable instruction into an artifact the model must produce.

- Require this exact line in the delivery response, alongside the existing export path and read-back confirmation:
  `HVR self-scan: N hard blockers. Fixed: <terms>. Kept with reason: <terms>.`
- A count of zero with no terms named is a valid line only when the artifact genuinely has none
- The `Kept with reason` half matters as much as `Fixed`: it forces the model to distinguish a sanctioned exemption from a miss

The soft-deduction count was dropped after implementation. The card carries hard blockers only, so demanding `M soft` forced an ON_DEMAND load of the standard and defeated the demotion R1 exists for. A line may only ask for what the ALWAYS tier can answer.

**The line is delivery metadata, never artifact content.** It sits in the response beside the export path, on the same footing as the existing rule that Mode, Template, Perspectives and Quality headers never enter a delivered artifact. This also resolves a conflict with the standard's output warnings, which ban meta-commentary about the writing process and references to the rules: those govern the artifact, not the delivery response.

Without hooks nothing verifies this line is honest. It is a forcing function, not evidence. Its value is that producing a specific count is harder to do absent-mindedly than asserting compliance.

### R3 — Conciseness layer

* * *

A layer above HVR: HVR governs word choice, conciseness governs quantity, structure and load-bearing-ness.

**The reconstruction test is the operational definition.** After a cut, could a reader who does not already know the answer recover what was removed from what remains? If yes, the cut was free. If no, the information moved out of the text and into the reader's head.

**Cut rules**, named so a reviewer can cite them: question echo, intent narration, compliance acknowledgement, terminal recap, hedge stack, importance assertion, the conclusion move, both-sides padding, empty enumeration, heading echo, restated constraint, effort reporting.

**Keep rules**, the anti-robotic half: semantic connectives, one concrete instance per non-obvious rule, the caveat that prevents a wrong action, the scope qualifier, the named referent, the negative case, the specific number, one human beat per roughly 400 words, and grammar itself. Conciseness removes claims, never articles, copulas or finite verbs.

**Five over-compression signatures**: connective stripping, referent stripping, telegraphese, condition collapse, example deletion.

The layer must state that section 12's connective cap applies to rhetorical connectives only, resolving the conflict in 2.3. It must also carry format guidance, because over-bulleting is the main way output becomes robotic while appearing concise.

**Placement decided: a Product Owner file, not the shared standard.** `sk-product-owner/references/conciseness.md`, ALWAYS-tier, sibling to `hvr-core.md`. It stays a separate file rather than folding into the card, because the card is the Human Voice standard and this is a distinct layer above it, and the two should version independently.

The mirror row, manifest entry and checksum line this costs land on one system rather than nine. Putting it in `z — Knowledge/` would have pushed a conciseness standard onto eight sibling systems that never asked for one.

**Shipped at 7,859 bytes and 1,837 tokens**, 112 lines, including a 144-word drop-in instruction block. ALWAYS-tier references now cost 8,808 tokens (card 1,820, conciseness 1,837, DEPTH 5,151) against 12,093 before R1 demoted the standard, so the layer fits inside the saving R1 created and the tier still costs 3,285 tokens less per request than it did.

### R4 — Clean the instruction surface

* * *

Bring the five worst-offending files to the standard they teach.

- Replace prose semicolons with full stops, curly quotes with straight quotes, prose em dashes with commas or colons
- Leave code fences and the sanctioned `*   **Term** — definition` delimiter alone
- `SKILL.md` and `Custom Instructions.md` are `contractInput` files, so this forces a kernel re-review and a compiler re-sync

With interception unavailable, the example the model reads is a primary lever rather than a marginal one. Telling a model to avoid semicolons inside a document containing 69 of them is asking it to ignore the strongest style signal in its context.

### R5 — Review-time validator

* * *

Give the existing validator something to check and something to check against.

- Add an argv path so `validate-output-format.cjs` can lint an arbitrary artifact, not only its own hardcoded source list. Two-line change, and the current behaviour of silently ignoring the argument is itself a defect
- Add a deterministic HVR pass over the file list it already builds, so R4 cannot silently rot
- Add the mechanically detectable conciseness checks from R3: sentence-initial opener list, terminal recap openers, hedge stacks in one sentence, heading echo
- Keep statistical checks advisory rather than blocking: bullet ratio, heading density, connective inventory, article and copula rate

The connective inventory is worth calling out. A value near zero in explanatory prose is the mechanical signature of the robotic failure mode, and it is the only proposed statistic that guards the keep side rather than the cut side.

This runs when a human or CI runs it. That is the honest limit of enforcement without hooks.

### R6 — Standalone scanner, if justified

* * *

Deferred, and possibly unnecessary.

A deterministic scanner for the fleet standard would live in `benchmark/format/`, owned by this repo, modelled on the reference implementation but sharing no code with it. It would need a parser for the standard's YAML block shape, a fail-closed minimum-term floor, and two exemptions learned from the reference: mask path-like and URL-like spans, and exempt the sanctioned definition delimiter.

The path exemption is not hypothetical. Ten of eleven story drafts scanned during this investigation showed exactly one hard blocker each, and it was the same false positive every time: an em dash inside a `Source: Product Context/z — …` line. A checker that fires on every legitimate artifact gets ignored within a week.

**Decide this after R1 and R5 have run for a while.** If the card plus the validator's HVR pass catch enough, a second scanner is duplicated machinery. Building it first would be solving for a gap that may not survive R1.

---

## 4. IMPLEMENTATION SURFACE

Verified present on disk. Two files are created, the rest are modified.

### 4.1 Create

| File | Note |
| --- | --- |
| `sk-product-owner/references/hvr-core.md` | The card. Every blocker term and punctuation rule inline, roughly 50 lines |
| `claude project/knowledge/Product Owner - Rules - Human Voice Core - v0.100.md` | Its mirror. Compiler-generated, never hand-edited |
| `sk-product-owner/references/conciseness.md` | The conciseness layer. Shipped at 112 lines, 7,859 bytes |
| `claude project/knowledge/Product Owner - Rules - Conciseness - v0.100.md` | Its mirror. Compiler-generated, never hand-edited |
| `benchmark/format/fixtures/conciseness-violation.md` | One case per newly blocking check, line numbers pinned |
| `benchmark/format/fixtures/conciseness-silent.md` | The near-miss half: a quoted opener, a single hedge, an informative lead-in |

### 4.2 Modify, by requirement

**R1, the card**

- `sk-product-owner/SKILL.md`, add the card to `RESOURCE_MAP["ALWAYS"]` and demote the full standard to ON_DEMAND
- `AGENTS.md`, the same change in the load-order section
- `claude project/Custom Instructions.md`, hand-synthesised rather than generated, so the change is written by hand
- `SYNC.md`, one new row in the mirror inventory table
- `claude-project.sync.json`, new mirror entry, and `expectedKnowledgeCount` 32 becomes 33
- `benchmark/router/route_contract.py`, the `ALWAYS` list at line 145
- `benchmark/router/fixtures.json`, **all 32 fixtures**, each asserts the loaded resource list

**R2, self-scan line**

- `sk-product-owner/SKILL.md`, the export and response contract
- `AGENTS.md`, the matching delivery step
- `claude project/Custom Instructions.md`

**R3, conciseness layer**

- `sk-product-owner/SKILL.md`, the ALWAYS table, `RESOURCE_MAP["ALWAYS"]`, the reference index and one new ALWAYS rule
- `AGENTS.md`, the always-load list, the DAG and the validation step
- `claude project/Custom Instructions.md`, hand-synthesised: resource domains, the loading table, the Knowledge consultation table, `RESOURCE_MAP` and one new ALWAYS rule
- `SYNC.md`, the manual-load order and the inventory row
- `claude-project.sync.json`, new mirror entry, and `expectedKnowledgeCount` 33 becomes 34
- `benchmark/router/route_contract.py` and all 33 fixtures in `benchmark/router/fixtures.json`
- `benchmark/format/validate-output-format.cjs`, four checks turned blocking plus a vocabulary-agreement guard
- `benchmark/format/run_fixtures.sh`, nine new cases
- The five discovery surfaces: `graph-metadata.json`, `description.json`, `sk-product-owner/README.md`, `benchmark/router/README.md`, `claude project/README.md`
- The shared standard in `z — Knowledge/` is deliberately **not** touched

**R4, clean the surface**

- `sk-product-owner/SKILL.md` (73 hard blockers), `references/prd-mode.md` (62), `claude project/Custom Instructions.md` (58), `references/doc-mode.md` (40), `AGENTS.md` (35)

**R5, validator**

- `benchmark/format/validate-output-format.cjs`

### 4.3 Two costs the file list hides

**R1 touches all 32 router fixtures.** Every fixture asserts which resources the router loaded, and each one names the ALWAYS tier. Changing that tier changes all 32 expected objects. The edit is mechanical, but R1 is not the small drop-in it appears to be, and fixtures not updated in the same commit turn the router gate red.

**`SKILL.md` and `Custom Instructions.md` each appear under four requirements.** Both are `contractInput` files, so every touch forces a kernel re-review and a compiler re-sync. Batch their edits into one pass rather than four.

### 4.4 After any change

`sync --write`, then `review-kernel`, then `check --run-validators`. Then the manual upload of the knowledge files to the claude.ai Project, which no mechanism verifies.

---

## 5. SEQUENCING

| Phase | Requirements | Status |
| --- | --- | --- |
| 1 | R1 | Done, card shipped and wired into all seven surfaces |
| 2 | R2, R4 | Done, self-scan in three contract files, five files cleaned to zero |
| 3 | R3 | Done, sibling file at `references/conciseness.md`, wired into every ALWAYS surface, four checks turned blocking |
| 4 | R5 | Done, validator takes a path, HVR pass blocking, conciseness checks now blocking too |
| 5 | R6 | Outstanding, and now less likely to be needed |

R1, R2 and R4 were implemented in one pass, since all three edit `SKILL.md` and `Custom Instructions.md` and each touch forces a kernel re-review.

**R5 shipped narrower than written, and R3 closed the gap.** The conciseness checks were advisory because their vocabulary came from R3, which did not exist. A gate blocking on 28 opener phrases no instruction file states enforces rules the model was never given. R3 states all 28 openers, all 11 recap openers and all 20 hedges verbatim, so the four checks now block, and a guard in the validator fails the run if a term is ever added to a check list without being written into the layer.

---

## 6. OUTSTANDING

**The kernel review is open and only a human can close it.** `check --system product-owner --run-validators` exits 3:

```
[KERNEL_REVIEW_REQUIRED] Contract inputs changed since the recorded kernel review (digest mismatch).
```

Both `contractInput` files changed. Clearing it needs `review-kernel --system product-owner --reviewer <name> --reason <why>`. No agent may supply the name.

**R3 shipped**: `sk-product-owner/references/conciseness.md`, inside Product Owner. The shared standard stays untouched, so the eight sibling systems are unaffected.

It also unblocked the four conciseness checks in `validate-output-format.cjs`. They now block on every file, and the existing 36 sources plus the new layer pass with them blocking, so nothing had to be loosened to stay green.

**R6 is less likely to be needed than when written.** The validator now carries a blocking HVR punctuation pass and the card carries the full term lists, so the gap a standalone scanner would fill has narrowed. Decide it after the card has been in use for a while.

**The manual upload to the claude.ai Project remains unverified.** The compiler renders 34 mirrors, and nothing confirms a human uploaded them.

---

## 7. RISKS

| Risk | Mitigation |
| --- | --- |
| The self-scan line is emitted without the scan | Unsolved by design. No hooks means no verification. Treat R2 as a forcing function, and rely on R1 and R4 to make violations rarer rather than caught |
| The card drifts from the standard it summarises | R5's HVR pass covers the card itself, and the card names the standard as authority for anything it does not carry |
| Conciseness rules strip connectives | R3's keep rules and the rhetorical-versus-semantic distinction are not optional parts of the layer |
| R4 regresses over time | R5's HVR pass over source files, run at review |
| Nine sibling systems already report `KERNEL_REVIEW_REQUIRED` | Clear them before adding a new check, or a new signal lands in a list that is nine-tenths noise |
| The claude.ai Project is never re-uploaded | Unsolved, and outside this packet. No mechanism verifies the manual upload step |

---

## 8. EVIDENCE

Every measurement in section 2 was taken directly, not inferred:

- Hard-blocker counts produced by running a deterministic scanner against each instruction file
- Standard size measured with `wc -c`, 27,660 characters
- Validator behaviour confirmed by passing it a nonexistent path and observing it report success across its own 35 source files
- Symlink target resolved with `ls -l`, confirming `Product Context/z — Human Voice Rules/` is a view of `AI Systems/z — Knowledge/`

Three parallel investigations produced the underlying findings independently. Their proposals for harness automation and cross-repo reconciliation were discarded when the two constraints in 2.1 were set.
