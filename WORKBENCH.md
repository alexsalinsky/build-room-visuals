# build-room-visuals workbench

## 2026-07-23 -- [Tool: Claude Code] (Build Vault: Ruben removed, consent mechanism, published internal)

**Focus:** Alex reviewed the Build Vault prototype, pulled Ruben's card, and asked to publish.

**What happened:**
- Removed Ruben's Debt Payoff App card and the now-empty single-file-app filter chip from `build-vault.html`. Alex confirmed he's sensitive about sharing it.
- Design doc gained a do-not-share mechanism proposal: optional top-level `do_not_share` (enforcement flag, excludes entry from Vault at every tier and from content/outreach) + `consent_note` (plain-language record of what the builder said and when). Schema change still pends the normal mutation order.
- Published the Vault to the token-gated EC2 plan server: added `/build-vault.html` to SERVE_ROUTES in `scripts/build-room-plan-refresh.js`, scp'd script + page, pm2 restart. Verified 401 without token, 200 with. Live at https://13-218-176-29.sslip.io/plan/build-vault.html
- Draft banner now reads INTERNAL / Build Room members only. Page remains uncommitted in the build-room-visuals repo so it can't reach public GitHub Pages.
- Cockpit review item #2 (Alex's owed review) resolved.

**Decisions:**
- [DECISION] Internal hosting question resolved by publish: EC2 token-gated plan server, per design doc recommendation.
- [DECISION] Ruben's entries get do-not-share treatment across all tiers, not just the public one.

**Still open:** cut S4 demo clips (first batch: the 4 live cards), test the 4 starter prompts in a real agent, journey placement, Mon-track batch 2, schema fields not yet applied to proof-library-schema.md/JSON.

**Key files:** build-vault.html, scripts/build-room-plan-refresh.js, docs/superpowers/specs/2026-07-22-build-vault-design.md

---

## 2026-07-22 -- [Tool: Claude Code] (Build Vault: design doc + prototype)

**Focus:** Designed and prototyped "The Build Vault", a browsable showcase answering a new builder's "what could I build?" Origin: Bernice 1:1 (2026-07-22, 20:12-21:02); her ask was a card that "takes it into the agent that you use", so every card carries a copy-paste starter prompt.

**What happened:**
- Design doc + proposed schema extension: `docs/superpowers/specs/2026-07-22-build-vault-design.md`. Adds ONE optional `vault` object per proof-library entry (project_name, what_it_is, how_it_was_built, build_pattern, how_to_think, starter_prompt, demo_url, tier). Schema change not yet applied; awaits Alex review.
- Prototype `build-vault.html` (local, NOT committed): 5 real S4 cards (Ruben, Anthony, Dominika, Cece, Sarah), pattern filter, modal with WHAT/HOW/THINK layers + starter prompt with copy button. Browser-verified via Playwright.
- Only real video embed is Cece's cleared S1 Drive clip; other cards link to Fathom at verified demo timestamps because no S4 recordings exist locally and no S4 clips are cut.

**Decisions:**
- [DECISION] Vault is a derived view of proof-library.json via a `vault` extension field, not a second database. Keeps single-inventory rule and one write path (debrief skill).
- [DECISION] Two tiers: internal (recommend EC2 token-gated; Pages is public) and public (cleared-for-public status only). Prototype stays uncommitted until Alex clears hosting + consent.

**Still open:** 6 decision points in the design doc: internal hosting, clip cutting order, Ruben consent (his S1 confidentiality request), starter-prompt testing (drafted, NOT machine-tested), journey placement, Mon-track coverage.

**Key files:** build-vault.html (uncommitted), docs/superpowers/specs/2026-07-22-build-vault-design.md

---

## 2026-07-15 13:53 -- [Tool: Claude Code] (Restore LLM pricing section)

**Focus:** Alex asked where the LLM pricing/options content went; restored it onto minimum-tech-stack.html (8d3c866, live).

**What happened:**
- Traced the missing content: the pre-rewrite Minimum Tech Stack page (before de232bf) had "The Two Options" pricing cards; the two-branch rewrite dropped them.
- Restored as a "What it costs" section between the branches and the converge block: ChatGPT Plus card ($20/mo, includes Codex) and Claude Pro or Max card (Pro $20/mo, Max from $100, includes Claude Code), each with official pricing links, plus the "you only need one $20/month subscription" line.

**Decisions:**
- [DECISION] Restored on the same page (option 1) rather than a separate pricing page because the radical-simplicity direction favors one link for builders; Alex chose 1.
- [DECISION] Dropped the old GitHub add-on and $10/mo server mentions because new-builder pages now exclude GitHub/terminal/server complexity; Alex approved the result.

**Still open:** None.

**Key files:** minimum-tech-stack.html

---

## 2026-07-15 -- [Tool: Claude Code] (Simplify two resource pages)

**Focus:** Alex-directed simplification of two Build Room resource pages; pushed live (1dc907a).

**What happened:**
- `publish-online-free-cloudflare.html`: removed old step 3 (save token to shell env / .env) as redundant with the paste-into-robot prompt, which already carries the token. Now three steps: sign up, create token, paste prompt. Heading updated to "Three steps".
- `minimum-tech-stack.html` Branch B: replaced terminal install commands + GitHub link with a single line — download the Codex desktop app (links to openai.com/codex/get-started/, verified live), sign in with ChatGPT account. Added "You only need the $20/month ChatGPT plan to get started." Removed now-unused install-steps/codeblock CSS.

**Decisions:**
- [DECISION] Resource pages for new builders get the radical-simplicity bar: no terminal, no GitHub, no env-var steps. If a step duplicates what the robot prompt already does, cut the step. Memory updated (feedback_simpler_builder_pre_work).

## 2026-07-06 -- [Tool: Claude Code, worker] (Facilitator notes page)

**Focus:** Generic facilitator notes page for coaches (Jessica, Thierry), pushed live.

**What happened:**
- Created `facilitator/facilitator-notes.html` (aa52d6d): one-screen page built on Alex's three rules. 1) Ledger time is for the next step, not troubleshooting. 2) Troubleshooting is 1:1 or small group in the build hour, at facilitator discretion. 3) Prompt builders to articulate demo, prototype, WHY and HOW. Added a 60-90 sec ledger exchange script (where / next step / lock it / move on), four coaching questions (Demo, Prototype, Why, How), and a short build-hour section (rotate 1:1s, park rabbit holes, protect momentum). Reused ff-hub CSS so it feels native. Footer verbatim, no em dashes, no thesis line needed.
- Added a link card to `facilitator/ff-hub.html` in the "Open every session with this" grid, next to Session Opener and Drafting Table.
- Pushed to origin; live at https://alexsalinsky.github.io/build-room-visuals/facilitator/facilitator-notes.html

**Decisions:**
- [DECISION] Kept content strictly to elaborations of the three rules; no new policy invented. The "if a builder can answer all four crisply they're on track" line is a reading of rule 3, not new doctrine.
- [DECISION] Placed the hub card in the every-session section (not Live tools) because it's a pre-session read, cohort-agnostic.

## 2026-07-06 -- [Tool: Claude Code, ff-mon-s3-agenda-slides] (F&F Mon S3 deck + hub update)

**Focus:** Ship the F&F Mon Session 3 (Become a Publisher) deck and update the facilitator hub S3 block.

**What happened:**
- Created `facilitator/ff-mon-s3.html` (23705bc): 10-slide deck with the 2-slide opener built in (thesis verbatim + agreements from session-opener.html), agenda, builder shares, Cloudflare publish walkthrough link, ledger review, 66-min build time, Demo Day close, send-off. Inlined tokens per the ff-mon-kickoff precedent; template nav + arrow keys + 50px swipe handlers; glassy HUD pill; footer "Alex Salinsky · The Build Room".
- Rewrote ff-hub.html S3 block to the new 5-block flow (arc-v2026-07-06), moved `s-now` to S3, corrected the date to Mon Jul 7, demoted old lesson pills to reference, linked the deck + agenda.
- Verification: script parses, nav handlers present, zero em dashes outside `<title>`, thesis + footer verbatim. Live browser click-through blocked (both browser MCPs locked), fell back to static checks.

**Decisions:**
- [DECISION] Static nav verification accepted over live browser test because Playwright MCP held a stale profile lock and chrome-devtools needs a pre-launched Chrome; the nav script is the proven template pattern unchanged plus standard swipe handlers.

**Still open:**
- Alex click-through of the live deck before Mon 9am (arrows + swipe on phone).

**Key files:** facilitator/ff-mon-s3.html, facilitator/ff-hub.html

---

## 2026-07-06 -- [Tool: Claude Code] (landing page final review + proof data hotfix)

**Focus:** Final whole-implementation review of the live landing page, hotfix what it found.

**What happened:**
- Final reviewer pass on live build-room.html: ship-worthy. Verified thesis verbatim, footer, Skool -3309 URL, 2-hour session copy, no webinar embed, XSS-safe rendering (createTextNode), rel=noopener on external links, status-allowlist filtering correct (raw/redacted never render).
- Hotfix shipped (4d463b5): two LinkedIn `published` entries in proof-library.json had internal note text in their `quote` fields, rendering on the live wall as if quoted from Alex. Quotes nulled (cards render title-only), note text preserved in `notes` fields.

**Decisions:**
- [DECISION] Null the leaked quote fields instead of writing replacement quotes, because fabricating public quotes attributed to Alex violates the no-fabrication rule; title-only cards are honest and the renderer already null-guards.

**Still open:**
- Proof-point hero card is the thesis clip (redundant with hero) until a raw `win` entry gets promoted to cleared-for-public
- Section numbering visibly skips 03 while testimonials rail is empty; self-corrects when a permissioned testimonial lands

**Key files:** proof-library.json

---

## 2026-07-04 -- [Tool: Claude Code] (build-room.html SHIPPED)

**Focus:** Close out the landing page: redesign, final copy, deploy live.

**What happened:**
- `build-room.html` redesigned after Alex rejected the first flat look; final direction is "workshop heat" (charcoal/amber/cream). Pushed to main, live at https://alexsalinsky.github.io/build-room-visuals/build-room.html.
- CONFIG filled in: Luma https://luma.com/rnmkpxoc + real Stripe payment link. No more placeholder fallbacks.

**Decisions:**
- [DECISION] Standalone page here in build-room-visuals (not Luma-only, not folded into the Build Day site): owned destination for all channels, evergreen after July 15.
- [DECISION] Stripe CTA = USD $350. Pricing copy: "The cohort is $450. Reserve your seat now and lock in the $350 Kickoff price."

**Still open for Alex before July 15:** promote raw proof entries to cleared-for-public so the proof rail fills out; Stage 11 testimonial form so the testimonials rail isn't empty.

Spec: brain/the-build-room/specs/2026-07-04-build-room-landing-page-design.md · Plan: my-work/plans/2026-07-04-build-room-landing-page.md

---

## 2026-07-04 -- [Tool: Claude Code] (Jul 10 + Jul 14 accent cards, LinkedIn scheduling)

**Focus:** Render the two missing accent cards plus the framed Wins Wall image, schedule the Jul 10 and Jul 14 LinkedIn posts via Late.

**What happened:**
- Built three exports per the visual-direction spec, rendered via `exports/render-2026-07-04-cards.js` (copied from events/render.js pattern, 2x scale): `2026-07-10-brand-card.png` (1200x1200, sky tint, giant Georgia "35"), `2026-07-14-countdown-card.png` (1200x1200, amber tint, Georgia "15", dark band with white luma chip), `2026-07-14-wins-wall-framed.png` (1200x1200, Wins Wall screenshot in ink-border paper frame). Source HTML next to each PNG.
- Wins Wall screenshot served locally (wins-wall.html fetches proof-library.json, blocked over file://), clipped to skip the page's own pill so the frame pill isn't duplicated.
- Scheduled two LinkedIn posts via Late API, captions verbatim: Jul 10 9:00am Bogota (post 6a49259fded834bc384fe04c, photo-33 + 35-card) and Jul 14 9:00am Bogota (post 6a4925a263e32c5fb851d636, photo-10 + countdown card + framed wall). Both verified via GET. Queue files logged and moved to scheduled/.

**Decisions:**
- [DECISION] Card sizes 1200x1200 (spec silent; square carries well as image 2+ on LinkedIn, task default).
- [DECISION] Fixed "Maho" to "Majo" in proof-library.json display text (9 spots, id slugs untouched, standing spelling correction), committed and pushed (064ea29) so the live wall matches the screenshot.

**Next up:** Kandice/Kate permission check before Jul 10 for the named-clip upgrade path.

---

## 2026-07-04 -- [Tool: Claude Code] (build-room.html landing page)

**Focus:** New static landing page `build-room.html`, the public front door for the July cohort launch.

**What happened:**
- Built in 3 commits (6a7873d scaffold, 062038b copy, e9c1b20 proof rendering). Sections: hero, proof-point, how-it-works, proof-wall, testimonials, vocabulary, who-pricing, final-cta. Design tokens reused from wins-wall.html exactly (system stack, #fafafa/#1a1a1a, 2px-border cards, cohort tints).
- 4-value CONFIG block at top of head (kickoff date, Luma URL, Stripe URL, cohort start) for per-launch edits.
- Proof sections render client-side from proof-library.json, filtered to PUBLIC_STATUSES only (6 entries today). Fetch failure hides all three proof sections; static sections stand alone. Zero qualifying testimonials hides that section entirely.
- Verified with Playwright at 1280 + 390: CTAs above the fold on mobile, Ruben raw entry absent, no console errors, fetch-abort path clean.

**Decisions:**
- [DECISION] STRIPE_URL is "PLACEHOLDER", so the reserve button falls back to Skool with "Join the community, seat reservation opens shortly". Same guard exists for Luma. No dead links regardless of config state.
- [DECISION] Price shows literal `[PRICE - Alex confirms at copy review]` pending Alex's call.
- [DECISION] Proof-point picks first featured win, else first featured (today: nc17-thesis-line clip).

**Next up:** Alex confirms price + Stripe payment link, edit CONFIG, push to GitHub Pages.

---

## 2026-07-04 -- [Tool: Claude Code] (events graphic + visual direction)

**Focus:** All-upcoming-events graphic (2 exports) + July visual direction doc.

**What happened:**
- Built `events/upcoming-events-ig.html` (1080x1350) and `events/upcoming-events-linkedin.html` (1200x627), rendered to PNG at 2x via `events/render.js` (local Playwright; MCP browser was locked). Look reused from wins-wall/proof-library: #fafafa paper, ink borders, pastel tints, Georgia serif accent.
- Events included: Jul 15 Kickoff (free, no time printed, luma.com/rnmkpxoc), Jul-Aug cohort, Sep 30 Boston AI Week (Build Hour + dinner), Oct 12-16 PDC retreat, Nov 16-20 Chiang Mai retreat. Learning Live Sep 16-17 as a dashed "on the road" strip.
- Wrote `brain/the-build-room/marketing/2026-07-04-visual-direction.md`: palette/type/image-treatment rules + upgraded per-post visual specs for all 10 July queue files (queue files themselves not edited).

**Decisions:**
- [DECISION] Excluded DCBKK (Oct 22-25) from the public graphic: members-only DC conference Alex attends for private retreat pre-sales, not a joinable Build Room event.
- [DECISION] Learning Live listed as "on the road" not hosted, since the speaker slot is unconfirmed.

**Next up:** Alex reviews both PNGs; if approved, schedule via content engine and apply the direction doc specs to the Jul 10/14 built cards.

---

## 2026-07-04 -- [Tool: Claude Code]

**Focus:** Claude Design integration + first IG thesis asset shipped via the HTML-to-screenshot pattern.

**What happened:**
- Connected the `claude-design` MCP server (user scope, auto-auth on CLI >= 2.1.201). Details in memory `reference_claude_design_mcp.md`.
- Ran /design-sync against this repo: NOT syncable as-is (static HTML, no compiled React components). No changes made by the sync.
- Built `social/ig-thesis-post.html` (1080x1350). First flat version got "doesn't look that cool"; produced 3 variants (amber flood / poster stack / stacked bands). Alex picked A: full amber-bg canvas, 190px black type, "Stay Human." in tilted black block, black chip header, footer with handle + four adoption-dot outlines. Promoted A to canonical, deleted B/C drafts.
- Rendering via `social/render.js` (local Playwright at 2x, same pattern as events/render.js).
- Proof-library lookup confirmed the thesis line is a featured entry (`nc17-thesis-line`), so it's honest to publish.

**Decisions:**
- [DECISION] Skipped building a React component library just to satisfy /design-sync -- Alex wants working assets, not a brand system. Revisit only if Claude Design proves sticky.
- [DECISION] Social assets pattern going forward: fixed-dimension HTML on tokens.css, node render.js to PNG at 2x. Repeatable without any design tooling.
- [DECISION] Alex's visual preference: bold/loud beats clean/minimal for IG. Amber-flood treatment won over quieter layouts.

**Next up:** Alex posts `social/ig-thesis-post.png` to @the.build.room.

---

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
