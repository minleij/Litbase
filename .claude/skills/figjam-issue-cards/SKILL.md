---
name: figjam-issue-cards
description: Generates one color-coded, quote-backed "issue card" PNG image per reported interface-design/human-centered problem, pulled from this project's coded_articles/ corpus and their source markdown in articles/, for pinning up on a whiteboard (FigJam, Miro, Mural, or similar) to qualitatively compare interface issues across articles by task type, computational design, and interactional qualities. Use this any time the user wants to "make issue cards," "export cards for FigJam/Miro/a whiteboard," "make a card wall," "compare interface issues visually," "regenerate the cards," or asks about the card color scheme / the legend / why a card looks a certain way. Also use it if they ask to redo or extend a previous card export (e.g. "add cards for the new articles I just coded," "the cards don't look right, fix them," "I got more Figma credits, can you push these to FigJam"). Do not use this for the underlying article coding itself (that's the analytic-coding skill) or for writing prose about the issues (that's the literature review itself) — this skill only turns already-coded articles into card images.
---

# FigJam / whiteboard issue cards

## What this produces and why it's shaped this way

One PNG image per reported interface-design or human-centered issue in the coded corpus, styled as a small card: a row of color-coded dimension chips, a one-sentence title, the verbatim quote(s) that back it up, and a footer with the citation. The point is a qualitative comparison board — spread these across a whiteboard and eyeball which kinds of issues cluster around which kinds of tasks, computational designs, or interaction models. That comparison goal drives most of the specific choices below (which dimensions get chips, why quotes must be verbatim, why each card is its own file), so if a step below seems arbitrary, it's probably load-bearing for that goal — check before changing it.

This skill was built by extracting a working, already-validated pipeline from a real session (see git history around the `exports/figjam_issue_cards/` folder for the original run), including two real failures worth knowing about up front:

1. **Grouping several cards into one bigger "sheet" image was tried first and abandoned.** Once flattened to an image, individual cards can't be pulled apart on a whiteboard — the entire point of a card wall is that each issue is independently movable. Every script here generates **one file per card**. Don't regress this even if it seems more efficient.
2. **Figma's own SVG-to-node importer badly mangles hand-rolled multi-`<text>`-element SVG** — it overlapped and collapsed lines that render correctly in any real browser. That's why this pipeline rasterizes to PNG with a real headless browser rather than handing raw SVG to Figma to import. PNGs work in any whiteboard tool, not just Figma.

Read `scripts/generate_cards.py`'s module docstring for the fuller version of both of these if you're about to change the card-grouping or output-format logic — it explains exactly what broke and what the symptom looked like.

## Step 0 — Confirm scope with the user

Before running anything, confirm (don't just assume) with the user:
- **Which study types to include.** Default is `"User Study"` only — other study types (System/Architecture Paper, Meta-Review/Survey, Algorithm/Controller Evaluation, Design/Interface Concept Paper) rarely report concrete interface issues from real use, so including them mostly produces empty-issues entries. Only widen this if the user asks.
- **Where output should go.** Default to `exports/figjam_issue_cards/` at the project root (matches the existing convention already in this repo, with `svg/` and `png/` subfolders) unless the user wants somewhere else.
- **Full corpus or a subset** (e.g. "just the articles I coded this week"). If a subset, get the specific `article_id`s or a filter the user has in mind before Step 1.

Locate the project root by finding the sibling `articles/` and `coded_articles/` directories — don't assume the current working directory is the root.

## Step 1 — Extract scope

```
python .claude/skills/figjam-issue-cards/scripts/extract_scope.py \
    --project-root <project root> \
    --out <workspace>/article_meta.json \
    --study-types "User Study"
```

This reads `coded_articles/index.json` + each matching `coded_articles/<id>.json`, filters to the requested study type(s), and writes a flat `article_meta.json` with citation info, the source markdown path, each article's chip-relevant dimension codes, and `summary.issues` (a paraphrased hint used only as a checklist in the next step — never quoted directly). Read the printed per-article dimension-coverage line; an article with 0 dimensions coded usually means it has no `task_environment_v*` classification block yet and will just get chip-less cards, which is fine but worth mentioning to the user.

If the user asked for a specific subset of articles, filter `article_meta.json` down to just those `article_id`s after this step (or re-run with a narrower `--study-types`, or hand-edit the list — whichever is simplest for the given ask).

## Step 2 — Extract verbatim quotes (parallel subagents)

This is the one step that needs real judgment — deciding what counts as a human-centered/interface issue, and locating the exact backing sentence — so it runs as subagents reading the actual article text, not a deterministic script.

Read `references/quote_extraction_prompt.md` now. It has the full prompt template plus the reasoning behind its specific wording — don't skip the "Why this wording" section, it explains the two things most likely to go wrong if you improvise a shorter prompt (the board filling up with methodology-caveat noise instead of real interface issues, and paraphrased "quotes" that can't be trusted without re-opening the source).

Batch the in-scope articles from `article_meta.json` into groups of ~5, fill in the template per batch, and launch all batches as `Agent` tool calls **in the same message** (`subagent_type: general-purpose`, `run_in_background: true`) so they run concurrently rather than one at a time. Save each subagent's returned JSON array to its own file (`batch1.json`, `batch2.json`, ...) in a workspace/scratch directory as the results come back.

Once all batches are back:

```
python .claude/skills/figjam-issue-cards/scripts/merge_batches.py \
    --batches-dir <workspace> \
    --article-meta <workspace>/article_meta.json \
    --out <workspace>/issues_data.json
```

This cross-checks that every in-scope article actually got covered by some batch and flags anything that didn't (a batch that silently dropped an article, or a subagent that typo'd an `article_id`) — fix any warning before moving on rather than shipping a card set with silent gaps.

## Step 3 — Generate per-card SVGs

```
python .claude/skills/figjam-issue-cards/scripts/generate_cards.py \
    --article-meta <workspace>/article_meta.json \
    --issues-data <workspace>/issues_data.json \
    --out-dir <output dir>/svg
```

Read `references/color_coding.md` before running this if you haven't already this session — it explains exactly which dimensions get a colored chip, where their codes come from, and how the viridis color scale is computed from `references/dimension_order.json`. That file is a **hand-copied snapshot** of `analysis/visualize.py`'s `DIMENSION_ORDER` — the color-coding reference explains how to check it hasn't drifted out of sync before trusting the colors on a new batch of cards.

This writes one `.svg` per issue card, `_legend.svg`, and a `card_manifest.json` (card id → pixel dimensions) that the next step consumes. Want to preview just the legend/color scheme without a full corpus run (e.g. the user asks "what would the colors look like")? Run with `--legend-only` instead.

## Step 4 — Rasterize to PNG

```
python .claude/skills/figjam-issue-cards/scripts/rasterize_cards.py \
    --svg-dir <output dir>/svg \
    --out-dir <output dir>/png
```

Runs a headless Chromium/Edge process per card (auto-detected; pass `--browser-path` explicitly if detection fails), matching the browser window to each card's own SVG dimensions so the screenshot is pixel-exact. This takes a few minutes for a full corpus (~100+ individual browser launches) — that's expected, not a hang. If it reports failures, check the printed stderr snippet per failed card before retrying; a common cause is the browser path not being found (pass `--browser-path` explicitly).

Spot-check 2-3 of the resulting PNGs (read them with the Read tool) before telling the user it's done — look specifically for: chip text not overlapping the row above/below it, quote text staying inside the card's right edge, and the footer showing the full author name and article_id without being cut off. These are the exact three things that broke in the original run this skill was extracted from.

## Step 5 — Package and report

```
python .claude/skills/figjam-issue-cards/scripts/package_zip.py \
    --png-dir <output dir>/png \
    --out <output dir>_png.zip
```

Report back to the user:
- Where the zip and the unzipped PNG folder are.
- Card count and which articles contributed zero cards (from `merge_batches.py`'s output) — worth a one-line mention since an article with a genuinely thin `summary.issues` (e.g. purely methodological limitations) legitimately produces zero cards, which can look like a bug if unexplained.
- A reminder of the legend file's location and that colors only compare meaningfully within one chip label (e.g. TASK vs TASK), not across dimensions.

## Re-running for new or updated articles

If the user has coded new articles since the last card export, or wants to redo a subset, re-run Steps 1-5 — there's no incremental/append mode, since the color scale in Step 3 is computed globally across whatever's in `article_meta.json` at generation time (an ordinal scale needs to see the full set it's coloring to place codes consistently). Regenerating the whole set is cheap enough (dominated by Step 4's rasterization time) that this isn't worth optimizing away.
