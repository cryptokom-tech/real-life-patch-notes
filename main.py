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


def main() -> int:
    line = ENTRY.strip()
    if not line:
        print("entry is empty", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("entry must be a single line", file=sys.stderr)
        return 1
    if len(line) > MAX_LEN:
        print(f"entry is {len(line)} chars, over the {MAX_LEN} limit",
              file=sys.stderr)
        return 1
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    print(f"wrote {len(line)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
