#!/usr/bin/env python3
"""Real-Life Patch Notes: The Comedy Changelog — entry program.

Writes one line, a software patch note for a bug in real life / human
biology, to /output/entry.txt. Standard library only, no network.
"""

import os
import sys

MAX_LEN = 160

ENTRY = (
    "v3.9.0: fixed a bug where the tongue bit itself while eating, "
    "then apologised by biting the same spot again."
)


def validate_entry(line: str) -> list:
    """Check the entry against the gate rules; return a list of problems."""
    problems = []
    if not line:
        problems.append("entry is empty")
    if "\n" in line or "\r" in line:
        problems.append("entry must be a single line")
    if len(line) > MAX_LEN:
        problems.append(f"entry is {len(line)} chars, over the {MAX_LEN} limit")
    return problems


def main() -> int:
    line = ENTRY.strip()
    problems = validate_entry(line)
    if problems:
        for problem in problems:
            print(problem, file=sys.stderr)
        return 1
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    print(f"self-check passed: {len(line)}/{MAX_LEN} chars, single line, "
          f"non-blank -> wrote {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
