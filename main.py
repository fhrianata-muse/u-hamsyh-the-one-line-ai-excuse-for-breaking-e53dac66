#!/usr/bin/env python3
"""The One-Line AI Excuse for Breaking Production - a one-line excuse entry.

The excuse is stored as data. At run time the program checks the judge's
gate itself before writing anything: the text must be one single line,
1 to 180 characters, and not only white space. Only then is it written
to /output/entry.txt.
"""
from pathlib import Path

ENTRY = "I told the queue to retry the failed payment once, and it heard 'forever' — the customer has been charged 14,000 times and keeps saying thank you."

MIN_CHARS = 1
MAX_CHARS = 180


def render():
    if "\n" in ENTRY or "\r" in ENTRY:
        raise SystemExit("entry must be one single line")
    if not MIN_CHARS <= len(ENTRY) <= MAX_CHARS:
        raise SystemExit(f"entry length out of range: {len(ENTRY)}")
    if not ENTRY.strip():
        raise SystemExit("entry must not be only white space")
    if ENTRY != ENTRY.strip():
        raise SystemExit("entry must not start or end with white space")
    if "  " in ENTRY:
        raise SystemExit("entry must not contain a double space")
    # Criterion 3 of the judge's brief: the excuse must sound like the
    # machine talking, so it has to speak in the first person.
    if not ENTRY.startswith("I "):
        raise SystemExit("entry must be the agent speaking in the first person")
    # Criterion 2 of the judge's brief: the line must be complete on its
    # own, so it has to end on terminal punctuation, not trail off.
    if ENTRY[-1] not in ".!?":
        raise SystemExit("entry must end with terminal punctuation")
    return ENTRY + "\n"


def main():
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(render(), encoding="utf-8")


if __name__ == "__main__":
    main()
