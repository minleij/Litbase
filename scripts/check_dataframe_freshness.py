#!/usr/bin/env python3
"""
Check whether analysis/data/corpus_{long,wide}.csv are up to date with coded_articles/*.json.

build_dataframe.py always rebuilds both CSVs from scratch and has no incremental
state (see its own docstring), so "up to date" here just means: no coded-article
JSON has been added or modified more recently than the CSVs were last built.

Usage:
    python scripts/check_dataframe_freshness.py [project_root]

Exits non-zero if the CSVs need rebuilding.
"""

import sys
from pathlib import Path

from _pipeline_common import find_project_root

CSV_NAMES = ["corpus_long.csv", "corpus_wide.csv"]


def main() -> int:
    start = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path.cwd()
    project_root = find_project_root(start)

    coded_dir = project_root / "coded_articles"
    data_dir = project_root / "analysis" / "data"

    json_files = [f for f in coded_dir.glob("*.json") if f.name != "index.json"]
    if not json_files:
        print("OK    no coded_articles/ records yet -- nothing to build")
        return 0

    csv_paths = [data_dir / name for name in CSV_NAMES]
    missing = [p for p in csv_paths if not p.exists()]
    if missing:
        print(f"STALE analysis/data/: {', '.join(p.name for p in missing)} missing")
        print("      -> run: python analysis/build_dataframe.py")
        return 1

    oldest_csv_mtime = min(p.stat().st_mtime for p in csv_paths)
    newer_json = [f for f in json_files if f.stat().st_mtime > oldest_csv_mtime]

    if newer_json:
        newest = max(newer_json, key=lambda p: p.stat().st_mtime)
        print(
            f"STALE analysis/data/*.csv: {len(newer_json)} coded_articles record(s) "
            f"changed since the last build (newest: {newest.name})"
        )
        print("      -> run: python analysis/build_dataframe.py")
        return 1

    print("OK    analysis/data/*.csv up to date with coded_articles/")
    return 0


if __name__ == "__main__":
    sys.exit(main())
