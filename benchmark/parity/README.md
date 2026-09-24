---
title: "benchmark/parity: wrappers into the shared parity gate"
description: "Three wrappers that exec into the shared parity gate, passing the id or directory it cannot know."
trigger_phrases:
  - "parity wrappers"
  - "upload receipt"
---

# benchmark/parity: wrappers into the shared parity gate

---

## 1. OVERVIEW

`benchmark/parity/` holds this system's wrappers into the shared parity gate. The gate lives in `AI Systems/z — Claude Project Sync Loop/` and decides whether the hand-authored Claude Project package matches its skill sources. A wrapper hands over the only per-system thing the gate cannot know, a system id or a target directory, then execs.

Current state:

- Two wrappers run the shared gate, one runs the receipt writer
- Each ends in an `exec`, so the tool's exit code is the wrapper's
- No check or receipt logic lives here, the shared gate owns those
- Every wrapper finds its own directory first, so where you run it does not matter

---

## 2. FILES

| Wrapper | Responsibility |
|---|---|
| `run_parity.sh` | Runs the shared gate with this system's id. Extra arguments pass through, so `--range` pins a commit range, default `origin/main..HEAD` |
| `run_receipts.sh` | Runs the shared gate with `--receipts`, which makes the dated upload receipt a required check |
| `run_receipt_write.sh` | Runs the shared receipt writer against this system's directory, resolved at run time |

---

## 3. EXIT CODES

`run_parity.sh` and `run_receipts.sh` return the shared gate's codes:

| Exit | Meaning |
|---|---|
| 0 | every check passed |
| 1 | the gate reported findings, a parity violation or a due mirror review |
| 2 | the system layout is incomplete or the id is not declared in the gate |

Under `--receipts` a receipt that is missing or stale is a finding like any other, and the run exits 1.

`run_receipt_write.sh` returns the receipt writer's own codes. 0, the rendered line passed the gate's own checks. 1, the rendered line failed them. 2, the system layout or a supplied argument is unusable.

---

## 4. RUN

From the system directory:

```bash
bash benchmark/parity/run_parity.sh
```

Expected result: a line that names this system and the range. Then notes. Then `PASSED` with the declared pair count. Exit 0.

```bash
bash benchmark/parity/run_receipt_write.sh
```

Expected result: the one dated receipt line, printed after the gate's receipt check accepts it. Exit 0. With `--append` the line is added to `SYNC.md` under the review notes heading.

---

## 5. IDENTICAL BY DESIGN

The same bytes sit in all eight systems that have these wrappers. The wrappers earn it. Two of them differ across systems in exactly one line, the id they pass. The receipt writer passes a directory resolved at run time, so even its copies are byte-identical. Nothing here names a system, so one text covers all eight.

---

## 6. RELATED

- [`SYNC.md`](../../SYNC.md), the parity rules it states, the four the gate decides
- [`z — Claude Project Sync Loop/README.md`](../../../z%20—%20Claude%20Project%20Sync%20Loop/README.md), the shared checks these wrappers exec into
