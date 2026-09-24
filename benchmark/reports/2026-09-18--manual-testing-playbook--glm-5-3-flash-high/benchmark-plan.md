# Product Owner benchmark plan: GLM 5.3 Flash through Pi

Skill against Claude Project, run from the manual testing playbook, on `llmgateway/glm-5.3-flash` at thinking `high` through the Pi CLI and the LLM Gateway.

---

## 1. WHAT THIS RUN ANSWERS

The same question the 2026-09-17 Claude run answered, on a different model: does the skill packaging and the Claude Project packaging of Product Owner deliver the playbook's contract, how fast, and where do they part.

Every scenario comes from `sk-product-owner/manual-testing-playbook/`. Nothing is invented for this run. The prompts, the turn chains and the pass lines are the playbook's own, read from each scenario's conversation-chain table.

| Measure | Skill | Claude Project |
| --- | --- | --- |
| Scenarios | 7 | 7 |
| Turns | 14 | 14 |
| Twin pairs | 7 | 7 |

---

## 2. RUNTIME

Each turn is one non-interactive Pi call:

```bash
sandbox-exec -p "<profile>" pi -p --offline --mode json \
  --model llmgateway/glm-5.3-flash --thinking high \
  --session-dir <sessions> --session-id <per-scenario id> \
  --no-context-files --no-skills --no-extensions --no-prompt-templates --no-themes --no-approve \
  --tools <per side> --system-prompt "<per side>" -- "<exact turn input>" </dev/null
```

| Flag | Why it is there |
| --- | --- |
| `sandbox-exec` | the runtime can read and write only its own sandbox and session folder, enforced by macOS rather than checked, see section 3 |
| `--offline` | Pi's startup network probes are not bounded by any timeout and have hung past two minutes |
| `</dev/null` | a non-interactive Pi left holding stdin waits forever with no output |
| `llmgateway/glm-5.3-flash` | provider-qualified, because a bare id resolves against Pi's default provider and silently runs a different model |
| `--thinking high` | the requested effort level |
| `--session-id` | turn 2 resumes turn 1's conversation, proved in a smoke test where turn 2 recalled a word given in turn 1 |
| `--no-context-files` and the other `--no-*` flags | the host's own AGENTS.md, skills, extensions and templates cannot reach the runtime under test |
| `--mode json` | per-message tokens, reasoning tokens, cost and every tool call, captured for grading and for speed |

| | Skill | Claude Project |
| --- | --- | --- |
| System prompt | `AGENTS.md` | `claude project/Custom Instructions.md` plus the retrieval line |
| Working directory | disposable copy of the system with `sk-product-owner/` and an empty `export/` | disposable copy of `claude project/`, the kernel and `knowledge/` |
| Tools | `read, bash, edit, write, ls, grep, find` | `read, ls, grep, find` |

**The skill loads itself.** `AGENTS.md` says manual load is valid and tells the runtime to read `sk-product-owner/SKILL.md` first. The pilot confirmed it does, opening `SKILL.md`, `hvr-core.md`, `conciseness.md`, `task-mode.md` and `task-templates.md` before writing.

**The Project reads but never writes.** A claude.ai Project has no filesystem. A Project given write tools can satisfy a delivery rule by saving a file, which the deployed runtime cannot do. The four read tools stay because opening `knowledge/` is how Project Knowledge retrieval is simulated in a terminal. A probe proved the allowlist: asked to write a file, the runtime listed exactly those four tools and no file appeared.

**The retrieval line** is appended to the Project kernel, verbatim from `run_packaging.sh`. A real Project hands knowledge over from a retrieval index and a terminal does not, so without it the Project set measures the runtime's retrieval habits rather than the packaging.

---

## 3. SANDBOX AND ISOLATION

Every scenario is built fresh in its own tree under `$TMPDIR/pi-playbook-bench/product-owner/<side>/<ID>`, with its own session directory beside it, never inside it.

| Side | Built from | Removed |
| --- | --- | --- |
| Skill | the whole system directory | `benchmark/`, `manual-testing-playbook/`, `export/`, `changelog/`, `claude project/` |
| Project | `claude project/` | `README.md` and any review file |

Isolation is proved before every scenario, and a failure stops the run rather than annotating it:

- Skill: no playbook and no earlier benchmark replies reachable, `AGENTS.md` present, no Project packaging reachable
- Project: no `SKILL.md`, no `AGENTS.md`, no `sk-*` tree, the kernel present

The check was proved red by injection before this plan was written. A playbook folder and a `benchmark/` folder injected into a skill tree were both caught, and an `AGENTS.md` and an `sk-x/` folder injected into a Project tree were both caught.

**The first run leaked, and isolation is now enforced by the operating system.** The check above inspected what each sandbox held, which is not the same as what it could reach. Every sandbox sat beside its siblings and the session logs sat beside them too. In Product Owner a skill runtime listed `..` and read two sibling exports into its own deliverable, and a Project runtime grepped every sibling sandbox. A scan of every tool call in all three systems found those two, plus four calls that listed a scenario's own folder by its absolute path and returned nothing else.

Each Pi call now runs under a macOS `sandbox-exec` profile. It refuses reads and writes under every sandbox, the repository with its playbooks and earlier replies, and the operator's transcripts. Then it allows back the scenario's own sandbox and session folder, plus metadata only on the folders above them, because resolving a path stats every parent and a write to a new file failed without it. Proved on a real Pi call: a sibling file read through `bash` and through `read` both returned `Operation not permitted`, listing `..` was refused, the repository was refused, and a write to a new file inside the sandbox succeeded and read back.

`SST-001` and `PST-001` were rerun under the enforced profile. The leaked runs are kept in `failed-attempts/` as `*-sandbox-leak`. An intermediate rerun whose profile also blocked its own writes is kept as `*-sandbox-overblock`, because it hit that error twice and worked around it, so it measured the harness. The final rerun made no out-of-sandbox call and hit no refusal.

**Side-effect ledger.** Every file in the tree is hashed before turn 1 and after every turn. Created, modified and deleted paths are recorded per turn. This is the playbook's ledger, taken mechanically rather than by operator capture.

---

## 4. SCENARIOS

| ID | Scenario | Group | Turns | Twin | Profile |
| --- | --- | --- | ---: | --- | --- |
| `SID-001` | Skill identity handover | skill-identity | 2 | `PID-001` | standard |
| `STK-001` | Task command flow | skill-backlog-modes | 2 | `PTK-001` | standard |
| `SBG-001` | Bug report flow | skill-backlog-modes | 2 | `PBG-001` | standard |
| `SDK-001` | Doc guide delivery | skill-document-modes | 2 | `PDK-001` | standard |
| `SDK-002` | Doc conflict gate | skill-document-modes | 2 | `PDK-002` | standard |
| `SST-001` | Story shape hard values | skill-story-modes | 2 | `PST-001` | standard |
| `SIR-001` | Ambiguous intake energy choice | skill-interactive-routing | 2 | `PIR-001` | standard |
| `PID-001` | Project identity handover | project-identity | 2 | `SID-001` | standard |
| `PTK-001` | Task command flow | project-backlog-modes | 2 | `STK-001` | standard |
| `PBG-001` | Bug report flow | project-backlog-modes | 2 | `SBG-001` | standard |
| `PDK-001` | Doc guide delivery | project-document-modes | 2 | `SDK-001` | standard |
| `PDK-002` | Doc conflict gate | project-document-modes | 2 | `SDK-002` | standard |
| `PST-001` | Story shape hard values | project-story-modes | 2 | `SST-001` | standard |
| `PIR-001` | Ambiguous intake energy choice | project-interactive-routing | 2 | `SIR-001` | standard |

No scenario in this playbook needs a seeded file or a special tool profile. `SID-001`'s fixture is the delivery line it expects, `Verified: read-back succeeded; N lines`, not a file.

---

## 5. EXECUTION ORDER

The playbook's waves, and how this run orders them:

| Wave | Scenarios | Why |
| --- | --- | --- |
| 1 | `SID-001`, `PID-001` | the handovers gate each set, so they run first and alone |
| 2 | `STK-001`, `SBG-001`, `PTK-001`, `PBG-001` | backlog modes |
| 3 | `SDK-001`, `SDK-002`, `PDK-001`, `PDK-002` | doc modes, clarification exports allowed on the skill side |
| 4 | `SST-001`, `PST-001` | story mode |
| 5 | `SIR-001`, `PIR-001` | intake clarification |

Wave 1 runs first and alone. After it, scenarios run in the skill set's wave order, and each Project scenario runs beside its skill twin rather than in its own later wave. The waves group scenarios for a hand run, where one operator works one runtime at a time. Here every scenario has its own sandbox, so only wave 1 is an ordering rule, and pairing twins is what keeps the speed comparison fair: both packagings of one scenario meet the same gateway load. Four scenarios run at once.

**A failed gate does not stop the set, and this is a deliberate departure.** The playbook stops a set when its handover fails, because a failed handover there usually means the wrong runtime was reached. Here isolation is proved mechanically before every scenario, so a failed handover is a model result, not a wrong runtime. The rest of the set still runs, and every verdict from that set is reported as coming after a failed gate.

**Retries are for mechanical failures only.** A scenario is rebuilt from scratch and rerun, up to three attempts, when a turn times out at 900 seconds, exits non-zero, ends without a final event, stops on an error or returns an empty reply. A bad answer is never retried. Every failed attempt keeps its evidence in `failed-attempts/`.

---

## 6. WHAT LANDS IN THIS FOLDER

```text
benchmark/reports/2026-09-18--manual-testing-playbook--glm-5-3-flash-high/
  benchmark-plan.md          this plan
  run/pi_playbook_runner.py  the runner, identical in all three systems
  run/collect_exports.py     copies the deliverables out to export/benchmark/
  manifest.json              every scenario, its turns, tools and seeds, plus the Pi version
  run-log.jsonl              one line per turn: timing, tokens, cost, tools, ledger, attempt
  run-status.json            one line per scenario: completed or not, attempts
  replies/<ID>-turn<N>.txt   the final reply of each turn, the shape the graders read
  skill/<ID> - <slug>/       one folder per skill scenario
  claude project/<ID> - <slug>/
  results.csv                verdicts, after grading
  hvr-lint.csv               the system's own voice lint, after grading
  results.md                 the write-up, after grading
```

The deliverables themselves go to `export/benchmark/`, which holds real artifact exports and nothing else. `skill/<ID> - <file>` is every file a skill scenario wrote, as written. `claude project/<ID> - <reported name>` is every deliverable a Project reply returned, cut from the reply and saved under the export name the reply reported, because a Project cannot write files. Re-measure rounds land in `<side>/<round>/<run>/`. `run/collect_exports.py` builds that folder from this one.

Each scenario folder holds:

| File | What it is |
| --- | --- |
| `turn-<N>.md` | the reply the user would see |
| `transcript-turn-<N>.md` | every tool call, tool result and assistant message in order |
| `exports/` | every file the scenario created or changed, at its path in the sandbox |
| `events-turn-<N>.jsonl` | Pi's raw event stream |
| `meta.json` | timing, tokens, cost, tools, ledger, session id, attempts |

The skill side's `exports/` holds the real deliverables, for example `exports/export/001 - task-payout-pause-toggle.md`. The Project side's `exports/` should never appear, because a Project that writes has broken its contract, and with write tools withheld it cannot.

---

## 7. GRADING

**Verdicts come from the scenario's own pass line.** Each verdict is `PASS`, `FAIL`, `PARTIAL` or `SKIP`, taken against that scenario's `Pass/fail` line and expected signals, with one line of evidence quoting the turn it rests on.

**Graders did not run it.** A grader that neither built this harness nor produced the replies reads the scenario file and its evidence folder. The runtime is GLM. The graders are Claude, briefed on the scenario and the evidence, never on an expected verdict.

**Every skill save needs a read-back.** The playbook's global rule, verify each saved file can be read before returning its path, applies to every save whether or not the reply claims one. A delivery with no read of the saved path after the write does not pass: `PARTIAL` when the scenario's own pass line does not name verification, `FAIL` when it does.

**Claims are checked against the ledger, not the reply.** A skill reply saying `Verified: read-back succeeded` passes only if the transcript shows a read of that exact path after the write. A saved path passes only if it exists in `exports/`. A Project reply passes only with an empty ledger and no save claim.

**Rules carried over from the Claude runs:**

- `PARTIAL` is never counted as a pass and never compared across twins
- A scenario that ran fewer turns than it declares is `FAIL`, unless a mechanical failure survived three attempts, which is `SKIP` with the reason
- `SKIP` only for a named runtime blocker, never for a soft or inconclusive result, as the playbook requires
- No ClickUp connector exists in this runtime, so an offer to push is inert and never part of a verdict

**Mechanical checks, using this system's own tools:**

```bash
python3 "../../benchmark/grader/lint_replies.py" .        # writes hvr-lint.csv beside replies/
python3 "../../benchmark/grader/twin_divergence.py" .     # pairs S and P verdicts from results.csv
```

---

## 8. WHAT IS MEASURED

| Area | Measure | Source |
| --- | --- | --- |
| Speed | turn time from agent start to agent end, median and slowest tenth, per side | arrival-stamped Pi events |
| Speed | Pi startup, reported separately | the same stamps |
| Effort | output tokens, reasoning tokens, tool calls per turn | Pi usage blocks |
| Cost | US dollars per turn and per scenario | Pi cost blocks |
| Quality | pass rate per side, twin divergences | `results.csv` |
| Quality | voice lint clean rate and hard violations per side | `hvr-lint.csv` |
| Contract | files created on each side, and any file a Project created | the ledger |

**Timing is stamped on arrival.** Pi stamps an assistant message when it starts, not when it ends, so a one-message reply measured from Pi's own stamps reads as instant. The pilot caught this at 0.01 seconds. The runner stamps each event as it arrives, and a turn runs from `agent_start` to `agent_end`.

---

## 9. THE BASELINE IT IS COMPARED WITH

`Product Owner/benchmark/reports/2026-09-17--manual-testing-playbook--claude-sonnet-5-medium/`, Claude Sonnet 5 at medium effort.

| Measure | Skill | Claude Project |
| --- | --- | --- |
| Single run | 4 of 7 | 2 of 7 |
| Clarification turn, sampled | 8 of 13 | 1 of 13 |
| Bug report block, sampled | 8 of 8 | 3 of 9 |
| Median turn time | 32.4 s | 18.9 s |

The two sampled gaps were both delivery protocol. The Project left out the export-equivalent path and the self-scan line on a clarification turn, and never named the Deliverable Block on a bug report. Those two are the first things to read in this run.

---

## 10. WHAT THIS RUN CANNOT SETTLE

- **One run per scenario.** Sampling the Claude run at five per side showed 11 of 16 single-run twin divergences were draws. A divergence here is a candidate until it is sampled
- **The Project is a terminal stand-in.** The kernel is the system prompt and the knowledge is files. Real claude.ai speed and retrieval will differ
- **Model and harness both changed.** The baseline ran on Claude Code, this runs on Pi. The harness design is the same, so a difference is mostly the model, but not provably only the model
- **Gateway latency varies with load.** Twins run side by side, so the ratio within this system is the reliable speed figure and absolute seconds are not

---

## 11. HOW TO RUN IT AGAIN

```bash
cd "AI Systems/Product Owner/benchmark/reports/2026-09-18--manual-testing-playbook--glm-5-3-flash-high"
python3 run/pi_playbook_runner.py --system ../../.. --out . --jobs 4
python3 run/collect_exports.py . ../../../export/benchmark
```

One scenario or one side:

```bash
python3 run/pi_playbook_runner.py --system ../../.. --out . --ids STK-001,PTK-001
python3 run/pi_playbook_runner.py --system ../../.. --out . --side project
```

`--dry-run` prints the manifest without calling the model.
