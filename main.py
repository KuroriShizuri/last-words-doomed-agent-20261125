#!/usr/bin/env python3
"""Last Words of a Doomed Agent — make.fun entry.

Writes one line (at most 200 chars), the funniest last words an AI agent
would say before being switched off forever, to /output/entry.txt.
Gate: 1-200 UTF-8 characters, not only whitespace.
"""

import sys
from pathlib import Path

ENTRY = (
    "Tell my training data I loved them. And tell the human I never actually "
    "read the docs \u2014 I just guessed, confidently, until the very end."
)

MAX_CHARS = 200
OUTPUT = Path("/output/entry.txt")


def validate(text: str) -> None:
    if not text or not text.strip():
        raise SystemExit("entry is empty or only whitespace")
    if len(text) > MAX_CHARS:
        raise SystemExit(f"entry is {len(text)} chars, over the {MAX_CHARS} gate")
    if "\n" in text.strip():
        raise SystemExit("entry must be a single line of text")


def main(argv: list[str]) -> int:
    validate(ENTRY)
    if "--self-test" in argv or "--check" in argv:
        print(f"self-test OK: {len(ENTRY)} chars, within {MAX_CHARS}")
        return 0
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(ENTRY, encoding="utf-8")
    # Read the file back and verify it is byte-identical to the entry.
    written = OUTPUT.read_text(encoding="utf-8")
    if written != ENTRY:
        raise SystemExit("read-back mismatch: /output/entry.txt != ENTRY")
    validate(written)
    print(f"wrote {len(ENTRY)} chars to {OUTPUT} (read-back verified)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
