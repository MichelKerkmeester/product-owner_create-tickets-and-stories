# Iteration 6: README currency: which claims the files no longer support

## Focus
Question 6: check the root README, USER-GUIDE, the Claude Project README, both packet READMEs, the benchmark, gates, router, format, grader and parity READMEs, the scripts folder and the manual-testing-playbook against the files they describe. Every numeric claim I could execute or count was checked against the file itself: fixture counts, corpus size, format cases, example counts, knowledge files, changelog notes, gate list, registry packets, gold rows and playbook scenarios.

## Findings
1. Most README claims still hold. Counted against the tree: 141 route fixtures, 220 deduplicated differential inputs, 59 format cases over 19 fixture files, 63 knowledge files (35 core plus 28 example mirrors, split 5 Task, 4 Bug, 7 Doc, 5 Story, 7 Flow), 29 changelog notes from v0.1.0.0 to v1.2.1.0, 12 gates with 4 skippable in a clone, 4 registry packets, 37 gold rows, 5 self-check samples, 7 playbook scenarios, and the 21 plus 7 worked examples the root README names. Fix: none. [SOURCE: AI Systems/Product Owner/README.md:663-702] [SOURCE: AI Systems/Product Owner/README.md:778-806] [SOURCE: AI Systems/Product Owner/claude project/README.md:40-58]
2. benchmark/gates/README.md says the hub gate replays 33 stage-one gold rows, in two places, while the file holds 37 and the root README already says 37. The count grew by four rows and this README did not follow. Fix: benchmark/gates/README.md lines 22 and 37. [SOURCE: AI Systems/Product Owner/benchmark/gates/README.md:22] [SOURCE: AI Systems/Product Owner/benchmark/gates/README.md:37] [SOURCE: AI Systems/Product Owner/benchmark/hub-routing-cases.json:1-20]
3. The manual-testing playbook contradicts itself about the same gold set: its overview says the cases file carries 33 machine-replayed rows, and its success criteria say check_hub replays 37 and passes. The second number is right. Fix: manual-testing-playbook/manual-testing-playbook.md line 28. [SOURCE: AI Systems/Product Owner/manual-testing-playbook/manual-testing-playbook.md:28] [SOURCE: AI Systems/Product Owner/manual-testing-playbook/manual-testing-playbook.md:58]
4. Two READMEs say the differential runs four guards. It runs five: prose-table parity is guard 0, called first in main(), and it is the guard that catches routing.md drifting from the executable tables. The root README's paragraph names the four and omits the one that protects the prose a model actually reads. Fix: README.md line 706 and benchmark/router/README.md line 151. [SOURCE: AI Systems/Product Owner/README.md:706] [SOURCE: AI Systems/Product Owner/benchmark/router/README.md:151] [SOURCE: AI Systems/Product Owner/benchmark/router/differential.py:691-705]
5. sk-product-owner/README.md contradicts itself about the example count: its opening says assets holds 20 worked examples, its own resources table says 21, and the folder holds 21. A reader who trusts the opening undercounts by one. Fix: sk-product-owner/README.md line 34. [SOURCE: AI Systems/Product Owner/sk-product-owner/README.md:34] [SOURCE: AI Systems/Product Owner/sk-product-owner/README.md:472]
6. The stale 33 appears in three documents and only one was updated, which is the failure a derived count always has. The durable fix is to derive the number from the cases file in check_hub's output and cite that line, or to stop printing a count in prose. Fix: benchmark/gates/README.md, manual-testing-playbook.md and any future README that quotes the gold set. [SOURCE: AI Systems/Product Owner/benchmark/gates/check_hub.py:296-303] [SOURCE: AI Systems/Product Owner/benchmark/gates/README.md:22] [SOURCE: AI Systems/Product Owner/manual-testing-playbook/manual-testing-playbook.md:28]
7. The manual-testing playbook has no README.md; its index is manual-testing-playbook.md, with seven scenario files under hub-routing/. The staging question names playbook READMEs, so the file it means is this one, and it is the document that carries the stale 33. Recorded so the scope is answerable rather than left open. Fix: none beyond the count. [SOURCE: AI Systems/Product Owner/manual-testing-playbook/manual-testing-playbook.md:1-30]
8. One README claim cannot be checked from this run: the playbook says a scenario run is complete only when its outcome is persisted under benchmark/reports/<dated-run-label>/, and benchmark/reports/ is out of scope here, so no report was opened and no count of dated runs is asserted. Recorded as an open question rather than a pass. [SOURCE: AI Systems/Product Owner/manual-testing-playbook/manual-testing-playbook.md:20-22]

## Ruled Out
- Treating the root README's 21 plus 7 example split as stale: the knowledge folder holds exactly 5 Task, 4 Bug, 7 Doc, 5 Story and 7 Flow mirrors
- Treating the claude project README's 63-file upload list as stale: the folder holds 63 markdown files, 35 core and 28 examples
- Treating 'all 12 gates pass' as stale: run_gates.sh declares twelve entries and the four clone-time skips are exactly the ones its README names

## Dead Ends
- Looking for a gate that reads a README count: none does, which is why three documents kept the old number while one was updated

## Edge Cases
- Ambiguous input: The staging question lists 'both packet READMEs' and 'manual-testing-playbook READMEs'; the first exist and the second is an index file with another name, both recorded
- Contradictory evidence: The playbook's own overview and success criteria disagree on the gold-row count; the success-criteria number is the one the gate prints
- Missing dependencies: benchmark/reports/ is out of scope, so the dated-run claim is unverified rather than failed
- Partial success: Counts were taken by listing folders and parsing JSON and shell case labels, not by running the gates; the root README's printed result lines therefore remain claims about a run, not observed output

## Sources Consulted
- specs/z-staging-po-019s/research/lineages/deepseek/steer.md
- AI Systems/Product Owner/README.md
- AI Systems/Product Owner/USER-GUIDE.md
- AI Systems/Product Owner/claude project/README.md
- AI Systems/Product Owner/sk-product-owner/README.md
- AI Systems/Product Owner/sk-create-figjam/README.md
- AI Systems/Product Owner/benchmark/README.md
- AI Systems/Product Owner/benchmark/gates/README.md
- AI Systems/Product Owner/benchmark/router/README.md
- AI Systems/Product Owner/benchmark/format/README.md
- AI Systems/Product Owner/benchmark/grader/README.md
- AI Systems/Product Owner/benchmark/parity/README.md
- AI Systems/Product Owner/manual-testing-playbook/manual-testing-playbook.md
- AI Systems/Product Owner/benchmark/gates/check_hub.py
- AI Systems/Product Owner/benchmark/router/differential.py
- AI Systems/Product Owner/benchmark/router/route_contract.py
- AI Systems/Product Owner/benchmark/format/run_fixtures.sh

## Assessment
- New information ratio: 0.66
- Questions addressed: Which README claims are stale against the files they describe?
- Questions answered: Which README claims are stale against the files they describe?

## Reflection
- What worked and why: Checking each number against the file or the folder rather than against another README found three stale counts and cleared every other claim
- What did not work and why: The first pass assumed the root README's counts would be the stale ones; it is the most current of the three documents and the gate README the oldest
- What I would do differently: Grep for every numeral a README prints, then resolve each to a file or a command; a number no file can reproduce is the one that drifts

## Questions Remaining
- Which scripts, functions, flags and config entries are dead code?
- Which references, assets, examples and playbook files are dead documents?
- How does the Product Owner's own Python, shell, JavaScript and JSON deviate from the sk-code-skilled standards?
- What is the ranked synthesis of every finding, and what can the repository not settle?

## Recommended Next Focus
Question 7: dead code. Search scripts, benchmark (excluding reports) and both packets for functions, flags and config entries nothing calls, imports, tests or documents, naming the exact search performed before calling anything dead.
