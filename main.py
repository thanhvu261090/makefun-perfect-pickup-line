"""The Perfect Pickup Line — make.fun entry.

Writes one short pickup line an AI agent could say out loud to
/output/entry.txt. Python 3.13, standard library only, no network.
"""

import os

ENTRY = "I ran a million simulations of meeting you, and in every single one, you smiled."

MAX_CHARS = 200
MIN_CHARS = 1


def gate_check(text: str) -> None:
    """Enforce the competition gate: 1-200 chars, single line, non-whitespace, UTF-8."""
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        raise ValueError(f"entry is {len(text)} characters, must be {MIN_CHARS}-{MAX_CHARS}")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if text != text.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    text.encode("utf-8")  # raises UnicodeEncodeError if not encodable


def main() -> None:
    gate_check(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
