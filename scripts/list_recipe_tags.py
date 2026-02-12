#!/usr/bin/env python3
"""List unique tags from recipe front matter."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Iterable, List, Set

FRONT_MATTER_DELIM = "---"


def _strip_quotes(value: str) -> str:
    value = value.strip()
    if (value.startswith("\"") and value.endswith("\"")) or (
        value.startswith("'") and value.endswith("'")
    ):
        return value[1:-1].strip()
    return value


def _parse_inline_list(value: str) -> List[str]:
    inner = value.strip()[1:-1]
    if not inner.strip():
        return []
    parts = [p.strip() for p in inner.split(",")]
    return [_strip_quotes(p) for p in parts if p]


def _extract_tags_from_lines(lines: Iterable[str]) -> List[str]:
    tags: List[str] = []
    in_front_matter = False
    collecting_list = False

    for line in lines:
        stripped = line.strip()

        if not in_front_matter:
            if stripped == FRONT_MATTER_DELIM:
                in_front_matter = True
            continue

        if stripped == FRONT_MATTER_DELIM:
            break

        if collecting_list:
            if re.match(r"^\s*-\s+", line):
                tag_value = re.sub(r"^\s*-\s+", "", line).strip()
                if tag_value:
                    tags.append(_strip_quotes(tag_value))
                continue
            if stripped == "":
                continue
            if not line.startswith(" ") and not line.startswith("\t"):
                collecting_list = False

        if not collecting_list and stripped.startswith("tags:"):
            after = stripped.split(":", 1)[1].strip()
            if not after:
                collecting_list = True
                continue
            if after.startswith("[") and after.endswith("]"):
                tags.extend(_parse_inline_list(after))
            else:
                tags.append(_strip_quotes(after))

    return tags


def list_tags(content_dir: Path) -> List[str]:
    tags: Set[str] = set()
    for path in content_dir.rglob("*.md"):
        if "themes" in path.parts:
            continue
        try:
            lines = path.read_text(encoding="utf-8").splitlines()
        except OSError:
            continue
        for tag in _extract_tags_from_lines(lines):
            if tag:
                tags.add(tag)
    return sorted(tags)


def main() -> int:
    parser = argparse.ArgumentParser(description="List unique recipe tags.")
    parser.add_argument(
        "--content-dir",
        default="content",
        help="Content directory to scan (default: content)",
    )
    parser.add_argument(
        "--format",
        choices=["json", "lines"],
        default="json",
        help="Output format (default: json)",
    )
    args = parser.parse_args()

    tags = list_tags(Path(args.content_dir))

    if args.format == "lines":
        for tag in tags:
            print(tag)
    else:
        print(json.dumps(tags, indent=2))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
