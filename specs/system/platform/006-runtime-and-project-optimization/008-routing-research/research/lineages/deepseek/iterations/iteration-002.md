# Iteration 2: Which router copies a gate holds equal, and which drift unchecked

## Focus
Question 2: compare sk-product-owner/references/router-contract.md, benchmark/router/route_contract.py, Section 11 of claude project/Custom Instructions.md, the routing trigger tables and sk-create-figjam's routing. Determine which copies a gate holds equal and which drift unchecked. Walked every row of benchmark/gates/run_gates.sh to the file it reads, then read the differential harness guard by guard, the skilled root-router contract and the figjam packet's router.

## Findings
1. Three routing implementations are genuinely held equal. differential.py lifts the pseudocode out of router-contract.md, executes it as a module, and compares route_contract.py to it on five guards: prose-table subset, copy parity, table parity, behavior parity over 220 corpus inputs, and corpus coverage of every command, false prefix, topic and shape. It also requires the kernel to carry exactly one python fence and holds that block byte-equal, then AST-equal, to the pseudocode minus comments. Fix: none; this is the one sound routing gate. [SOURCE: AI Systems/Product Owner/benchmark/router/differential.py:200-240] [SOURCE: AI Systems/Product Owner/benchmark/router/differential.py:307-421] [SOURCE: AI Systems/Product Owner/benchmark/router/differential.py:468-521] [SOURCE: AI Systems/Product Owner/benchmark/router/differential.py:620-644]
2. Only the kernel's code is gated, not its routing prose: copy parity compares Section 11 and checks that Section 11 is reachable from the kernel and from routing.md, but nothing compares Sections 2 and 7 to that code or to each other, so the always-loaded prose can instruct behaviour the router no longer has while every guard stays green. Fix: claude project/Custom Instructions.md sections 2 and 7. [SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:35-74] [SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:180-188] [SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:323-325]
3. The two leaf maps are validated by different gates that never compare them: ROUTER.md's RESOURCE_MAP is held by the skilled root-router contract for on-disk resolution and leaf-manifest registration, while router-contract.md's RESOURCE_MAP is held by differential's table parity against route_contract.py. Either map can change which leaf an intent loads without the other gate noticing, which is why the CLICK_UP and FIGMA lanes can exist in one map only. Fix: compare the two maps, or delete one. [SOURCE: AI Systems/Product Owner/ROUTER.md:66-103] [SOURCE: AI Systems/Product Owner/sk-product-owner/references/router-contract.md:136-152] [SOURCE: .skilled/skills/sk-doc/sk-create-skill/scripts/lib/root-router-contract.cjs:13-25] [SOURCE: AI Systems/Product Owner/benchmark/router/differential.py:503-510]
4. DEFAULT_RESOURCE in router-contract.md is read by nothing: route_contract.py has no occurrence of the constant, differential's table parity compares thresholds, regexes, lane maps, shape tables and the checklist but never this value, and its published value contradicts ROUTER.md. It is a dead constant carrying a wrong answer. Fix: router-contract.md line 49. [SOURCE: AI Systems/Product Owner/sk-product-owner/references/router-contract.md:49] [SOURCE: AI Systems/Product Owner/benchmark/router/route_contract.py:1-60] [SOURCE: AI Systems/Product Owner/benchmark/router/differential.py:496-520]
5. Hub stage one is gated only by its gold rows: check_hub.py replays 37 cases against its own Python replica of the rules, and never parses the seven SKILL.md rules or the five hub-router bullets, so a prose-only edit that contradicts the replica stays green until a row happens to exercise it. Fix: benchmark/gates/check_hub.py and benchmark/hub-routing-cases.json. [SOURCE: AI Systems/Product Owner/benchmark/gates/check_hub.py:239-293] [SOURCE: AI Systems/Product Owner/SKILL.md:50-58] [SOURCE: AI Systems/Product Owner/hub-router.json:24-30]
6. The FLOW lane escapes table parity: differential compares RESOURCE_MAP lanes for TASK, BUG, DOC, STORY and INTERACTIVE only, and its coverage guard never routes a Flow intent, so the Flow pair and the figjam packet's type routes have no executable contract. The figjam packet is self-consistent, but nothing holds its type table, its route_flow() and the hub ROUTER.md together. Fix: add FLOW to the compared lanes or state why it is out. [SOURCE: AI Systems/Product Owner/benchmark/router/differential.py:509-510] [SOURCE: AI Systems/Product Owner/sk-create-figjam/SKILL.md:35-57] [SOURCE: AI Systems/Product Owner/sk-create-figjam/SKILL.md:71-140]
7. benchmark/router/README.md says four guards fire independently, while the harness runs five: prose-table parity is guard 0 and main() calls it before the other four. A reader counting guards from the README undercounts the gate. Fix: benchmark/router/README.md line 151. [SOURCE: AI Systems/Product Owner/benchmark/router/README.md:151-166] [SOURCE: AI Systems/Product Owner/benchmark/router/differential.py:691-705]
8. The staging spec names sk-create-figjam/ROUTER.md as a router copy to compare, but no such file exists, and check_hub fails the build if one appears because ROUTER.md is in its packet-residue list. The figjam routing copy is its SKILL.md Section 2 plus its route_flow pseudocode. Recorded so the question is not answered against a phantom file. [SOURCE: AI Systems/Product Owner/benchmark/gates/check_hub.py:52-54] [SOURCE: AI Systems/Product Owner/sk-create-figjam/SKILL.md:31-57]
9. The router-contract ALWAYS lane names sk-product-owner/SKILL.md, a path its own load guard can never load because the inventory is packet-relative; differential works around it by filtering the entry out before comparing lanes. The inconsistency is tolerated by the gate rather than fixed, so a second such entry would also pass. Fix: router-contract.md line 137-141. [SOURCE: AI Systems/Product Owner/sk-product-owner/references/router-contract.md:136-141] [SOURCE: AI Systems/Product Owner/sk-product-owner/references/router-contract.md:283-296] [SOURCE: AI Systems/Product Owner/benchmark/router/differential.py:503-507]
10. Coverage by surface, which is the direct answer to this question: intent routing inside sk-product-owner is fully gated across three implementations; hub stage one is gated only by 37 gold rows against a replica; the stage-two leaf map has its paths gated but its intent-to-leaf equality ungated; figjam type routing is ungated; kernel routing prose is ungated while kernel routing code is byte-gated. Fix: the three ungated rows need a gate each, and the two Leaf Maps need one comparison. [SOURCE: AI Systems/Product Owner/benchmark/gates/run_gates.sh:41-54] [SOURCE: AI Systems/Product Owner/benchmark/router/run_fixtures.sh:36-39]

## Ruled Out
- Counting the gold-row replay as a stage-one specification gate: it tests a replica against expectations, not the prose against the replica
- Treating the differential corpus group named known-divergences as an exemption: compare_input applies to every corpus input with no exception list, so those two entries must now agree
- Treating sk-create-figjam/ROUTER.md as an existing copy: the file is absent and a hub gate forbids it

## Dead Ends
- Looking for a second Python fence or a pasted router definition in SKILL.md or routing.md: both are refused by copy parity, which is why the prose copies are prose only

## Edge Cases
- Ambiguous input: Question 2 asks which copies a gate 'such as' differential.py holds equal; the answer separates implementations (held equal) from prose (held only as a subset or not at all)
- Contradictory evidence: The spec presupposes a figjam packet ROUTER.md that the hub gate forbids; recorded rather than scored as a drift
- Missing dependencies: No gate was executed, because this run is read-only and outside the target repository; every guard claim is read from the gate source
- Partial success: The differential corpus count of 220 was computed from fixtures.json and differential_corpus.json by deduplicating input strings

## Sources Consulted
- specs/z-staging-po-019s/research/lineages/deepseek/steer.md
- AI Systems/Product Owner/benchmark/router/differential.py
- AI Systems/Product Owner/benchmark/router/route_contract.py
- AI Systems/Product Owner/benchmark/router/README.md
- AI Systems/Product Owner/benchmark/router/run_fixtures.sh
- AI Systems/Product Owner/benchmark/router/fixtures.json
- AI Systems/Product Owner/benchmark/router/differential_corpus.json
- AI Systems/Product Owner/benchmark/gates/check_hub.py
- AI Systems/Product Owner/benchmark/gates/run_gates.sh
- AI Systems/Product Owner/benchmark/hub-routing-cases.json
- AI Systems/Product Owner/sk-product-owner/references/router-contract.md
- AI Systems/Product Owner/sk-product-owner/references/routing.md
- AI Systems/Product Owner/sk-create-figjam/SKILL.md
- AI Systems/Product Owner/sk-create-figjam/scripts/flow_check.py
- AI Systems/Product Owner/claude project/Custom Instructions.md
- AI Systems/Product Owner/ROUTER.md
- .skilled/skills/sk-doc/sk-create-skill/scripts/lib/root-router-contract.cjs

## Assessment
- New information ratio: 0.78
- Questions addressed: Which router copies are held equal by a gate such as benchmark/router/differential.py, and which drift unchecked?
- Questions answered: Which router copies are held equal by a gate such as benchmark/router/differential.py, and which drift unchecked?

## Reflection
- What worked and why: Reading the gate source instead of its README separated the four guards the prose names from the five the harness runs, and showed exactly which lanes table parity skips
- What did not work and why: The first assumption that ROUTER.md was unverified was wrong; the skilled root-router contract checks it, which is why the two maps can both be green and still disagree
- What I would do differently: Enumerate the files each gate reads before comparing copies, then mark every unread copy as ungated

## Questions Remaining
- Where is a hand-off between modes undefined, duplicated or contradictory?
- Is routing embedded in the right Claude Project layer, and what could shrink without losing a rule that must fire every turn?
- What are the concrete, ranked routing and mode-link changes, each with the files it touches, its risk, the gate that proves it and the byte effect on the kernel?
- Which README claims are stale against the files they describe?
- Which scripts, functions, flags and config entries are dead code?
- Which references, assets, examples and playbook files are dead documents?
- How does the Product Owner's own Python, shell, JavaScript and JSON deviate from the sk-code-skilled standards?
- What is the ranked synthesis of every finding, and what can the repository not settle?

## Recommended Next Focus
Question 3: how the modes connect. Trace each hand-off, task/subtask, bug, doc shapes, story/epic, interactive, quick/standard/deep/raw, flow with its seven types and the then-FLOW pair, refinement and the ClickUp handoff, and record where a hand-off is undefined, duplicated or contradictory.
