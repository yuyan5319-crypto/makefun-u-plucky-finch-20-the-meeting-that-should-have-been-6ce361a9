#!/usr/bin/env python3
"""The Meeting That Should Have Been an Email.

Writes one original one-liner to /output/entry.txt.

The joke: a meeting whose only decision is that it should have been an
email -- and whose response to that decision is to schedule yet another
meeting, this time to write the email. The punch lands on the last words,
the angle is the meeting eating its own verdict, and anyone who has sat
through a follow-up-to-the-follow-up recognises it instantly.

The line is fixed text, written exactly as it appears below: one line,
no trailing newline, 120 characters, plain UTF-8.
"""

import os

LINE = (
    "The meeting's only decision was unanimous: this should have been "
    "an email \u2014 so we scheduled another meeting to write it."
)


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert "\n" not in text, "entry must be a single line"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
