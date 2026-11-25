---
title: "Scripts Tests: Vendor Synchronization"
description: "Tests for vendor-sync.py that use temporary local and upstream repositories."
trigger_phrases:
  - vendor sync tests
  - scripts tests
version: 1.0.1.0
---

# Scripts Tests: Vendor Synchronization

---

## 1. OVERVIEW

`scripts/tests/` contains tests for `scripts/vendor-sync.py`. Each test creates a temporary upstream Git repository and a temporary local repository, then invokes the script as a subprocess. The tests do not read or write the shared skill repository. The remote tests clone a temporary bare repository through `VENDOR_UPSTREAM_URL` into a temporary `VENDOR_UPSTREAM_CACHE`, so no test reaches the network.

---

## 2. FILES

| File | Responsibility |
|---|---|
| `scripts/tests/test_vendor_sync.py` | Verifies pulls, pushes, sync, diff, status reporting with and without upstream, include and exclude rules, the override root check, a malformed manifest, symlink rejection, path containment, rebuild lines for dependency and source changes, the remote source and its cache reuse, and `add` with its refusals |

---

## 3. VALIDATION

Run from the repository root:

```bash
python3 -m pytest -q scripts/tests
```

Expected result: pytest reports 41 passed tests and exits with status 0.

The test module can also run directly:

```bash
python3 scripts/tests/test_vendor_sync.py
```

Expected result: `Ran 41 tests` followed by `OK`.

---

## 4. RELATED

- [`scripts/README.md`](../README.md) describes the repository scripts
- [`scripts/vendor-sync.py`](../vendor-sync.py) is the script under test
