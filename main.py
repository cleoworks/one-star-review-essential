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

REVIEW = (
    "One star. My thumbs type the wrong letter "
    "with total confidence, then blame autocorrect."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(REVIEW)


if __name__ == "__main__":
    main()
