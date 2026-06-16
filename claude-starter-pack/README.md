# Build Room — Claude Starter Pack

A portable set of rules and templates that make Claude (Code, Desktop, or Chat) document your project as you build, without you having to think about it.

Drop these into your Claude setup once. From then on, every working session leaves behind: a workbench entry of what just happened, a current architecture doc, a user guide written for the next reader, and an honest TODO list.

You stop losing context between sessions. The next session (yours or someone else's) starts warm.

## What's inside

- `CLAUDE.md` — the rules. This is what Claude actually reads.
- `templates/session-summary.md` — workbench entry format.
- `templates/ARCHITECTURE.md` — skeleton for your project's tech doc.
- `templates/USER_GUIDE.md` — skeleton for the doc your future user reads.
- `templates/TODOS.md` — simple unbloated TODO format.

## 60-second install

Pick one of two paths:

**Path A: Global (every project on your machine).**
1. Open `~/.claude/CLAUDE.md`. Create it if it doesn't exist.
2. Paste the contents of `CLAUDE.md` from this pack into it.
3. Done. Every new Claude session on your machine now follows these rules.

**Path B: One project only.**
1. Drop `CLAUDE.md` in the root of your project folder.
2. Drop the `templates/` folder next to it.
3. Open Claude in that folder. Done.

Either works. Most people start with Path B on one project, then graduate to Path A once the rhythm feels right.

## What you'll see after one session

The first time you finish a working session under these rules, Claude will:

1. Write a 100-300 word entry to `WORKBENCH.md` in your project.
2. Update `ARCHITECTURE.md` if anything in the stack changed.
3. Update `USER_GUIDE.md` if anything a user touches changed.
4. Refresh `TODOS.md`.

Open those files. Read what got written. That's the artifact you'll thank yourself for next week.

## Why each rule exists

- **Workbench** captures decisions and reasoning that `git log` doesn't.
- **ARCHITECTURE.md** stops you re-explaining your own stack to Claude every session.
- **USER_GUIDE.md** keeps you honest about what the thing actually does for the person using it.
- **TODOs** stop you from carrying unfinished work in your head.

Together they close the loop: Claude builds, Claude documents, you trust the docs, next session starts faster.

---

Alex Salinsky · The Build Room
