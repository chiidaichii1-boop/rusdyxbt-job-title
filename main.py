#!/usr/bin/env python3
"""Entry for u-rusdyxbt-weirdest-job-title-blind-judge-showdown-552d7922.

Writes a single weird job title (at most 60 characters) to
/output/entry.txt. Stdlib only; no network, no randomness, no timestamps.
"""

import os

ENTRY = "Senior Vice President of Abandoned Shopping Carts"
# Verified: 49 characters, within the 1-60 gate.


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = ENTRY
    assert 1 <= len(text) <= 60, "entry must be 1-60 characters"
    assert text.strip(), "entry must not be only whitespace"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
