#!/usr/bin/env python3
"""
Check whether analysis/figures/ are up to date with analysis/data/corpus_*.csv.

visualize.py has no incremental state either, so the primary check here is the
same shape as check_dataframe_freshness.py: has the data been rebuilt more
recently than the figures were last generated.

Separately (informational only, not a staleness failure): visualize.py renders
one count-plot set per codebook version actually present in the corpus data, so
e.g. task_environment_v0.8__*.png and task_environment_v0.9__*.png can validly
coexist while the corpus is only partly recoded onto v0.9 -- that is NOT stale.
What *would* be worth a look is a version-tagged figure whose version no longer
appears in ANY current coded_articles record (i.e. every article that used to be
at that version has since been recoded away, so the old figure is now an orphan
that visualize.py will never regenerate or remove on its own, since it doesn't
clear its output directory before writing). That comparison is against what's
actually in coded_articles/, not just "older than the current codebook file" --
using the codebook file version alone would false-positive on every normal
mixed-version corpus.

Usage:
    python scripts/check_figures_freshness.py [project_root]

Exits non-zero only for true staleness (figures older than the data); orphaned
version-tagged figures are printed as INFO and don't affect the exit code.
"""

import json
import re
import sys
from pathlib import Path

from _pipeline_common import find_project_root

CSV_NAMES = ["corpus_long.csv", "corpus_wide.csv"]
FIGURE_VERSION_RE = re.compile(r"(?P<key>[a-z_]+)_v(?P<major>\d+)\.(?P<minor>\d+)__")


def versions_in_use(coded_dir: Path) -> dict:
    """{short_key: set of (major, minor) tuples} stamped across current coded_articles records."""
    in_use: dict = {}
    for f in coded_dir.glob("*.json"):
        if f.name == "index.json":
            continue
        try:
            with open(f, "r", encoding="utf-8") as fh:
                record = json.load(fh)
        except (json.JSONDecodeError, OSError):
            continue
        stamped = record.get("extraction_metadata", {}).get("codebook_versions", {})
        for key, version_str in stamped.items():
            nums = tuple(int(p) for p in re.findall(r"\d+", version_str))
            if len(nums) >= 2:
                in_use.setdefault(key, set()).add(nums[:2])
    return in_use


def main() -> int:
    start = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path.cwd()
    project_root = find_project_root(start)

    data_dir = project_root / "analysis" / "data"
    figures_dir = project_root / "analysis" / "figures"
    coded_dir = project_root / "coded_articles"

    csv_paths = [data_dir / name for name in CSV_NAMES]
    existing_csvs = [p for p in csv_paths if p.exists()]
    if not existing_csvs:
        print("OK    no analysis/data/*.csv yet -- nothing to check figures against")
        return 0

    figure_files = list(figures_dir.rglob("*.png"))
    if not figure_files:
        print("STALE analysis/figures/: no figures generated yet")
        print("      -> run: python analysis/visualize.py")
        return 1

    exit_code = 0

    newest_csv = max(existing_csvs, key=lambda p: p.stat().st_mtime)
    older_figures = [f for f in figure_files if f.stat().st_mtime < newest_csv.stat().st_mtime]
    if older_figures:
        print(
            f"STALE analysis/figures/: data rebuilt ({newest_csv.name}) more recently "
            f"than {len(older_figures)} figure(s)"
        )
        print("      -> run: python analysis/visualize.py")
        exit_code = 1
    else:
        print("OK    analysis/figures/ up to date with analysis/data/")

    in_use = versions_in_use(coded_dir)
    orphaned: dict = {}
    for f in figure_files:
        m = FIGURE_VERSION_RE.search(f.name)
        if not m:
            continue
        key = m.group("key")
        version = (int(m.group("major")), int(m.group("minor")))
        if key in in_use and version not in in_use[key]:
            orphaned.setdefault((key, version), []).append(f)

    for (key, version), files in sorted(orphaned.items()):
        print(
            f"INFO  analysis/figures/: {len(files)} figure(s) tagged {key}_v{version[0]}.{version[1]} "
            f"but no current coded_articles record uses that version anymore"
        )
        print("      -> likely safe to delete once you've confirmed nothing still needs them")

    return exit_code


if __name__ == "__main__":
    sys.exit(main())
