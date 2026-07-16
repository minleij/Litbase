"""
Step 3 of the figjam-result-cards pipeline.

Generates one standalone SVG per result card (plus one legend SVG) from
article_meta.json + results_data.json. These get rasterized to PNG by
rasterize_cards.py in the next step.

This is a near-identical port of figjam-issue-cards' generate_cards.py --
the color logic, text-wrapping, card geometry, and footer rendering are
byte-for-byte the same (none of that is issue-specific, it's just correct
card-rendering logic), and the "why" notes below are carried over verbatim
because they apply equally here. The only real differences are the data
field names (results_data.json / "results" key instead of issues_data.json
/ "issues") and the card-id/print-statement wording.

WHY ONE SVG PER CARD, NOT A GRID/SHEET OF SEVERAL CARDS PER FILE:
An earlier version of the sibling figjam-issue-cards pipeline grouped
several cards per article into one bigger "sheet" SVG (a grid layout),
meant to be imported into Figma/FigJam as an editable vector group. Two
things went wrong: (1) Figma's SVG importer badly mangled hand-rolled
multi-<text>-element SVGs -- it collapsed and overlapped sibling <text>
lines that render perfectly correctly in any real browser, apparently not
respecting each element's own y position; and (2) even fixed, a flattened
multi-card image can't be pulled apart on a whiteboard -- the whole point
of a card wall is that each result is independently movable. So: rasterize
to PNG (sidesteps Figma's importer entirely -- a real browser renders this
SVG correctly, see rasterize_cards.py) AND keep card granularity at
one-file-per-card (so each PNG stays independently draggable once it's on
the board). Don't regress either of these without a specific reason.

WHY THE FOOTER WRAPS FULLY: an earlier version computed the footer's
possible wrap lines but only rendered line[0], silently dropping the rest --
a long author list would just lose text off the edge of the footer with no
visible sign anything was missing. Render every wrapped line.

Usage:
    python generate_cards.py --article-meta <path> --results-data <path> \
        --out-dir <output dir> [--dimension-order <path/to/dimension_order.json>]

    python generate_cards.py --dimension-order <path> --out-dir <dir> --legend-only
        (generates just _legend.svg, e.g. to preview the color scheme without
        needing article_meta.json/results_data.json yet)

Writes:
    <out-dir>/<article_id>__<NN>_<slug>.svg   -- one per result card
    <out-dir>/_legend.svg
    <out-dir>/card_manifest.json              -- {card_id, article_id, width, height, title}
                                                  per card; rasterize_cards.py consumes this
"""
from __future__ import annotations

import argparse
import json
import re
from html import escape
from pathlib import Path

DEFAULT_DIM_ORDER = Path(__file__).resolve().parent.parent / "references" / "dimension_order.json"

# ---------------------------------------------------------------------------
# Color scale: viridis anchor stops (same colormap analysis/visualize.py
# already uses for its own count/scatter plots), linearly interpolated in RGB.
# ---------------------------------------------------------------------------
VIRIDIS_STOPS = [
    (0.00, (68, 1, 84)),
    (0.25, (59, 82, 139)),
    (0.50, (33, 144, 140)),
    (0.75, (93, 200, 99)),
    (1.00, (253, 231, 37)),
]


def viridis(t: float) -> tuple[int, int, int]:
    t = max(0.0, min(1.0, t))
    for (t0, c0), (t1, c1) in zip(VIRIDIS_STOPS, VIRIDIS_STOPS[1:]):
        if t0 <= t <= t1:
            f = 0 if t1 == t0 else (t - t0) / (t1 - t0)
            return tuple(round(c0[i] + f * (c1[i] - c0[i])) for i in range(3))
    return VIRIDIS_STOPS[-1][1]


def hex_color(rgb) -> str:
    return "#{:02x}{:02x}{:02x}".format(*rgb)


def text_color_for_bg(rgb) -> str:
    r, g, b = rgb
    luminance = (0.299 * r + 0.587 * g + 0.114 * b) / 255
    return "#1a1a1a" if luminance > 0.55 else "#ffffff"


def strip_suffix(code: str) -> str:
    """Strips a trailing parenthetical, e.g. 'Direct (LHCA 1)' -> 'Direct',
    'Task-Allocation (Placeholder)' -> 'Task-Allocation' -- codes are often
    stored with a qualifier suffix that isn't part of the ordinal scale's
    own naming."""
    return re.sub(r"\s*\([^)]*\)\s*$", "", code).strip()


def build_full_order(dim: str, dim_meta: dict, all_codes: set[str]) -> list[str]:
    """Base scale (from dimension_order.json) + any codes actually present
    in the data but not in that scale, appended alphabetically -- mirrors
    _ordered_categories() in analysis/visualize.py. See references/
    color_coding.md for why an unmatched code isn't an error."""
    base = dim_meta["dimensions"][dim]["order"]
    unclear = dim_meta["unclear_code"]
    present_stripped = {strip_suffix(c) for c in all_codes if c != unclear}
    leftover = sorted(present_stripped - set(base))
    return base + leftover


def code_color(dim: str, code: str, dim_meta: dict, full_order: dict[str, list[str]]) -> tuple[str, str]:
    if code == dim_meta["unclear_code"]:
        return "#9e9e9e", "#ffffff"
    order = full_order[dim]
    stripped = strip_suffix(code)
    try:
        idx = order.index(stripped)
    except ValueError:
        idx = len(order) - 1
    n = len(order)
    t = 0.0 if n <= 1 else idx / (n - 1)
    return hex_color(viridis(t)), text_color_for_bg(viridis(t))


# ---------------------------------------------------------------------------
# Text layout helpers (SVG has no auto text-wrap, so we wrap in Python using
# a conservative average-character-width estimate per font weight)
# ---------------------------------------------------------------------------
def char_width(font_size: float, weight: str = "regular") -> float:
    factor = {"regular": 0.52, "bold": 0.58, "italic": 0.50}.get(weight, 0.52)
    return font_size * factor


def wrap_text(text: str, font_size: float, max_width: float, weight: str = "regular") -> list[str]:
    cw = char_width(font_size, weight)
    # 0.94 safety margin: real font metrics vary slightly by renderer/platform,
    # so wrap a bit early rather than risk a line bleeding past the card edge.
    max_chars = max(4, int((max_width * 0.94) / cw))
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if len(trial) <= max_chars or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines or [""]


def esc(s: str) -> str:
    return escape(s, quote=True)


def slugify(text: str, max_len: int = 44) -> str:
    s = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return s[:max_len].rstrip("-")


# ---------------------------------------------------------------------------
# Card geometry -- identical to figjam-issue-cards; keep both in sync if
# either is ever intentionally restyled, since the point is a shared visual
# language across both card sets.
# ---------------------------------------------------------------------------
CARD_W = 420
PAD = 20
CHIP_H = 22
CHIP_GAP_X = 6
CHIP_GAP_Y = 6
TITLE_SIZE = 15.5
TITLE_LH = 20
QUOTE_SIZE = 12
QUOTE_LH = 16
FOOTER_LINE_H = 15
FOOTER_PAD = 10


def layout_chips(chips: list[tuple[str, str]], dim_meta: dict, dim_orders: dict) -> tuple[list[list[dict]], int]:
    """chips: list of (dim, code). Returns wrapped rows of chip render-specs and total height."""
    max_w = CARD_W - 2 * PAD
    rows, cur_row, cur_x = [], [], 0
    for dim, code in chips:
        bg, fg = code_color(dim, code, dim_meta, dim_orders)
        abbr = dim_meta["dimensions"][dim]["abbr"]
        unclear = dim_meta["unclear_code"]
        label = f"{abbr}: {strip_suffix(code) if code != unclear else 'Unclear/New'}"
        w = char_width(9.5, "bold") * len(label) + 16
        w = min(w, max_w)
        if cur_x + w > max_w and cur_row:
            rows.append(cur_row)
            cur_row, cur_x = [], 0
        cur_row.append({"label": label, "w": w, "bg": bg, "fg": fg, "x": cur_x})
        cur_x += w + CHIP_GAP_X
    if cur_row:
        rows.append(cur_row)
    height = len(rows) * CHIP_H + max(0, len(rows) - 1) * CHIP_GAP_Y
    return rows, height


def render_card_svg(card: dict, dim_meta: dict, dim_orders: dict) -> tuple[str, int, int]:
    """Standalone single-card SVG, top-left origin (0,0) -- meant to be
    rasterized 1:1 to its own PNG file, one image per result card."""
    parts = []
    cy = PAD

    chip_rows, chips_h = layout_chips(card["chips"], dim_meta, dim_orders)
    for ri, row in enumerate(chip_rows):
        ry = cy + ri * (CHIP_H + CHIP_GAP_Y)
        for chip in row:
            parts.append(
                f'<rect x="{chip["x"]}" y="{ry}" width="{chip["w"]:.1f}" height="{CHIP_H}" rx="11" '
                f'fill="{chip["bg"]}"/>'
            )
            parts.append(
                f'<text x="{chip["x"] + chip["w"] / 2:.1f}" y="{ry + CHIP_H / 2 + 3.5:.1f}" '
                f'font-family="Inter, Arial, sans-serif" font-size="9.5" font-weight="700" '
                f'fill="{chip["fg"]}" text-anchor="middle">{esc(chip["label"])}</text>'
            )
    cy += chips_h + (12 if chip_rows else 0)

    title_lines = wrap_text(card["title"], TITLE_SIZE, CARD_W - 2 * PAD, "bold")
    for line in title_lines:
        cy += TITLE_LH
        parts.append(
            f'<text x="0" y="{cy - 5}" font-family="Inter, Arial, sans-serif" font-size="{TITLE_SIZE}" '
            f'font-weight="700" fill="#161616">{esc(line)}</text>'
        )
    cy += 10

    for qi, quote in enumerate(card["quotes"]):
        q_text = f'“{quote}”'
        q_lines = wrap_text(q_text, QUOTE_SIZE, CARD_W - 2 * PAD - 14, "italic")
        block_top = cy
        for line in q_lines:
            cy += QUOTE_LH
            parts.append(
                f'<text x="14" y="{cy - 4}" font-family="Inter, Arial, sans-serif" font-size="{QUOTE_SIZE}" '
                f'font-style="italic" fill="#3d3d3d">{esc(line)}</text>'
            )
        parts.append(
            f'<rect x="0" y="{block_top - 12}" width="3" height="{cy - block_top + 4}" rx="1.5" fill="#c7c7c7"/>'
        )
        cy += 6 if qi < len(card["quotes"]) - 1 else 0

    cy += PAD
    body_h = cy

    # Footer: wrap both lines FULLY (render every line -- see module
    # docstring on why this must never silently truncate).
    author_lines = wrap_text(card["footer_author"], 11.5, CARD_W - 2 * PAD, "bold")
    id_lines = wrap_text(card["footer_id"], 9.5, CARD_W - 2 * PAD, "regular")
    footer_h = FOOTER_PAD * 2 + len(author_lines) * FOOTER_LINE_H + len(id_lines) * (FOOTER_LINE_H - 2)
    footer_y = body_h
    total_h = body_h + footer_h

    svg = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {CARD_W} {total_h}" '
        f'width="{CARD_W}" height="{total_h}">',
        f'<rect x="0" y="0" width="{CARD_W}" height="{total_h}" rx="14" fill="#ffffff" '
        f'stroke="#e2e2e2" stroke-width="1.5"/>',
        f'<g transform="translate({PAD},{PAD})">',
    ]
    svg.extend(parts)
    svg.append('</g>')
    svg.append(f'<rect x="0" y="{footer_y}" width="{CARD_W}" height="{footer_h}" rx="0" fill="#f4f4f5"/>')
    svg.append(f'<rect x="0" y="{footer_y}" width="{CARD_W}" height="2" fill="#e2e2e2"/>')

    fy = footer_y + FOOTER_PAD + 10
    for line in author_lines:
        svg.append(
            f'<text x="{PAD}" y="{fy:.1f}" font-family="Inter, Arial, sans-serif" '
            f'font-size="11.5" font-weight="700" fill="#333333">{esc(line)}</text>'
        )
        fy += FOOTER_LINE_H
    fy += 2
    for line in id_lines:
        svg.append(
            f'<text x="{PAD}" y="{fy:.1f}" font-family="Inter, Arial, sans-serif" '
            f'font-size="9.5" font-weight="400" fill="#777777">{esc(line)}</text>'
        )
        fy += FOOTER_LINE_H - 2

    svg.append('</svg>')
    return "\n".join(svg), CARD_W, total_h


def build_legend(dim_meta: dict, dim_orders: dict) -> str:
    total_w = 760
    lines = [
        '<text x="24" y="38" font-family="Inter, Arial, sans-serif" font-size="19" font-weight="800" '
        'fill="#111111">Code color legend</text>',
    ]
    subtitle = ("Color = position on that dimension's ordinal scale (dark -> light = low -> high). "
                "Compare colors only within the same chip label (e.g. only TASK vs TASK).")
    sub_lines = wrap_text(subtitle, 11.5, total_w - 48, "regular")
    y = 58
    for line in sub_lines:
        lines.append(
            f'<text x="24" y="{y}" font-family="Inter, Arial, sans-serif" font-size="11.5" '
            f'fill="#555555">{esc(line)}</text>'
        )
        y += 16
    y += 20
    for dim, meta in dim_meta["dimensions"].items():
        order = dim_orders[dim]
        lines.append(
            f'<text x="24" y="{y}" font-family="Inter, Arial, sans-serif" font-size="13" font-weight="700" '
            f'fill="#161616">{esc(meta["abbr"])} — {esc(meta["label"])}</text>'
        )
        y += 22
        x = 24
        for code in order:
            bg, fg = code_color(dim, code, dim_meta, dim_orders)
            w = char_width(10, "bold") * len(code) + 18
            if x + w > total_w - 24:
                x = 24
                y += 30
            lines.append(f'<rect x="{x}" y="{y - 16}" width="{w:.1f}" height="24" rx="12" fill="{bg}"/>')
            lines.append(
                f'<text x="{x + w / 2:.1f}" y="{y - 16 + 12 + 3.5:.1f}" font-family="Inter, Arial, sans-serif" '
                f'font-size="10" font-weight="700" fill="{fg}" text-anchor="middle">{esc(code)}</text>'
            )
            x += w + 8
        y += 40
    lines.append(
        f'<text x="24" y="{y}" font-family="Inter, Arial, sans-serif" font-size="10.5" fill="#777777">'
        f'Gray chips = "{esc(dim_meta["unclear_code"])}" (not yet placed on the scale).</text>'
    )
    total_h = y + 24

    header = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {total_w} {total_h}" '
        f'width="{total_w}" height="{total_h}">',
        f'<rect x="0" y="0" width="{total_w}" height="{total_h}" fill="#ffffff" '
        f'stroke="#e2e2e2" stroke-width="1.5" rx="14"/>',
    ]
    return "\n".join(header + lines + ['</svg>'])


def compute_dim_orders(dim_meta: dict, article_meta: list[dict]) -> dict[str, list[str]]:
    dim_keys = list(dim_meta["dimensions"].keys())
    all_codes = {dim: set() for dim in dim_keys}
    for a in article_meta:
        for dim, codes in a.get("dims", {}).items():
            all_codes[dim].update(codes)
    return {dim: build_full_order(dim, dim_meta, all_codes[dim]) for dim in dim_keys}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--article-meta")
    ap.add_argument("--results-data")
    ap.add_argument("--out-dir", required=True)
    ap.add_argument("--dimension-order", default=str(DEFAULT_DIM_ORDER))
    ap.add_argument("--legend-only", action="store_true",
                     help="Only (re)generate _legend.svg -- useful to preview the color scheme "
                          "without needing article_meta.json/results_data.json yet.")
    args = ap.parse_args()

    dim_meta = json.loads(Path(args.dimension_order).read_text(encoding="utf-8"))
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    if args.legend_only:
        # No real data yet -- every code across every dimension gets its
        # "natural" position (i.e. just the defined scale itself).
        dim_orders = {dim: meta["order"] for dim, meta in dim_meta["dimensions"].items()}
        (out_dir / "_legend.svg").write_text(build_legend(dim_meta, dim_orders), encoding="utf-8")
        print(f"Wrote {out_dir / '_legend.svg'}")
        return

    if not args.article_meta or not args.results_data:
        raise SystemExit("--article-meta and --results-data are required unless --legend-only is set")

    article_meta = json.loads(Path(args.article_meta).read_text(encoding="utf-8"))
    results_by_id = json.loads(Path(args.results_data).read_text(encoding="utf-8"))
    meta_by_id = {a["article_id"]: a for a in article_meta}
    dim_orders = compute_dim_orders(dim_meta, article_meta)

    for f in out_dir.glob("*.svg"):
        f.unlink()

    manifest = []
    for aid, result_entry in results_by_id.items():
        meta = meta_by_id.get(aid)
        if not meta:
            continue
        results = result_entry.get("results", [])
        if not results:
            continue

        first_author = meta["authors"].split(",")[0].split(" and ")[0].split(" & ")[0].strip()
        is_single_author = (meta["authors"].count(",") == 0 and "&" not in meta["authors"]
                             and " and " not in meta["authors"])
        footer_author = (f'{meta["authors"]} ({meta["year"]})' if is_single_author
                          else f'{first_author} et al. ({meta["year"]})')

        chips = []
        for dim in dim_meta["dimensions"]:
            for code in meta["dims"].get(dim, []):
                chips.append((dim, code))

        for idx, result in enumerate(results, start=1):
            card = {
                "chips": chips,
                "title": result["title"],
                "quotes": result["quotes"],
                "footer_author": footer_author,
                "footer_id": aid,
            }
            svg_str, w, h = render_card_svg(card, dim_meta, dim_orders)
            card_id = f"{aid}__{idx:02d}_{slugify(result['title'])}"
            (out_dir / f"{card_id}.svg").write_text(svg_str, encoding="utf-8")
            manifest.append({"card_id": card_id, "article_id": aid, "width": w, "height": h, "title": result["title"]})

    legend_svg = build_legend(dim_meta, dim_orders)
    m = re.search(r'height="(\d+)"', legend_svg)
    legend_h = int(m.group(1)) if m else 900
    (out_dir / "_legend.svg").write_text(legend_svg, encoding="utf-8")
    manifest.append({"card_id": "_legend", "article_id": None, "width": 760, "height": legend_h, "title": "Code color legend"})

    manifest_path = out_dir / "card_manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print(f"Wrote {len(manifest) - 1} per-card SVGs + legend to {out_dir}")
    print(f"Manifest: {manifest_path} ({len(manifest)} entries)")


if __name__ == "__main__":
    main()
