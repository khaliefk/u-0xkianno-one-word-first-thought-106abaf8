"""One Word, First Thought.

Writes exactly one word to entry.txt.
"""

import os
from pathlib import Path

WORD = "psithurism"


def main() -> None:
    out_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(WORD, encoding="utf-8")


if __name__ == "__main__":
    main()
