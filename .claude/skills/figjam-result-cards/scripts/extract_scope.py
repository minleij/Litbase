"""
Step 1 of the figjam-result-cards pipeline.

Reads coded_articles/index.json + coded_articles/*.json, filters to the
requested study type(s), and writes a flat article_meta.json with just what
the rest of the pipeline needs per article: citation info, the source
markdown path, its SCATTER_DIMENSIONS codes (for chip colors), and the
summary.results text (used as a checklist by the quote-extraction subagents,
not quoted directly).

This is a near-identical port of figjam-issue-cards' extract_scope.py -- the
only functional difference is pulling summary.results instead of
summary.issues.

Usage:
    python extract_scope.py --project-root <path> --out <path/to/article_meta.json> \
        [--study-types "User Study"] [--dimension-order <path/to/dimension_order.json>]

By default only "User Study" articles are included -- other study types
(System/Architecture Paper, Meta-Review, Algorithm/Controller Evaluation,
Design/Interface Concept Paper) rarely report empirical results in the same
sense (no participants, no measured outcomes), so including them mostly
just produces empty-results entries. Pass --study-types with a comma-
separated list to widen scope if the user asks for it (e.g. "User
Study,Design/Interface Concept Paper").
"""
import argparse
import json
from pathlib import Path

DEFAULT_DIM_ORDER = Path(__file__).resolve().parent.parent / "references" / "dimension_order.json"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--project-root", required=True, help="Project root containing coded_articles/ and articles/")
    ap.add_argument("--out", required=True, help="Path to write article_meta.json")
    ap.add_argument("--study-types", default="User Study",
                     help="Comma-separated list of study_type_primary values to include")
    ap.add_argument("--dimension-order", default=str(DEFAULT_DIM_ORDER))
    args = ap.parse_args()

    root = Path(args.project_root)
    coded_dir = root / "coded_articles"
    dim_meta = json.loads(Path(args.dimension_order).read_text(encoding="utf-8"))
    dim_keys = list(dim_meta["dimensions"].keys())
    uninformative = set(dim_meta.get("uninformative_codes", ["Not Applicable", "Not Described"]))

    wanted_types = {t.strip() for t in args.study_types.split(",")}

    index = json.loads((coded_dir / "index.json").read_text(encoding="utf-8"))
    in_scope_ids = [e["article_id"] for e in index if e["study_type_primary"] in wanted_types]

    out = []
    for aid in in_scope_ids:
        rec = json.loads((coded_dir / f"{aid}.json").read_text(encoding="utf-8"))
        citation = rec["citation"]
        summary = rec.get("summary", {})
        classification = rec.get("classification", {})

        te_key = next((k for k in classification if k.startswith("task_environment_v")), None)
        dims = {}
        if te_key:
            te = classification[te_key]
            for dim in dim_keys:
                codes, seen = [], set()
                for entry in te.get(dim, []):
                    code = entry.get("code")
                    if code in uninformative or code in seen:
                        continue
                    seen.add(code)
                    codes.append(code)
                if codes:
                    dims[dim] = codes

        out.append({
            "article_id": aid,
            "authors": citation.get("authors"),
            "year": citation.get("year"),
            "title": citation.get("title"),
            "source_file": citation.get("source_file"),
            "codebook_version": te_key,
            "dims": dims,
            "results_summary": summary.get("results", ""),
        })

    Path(args.out).write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Wrote {len(out)} in-scope articles ({', '.join(sorted(wanted_types))}) to {args.out}")
    for a in out:
        n_dims = len(a["dims"])
        flag = "  [no task_environment classification found]" if not a["codebook_version"] else ""
        thin = "  [no summary.results text]" if not a["results_summary"].strip() else ""
        print(f"  {a['article_id']}: {n_dims}/{len(dim_keys)} dimensions coded{flag}{thin}")


if __name__ == "__main__":
    main()
