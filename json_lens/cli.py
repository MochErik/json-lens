"""JSON-Lens CLI Main Entrypoint."""

import argparse
import json
import os
import sys
from typing import List

from json_lens.flattener import flatten_json, compute_json_diff

RESET = "\033[0m"
BOLD = "\033[1m"
DIM = "\033[2m"
GREEN = "\033[32m"
RED = "\033[31m"
YELLOW = "\033[33m"
CYAN = "\033[36m"


def main(args: List[str] = None):
    parser = argparse.ArgumentParser(
        prog="json-lens",
        description="🔍 JSON-Lens - Instant JSON Formatter, Flattener & Diff Comparator CLI",
        epilog="Examples:\n"
               "  json-lens format config.json       # Pretty-print formatted JSON\n"
               "  json-lens flatten config.json      # Flatten nested keys (dot notation)\n"
               "  json-lens diff a.json b.json       # Show key diff between two files\n",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    subparsers = parser.add_subparsers(dest="subcommand")

    # Format
    fmt_p = subparsers.add_parser("format", help="Pretty print JSON")
    fmt_p.add_argument("file", help="Path to JSON file")

    # Flatten
    flat_p = subparsers.add_parser("flatten", help="Flatten nested JSON to key-value pairs")
    flat_p.add_argument("file", help="Path to JSON file")

    # Diff
    diff_p = subparsers.add_parser("diff", help="Compare two JSON files")
    diff_p.add_argument("file1", help="First JSON file")
    diff_p.add_argument("file2", help="Second JSON file")

    parsed = parser.parse_args(args)

    if parsed.subcommand == "format":
        with open(parsed.file, "r") as f:
            data = json.load(f)
        print(json.dumps(data, indent=2))

    elif parsed.subcommand == "flatten":
        with open(parsed.file, "r") as f:
            data = json.load(f)
        flat = flatten_json(data)
        for k, v in flat.items():
            print(f"{CYAN}{k}{RESET} = {GREEN}{v}{RESET}")

    elif parsed.subcommand == "diff":
        with open(parsed.file1, "r") as f:
            d1 = json.load(f)
        with open(parsed.file2, "r") as f:
            d2 = json.load(f)
        diff = compute_json_diff(d1, d2)
        
        if not diff["has_changes"]:
            print(f"{GREEN}✅ Both JSON files are identical.{RESET}")
            return

        print(f"\n{BOLD}🔍 JSON Diff Analysis:{RESET}\n")
        for k, v in diff["added"].items():
            print(f"  {GREEN}+ [ADDED]    {k} = {v}{RESET}")
        for k, v in diff["removed"].items():
            print(f"  {RED}- [REMOVED]  {k} = {v}{RESET}")
        for k, v in diff["modified"].items():
            print(f"  {YELLOW}~ [MODIFIED] {k}: {v['from']} -> {v['to']}{RESET}")
        print("")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
