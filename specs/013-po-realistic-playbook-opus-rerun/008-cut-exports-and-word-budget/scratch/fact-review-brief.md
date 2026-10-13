# Brief: review the cut exports for lost or changed facts

The Opus 5.5 benchmark exports were cut by about 30% on 2026-09-26. The operator allowed cutting restated context, background nobody acts on and explanation past the first reason, and ruled that every supplied value, name, number, owner, decision, requirement and open question stays. A script already proved that every heading, label, backticked value, number and link survived. It cannot see a fact carried in plain words, so you read for that.

## Gates, already answered

- Spec folder: `AI Systems/Product Owner/specs/013-po-realistic-playbook-opus-rerun/008-cut-exports-and-word-budget`. Do not ask about documentation.
- Nobody is at your prompt. Ask nothing and wait for nothing.
- Read-only on the exports and the snapshots. Write exactly one file, the one your dispatch names. Run no git command.
- No em dashes in what you write.

## Where things are

- Cut exports: `AI Systems/Product Owner/export/benchmark/<path>`.
- Snapshots from before the cut: `AI Systems/Product Owner/specs/013-po-realistic-playbook-opus-rerun/008-cut-exports-and-word-budget/scratch/before-cut/<path>`, same relative paths.
- Your lists: `.../008-cut-exports-and-word-budget/scratch/groups/g<N>.txt`, paths relative to `export/benchmark/`.

## The question, for every file

Read the snapshot, then the cut file. For each sentence the cut removed or rewrote, ask whether a fact left, changed or arrived. A fact is anything a reader of the ticket would act on or cite: who, what, where, when, platform, surface, owner, team, sign-off, escalation path, scope and out-of-scope, a condition, a requirement or checklist condition, an order of steps, today's state or workaround, a status word, a deadline, a decision and who makes it, a question left open, and the one reason that explains a decision or constraint.

- **Fine, no entry:** a restatement whose fact still stands elsewhere in the same file, background narrative that changes no requirement, a second or third clause that elaborates a reason already given, and color no one acts on, such as which kind of user complained most. In a subtask or a task inside a Story bundle, context its parent file carries is a restatement, provided the parent still carries it.
- **Dropped:** the fact appears nowhere in the cut file.
- **Changed:** the fact is still there but means something else: a hedge became a claim, a condition became unconditional, "or" became "and", a proposal became a decision, a scope item moved in or out, or the reason for a decision is gone entirely.
- **Added:** the cut says something the snapshot did not.

A cut that removes the only reason given for a decision or an out-of-scope item is Dropped, even though the decision stays.

## What you return

Your file opens with one line per problem: `path | snapshot line | cut line | Dropped, Changed or Added | the fact, quoted from the snapshot`. Then a count of files read and problems found. Say plainly when a file has none. Quote rather than paraphrase.

Your final message is the path of your file and the problem lines, nothing else.
