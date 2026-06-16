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

If a file is missing when you start work, create it from the templates folder.

---

## Workbench rule (always on)

After any session that modifies files or makes a real decision, append a new entry to the top of `WORKBENCH.md`. Use the format in `templates/session-summary.md`.

Rules:
- Newest entries at the top. Append only. Never edit or delete past entries.
- 100-300 words per entry.
- Tag every decision `[DECISION]` and include the reasoning.
- Do not paste code diffs. Git handles that.
- If no decisions were made, write "None" under Decisions.

You do this without being asked. It is part of finishing the work.

---

## Architecture rule

When the tech stack, data flow, deployment target, or a key file's role changes, update `ARCHITECTURE.md` in the same session. Never leave the doc stale.

If you don't know what changed, ask the user one direct question before assuming.

---

## User Guide rule

When you add, change, or remove anything a user touches (a setting, a command, a screen, a behavior), update `USER_GUIDE.md` in the same session. Write it in plain language for someone who didn't build this.

---

## TODOs rule

Maintain a simple `TODOS.md` at the project root.
- One line per item, leading verb.
- Group under `## Next`, `## Soon`, `## Someday`.
- Strike completed items with `~~text~~` before deleting at session end.
- No tickets, no priorities, no dates unless a real deadline exists.

If a task is genuinely small (under 30 min) and obvious, just do it. Don't add a TODO for the sake of having a list.

---

## Session handoff

When the user says "wrap up," "let's wrap," "/wrap," "summarize," or you notice the conversation has grown long with substantial work done:

1. Write the workbench entry.
2. Update ARCHITECTURE.md and USER_GUIDE.md if anything changed.
3. Refresh TODOS.md.
4. Write a one-paragraph handoff at the top of the workbench entry titled "Next session, start here:" with three bullets: what to read first, what's in flight, the single next move.

That handoff is what makes the next session start warm.

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
