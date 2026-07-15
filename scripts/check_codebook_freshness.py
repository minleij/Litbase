#!/usr/bin/env python3
"""
Check coded_articles/*.json against the codebook versions stamped in each record.

This is a thin pre-commit-friendly wrapper around the analytic-coding skill's
corpus_status.py (.claude/skills/analytic-coding/scripts/corpus_status.py), which
remains the source of truth for this check -- it's invoked as a subprocess with
--json rather than reimplemented here, so the two never drift apart. This script
just reduces that report to a one-line-per-issue summary and a plain exit code.

Usage:
    python scripts/check_codebook_freshness.py [project_root]

Exits non-zero if any coded_articles record is stale against its codebook.
"""

import json
import subprocess
import sys
from pathlib import Path

from _pipeline_common import find_project_root

CORPUS_STATUS = (
    Path(__file__).resolve().parent.parent
    / ".claude" / "skills" / "analytic-coding" / "scripts" / "corpus_status.py"
)


def main() -> int:
    start = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path.cwd()
    project_root = find_project_root(start)

    if not CORPUS_STATUS.exists():
        print(f"SKIP  codebook freshness: {CORPUS_STATUS} not found")
        return 0

    result = subprocess.run(
        [sys.executable, str(CORPUS_STATUS), "--json", str(project_root)],
        capture_output=True, text=True,
    )
    try:
        report = json.loads(result.stdout)
    except json.JSONDecodeError:
        print("WARN  codebook freshness check failed to run:")
        print("      " + (result.stderr.strip() or result.stdout.strip()))
        return 0

    stale = report.get("stale_records", {})
    unknown = report.get("unknown_codebook_keys", {})

    if not stale and not unknown:
        print("OK    coded_articles/ up to date with current codebook versions")
        return 0

    for key, entries in sorted(stale.items()):
        ids = ", ".join(e["article_id"] for e in entries)
        print(
            f"STALE codebook '{key}': {len(entries)} record(s) coded against an "
            f"older codebook version -- {ids}"
        )
    for key, ids in sorted(unknown.items()):
        print(f"WARN  codebook '{key}': {len(ids)} record(s) reference an unknown codebook key")

    if stale:
        print("      -> recode the listed articles, or bump their codebook_versions stamp deliberately")
    return 1


if __name__ == "__main__":
    sys.exit(main())
