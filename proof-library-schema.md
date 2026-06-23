# Proof Library — Schema

Last updated: 2026-06-23

Single source of truth for the structure of `proof-library.json`. The static page at `proof-library.html` reads this JSON client-side. Anything that writes to the JSON (skills, workers, manual edits) MUST conform to the entry shape below.

This is the data layer for a future content-generation pipeline. Honest gaps (status=raw, null URLs) are more useful than fabricated entries.

---

## Entry shape

Each entry is a JSON object with these fields. Required unless marked optional.

| Field | Type | Required | Notes |
|---|---|---|---|
| `id` | string (kebab-case slug) | yes | Globally unique. Convention: `<cohort>-s<N>-<builder-slug>-<short-tag>` for wins, `<cohort>-<short-tag>` for everything else, e.g. `rpa-s2-david-zoom-downloader`, `nc17-thesis-line`. |
| `type` | enum | yes | One of: `clip`, `win`, `testimonial`, `lesson`, `screenshot`, `published`, `quote`. |
| `cohort` | enum | yes | One of: `rpa`, `dbalp`, `ff-mon`, `ff-thu`, `nc17`, `dcmex`, `none`, `cross-cohort`. |
| `title` | string (one line) | yes | Short and concrete. The card headline. |
| `source_url` | string OR null | yes | Where this came from. Transcript file path (relative repo path is OK), Skool post URL, LinkedIn URL, Fathom URL. Null if unverified. |
| `media_url` | string OR null | yes | YouTube unlisted, Drive, direct file. Null if no media uploaded yet. Use TODO marker in `notes` when waiting on upload. |
| `thumbnail` | string OR null | yes | Path under `build-room-visuals/assets/proof/` or absolute URL. Null if none. |
| `quote` | string OR null | yes | The actual text. Markdown allowed. Null when the entry is purely a media reference (e.g. screenshot, video clip with no transcript line). |
| `attribution` | string OR null | yes | Person + cohort, e.g. "Kate (DBALP cohort)". Null for cross-cohort or facilitator-only entries. |
| `timestamp` | string OR null | yes | `HH:MM:SS` or `MM:SS` in the source transcript or video. Null if not applicable. |
| `tags` | array of strings | yes | Free-form. Examples: `first-brick`, `thesis`, `breakthrough`, `pivot`, `peer-teaching`, `live-demo`, `mid-session-extension`, `recovery`. Empty array allowed. |
| `status` | enum | yes | One of: `raw`, `cleared-for-public`, `live`, `featured`, `redacted`. Default is `raw`. See lifecycle below. |
| `date_captured` | string (YYYY-MM-DD) | yes | Date this entry was added to the library. |
| `date_cleared` | string OR null | yes | Date status moved past `raw`. Null until that happens. |
| `notes` | string | optional | Internal-use free-form. TODO markers, permission asks pending, sensitivity flags. |

---

## Field detail

### `id`

Globally unique kebab-case slug. Convention by type:

- **win** — `<cohort>-s<N>-<builder-slug>-<short-tag>`, e.g. `dbalp-s3-kate-missive-live`
- **clip** — `<cohort>-<short-tag>` or `<source>-<short-tag>`, e.g. `nc17-thesis-line`, `dbalp-s3-kate-applause`
- **published** — `<platform>-<slug-from-url>`, e.g. `linkedin-how-to-get-your-team-to-actually-use-ai`
- **testimonial** / **quote** — `<cohort>-<speaker-slug>-<short-tag>`, e.g. `ff-mon-ruben-on-purpose-on-track`
- **lesson** — `<cohort>-s<N>-<concept-slug>`, e.g. `cross-cohort-burn-the-thread`
- **screenshot** — `<cohort>-s<N>-<builder-slug>-screenshot-<N>`

If a builder appears multiple times in one session, append a discriminator: `-1`, `-2`, or a concept-tag.

### `type`

| Value | Use for |
|---|---|
| `clip` | Audio / video moment, transcript-grounded. Marketing-ready or near-ready. |
| `win` | Per-builder, per-session breakthrough from a debrief wins post. The primary debrief artifact. |
| `testimonial` | A participant said something quotable about the program. Permission status matters. |
| `lesson` | A teaching / framework / heuristic surfaced live in a session (cross-cohort value). |
| `screenshot` | Image-only proof: a dashboard, sidebar, deck, working tool. |
| `published` | Already shipped publicly (LinkedIn newsletter, podcast episode, talk recording). |
| `quote` | A noteworthy thing someone said that doesn't fit `testimonial` (e.g. a sponsor's offhand line, a builder's own framing of their work). |

### `cohort`

Use `cross-cohort` when the entry applies to multiple cohorts or to The Build Room as a whole (e.g. the thesis line). Use `none` for things outside any cohort context (e.g. Alex's own published article).

### `status` — lifecycle

| Value | Meaning |
|---|---|
| `raw` | Default. Captured but no permission asked, no public clearance, no media uploaded. Library shows but does not surface for promo. |
| `cleared-for-public` | Permission granted (testimonial form, explicit text consent, builder posted it themselves). Ready for repurposing. |
| `live` | Currently in active use somewhere public (LinkedIn post, Skool homepage, landing page). |
| `featured` | Flagged as a top-of-funnel hero asset. The handful of strongest proofs. |
| `redacted` | Previously surfaced but pulled. Keep the record; explain why in `notes`. |

Promote conservatively. The default is `raw`. Only mark `cleared-for-public` if there's already explicit evidence Alex shared it publicly (e.g. a live LinkedIn post URL).

### `source_url`

Honest gaps over fabrication. If you can't verify a URL, set null. Acceptable values:

- Relative repo paths (`brain/the-build-room/cohorts/.../s2-wins-post-2026-06-23.md`)
- Absolute URLs (Fathom, Skool, LinkedIn, YouTube)
- `null`

### `media_url` and `thumbnail`

Both nullable. The library deliberately does NOT host media at v1. Media uploads to Drive / YouTube unlisted are a later project. When a media upload is pending, set `media_url: null` and add `"TODO: upload <type> to <destination>"` to `notes`.

`thumbnail`, when set, should be a path under `build-room-visuals/assets/proof/` (relative) for repo-tracked images, or an absolute URL.

### `tags`

Free-form, but reuse existing tags when they fit. Live working set:

`first-brick`, `thesis`, `breakthrough`, `pivot`, `peer-teaching`, `live-demo`, `mid-session-extension`, `recovery`, `scope-lock`, `tooling`, `vision`, `urgency`, `framework`, `cohort-promise`, `objection-handling`, `humor`, `story`, `recognition`.

Don't invent a tag if an existing one works.

---

## What NOT to put in the library

- Quotes you can't trace to a transcript line or a written source
- Builder last names + identifying detail in any `cleared-for-public` entry without evidence the builder posted it themselves
- Internal facilitator-only diagnostics (those belong in facilitator recap docs)
- Media speculation (don't claim a video exists if it hasn't been recorded)

---

## Mutation rules

- Append-only by default. Promote `status` upward as evidence arrives.
- `id` is immutable once set. If wrong, mark old entry `redacted` and add a new one.
- Schema changes happen here first, then the JSON, then the HTML.
- Skills that write to the JSON (e.g. `build-room-debrief`) must conform to this schema. Drift gets caught at HTML render time (cards will show empty fields).

---

Alex Salinsky · The Build Room
