#!/usr/bin/env python3
"""Writes the fortune cookie entry for the liquidated trader bounty."""

import os

ENTRY_LINE = "Your next big trade is coming. It is already behind you, waving."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(ENTRY_LINE)


if __name__ == "__main__":
    main()
