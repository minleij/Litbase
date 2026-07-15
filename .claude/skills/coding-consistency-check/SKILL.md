---
name: coding-consistency-check
description: Compares two versions of the same coded_articles/<article_id>.json record (a past git version against the current one, either uncommitted or already committed) to check whether repeated analytic coding of the same article produced consistent results. Use this whenever the user wants to "check consistency," "check for drift," "compare recodes," "did I code this the same way," or "verify my recoding" for one article or the whole HSI/HRI corpus — especially after they've recoded articles following a codebook version bump and want reassurance the change was applied as intended and nothing else drifted. Distinguishes expected changes (driven by a documented codebook version bump) from true inconsistency (same codebook version, different judgment call). Do not use this for the initial coding of a new article — that's the analytic-coding skill's job — or for editing codebooks themselves.
---

# Coding Consistency Check (HSI/HRI Literature Review)

## What this skill does and why

The analytic-coding skill overwrites `coded_articles/<article_id>.json` in place every time an article is (re)coded, and git already keeps every version. That means the raw material for a consistency check already exists — nothing needs to be saved specially before a recode. This skill's job is to pull two versions of a record, diff them field by field, and — critically — separate differences that are *expected* (a codebook version bumped and the article was deliberately re-coded against the new rules) from differences that look like plain inconsistency (the same rules, applied twice, producing a different answer). Only the second kind is the actual reliability problem worth the user's attention.

The diffing itself (matching classification items by dimension/condition, computing what changed) is mechanical, so it's handled by a bundled script. Deciding *why* something changed — whether a version-bump note actually covers a given dimension, whether a reworded justification represents a substantive change of mind or just better phrasing — needs judgment, so that part is this skill's job, not the script's.

## Step 0 — Establish scope and project root

Confirm the project root the same way analytic-coding does: the directory containing both `articles/` and `coded_articles/` as siblings. Then figure out what the user actually wants compared:

- **One or a few named articles** (e.g. "check consistency for cummings_2008" or "did I recode donmez and bashyal the same way as before?") → pass their `article_id`s to the script directly.
- **The whole corpus** ("check the whole corpus for drift", "did anything drift since I bumped the codebook") → use `--all`.
- **A specific baseline** ("compare against last month", "compare since the v0.9 release", a specific commit/tag the user names) → pass `--old-ref`. Otherwise let the script's default version resolution run: it compares the working tree against HEAD if there are uncommitted changes, or the two most recent commits touching the file if not. This default matches the normal workflow (recode, then check before committing) so you usually don't need to pass any ref yourself — only do so when the user asks for a specific comparison point.

## Step 1 — Run the diff script

```
python scripts/compare_codings.py <article_id> [<article_id> ...] --out <tmp_path>
python scripts/compare_codings.py --all --out <tmp_path>
```

(Path is relative to this skill's own folder: `.claude/skills/coding-consistency-check/scripts/compare_codings.py`. Run it from, or pass `--project-root`, the project root.)

Read the resulting JSON. Each article entry is either `{"skipped": "<reason>"}` (nothing to compare — report this plainly, don't treat it as an error) or a full structural diff: `codebook_versions`, `study_type`, `summary`, `classification` (a flat list of only the items that changed, each tagged with a `status`), and `flags`. Each entry also carries the raw `notes_old` / `notes_new` text — read these yourself; the script does not attempt to match them against dimensions, because that's a natural-language judgment call, not a string-matching one.

## Step 2 — Categorize every classification diff

For each item in `classification` with `status: "code_changed"`:

1. If `version_bumped` is `true` for that item's `governing_codebook_key` — read `notes_new` and judge whether it actually documents *this dimension* being re-coded (not just that the codebook was bumped at all; the note needs to plausibly cover this specific dimension or condition). If yes → **expected, documented**. If the version bumped but the notes don't mention this dimension → **version bumped, undocumented** (a soft flag — probably just a missed note, still worth a one-line mention).
2. If `version_bumped` is `false` (both versions were coded against the identical codebook version for that key) → **drift, needs review**. This is the case the skill exists to catch: same rules, different answer. Report every one of these, even ones that seem minor — a small inconsistency in one article is exactly the kind of thing that becomes a bigger problem at corpus scale, and it's not this skill's place to decide something is too trivial to mention.
3. If `version_bumped` is `null` (the dimension/codebook key only exists on one side — e.g. a codebook was newly applied to this article) → not drift at all, just new coverage. Mention it informationally, not as a flag.

Items with `status: "justification_only_changed"` (same code, different wording) are not inconsistency by definition — the coder can rightly phrase a justification differently on a reread. Read the old and new text and use judgment: does the new justification describe a *different reason* for the same code (worth a "notable text change" mention, since it might mean the reasoning shifted even though the conclusion happened to land the same place), or is it the same reasoning in different words (skip it, don't clutter the report)? Apply this same judgment to `study_type.justification` and any changed `summary` fields.

## Step 3 — Study type, flags, and added/removed items

- `study_type.primary` / `.secondary`: same categorization logic as classification items, keyed off the `study_type` codebook version.
- `flags.added` / `flags.removed`: usually these just follow from a classification change you've already covered above (e.g. an "Unclear" flag disappearing because that dimension got a real code) — don't re-report those separately. Only call out a flag change on its own if it doesn't correspond to any classification diff already reported (e.g. a flag was resolved without any visible code change, which is itself worth a mention).
- `classification` items with `status: "added"` or `"removed"`: usually a dimension or condition that's new or no-longer-applicable coverage, not drift — but if a condition that clearly still applies to the article seems to have silently vanished, say so.

## Step 4 — Write the report

Follow `references/report-template.md` for structure. Write the file to `coding_consistency_reports/<name>_<YYYY-MM-DD>.md` at the project root (create the directory if it doesn't exist yet) — use the article's id for a single-article check, or something like `corpus_<date>.md` for a batch/whole-corpus check. Don't overwrite a same-day report from an earlier run without checking with the user first; append a suffix if needed.

## Step 5 — Report back to the user

In chat (not just the file), lead with the headline: how many articles were compared, and how many genuine drift items were found. If there's any true drift (Step 2, case 2), name the specific article/dimension/codes inline in chat — don't make the user open the file to learn there's a real problem. Mention the file path for the full detail. If everything checked out clean, say so plainly rather than padding the response.

## A note on scale

If this is run across the whole corpus regularly, the report file itself becomes a useful trend record — don't feel obligated to reconcile every past report, but if the user asks something like "has drift gotten better or worse," the dated files in `coding_consistency_reports/` are there to compare.
