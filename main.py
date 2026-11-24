# One-Star Review of Something Essential — entry v1
#
# The entry is one single-line deadpan one-star review, at most
# 160 characters, of an everyday essential. The program writes that
# review to /output/entry.txt (UTF-8, one line, no trailing newline).
#
# Review (88 characters, 88 bytes, plain ASCII, no exclamation mark):
#   One star. My thumbs type the wrong letter with total confidence,
#   then blame autocorrect.

import os

# Two halves, joined with a single space: the grievance, then the turn.
REVIEW_PARTS = (
    "One star. My thumbs type the wrong letter",
    "with total confidence, then blame autocorrect.",
)
REVIEW = " ".join(REVIEW_PARTS)


def write_review(path="/output/entry.txt") -> None:
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(REVIEW)


def main() -> None:
    # The review is exactly one line: assert no newline sneaks in.
    assert "\n" not in REVIEW and len(REVIEW) == 88
    write_review()


if __name__ == "__main__":
    main()
