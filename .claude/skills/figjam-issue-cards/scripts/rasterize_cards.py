"""
Step 4 of the figjam-issue-cards pipeline.

Rasterizes each per-card SVG to a tightly-sized PNG, one headless-browser
process per file, with the browser window set to exactly that card's own
SVG width/height (read from card_manifest.json) so the screenshot is
pixel-exact with no extra chrome or whitespace to crop.

WHY A REAL BROWSER INSTEAD OF A SVG-TO-PNG LIBRARY (e.g. cairosvg): this
was tried first and failed to import (missing native cairo DLL on Windows,
and similar native-dependency issues are common on other platforms too). A
headless browser needs no extra native libraries beyond the browser install
itself, which is very likely already present.

WHY NOT JUST HAND THE SVGs TO FIGMA DIRECTLY: see the docstring at the top
of generate_cards.py -- Figma's own SVG importer mangles hand-rolled
multi-<text>-element SVGs. Rasterizing here, with a renderer that handles
plain SVG correctly, sidesteps that entirely. The PNG output works with any
whiteboard tool (FigJam, Miro, Mural, ...) since it's just an image.

Usage:
    python rasterize_cards.py --svg-dir <dir with *.svg + card_manifest.json> \
        --out-dir <dir to write *.png> [--browser-path <path to msedge/chrome>] [--scale 2]
"""
import argparse
import json
import shutil
import subprocess
from pathlib import Path

# Common install locations to try, in order, if --browser-path isn't given.
CANDIDATE_BROWSERS = [
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "msedge",
    "google-chrome",
    "chromium",
    "chromium-browser",
]


def find_browser(explicit: str | None) -> str:
    if explicit:
        return explicit
    for candidate in CANDIDATE_BROWSERS:
        if Path(candidate).exists():
            return candidate
        found = shutil.which(candidate)
        if found:
            return found
    raise SystemExit(
        "Couldn't find a headless-capable Chromium/Edge browser automatically. "
        "Pass --browser-path pointing at msedge.exe / chrome.exe / chromium explicitly."
    )


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--svg-dir", required=True, help="Directory with *.svg files + card_manifest.json")
    ap.add_argument("--out-dir", required=True)
    ap.add_argument("--browser-path", default=None)
    ap.add_argument("--scale", type=int, default=2, help="Device scale factor for crisper output (default 2x)")
    ap.add_argument("--timeout", type=int, default=30)
    args = ap.parse_args()

    svg_dir = Path(args.svg_dir)
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    browser = find_browser(args.browser_path)

    manifest = json.loads((svg_dir / "card_manifest.json").read_text(encoding="utf-8"))

    ok, failed = 0, []
    for i, entry in enumerate(manifest, start=1):
        svg_path = svg_dir / f"{entry['card_id']}.svg"
        png_path = out_dir / f"{entry['card_id']}.png"
        w, h = entry["width"], entry["height"]
        result = subprocess.run(
            [browser, "--headless", "--disable-gpu",
             f"--screenshot={png_path}",
             f"--window-size={w},{h}",
             "--hide-scrollbars",
             f"--force-device-scale-factor={args.scale}",
             svg_path.as_uri()],
            capture_output=True, text=True, timeout=args.timeout,
        )
        if png_path.exists() and png_path.stat().st_size > 0:
            ok += 1
        else:
            failed.append((entry["card_id"], result.stderr[-500:] if result.stderr else "no output file"))
        if i % 20 == 0 or i == len(manifest):
            print(f"  {i}/{len(manifest)} done...")

    print(f"Rasterized {ok}/{len(manifest)} cards to {out_dir}")
    if failed:
        print(f"FAILED ({len(failed)}):")
        for card_id, err in failed:
            print(f"  {card_id}: {err}")
        raise SystemExit(1)


if __name__ == "__main__":
    main()
