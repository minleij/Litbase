"""
Data visualization for the coded_articles/ corpus.

Two kinds of plots, both saved as PNGs under analysis/figures/:

1. Count plots (figures/counts/<codebook>__<dimension>.png)
   How many articles carry each code, for every coded dimension (study type,
   task type, control/autonomy level, team structure, ...). Built from the
   long/tidy DataFrame so multi-label dimensions (a dimension can have more
   than one code per article, e.g. one per experimental condition) are
   counted correctly -- each article is counted at most once per code.

2. Pairplots (figures/pairplot_<codebook>.png), one grid per codebook
   All the short categorical "label" columns are plotted against each other
   in a seaborn-pairplot-style grid (scatterplot matrix), grouped by codebook
   so each grid stays a readable size. Long free-text fields (summaries,
   justifications, citations, ...) are excluded -- see build_dataframe.py's
   wide DataFrame, which only keeps short label columns to begin with.
   Since the labels are categorical rather than numeric, this uses a
   seaborn PairGrid with jittered stripplots off-diagonal and count bars on
   the diagonal, rather than sns.pairplot (which only handles numeric data).

Run: python analysis/visualize.py
"""

from __future__ import annotations

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from build_dataframe import build_dataframe

FIG_DIR = Path(__file__).resolve().parent / "figures"
COUNTS_DIR = FIG_DIR / "counts"

NON_LABEL_COLS = {"article_id", "year"}


def plot_counts(long_df: pd.DataFrame, out_dir: Path = COUNTS_DIR) -> None:
    """One horizontal bar chart per (codebook, dimension): number of
    articles assigned each code."""
    out_dir.mkdir(parents=True, exist_ok=True)

    for (codebook, dimension), group in long_df.groupby(["codebook", "dimension"]):
        counts = group.groupby("code")["article_id"].nunique().sort_values(ascending=True)
        if counts.empty:
            continue

        height = max(2, 0.4 * len(counts) + 1)
        fig, ax = plt.subplots(figsize=(8, height))
        counts.plot.barh(ax=ax, color=sns.color_palette("viridis", len(counts)))
        ax.set_xlabel("Number of articles")
        ax.set_ylabel("")
        ax.set_title(f"{codebook} / {dimension}")
        ax.xaxis.get_major_locator().set_params(integer=True)
        fig.tight_layout()

        out_path = out_dir / f"{codebook}__{dimension}.png"
        fig.savefig(out_path, dpi=150)
        plt.close(fig)
        print(f"  wrote {out_path.relative_to(FIG_DIR.parent)}")


def _categorical_pairgrid(df: pd.DataFrame, vars_: list[str], hue: str | None, title: str):
    """A pairplot-style grid for categorical columns: jittered stripplots
    off-diagonal (co-occurrence between two label columns), bar counts on
    the diagonal (distribution of a single label column)."""
    plot_df = df[vars_ + ([hue] if hue and hue not in vars_ else [])].fillna("(not coded)")

    g = sns.PairGrid(plot_df, vars=vars_, hue=hue, height=2.0, aspect=1.1)
    g.map_offdiag(sns.stripplot, size=5, alpha=0.7, jitter=0.3)

    for ax in g.axes.flatten():
        if ax is None:
            continue
        ax.tick_params(axis="x", labelrotation=90, labelsize=7)
        ax.tick_params(axis="y", labelsize=7)

    for i, col in enumerate(vars_):
        ax = g.axes[i, i]
        counts = plot_df[col].value_counts()
        ax.barh(counts.index, counts.values, color="steelblue")
        ax.tick_params(axis="y", labelsize=7)
        ax.tick_params(axis="x", labelsize=7)

    if hue:
        g.add_legend(title=hue, bbox_to_anchor=(1.02, 0.5), loc="center left")
    g.fig.suptitle(title, y=1.02)
    return g


def plot_pairplots(wide_df: pd.DataFrame, out_dir: Path = FIG_DIR) -> None:
    """One pairplot grid per codebook (study_type, summary, task_environment_v0.8, ...)."""
    out_dir.mkdir(parents=True, exist_ok=True)
    label_cols = [c for c in wide_df.columns if c not in NON_LABEL_COLS]

    groups: dict[str, list[str]] = {}
    for col in label_cols:
        codebook = col.split("__", 1)[0]
        groups.setdefault(codebook, []).append(col)

    hue_col = "study_type__primary" if "study_type__primary" in label_cols else None

    for codebook, cols in groups.items():
        if len(cols) < 2:
            continue  # nothing to pair against
        g = _categorical_pairgrid(wide_df, cols, hue=hue_col, title=f"Pairplot: {codebook}")
        out_path = out_dir / f"pairplot_{codebook}.png"
        g.fig.savefig(out_path, dpi=150, bbox_inches="tight")
        plt.close(g.fig)
        print(f"  wrote {out_path.relative_to(FIG_DIR.parent)}")


def main() -> None:
    wide_df, long_df = build_dataframe()
    print(f"Loaded {long_df['article_id'].nunique()} articles.\n")

    print("Building count plots...")
    plot_counts(long_df)

    print("\nBuilding pairplots...")
    plot_pairplots(wide_df)


if __name__ == "__main__":
    main()
