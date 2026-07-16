# Quote-extraction subagent prompt template

This is the step in the pipeline that genuinely needs judgment (deciding what counts as a reported study result/finding, and locating the exact sentence that supports it) rather than a deterministic script — so it runs as parallel research subagents, not code. Use the `Agent` tool with `subagent_type: general-purpose`, one call per batch of ~5 articles, all launched in the same message so they run concurrently. Set `run_in_background: true` for each and wait for the completion notifications rather than polling.

Fill in the `{...}` placeholders below per batch and use the result as the subagent's `prompt`. Keep the instructional text itself intact — it encodes real lessons (see "Why this wording" below) rather than boilerplate.

---

```
You are doing factual research extraction for a literature review project at {PROJECT_ROOT}. This is NOT a coding task — you must not write or edit any files. You only need to read files and return a JSON answer in your final message.

## Background
The project has coded human-swarm-interaction (HSI/HRI) research articles. Each article has a markdown source file under `articles/`, and a structured JSON coding record under `coded_articles/`. The JSON record has a `summary.results` field with a PARAPHRASED list of reported results/findings for that article — but we now need the ACTUAL VERBATIM sentences/passages from the article's markdown text that report each of those results, because these will become quote-cards on a design board.

## Your task
For each of the {N} articles below, do the following:
1. Read the markdown source file (path given).
2. Using the given `results_summary` as a checklist/guide of what results were already identified, locate the actual verbatim text in the markdown that reports each result (usually in a Results section, but qualitative findings often show up in Discussion too).
3. Only keep genuinely reported RESULTS/FINDINGS — things the study actually observed or measured, not methodology. This includes:
   - **Qualitative findings** (prioritize these): described participant behaviors or patterns, thematic takeaways from open-ended feedback or interviews, qualitative comparisons between conditions/interfaces ("participants preferred X because..."), notable participant quotes/reactions the authors themselves reported.
   - **Quantitative findings** (also relevant, but secondary to qualitative when you have to choose what to include or space is tight): statistically significant effects, performance numbers, before/after or between-condition comparisons. For these, the actual number or statistic IS the finding — always keep it in the quote (e.g. "43% faster, t(14)=3.2, p<.01"), never let the quote say only "significantly faster" with the number dropped.
4. **Exclude**:
   - Pure methodology/procedure/setup description (task design, participant demographics, apparatus, experimental conditions) that isn't itself a finding — that's what was DONE, not what was FOUND.
   - Don't try to cover the same ground as an "interface issue" framing (that's a different, sibling extraction pass over this same corpus). A "problem the interface had" and "a result the study found" often describe the same underlying passage from two angles — that overlap is fine and expected, you don't need to avoid it, just frame the title and quote around what was OBSERVED/MEASURED rather than what was WRONG.
5. Write a one-sentence, plain-English TITLE for each result in your own words (not a quote) — this is what a reader skims first, so make it concrete and specific to this finding (not generic). For quantitative results, work the key number into the title itself when it's the headline fact (e.g. "Task completion was 43% faster with the shared display" rather than "The shared display improved performance").
6. Attach 1-3 VERBATIM quotes per result, copied EXACTLY character-for-character from the markdown file (do not paraphrase, do not fix typos, preserve PDF-extraction artifacts like ligatures if present; include ellipses "..." only if you are genuinely joining two non-adjacent quoted spans — never alter wording, and never drop a statistic/number to shorten a quote). Keep each quote reasonably short (1-4 sentences) — pick the most load-bearing sentence(s), not whole paragraphs.
7. It's fine for one article to yield anywhere from 1 to 20 result cards. It's also fine to combine closely related sub-findings into one card, or split one summary sentence into two cards if the article reports genuinely distinct findings. If an article's results are ALL pure methodology after filtering (rare, but possible for a thin or unusual write-up), return an empty results array for it rather than forcing weak cards.

## Articles to process

{FOR EACH ARTICLE:}
### Article {i}
article_id: {article_id}
source_file: {source_file}
results_summary (paraphrased guide, NOT to be quoted): "{results_summary text from article_meta.json}"

## Output format
Return ONLY a JSON array (inside a ```json code block), no other commentary, matching exactly this schema:

​```json
[
  {
    "article_id": "{first article_id}",
    "results": [
      { "title": "One-sentence plain-English summary of the finding", "quotes": ["Verbatim quote 1 from the markdown.", "Verbatim quote 2 if needed."] }
    ]
  },
  ...
]
​```

Double check every quote is character-for-character accurate by re-reading the source before finalizing.
```

---

## After the subagents return

Save each subagent's JSON array to its own file (e.g. `batch1.json`, `batch2.json`, ...) in your scratch/workspace directory — copy the JSON out of the subagent's final message exactly as returned. Then run `scripts/merge_batches.py` to combine them into `results_data.json` and cross-check that every in-scope article_id got covered (see SKILL.md Step 3).

## Why this wording (context if you need to adapt it)

- **"NOT a coding task... must not write or edit any files"** — keeps the subagent from wandering into implementation and wasting its budget; it only needs to read and report.
- **Qualitative findings listed first, quantitative "secondary when you have to choose"** — directly reflects what the user asked for: both matter, but qualitative gets priority. Without this ordering, a subagent tends to default to whatever's easiest to spot (usually a p-value in a results table) and under-mine the qualitative, interview/open-feedback-shaped findings that take more reading to surface.
- **"the number IS the finding... never drop it"** — the single biggest quality risk for quantitative cards specifically. A subagent asked to write a "plain-English title" will happily produce "participants performed significantly better," which is true of almost every published result and tells a whiteboard-viewer nothing — the number is what makes it comparable across cards.
- **The methodology-vs-finding distinction in step 4** — same shaped problem as the issues skill's methodological-caveat filter, but pointed the other way: there, generic caveats had to be excluded; here, generic setup description has to be excluded. Both exist because a subagent given the whole article will happily lift the easiest-to-find sentence rather than the one that's actually a reported outcome.
- **The note about overlapping with the issues-skill's territory** — without this, a subagent second-guesses itself into narrowing scope to avoid "duplicating" the other skill, which isn't necessary or wanted; the two skills read the same source text through different lenses on purpose.
- **Batch size ~5 articles** — balances subagent context (reading 5 full markdown articles plus writing considered output) against total wall-clock time; more articles per batch risks the subagent skimming rather than reading closely. Same reasoning as `figjam-issue-cards`.
