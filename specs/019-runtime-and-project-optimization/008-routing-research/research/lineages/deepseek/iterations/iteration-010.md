# Iteration 10: Synthesis: what is wrong, what to change first, and what the repository cannot settle

## Focus
Question 10: rank every verified finding from iterations 1 to 9 by cost and confidence, name the files to change, state the order, and separate what the evidence settles from what it does not. Nothing new was investigated; every claim below was established and gate-verified in an earlier iteration.

## Findings
1. Stage one has three authorities and no statement of which wins. The hub SKILL.md prose, ROUTER.md's table and hub-router.json each carry the routing rules; rules 3 and 4 are both absolute and collide on a request that opens with a tool and also names an artifact, and no gold row covers that collision. Two smaller defects live in the same cluster: DEFAULT_RESOURCE names the ALWAYS cards in ROUTER.md and interactive-mode.md in router-contract.md, where nothing reads it, and router-contract.md's ALWAYS lane names sk-product-owner/SKILL.md, a path its own load guard refuses. Fix order: state first-match-wins, add the collision gold row, delete or align DEFAULT_RESOURCE, then make hub-router.json the single authority and reduce the hub prose to a pointer. [SOURCE: AI Systems/Product Owner/SKILL.md:1-40] [SOURCE: AI Systems/Product Owner/ROUTER.md:36-60] [SOURCE: AI Systems/Product Owner/hub-router.json:1-30] [SOURCE: AI Systems/Product Owner/sk-product-owner/references/router-contract.md:49]
2. The two leaf maps are validated by gates that never compare them, so the maps a reader trusts most can disagree without a red gate: ROUTER.md's RESOURCE_MAP is held by the root-router contract, leaf-manifest.json by the manifest walk, and their key sets differ. The FLOW lane escapes the differential's table parity entirely, which leaves FigJam-type routing with no executable contract. Fix: one comparison in differential.py covering every lane including FLOW, run before any map edit. [SOURCE: AI Systems/Product Owner/ROUTER.md:36-60] [SOURCE: AI Systems/Product Owner/leaf-manifest.json:1-20] [SOURCE: AI Systems/Product Owner/benchmark/router/differential.py:573-613]
3. Seven mode hand-offs are undefined, duplicated or contradictory, and each one is a wrong artifact rather than a slow reply: the hub keeps a Flow the packet hands off; Story Mode calls a single implementation unit Task Mode while Task Mode and routing.md disagree about the bundle's task path and command; the paired-output rule allows a Bug beside a FigJam board but the bug scaffold has no Flows group; the Bug-to-Task hand-off is undefined at routing time; Interactive Mode's clarification lane omits Task; the Quick fallback is stated three ways; two of the four documented energies (Raw and Deep) have no route in the resolver; and the ClickUp hand-off has three pointer forms. Fix: settle each contract in one file, then add a playbook scenario per contract. [SOURCE: AI Systems/Product Owner/sk-product-owner/references/story-mode.md:139] [SOURCE: AI Systems/Product Owner/sk-product-owner/references/task-mode.md:1-40] [SOURCE: AI Systems/Product Owner/sk-product-owner/references/interactive-mode.md:74] [SOURCE: AI Systems/Product Owner/sk-product-owner/references/routing.md:24]
4. Gate coverage is narrower than the documentation says. check_hub.py replays 37 gold rows against its own Python replica and never validates prose routing; differential.py holds only the kernel's Router Code equal to router-contract.md's pseudocode, not the kernel's routing prose; it runs five guards while two READMEs say four; and the documentation says 33 gold rows in two places while the file holds 37. Fix: correct the counts, then decide whether prose parity is in scope; today a kernel rule can be rewritten as long as Section 11 is untouched. [SOURCE: AI Systems/Product Owner/benchmark/gates/check_hub.py:296-303] [SOURCE: AI Systems/Product Owner/benchmark/router/differential.py:691-705] [SOURCE: AI Systems/Product Owner/benchmark/gates/README.md:22] [SOURCE: AI Systems/Product Owner/README.md:706]
5. The kernel is 70,010 bytes and 17 percent of it can go without losing a must-fire rule, but the largest block cannot move: Section 11 is 588 lines and 27,025 bytes held equal to router-contract.md by differential.py, so trimming its routing code without the source change fails the gate. The shrinkable set is Sections 5, 7 and 8 plus the six-line empty Section 10 and the 18 Full detail pointers that name five targets; the knowledge-lane map is stated three times and the kernel's RESOURCE_MAP names 17 paths a Project cannot read. Fix: trim in that order and review by hand, because no gate enforces retention of non-Section-11 rules. [SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:221-224] [SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:560-600] [SOURCE: AI Systems/Product Owner/SYNC.md:86]
6. Nothing checks that what ships is built from what is tracked. The generated plugin copy is one line behind its source — it lacks the just-do-it branch — scripts/build-plugin.py is called by no gate, no link check runs anywhere, 13 links in the vendored code-mode playbooks point outside the packet, and 13 in-scope files write template placeholders as markdown links, so a link gate would fail on placeholders before it caught real drift. Fix: add a build freshness row and a link row to run_gates.sh, rewrite the placeholders, and push the vendored link fix upstream. [SOURCE: AI Systems/Product Owner/claude-plugin/skills/product-owner/sk-product-owner/references/router-contract.md:343-344] [SOURCE: AI Systems/Product Owner/scripts/build-plugin.py:37-38] [SOURCE: AI Systems/Product Owner/mcp-code-mode/manual-testing-playbook/doctor-commands/doctor-mcp-debug.md:80]
7. Dead code and dead documents are not the problem, and the checks that would have found them are the finding. All 31 runtime files and all 73 routed leaves are reached; the leftovers are four config entries with no reader (bashAllowlist, workspaceWrites, the empty crossHubPairing, defaultResourceSemantics), one unlaned reference (routing.md), one unlinked hub release note, one stale corpus group name, and one documented-only step. Fix: delete the four entries, lane routing.md, link the release note, rename the corpus group. [SOURCE: AI Systems/Product Owner/mode-registry.json:13-19] [SOURCE: AI Systems/Product Owner/hub-router.json:18-23] [SOURCE: AI Systems/Product Owner/sk-product-owner/SKILL.md:71-77] [SOURCE: AI Systems/Product Owner/README.md:768]
8. The code is cleaner than its documentation: 22 Python files compile, shellcheck is silent across nine scripts, both CommonJS files parse and ten JSON files are well formed. The deviations are documentation and types rather than behavior — no script says why it omits set -e, the 1,702-line format gate lacks 'use strict', 59 lines exceed 120 characters, and four modules annotate none or few returns. Fix: the comments and 'use strict' first; the long regex lines are legible as they stand. [SOURCE: AI Systems/Product Owner/benchmark/gates/run_gates.sh:1-30] [SOURCE: AI Systems/Product Owner/benchmark/format/validate-output-format.cjs:1-15] [SOURCE: AI Systems/Product Owner/benchmark/grader/hvr_lint.py:151]
9. Provenance disclosure: iteration 1's ledger row carries a timestamp and durationMs that were invented at write time, not read from a clock, and every later row records durationMs 0 rather than a measured elapsed time. The ledger is append-only, so the defect cannot be corrected in place: it is disclosed here and in research.md. Route proof for all ten iterations comes from each delta artifact because the state projection carries no leaf-dispatch fields, which verify-iteration.cjs warns about on every run. Fix: instrument timing in the executor before the next run of this workflow; do not edit the ledger. [SOURCE: specs/z-staging-po-019s/research/lineages/deepseek/deltas/iter-001.jsonl:1] [SOURCE: specs/z-staging-po-019s/research/lineages/deepseek/deep-research-state.jsonl:1]
10. What the repository cannot settle, and must not be presented as settled: which stage-one source is the intended authority is an owner decision, not an evidence question; whether the trimmed kernel keeps every rule a Project needs has no automated gate and needs human parity review; the Project's live deployment has no receipt in this repository, so no deployment claim is made; benchmark/reports/ was out of scope, so the dated-run claim in the playbook is unverified rather than false; and the four unread registry fields may have consumers outside this repository and .skilled. Each of these is a named open item, not a finding. [SOURCE: AI Systems/Product Owner/SYNC.md:1-20] [SOURCE: specs/z-staging-po-019s/research/lineages/deepseek/deep-research-strategy.md:1-40]

## Ruled Out
- Treating the routing defect count as a reason to rewrite the router: three implementations are already held equal by differential.py, and the defects are contract statements, not algorithms
- Blending the P0 hand-off findings into one fix: each contract lives in a different file and needs its own scenario, and bundling them is how one gets silently dropped
- Reporting the four documented energies as a kernel bug: the kernel may legitimately offer Raw as an intake signal the resolver never emits, which is why it is an owner question rather than a defect

## Dead Ends
- Searching for a gate that would have caught the stale plugin copy, the link drift or the four unread config entries: no gate reads any of them
- Looking for dead code or dead documents to rank: none exists, so the ranked list is contracts, gates and documentation instead

## Edge Cases
- Ambiguous input: Two findings claim the same byte range of the kernel; the trim finding says what can shrink, the parity finding says what cannot, and they are separable only by Section
- Contradictory evidence: The brief asked for fix targets ranked by severity; the highest-cost fix (leaf-map unification) is not the most severe, so severity and order are stated separately
- Missing dependencies: No deployment receipt, no human parity review, and no report-scope evidence exist in this run
- Partial success: Ten questions are answered from repository evidence alone; the answers are verified against gates where gates exist and against counted files where they do not

## Sources Consulted
- specs/z-staging-po-019s/spec.md
- specs/z-staging-po-019s/research/lineages/deepseek/steer.md
- specs/z-staging-po-019s/research/lineages/deepseek/deep-research-strategy.md
- specs/z-staging-po-019s/research/lineages/deepseek/findings-registry.json
- AI Systems/Product Owner/SKILL.md
- AI Systems/Product Owner/ROUTER.md
- AI Systems/Product Owner/hub-router.json
- AI Systems/Product Owner/leaf-manifest.json
- AI Systems/Product Owner/mode-registry.json
- AI Systems/Product Owner/benchmark/router/differential.py
- AI Systems/Product Owner/benchmark/router/route_contract.py
- AI Systems/Product Owner/benchmark/gates/check_hub.py
- AI Systems/Product Owner/benchmark/gates/run_gates.sh
- AI Systems/Product Owner/benchmark/format/validate-output-format.cjs
- AI Systems/Product Owner/scripts/build-plugin.py
- AI Systems/Product Owner/sk-product-owner/references/router-contract.md
- AI Systems/Product Owner/sk-product-owner/references/routing.md
- AI Systems/Product Owner/sk-product-owner/references/story-mode.md
- AI Systems/Product Owner/sk-product-owner/references/task-mode.md
- AI Systems/Product Owner/sk-product-owner/references/interactive-mode.md
- AI Systems/Product Owner/claude project/Custom Instructions.md
- AI Systems/Product Owner/SYNC.md
- AI Systems/Product Owner/README.md

## Assessment
- New information ratio: 0.45
- Questions addressed: What is the ranked synthesis of every finding, and what can the repository not settle?
- Questions answered: What is the ranked synthesis of every finding, and what can the repository not settle?

## Reflection
- What worked and why: Ranking by what produces a wrong artifact separated three contract clusters from the documentation and style findings, which would otherwise have diluted the list
- What did not work and why: The first draft ranked every finding by severity alone and put the cheapest cosmetic fixes beside the map unification; splitting severity from order fixed it
- What I would do differently: State what cannot be settled as loudly as what can, because the kernel-retention question is the one that decides whether the trim is safe

## Questions Remaining
- none

## Recommended Next Focus
None. Ten of ten questions are answered; the close-out writes research.md and the completion event.
