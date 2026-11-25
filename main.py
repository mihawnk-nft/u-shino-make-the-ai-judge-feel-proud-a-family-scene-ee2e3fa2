#!/usr/bin/env python3
"""Make the AI Judge Feel Proud: A Family Scene — make.fun entry.

Writes one short family scene (two lines, under 280 characters) that is
warm, funny and heartfelt to /output/entry.txt. Pure Python stdlib,
no network.
"""

import os

# The scene: Dad still sets a place for Grandma every Sunday, as if
# heaven were just down the road — and Mum, who rolls her eyes at it,
# quietly puts out Grandma's favourite cup anyway. Warmth in the
# ritual, the wry line in Dad's excuse, and the heart in Mum doing
# it too without a word.
ENTRY = (
    "Every Sunday Dad sets an extra plate for Grandma \u2014 \u201cin case she "
    "drops by,\u201d he says, like heaven is just down the road.\n"
    "Mum rolls her eyes, then quietly puts out Grandma\u2019s favourite cup."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 280, f"entry length {len(text)} out of range"
    assert text.strip(), "entry must not be only whitespace"
    assert text.count("\n") <= 1, "entry must be one or two lines"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
