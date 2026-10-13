---
title: "Phase Record: Route what people actually type"
description: "What shipped for R1: the semantic topic table restored to SKILL.md, four overfitted pattern families generalised, a semantic path to the Epic shape, a prose-versus-executable drift guard and a held-out probe set."
importance_tier: "high"
contextType: "implementation-record"
---
# Phase Record: Route what people actually type

<!-- SPECKIT_LEVEL: 2 -->

---

## 1. WHAT WAS WRONG

Three defects were found by routing real requests through a fresh model rather than through the gates the router was written against.

The first was the serious one. Moving the router pseudocode out of `SKILL.md` and into the ON_DEMAND `references/router-contract.md` left `SKILL.md` instructing a scoring step whose vocabulary it no longer carried. Every gate stayed green, because the executable contract was untouched and nothing executed the prose. A model routing from `SKILL.md` alone could not resolve any request that reached step 7, so it emitted no command token and no artifact framing. Five of eighteen tested requests failed for exactly that reason.

The second was overfitting. An earlier pass fixed a twenty-request probe set and then promoted those twenty requests into fixtures, which made the fixtures unable to detect that the patterns had learned the probe strings rather than the intent. "tidy up the copy" routed and "tidy up the labels" did not. "shows `--`" routed and "shows a broken image" did not. "crashes" routed and "freezes" did not.

The third was reachability. Shape resolution defaults to Story whenever no framing matches, so a large-scope request could never reach the Epic shape without the literal word "epic".

---

## 2. WHAT SHIPPED

### Semantic topics restored to the surface a model reads

`SKILL.md` section 2 now carries a `### Semantic Topics` subsection: the nine topics with their route, a usable trigger set and the confidence override, in eighteen lines. The regex mechanics, the scoring arithmetic and the phrase-gap machinery stay in `references/router-contract.md` as the exact implementation. `SKILL.md` went from 359 to 377 lines against a 600-line ceiling.

### Four pattern families generalised

| Family | Was | Now |
| --- | --- | --- |
| Bug symptom | `crash` inflections, `this is broken`, `shows --` | a symptom verb family (freeze, hang, stall, glitch, lock up, time out, stop doing X, come out wrong), a broken-value family across show, display and render, and a 4xx or 5xx status code |
| Task polish | the literals `tidy up the copy`, `make it consistent`, `inconsistent copy`, `copy consistency` | the stems `tidy up`, `clean up`, `tighten up`, `consistent`, `consistency`, `inconsistent`, `inconsistently`, plus `wording` and `label` |
| Story denial | `can't ... let them` only | a person noun followed by a denial of capability, with whole-line lookaheads that keep defect reports and regressions out |
| Epic scale | `whole ... thing` only | a scale word landing on a noun that names a body of work |
| Doc commissioning | `write`, `create`, `draft` only | the same verbs plus `put together`, `pull together`, `prepare`, `assemble`, and a `written up` or `written down` construction |

Doc was not one of the four families named for this phase. It carried the same defect in the same shape, its probes sat in the held-out set, and the widening was kept to two constructions.

### A semantic path to the Epic shape

The initiative-scale construction lives in `SHAPE_FRAMES["EPIC"]`, so one pattern selects the Story lane and resolves the Epic shape together. A pure topic score still defaults to Story, because a topic score names the lane rather than the shape and Story is the cheaper mistake for an author to correct. What was unreachable was the case where the request does say how big the thing is without using the word "epic", and that case now resolves.

### A drift guard between the prose and the executable tables

`benchmark/router/differential.py` gained Guard 0. It parses the `SKILL.md` topic table and asserts the topic names and their order match the executable tables, each route label maps to the same intent, each override matches, each row carries at least three triggers, and every trigger printed in the prose is a real synonym the router scores. The check is a subset check rather than an equality check, because the prose table is deliberately a summary. It fails on a removed synonym and on a changed override, both verified by tampering with the loaded tables.

---

## 3. MEASUREMENT

The original twenty probes are fixtures now and cannot measure generalisation, so a new held-out set of twenty-five requests plus five guards was written. It spans Bug, Task, Doc, Story, Epic and Story Draft, and it stays out of `fixtures.json` and `differential_corpus.json`. `run_probe.py` in this folder routes it and prints the resolved intent and shape per request so correctness can be judged rather than counted.

| Measure | Before | After |
| --- | --- | --- |
| Held-out probes correct | 4 of 25 | 25 of 25 |
| Held-out probes falling back | 21 | 0 |
| Guards correct | 5 of 5 | 5 of 5 |
| Router fixtures | 100 of 100 | 118 of 118 |
| Differential inputs | 174 of 174 | 192 of 192 |

Eighteen fixtures were added, each one declared with its expected route before the router was consulted and refused if the router disagreed. Nine of them are negative or guard cases for the widenings: the imperative sense of "stop", a system subject rather than a role in front of "is unable to", "the whole team", "we cant let this slip", a defect that says "writing up", and the four excluded initiative verbs.

---

## 4. FILES

| File | Change |
| --- | --- |
| `AI Systems/Product Owner/sk-product-owner/SKILL.md` | semantic topic table added to section 2 |
| `AI Systems/Product Owner/sk-product-owner/references/router-contract.md` | pseudocode widened to match the contract |
| `AI Systems/Product Owner/claude project/Custom Instructions.md` | pseudocode block resynced byte for byte |
| `AI Systems/Product Owner/benchmark/router/route_contract.py` | the four generalised families plus the Doc verbs |
| `AI Systems/Product Owner/benchmark/router/differential.py` | Guard 0, prose versus executable table parity |
| `AI Systems/Product Owner/benchmark/router/fixtures.json` | eighteen fixtures added |
| `AI Systems/Product Owner/specs/008-router-and-skill-slimming/003-router-coverage/probe-set.json` | the held-out set |
| `AI Systems/Product Owner/specs/008-router-and-skill-slimming/003-router-coverage/run_probe.py` | the held-out runner |

---

## 5. NOT DONE

`ai-system-sync check --run-validators` exits 3 on `KERNEL_REVIEW_REQUIRED`, because the contract inputs changed and the recorded kernel review digest no longer matches. Clearing it needs `review-kernel` with a named human reviewer and a reason, which was out of scope for this phase. Every other check in that run passed, and `sync --write` applied its three changes with the Router Contract mirror byte-identical to its source.
