"""
Compound the coded-article JSON records in coded_articles/ into pandas DataFrames.

Produces two DataFrames:

  long_df  -- tidy/"long" format: one row per (article, codebook, dimension,
              code assignment). This is the source of truth; every other view
              is derived from it. Handles multi-label dimensions (a dimension
              can have several codes per article, e.g. one per experimental
              condition) without losing information.

  wide_df  -- one row per article, one column per (codebook, dimension) label.
              When a dimension has multiple codes for an article (e.g. from
              different conditions), they are combined into a single
              " + "-joined string so the DataFrame stays one-row-per-article.
              Only short/categorical fields are included -- long free-text
              fields (summaries, justifications, citation title/authors, ...)
              are deliberately left out.

Re-run this script (`python analysis/build_dataframe.py`) any time new JSONs
are added to coded_articles/ -- it always rebuilds from scratch, so there is
no incremental state to go stale. Results are cached to analysis/data/ as CSV.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

import pandas as pd

ROOT_DIR = Path(__file__).resolve().parent.parent
CODED_DIR = ROOT_DIR / "coded_articles"
DATA_DIR = Path(__file__).resolve().parent / "data"

LONG_CSV = DATA_DIR / "corpus_long.csv"
WIDE_CSV = DATA_DIR / "corpus_wide.csv"


def _clean_code(code: str) -> str:
    """Strip trailing parenthetical free-text detail from a code so that
    e.g. 'Other / Not Listed (learnability, inferred from ...)' becomes the
    canonical category 'Other / Not Listed' instead of a one-off unique string.
    """
    return re.sub(r"\s*\([^)]*\)\s*$", "", code or "").strip()


def load_records(coded_dir: Path = CODED_DIR) -> list[tuple[Path, dict]]:
    """Load every coded-article JSON (skipping index.json)."""
    records = []
    for path in sorted(coded_dir.glob("*.json")):
        if path.name == "index.json":
            continue
        with open(path, encoding="utf-8") as f:
            records.append((path, json.load(f)))
    return records


def build_long_dataframe(coded_dir: Path = CODED_DIR) -> pd.DataFrame:
    """One row per code assignment: article_id, year, codebook, dimension,
    code, condition. This is the tidy format used for count plots (group by
    codebook/dimension/code and count distinct article_id)."""
    rows: list[dict] = []

    for path, rec in load_records(coded_dir):
        article_id = rec["article_id"]
        year = rec.get("citation", {}).get("year")

        # --- top-level study_type block (sits outside "classification") ---
        st = rec.get("study_type", {})
        if st.get("primary"):
            rows.append(dict(article_id=article_id, year=year, codebook="study_type",
                              dimension="primary", code=st["primary"], condition=None))
        if st.get("secondary"):
            rows.append(dict(article_id=article_id, year=year, codebook="study_type",
                              dimension="secondary", code=st["secondary"], condition=None))
        sub = st.get("sub_attributes") or {}
        if sub.get("setting"):
            rows.append(dict(article_id=article_id, year=year, codebook="study_type",
                              dimension="setting", code=sub["setting"], condition=None))
        for c in sub.get("measured_constructs") or []:
            rows.append(dict(article_id=article_id, year=year, codebook="study_type",
                              dimension="measured_constructs", code=_clean_code(c), condition=None))
        for c in sub.get("modality_flags") or []:
            rows.append(dict(article_id=article_id, year=year, codebook="study_type",
                              dimension="modality_flags", code=_clean_code(c), condition=None))

        # --- summary.template ("user_study" / "abstract_only") ---
        template = rec.get("summary", {}).get("template")
        if template:
            rows.append(dict(article_id=article_id, year=year, codebook="summary",
                              dimension="template", code=template, condition=None))

        # --- classification block: "<codebook>_v<version>" -> dimension -> [assignments] ---
        for codebook, dims in rec.get("classification", {}).items():
            for dimension, assignments in dims.items():
                for a in assignments:
                    code = _clean_code(a.get("code", ""))
                    if not code:
                        continue
                    rows.append(dict(
                        article_id=article_id,
                        year=year,
                        codebook=codebook,
                        dimension=dimension,
                        code=code,
                        condition=a.get("condition"),
                    ))

    return pd.DataFrame(rows, columns=["article_id", "year", "codebook", "dimension", "code", "condition"])


def build_wide_dataframe(long_df: pd.DataFrame) -> pd.DataFrame:
    """One row per article. Each (codebook, dimension) pair becomes a column
    named '<codebook>__<dimension>'. Multiple codes for the same article+
    dimension (e.g. one per condition) are combined into a single
    ' + '-joined string of the unique codes."""
    if long_df.empty:
        return pd.DataFrame(columns=["article_id", "year"])

    def combine(codes: pd.Series) -> str:
        return " + ".join(sorted(set(codes)))

    pivot = (
        long_df.groupby(["article_id", "codebook", "dimension"])["code"]
        .apply(combine)
        .unstack(["codebook", "dimension"])
    )
    pivot.columns = [f"{codebook}__{dimension}" for codebook, dimension in pivot.columns]
    wide = pivot.reset_index()

    year_lookup = long_df.groupby("article_id")["year"].first()
    wide.insert(1, "year", wide["article_id"].map(year_lookup))

    return wide.sort_values(["year", "article_id"]).reset_index(drop=True)


def build_dataframe(coded_dir: Path = CODED_DIR, save: bool = True) -> tuple[pd.DataFrame, pd.DataFrame]:
    """Rebuild both DataFrames from the JSONs in coded_dir. Always rebuilds
    from scratch (cheap at this corpus size), so calling this again after
    adding/editing JSONs picks up the changes automatically."""
    long_df = build_long_dataframe(coded_dir)
    wide_df = build_wide_dataframe(long_df)

    if save:
        DATA_DIR.mkdir(parents=True, exist_ok=True)
        long_df.to_csv(LONG_CSV, index=False)
        wide_df.to_csv(WIDE_CSV, index=False)

    return wide_df, long_df


def _report_dimension_name_drift(long_df: pd.DataFrame) -> None:
    """Warn about dimensions whose name only appears for a handful of
    articles -- often a sign the same dimension was coded under slightly
    different key names across sessions (e.g. 'team_size' vs
    'team_structure_team_size'), which will fragment the wide DataFrame."""
    counts = long_df.groupby(["codebook", "dimension"])["article_id"].nunique()
    total_articles = long_df["article_id"].nunique()
    sparse = counts[counts < max(2, total_articles * 0.15)]
    if not sparse.empty:
        print("\nNote: these (codebook, dimension) pairs appear in very few articles "
              "-- check for naming drift across coded JSONs:")
        for (codebook, dimension), n in sparse.items():
            print(f"  {codebook} / {dimension}: {n} article(s)")


if __name__ == "__main__":
    wide_df, long_df = build_dataframe()
    print(f"Loaded {long_df['article_id'].nunique()} articles from {CODED_DIR}")
    print(f"long_df: {long_df.shape[0]} rows x {long_df.shape[1]} cols -> {LONG_CSV}")
    print(f"wide_df: {wide_df.shape[0]} rows x {wide_df.shape[1]} cols -> {WIDE_CSV}")
    _report_dimension_name_drift(long_df)
