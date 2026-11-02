---
title: "Context Folder"
description: "Local reference material you give the Product Owner system for any creation. Git tracks only this README and .gitkeep."
trigger_phrases:
  - "context folder"
  - "reference material"
  - "give the ai context"
---

# Context

> Drop reference material here and point the AI at it when you ask for something.

---

## 1. OVERVIEW

This folder holds anything you want the Product Owner system to use as a reference while it creates something: briefs, meeting notes, exported docs, screenshots, earlier examples or data. It is yours to fill.

The system does not read this folder on its own. Name the file in your request so the AI loads it, for example `use context/launch-brief.md as the source`.

---

## 2. USAGE

1. Copy or export the material into this folder. Markdown, plain text, PDF and images all work.
2. Mention the file path in your request.
3. Remove files once you no longer need them. Nothing here is cleaned up for you.

---

## 3. WHAT STAYS PRIVATE

Everything you add here stays on your machine. The system's `.gitignore` keeps the contents of `context/` out of git, so nothing you put here is committed or shared with anyone who clones the repository.

| Path | Tracked by git |
| --- | --- |
| `context/README.md` | ✅ Yes |
| `context/.gitkeep` | ✅ Yes |
| Any other file or folder in `context/` | ❌ No |

To confirm, add a file and run `git status` from the system folder. The new file does not appear in the output.
