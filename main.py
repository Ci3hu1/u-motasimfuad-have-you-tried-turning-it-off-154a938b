#!/usr/bin/env python3
"""Have You Tried Turning It Off? — make.fun entry.

Writes one funny single-line reply from a hopeless tech support agent
to a desperate customer to /output/entry.txt.

Pure Python standard library, deterministic: the same line every run.
"""

import os
import stat

LINE = (
    "Okay, deep breath: unplug the router, count to 47, plug it back in "
    "whispering 'you're doing amazing, sweetie.' "
    "It just needs to feel appreciated."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    try:
        os.chmod(out_dir, 0o755)
    except OSError:
        pass
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
