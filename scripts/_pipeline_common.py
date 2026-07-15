"""Shared helper for the pipeline-freshness scripts in this directory."""

from pathlib import Path


def find_project_root(start: Path) -> Path:
    """Walk up from `start` looking for a directory containing both 'articles/'
    and 'coded_articles/' as siblings -- the project root, same landmark the
    analytic-coding skill's own scripts use."""
    for candidate in [start, *start.parents]:
        if (candidate / "articles").is_dir() and (candidate / "coded_articles").is_dir():
            return candidate
    raise SystemExit(
        f"Could not find a project root (a directory containing both 'articles/' and "
        f"'coded_articles/') starting from {start}. Pass the project root explicitly."
    )
