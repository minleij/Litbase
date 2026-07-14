"""
Data visualization for the coded_articles/ corpus.

Two kinds of plots, both saved as PNGs under analysis/figures/:

1. Count plots (figures/counts/<codebook>__<dimension>.png)
   How many articles carry each code, for every coded dimension (study type,
   task type, control/autonomy level, team structure, ...). Built from the
   long/tidy DataFrame so multi-label dimensions (a dimension can have more
   than one code per article, e.g. one per experimental condition) are
   counted correctly -- each article is counted at most once per code.

2. Dimension scatterplots, one per pair of SCATTER_DIMENSIONS (the
   task_environment dimensions of interest). Each is a bubble chart: one
   point per (code_x, code_y) combination, marker size/color = number of
   distinct articles with that combination. A plain jittered scatter is
   unreadable here (many articles share the same code pair, and points would
   just overlap), so size-encoding the count is what actually makes
   co-occurrence between two categorical dimensions legible. Dimensions are
   coalesced across whatever task_environment_v* codebook versions are
   actually present in the corpus (highest version wins per article), since
   the corpus is not always uniformly coded at the current version. Produced
   in two variants, since an article
   can carry more than one code per dimension (e.g. one per experimental
   condition):
     - figures/scatter/<dim_x>__vs__<dim_y>.png -- multi-condition
       " + "-joined codes are exploded back into individual codes, so an
       article with codes "A + B" contributes to both the A and B rows/cols.
     - figures/scatter_combined/<dim_x>__vs__<dim_y>.png -- multi-condition
       codes are kept as their own distinct joined category ("A + B") rather
       than being split apart.
   In both variants, datapoints coded exactly "Not Described" or "Not
   Applicable" (UNINFORMATIVE_CODES) are dropped before plotting -- they
   carry no substantive information about the dimension.

Run: python analysis/visualize.py
"""

from __future__ import annotations

import itertools
import re
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from build_dataframe import build_dataframe

FIG_DIR = Path(__file__).resolve().parent / "figures"
COUNTS_DIR = FIG_DIR / "counts"
SCATTER_DIR = FIG_DIR / "scatter"
SCATTER_COMBINED_DIR = FIG_DIR / "scatter_combined"

NON_LABEL_COLS = {"article_id", "year"}

# task_environment dimensions to scatter against each other, pairwise.
SCATTER_DIMENSIONS = [
    "behavioral_relation_to_task_object",
    "communication_proximity",
    "computational_characteristics",
    "coordination_architecture",
    "interaction_model",
    "level_of_human_control_abstraction",
    "task_object_spatiotemporal_dynamics",
]

# Codes that carry no substantive information for these scatterplots -- drop
# any datapoint whose code is exactly one of these before plotting.
UNINFORMATIVE_CODES = {"Not Described", "Not Applicable"}

# Axis order for dimensions whose codes fall on one real underlying scale
# (per the Task-Environment codebook's own framing), least to most of
# whatever the scale measures. Dimensions not listed here are nominal --
# no single scale connects their codes -- and stay alphabetically sorted.
DIMENSION_ORDER: dict[str, list[str]] = {
    # User-specified ordering (not derived from the codebook, which treats
    # these as unordered nominal categories): monitor own status -> relocate
    # a known object -> find an unknown one -> track it -> act on it
    # decisively -> block an adversary from it -> steer clear of a hazard.
    "behavioral_relation_to_task_object": [
        "Monitoring/Maintenance Task",
        "Transport/Delivery Task",
        "Search Task",
        "Pursuit Task",
        "Engagement Task",
        "Defend/Block Task",
        "Avoidance Task",
    ],
    # User-specified ordering (not derived from the codebook): known/visible
    # -> discovered-but-fixed -> moving -> scattered separate instances ->
    # growing from a point.
    "task_object_spatiotemporal_dynamics": [
        "Known Fixed Task Object",
        "Static/Fixed Task Object",
        "Moving Task Object",
        "Distributed Task Object",
        "Spreading Task Object",
    ],
    # LHCA 1-5 (codebook Section 9.5): increasing operator-input granularity.
    "level_of_human_control_abstraction": [
        "Direct", "Augmented", "Parametric", "Goal-Oriented", "Mission-Capable",
    ],
    # Increasing breadth of who's connected on the receiving end.
    "interaction_model": [
        "One-to-one", "One-to-many", "Many-to-many",
    ],
    # Centralized -> decentralized (Verma et al. 2020). Hybrid explicitly
    # mixes both mechanisms rather than sitting at one point on this line,
    # so it's appended after the scale rather than placed within it.
    "coordination_architecture": [
        "Strongly Centralized Coordination",
        "Weakly Centralized Coordination",
        "Hierarchical Coordination",
        "Distributed Coordination",
        "Hybrid Coordination",
    ],
    # Binary closeness scale.
    "communication_proximity": [
        "Remote", "Proximate",
    ],
    # Tentative ordering by degree of adaptivity/data-dependence -- the
    # codebook doesn't define this as a scale, unlike LHCA above, so treat
    # this one as an interpretive judgment call rather than a codebook fact.
    # Task-Allocation is an orthogonal placeholder (answers "who", not
    # "how"), so it's appended last rather than placed within the scale.
    "computational_characteristics": [
        "Predefined / Rule-Based Control",
        "Classical Geometric / Sampling-Based Control",
        "Heuristic Search-Based Control",
        "Bio-Inspired / Metaheuristic Optimization Control",
        "Learning-Based Control",
        "Task-Allocation",
    ],
}


def _ordered_categories(codes: pd.Series, dimension: str) -> list[str]:
    """Unique codes present in `codes`, ordered per DIMENSION_ORDER[dimension]
    if that dimension has a defined scale (codes present but not listed there,
    e.g. "Unclear / Candidate New Code", are appended alphabetically at the
    end); falls back to plain alphabetical for dimensions with no defined
    order (the nominal ones)."""
    present = set(codes.unique())
    order = DIMENSION_ORDER.get(dimension)
    if not order:
        return sorted(present)
    ordered = [c for c in order if c in present]
    leftover = sorted(present - set(order))
    return ordered + leftover


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


_TASK_ENV_COL_RE = re.compile(r"^task_environment_v(?P<major>\d+)\.(?P<minor>\d+)__(?P<dim>.+)$")


def _task_env_version_cols(wide_df: pd.DataFrame, dim: str) -> list[str]:
    """All task_environment_v*__<dim> columns actually present in wide_df for
    this dimension, sorted from highest version to lowest -- so whichever
    versions the corpus happens to be coded under (possibly several at once,
    e.g. mid-recode) are all covered without hardcoding specific numbers."""
    matches = []
    for col in wide_df.columns:
        m = _TASK_ENV_COL_RE.match(col)
        if m and m.group("dim") == dim:
            matches.append((int(m.group("major")), int(m.group("minor")), col))
    matches.sort(reverse=True)
    return [col for _, _, col in matches]


def _combined_dimension_frame(wide_df: pd.DataFrame) -> pd.DataFrame:
    """One row per article, one column per SCATTER_DIMENSIONS entry, coalescing
    across every task_environment_v* version column present (highest version
    wins where an article has been coded under more than one)."""
    out = pd.DataFrame({"article_id": wide_df["article_id"]})
    for dim in SCATTER_DIMENSIONS:
        combined = pd.Series(index=wide_df.index, dtype=object)
        for col in _task_env_version_cols(wide_df, dim):
            combined = combined.combine_first(wide_df[col])
        out[dim] = combined
    return out


def plot_dimension_scatterplots(wide_df: pd.DataFrame, out_dir: Path = SCATTER_DIR,
                                 explode_multi: bool = True) -> None:
    """One bubble-chart scatterplot per pair of SCATTER_DIMENSIONS: point at
    (code_x, code_y) sized/colored by the number of distinct articles with
    that code combination.

    Multi-condition cells (" + "-joined codes, e.g. an article with both a
    centralized and a distributed condition) are exploded back into
    individual codes before counting when explode_multi=True. When False,
    each joined combination (e.g. "Distributed Coordination + Strongly
    Centralized Coordination") is kept as its own distinct category instead
    of being split apart."""
    out_dir.mkdir(parents=True, exist_ok=True)
    combined = _combined_dimension_frame(wide_df)

    for dim_x, dim_y in itertools.combinations(SCATTER_DIMENSIONS, 2):
        sub = combined[["article_id", dim_x, dim_y]].dropna(subset=[dim_x, dim_y])
        if sub.empty:
            continue
        if explode_multi:
            sub = sub.assign(**{dim_x: sub[dim_x].str.split(" + ", regex=False),
                                 dim_y: sub[dim_y].str.split(" + ", regex=False)})
            sub = sub.explode(dim_x).explode(dim_y)

        sub = sub[~sub[dim_x].isin(UNINFORMATIVE_CODES) & ~sub[dim_y].isin(UNINFORMATIVE_CODES)]
        if sub.empty:
            continue

        counts = sub.groupby([dim_x, dim_y])["article_id"].nunique().reset_index(name="count")
        x_order = _ordered_categories(counts[dim_x], dim_x)
        y_order = _ordered_categories(counts[dim_y], dim_y)
        x_pos = counts[dim_x].map({v: i for i, v in enumerate(x_order)})
        y_pos = counts[dim_y].map({v: i for i, v in enumerate(y_order)})

        fig, ax = plt.subplots(figsize=(max(6, 0.7 * len(x_order) + 2), max(5, 0.5 * len(y_order) + 2)))
        sc = ax.scatter(x_pos, y_pos, s=counts["count"] * 120, c=counts["count"],
                         cmap="viridis", alpha=0.85, edgecolor="black", linewidth=0.5)
        for xi, yi, c in zip(x_pos, y_pos, counts["count"]):
            ax.annotate(str(c), (xi, yi), ha="center", va="center", fontsize=8, color="white")

        ax.set_xticks(range(len(x_order)))
        ax.set_xticklabels(x_order, rotation=45, ha="right", fontsize=8)
        ax.set_yticks(range(len(y_order)))
        ax.set_yticklabels(y_order, fontsize=8)
        ax.set_xlim(-0.5, len(x_order) - 0.5)
        ax.set_ylim(-0.5, len(y_order) - 0.5)
        ax.set_xlabel(dim_x)
        ax.set_ylabel(dim_y)
        ax.set_title(f"{dim_y} vs. {dim_x}")
        fig.colorbar(sc, ax=ax, label="Number of articles")
        fig.tight_layout()

        out_path = out_dir / f"{dim_x}__vs__{dim_y}.png"
        fig.savefig(out_path, dpi=150)
        plt.close(fig)
        print(f"  wrote {out_path.relative_to(FIG_DIR.parent)}")


def main() -> None:
    wide_df, long_df = build_dataframe()
    print(f"Loaded {long_df['article_id'].nunique()} articles.\n")

    print("Building count plots...")
    plot_counts(long_df)

    print("\nBuilding dimension scatterplots (multi-condition codes split apart)...")
    plot_dimension_scatterplots(wide_df, out_dir=SCATTER_DIR, explode_multi=True)

    print("\nBuilding dimension scatterplots (multi-condition codes kept combined)...")
    plot_dimension_scatterplots(wide_df, out_dir=SCATTER_COMBINED_DIR, explode_multi=False)


if __name__ == "__main__":
    main()
