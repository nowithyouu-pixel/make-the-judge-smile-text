#!/usr/bin/env python3
"""Entry for make.fun's "Make the Judge Smile" bounty.

Writes one short text (167 Unicode characters) to /output/entry.txt.
No network, no input, deterministic.
"""

import os

TEXT = (
    "The lift broke this morning, so I took the stairs and found my "
    "neighbour's cat asleep on the third-floor landing, guarding one "
    "dropped strawberry like it was treasure."
)


def main() -> None:
    if not 1 <= len(TEXT) <= 200:
        raise ValueError(f"entry text must be 1-200 chars, got {len(TEXT)}")
    if not TEXT.strip():
        raise ValueError("entry text must not be whitespace-only")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
