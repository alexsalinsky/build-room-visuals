# build-room-visuals workbench

## 2026-07-01 -- [Tool: Claude Code]

**Focus:** session-opener.html cleanup — removed the three redundant "Learn AI / Build Robots / Stay Human" pill boxes on slide 1 (duplicated the big headline verbatim) and their orphaned `.three` + `.pill` CSS. Committed + pushed to main.

## 2026-07-01 -- [Tool: Claude Code]

**Focus:** Ship IG carousel announcing upcoming Build Room events (Jul-Nov 2026) for @the.build.room.

**What happened:**
- Built `ig/2026-07-01-upcoming-events-carousel.html`: 9 slides, 1080x1350, brand palette (sand + forest with sage/tangerine/grape/blueberry accents per event type), print-friendly, html-to-image export button.
- Slides: Intro / Jul 15 Kickoff Session / Late July Cohort / Oct 12-16 PDC Retreat / Oct 22-25 DCBKK on-the-ground / Nov 9-13 CMSEO on-the-ground / Nov 14-18 Chiang Mai Retreat / CTA / Thesis close (verbatim).
- Wrote paired caption + hashtag block at `ig/2026-07-01-upcoming-events-caption.md`. Alex voice: short sentences, fragments, direct 2nd person, no em dashes, no "drop a comment" prompts.
- Verified dates from `INDEX.md`, `marketing-sprint-v1.md`, `DECISIONS.md`, `jess-pack`. Dropped NC17, London, DCMex from the deck (not Build Room products or not yet public).

**Decisions:**
- [DECISION] Treated DCBKK and CMSEO as "on the ground" not "speaking" -- speaker slots are pitched, not confirmed, per source docs. Avoids overclaiming.
- [DECISION] Kept the two Chiang Mai retreat concepts as ONE event (Nov 14-18) per marketing-sprint-v1 section 5 + DECISIONS 2026-06-28. Older Nov 16-20 date in memory is stale.
- [DECISION] Skool URL used as CTA anchor on Slide 8 since no confirmed public Luma URL for Jul 15 was in sources; caption notes Alex to update link-in-bio to Kickoff RSVP.

**Next up:** Alex uploads to @the.build.room; swap link-in-bio to Kickoff RSVP once URL locked.

---

## 2026-06-30 -- [Tool: Claude Code]

**Focus:** Rewrite `minimum-tech-stack.html` to match the standing "simpler builder pre-work" rule: two branches, no comparison table.

**What happened:**
- Replaced the old ChatGPT-Plus-vs-Claude-Pro comparison page with a two-branch decision: (A) if you already use an AI coding tool, use it; (B) if not, install Codex.
- On-page title changed to "Pick Your AI Coding Tool"; filename kept as `minimum-tech-stack.html` to preserve existing Skool and hub links.
- Branch B includes verified install commands from `github.com/openai/codex` for Mac/Linux and Windows PowerShell, plus `brew install --cask codex` fallback.
- Both branches converge on `bot-setup-standards.html` as the shared next step.
- Preserved brand style (mono footer, black chip header, card treatment, mobile-first).

**Decisions:**
- [DECISION] Kept filename `minimum-tech-stack.html`. Retitling on-page only avoids breaking existing Skool posts, hub pages, and share links that already point to this URL.

---

## 2026-06-30 -- [Tool: Claude Code]

**Focus:** Tiny follow-up to `ab08452` — surface date_captured as a labeled column in the Proof Library table view.

**What happened:**
- Renamed the existing table header for `date_captured` from "Captured" to "Date added" in `proof-library.html`. Column, sort handler, arrow indicator, and row value were already wired from the prior commit; only the label was off.
- Card view untouched.

**Decisions:**
- [DECISION] Rename in place rather than adding a new column — `date_captured` was already the sortable column, just labeled ambiguously. Matches the card view's "Added: " prefix and the sort-select's "Date added" wording.

---

## 2026-06-29 -- [Tool: Claude Code]

**Focus:** Add a beginner-friendly, copy-paste workspace bootstrap to the LLM Builder Best Practices file + page, anchored on a new top-level `WORKSPACE.md` router concept.

**What happened:**
- Extended `llm-builder-bps/llm-builder-bps.md` with three new sections: Install behavior now triggers a workspace bootstrap, Workspace Navigation rule (read root `WORKSPACE.md` first every session), First-time workspace setup spec (now creates 4 files: `.gitignore`, `.env`, `.env.example`, `WORKSPACE.md`).
- "When in doubt" rule re-routed to start at root `WORKSPACE.md`.
- Iterated `llm-builder-bps.html`: added section + styled table, swapped between "auto-runs on install" framing and "self-contained copy-paste prompt" framing twice based on feedback.
- Final HTML ships a single fat dark prompt-box with copy button bundling install + bootstrap + WORKSPACE.md skeleton + four-doc rules + workbench format + honesty + comms + wrap rules.
- Three commits to alexsalinsky/build-room-visuals main: `2eb6883`, `8871d37`, `c9fc080`. All pushed.

**Decisions:**
- [DECISION] Named the router `WORKSPACE.md` (tool-agnostic) instead of `CLAUDE.md` (Claude-only) so the BP file stays portable across Cursor/ChatGPT/Codex/Claude Code.
- [DECISION] Kept the copy-paste prompt on the HTML page (reversed earlier "fold into install" decision) after Alex confirmed copy-paste is the more useful UX for cohort newcomers.
- [DECISION] Bootstrap creates 4 files at root, not 3 — added `WORKSPACE.md` so any future LLM session has a single entry point to find the right project.

**Still open:**
- WORKSPACE.md concept is not yet tested with a real new cohort member. Worth grilling on first user.
- Build Room landing/index may want a link to the new BP page if not already linked.

**Key files:** `llm-builder-bps/llm-builder-bps.md`, `llm-builder-bps.html`

---

## 2026-06-25 - F&F Thu hub fixes before S1 kickoff

Pre-S1 audit-driven pass on `facilitator/ff-hub.html`. Same hub serves Mon + Thu cohorts; Thu S1 starts 15:00 COT today and hub was pointing builders at Mon ledger.

**What changed:**
- Two ledger cards now (Mon `1dzAa...` + Thu `1r5JG...`), labeled per cohort. Same split in S1 pills and Standing protocols.
- Live tools: added Build Room: Next Move paste-prompt, Meet Your Project paste-prompt, Credentials Hygiene deck, LLM Builder Best Practices.
- Header: Mon line (09:00 COT Zoom) + Thu line (Thu Jun 25, 15:00 COT, Lotus Rooftop, Medellín) above the glance grid.
- S1: backward-design frame box (Dream → Prototype → Demo, reverse-design S4→S3→S2→S1).
- Standing protocols: pay-tab reminder (Thierry $50, Jess 100K COP, Trello 6a3ae3647411e7d5f2aa537a), `/build-room-debrief` skill reminder, Justin Gary guest flag.
- Stripped all em dashes (15 instances → 0).

**Decisions:** none new, fixes against prior decisions.

**Files touched:** facilitator/ff-hub.html, WORKBENCH.md

---

## 2026-06-24 - LLM Builder BPs page: add "What is this?" before install

Follow-up pass on `llm-builder-bps.html`. Previous rewrite cut the "what / why" framing in the push to make the install path crystal clear. People landed on the page learning HOW to install without knowing WHAT they were installing.

**What changed:**
- Added new "What is this?" section ABOVE the install steps. One-sentence definition (standing rules for LLM-driven build sessions: file structure, doc discipline, decision logging, wrap rituals). 2-line "why it matters" (builds get messy, stacks drift, next Monday your AI has no context).
- Moved the four-doc preview up from "What's inside the file" (after install) to the new "What is this?" block (before install). Same content, better placement.
- Install steps still ONE path, button still prominent.

**Decisions:**
- [DECISION] Placed What/Why BEFORE install steps, not after. Install is the action; context is the prerequisite for taking that action.

**Files touched:** llm-builder-bps.html, WORKBENCH.md

---

## 2026-06-24 - LLM Builder BPs page rewrite: one path + skill-style MD

Rewrote `llm-builder-bps.html` and `llm-builder-bps/llm-builder-bps.md` so the resource has ONE clear use path and the MD teaches the LLM to apply the practices automatically (like Alex's `wrap` skill).

**What changed:**
- Killed Path A / Path B / Codex paths entirely. Replaced with single 3-step path: download MD, drop into LLM, tell it to install.
- HTML now leads with "How to use it" steps + prominent download button. Preview of the four-doc system stays as "what you're installing." Why-it-works kept.
- MD now opens with an "Install" block addressed to the assistant ("Best Practices installed. Active for every session."), then a "When to apply" trigger list (any build work, file modifications, decisions, wrap phrases), then a "How to stay applied" memory hint for context compression.
- Updated card description on `build-room-resources.html` + `index.html` to match the new "drop into your LLM and tell it to install" framing.

**Decisions:**
- [DECISION] Removed Path A/B/Codex entirely instead of light-editing. Alex was explicit: one path only, no "you could also" options. Optionality was the problem.
- [DECISION] MD opens addressed to the assistant, not the human. Matches the wrap-skill pattern Alex referenced. Human reads the HTML; the MD talks to the LLM.

**Still open:**
- None. Ship-ready.

**Files touched:** llm-builder-bps.html, llm-builder-bps/llm-builder-bps.md, build-room-resources.html, index.html, WORKBENCH.md

---

## 2026-06-23 - Credentials hygiene deck v2: fix tokens 404 + file-structure reframe

V2 pass on `credentials-hygiene-deck.html`. Real bugs on the live deck plus a content reframe.

Formatting bugs found and fixed:
- **Root cause of every "looks broken" symptom**: `_template/tokens.css` 404'd on GitHub Pages because Jekyll ignores underscore-prefixed dirs by default. Every `var(--br-*)` resolved to empty, so h1 fell back to 16px, `.floor` dark pill rendered transparent, etc. Inlined the tokens directly into the deck (matches the template's stated "portable if served outside the repo" intent).
- Em dash in `<title>` swapped for middle dot.
- Worked-example scene was overflowing the viewport (h2 colliding with section chip, bottom of `src/main.py` block cut off). Compacted code-block font and added explicit `margin-top` to clear the chip.
- Slide-wrap top padding bumped from 20px to 40px so chip + heading have breathing room across all 9 slides.

Reframe (the load-bearing ask): credential hygiene is a file-structure story. Built a reusable `tree()` function that renders the same project tree across multiple scenes with mode-based highlighting: yellow highlight on `.env` in "The Pattern", yellow on `.gitignore` in "Hide it from GitHub", strikethrough + dim on `.env` in "What git sees", **red danger background + 'PUSHED TO GITHUB' note on `.env` in the leak scene**, clean ok-green annotations in the close. Tree uses real monospace branch chars (├── │ └──), distinguishable from prose.

Also added a new scene 4: side-by-side `git status` before/after, with red `.env` showing as untracked on the "without" side and green `.gitignore` showing as untracked on the "with" side. The dimmed-out tree sits below to reinforce.

[DECISION] Deck went from 8 → 9 scenes (added the git-status before/after). Static reference page untouched per scope.

Verified all 9 scenes locally before pushing. Commit `e133cd2`. Live URL same: https://alexsalinsky.github.io/build-room-visuals/credentials-hygiene-deck.html.

## 2026-06-23 - Credentials hygiene: ported static page to teach-from deck

Shipped `credentials-hygiene-deck.html` as a Build Room style 8-scene click-through deck mirroring the static `credentials-hygiene.html` content. Scenes: title + floor rule, the .env pattern, .gitignore (order matters), edit-it-yourself (why keys leak into transcripts), Do/Don't grid, leak rotation (with the 3 provider links and rotation order warn box), worked example (3 files at root + Python loader), close. Used the standard deck scaffold (tokens.css, glassy floating HUD, swipe + arrow + click nav, 96px bottom padding on slide-wrap). No black-box treatment, no em dashes, no audience-participation prompts. Footer middle dot. Thesis line omitted (didn't land naturally in a setup deck).

[DECISION] Kept BOTH the static page and the deck. Static = reference (link from Skool, read once). Deck = teach-from for cohort sessions. Updated `index.html` and `build-room-resources.html` to show two cards: "(Deck)" and "(Reference)". Alex can flip to deck-only if he prefers later.

Wired into resource library (`index.html` + `build-room-resources.html`), live at https://alexsalinsky.github.io/build-room-visuals/credentials-hygiene-deck.html after push.

## 2026-06-22 - Scrub black-box treatment from F&F Mon kickoff deck

Applied the no-black-box rule to `facilitator/ff-mon-kickoff.html`. Slide 8 (Agreements) had three `background:#1a1a1a` cards holding real content (Presence, Teamwork, Positive Possibility). Rewrote to the standard light-airy bordered card pattern from `_template/components.html` (white background, 2px black border, dark heading, gray body). Content preserved verbatim. Slide 12 inspected: no black-box container present, just an agenda list and a "Let's go." punchline. No change needed there. Committed and pushed to origin/main for GitHub Pages.

[DECISION] Kept slide 12 untouched. The forever-rule diagnostic flags filler dressed up by dramatic containers; slide 12 has neither a container nor filler.
