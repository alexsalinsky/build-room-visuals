# Project Operating Rules for Claude

These rules govern how you (Claude) work in this project. Follow them automatically. Do not wait to be asked.

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
## YYYY-MM-DD HH:MM — [tool: Claude Code / Desktop / Chat]

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
- 100-300 words per entry.
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
2. Update ARCHITECTURE.md and USER_GUIDE.md if anything changed.
3. Refresh TODOS.md.
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

Read `ARCHITECTURE.md`, then the top entry of `WORKBENCH.md`. If those don't answer it, ask one direct question.
