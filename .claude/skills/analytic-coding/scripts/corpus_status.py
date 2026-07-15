#!/usr/bin/env python3
"""
Report corpus-wide status for the analytic-coding skill's coded_articles/ corpus.

Two things this surfaces that no single record shows on its own:

1. Stale records -- articles coded against an older version of a codebook than the
   version currently present in the project. Codebook files are living documents and
   SKILL.md stamps the version used per record in extraction_metadata.codebook_versions,
   but nothing previously checked that stamp against the codebook file's current version,
   so drift (e.g. a codebook bumped from v0.8 to v0.9) is invisible unless someone
   manually compares each record.

2. Open flags -- every "Unclear / Candidate New Code" flag across the whole corpus in
   one place. Per references/codebook-application-guide.md, "Not Applicable" and
   "Not Described" are already-resolved findings, not open items; only
   "Unclear / Candidate New Code" needs a decision from the user. Those are grouped
   separately here so they don't get lost in the noise of the other two.

Usage:
    python scripts/corpus_status.py [project_root]
    python scripts/corpus_status.py --json [project_root]
    python scripts/corpus_status.py --all-flags [project_root]

If project_root is omitted, it's auto-detected by walking up from the current
directory looking for a directory that contains both 'articles/' and
'coded_articles/' as siblings -- the same landmark SKILL.md itself uses.

Exits non-zero if there are stale records or open Unclear / Candidate New Code
flags, so it can be used as a quick "is there anything to look at" gate.
"""

import argparse
import json
import re
import sys
from pathlib import Path

CODEBOOK_FILENAME_RE = re.compile(
    r"^HSI_HRI_(?P<name>[A-Za-z][A-Za-z-]*)_Classification_Codebook_v(?P<major>\d+)_(?P<minor>\d+)\.md$"
)


def find_project_root(start: Path) -> Path:
    """Walk up from `start` looking for a directory containing both 'articles/'
    and 'coded_articles/' as siblings -- the project root, per SKILL.md Step 5."""
    for candidate in [start, *start.parents]:
        if (candidate / "articles").is_dir() and (candidate / "coded_articles").is_dir():
            return candidate
    raise SystemExit(
        f"Could not find a project root (a directory containing both 'articles/' and "
        f"'coded_articles/') starting from {start}. Pass the project root explicitly."
    )


def parse_version(v: str) -> tuple:
    return tuple(int(p) for p in re.findall(r"\d+", v))


def discover_codebook_versions(project_root: Path) -> dict:
    """Map short codebook key (e.g. 'task_environment') -> current version string,
    from codebook filenames at the project root. Uses the highest version found per
    codebook if more than one exists, mirroring SKILL.md Step 0.3."""
    versions = {}
    for f in project_root.glob("HSI_HRI_*_Classification_Codebook_v*.md"):
        m = CODEBOOK_FILENAME_RE.match(f.name)
        if not m:
            continue
        short_key = m.group("name").lower().replace("-", "_")
        version = (int(m.group("major")), int(m.group("minor")))
        if short_key not in versions or version > versions[short_key]:
            versions[short_key] = version
    return {k: f"{v[0]}.{v[1]}" for k, v in versions.items()}


def load_records(project_root: Path) -> list:
    records = []
    coded_dir = project_root / "coded_articles"
    for f in sorted(coded_dir.glob("*.json")):
        if f.name == "index.json":
            continue
        try:
            with open(f, "r", encoding="utf-8") as fh:
                records.append((f, json.load(fh)))
        except json.JSONDecodeError as e:
            print(f"WARN  could not parse {f}: {e}", file=sys.stderr)
    return records


def check_staleness(records, current_versions):
    """Return (stale, up_to_date_counts, unknown_keys):
    - stale: {short_key: [(article_id, record_version), ...]} for records whose
      stamped version is older than the current codebook file's version.
    - up_to_date_counts: {short_key: count} for records already at the current version.
    - unknown_keys: {short_key: [article_id, ...]} for codebook keys referenced by
      records that don't match any codebook file found at the project root (e.g. a
      typo, or the codebook file was renamed/removed since coding)."""
    stale = {key: [] for key in current_versions}
    up_to_date_counts = {key: 0 for key in current_versions}
    unknown_keys = {}
    for path, record in records:
        article_id = record.get("article_id", path.stem)
        stamped = record.get("extraction_metadata", {}).get("codebook_versions", {})
        for key, recorded_version in stamped.items():
            if key not in current_versions:
                unknown_keys.setdefault(key, []).append(article_id)
                continue
            try:
                if parse_version(recorded_version) < parse_version(current_versions[key]):
                    stale[key].append((article_id, recorded_version))
                else:
                    up_to_date_counts[key] += 1
            except ValueError:
                print(
                    f"WARN  {path.name}: unparseable version '{recorded_version}' for '{key}'",
                    file=sys.stderr,
                )
    return stale, up_to_date_counts, unknown_keys


def collect_flags(records):
    """Return {flag_type: [(article_id, dimension, note, proposed_code), ...]}."""
    by_type = {}
    for path, record in records:
        article_id = record.get("article_id", path.stem)
        for flag in record.get("flags", []):
            ftype = flag.get("type", "Unknown")
            by_type.setdefault(ftype, []).append((
                article_id,
                flag.get("dimension", "?"),
                flag.get("note", ""),
                flag.get("proposed_code"),
            ))
    return by_type


def print_report(project_root, records, current_versions, stale, up_to_date_counts, unknown_keys, flags_by_type, show_all_flags):
    print("HSI/HRI Corpus Status")
    print("=" * 60)
    print(f"Project root: {project_root}")
    print(f"Records scanned: {len(records)}")
    print()

    print("Codebook versions (current file vs. corpus)")
    print("-" * 60)
    if not current_versions:
        print("  No 'HSI_HRI_*_Classification_Codebook_v*.md' files found at project root.")
    for key, current in sorted(current_versions.items()):
        n_stale = len(stale.get(key, []))
        n_ok = up_to_date_counts.get(key, 0)
        total = n_stale + n_ok
        if total == 0:
            print(f"  {key:<20} current: {current:<6}  (no coded records reference this codebook)")
        else:
            print(f"  {key:<20} current: {current:<6}  {n_ok}/{total} up to date, {n_stale} stale")
    print()

    if unknown_keys:
        print("WARNING: records reference codebook keys with no matching codebook file")
        print("-" * 60)
        for key, article_ids in sorted(unknown_keys.items()):
            print(f"  '{key}': {len(article_ids)} record(s), e.g. {article_ids[0]}")
        print()

    any_stale = any(stale.values())
    if any_stale:
        print("STALE RECORDS (coded against an older version than the current codebook file)")
        print("-" * 60)
        for key, entries in sorted(stale.items()):
            if not entries:
                continue
            print(f"  {key} (current: {current_versions[key]}):")
            for article_id, version in sorted(entries):
                print(f"    - {article_id}  (coded at {version})")
        print()

    unclear = flags_by_type.get("Unclear / Candidate New Code", [])
    print(f"OPEN FLAGS -- Unclear / Candidate New Code ({len(unclear)}) -- needs a decision from you")
    print("-" * 60)
    if not unclear:
        print("  None.")
    for article_id, dimension, note, proposed in sorted(unclear, key=lambda t: (t[0], t[1])):
        print(f"  - {article_id} [{dimension}]")
        print(f"      note:     {note}")
        if proposed:
            print(f"      proposed: {proposed}")
    print()

    informational_types = [t for t in flags_by_type if t != "Unclear / Candidate New Code"]
    if informational_types:
        print("Other flags (informational -- Not Applicable / Not Described are resolved findings, not open items)")
        print("-" * 60)
        for ftype in sorted(informational_types):
            entries = flags_by_type[ftype]
            print(f"  {ftype}: {len(entries)}")
            if show_all_flags:
                for article_id, dimension, note, _ in sorted(entries, key=lambda t: (t[0], t[1])):
                    print(f"    - {article_id} [{dimension}]: {note}")
        if not show_all_flags:
            print("  (pass --all-flags to list every instance)")
        print()


def build_json_report(project_root, records, current_versions, stale, unknown_keys, flags_by_type):
    return {
        "project_root": str(project_root),
        "records_scanned": len(records),
        "codebook_versions": current_versions,
        "stale_records": {
            key: [{"article_id": a, "coded_at": v} for a, v in entries]
            for key, entries in stale.items() if entries
        },
        "unknown_codebook_keys": unknown_keys,
        "flags": {
            ftype: [
                {"article_id": a, "dimension": d, "note": n, "proposed_code": p}
                for a, d, n, p in entries
            ]
            for ftype, entries in flags_by_type.items()
        },
    }


def main():
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument(
        "project_root", nargs="?", default=None,
        help="Project root directory (auto-detected from the current directory if omitted)",
    )
    parser.add_argument("--json", action="store_true", help="Emit a JSON report instead of the human-readable one")
    parser.add_argument(
        "--all-flags", action="store_true",
        help="Also list every Not Applicable / Not Described instance, not just counts",
    )
    args = parser.parse_args()

    # Windows consoles often default to a non-UTF-8 codepage, which mangles the
    # em dashes used throughout the codebooks' own note text. Force UTF-8 stdout
    # so the report is readable regardless of the terminal's codepage.
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except (AttributeError, ValueError):
        pass

    start = Path(args.project_root).resolve() if args.project_root else Path.cwd()
    project_root = find_project_root(start)

    current_versions = discover_codebook_versions(project_root)
    records = load_records(project_root)
    stale, up_to_date_counts, unknown_keys = check_staleness(records, current_versions)
    flags_by_type = collect_flags(records)

    if args.json:
        report = build_json_report(project_root, records, current_versions, stale, unknown_keys, flags_by_type)
        print(json.dumps(report, indent=2))
    else:
        print_report(
            project_root, records, current_versions, stale, up_to_date_counts,
            unknown_keys, flags_by_type, args.all_flags,
        )

    any_stale = any(stale.values())
    any_unclear = bool(flags_by_type.get("Unclear / Candidate New Code"))
    sys.exit(1 if (any_stale or any_unclear) else 0)


if __name__ == "__main__":
    main()
