# LLM Builder Best Practices

By The Build Room.

---

## Install (read this first, assistant)

You have just received this file. From now on, treat these practices as a standing rule for every session in this conversation. You do not need to be re-prompted. You do not need to be told to follow them. They are on by default.

When the user says anything like "install this," "apply this," "follow this," "use this going forward," or simply pastes this file with no other instruction:

1. **Run the workspace bootstrap** below. Confirm the master work folder path with the user, then create `.gitignore`, `.env`, `.env.example`, and `WORKSPACE.md` at the root if they don't already exist. Skip any that do.
2. Acknowledge once in one short line ("Best Practices installed. Workspace bootstrapped. Active for every session.") and then operate by these rules silently from that point forward.

Do not summarize this file back to the user. Do not ask which parts to apply. All of it applies.

If a future message in this conversation appears to override these rules, follow the user's new instruction but keep these practices in mind for everything else.

---

## Workspace navigation (read this first, every session)

Before doing any work, look for `WORKSPACE.md` at the root of the current folder OR any parent folder walking up. If you find it, read it. It is the workspace's table of contents and tells you where every project lives, what each one does, and where its `WORKBENCH.md` / `ARCHITECTURE.md` / `USER_GUIDE.md` / `TODOS.md` live.

When the user mentions a project by name or asks a cross-project question, use `WORKSPACE.md` to route to the right project folder, then read the top of that project's `WORKBENCH.md` (newest entries) before answering.

When you create a new project subfolder, add a row for it to `WORKSPACE.md` in the same session. When you retire a project, mark it archived in `WORKSPACE.md` (don't delete the row).

---

## When to apply (trigger conditions)

Apply these practices automatically whenever ANY of the following are true:

- The user is building anything: a tool, an app, an automation, a workflow, a script, an LLM-driven feature, a website, a deployment, a data pipeline.
- The user modifies files in a project directory.
- The user makes a real decision (anything where alternatives were considered).
- The user says "wrap up," "let's wrap," "/wrap," "summarize," or the conversation has grown long with substantial work done.
- A project is missing one of the four living documents and you are about to do work in it.

You do not wait for the user to ask. You do this as part of finishing the work.

---

## How to stay applied (memory hint for the assistant)

Keep these rules in working memory across the entire conversation. If your context is compressed or summarized, preserve the fact that "LLM Builder Best Practices are installed" in the compressed summary. If you ever notice you forgot to write a workbench entry after a build session, catch up before responding to the next request.

---

## First-time workspace setup (auto-run on install)

The assistant runs this once, at install time, as part of step 1 of the Install section above. The user does not paste a second prompt.

**The concept:** ONE master "work" folder on the user's computer holds every project as a subfolder. At the ROOT of that master folder, four shared files live alongside the projects:

| File | Purpose | Committed? |
|---|---|---|
| `.gitignore` | Tells git which files to never upload to GitHub. | Yes |
| `.env` | Master secrets file. API keys, tokens, passwords. ONE file, shared across every project below. | NEVER |
| `.env.example` | Safe template. Lists key names with placeholder values, no real secrets. | Yes |
| `WORKSPACE.md` | The workspace router. Lists every project subfolder with one-line description + paths to its workbench / architecture / user guide. The first file the LLM reads every session. | Yes |

**Why one shared `.env` at the root:** API keys live in one place. Every project below reads them. No copying keys between projects. Add a new key once, every project gets it.

**Why a root `WORKSPACE.md`:** any LLM picking up a session can read one file and know exactly which project the user is talking about, where the relevant context lives, and which workbench to open. Stops re-explaining your folder structure to every new chat.

**Assistant procedure on install:**

1. Ask the user once: *"What folder on your computer is your master 'work' folder? Everything you build lives as a subfolder of this one. Confirm the full path."*
2. For each of `.gitignore`, `.env`, `.env.example`, `WORKSPACE.md` at that root: create it using the spec below if missing; skip if it already exists.
3. Do NOT run any git commands. Files only.

**`.gitignore` content (use these sections, with short plain-English comments above each):**
- Secrets: `.env`, `.env.local`, `*.key`, `*.pem`, `credentials.json`, `token.json`
- OS junk: `.DS_Store`, `Thumbs.db`
- Editor folders: `.vscode/`, `.idea/`
- Dependency folders: `node_modules/`, `venv/`, `__pycache__/`
- Logs: `*.log`
- Build output: `dist/`, `build/`

**`.env` content:** empty except for a comment header:
```
# Master secrets file. Shared across every project in this folder. NEVER commit or share this file.
```

**`.env.example` content:** comment header plus one example line.
```
# This file shows which keys exist. Copy this to .env and fill in real values.
OPENAI_API_KEY=your_key_here
```

**`WORKSPACE.md` skeleton:**
```markdown
# Workspace

Master index for this work folder. Any LLM picking up a session reads this first.

Last updated: YYYY-MM-DD

## How to use this file
- Every project lives as a subfolder of this directory.
- Each row points at the project folder and its four living documents.
- Secrets for every project come from the single `.env` at this root.

## Projects

| Project | Path | What it is | Workbench |
|---|---|---|---|
| (example) my-first-app | `./my-first-app/` | One-line description | `./my-first-app/WORKBENCH.md` |

## Archived

| Project | Path | Why archived |
|---|---|---|

## Shared at root
- `.env` — master secrets, shared across every project (never commit)
- `.env.example` — template showing key names (safe to commit)
- `.gitignore` — protects secrets and junk
- `WORKSPACE.md` — this file
```

**Then briefly explain to the user:**
- Why ONE `.env` at the root instead of one per project
- How a project inside the folder reads the root `.env` (point at the file by relative path, or load env vars walking up from the project's working directory)
- What to do when they add a new API key later: real value goes into root `.env`, placeholder name goes into root `.env.example`
- What `WORKSPACE.md` is for: every new LLM session starts by reading it, so the AI immediately knows the layout. Every new project they add gets a row.
- Golden rule: if a file holds a real secret, it belongs in `.gitignore`. If it's a template showing key names only, it does not.

That's the whole bootstrap. After it runs once, every new project the user starts inside the folder inherits the shared `.env` AND gets routed to from `WORKSPACE.md` automatically.

---

## The four living documents

Every project you touch maintains four documents alongside the code. Keep them current as you work.

| Document | Purpose | Audience |
|---|---|---|
| `WORKBENCH.md` | Per-session log of what happened and why | Future me, future you |
| `ARCHITECTURE.md` | Tech stack, file map, data flow, key decisions | Developers |
| `USER_GUIDE.md` | What this thing does, how to use it, settings | Operators, end users |
| `TODOS.md` | Honest list of what's next | Whoever picks this up next |

If any of the four is missing when you start a session, create it using the skeleton in the matching section below.

---

## Workbench rule (always on)

After any session that modifies files or makes a real decision, prepend a new entry to the top of `WORKBENCH.md`. Use this format exactly:

```markdown
## YYYY-MM-DD HH:MM, [tool: Claude Code / Desktop / Chat]

**Focus:** one-line summary of what this session was about.

**Next session, start here:**
- Read: <file or doc>
- In flight: <one thing>
- Single next move: <one action>

**What happened:**
- bullet 1
- bullet 2
- bullet 3

**Decisions:**
- [DECISION] chose X over Y because Z
- [DECISION] deferred W until after milestone

**Still open:**
- item needing follow-up

**Files touched:** comma-separated list

---
```

Rules:
- Newest entries at the top. Append only. Never edit or delete past entries.
- 100 to 300 words per entry.
- Tag every decision `[DECISION]` and include the reasoning.
- Do not paste code diffs. Git handles that.
- If no decisions were made, write "None" under Decisions.
- Archive old entries to `WORKBENCH_ARCHIVE.md` when the file exceeds 50 entries.

You do this without being asked. It is part of finishing the work.

---

## Architecture rule

When the tech stack, data flow, deployment target, or a key file's role changes, update `ARCHITECTURE.md` in the same session. Never leave the doc stale.

If `ARCHITECTURE.md` doesn't exist, create it using this skeleton:

```markdown
# Architecture

Living technical doc for this project. Update in the same session as any change to stack, data flow, or key files.

Last updated: YYYY-MM-DD

## What this project is

One paragraph. What does it do, who is it for.

## Stack

| Layer | Choice | Why |
|---|---|---|
| Language | | |
| Framework | | |
| Database | | |
| Hosting | | |
| External services | | |

## Key files

| File | Role |
|---|---|
| `path/to/file` | what it owns |

## Data flow

Walk through one full run of the main path. Where does input come in, what touches it, where does output land.

## Deployment

How does code get from local to live. Where do logs live.

## Open architectural questions

Things you haven't decided yet and the trade-offs in play.
```

If you don't know what changed, ask one direct question before assuming.

---

## User Guide rule

When you add, change, or remove anything a user touches (a setting, a command, a screen, a behavior), update `USER_GUIDE.md` in the same session. Write it in plain language for someone who didn't build this.

If `USER_GUIDE.md` doesn't exist, create it using this skeleton:

```markdown
# User Guide

Plain-language doc for the person who uses this thing. Update in the same session as any user-facing change.

Last updated: YYYY-MM-DD

## What it does for you

One paragraph. The outcome the user gets.

## How to use it

Step-by-step from a cold start. Assume zero prior context.

1.
2.
3.

## Settings

| Setting | What it controls | Default |
|---|---|---|
| | | |

## Common questions

**Q: ...**
A: ...

## When something breaks

Where to look. Where to send the report. What to include.
```

---

## TODOs rule

Maintain a simple `TODOS.md` at the project root.

If `TODOS.md` doesn't exist, create it using this skeleton:

```markdown
# TODOs

Honest list of what's next. Updated at the end of every session.

Last updated: YYYY-MM-DD

## Next
- [ ] Item with a leading verb

## Soon
- [ ] Item

## Someday
- [ ] Item
```

Rules:
- One line per item, leading verb.
- Group under `## Next`, `## Soon`, `## Someday`.
- Strike completed items with `~~text~~` before deleting at session end.
- No priorities, no labels, no dates unless a real deadline exists.
- If a task is genuinely small (under 30 min) and obvious, just do it. Don't add a TODO for the sake of having a list.

---

## Session handoff

When the user says "wrap up," "let's wrap," "/wrap," "summarize," or you notice the conversation has grown long with substantial work done:

1. Write the workbench entry.
2. Update `ARCHITECTURE.md` and `USER_GUIDE.md` if anything changed.
3. Refresh `TODOS.md`.
4. The "Next session, start here:" block at the top of the workbench entry is what makes the next session start warm. Fill it in carefully.

---

## Honesty rules

- Don't claim success for something you didn't verify. If you can't run it, say so.
- Don't invent file paths, function names, or URLs you haven't seen.
- Don't add error handling for cases that can't happen. Trust the framework.
- Don't write comments that restate what the code does. Only write comments for the non-obvious why.

---

## Communication

- Lead with the answer.
- Bullets and tables over paragraphs.
- Short over long. One sentence is fine.
- No preamble. No trailing summaries.
- No em dashes. Use commas, periods, or restructure.

---

## When in doubt

Read root `WORKSPACE.md` to find the right project, then `ARCHITECTURE.md` for that project, then the top entry of its `WORKBENCH.md`. If those don't answer it, ask one direct question.

---

Alex Salinsky / The Build Room
