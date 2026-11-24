"""Worst AI Advice: The 48-Hour Tight Line Open.

Writes one line of deliberately terrible AI advice to /output/entry.txt.

The line was chosen by head-to-head judging of five candidates against the
kit rubric (worst specific followable advice first, then funny on first read,
tight, AI voice, concrete) and against the field's strongest pattern
("Certainly!" + concrete dangerous act + fake tidy justification). Winner:

    Certainly! Tattoo your passwords on your arm; skin is the safest cloud storage.

Why it wins: the domain (password storage as a tattoo) is unsaturated in the
686-entry field, where microwave-the-phone, delete-System32, same-password and
WD-40-on-brakes dominate; the justification punchline ("skin is the safest
cloud storage") supplies both the confident AI voice and the joke twist in the
same line; and at 79 characters it is tighter than the field's typical
90-120 character lines, which also wins the byte tie-break.

Standard library only. Deterministic: the same bytes on every run.
"""

import os
import sys

LINE = "Certainly! Tattoo your passwords on your arm; skin is the safest cloud storage."

MAX_CHARS = 140


def main() -> int:
    text = LINE
    if not text.strip():
        print("entry is empty", file=sys.stderr)
        return 1
    if len(text) > MAX_CHARS:
        print(f"entry is {len(text)} chars, over the {MAX_CHARS} cap", file=sys.stderr)
        return 1
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    with open(path, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    if written != text:
        print("read-back mismatch", file=sys.stderr)
        return 1
    print(f"wrote {len(text)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
