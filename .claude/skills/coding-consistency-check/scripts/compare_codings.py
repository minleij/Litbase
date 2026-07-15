#!/usr/bin/env python3
"""
Structurally diff two versions of a coded_articles/<article_id>.json record.

This script only does the deterministic part: it pulls the "old" and "new"
JSON (from git history and/or the working tree), matches up every
classification item, study-type field, summary field, and flag between the
two versions, and reports what changed. It does NOT decide whether a change
is expected or a sign of drift -- that requires reading the article-specific
`extraction_metadata.notes` text and judging whether wording changes are
cosmetic or substantive, which is exactly the kind of call a model should
make, not a script. See the coding-consistency-check SKILL.md for how the
output of this script gets turned into that judgment and a report.

Version resolution (per article, unless overridden):
  - If the working tree has uncommitted changes to the file relative to HEAD,
    compare HEAD (old) against the working tree (new) -- this is the normal
    "I just recoded this and haven't committed yet" case.
  - Otherwise, if the file has no uncommitted changes, compare the two most
    recent commits that touched the file -- the "I already committed my
    recode(s)" case.
  - If the file has only ever existed in one commit (or isn't tracked at
    all), there is nothing to compare against; this is reported, not treated
    as an error.

Usage:
    python scripts/compare_codings.py <article_id> [<article_id> ...]
    python scripts/compare_codings.py --all
    python scripts/compare_codings.py --all --old-ref v0.9-recode
    python scripts/compare_codings.py <article_id> --old-ref HEAD~3 --new-ref HEAD
    python scripts/compare_codings.py --all --out comparison.json

Prints a JSON report to stdout (or --out). One object per article requested,
under "articles"; each has either a "skipped" reason or a full diff.
"""

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

WORKING = "WORKING"  # sentinel meaning "read from the working tree on disk"

CLASSIFICATION_KEY_RE = re.compile(r"^(?P<short>.+)_v(?P<version>[\d.]+)$")


def find_project_root(start: Path) -> Path:
    for candidate in [start, *start.parents]:
        if (candidate / "articles").is_dir() and (candidate / "coded_articles").is_dir():
            return candidate
    raise SystemExit(
        f"Could not find a project root (a directory containing both 'articles/' and "
        f"'coded_articles/') starting from {start}. Pass --project-root explicitly."
    )


def run_git(args, cwd):
    return subprocess.run(
        ["git", *args], cwd=cwd, capture_output=True, text=True, encoding="utf-8", errors="replace"
    )


def is_tracked(rel_path: str, cwd: Path) -> bool:
    result = run_git(["ls-files", "--error-unmatch", rel_path], cwd)
    return result.returncode == 0


def has_uncommitted_changes(rel_path: str, cwd: Path) -> bool:
    result = run_git(["diff", "--name-only", "HEAD", "--", rel_path], cwd)
    return bool(result.stdout.strip())


def commits_touching_file(rel_path: str, cwd: Path):
    """Most-recent-first list of commit hashes that touched this file."""
    result = run_git(["log", "--follow", "--format=%H", "--", rel_path], cwd)
    return [line for line in result.stdout.splitlines() if line.strip()]


def resolve_refs(rel_path: str, cwd: Path, old_ref_override: str, new_ref_override: str):
    """Return (old_ref, new_ref, skip_reason). skip_reason is None if there's
    something to compare; otherwise old_ref/new_ref may be None."""
    if old_ref_override or new_ref_override:
        old_ref = old_ref_override or "HEAD"
        new_ref = new_ref_override or WORKING
        return old_ref, new_ref, None

    if not is_tracked(rel_path, cwd) and not (cwd / rel_path).exists():
        return None, None, f"'{rel_path}' does not exist in git history or the working tree."

    if is_tracked(rel_path, cwd) and has_uncommitted_changes(rel_path, cwd):
        return "HEAD", WORKING, None

    commits = commits_touching_file(rel_path, cwd)
    if len(commits) >= 2:
        return commits[1], commits[0], None
    if len(commits) == 1:
        return None, commits[0], "Only one committed version exists for this article; nothing to compare yet."
    return None, WORKING, "This article isn't tracked in git yet; nothing to compare yet."


def get_content(ref: str, rel_path: str, cwd: Path):
    """Return the file's text content at `ref`, or None if it doesn't exist there."""
    if ref is None:
        return None
    if ref == WORKING:
        p = cwd / rel_path
        return p.read_text(encoding="utf-8") if p.exists() else None
    result = run_git(["show", f"{ref}:{rel_path}"], cwd)
    if result.returncode != 0:
        return None
    return result.stdout


def load_json(text):
    if text is None:
        return None
    try:
        return json.loads(text)
    except json.JSONDecodeError as e:
        return {"__parse_error__": str(e)}


def diff_codebook_versions(old, new):
    old_v = (old or {}).get("extraction_metadata", {}).get("codebook_versions", {}) or {}
    new_v = (new or {}).get("extraction_metadata", {}).get("codebook_versions", {}) or {}
    keys = sorted(set(old_v) | set(new_v))
    out = {}
    for k in keys:
        ov, nv = old_v.get(k), new_v.get(k)
        bumped = None
        if ov is not None and nv is not None:
            bumped = tuple(int(p) for p in re.findall(r"\d+", nv)) > tuple(int(p) for p in re.findall(r"\d+", ov))
        out[k] = {"old": ov, "new": nv, "bumped": bumped}
    return out


def diff_study_type(old, new, codebook_versions):
    old_st = (old or {}).get("study_type", {}) or {}
    new_st = (new or {}).get("study_type", {}) or {}
    result = {
        "codebook_version": codebook_versions.get("study_type", {}),
        "primary": {"old": old_st.get("primary"), "new": new_st.get("primary"),
                    "changed": old_st.get("primary") != new_st.get("primary")},
        "secondary": {"old": old_st.get("secondary"), "new": new_st.get("secondary"),
                      "changed": old_st.get("secondary") != new_st.get("secondary")},
        "justification": {"old": old_st.get("justification"), "new": new_st.get("justification"),
                           "changed": old_st.get("justification") != new_st.get("justification")},
    }
    old_sub = old_st.get("sub_attributes", {}) or {}
    new_sub = new_st.get("sub_attributes", {}) or {}
    sub_changed = old_sub != new_sub
    result["sub_attributes_changed"] = sub_changed
    if sub_changed:
        result["sub_attributes_detail"] = {"old": old_sub, "new": new_sub}
    return result


SUMMARY_FIELDS = ["task", "control", "participants", "results", "issues",
                   "recommendations", "autonomous_capabilities", "abstract_summary"]


def diff_summary(old, new):
    old_s = (old or {}).get("summary", {}) or {}
    new_s = (new or {}).get("summary", {}) or {}
    out = {}
    for field in SUMMARY_FIELDS:
        ov, nv = old_s.get(field), new_s.get(field)
        if ov is None and nv is None:
            continue
        out[field] = {"old": ov, "new": nv, "changed": ov != nv}
    return out


def split_classification_key(key):
    m = CLASSIFICATION_KEY_RE.match(key)
    if m:
        return m.group("short"), m.group("version")
    return key, None


def diff_classification(old, new, codebook_versions):
    old_c = (old or {}).get("classification", {}) or {}
    new_c = (new or {}).get("classification", {}) or {}

    old_by_short = {}
    for k in old_c:
        short, ver = split_classification_key(k)
        old_by_short[short] = (k, ver)
    new_by_short = {}
    for k in new_c:
        short, ver = split_classification_key(k)
        new_by_short[short] = (k, ver)

    items = []
    for short in sorted(set(old_by_short) | set(new_by_short)):
        old_key, old_ver = old_by_short.get(short, (None, None))
        new_key, new_ver = new_by_short.get(short, (None, None))
        old_dims = old_c.get(old_key, {}) if old_key else {}
        new_dims = new_c.get(new_key, {}) if new_key else {}
        version_bumped = None
        if old_ver is not None and new_ver is not None:
            version_bumped = tuple(int(p) for p in re.findall(r"\d+", new_ver)) > \
                              tuple(int(p) for p in re.findall(r"\d+", old_ver))

        for dim in sorted(set(old_dims) | set(new_dims)):
            old_list = old_dims.get(dim, []) or []
            new_list = new_dims.get(dim, []) or []

            # Group by condition (None counts as its own bucket); pair items
            # within a condition bucket in order. This handles the common
            # case (one item per condition) robustly and degrades gracefully
            # when a dimension has several same-condition entries.
            def by_condition(lst):
                buckets = {}
                for item in lst:
                    buckets.setdefault(item.get("condition"), []).append(item)
                return buckets

            old_buckets = by_condition(old_list)
            new_buckets = by_condition(new_list)

            for condition in sorted(set(old_buckets) | set(new_buckets), key=lambda c: (c is None, c)):
                olds = old_buckets.get(condition, [])
                news = new_buckets.get(condition, [])
                for i in range(max(len(olds), len(news))):
                    old_item = olds[i] if i < len(olds) else None
                    new_item = news[i] if i < len(news) else None
                    if old_item is None:
                        status = "added"
                    elif new_item is None:
                        status = "removed"
                    elif old_item.get("code") != new_item.get("code"):
                        status = "code_changed"
                    elif old_item.get("justification") != new_item.get("justification"):
                        status = "justification_only_changed"
                    else:
                        status = "unchanged"

                    if status == "unchanged":
                        continue  # no need to report items that didn't change

                    items.append({
                        "governing_codebook_key": short,
                        "old_codebook_version": old_ver,
                        "new_codebook_version": new_ver,
                        "version_bumped": version_bumped,
                        "dimension": dim,
                        "condition": condition,
                        "status": status,
                        "old_code": old_item.get("code") if old_item else None,
                        "new_code": new_item.get("code") if new_item else None,
                        "old_justification": old_item.get("justification") if old_item else None,
                        "new_justification": new_item.get("justification") if new_item else None,
                    })
    return items


def normalize_flag_dimension(dimension):
    """Flag 'dimension' strings look like 'task_environment_v0.10 / some_dim'.
    Strip the codebook version so a flag carried forward across a version
    bump still matches its earlier self instead of showing as both added
    and removed."""
    if not dimension or " / " not in dimension:
        return dimension
    codebook_key, _, dim_name = dimension.partition(" / ")
    short, _ = split_classification_key(codebook_key)
    return f"{short} / {dim_name}"


def diff_flags(old, new):
    old_flags = (old or {}).get("flags", []) or []
    new_flags = (new or {}).get("flags", []) or []

    def key(f):
        return (normalize_flag_dimension(f.get("dimension")), f.get("type"))

    old_by_key = {}
    for f in old_flags:
        old_by_key.setdefault(key(f), []).append(f)
    new_by_key = {}
    for f in new_flags:
        new_by_key.setdefault(key(f), []).append(f)

    added, removed, modified = [], [], []
    for k in sorted(set(old_by_key) | set(new_by_key), key=lambda x: (x[0] or "", x[1] or "")):
        olds, news = old_by_key.get(k, []), new_by_key.get(k, [])
        for i in range(max(len(olds), len(news))):
            o = olds[i] if i < len(olds) else None
            n = news[i] if i < len(news) else None
            if o is None:
                added.append(n)
            elif n is None:
                removed.append(o)
            elif o.get("note") != n.get("note") or o.get("proposed_code") != n.get("proposed_code"):
                modified.append({"dimension": k[0], "type": k[1], "old_note": o.get("note"),
                                  "new_note": n.get("note"), "old_proposed_code": o.get("proposed_code"),
                                  "new_proposed_code": n.get("proposed_code")})
    return {"added": added, "removed": removed, "modified_note_only": modified}


def diff_citation(old, new):
    old_c = (old or {}).get("citation", {}) or {}
    new_c = (new or {}).get("citation", {}) or {}
    changed = {k: {"old": old_c.get(k), "new": new_c.get(k)}
               for k in sorted(set(old_c) | set(new_c)) if old_c.get(k) != new_c.get(k)}
    return changed


def compare_article(article_id, project_root, old_ref_override, new_ref_override):
    rel_path = f"coded_articles/{article_id}.json"
    old_ref, new_ref, skip_reason = resolve_refs(rel_path, project_root, old_ref_override, new_ref_override)

    if skip_reason and old_ref is None:
        return {"article_id": article_id, "skipped": skip_reason}

    old_text = get_content(old_ref, rel_path, project_root)
    new_text = get_content(new_ref, rel_path, project_root)
    old = load_json(old_text)
    new = load_json(new_text)

    if old is None or new is None:
        missing_side = "old" if old is None else "new"
        return {"article_id": article_id, "skipped": f"Could not read the {missing_side} version "
                f"(ref={old_ref if missing_side == 'old' else new_ref})."}
    if "__parse_error__" in (old or {}) or "__parse_error__" in (new or {}):
        return {"article_id": article_id, "skipped": "One of the two versions is not valid JSON.",
                "old_parse_error": old.get("__parse_error__") if old else None,
                "new_parse_error": new.get("__parse_error__") if new else None}

    codebook_versions = diff_codebook_versions(old, new)
    return {
        "article_id": article_id,
        "old_ref": old_ref,
        "new_ref": new_ref,
        "notes_old": (old.get("extraction_metadata", {}) or {}).get("notes"),
        "notes_new": (new.get("extraction_metadata", {}) or {}).get("notes"),
        "codebook_versions": codebook_versions,
        "citation_changed": diff_citation(old, new),
        "study_type": diff_study_type(old, new, codebook_versions),
        "summary": diff_summary(old, new),
        "classification": diff_classification(old, new, codebook_versions),
        "flags": diff_flags(old, new),
    }


def discover_all_article_ids(project_root: Path):
    coded_dir = project_root / "coded_articles"
    ids = []
    for f in sorted(coded_dir.glob("*.json")):
        if f.name == "index.json":
            continue
        ids.append(f.stem)
    return ids


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("article_ids", nargs="*", help="One or more article_id values (matches coded_articles/<id>.json)")
    parser.add_argument("--all", action="store_true", help="Compare every article in coded_articles/")
    parser.add_argument("--old-ref", default=None, help="Git ref for the 'old' version (default: smart per-article resolution)")
    parser.add_argument("--new-ref", default=None, help="Git ref for the 'new' version, or 'WORKING' for the working tree (default: smart per-article resolution)")
    parser.add_argument("--project-root", default=None)
    parser.add_argument("--out", default=None, help="Write JSON to this path instead of stdout")
    args = parser.parse_args()

    start = Path(args.project_root).resolve() if args.project_root else Path.cwd()
    project_root = find_project_root(start)

    if args.all:
        article_ids = discover_all_article_ids(project_root)
    elif args.article_ids:
        article_ids = args.article_ids
    else:
        parser.error("Provide one or more article_id values, or pass --all.")

    articles = [compare_article(aid, project_root, args.old_ref, args.new_ref) for aid in article_ids]
    report = {"project_root": str(project_root), "articles": articles}

    text = json.dumps(report, indent=2)
    if args.out:
        Path(args.out).write_text(text, encoding="utf-8")
        print(f"Wrote {args.out}")
    else:
        try:
            sys.stdout.reconfigure(encoding="utf-8")
        except (AttributeError, ValueError):
            pass
        print(text)


if __name__ == "__main__":
    main()
