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

This folder holds anything you want the Product Owner system to use as a reference while it creates something: briefs, meeting notes, exported docs, screenshots, earlier examples or data. It is yours to fill, and whatever you add stays on your machine.

The system does not read this folder on its own. Name the file in your request so the AI loads it.

| Question | Answer |
| --- | --- |
| What goes here | Any file the AI should read before it writes |
| When the AI reads it | Only when your request names the file |
| Who sees it | Only you. Git ignores everything here except this README and `.gitkeep` |

---

## 2. USAGE

1. Copy or export the material into this folder. Markdown, plain text, PDF and images all work.
2. Name the file in your request, for example:

```text
Use context/launch-brief.md as the source for this task.
```

3. Remove files once you no longer need them. Nothing here is cleaned up for you.

---

## 3. STRUCTURE

```text
context/
├── README.md        this file
├── .gitkeep         keeps the empty folder in the repository
└── <your files>     your reference material
```

| Path | Tracked by git | Purpose |
| --- | --- | --- |
| `README.md` | ✅ Yes | Explains what the folder is for |
| `.gitkeep` | ✅ Yes | Keeps the empty folder in the repository |
| Any other file or folder | ❌ No | Your reference material, kept on your machine |

---

## 4. VERIFICATION

Add a file, then run this from the system folder:

```bash
git status --short context/
```

Expected output: nothing. A file listed there would be committed, so check the system's `.gitignore` before you commit.

---

## 5. RELATED RESOURCES

| Resource | What it is |
| --- | --- |
| [`../README.md`](../README.md) | The Product Owner system's own README |
| [`../specs/personal/README.md`](../specs/personal/README.md) | Your private spec track for planning your own changes to this system |
| [Skilled](https://github.com/MichelKerkmeester/skilled-agent-harness_spec-driven-loops) | The spec-driven agent framework these systems are built and maintained with: spec folders, memory, skills and agents |
