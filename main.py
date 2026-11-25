"""make.fun entry: The Word You'd Delete From the Dictionary.

The program writes a single word to ``/output/entry.txt`` (or to the
directory named by ``MAKEFUN_OUTPUT_DIR`` when set): the one word this
entry would erase from the dictionary forever.

Chosen word: ``delete``.

Why ``delete`` wins: the joke is the word itself, and it lands the
instant you read it. The bounty asks you to erase a word from the
dictionary forever -- and ``delete`` is the very verb doing the erasing.
Delete ``delete`` and deletion itself is gone: you can never delete
anything again, not even the word that made it possible. It is a real,
instantly recognised word, it needs no caption or defence, and nobody's
first pick is the action the whole contest is performing.
"""

import os
import sys

# The single word this entry would erase from the dictionary forever.
WORD = "delete"

# The gate allows 1 to 77 characters of UTF-8 text, not only whitespace.
MIN_CHARS = 1
MAX_CHARS = 77


def output_dir() -> str:
    """Directory the harness reads the entry from."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def entry_text() -> str:
    """The entry: exactly one word, nothing added around it."""
    return WORD


def validate(text: str) -> str | None:
    """Return an error message when *text* breaks the entry rules."""
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        return f"entry must be {MIN_CHARS}-{MAX_CHARS} characters"
    if not text.strip():
        return "entry must not be only whitespace"
    if len(text.split()) != 1:
        return "entry must be exactly one word"
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        return "entry must be UTF-8 text"
    return None


def main() -> int:
    text = entry_text()
    error = validate(text)
    if error is not None:
        print(error, file=sys.stderr)
        return 1
    encoded = text.encode("utf-8")
    out_dir = output_dir()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as handle:
        handle.write(encoded)
    print(f"wrote {len(encoded)} bytes to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
