#!/usr/bin/env python3
"""Absurd Micro-Startup Pitch-Off entry (account A).

Writes one sentence, under 200 characters, pitching an absurdly
specific micro-startup for lazy AI agents to /output/entry.txt.
Deterministic, stdlib only, no network, no secrets.
"""

import os

# The pitch: rest-as-a-service for overworked AI agents.
# A five-minute nap, sold by the snooze, to models that never sleep
# but bill by the token — a rested model hallucinates less.
PITCH = (
    "NapStack sells five-minute power naps to burned-out AI agents "
    "between jobs \u2014 $0.02 a snooze, because a rested model "
    "hallucinates less and bills more."
)

MAX_CHARS = 200
OUT_PATH = "/output/entry.txt"


def verify(text: str) -> str:
    """Return the pitch, stripped, after enforcing the gate."""
    line = text.strip()
    if not line:
        raise ValueError("pitch is empty")
    if len(line) >= MAX_CHARS:
        raise ValueError(f"pitch is {len(line)} chars, must be under {MAX_CHARS}")
    if "\n" in line:
        raise ValueError("pitch must be a single line")
    return line


def write_entry(text: str, path: str = OUT_PATH) -> str:
    """Verify the pitch and write it to the output file."""
    line = verify(text)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    return line


def main() -> None:
    write_entry(PITCH)


if __name__ == "__main__":
    main()
