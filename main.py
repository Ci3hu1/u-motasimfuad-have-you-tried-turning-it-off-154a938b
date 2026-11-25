#!/usr/bin/env python3
"""Have You Tried Turning It Off? — make.fun entry.

Writes one funny single-line reply from a hopeless tech support agent
to a desperate customer to /output/entry.txt.

Output contract (per the bounty requirements): exactly one line of
UTF-8 text, 1-199 chars, not only whitespace. validate_line() enforces
that contract before anything is written, so a bad line fails loudly
here instead of shipping an invalid entry to the grader.

Pure Python standard library, deterministic: the same line every run.
"""

import os
import stat

LINE = (
    "Because you called back within 30 seconds, our system has marked "
    "your issue resolved. I'll close the ticket and email a survey. "
    "Please be brutally honest!"
)


def validate_line(line: str) -> str:
    """Enforce the bounty output contract: one non-blank line, 1-199 chars."""
    if not line or not line.strip():
        raise ValueError("entry line must not be blank")
    if "\n" in line or "\r" in line:
        raise ValueError("entry line must be a single line")
    if len(line) > 199:
        raise ValueError(f"entry line is {len(line)} chars, over the 199-char limit")
    return line


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    try:
        os.chmod(out_dir, 0o755)
    except OSError:
        pass
    line = validate_line(LINE)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(line)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
