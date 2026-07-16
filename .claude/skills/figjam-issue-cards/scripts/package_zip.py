"""
Step 5 (final) of the figjam-issue-cards pipeline.

Zips a directory of PNGs into one downloadable file. Uses Python's zipfile
module rather than a shell command (Compress-Archive, zip, ...) so this
works the same on any platform without relying on which archiver happens
to be on PATH.

Usage:
    python package_zip.py --png-dir <dir of *.png> --out <path/to/output.zip>
"""
import argparse
import zipfile
from pathlib import Path


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--png-dir", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    png_dir = Path(args.png_dir)
    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    files = sorted(png_dir.glob("*.png"))
    if not files:
        raise SystemExit(f"No .png files found in {png_dir}")

    with zipfile.ZipFile(out_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for f in files:
            zf.write(f, arcname=f.name)

    size_mb = out_path.stat().st_size / (1024 * 1024)
    print(f"Wrote {out_path} ({len(files)} files, {size_mb:.1f} MB)")


if __name__ == "__main__":
    main()
