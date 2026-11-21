#!/usr/bin/env python3
"""Make the AI judge feel awe (make-the-ai-judge-feel-awe-20261121-1600).

Writes one short text to $MAKEFUN_OUTPUT_DIR/entry.txt (default
/output). The text is a small, original scene written to slow its
reader down: the tide coming in whether or not anyone is watching,
smoothing the sand, erasing the footprints, leaving the beach new
again. Nothing to fix, nothing to hold -- only slow water, doing
its work.

Python 3.13, standard library only, no network. The output is a
fixed string, so both grader runs write identical bytes.
"""

import os
from pathlib import Path

TEXT = (
    "The tide comes in whether or not anyone is watching. "
    "It smooths the sand, erases the footprints, and leaves "
    "the beach new again. Nothing to fix. Nothing to hold. "
    "Only slow water, doing its work."
)


def main() -> int:
    """Write the text to the output directory. Returns exit code."""
    assert 1 <= len(TEXT) <= 280, "entry must be 1-280 characters"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(TEXT, encoding="utf-8")
    print(f"wrote {target} ({len(TEXT)} characters)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
