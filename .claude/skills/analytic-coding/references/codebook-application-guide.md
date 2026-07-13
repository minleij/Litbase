# Codebook Application Guide

This file defines rules that apply whenever this skill applies *any* classification codebook — the Study-Type codebook in Step 2 and the Task-Environment codebook in Step 4, and any codebook added to this project later. It exists as a separate file so that adding a new codebook to the workflow doesn't mean duplicating these rules again; the codebook-specific file only needs to define its own dimensions and codes, and this guide covers how to use them.

These rules are drawn directly from the codebooks' own "How a Classifying Model Should Use This Codebook" sections — they're collected here because both codebooks converged on essentially the same rules independently, which is a good sign they're the right defaults for any future codebook too.

## Evidence requirement

Base every code on the article's actual stated contribution, methodology, and described text — the abstract, introduction, methods, and results sections are the primary evidence. Do not infer a code from a title, keyword list, or venue alone, and do not infer a code from what a system of that general type *usually* does elsewhere in the literature. If you can't point to a passage that supports a code, you don't have enough to assign it yet.

## Not Applicable vs. Not Described — these are different findings, don't merge them

- **Not Applicable**: the dimension doesn't conceptually apply to this kind of system at all (e.g., Coordination Architecture for an article about a single robot; Operational Domain for a purely theoretical study with no deployment context).
- **Not Described**: the dimension plausibly applies, but the article's text just doesn't say enough to code it (e.g., the article studies multiple robots, so coordination conceptually applies, but never describes how they coordinate).

Both are legitimate, useful outcomes — they tell a future reader different things about the corpus ("this doesn't apply to this kind of work" vs. "this would be interesting to know but wasn't reported"), so don't collapse them into one tag and don't force a best-guess code just to avoid using either.

## Unclear / Candidate New Code

If an article describes something that doesn't cleanly map onto any existing code — not just an awkward fit at the seam between two codes, which the codebook's own "Distinguish from" notes are meant to resolve, but a genuine gap — assign "Unclear / Candidate New Code." Describe the construct in a short note, and propose a name and draft definition if one comes to mind.

**Do not resolve this yourself by stretching an existing code's definition, and do not add a new code to the codebook document on your own authority.** The codebook is a living document maintained by the user; your job is to flag the gap clearly (see Step 6 of `SKILL.md`) so they can decide whether to widen a definition, add a code, or treat it as a one-off. This is the same process that has already produced several of the amendments visible in these codebooks' own change logs — it's expected to keep happening as the corpus grows, not a sign something went wrong.

## Justification and citation format

Report each code assignment as: **code assigned → one- to two-sentence justification, paraphrased, with a page/section reference if available.** Never reproduce more than a short (<15 word) verbatim phrase from the source article when justifying a code — paraphrase the reasoning instead of quoting it.

## Multiple codes and conditions

Some dimensions genuinely allow more than one code for a single article — e.g., an article that tests several experimental conditions may warrant more than one Task-Object code, one per condition. When this happens, assign every code the text supports and note which condition or experiment each applies to, rather than forcing a single choice. Check each codebook's own text for whether a given dimension is single-select or multi-select — this varies by dimension, not just by codebook.

## Definitions are authoritative

A codebook's definitions of its own terms (e.g., what "distributed," "autonomous," or "user study" means *in this project*) take precedence over your own general-language associations with those words. Read each code's definition and "Distinguish from" notes before assigning it, even for terms that seem self-explanatory.
