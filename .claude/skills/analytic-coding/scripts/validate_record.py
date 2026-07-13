#!/usr/bin/env python3
"""
Validate one or more coded-article JSON records against schemas/article_record.schema.json.

Usage:
    python scripts/validate_record.py coded_articles/williams_2023_command_control_swarm.json
    python scripts/validate_record.py coded_articles/*.json
    python scripts/validate_record.py --all coded_articles/

Exits non-zero if any file fails validation, so it can be used as a simple gate
before treating a record as done (see SKILL.md Step 5).
"""

import argparse
import json
import sys
from pathlib import Path

try:
    import jsonschema
except ImportError:
    sys.stderr.write(
        "jsonschema is required: pip install jsonschema --break-system-packages\n"
    )
    sys.exit(2)

SCHEMA_PATH = Path(__file__).resolve().parent.parent / "schemas" / "article_record.schema.json"


def load_schema():
    with open(SCHEMA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def validate_file(path: Path, schema: dict) -> list[str]:
    """Return a list of human-readable error strings (empty if valid)."""
    errors = []
    try:
        with open(path, "r", encoding="utf-8") as f:
            record = json.load(f)
    except json.JSONDecodeError as e:
        return [f"Not valid JSON: {e}"]

    validator = jsonschema.Draft7Validator(schema)
    for err in sorted(validator.iter_errors(record), key=lambda e: e.path):
        loc = "/".join(str(p) for p in err.path) or "(root)"
        errors.append(f"{loc}: {err.message}")

    # A couple of checks the JSON Schema can't easily express:
    study_type = record.get("study_type", {})
    summary = record.get("summary", {})
    is_user_study = "User Study" in (
        [study_type.get("primary")] + [study_type.get("secondary")]
    )
    if is_user_study and summary.get("template") != "user_study":
        errors.append(
            "study_type includes User Study but summary.template is not 'user_study'"
        )
    if not is_user_study and summary.get("template") == "user_study":
        errors.append(
            "summary.template is 'user_study' but study_type does not include User Study"
        )
    if summary.get("template") == "user_study":
        for field in [
            "task", "control", "participants", "results",
            "issues", "recommendations", "autonomous_capabilities",
        ]:
            if not summary.get(field, "").strip():
                errors.append(f"summary.{field} is empty but required for template 'user_study'")
    if summary.get("template") == "abstract_only" and not summary.get("abstract_summary", "").strip():
        errors.append("summary.abstract_summary is empty but required for template 'abstract_only'")

    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="+", help="JSON file(s) or a directory to validate")
    args = parser.parse_args()

    schema = load_schema()

    files: list[Path] = []
    for p in args.paths:
        path = Path(p)
        if path.is_dir():
            files.extend(sorted(path.glob("*.json")))
        else:
            files.append(path)
    files = [f for f in files if f.name != "index.json"]

    if not files:
        print("No files to validate.")
        sys.exit(0)

    any_failed = False
    for f in files:
        errors = validate_file(f, schema)
        if errors:
            any_failed = True
            print(f"FAIL  {f}")
            for e in errors:
                print(f"        - {e}")
        else:
            print(f"OK    {f}")

    sys.exit(1 if any_failed else 0)


if __name__ == "__main__":
    main()
