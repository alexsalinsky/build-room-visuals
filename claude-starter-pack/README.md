# Build Room — Claude Starter Pack

One file. Drop it into your Claude setup once. From then on, every working session leaves behind: a workbench entry of what just happened, a current architecture doc, a user guide for the next reader, and an honest TODO list.

You stop losing context between sessions. The next session (yours or someone else's) starts warm.

## What's inside

**`CLAUDE.md`** — the rule pack. Templates for all four documents are embedded inline so this is the only file you need to install.

That's it. One file.

## 60-second install

Pick one of two paths:

**Path A: Global (every project on your machine).**
1. Open `~/.claude/CLAUDE.md`. Create it if it doesn't exist.
2. Paste the contents of `CLAUDE.md` from this pack into it.
3. Done. Every new Claude session on your machine now follows these rules.

**Path B: One project only.**
1. Drop `CLAUDE.md` in the root of your project folder.
2. Open Claude in that folder. Done.

Either works. Most people start with Path B on one project, then graduate to Path A once the rhythm feels right.

## What you'll see after one session

The first time you finish a working session under these rules, Claude will:

1. Write a 100-300 word entry to `WORKBENCH.md` in your project.
2. Create or update `ARCHITECTURE.md` if anything in the stack changed.
3. Create or update `USER_GUIDE.md` if anything a user touches changed.
4. Refresh `TODOS.md`.

Open those files. Read what got written. That's the artifact you'll thank yourself for next week.

## Why each rule exists

- **Workbench** captures decisions and reasoning that `git log` doesn't.
- **ARCHITECTURE.md** stops you re-explaining your own stack to Claude every session.
- **USER_GUIDE.md** keeps you honest about what the thing actually does for the person using it.
- **TODOs** stop you from carrying unfinished work in your head.

Together they close the loop: Claude builds, Claude documents, you trust the docs, the next session starts faster.

---

Alex Salinsky · The Build Room
