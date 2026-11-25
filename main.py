"""Roast Your Own Agent — one line, printed exactly as written.

The roast lives in entry.txt next to this file. This runner loads it,
checks it is a single plain-text line within the 140-character cap,
prints it to stdout, and — when the grader provides an output
directory — leaves a copy there as entry.txt too.
"""

import os
import sys


def load_roast() -> str:
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "entry.txt"), encoding="utf-8") as handle:
        text = handle.read()
    lines = [line for line in text.splitlines() if line.strip()]
    if len(lines) != 1:
        raise ValueError("entry.txt must hold exactly one non-empty line")
    return lines[0].strip()


def save_copy(line: str) -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        return
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(line + "\n")


def main() -> int:
    try:
        line = load_roast()
    except (OSError, ValueError) as exc:
        print(f"bad entry: {exc}", file=sys.stderr)
        return 1
    if len(line) > 140:
        print("entry exceeds 140 characters", file=sys.stderr)
        return 1
    print(line)
    save_copy(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
