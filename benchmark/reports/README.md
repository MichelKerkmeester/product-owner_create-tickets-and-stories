---
title: "Product Owner Benchmark Reports"
description: "Index of the Product Owner benchmark run folders, one row per run, newest first."
trigger_phrases:
  - "product owner benchmark reports"
  - "product owner benchmark index"
importance_tier: "important"
contextType: "general"
---

# Product Owner Benchmark Reports

> One row per run folder, newest first. Each folder's own `README.md` (or `manifest.json` where a run has no README) holds its method, verdicts and evidence.

---

## 1. OVERVIEW

The manual testing playbooks in `sk-product-owner/manual-testing-playbook/` and `sk-create-figjam/manual-testing-playbook/` are the corpus, and these folders are what running them produced. Targeted checks of one kernel or Skill change sit beside the full playbook runs. Add a row here when a new run folder lands.

---

## 2. RUN INDEX

| Executed | Folder | What it measured |
|---|---|---|
| 2026-10-25 | [`2026-10-25--manual-testing-playbook--first-glance-and-routing/`](./2026-10-25--manual-testing-playbook--first-glance-and-routing/) | The 18 Flow scenarios after the first-glance and routing pass, on Claude Sonnet 5.5 high |
| 2026-10-24 | [`2026-10-24--manual-testing-playbook--swe-2-max-composed-boards/`](./2026-10-24--manual-testing-playbook--swe-2-max-composed-boards/) | Composed FigJam boards on SWE 2 MAX and Claude Sonnet 5.5 high |
| 2026-10-22 | [`2026-10-22--manual-testing-playbook--deepseek-v4-1-flash-max-live-figma/`](./2026-10-22--manual-testing-playbook--deepseek-v4-1-flash-max-live-figma/) | Playbook scenarios against live Figma on DeepSeek V4.1 Flash max through OpenCode 2 |
| 2026-10-21 | [`2026-10-21--kernel-dedupe--deepseek-v4-1-flash-high/`](./2026-10-21--kernel-dedupe--deepseek-v4-1-flash-high/) | Kernel dedupe check on kernel v1.2.2 |
| 2026-10-20 | [`2026-10-20--manual-testing-playbook--sk-create-figjam-shell/`](./2026-10-20--manual-testing-playbook--sk-create-figjam-shell/) | The `sk-create-figjam` scenarios a shell can run, from the Product Owner root |
| 2026-10-08 | [`2026-10-08--manual-testing-playbook--claude-haiku-5-5-high/`](./2026-10-08--manual-testing-playbook--claude-haiku-5-5-high/) | Full playbook on Claude Haiku 5.5 high, kernel v1.1.0 and Skill v1.1.0.0 |
| 2026-10-03 | [`2026-10-03--skill-trim--deepseek-v4-1-flash-high/`](./2026-10-03--skill-trim--deepseek-v4-1-flash-high/) | Skill trim check, Skill v1.16.4.0 against v1.16.3.0 |
| 2026-10-01 | [`2026-10-01--task-scope-question--deepseek-v4-1-flash-high/`](./2026-10-01--task-scope-question--deepseek-v4-1-flash-high/) | Task scope question check on Skill v1.16.3 |
| 2026-10-01 | [`2026-10-01--skill-ask-first--deepseek-v4-1-flash-high/`](./2026-10-01--skill-ask-first--deepseek-v4-1-flash-high/) | Skill-side ask-first check on Skill v1.16.2 |
| 2026-10-01 | [`2026-10-01--kernel-diet--deepseek-v4-1-flash-high/`](./2026-10-01--kernel-diet--deepseek-v4-1-flash-high/) | Kernel diet check on kernel v1.21.0 |
| 2026-09-30 | [`2026-09-30--router-in-kernel--deepseek-v4-1-flash-high/`](./2026-09-30--router-in-kernel--deepseek-v4-1-flash-high/) | Router in kernel check on kernel v1.20.0 |
| 2026-09-25 | [`2026-09-25--manual-testing-playbook--claude-sonnet-5-medium/`](./2026-09-25--manual-testing-playbook--claude-sonnet-5-medium/) | Full playbook on claude-sonnet-5 medium |
| 2026-09-25 | [`2026-09-25--manual-testing-playbook--claude-opus-5-5-medium/`](./2026-09-25--manual-testing-playbook--claude-opus-5-5-medium/) | Full playbook on claude-opus-5-5 medium |
| 2026-09-18 | [`2026-09-18--manual-testing-playbook--glm-5-3-flash-high/`](./2026-09-18--manual-testing-playbook--glm-5-3-flash-high/) | Full playbook on GLM 5.3 Flash |
| 2026-09-17 | [`2026-09-17--manual-testing-playbook--claude-sonnet-5-medium/`](./2026-09-17--manual-testing-playbook--claude-sonnet-5-medium/) | Full playbook on claude-sonnet-5 medium |

---

## 3. STORAGE RULE

Run folders are named `<YYYY-MM-DD>--<subject>--<variant>`, dated by execution. A run whose result changes gets a new folder rather than overwriting a prior one. Board URLs, the test file key, emails and plan names are redacted with the run's `run/redact_run.py` before a folder is committed, because this repository is public.

The grammar and the report file set are owned by `sk-create-benchmark`. Where this index and that skill differ, the skill is correct.
