"""
Step 2 of the figjam-issue-cards pipeline.

Merges the per-batch JSON arrays returned by the quote-extraction subagents
(see references/quote_extraction_prompt.md) into one issues_data.json, and
cross-checks the result against article_meta.json so a batch that silently
dropped an article -- or a subagent that returned a slightly wrong
article_id -- gets caught here instead of surfacing later as a missing card
set with no explanation.

Usage:
    python merge_batches.py --batches-dir <dir of batch*.json files> \
        --article-meta <path/to/article_meta.json> --out <path/to/issues_data.json>
"""
import argparse
import json
from pathlib import Path


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--batches-dir", required=True, help="Directory containing batch*.json files")
    ap.add_argument("--article-meta", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    batches_dir = Path(args.batches_dir)
    batch_files = sorted(batches_dir.glob("batch*.json"))
    if not batch_files:
        raise SystemExit(f"No batch*.json files found in {batches_dir}")

    merged = {}
    total_cards = 0
    for bf in batch_files:
        batch = json.loads(bf.read_text(encoding="utf-8"))
        for entry in batch:
            aid = entry["article_id"]
            if aid in merged:
                raise ValueError(f"duplicate article_id '{aid}' (in {bf.name}, already seen in an earlier batch)")
            merged[aid] = {"issues": entry["issues"]}
            total_cards += len(entry["issues"])

    article_meta = json.loads(Path(args.article_meta).read_text(encoding="utf-8"))
    expected_ids = {a["article_id"] for a in article_meta}
    got_ids = set(merged.keys())
    missing = expected_ids - got_ids
    extra = got_ids - expected_ids

    print(f"Merged {len(batch_files)} batch file(s): {len(merged)} articles, {total_cards} total issue cards.")
    if missing:
        print(f"WARNING -- {len(missing)} in-scope article_id(s) never showed up in any batch: {sorted(missing)}")
        print("  These articles were likely dropped from a subagent's batch assignment -- re-run extraction for them.")
    if extra:
        print(f"WARNING -- {len(extra)} article_id(s) in the batches aren't in article_meta.json: {sorted(extra)}")
        print("  Likely a typo'd article_id from a subagent -- check the batch file and fix before trusting the merge.")

    empty = [aid for aid, v in merged.items() if not v["issues"]]
    if empty:
        print(f"Articles with zero issue cards (expected for some -- e.g. purely methodological limitations): {empty}")

    Path(args.out).write_text(json.dumps(merged, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Wrote {args.out}")

    if missing or extra:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
