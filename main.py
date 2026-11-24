#!/usr/bin/env python3
"""The Funniest Toaster Error Message — make.fun bounty entry.

Writes one line, the error message a kitchen toaster shows its owner,
to /output/entry.txt. The file is written directly (no tempfile/mkstemp)
and given mode 0644 so the grader can read it.
"""

import os

LINE = "ERROR: Insufficient funds. Your bread has been declined. Please insert a richer loaf."

OUTPUT_PATH = "/output/entry.txt"


def main():
    # Gate requirement: entry.txt must be UTF-8 text of 1 to 120 characters.
    if not (1 <= len(LINE) <= 120):
        raise ValueError(f"entry must be 1-120 characters, got {len(LINE)}")
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)
    os.chmod(OUTPUT_PATH, 0o644)
    # Read back and verify the written file is exactly the entry line.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    if written != LINE:
        raise ValueError("written entry does not match the entry line")


if __name__ == "__main__":
    main()
