---
name: analytic-coding
description: First analytic step in the HSI/HRI (human-swarm/human-robot interaction) literature review workflow. Takes one article (typically already converted to Markdown) and produces a structured JSON record for it — classifying its study type, extracting a study-type-appropriate free-text summary (Task/Control/Participants/Results/Issues/Recommendations/Autonomous Capabilities for anything with a user study, a paraphrased abstract otherwise), and coding it against the project's living HSI/HRI classification codebooks. Use this any time the user wants to "code," "classify," "extract info from," "add to the corpus/database," or "run through the pipeline" a new article for this literature review — even if they just paste a filename or say "do the next one" — and any time they ask about coding conventions, the JSON schema, flagged/unclear codes, or the coded_articles corpus. Do not use for general-purpose summarization of unrelated PDFs/articles outside this project, or for writing the review itself.
---

# Analytic Coding (HSI/HRI Literature Review)

## What this skill does and why it's structured this way

This skill turns one article into one structured JSON record, so that a corpus of many articles can eventually be queried, filtered, and analyzed as data rather than re-read one at a time. Because the project's classification codebooks are themselves living documents that get revised as new articles surface new cases, this skill is deliberately split into small, swappable pieces rather than one long procedure: the codebooks live in the project (not inside this skill) and are always read fresh; the rules for *how* to use a codebook are factored into one shared reference so they don't need repeating for every codebook; and the free-text summary format branches by study type via small template files. This means adding a new codebook, or a new summary template for a new study type, later is a matter of adding one file — not rewriting this one.

Read this whole file before starting. Load the reference files named at each step only when you reach that step — don't front-load everything, since the codebooks especially can be long and only some of their sections matter for a given article.

## Step 0 — Locate the article and the current codebooks

1. Find the article's Markdown file. If the user references a PDF or other format instead, convert or locate the Markdown version first — do not code from a format you haven't actually read.
2. Find the current version of each codebook that this skill applies, by searching the project for filenames matching:
   - `HSI_HRI_Study-Type_Classification_Codebook_v*`
   - `HSI_HRI_Task-Environment_Classification_Codebook_v*` (this supersedes any older standalone `Classification_Codebook` file without a version suffix in its filename — if both exist, use the versioned one and mention the discrepancy to the user)
3. If more than one version of a codebook exists, use the highest version number and note which version you used in the output record — this matters later if the codebook is revised again and old records need to be identified for re-coding.

## Step 1 — Read the shared application rules

Read `references/codebook-application-guide.md` now if you haven't already this session. It defines rules that apply to *every* codebook used in this skill (evidence requirements, how to handle Not Applicable / Not Described / Unclear cases, citation format, and — importantly — that you propose but never silently finalize new or revised codes). Apply these rules throughout Steps 2 and 4 below; they're written once here rather than repeated per codebook.

## Step 2 — Classify study type

Apply the Study-Type codebook you located in Step 0, following its own decision procedure (its Section 3.12) and the shared rules from Step 1. Produce:
- Primary code, and Secondary code if the article genuinely combines two contributions at comparable weight.
- If User Study is the Primary **or** Secondary code (the codebook's research-aim priority rule means this includes even a handful of informal participant comments), its three sub-attributes: Setting, Measured Construct(s), Study Modality Flags.
- A one- to two-sentence, paraphrased justification.

This determines which summary template you use next — check specifically whether User Study applies at all (primary or secondary), not just whether it's the Primary code.

## Step 3 — Extract the free-text summary

- **If User Study applies (primary or secondary) →** use `references/summary-templates/user-study.md`. This is almost always the relevant case for this project's research aim, so read that template carefully — it explains why Issues and Recommendations are the fields worth spending the most care on.
- **If no User Study component was found at all →** use `references/summary-templates/abstract-only.md`.

## Step 4 — Apply the Task-Environment classification codebook

Apply the Task-Environment codebook located in Step 0, dimension by dimension, using the shared rules from `references/codebook-application-guide.md`. Work through every dimension the codebook defines; for each, either assign the supported code(s) with a paraphrased justification, or mark it Not Applicable / Not Described / Unclear per the shared guide — don't skip a dimension silently.

As more codebooks are added to this project (the companion codebook already anticipates this — e.g. a possible future SA-measurement or finer-grained human-involvement dimension), each gets its own step here and its own key in the output JSON's `classification` object. Ask the user if you're unsure whether a newly-added codebook file is meant to be applied at this step or represents a different kind of coding pass.

## Step 5 — Assemble and write the JSON record

Build one JSON object following this skill's `schemas/article_record.schema.json` (path relative to this SKILL.md's own folder — this skill lives at `.claude/skills/analytic-coding/` within the project, so the full path is `.claude/skills/analytic-coding/schemas/article_record.schema.json`).

Write the record to `coded_articles/<article_id>.json` at the **project root** — the top-level project directory (the one containing `articles/` and `.claude/`), not anywhere under `.claude/skills/analytic-coding/`. `article_id` is `<first_author_lastname>_<year>_<short_slug>` (lowercase, underscores, e.g. `williamson_2023_command_control_swarm`). Before writing, confirm where the project root actually is (e.g. by locating the sibling `articles/` directory containing the source Markdown files) rather than assuming the current working directory — do not write `coded_articles/` anywhere under `.claude/skills/analytic-coding/`. Then:

1. Run `scripts/validate_record.py` (also under this skill's own folder, `.claude/skills/analytic-coding/scripts/`) against the new file to check it against the schema before treating it as done. Fix and re-validate if it fails — don't hand the user an unvalidated record.
2. Update (or create) `coded_articles/index.json` at the project root, a flat manifest array with one entry per coded article: `{article_id, title, year, study_type_primary, file}`. This is what lets the user (or a future script) browse or filter the whole corpus without opening every record. Append to it; don't regenerate it from scratch each time, so you don't clobber entries from articles coded in earlier sessions unless the user asks you to rebuild it.
3. If `coded_articles/` or `index.json` doesn't exist yet at the project root, create it there — this is normal for the first article coded in a project.

## Step 6 — Report back to the user

After writing the file, tell the user in chat (not just in the JSON):
- The assigned study type (primary/secondary) in one line.
- Any Not Applicable / Not Described / Unclear-Candidate-New-Code flags raised during Step 4, each with what prompted it and a proposed code/definition if you have one — per the shared application guide, these are for the user to decide on, not for you to resolve unilaterally.
- Where the file was written.

Do not reproduce more than a short (<15 word) verbatim phrase from the source article anywhere in the summary, justifications, or JSON fields — paraphrase throughout, consistent with the codebooks' own citation rules.

## Coding multiple articles

If asked to code a batch, run Steps 0–6 once per article, but only read the codebooks and `codebook-application-guide.md` once per session (they don't change between articles in the same batch) — re-reading them for every single article wastes context for no benefit. Re-check the codebook filenames once at the start of the batch, not per-article.
