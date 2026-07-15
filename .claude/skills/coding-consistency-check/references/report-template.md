# Report template

Use this structure for the markdown file written to `coding_consistency_reports/`.
Fill in every section; omit a section only if it's genuinely empty for every
article in scope (say so — "No drift found" — don't just delete the heading).

```markdown
# Coding Consistency Report

**Scope:** <article_id, or "N articles" / "whole corpus">
**Compared:** <old_ref> -> <new_ref>
**Generated:** <date>

## Summary

- Articles compared: N (M skipped — no prior version to compare yet)
- Drift needing review: N item(s)
- Version bumped, undocumented in notes: N item(s)
- Expected changes (documented): N item(s)
- Notable text/substance changes: N item(s)

## <article_id>

**Codebook versions:** `<key>`: old -> new (bumped) · `<key>`: old -> new (unchanged)

### Drift — needs review

Same codebook version both times, different code assigned. This is the signal
the skill exists to catch — surface every one of these, even if it looks minor.

- **<dimension>** (<condition, or "no condition">): `<OLD_CODE>` -> `<NEW_CODE>`
  - old: <old justification, paraphrased or quoted briefly>
  - new: <new justification, paraphrased or quoted briefly>

### Version bumped, not documented in notes

The codebook version moved and the code changed, but `extraction_metadata.notes`
doesn't mention this dimension. Probably fine (the note was just incomplete) —
worth a quick human glance, not a red flag.

- **<dimension>** (<condition>): `<OLD_CODE>` -> `<NEW_CODE>` (codebook <old_v> -> <new_v>)

### Expected changes (documented)

Codebook version moved, code changed, and the notes field explains why.

- **<dimension>** (<condition>): `<OLD_CODE>` -> `<NEW_CODE>` — per note: "<short paraphrase of the relevant note sentence>"

### Study type

- Primary: unchanged / `<old>` -> `<new>` (<expected or drift, with reason>)
- Secondary: unchanged / `<old>` -> `<new>` (<expected or drift, with reason>)
- Justification: unchanged / notably revised (<one line on what shifted, if anything>)

### Notable text changes

Wording changed enough that the substance looks different, not just phrasing.
Skip fields where the change reads as cosmetic — don't list everything that
has a nonzero diff.

- **<field>**: <one or two sentences on what actually changed in meaning>

### Newly covered / dropped conditions

Dimensions or conditions present in only one version — usually just new
codebook coverage, not drift, but call out anything that looks like a
condition silently disappeared.

- <dimension> (<condition>): added in this recode / no longer present

### Flags

- Added: <count, and any that aren't already explained above>
- Removed: <count, and any that aren't already explained above>

---

## Skipped articles

- `<article_id>`: <reason from the script's "skipped" field>
```

## Notes on filling this in

- Every "Drift" and "Version bumped, not documented" item should read clearly
  on its own — someone skimming just that section should understand what
  changed without opening the JSON files.
- Don't quote more than a sentence or two of any justification; paraphrase the
  rest, consistent with how the analytic-coding skill itself handles source
  material.
- If an article has zero differences worth reporting (script found nothing,
  or everything is cosmetic), still give it a one-line entry: "No differences
  found." Silence would be indistinguishable from the article never having
  been checked.
