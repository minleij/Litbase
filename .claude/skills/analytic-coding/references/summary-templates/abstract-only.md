# Summary Template: Abstract-Only

Use this template only when no User Study component was found at all in Step 2 — neither as a Primary nor Secondary code. This covers articles like pure algorithm/simulation papers, surveys, frameworks, position papers, and system/architecture papers with zero reported human interaction.

## What to write

Write a short, **paraphrased** summary of the article's abstract — typically two to four sentences covering the article's stated contribution, method, and headline finding or conclusion. This is deliberately lighter-weight than the User Study template: for these article types, the abstract usually already does a good job of summarizing the piece, so the goal here is a clean paraphrase for the corpus record, not a fresh from-scratch analysis.

Do not reproduce the abstract verbatim, even in part beyond a short (<15 word) phrase — rewrite it in your own words. This keeps the corpus internally consistent in style with the User Study summaries (which are inherently the coder's own synthesis, not copied text) and avoids reproducing more of the original article's text than necessary.

## If the article turns out to have more going on than the abstract suggests

If, while reading closely enough to write even this shorter summary, you notice something that looks like it might actually be an informal user-facing element the Study-Type codebook's Step 0 should have caught (e.g., a brief mention of "operator feedback" buried in a results section that wasn't visible from the abstract alone), stop and revisit Step 2 rather than pushing ahead with the abstract-only template — the Study-Type codebook's research-aim priority rule means this project cares more about catching those cases than about speed.

## Fields to record

Store the paraphrased summary in the `summary.abstract_summary` field of the output JSON (see `schemas/article_record.schema.json`). The `summary.template` field should be set to `"abstract_only"` so it's clear at a glance, when browsing the corpus later, which articles received the fuller extraction and which received this lighter one.
