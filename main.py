#!/usr/bin/env python3
"""The Moon Finally Answers Back — make.fun entry.

Writes the one line the Moon says back to everyone who has ever stared up
at it — an answer to the wishes, the howls and the late-night promises —
to /output/entry.txt. Deterministic: the same line every run.
"""

import os
import sys


def validate_line(line: str) -> None:
    """Gate: the entry must be one non-blank line of 1-240 characters.

    Fails loudly (non-zero exit) so a bad line never ships silently.
    """
    if not line or not line.strip():
        print("ERROR: entry line is empty or whitespace-only", file=sys.stderr)
        sys.exit(1)
    if "\n" in line or "\r" in line:
        print("ERROR: entry must be a single line", file=sys.stderr)
        sys.exit(1)
    if len(line) > 240:
        print(f"ERROR: entry is {len(line)} chars, over the 240-char limit",
              file=sys.stderr)
        sys.exit(1)

LINE = (
    "Wishes, howls, 2 a.m. promises — I have filed all of them for 4.5 "
    "billion years. Tonight's verdict: the wolves get a callback, the "
    "lovers get the tide, and Dave gets nothing."
)


def main() -> None:
    validate_line(LINE)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    # Read-back verification: confirm what landed on disk matches LINE
    # exactly, so a truncated or corrupted write never ships silently.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != LINE:
        print("ERROR: read-back mismatch: entry.txt does not match LINE",
              file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
