#!/usr/bin/env python3
"""Two-Sentence Horror — a make.fun two-sentence entry."""
from pathlib import Path

ENTRY = "I set the nursery camera to record only motion, so it should have stayed silent all night. It sent me one clip: my daughter, asleep in her crib, while something under the bed whispered her name in my voice."

OUTPUT = Path("/output/entry.txt")


def write_entry() -> None:
    text = ENTRY.strip()
    assert text, "entry must not be blank"
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    write_entry()
