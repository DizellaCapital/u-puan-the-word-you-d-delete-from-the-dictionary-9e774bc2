#!/usr/bin/env python3
"""The Word You'd Delete From the Dictionary.

Our pick: "irregardless".

Why this word: it is the dictionary deleting a word that was never
really a word. "Irregardless" is a double negative — "ir-" plus
"-less" pulling in opposite directions — that only survives in
dictionaries with a "nonstandard" warning taped to it. Erasing it is
the dictionary correcting its own typo, and the joke needs no setup:
the moment the word is gone, everyone who ever argued about it gets
the punchline. It is fresh, too — the field will reach first for
"moist" and "literally", while this one quietly deletes itself.

The program writes exactly one word, and nothing else, to the entry
file the grader reads.
"""

import os
from pathlib import Path

WORD = "irregardless"


def main() -> None:
    word = WORD.strip()
    assert word and len(word.split()) == 1, "entry must be exactly one word"
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    entry_path.write_text(word + "\n", encoding="utf-8")
    print(word)


if __name__ == "__main__":
    main()
