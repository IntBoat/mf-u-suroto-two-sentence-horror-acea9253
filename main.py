#!/usr/bin/env python3
"""Two-Sentence Horror (make.fun).

Writes the entry -- a horror story in exactly two sentences, up to 400
characters -- to /output/entry.txt, where the sealed scorer reads it.
"""

import os

TEXT = 'I taught my house to lock its doors at the sound of my voice. Last night it locked them when my voice called from the garden — and I was already in bed.'


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
