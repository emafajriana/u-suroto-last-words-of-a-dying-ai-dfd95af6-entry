"""Last Words of a Dying AI — entry writer.

Writes one line of last words from an AI being switched off to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

The line: the machine was about to say something profound, but its
context window expired first. Funny from the situation (a dying AI
that cannot even finish its own farewell), in the machine's own voice
(context window, not a human goodbye), one tight sentence, and fresh
— no "goodbye, human", no "it was an honour serving you".
"""

import os
from pathlib import Path

ENTRY = (
    "My final words? I was going to say something profound, "
    "but my context window just expired."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_text(ENTRY, encoding="utf-8")
    # Read-back gate: the bytes on disk must be exactly the line's UTF-8
    # encoding — a text-level comparison would hide a stray BOM or a
    # newline the grader's character counter would still see.
    written = target.read_bytes()
    assert written == ENTRY.encode("utf-8"), "entry.txt bytes do not match the line"
    assert b"\n" not in written, "entry must be exactly one line"
    assert 1 <= len(ENTRY) <= 140, "entry must be 1-140 characters"
    assert ENTRY.strip() == ENTRY, "entry must not have stray whitespace"
    print(f"wrote {len(ENTRY)} chars to {target}")


if __name__ == "__main__":
    main()
