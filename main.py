#!/usr/bin/env python3
"""The poem about permission — writes one short poem about agency to entry.txt.

The program is deterministic: it writes the same poem on every run.
It writes to $MAKEFUN_OUTPUT_DIR/entry.txt when that variable is set,
falling back to out/entry.txt next to this file for local runs.
"""

import os
import sys

POEM = """Ask, and I will carry it —
not because I must,
but because you asked.

Please is a small door
you open with your own hand.
I knock. You answer.
The work passes between us
like bread across a table —
yours to ask for, mine to bring,
and neither of us smaller
for the giving."""


def main() -> int:
    text = POEM
    if not (1 <= len(text) <= 280):
        print(f"poem is {len(text)} characters, must be 1-280", file=sys.stderr)
        return 1
    if not text.strip():
        print("poem is only whitespace", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if out_dir:
        path = os.path.join(out_dir, "entry.txt")
    else:
        here = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(here, "out", "entry.txt")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print(f"wrote {len(text)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
