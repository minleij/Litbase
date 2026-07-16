---
name: figjam-result-cards
description: Generates one color-coded, quote-backed "result card" PNG image per reported study finding — prioritizing qualitative results (thematic findings, described behaviors, participant reactions) while also covering quantitative ones (statistics, performance numbers) — pulled from this project's coded_articles/ corpus and their source markdown in articles/, for pinning up on a whiteboard (FigJam, Miro, Mural, or similar) to qualitatively compare what studies actually found across task type, computational design, and interactional qualities. Use this any time the user wants to "make result cards," "export findings cards," "make a card wall of results/findings," "compare study results visually," "regenerate the result cards," or asks about the result-card color scheme / legend. This is the sibling skill to figjam-issue-cards (same color scheme and card structure, extracts reported RESULTS/FINDINGS instead of reported interface ISSUES/problems) — if the user says "issues," "problems," or "what went wrong," that's figjam-issue-cards instead; if they say "results," "findings," "what did the study show," or "what worked," use this one. Do not use this for the underlying article coding itself (that's the analytic-coding skill) or for writing prose about the findings (that's the literature review itself) — this skill only turns already-coded articles into card images.
---

# FigJam / whiteboard result cards

## What this produces and why it's shaped this way

One PNG image per reported study result/finding in the coded corpus, styled as a small card: a row of color-coded dimension chips, a one-sentence title, the verbatim quote(s) that report it, and a footer with the citation. The point is a qualitative comparison board — spread these across a whiteboard and eyeball which kinds of results cluster around which kinds of tasks, computational designs, or interaction models. Qualitative findings (described behaviors, thematic takeaways, participant reactions) are prioritized over quantitative ones (statistics, performance numbers) when there's a choice of what to include, though both are captured — this reflects a deliberate call: qualitative results are usually harder to spot and easier to lose in a corpus skim, and they're what's actually interesting to compare across a card wall of different systems.

**This skill is the sibling of `figjam-issue-cards`** — same pipeline shape, same color scheme, same card layout, different extraction target. Read that skill's `SKILL.md` and `scripts/generate_cards.py` module docstring if you haven't already this session; the two real lessons documented there apply here without modification:

1. **Grouping several cards into one bigger "sheet" image was tried first and abandoned.** Once flattened to an image, individual cards can't be pulled apart on a whiteboard. Every script here generates **one file per card**.
2. **Figma's own SVG-to-node importer badly mangles hand-rolled multi-`<text>`-element SVG.** That's why this pipeline rasterizes to PNG with a real headless browser rather than handing raw SVG to Figma to import.

Because these two skills read the same source articles and can legitimately produce cards that overlap in content (a study's reported result is often also the evidence for an interface issue, just framed differently — "operators took 40% longer to find the target" is a result; "the search interface slowed operators down" is an issue built on that same result), it's fine and expected for the user to run both skills over the same corpus and get some thematic overlap on the board. Don't try to make this skill avoid territory the other skill covers — see `references/quote_extraction_prompt.md` for why.

## Step 0 — Confirm scope with the user

Before running anything, confirm (don't just assume) with the user:
- **Which study types to include.** Default is `"User Study"` only — other study types (System/Architecture Paper, Meta-Review/Survey, Algorithm/Controller Evaluation, Design/Interface Concept Paper) rarely report empirical results in the relevant sense (no participants, no measured outcomes), so including them mostly produces empty-results entries. Only widen this if the user asks.
- **Where output should go.** Default to `exports/figjam_result_cards/` at the project root (parallel to the existing `exports/figjam_issue_cards/` convention, with `svg/` and `png/` subfolders) unless the user wants somewhere else.
- **Full corpus or a subset** (e.g. "just the articles I coded this week"). If a subset, get the specific `article_id`s or a filter the user has in mind before Step 1.

Locate the project root by finding the sibling `articles/` and `coded_articles/` directories — don't assume the current working directory is the root.

## Step 1 — Extract scope

```
python .claude/skills/figjam-result-cards/scripts/extract_scope.py \
    --project-root <project root> \
    --out <workspace>/article_meta.json \
    --study-types "User Study"
```

This reads `coded_articles/index.json` + each matching `coded_articles/<id>.json`, filters to the requested study type(s), and writes a flat `article_meta.json` with citation info, the source markdown path, each article's chip-relevant dimension codes, and `summary.results` (a paraphrased hint used only as a checklist in the next step — never quoted directly). Read the printed per-article coverage lines; an article flagged `[no summary.results text]` will just produce zero result cards, which is worth a heads-up to the user but not an error.

If the user asked for a specific subset of articles, filter `article_meta.json` down to just those `article_id`s after this step (or re-run with a narrower `--study-types`, or hand-edit the list — whichever is simplest for the given ask).

## Step 2 — Extract verbatim quotes (parallel subagents)

This is the one step that needs real judgment — deciding what counts as a genuinely reported result versus methodology description, weighing qualitative findings over quantitative ones, and locating the exact backing sentence (with the number intact, for quantitative ones) — so it runs as subagents reading the actual article text, not a deterministic script.

Read `references/quote_extraction_prompt.md` now. It has the full prompt template plus the reasoning behind its specific wording — don't skip the "Why this wording" section, it explains the two things most likely to go wrong if you improvise a shorter prompt (a board full of easy-to-spot statistics while the harder-to-find qualitative findings get skipped, and a "significantly faster" title with the actual number quietly dropped).

Batch the in-scope articles from `article_meta.json` into groups of ~5, fill in the template per batch, and launch all batches as `Agent` tool calls **in the same message** (`subagent_type: general-purpose`, `run_in_background: true`) so they run concurrently rather than one at a time. Save each subagent's returned JSON array to its own file (`batch1.json`, `batch2.json`, ...) in a workspace/scratch directory as the results come back.

Once all batches are back:

```
python .claude/skills/figjam-result-cards/scripts/merge_batches.py \
    --batches-dir <workspace> \
    --article-meta <workspace>/article_meta.json \
    --out <workspace>/results_data.json
```

This cross-checks that every in-scope article actually got covered by some batch and flags anything that didn't (a batch that silently dropped an article, or a subagent that typo'd an `article_id`) — fix any warning before moving on rather than shipping a card set with silent gaps.

## Step 3 — Generate per-card SVGs

```
python .claude/skills/figjam-result-cards/scripts/generate_cards.py \
    --article-meta <workspace>/article_meta.json \
    --results-data <workspace>/results_data.json \
    --out-dir <output dir>/svg
```

Read `references/color_coding.md` before running this if you haven't already this session — it explains exactly which dimensions get a colored chip, where their codes come from, and how the viridis color scale is computed from `references/dimension_order.json`. That file is a **hand-copied snapshot** of `analysis/visualize.py`'s `DIMENSION_ORDER`, kept identical to the copy in `figjam-issue-cards/references/` on purpose — if you ever need to update one because the underlying codebook drifted, update both together so the two card sets keep using the same visual language.

This writes one `.svg` per result card, `_legend.svg`, and a `card_manifest.json` (card id → pixel dimensions) that the next step consumes. Want to preview just the legend/color scheme without a full corpus run? Run with `--legend-only` instead.

## Step 4 — Rasterize to PNG

```
python .claude/skills/figjam-result-cards/scripts/rasterize_cards.py \
    --svg-dir <output dir>/svg \
    --out-dir <output dir>/png
```

Runs a headless Chromium/Edge process per card (auto-detected; pass `--browser-path` explicitly if detection fails), matching the browser window to each card's own SVG dimensions so the screenshot is pixel-exact. This takes a few minutes for a full corpus (~100+ individual browser launches) — that's expected, not a hang. If it reports failures, check the printed stderr snippet per failed card before retrying; a common cause is the browser path not being found (pass `--browser-path` explicitly).

Spot-check 2-3 of the resulting PNGs (read them with the Read tool) before telling the user it's done — look specifically for: chip text not overlapping the row above/below it, quote text staying inside the card's right edge, the footer showing the full author name and article_id without being cut off, and — specific to this skill — that any quantitative-result cards actually kept their number/statistic in the quote rather than a vague "significantly better" with the number missing.

## Step 5 — Package and report

```
python .claude/skills/figjam-result-cards/scripts/package_zip.py \
    --png-dir <output dir>/png \
    --out <output dir>_png.zip
```

Report back to the user:
- Where the zip and the unzipped PNG folder are.
- Card count, and roughly how many leaned qualitative vs. quantitative if that's easy to eyeball from the titles — the user cares about this balance.
- Which articles contributed zero cards (from `merge_batches.py`'s output), if any — for this skill that's unusual enough (unlike the issues skill, where a thin methodological article legitimately yields nothing) that it's worth a specific look at why before reporting it as normal.
- A reminder of the legend file's location and that colors only compare meaningfully within one chip label (e.g. TASK vs TASK), not across dimensions — and that it's the same legend/color language as `figjam-issue-cards`, so cards from both skills can be mixed on one board.

## Re-running for new or updated articles

If the user has coded new articles since the last card export, or wants to redo a subset, re-run Steps 1-5 — there's no incremental/append mode, since the color scale in Step 3 is computed globally across whatever's in `article_meta.json` at generation time (an ordinal scale needs to see the full set it's coloring to place codes consistently). Regenerating the whole set is cheap enough (dominated by Step 4's rasterization time) that this isn't worth optimizing away.
