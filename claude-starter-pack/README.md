# Build Room — Claude Starter Pack

One file (`team-tech.md`). Save it, then add one line to your existing Claude or Codex config that points to it.

From then on, every working session leaves behind: a workbench entry of what just happened, a current architecture doc, a user guide for the next reader, and an honest TODO list.

You stop losing context between sessions. The next session (yours or someone else's) starts warm.

## What's inside

**`team-tech.md`** — the rule pack. All four document templates (workbench, ARCHITECTURE, USER_GUIDE, TODOS) are embedded inline so this is the only file you install.

## Why a separate file (not a CLAUDE.md)

If you already use Claude Code or Codex, you probably already have a `CLAUDE.md` or `AGENTS.md`. Overwriting it would nuke your existing rules. So this pack is a standalone file you point your config at with one line. Nothing of yours gets touched.

## 60-second install

Pick one of two paths.

### Path A — every project on your machine (Claude Code)

1. Download `team-tech.md` to `~/.claude/team-tech.md`.
2. Open `~/.claude/CLAUDE.md` (create it if it doesn't exist).
3. Add this line anywhere in the file:
   ```
   @~/.claude/team-tech.md
   ```
4. Done. Every Claude Code session on your machine now follows these rules in addition to whatever else is in your CLAUDE.md.

### Path B — one project (Claude Code)

1. Drop `team-tech.md` in the root of your project folder.
2. Open or create `CLAUDE.md` in the same folder.
3. Add this line:
   ```
   @team-tech.md
   ```
4. Done.

### Codex users

Codex reads `AGENTS.md` and doesn't have a formal import directive. Two options:

- **Easiest:** open `team-tech.md`, copy its contents, paste them into your `AGENTS.md` under a `## Team Tech Rules` heading.
- **Cleaner:** save `team-tech.md` next to `AGENTS.md`, then add a line at the top of AGENTS.md: `Also follow the rules in team-tech.md (in this folder).` Codex will pick it up when it reads the folder.

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
