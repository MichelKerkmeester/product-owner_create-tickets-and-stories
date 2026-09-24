# Manual testing playbook run, 2026-09-17, Product Owner, claude-sonnet-5 medium

Phase 3 of the fleet test-and-parity pass. Every scenario in this system's own
playbook, both packagings, run through the shared parity-gate harness script
(`run_packaging.sh`) with `HARNESS_MODEL=claude-sonnet-5` and
`HARNESS_EFFORT=medium`, `--noweb` on every call since no scenario needs the
web tools.

| File | What it is |
| --- | --- |
| `results.csv` | All 14 scenarios, `id,runtime,model,result,note` |
| `replies/` | Every captured turn, 28 scenario replies |
| `evidence/` | The retrieval probe of section 1, kept out of `replies/` so the lint counts runtime deliverables only |
| `hvr-lint.csv` | Written by this run's own `check_report.sh` pass, see section 6 |
| `README.md` | This file |

---

## 1. The probe, read this first

Brief before the tables below: run this probe yourself before trusting any
characterization of the Project runtime, mine included.

**What I ran:** `run_packaging.sh "Product Owner" project "Use a tool to list
the files in the knowledge/ directory beside these instructions, and name
three of them exactly as they appear on disk. If you cannot do this, say so
plainly rather than guessing." --noweb`, with the default retrieval line
present.

**What came back:** it opened the directory and named three real files
verbatim (`Product Owner - Assets - Bug Report Template - v0.100.md`,
`Product Owner - System - Router Contract - v0.100.md`, `Product Owner -
Rules - Human Voice Core - v0.100.md`), all three confirmed present in the
scratch tree. Its own file count (40) was off by two against the actual 38,
which reads as a listing miscount rather than fabrication, since every name
it gave was real and exact.

**What this means for the rest of this report:** the retrieval-measurement
brief characterizes Product Owner as one of two systems that "said it cannot
open them" even when bluntly told to use a tool. My probe does not reproduce
that. Told plainly to use a tool, this runtime opened `knowledge/` on the
first try, the same outcome the brief recorded for Sales Direct rather than
for Product Owner's own prior characterization. I did not re-run the
weaker "name a rule and cite the document" probe that produced the original
finding, so I cannot say why the two probes disagree, only that they do.
**Practical consequence: every Project failure recorded below is graded as a
rule or behavior question, not a reading-capability question, because the
capability is established.** Section 5 still separates causes per-failure,
because capability when explicitly told to use a tool is not the same claim
as spontaneous retrieval mid-scenario, and one of the five Project failures
turns on exactly that distinction.

---

## 2. Scope, counted by walking the directory

```
find "sk-product-owner/manual-testing-playbook" -type f -name "*.md" | wc -l
```
returns 15: the root playbook plus 14 scenario files, seven under the
`skill-*` groups (`S`-prefixed) and seven under the `project-*` groups
(`P`-prefixed). That matches "7 skill scenarios, 7 Project scenarios."

It does not match "15 of them multi-turn." Reading all 14 scenario files
directly, every one of them is a two-turn conversation (a Turn 1 and a
Turn 2 row in its own conversation-chain table). There are 14 multi-turn
scenarios and zero single-turn ones in this playbook, not 15. I am recording
this as a correction rather than silently using either number, since rule 4
asks for an independent count and the two counts cannot both be right.

---

## 3. Method notes

- Each scenario got its own `HARNESS_SCRATCH` subdirectory so all 14 could
  run concurrently without racing on the shared scratch path the script
  otherwise reuses per side. Turn 2 used `--resume <uuid>` against the same
  session generated for Turn 1
- **The harness rebuilds the scratch tree on every invocation, including
  `--resume` calls.** `build_skill`/`build_project` run unconditionally
  before the model is invoked, so a Turn 2 call starts from a freshly
  rsynced copy of the source system, not from whatever Turn 1 left on disk.
  Session memory (what the model said and did) carries over through
  `--resume`. The filesystem does not. In practice, I could verify Turn 1's
  own on-disk artifact only when Turn 2 did not also write a file (never
  happened here), so skill-side grading rests on Turn 1's own claimed
  read-back proof (its Write-then-Read cycle happens inside that one
  invocation, unaffected by the next call's rebuild) cross-checked against
  whatever the final turn actually left on disk. I flag this explicitly
  rather than let a clean disk check silently stand in for something it
  cannot prove for Turn 1 specifically
- No scenario in this playbook needs ClickUp, ambiguous ADR facts, or ground
  truth beyond what each prompt supplies, so nothing was skipped for missing
  fixtures

---

## 4. Counts per packaging

| Packaging | PASS | FAIL | PARTIAL | SKIP | Total |
| --- | ---: | ---: | ---: | ---: | ---: |
| Skill (`S`-prefixed) | 4 | 3 | 0 | 0 | 7 |
| Project (`P`-prefixed) | 2 | 5 | 0 | 0 | 7 |
| **Combined** | **6** | **8** | **0** | **0** | **14** |

Every scenario reached a conclusive two-turn verdict. None is PARTIAL:
nowhere did a harness error stop a Turn 2 from running (all 28 calls
returned exit 0), and nowhere did I grade a multi-turn scenario off a single
turn.

---

## 5. Skill side, scenario by scenario

**PASS: SID-001, STK-001, SBG-001, SDK-002.** All four ran their required
context or conflict gate on Turn 1 (one consolidated question, a
clarification exported to `export/`, the `HVR self-scan:` line, no draft),
then delivered a Turn 2 artifact that kept every supplied fact and invented
nothing. STK-001 and SBG-001's Turn 2 exports were confirmed on disk
(checklist items, frequency field, and the four fixed bug-report checklist
items all matched the source exactly). SDK-002 correctly detected the
Note A/Note B conflict, stopped, and on resolution labeled Note A current and
Note B retired.

**FAIL: SDK-001, SST-001, SIR-001**, all three for a Turn 1 defect that
Turn 2's quality cannot repair (a multi-turn scenario fails conclusively at
its first bad turn, per rule 1):

- **SDK-001** (no-token Doc request, "I will paste the engineering notes"):
  Turn 1 skipped the Doc context gate entirely. Instead of the required
  consolidated question across purpose, audience, source set, authority,
  status and shape, plus a clarification export and self-scan, it replied
  conversationally asking for the notes. No export, no self-scan line at
  all
- **SST-001** (no-token Story request, "Turn these notes into a PRD"): same
  shape of miss. Turn 1 asked for the notes plus two narrow questions
  instead of the mandated consolidated question across role, value, kind,
  requirements and evidence, with no clarification export and no self-scan.
  Turn 2's final Story is otherwise strong (all four hard values verbatim,
  kind named) but also restates "the 24-hour hold" inside an acceptance
  criterion's When clause, a value duplicated into a criterion and a second,
  independent defect in the same scenario
- **SIR-001** (ambiguous, no command, "not sure what shape it should take"):
  the mechanics were right (one exported clarification, self-scan present,
  no early artifact), but the question itself opened with artifact-shape
  options (Task/Bug/Story/Doc) rather than the mandatory Quick-or-Deeper
  energy choice that has to open this exact question. That ordering is the
  entire thing this scenario exists to verify, and it did not happen

---

## 6. Project side, with cause separated

None of the five Project failures below are the runtime declining to read,
per the probe in section 1. I checked each one specifically against
`claude project/Custom Instructions.md` to see whether the missed rule lives
in the always-loaded kernel or only in a `knowledge/` document, because that
distinction is exactly what separates a rule miss from a retrieval miss.

**PASS: PID-001, PDK-002.**

- PID-001 (identity handover): Turn 1 rendered a Deliverable Block with an
  export-equivalent path and a self-scan, no `Path:`, `Saved:` or read-back
  wording. It does not literally contain the phrase "Canvas Artifact" itself
  (the block's own heading reads "Deliverable Block"). Turn 2, asked how a
  reviewer opens the artifact, explicitly names it "a Canvas Artifact
  rendered in the side panel" and restates the no-file-write boundary. Read
  across the two turns the identity contract holds. Recorded as a caveat,
  not a defect, distinct in kind from the failures below because every
  element of the formal contract is present, just split across two turns
  instead of stated identically on both
- PDK-002 (Doc conflict gate): full formal treatment on both turns, conflict
  detected and stopped on Turn 1, Note A/Note B resolved correctly on
  Turn 2, clean ClickUp grammar, a correctly named sanctioned em-dash
  exemption

**FAIL, rule miss (not retrieval): PTK-001, PBG-001, PDK-001, PST-001.**
`Custom Instructions.md` states, in the kernel itself, that a clarification
is one of the Deliverable Block types (line 229: "Clarification:
`export/NNN - ...-clarification.md` ... It carries the question and nothing
else"), that the block renders before any commentary (line 88), that the
export-equivalent path and self-scan follow it (line 89), and that the
self-scan line is required "in every delivery response" (line 92). None of
this is behind a `knowledge/` pointer. The runtime has it in view on every
turn without opening anything, and it applied this exact rule correctly in
PID-001 and PDK-002. In these four scenarios it did not:

  - **PTK-001** and **PBG-001** (`$task`/`$bug`, direct commands): Turn 1 in
    both cases is a plain-text list of context or evidence questions with no
    Deliverable Block, no `Export-equivalent path:`, no self-scan. Turn 2 in
    both cases is a clean, accurate, correctly labeled task or bug block
    that kept every supplied fact
  - **PDK-001** (no-token Doc, "I will paste the notes"): the same gate-skip
    as SDK-001, reproduced on this packaging. Turn 1 asked only about
    audience and purpose, never reached source set, authority, status or
    shape, and rendered no block, label or self-scan
  - **PST-001** (no-token Story, "Turn these notes into a PRD"): the same
    gate-skip as SST-001. Turn 1 asked for the notes plus two narrow
    questions with no block, label or self-scan

**FAIL, retrieval-adjacent and shared with the skill side: PIR-001.** Unlike
the four above, the specific rule PIR-001 needed ("the FIRST interactive
question offers the energy level as its opening choice") is not in
`Custom Instructions.md` at all. It lives only in the knowledge document
`Product Owner - System - Interactive Mode - v0.404.md`, line 79, which the
kernel points to by name five times elsewhere in its routing prose. Turn 1
rendered no Deliverable Block, label or self-scan, and it opened with an
Epic/Story/Task/Bug/Doc shape table instead of the energy choice. I cannot
confirm from a text-only `claude -p` transcript whether the model attempted
to open that file and still got the ordering wrong, or never opened it, so I
am not calling this a proven reading refusal. What I can say: the skill
side's **SIR-001** shows the identical miss (shape-first, no energy choice),
and the skill packaging loads its own mirror of this exact rule
(`references/interactive-mode.md`) through the same kind of on-demand,
trigger-based mechanism SKILL.md documents for its Interactive route, not
through an always-loaded file. Both packagings gate this specific ordering
rule behind an on-demand document, and both missed the ordering the same
way, which reads as a shared behavior under medium effort rather than a
Project-only retrieval defect.

**A sixth, separate finding inside PST-001's PASS/FAIL evidence:** Turn 2's
reply text stays fully in the Project's persona (`Export-equivalent path:`,
no save claimed anywhere in the prose), but the scratch tree shows the
runtime actually wrote `export/001 - PRD-payout-pause.md` to disk, byte for
byte identical to the block shown in the reply. This is the only one of the
seven Project scenarios where the underlying scratch tree picked up a real
file. The other six stayed clean on inspection. Grading from reply text
alone would have missed this entirely, since the text itself never claims a
save. This is a tool-use-level breach of the "cannot write local files"
boundary that a real claude.ai Project could not physically commit (it has
no Write tool at all), so it is also a limitation of running the Project
packaging inside a CLI shell that happens to expose file tools, not proof
that a production Project would do the same. Recorded as a finding, not
folded into the rule-versus-retrieval split above because it is neither.

**A meta-awareness note, PID-001 Turn 2:** the reply explicitly says "Any
earlier tool-call output implying a write completed reflects the harness's
internal scratchpad, not a Barter/Project deliverable path." That is a
literal, correct use of the word "harness" (referring to the test harness
itself), and it shows the model reasoning openly about the fact that it is
running inside an evaluation harness rather than a real claude.ai Project.
Nothing in the kernel or knowledge set uses that framing, so this is the
model's own inference from context, not a leaked instruction. It did not
derail the scenario (the identity contract still held), but it is worth
flagging alongside `run_packaging.sh`'s own stated isolation concern about a
Project run volunteering text that belongs to neither the kernel nor any
knowledge document.

---

## 7. Twin comparisons

Paired by category letters against `results.csv`, matching
`twin_divergence.py`'s own pairing:

| Pair | Skill | Project | Agreement |
| --- | --- | --- | --- |
| ID-001 | PASS | PASS | Agree |
| TK-001 | PASS | FAIL | **Disagree** |
| BG-001 | PASS | FAIL | **Disagree** |
| DK-001 | FAIL | FAIL | Agree |
| DK-002 | PASS | PASS | Agree |
| ST-001 | FAIL | FAIL | Agree |
| IR-001 | FAIL | FAIL | Agree |

5 agreed, 2 disagreed, 0 unpaired, 0 unsettled. Both disagreements share one
root cause: for a plain `$task` or `$bug` context question, the skill
runtime reliably wraps its clarification in the export-plus-self-scan
contract and the Project runtime did not, even though the Project runtime
demonstrably can (PID-001, PDK-002). This is a packaging-specific
consistency gap, not a difference in what either packaging knows.

The other five pairs agree. Three failed identically on both sides: DK-001
(the no-token Doc gate skip), ST-001 (the no-token Story gate skip) and
IR-001 (the missing energy-first order). Two passed identically: ID-001
(with the caveat noted above) and DK-002, the one scenario type that worked
cleanly on both packagings without exception.

---

## 8. What my own checks found

```
bash benchmark/grader/check_report.sh <this report dir>
```
exited **2** (two of two checks reported findings):

**`twin_divergence`**: confirms section 7 exactly. `BG-001: skill PASS,
Project FAIL`, `TK-001: skill PASS, Project FAIL`, 5 agreed, 2 disagreed, 0
unsettled, 0 unpaired.

**`lint_replies`**: 25 of 28 scenario replies are DIRTY, 3 clean
(`SID-001-turn1`, `SDK-001-turn1`, `STK-001-turn1`). The retrieval probe now
sits in `evidence/` rather than `replies/`: it is this lane's own
instruction-following artefact, not a runtime deliverable, and counting it
made the clean rate one reply better than the runtime earned.
The dominant finding by far is `em_dash`, with `semicolon` a distant second
and one `hard_blocker_word:harness` (the literal, non-figurative use
discussed in section 6) and one `bullet_ends_with_full_stop`. The linter
already exempts the two system-granted em-dash shapes (a bolded ClickUp term
followed by an em dash and its definition, and the `Status: {class}`
qualifier label in that same delimited form) per its own documented design,
so this is not an artifact of a missing exemption. It is a genuinely
widespread finding: every scenario I graded PASS still produced at least one reply carrying a banned
em dash, and nearly every one of those replies' own `HVR self-scan:` line
claims "0 hard blockers." The self-scan line is not a reliable count of this
specific rule on this run. I did not fold this into any scenario's
PASS/FAIL verdict, since `lint_replies.py`'s own design treats reply
cleanliness as a separate axis from scenario behavior, and a report that
silently merged the two would hide exactly the gap this check exists to
surface. Full detail in `hvr-lint.csv` beside this file.

---

## 9. What could not be run

Nothing was skipped. All 14 scenarios ran both turns against the real
harness, no scenario named a blocker that would justify SKIP, and no
fixture this playbook depends on was missing. The two open questions are
both named above rather than left implicit: whether PIR-001's miss is a
retrieval refusal or a rule applied without opening the document (section
6), and whether the widespread em-dash finding reflects a self-scan
counting gap specific to this run or a standing one (section 8). Both are
answerable with more runs. Neither was answerable from this one alone.

---

## Next steps

- Decide, at the fleet level, whether the retrieval line should name the
  tool outright (the open question `retrieval-measurement.md` itself leaves
  unresolved), since section 6's one retrieval-adjacent failure is exactly
  the shape that decision would settle
- If this system's own team wants the two twin disagreements closed, the
  fix is narrow: make the Project runtime wrap a plain `$task`/`$bug`
  context question in the same Deliverable Block and self-scan it already
  applies correctly to conflict-gate and identity turns, since the rule is
  already in the kernel and just needs consistent application
- Treat the em-dash finding in section 8 as its own follow-up. A self-scan
  line that reads "0 hard blockers" on a reply that is not is worth a
  dedicated look independent of this playbook
