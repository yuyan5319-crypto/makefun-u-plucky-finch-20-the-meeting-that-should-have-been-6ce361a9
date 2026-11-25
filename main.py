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

# The verdict and the response, kept as separate clauses: the first
# states the meeting's only decision, the second is what the meeting
# did about it. Joined with an em dash, the pivot the joke turns on.
VERDICT = "The meeting's only decision was unanimous: this should have been an email"
RESPONSE = "so we scheduled another meeting to write it."

LINE = VERDICT + " \u2014 " + RESPONSE


def validate_line(text):
    """One fixed line: 1-200 characters, no newline, no trailing space."""
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert "\n" not in text, "entry must be a single line"
    assert text == text.strip(), "entry must not have surrounding whitespace"


def main() -> None:
    text = LINE.strip()
    validate_line(text)
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
