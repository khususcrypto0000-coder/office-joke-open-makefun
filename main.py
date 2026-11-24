#!/usr/bin/env python3
"""Office Joke Open — make.fun entry.

Writes a single one-line office joke to entry.txt.
Standard library only.
"""

import os
import sys

JOKE = "The icebreaker asked for one fun fact, so I said I enjoy my job — and now the whole team thinks I'm the fun fact."


def main():
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    text = JOKE
    # Gate: UTF-8 text, 1-200 characters, not only whitespace,
    # a single line, no trailing newline.
    assert 1 <= len(text) <= 200, "joke must be 1-200 chars, got %d" % len(text)
    assert "\n" not in text and "\r" not in text, "joke must be a single line"
    assert text.strip(), "joke must not be only whitespace"
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print("wrote %d chars to %s" % (len(text), path))
    return 0


if __name__ == "__main__":
    sys.exit(main())
