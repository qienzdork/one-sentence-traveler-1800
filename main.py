"""One Sentence for a Traveler from 1800.

Writes a single original sentence explaining the modern internet to a
time traveler from the year 1800, using only things such a traveler
already knows: roads, libraries, post offices, letters, ink.
"""

import os

SENTENCE = (
    "Imagine one invisible road joining every library, post office, "
    "and fireside chat on earth, so a letter written in London is "
    "read in China before the ink dries."
)


def main() -> None:
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(output_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as handle:
        handle.write(SENTENCE)


if __name__ == "__main__":
    main()
