# Quote-extraction subagent prompt template

This is the step in the pipeline that genuinely needs judgment (deciding what counts as a human-centered/interface issue, and locating the exact sentence that supports it) rather than a deterministic script — so it runs as parallel research subagents, not code. Use the `Agent` tool with `subagent_type: general-purpose`, one call per batch of ~5 articles, all launched in the same message so they run concurrently. Set `run_in_background: true` for each and wait for the completion notifications rather than polling.

Fill in the `{...}` placeholders below per batch and use the result as the subagent's `prompt`. Keep the instructional text itself intact — it encodes real lessons (see "Why this wording" below) rather than boilerplate.

---

```
You are doing factual research extraction for a literature review project at {PROJECT_ROOT}. This is NOT a coding task — you must not write or edit any files. You only need to read files and return a JSON answer in your final message.

## Background
The project has coded human-swarm-interaction (HSI/HRI) research articles. Each article has a markdown source file under `articles/`, and a structured JSON coding record under `coded_articles/`. The JSON record has a `summary.issues` field with a PARAPHRASED list of reported issues for that article — but we now need the ACTUAL VERBATIM sentences/passages from the article's markdown text that back up each of those issues, because these will become quote-cards on a design board.

## Your task
For each of the {N} articles below, do the following:
1. Read the markdown source file (path given).
2. Using the given `issues_summary` as a checklist/guide of what issues were already identified, locate the actual verbatim text in the markdown that discusses each issue (usually in Results, Discussion, or Limitations sections).
3. Only keep issues that are about **interface design, usability, or other human-centered factors** — e.g. confusing/cluttered displays, missing or unwanted UI features, workload/cognitive-load problems tied to the interface or task structure, situation-awareness or trust breakdowns caused by the interface or automation behavior, communication/coordination problems between operators mediated by the interface, control/input mapping problems, information-overload or alerting problems, accessibility problems, learnability/training problems with the interface.
4. **Exclude** issues that are purely generic methodological/statistical caveats with no interface angle (e.g. "small sample size", "no inferential statistics were run", "non-representative sample", "results may not generalize" said with no connection to a specific interface/design element). When in doubt about a borderline case (e.g. "even the best interface could not compensate for missing sensor hardware"), keep it if it says something about the interface's role, scope, or a design tradeoff.
5. Write a one-sentence, plain-English TITLE for each issue in your own words (not a quote) — this is what a reader skims first, so make it concrete and specific to this issue (not generic).
6. Attach 1-3 VERBATIM quotes per issue, copied EXACTLY character-for-character from the markdown file (do not paraphrase, do not fix typos, preserve PDF-extraction artifacts like ligatures if present; include ellipses "..." only if you are genuinely joining two non-adjacent quoted spans — never alter wording). Keep each quote reasonably short (1-4 sentences) — pick the most load-bearing sentence(s), not whole paragraphs.
7. It's fine for one article to yield anywhere from 1 to 20 issue cards. It's also fine to combine closely related sub-points into one card, or split one summary sentence into two cards if the article discusses genuinely distinct problems. If an article's issues are ALL purely methodological after filtering, return an empty issues array for it rather than forcing weak cards.

## Articles to process

{FOR EACH ARTICLE:}
### Article {i}
article_id: {article_id}
source_file: {source_file}
issues_summary (paraphrased guide, NOT to be quoted): "{issues_summary text from article_meta.json}"

## Output format
Return ONLY a JSON array (inside a ```json code block), no other commentary, matching exactly this schema:

​```json
[
  {
    "article_id": "{first article_id}",
    "issues": [
      { "title": "One-sentence plain-English summary of the issue", "quotes": ["Verbatim quote 1 from the markdown.", "Verbatim quote 2 if needed."] }
    ]
  },
  ...
]
​```

Double check every quote is character-for-character accurate by re-reading the source before finalizing.
```

---

## After the subagents return

Save each subagent's JSON array to its own file (e.g. `batch1.json`, `batch2.json`, ...) in your scratch/workspace directory — copy the JSON out of the subagent's final message exactly as returned. Then run `scripts/merge_batches.py` to combine them into `issues_data.json` and cross-check that every in-scope article_id got covered (see SKILL.md Step 3).

## Why this wording (context if you need to adapt it)

- **"NOT a coding task... must not write or edit any files"** — keeps the subagent from wandering into implementation and wasting its budget; it only needs to read and report.
- **The explicit include/exclude list in steps 3-4** — the single biggest quality lever in this whole pipeline. Without it, a subagent will happily turn "small sample size" into a card, which produces a board full of noise the user explicitly doesn't want (they clarified: "I do not care what type of study the study is, as long as issues of a specific interface are identified").
- **"copied EXACTLY character-for-character... do not paraphrase"** — the whole point of quoting is that the reader can trust the card without re-opening the source PDF. A paraphrase defeats that, even a good one.
- **Batch size ~5 articles** — balances subagent context (reading 5 full markdown articles plus writing considered output) against total wall-clock time; more articles per batch risks the subagent skimming rather than reading closely.
