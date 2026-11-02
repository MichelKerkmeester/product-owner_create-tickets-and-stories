# Iteration 17: batching the changes against the real gate state

## Focus

Rank the improvement set into reviewable batches and test each batch against the parity gate and the self-test. Running the gate read-only surfaced three state facts that change the plan: the gate refuses, the Flow Mode files are untracked, and the kernel is already modified in the working tree. Deepens iterations 15–16.

## Actions Taken

1. Ran `python3 validate_parity.py product-owner` read-only; it exited 2 without checking anything.
2. Checked `git status` for the declaration and the three Flow Mode files.
3. Read the live kernel H1 and skill version.
4. Checked which proofs run without git: the checker's `--self-test` and the format gate.

## Findings

1. **The parity gate refuses before it compares anything.** It exits 2 because `systems.py` differs from its HEAD revision, so the declaration is "not the one under version control" and nothing is checked [SOURCE: AI Systems/z — Claude Project Sync Loop/validate_parity.py:90]. Any completion claim of "parity passes" is impossible until the declaration is committed or restored.

2. **The three Flow Mode files are untracked.** `flow-mode.md`, the Flow Mode knowledge mirror and `flow_check.py` all show `??` in `git status`, so the drift comparison has no commit timestamp to compare [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:1] [SOURCE: AI Systems/Product Owner/claude project/knowledge/Product Owner - Templates - Flow Mode.md:1] [SOURCE: AI Systems/Product Owner/sk-product-owner/scripts/flow_check.py:1]. Manual parity step 3 cannot evaluate them until they are committed at least once.

3. **The working tree already carries a broad Product Owner batch.** `AGENTS.md`, `README.md`, `SYNC.md`, the format validator, the router fixtures and the gate scripts are all modified, and the kernel H1 is v1.2.2 against skill v1.2.1.0 [SOURCE: AI Systems/Product Owner/claude project/Custom Instructions.md:1] [SOURCE: AI Systems/Product Owner/sk-product-owner/SKILL.md:5]. Adding Flow Mode edits to this tree without staging discipline would mix unrelated work into one commit.

4. **The checker batch can be proven without git.** `flow_check.py --self-test` runs in a temp directory and proves each rule against a planted model, so the mechanical rules can be verified before any commit or parity run [SOURCE: AI Systems/Product Owner/sk-product-owner/scripts/flow_check.py:154]. That makes the checker the one batch with an independent gate.

5. **Batch A — checker rules.** Constants, conditions, eight planted models, docstring. Proof: `--self-test` exits 0. No mirror, no kernel, no version bump, because `flow_check.py` is not mirrored into the Project.

6. **Batch B — the model rules and the asset.** Nine-bullet rule list, reworded label rule, recalculated check/read-back split, v2 read-back shape in `flow-templates.md`. Proof: Batch A's self-test plus a read of the five shipped patterns against the new rules.

7. **Batch C — the Project mirror.** Section 4 rules, Section 5 write routes, Section 6 read-back, Section 7 recovery, all hand-written from Batch A and B's text. Proof: a paragraph-by-paragraph diff against the skill, recording every deliberate adaptation (no script, no `fj` route).

8. **Batch D — the kernel.** The one-line Flow Mode Delivery change for the section rule, plus the H1 minor bump from v1.2.2 to v1.3.0. Proof: the kernel line stays one line and the version moves in the same change.

9. **The order matters because C depends on A and B, and D depends on C.** Running D first would put a kernel rule ahead of the skill text it summarises, and the next parity read would find the mirror and the skill disagreeing. A → B → C → D is the only order where every step's proof exists when it runs.

10. **Commit is a human step, not part of the batch.** Committing the untracked files and the pending Product Owner work is required before the drift check means anything, but this lineage has no authority to stage or commit [SOURCE: AI Systems/Product Owner/SYNC.md:12]. The synthesis must name it as a precondition rather than perform it.

11. **The kernel review cannot be recorded now.** The `--reviews` check recomputes a content key from the kernel on disk, and the kernel is currently modified and uncommitted, so a review note written today would name text no commit contains [SOURCE: AI Systems/z — Claude Project Sync Loop/validate_parity.py:70]. The dated review line waits for a named human after the batch lands.

12. **The format gate does not apply to Flow Mode.** Flow Mode's deliverable is a board and it writes no artifact file, so the output-format validator has nothing to read; the applicable proofs are the checker self-test, the parity read and the read-back rule [SOURCE: AI Systems/Product Owner/sk-product-owner/references/flow-mode.md:143]. Claiming the format gate for this change would be a category error.

13. **The largest risk in the batch is a mirror drift, not a checker bug.** The skill and the mirror are hand-written pairs, and the page rule exists in three statements on each side; the gate compares commits, not content, so a missed statement passes the gate and stays live [SOURCE: AI Systems/Product Owner/SYNC.md:10]. A paragraph count per section is the only check that catches it before a reader does.

## Ruled Out

- **Running the parity gate as proof now**: it refuses on the declaration state.
- **Committing the batch**: not requested and not authorised here.
- **Recording a kernel review line**: the kernel is uncommitted and the reviewer is a human.
- **Applying the format gate to Flow Mode**: there is no artifact file.

## Dead Ends

- Looking for a git-tracked copy of `flow-mode.md` under another name: `git log` on the path is empty and `git status` shows it untracked, so no earlier revision exists to diff against. Recorded so a later iteration does not search.

## Edge Cases

- Ambiguous input: whether Batch D's kernel line should wait for Batch C's mirror. Resolved as C before D, so the kernel never summarises text the mirror lacks.
- Contradictory evidence: none.
- Missing dependencies: a committed baseline, a human reviewer and a commit authority are all external.
- Partial success: the gate ran but checked nothing; reported as exit 2, never as a pass.

## Questions Answered

- Follow-on: how should the change be batched? Four batches, A → B → C → D, each with its own proof.
- Follow-on: what can be proven today? The checker self-test; nothing gate-dependent.

## Questions Remaining

- Whether the pending Product Owner batch should land before or with the Flow Mode batch; that is the operator's call, not the research's.

## Sources Consulted

- `AI Systems/z — Claude Project Sync Loop/validate_parity.py`
- `AI Systems/Product Owner/SYNC.md`
- `AI Systems/Product Owner/claude project/Custom Instructions.md`
- `AI Systems/Product Owner/sk-product-owner/SKILL.md`
- `AI Systems/Product Owner/sk-product-owner/scripts/flow_check.py`
- `AI Systems/Product Owner/sk-product-owner/references/flow-mode.md`

## Assessment

- New information ratio: 0.66 (the gate refusal, the untracked surfaces and the live versions are new runtime facts; the batching is synthesis)
- Questions addressed: batch order, provability, external preconditions
- Questions answered: both above

## Reflection

- What worked and why: running the gate instead of assuming it would pass produced the state facts that make the plan honest; a gate that cannot run is different from a gate that passes.
- What did not work and why: the first batch order put the kernel second, until the dependency on the mirror showed it had to be last.
- What I would do differently: check git state before writing replacement text, so the plan never assumes a committed baseline.

## Recommended Next Focus

Iteration 18: build the final ranked table — impact, effort, risk, dependencies and proof for each of the thirteen candidates — and settle ties with the corpus evidence rather than with implementation convenience.
