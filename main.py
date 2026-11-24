#!/usr/bin/env python3
"""One Letter: Coffee or Tea.

Writes exactly one letter to /output/entry.txt: "A" for coffee.
No words, no explanation, no punctuation -- the letter alone is the entry.
"""

import os

LETTER = "A"  # A = coffee, B = tea
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # The entry must be exactly one letter, A for coffee or B for tea.
    assert LETTER in ("A", "B"), "entry letter must be A or B"
    assert len(LETTER) == 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LETTER)
    # Read back and verify: exactly one byte, the chosen letter, nothing else.
    with open(OUTPUT_PATH, "rb") as f:
        written = f.read()
    assert written == LETTER.encode("ascii"), "entry.txt must hold exactly one letter"


if __name__ == "__main__":
    main()
