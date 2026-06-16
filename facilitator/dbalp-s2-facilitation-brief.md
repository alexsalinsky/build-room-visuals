# DBALP S2 Facilitation Brief

> **For the live show-and-discuss in S2:** the scrollable companion to this brief is [s2-matrix.md](./s2-matrix.md) — one row per person, 8 columns (project / their words / the 4-step loop / win / principle / S4 taste / check-in line). Share-screen the matrix during stage 4 of the session arc. This long-form brief is Alex's prep doc; the matrix is what the team sees.



**For:** Alex, walking into S2 Tue Jun 16, 1pm Bogota
**Source:** S1 transcript verbatim (2026-06-09, 142 min), kickoff transcript, bryce-cohort-notes, ledger sheet.
**Format:** One page per person. Read what they said in their own words. The small win is something they can SEE at the end of S2's 25-min build block — not a doc, not architecture notes. The stepping stones show how S3 and S4 build from it. Only 3 sessions left.

---

## The principles this session is actually teaching

The S2 wins are not the point. The PRINCIPLES they surface are the point. Each person's small win is shaped to make them feel a specific principle in their own hands. Read each S2 win section as: "this is the principle we want them to walk away holding."

**The core loop (apply to every project):**
1. **You do it yourself first.** Pick the smallest meaningful slice. Curate it by hand. This is what shows the robot what "good" looks like.
2. **Ask the robot to do the same.** Don't tell it the answer; ask it to produce one.
3. **Score the difference.** What did it get right? What did it miss? Where was it confidently wrong?
4. **Refine through correction.** Tell it what you would have done differently. That's the teaching.
5. **Repeat until the gap is small.** Only THEN automate the input or delivery.

This is what makes the participant the expert and the robot the apprentice. Not the other way around. Every win below walks this loop.

**The other thing that must be true at the end of S2:** each person walks away with a TASTE of their final product. Not a description of it — a fragment they can hold up and say "that's a piece of what demo day looks like." The S2 win is shaped so the artifact itself is a primitive version of S4. They should be able to point at what they produced and feel the shape of where this is going.

**Per-person principles surfaced:**

| Person | Principle their S2 surfaces |
|---|---|
| Ice | Teach by curating, score, refine, THEN automate. Rubrics emerge from doing the work, not from naming columns in advance. |
| Marley | Model what "good" looks like before asking the AI to produce it. The expert sample is the prompt. |
| Chanel | Fix the source of truth before adding tools on top. AI diagnoses what's broken; you fix it where the data actually lives. |
| Auds | Shrink the problem. Three sources is overwhelming; one source done well is a win. Add the second next time. |
| Kate | Meet the platform where it is. MCP > API > connector if available. Easiest connection first, hardest data later. |
| Ehdina | Train on the voice of the actual expert. Bryce is in the room — his sign-off is the score. |
| Kandice | Start with understanding, not matching. The hard problem is teaching the AI to know a client; matching comes after that. |
| Bryce | Facilitation is leverage. When you can build alone, helping seven others build creates more value than another personal hack. |

When you debrief at the end of S2, ask each person to name the principle their work surfaced. They probably won't articulate it perfectly the first time. That's the point — they'll feel it before they can say it. By S4 demo day, they should be able to say it.

---

## How everyone walked out of S1

Last hour of S1 was eaten by Git + Homebrew + Claude Code installs + Monday API key plumbing. Almost nobody got to a second integration. Here's actual S1 end state per person:

| Person | Monday connected? | Got data back? | Notes |
|---|---|---|---|
| Marley | Yes (pre-session) | Yes | Was co-facilitating others; her win was already in hand |
| Kate | Yes (during session) | Yes, filter slightly off | "Person filter didn't work on all boards. Let me query items more broadly." |
| Chanel | Yes (late, with 1:1 help) | Yes, "info on all the client boards and stuff" | Required full Claude restart via Task Manager |
| Kandice | Yes (demo subject) | Yes, but answers not what she wanted | Volunteered to share screen + walked group through Windows install live |
| Ice | Yes (very late) | Yes | Had to install Git via Homebrew via Cowork-assisted terminal |
| Auds | Yes (at 4:17am PH time) | Yes, but data not assignee-accurate | Last to get unstuck. Working night shift. |
| Ehdina | In progress at session end | Unknown | Was on Windows; CoWork helping. May not have closed the loop. |
| Bryce | Already connected | Yes | Facilitator mode |
| Jenina | **Not named anywhere in S1 transcript** | n/a | Confirm with Bryce: in cohort? |

Alex's S1 close-out homework: connect Google Drive this week, play with the robot before going to Monday directly. Realistic expectation walking into S2: most people did NOT do the homework. Plan S2 against that.

---

## Bryce North — CEO

**What he said he wants from the cohort (kickoff):** team understands they can build small AI systems, understands what he's already built, gets in the habit of researching and optimizing instead of waiting to be told.

**What he said in S1:** Will be jumping between people to help. Listed his hopes for team builds: "Quick report generators... pull up the most recent sales call from this client... proposal generators." Sunday hacks Spanish accent app + Consuela lead scraper + Stripe finance dashboards + auto-response email tool. Wants team to learn chat/co-work/code difference + how to use Claude Design.

**The "never answer another sales email" line** lives only in his S1 ledger entry, not in anything he said publicly. Treat it as his personal Sunday hack.

**S2 small win:** Bryce's win is OTHER PEOPLE'S wins. Sit him next to whoever's most stuck mid-build block (probably Ehdina if her S1 plumbing didn't close, or Kandice if she's stalled on the client-folder read). If he wants a 5-min personal micro-build for himself: paste 5 sales emails into Claude, ask for 3 categories. Done.

**Stepping stones:**
- S3: Bryce co-leads one mini-lesson (which one of his Sunday hacks does the team want to see live? 10 min.)
- S4: His Pitchy reporter database is ready (he said "one week left to finish scraping" in S1 — that lands right around S3). Wire it into Kandice's project as the join. That's a demo-day-worthy moment.

**What to say at check-in:** "You bought time today by helping Ehdina close her S1 plumbing. The team needs you as a co-builder more than another tool from you. Hold."

---

## Marley — Director, Client Success

**Her exact words (S1):** *"I'll feel accomplished if I can come out of here having built something that streamlines a workflow that everyone has a touchpoint on. Streamline a workflow but also improve the output. Very likely the project will be automating and improving our reporting system. I want people to feel more comfortable and have more time to look at the actual high-level strategy as opposed to just gathering data."*

**More she said:** Two report types: clients who just want a published link, clients who want minutiae (subject lines, sequences, success rates). Her dream report is two-parted: **client-facing** (analytics, metrics) + **internal** ("here's what we tried, here are recommendations for next campaign"). Data lives in PRVault (analytics) + Monday (leads + statuses + published links) + Inbound Requests. Her current hack: she takes SCREENSHOTS of PRVault dashboards because the CSV downloads are "wildly incorrect." Bryce confirmed: PRVault won't ban screenshots. Alex suggested Playwright in Claude Code (so Claude does the screenshots itself, no screen takeover).

**Her real concern:** "Maybe just having an understanding of what good looks like. What are the metrics that we absolutely need to be reporting on and what's nice to have?" Translation: she doesn't have a clear definition yet. That's the work.

**S2 small win — walks the full loop:**
1. **Marley does it herself first.** Pick ONE real client, ONE recent month. Write the **opening paragraph** of the client-facing section by hand (or grab one she already wrote in a past report). This is the "good" sample. It's the prompt.
2. **Ask Claude to do the same.** Pull Monday data for that client + paste in a screenshot of PRVault for that month. Hand Claude the sample paragraph and say: "match this voice and structure. Draft the opening paragraph for THIS month using this data."
3. **Score the gap.** Read both side by side. Where did Claude land the tone? Where did it slip? Which numbers did it pull correctly?
4. **Refine.** One correction sentence to Claude. ("Don't lead with email opens; lead with placements.")
5. Park the internal "what we tried" half. That's S3.

**The pass/fail to celebrate:** Did Claude produce one sentence Marley would send to a client without editing? Just one. That sentence is proof "AI writing is good enough" — for one sentence.

**Principle this surfaces:** model what "good" looks like before asking the AI to produce it. The expert sample IS the prompt. Marley is the expert; her past report is the lesson plan.

**Taste of the final product:** the one client-ready sentence is the seed of the full monthly report at S4. She walks out with proof that a real sentence of a real client report came out of this loop. The rest of the report is more of the same loop, repeated.

**Stepping stones:**
- S3: Bryce shares Pitchy reports as inspo (he offered this in S1). Marley adds the **internal "what we tried"** half. Workbench captures Claude's misses.
- S4: Demo Day. She shows a full monthly report draft for one client + the workbench of edits = proof the system has been learning. Multiplying-level move.

**What to say at check-in:** "You said you'd feel accomplished if you streamlined something everyone touches. You just drafted the part of a client report you usually write from scratch. How much time was that?"

---

## Ayeshah (Ice) — Campaign Manager

**Her exact words (S1):** *"Whenever I talk to Bryce about what he does on Claude, it feels like there's just so many opportunities I haven't explored, both for personal and work life. I want to see how far I can push that automation to make admin tasks easier."*

**Then on her project specifically:** *"I'll get like maybe like 100 a day and only two of them end up being relevant. So it just ends up looking really messy and getting becoming really hard to understand. So it'd be really cool if there was a way to kind of get like a brief at the beginning of the day or beginning of the week or a notification every time there was something that was hyper relevant to a client."*

**On filter approach:** Alex coached her: don't worry about delivery format (email vs dashboard vs Monday) yet. First refine the filtering. Show Claude 10, "I like 7, wish 1 of these other 990 was in here." Iterate.

**Her vibe:** Humor + meta. "I'm just learning radical acceptance of the robots." Comfortable being uncomfortable. Already has Google Alerts running (says they don't work well enough).

**S2 small win — walks the full loop:**
1. **Ice does it herself first.** Pick a batch of ~10 real notifications from the last week. Pick her favorite 3 — the most relevant ones — by gut. No rubric yet. Just instinct. Write down WHY each made the cut in a sentence.
2. **Ask Claude to do the same.** Paste the same 10 notifications + a paragraph describing ONE client. Ask: "score these 10 from most to least relevant to this client. Pick your top 3. Explain why."
3. **Score the gap.** Did Claude's top 3 match Ice's top 3? Which one did it miss? Which one did it add?
4. **Refine.** Ice tells Claude what she'd have done differently. "You missed X because you weighted recency too high." That's her teaching it. That's the rubric being born — not invented in advance.
5. Park the delivery format. Schedule, email, dashboard — all S3+.

**The pass/fail to celebrate:** Did Ice articulate ONE rule by the end of the block that she didn't have at the start? ("Recency matters less than topic specificity" or similar.) THAT is the rubric being born.

**Principle this surfaces:** rubrics emerge from doing the work and correcting the AI, not from naming columns in advance. The S1 auditor pass said "write 5 named filter criteria as `media-monitor-architecture.md`." That's backwards — the criteria come AFTER scoring real outputs, not before.

**Taste of the final product:** the one rule Ice articulates at the end of S2 is the first line of the rubric that scores the daily brief at S4. She can point at it and say "that's the seed."

**Stepping stones:**
- S3: Connect to Google Alerts feed (or a news/social API) so input is automated, not pasted. Run on real day's batch.
- S4: Scheduled brief delivered somewhere (Slack? email? doesn't matter — pick easiest).

**What to say at check-in:** "You said your goal is to see how far you can push the automation. You just made Claude rank media items the way you would. That's not radical acceptance, that's you driving."

---

## Chanel — Campaign Manager

**Her exact words (S1):** *"I want to create a system in Monday that organizes my whole day for me, depending on what project is most pressing, what maybe I haven't touched in too long. If I have approvals, like what's important I need to do right now and like lay it out for my whole week."*

**Her tell, immediately after:** *"I already attempted to do this and I have a broken board and workflow that doesn't quite work."* She built it with Monday's AI. Items would populate when she was tagged but no comments, no client name, and completed tasks didn't drop off the list. She "didn't think of [things], it was more of an idea rather than like a real plan."

**Alex's S1 call:** STAY INSIDE MONDAY. Don't rebuild in Claude Code as a parallel dashboard — Monday is the source of truth, parallel system would drift. Use Claude Code to talk to Monday and (eventually) build a custom view or improve the broken board.

**Her hope:** *"Build a really robust dashboard and then be able to share it with other people... it would just be nice to have like, what's most important today? This is what you need to do. Do that in this amount of time. This is the list."* — note: she wants to **share it with the team** (multiplying-level intent).

**S2 small win — walks the full loop:**
1. **Chanel does it herself first.** Open her broken Monday board. Write down by hand on paper what she WANTS to see when she opens it (what columns, what order, what filters). 3-5 lines max. This is the spec. **She doesn't need to type it up.** Take a photo of the page and drop it into Claude — Claude reads handwriting.
2. **Ask Claude to do the same.** Have Claude read the board via the connector. Ask: "compare what's on this board to this spec. Tell me what's wrong and what's missing." Name herself explicitly in any prompts about her items ("tasks where Assignee is Chanel" — the shared API key won't infer "me").
3. **Score the gap.** Claude returns a list of issues. Chanel reads it and picks the ONE that bothers her most.
4. **Refine through correction.** Apply the fix to the board (Claude proposes, Chanel approves). It changes visibly in Monday.
5. Park the priority + minutes ranking. That's S3.

**The pass/fail to celebrate:** Did one specific thing on her real Monday board change visibly during the build block? She entered S2 with a broken board; she leaves with a less-broken board.

**Principle this surfaces:** fix the source of truth before adding tools on top. Don't build a new dashboard parallel to a broken Monday board — that creates drift. Have AI diagnose where the data lives, and fix it there.

**Taste of the final product:** the one fixed bug is a piece of the dashboard she said she wants to share with the team. She can point at the corrected behavior and say "that's how it's supposed to work for the whole team."

**Stepping stones:**
- S3: Add priority + due + minutes-to-complete ranking logic to the now-less-broken board.
- S4: Share the dashboard with one teammate (Auds or Kate would love it). Multiplying.

**What to say at check-in:** "You said the board didn't quite work. You just fixed something on it during a 25-minute build block. What else on that list do you want to fix this week?"

---

## Audrey (Auds) — PRC

**Her exact words (S1):** *"I do a combination of admin tasks and a lot of writing and research. My days usually fall and I have a hard time tracking everything. Right now what I do is I have to go through everything one by one in order to make sure that I don't miss something. I want to build a task tracker that's connected to everyone else's task tracker that will be updated automatically every time there's movement."*

**More detail:** *"My tasks personally, they live in Monday, Missive and on Slack. I want everything to be in one place. That way, whenever I log in, I just have to look at one board and then go through everything. And not have all of my time wasted, like looking for everything, and then making sure that I did not miss anything."*

**Personality tell:** *"I can't start working on something unless everything is already organized."* She works the Philippines night shift (4am COT = her workday). Pulled S1 plumbing into 5am her time and stuck with it.

**Alex's S1 prediction for her:** An HTML dashboard pulling from Monday, reorganized for her preference. Start with Monday (where most lives), add Slack + Missive later.

**S2 small win — walks the full loop:**
1. **Auds does it herself first.** Open Monday. Pick her top 5 tasks for today by hand, in priority order. Write them on a sticky or in a doc. This is the gold standard for her brain.
2. **Ask Claude to do the same.** Have Claude pull **tasks assigned to Audrey** (name her explicitly — shared API key won't know who "me" is). Ask: "rank these by what I should do first today and why."
3. **Score the gap.** Compare Claude's top 5 to her top 5. Match? Misses? Surprises?
4. **Refine through correction.** "You ranked X above Y but client work always comes before internal." That's the rule getting taught.
5. Park Slack and Missive. One source done well > three sources half-done.

**The pass/fail to celebrate:** Did Auds see her real tasks in a less-cluttered single view, AND did Claude's top 5 land close enough to hers that she'd trust it tomorrow? Even a plain text list counts. "Organized" is her happy place.

**Principle this surfaces:** shrink the problem. Three sources is overwhelming; one source done well is a win. Add the second when the first stops being scary.

**Taste of the final product:** the ranked list is the primitive of the dashboard she wants. At S4, the same list with two more sources merged in and follow-up drafts attached. She walks out with the central feature already working on one source.

**Stepping stones:**
- S3: Add ONE more source — pick Slack or Missive, whichever has the easier connection (Missive has a new MCP per Bryce). Now she sees Monday + one other in one view.
- S4: Add follow-up draft layer: for each task that needs a follow-up, Claude pre-writes the message. Demo day with all 3 sources or 2 + follow-up drafts.

**What to say at check-in:** "You said you can't start working until everything's organized. You just made Claude organize it. What's the next thing you want it to clean up?"

**Cross-reference:** Chanel wants the same thing. Pair them. Their tools should talk to each other.

---

## Kate Sarmiento — Team Lead

**Her exact words (S1):** *"My first vision is, is it possible to integrate both Missive and Monday on Cloud so we can minimize the admin part that we do manually?"*

**Then on the actual project:** *"We monitor the opportunities coming in each client inboxes in Missive. Whenever there are opportunities coming in, the PRCs are doing everything manually. We search the reporter in Muckrack manually, we will find the website, we will input everything on Monday manually. UVPM and DA — these are the two most important data we need to present to the client so they can have another view if it's worth pursuing."*

**The painful tool sprawl:** UVPM comes from SimilarWeb (browser extension), NOT Muckrack — Muckrack's numbers are stale. DA comes from Muckrack, fallback to Moz Free, which is limited to **5 searches per day**, which is brutal on a Monday morning when opportunities pile in.

**Her ask:** *"There are no tools yet that you can get the UVPM and DA at same time. So I'm just wondering if it's possible to get that in one place."*

**Massive S1 reveal from Bryce:** *"Missive just launched an MCP, Alex, so we can do a connection towards it."* Better than the API for this case.

**S2 small win — walks the full loop:**
1. **Kate does it herself first.** Pick one recent opportunity from Missive. Look up the UVPM (SimilarWeb extension) and DA (Muckrack or Moz) the way she normally would. Note the numbers AND the time it took.
2. **Get the Missive MCP connected.** Bryce can help — he flagged the MCP just launched. Have Claude pull the same opportunity.
3. **Ask Claude to do the same lookup.** "For outlet [name], return UVPM and DA. Show the source for each."
4. **Score the gap.** Did Claude's numbers match Kate's? If sources differ, which does she trust? (This is where she discovers Claude can be told "always use SimilarWeb for UVPM.")
5. **Refine.** Lock the source-of-truth rule for each metric.

**The pass/fail to celebrate:** for ONE outlet, did Claude return believable UVPM + DA AND did the time-to-answer beat Kate's manual time?

**Principle this surfaces:** meet the platform where it is. Missive has an MCP; use it. SimilarWeb has no MCP; use a web search and lock the source. Easiest connection first, hardest data later. Don't over-engineer.

**Taste of the final product:** the one-outlet lookup IS one row of her final enrichment workflow. At S4, the same lookup auto-fires when an opportunity arrives in Missive. She walks out having done the core action manually + once via Claude — that's the entire arc compressed.

**Stepping stones:**
- S3: Auto-pull a new opportunity from Missive → enrich with UVPM + DA → format for Monday paste.
- S4: One-click "enrich this opportunity" workflow demoed end-to-end.

**What to say at check-in:** "You said your first vision was integrating Missive and Monday on Cloud. You're literally connected to Missive's MCP and you just looked up an outlet without opening four tabs. That's the vision in week 2."

---

## Ehdina — Content + Social Manager

**Her exact words (S1, on her cohort hope):** *"For me, I think the most basic would be really be comfortable with AI. Like, it integrates with everything that we do and just be comfortable with building. When I think about marketing or anything that we need to build, we build in Claude, and I think that everyone in the team would be able to understand how it works. So it's not just the person who built it, but the entire team would able to understand it exactly."*

**Then on her actual project:** *"The goal basically is to have drafts ready for me to build on because we need to be consistent. We need to lock in and never ghost when we start posting. The only way that happens at that volume, like across LinkedIn, Instagram, and all the other social media platforms is to have drafts ready like two weeks in advance or even one month in advance. The goal is for me to be able to use [Bryce's] sales call transcripts. I can just input that and then we can come up with an on-brand content that is trained with his voice and it already knows if it's for personal brand or for the company voice."*

**Inputs:** Google Drive folder of videos + a Google Doc with transcripts of all sales calls.

**Big reframe vs. the auditor pass:** The auditor said "extract 5 voice rules + 2 do-not-do examples from existing on-brand pieces." That's NOT what Ehdina said. She wants GENERATIVE drafts FROM Bryce's sales call transcripts, trained on his voice, distinguishing personal-brand vs company voice.

**S2 small win — walks the full loop:**
1. **Ehdina does it herself first.** Pick one of Bryce's sales call transcripts. Read it. Write 2 sentences in Bryce's voice as she'd put them on LinkedIn — her best attempt at his voice. These are the calibration.
2. **Get Drive connected** (this was her S1 homework; may not have happened). Point Claude at the same transcript.
3. **Ask Claude to do the same.** "Read this transcript. Give me 5 sentences in Bryce's voice as he'd say them on LinkedIn." Compare to her 2.
4. **Score the gap — and put Bryce in the loop.** Show Bryce the combined 7 sentences. Which does he claim? Which would he never say? Bryce is the expert; his nods are the score.
5. **Refine.** Update the prompt with Bryce's correction. ("More plain English, less PR-speak.")

**The pass/fail to celebrate:** did Bryce claim at least 2 sentences as something he'd actually say? Bryce in the room = instant feedback loop, and Ehdina sees the principle "the expert validates" in action.

**Principle this surfaces:** train on the voice of the actual expert, and put the expert in the scoring loop. AI can mimic; the expert decides what passes.

**Stepping stones:**
- S3: Repeat with 3 transcripts. Generate one full LinkedIn post + one Instagram caption. Tag each as personal-brand voice OR company voice.
- S4: Two weeks' worth of drafts queued. Demo day = scrollable queue.

**Taste of the final product:** the 2 sentences Bryce claimed are the first entries in her brand voice corpus. By S4 there are dozens, and Claude is producing full posts. She walks out with the seed sentences and Bryce's nod attached to them.

**What to say at check-in:** "You said you wanted to be comfortable building. Bryce just nodded at a sentence you didn't write. That's comfortable."

**Risk to watch:** Ehdina's S1 plumbing status wasn't confirmed before the transcript ended. First 2 min of S2 build block: verify she's actually in Claude Code with a working connection. If not, that's her win (small but real).

---

## Kandice — Campaign Manager

**Her exact words (S1 on her project):** *"We download lists of reporters from Muckrack based on certain keywords. Those get populated into Google Sheets or into a CSV, which gets run through a list filter tool. Sometimes two, three thousand contacts per campaign to filter it down to about five hundred."*

**The tedious part:** *"Looking through each reporter is like, what do they write about, what outlets do they write for, does it make sense to pitch this person based on the client we're working for. It's very time consuming."*

**Her overwhelm quote (use carefully):** *"The whole thing is very overwhelming because it's kind of like, where do I start? The opportunities are endless. Where's the most impactful place to start? Where do I set aside the time? Sometimes I'm like, okay, it's just easier for me to just keep doing it as I'm doing it now."* — She also said the cohort is the answer: "It sounds like all of us have different ideas of kind of what we want to build, and I think that's cool because then we can just all utilize each other's tools."

**HUGE reframe of the auditor's "attendance risk":** Kandice was the S1 demo subject. She volunteered to share her screen. She walked the room through the Windows Run setup live, in real time, while everyone watched. She is NOT a flight risk. She's the most exposed-but-engaged person in the room.

**The S1 first-brick decision (Alex + Bryce + Kandice):** Bryce has scraped 400,000 reporters into profiles with story arcs (1 week left in scraping). He'll provide that database. Kandice's first brick is the **CLIENT SIDE**, not the reporter side. Specifically: have Claude read ONE client's Google Drive folder and produce a paragraph describing the client + the pitch.

**S2 small win — walks the full loop:**
1. **Kandice does it herself first.** Pick ONE client she knows cold. Write one paragraph (3-5 sentences) describing who this client is and what they're pitching this campaign. This is the answer key.
2. **Get Drive connected.** Point Claude at the same client's Drive folder.
3. **Ask Claude to do the same.** "Read this folder. In one paragraph, tell me who this client is and what they're pitching this campaign."
4. **Score the gap.** Compare Kandice's paragraph to Claude's. What did Claude miss? What did it overweight? What field that lives in her head wasn't in the Drive at all?
5. **Refine.** Either correct Claude's prompt or add the missing context to the Drive folder. The fix tells her which is the real bottleneck.

**The pass/fail to celebrate:** does Claude's paragraph match how Kandice would describe that client? If yes, she has a repeatable client-summarizer. If no, what's missing tells her what fields to add — and that's diagnostic gold.

**Principle this surfaces:** start with understanding, not matching. The reporter match is the visible end product, but it's a thin function of two understood inputs (client + reporter). If understanding the client is hard, matching is impossible. Solve the hard half first.

**Stepping stones:**
- S3: Repeat for 3 clients. Bryce's reporter scrape should be done by then. Match top 10 reporters to ONE client's pitch.
- S4: End-to-end: client folder → profile → matched reporter shortlist. Multiplying-level move.

**Taste of the final product:** the one client paragraph IS the first row of the client-understanding layer that her final reporter-matching tool sits on top of. By S4 Bryce's reporter database joins this. She walks out with the foundation laid — visibly, in her own words for one real client.

**What to say at check-in:** "You said the hard part is where to start. We just started. Look at that paragraph. That used to take you a meeting and a Google Sheet."

---

## Jenina — [role unknown]

**Status:** Not named once in the S1 transcript (142 min). Not on the ledger sheet. Email exists in team-emails.csv. S2 invite marked needs-action.

**Best guess:** Either she dropped, was sick June 9, or is filed under a different name (Alex spelled people's names tentatively at the start — "is it Adina?", "Ayesha Hoover").

**Before S2:** DM Bryce: "Is Jenina in? If yes — was she on S1 under another name, or did she miss? What's her role + what does she want to build? Should I shape a S2 first brick for her assuming she shows up?"

**If she shows up at S2 cold:** Run the project-canvas template with her in the first 10 minutes while the room is settling. Her S2 win = same as everyone's S1 win was: get Monday connected + ask one question. Don't pretend she's caught up.

---

## Cross-cohort connections worth surfacing

- **Chanel ↔ Auds:** identical underlying ask (Monday tasks in one organized place). Suggest they pair from S3 onward.
- **Kate ↔ Auds:** both need Missive eventually. Kate's MCP win is Auds' next-session input.
- **Marley ↔ Bryce:** Pitchy reports + reporter database both feed Marley's reporting + Kandice's filtering. Bryce should plan to "ship" his data work in S3 when others need it.
- **Ehdina ↔ Bryce:** Ehdina's voice training depends on Bryce's transcript folder. Confirm with Bryce in S2: is the Drive folder shared correctly so Ehdina has access?
- **Kandice ↔ Bryce:** her reporter side is parked until his scrape finishes (he said "1 week left" on June 9 — so it should be done by S3 on June 23).

## The arc explicitly

| | S2 win = | S3 build = | S4 demo = |
|---|---|---|---|
| Bryce | Help others land theirs | Co-lead a 10-min lesson | Live demo of one Sunday hack |
| Marley | Client-facing section of one report | Internal "what we tried" half + Pitchy inspo | Full monthly report + workbench of edits |
| Ice | Top 3 of 10 notifications ranked + reasons | Auto-feed from real source | Scheduled brief |
| Chanel | One bug fixed on her real Monday board | Priority + due + minutes ranking on it | Dashboard shared with one teammate |
| Auds | Monday tasks in one clean view | + Slack OR Missive | + follow-up draft layer |
| Kate | Missive MCP connected + 1 outlet enriched | Auto-enrich a new opportunity | One-click opportunity enrichment |
| Ehdina | 5 sentences in Bryce's voice (Bryce nods at 2) | Full LinkedIn + Instagram drafts | 2 weeks of queued drafts |
| Kandice | One client described in a paragraph from Drive | Match 10 reporters to that client | Full client → reporter shortlist |

## Standing setup correction — name the assignee, don't say "my"

Alex flagged in S1 and Auds confirmed: the team is almost certainly sharing one org-level Monday API key (Bryce activated the integrations from his side). The key has no user identity attached. So when anyone asks Claude "what are MY tasks?" or "tasks assigned to me," Claude is guessing — usually pulling whoever the key authenticates as, or returning everything visible.

**The S2 fix:** every Monday prompt names the assignee explicitly. Never "my tasks." Always "tasks assigned to Audrey," "tasks assigned to Chanel," "opportunities Kate is monitoring." Same correction for filter columns: "where the Assignee column contains 'Kandice'."

**Who this affects directly:**
- **Auds** — her one-clean-view S2 win must explicitly request `assignee = Audrey`. Otherwise she sees Edina's tasks (as happened to Audrey in S1).
- **Chanel** — same. Her broken-board fix prompts name Chanel as the assignee.
- **Kate** — name herself when asking about Missive opportunities (Missive has the same user-key question; check during her MCP connect).
- **Kandice / Ice / Ehdina / Marley** — same standing rule when they touch Monday.

**Better long-term fix (offer, don't push):** each person generates their own personal Monday dev token from their own profile so the key carries their identity. Bryce will know if Monday's plan allows this. Don't burn S2 build block on it; mention it as an S3 cleanup option.

**At check-in if results look wrong:** ask "did you name yourself in the prompt?" before debugging anything else. That's the first cut.

---

## Paper is allowed (and welcome)

Several Step 1 moves ask the participant to do something by hand: Chanel writes her ideal board view, Auds ranks her top 5 tasks, Ice picks her favorite 3 of 10. **They don't have to type it up.** Tell them they can write it on paper, take a photo, and drop the photo into Claude. Claude reads handwriting. Removes the "now I have to put this in a doc" friction that kills momentum. Especially useful for Chanel (board diagnosis) and Auds (today's ranking) where the on-paper version is the natural shape.

---

## Standing rules for S2 facilitation

- **No architecture docs as wins.** Documentation is the byproduct, not the artifact. The win is something on screen that wasn't there 25 minutes ago.
- **Cameras-on during build.** Bryce already committed to enforcing this; remind once at the top.
- **Share-out is the win, not the brief itself.** Each person gets 60-90 sec to show what changed on their screen. That's where the "closing in" feeling lives.
- **Don't argue Marley's "AI isn't good enough."** Let her show a first-section draft and ask the room what they think.
- **Bryce as helper, not driver.** Park his own projects this session.
- **If plumbing is broken again (Git, Drive auth, etc.):** that's the win for that person. Don't apologize, name it: "you got into the second integration. That was Tuesday-night-engineer work." Sit Bryce next to them.
