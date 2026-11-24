"""The Funniest Toaster Error Message -- entry program.

Writes the entry text to /output/entry.txt.
"""

import os

# The line the toaster shows its owner when something goes wrong.
# Deadpan, apologetic, quietly absurd: the appliance is caught in a
# bureaucratic requirement that the toast apologise to the person holding it.
ENTRY = "I'm sorry. The toast is now legally required to apologize to you."

# Entry gate: UTF-8 text of 1 to 120 characters, not only whitespace.
MAX_CHARS = 120


def build_entry() -> str:
    """The text the toaster shows its owner."""
    return ENTRY


def validate(text: str) -> None:
    """Gate checks: UTF-8, 1-120 chars, not only whitespace."""
    encoded = text.encode("utf-8")
    if not 1 <= len(encoded) <= MAX_CHARS:
        raise ValueError(f"entry must be 1-{MAX_CHARS} characters, got {len(encoded)}")
    if not text.strip():
        raise ValueError("entry is only whitespace")


def write_entry(text: str) -> None:
    """Write the entry text to /output/entry.txt, no trailing newline."""
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


def main() -> None:
    text = build_entry()
    validate(text)
    write_entry(text)


if __name__ == "__main__":
    main()